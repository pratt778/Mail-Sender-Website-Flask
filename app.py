import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask.cli import load_dotenv
import google.generativeai as genai
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

load_dotenv()


app = Flask(__name__)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
PASSWORD = os.getenv('PASSWORD')

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def generate_personalized_email(company_name, gemini_api_key):
    """Generate personalized email using Gemini API"""
    try:
        genai.configure(api_key=gemini_api_key)

        print("Available Model")
        for m in genai.list_models():
            print(m.name)
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        prompt = f"""Write a job application email for a Flutter Developer position at {company_name}.

Requirements:
- Maximum 180 words
- Conversational and genuine tone
- Mention 1 year Flutter experience
- One sentence about why {company_name} specifically interests you
- Mention attached CV
- Simple closing
- Sign off with "Pratham Sharma"

Structure:
1. Opening: State the position you're applying for
2. Experience: Brief mention of 1 year Flutter experience and skill alignment
3. Interest: Few genuine sentences about the company
4. CV mention and simple call to action
5. Sign off

Write ONLY the email body. No subject line. No brackets or placeholders.
Keep sentences short and direct. Avoid flowery language like "express strong interest" or "thrilled to discuss."""

        response = model.generate_content(prompt)
        return True, response.text.strip()

    except Exception as e:
        return False, str(e)


def send_email(
    sender_email, sender_password, recipient_email, subject, body, attachment_path=None
):
    """Send email using Gmail SMTP"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Add body
        msg.attach(MIMEText(body, "plain"))

        # Add attachment if provided
        if attachment_path and os.path.exists(attachment_path):
            filename = os.path.basename(attachment_path)
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition", f"attachment; filename={filename}"
                )
                msg.attach(part)

        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        return True, "Email sent successfully"

    except Exception as e:
        return False, str(e)


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/generate-email", methods=["POST"])
def generate_email_endpoint():
    """Generate personalized email using Gemini API"""
    try:
        data = request.json
        company_name = data.get("company_name")
        # gemini_api_key = data.get("gemini_api_key")

        if not company_name:
            return (
                jsonify({"success": False, "error": "Missing company name or API key"}),
                400,
            )

        success, email_body = generate_personalized_email(company_name)

        if success:
            return jsonify({"success": True, "email_body": email_body})
        else:
            return jsonify({"success": False, "error": email_body}), 500

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/send-email", methods=["POST"])
def send_email_endpoint():
    try:
        data = request.form
        sender_email = data.get("sender_email")
        # sender_password = data.get("sender_password")
        recipient_email = data.get("recipient_email")
        company_name = data.get("company_name")
        # gemini_api_key = data.get("gemini_api_key")

        # Validate required fields
        if not all(
            [
                sender_email,
                # sender_password,
                recipient_email,
                company_name,
                # gemini_api_key,
            ]
        ):
            return jsonify({"success": False, "error": "Missing required fields"}), 400

        # Generate personalized email body
        success, email_body = generate_personalized_email(company_name, GEMINI_API_KEY)
        if not success:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": f"Failed to generate email: {email_body}",
                    }
                ),
                500,
            )

        # Generate subject
        subject = f"Application for Flutter Developer Position at {company_name}"

        # Handle file attachment
        attachment_path = None
        if "attachment" in request.files:
            file = request.files["attachment"]
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                attachment_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(attachment_path)

        # Send email
        success, message = send_email(
            sender_email,
            PASSWORD,
            recipient_email,
            subject,
            email_body,
            attachment_path,
        )

        # Clean up attachment file
        if attachment_path and os.path.exists(attachment_path):
            os.remove(attachment_path)

        if success:
            return jsonify(
                {"success": True, "message": message, "email_body": email_body}
            )
        else:
            return jsonify({"success": False, "error": message}), 500

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    print("=" * 60)
    print("EMAIL SENDER SERVER STARTED")
    print("=" * 60)
    print("Server running at: http://localhost:5000")
    print("Make sure to:")
    print("1. Enable 'Less secure app access' in your Gmail account")
    print("   OR")
    print("2. Generate an 'App Password' for Gmail (Recommended)")
    print("=" * 60)
    app.run(debug=True, port=5000)
