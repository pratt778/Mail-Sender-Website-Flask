# AI-Powered Job Application Sender 🤖✨

Send personalized job applications to multiple companies with **AI-generated emails** tailored for each company!

## 🎯 Features

- ✅ **AI-Generated Emails**: Gemini AI writes unique, personalized emails for each company
- ✅ **Company-Specific**: Each email mentions the specific company name
- ✅ **FREE**: Uses free Gmail SMTP + free Gemini API
- ✅ **Individual Sending**: Each recruiter gets their own email (no CC/BCC)
- ✅ **CV Attachments**: Attach your resume (PDF, DOC, DOCX)
- ✅ **Unlimited**: Send to as many companies as you want
- ✅ **Professional**: AI writes concise, professional emails highlighting your 1 year Flutter experience

## 🚀 Quick Setup (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get Gmail App Password
1. Go to https://myaccount.google.com/apppasswords
2. Sign in with your Gmail (pratham98861@gmail.com)
3. Select "Mail" → "Other (Custom name)"
4. Click "Generate"
5. Copy the 16-character password

### Step 3: Get Gemini API Key (FREE!)
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with Google
3. Click "Get API Key" or "Create API Key"
4. Copy the API key
5. **That's it! It's completely FREE!**

### Step 4: Start the Server
```bash
python app.py
```

### Step 5: Open Website
Open your browser and go to: `http://localhost:5000`

### Step 6: Send AI-Powered Applications!
1. Enter your Gmail and App Password
2. Enter your Gemini API Key
3. Add companies and recruiter emails:
   - Company Name: e.g., "Google"
   - Recruiter Email: e.g., "hiring@google.com"
4. Attach your CV
5. Click "Generate AI Emails & Send to All"

## 🤖 How the AI Works

For each company, Gemini AI generates a **unique, personalized email** that:
- Mentions the specific company name
- Highlights your 1 year Flutter experience
- Explains how your skills align with their requirements
- Expresses genuine interest in that specific company
- Mentions CV is attached
- Keeps it professional yet friendly (150-200 words)

### Example AI-Generated Emails:

**For Google:**
```
Dear Hiring Manager,

I am excited to apply for the Flutter Developer position at Google. With one year of 
hands-on Flutter development experience, I have built robust cross-platform applications 
that prioritize performance and user experience.

My expertise in Dart, state management, and creating responsive UIs aligns perfectly with 
Google's requirements for this role. I am particularly drawn to Google's innovative 
approach to mobile development and would love to contribute to your team's success.

Please find my CV attached for your review. I would welcome the opportunity to discuss 
how my Flutter skills can add value to Google's projects.

Best regards
```

**For Microsoft:**
```
Dear Hiring Manager,

I am writing to express my strong interest in the Flutter Developer position at Microsoft. 
My one year of Flutter development experience has equipped me with deep expertise in 
building performant, cross-platform mobile applications.

Microsoft's commitment to innovation resonates with my professional values, and I believe 
my skills in Dart programming, state management solutions, and UI development align well 
with your requirements.

I have attached my CV which details my Flutter projects and technical capabilities. I 
look forward to potentially discussing how I can contribute to Microsoft's mobile 
development initiatives.

Best regards
```

**Each email is UNIQUE and personalized!**

## 📁 Project Structure

```
email-sender/
├── app.py              # Flask backend with Gemini AI integration
├── index.html          # Beautiful frontend with company fields
├── requirements.txt    # Python dependencies
├── uploads/           # Temp folder for attachments (auto-created)
└── README.md          # This file
```

## 🔒 Security & Privacy

- **App Passwords**: Limited to email only (can't access other Google services)
- **Gemini API**: Only generates text, doesn't store your data
- **Attachments**: Saved temporarily, deleted immediately after sending
- **No Data Storage**: Nothing is saved permanently

## 💡 Why This is Better

### vs Traditional Job Applications:
- ❌ Generic template emails
- ❌ Same email to everyone
- ❌ Impersonal and robotic
- ❌ Takes hours to customize

### vs Our AI Solution:
- ✅ Unique email for each company
- ✅ Mentions company name specifically
- ✅ Professional and personalized
- ✅ Takes 5 minutes for 50 companies!

## 🎓 Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Email**: Gmail SMTP (smtp.gmail.com:587)
- **AI**: Google Gemini Pro API
- **Attachments**: MIME multipart messages

## 🐛 Troubleshooting

### "Invalid Gemini API Key"
- Make sure you copied the entire API key
- Check you created it at https://makersuite.google.com/app/apikey
- Gemini API is FREE but has rate limits (60 requests/minute)

### "Gmail authentication failed"
- Use App Password, not regular Gmail password
- Generate new App Password if needed

### "Server not running"
- Make sure you ran `python app.py`
- Check port 5000 is not in use

### "Too many requests"
- Gemini free tier: 60 requests/minute
- Add a small delay if sending to 50+ companies
- Or get a paid API key for higher limits

## 📊 Gemini API Limits (Free Tier)

- **Requests**: 60 per minute
- **Tokens**: 32,000 per request
- **Cost**: FREE! 
- **Perfect for**: Job applications (uses ~500 tokens per email)

## 🎉 Success Tips

1. **Company Names**: Be specific (e.g., "Google" not "google.com")
2. **Recruiter Emails**: Use real recruiter emails (check LinkedIn)
3. **CV File**: Keep under 10MB, PDF preferred
4. **Timing**: Send during business hours (9 AM - 5 PM)
5. **Check Spam**: First time, your emails might go to spam (Gmail warming up)

## 🔄 How It Works Behind the Scenes

1. **You enter**: Company name + Recruiter email
2. **AI generates**: Unique email mentioning that company specifically
3. **Flask backend**: Sends email via Gmail SMTP
4. **Recruiter receives**: Personalized email with your CV
5. **Repeat**: For each company individually

## 🌟 Example Usage

```python
# What happens when you click "Send":

For "Google" (hiring@google.com):
→ AI generates email mentioning Google
→ Email sent individually to hiring@google.com

For "Microsoft" (jobs@microsoft.com):
→ AI generates NEW email mentioning Microsoft  
→ Email sent individually to jobs@microsoft.com

For "Amazon" (recruiting@amazon.com):
→ AI generates ANOTHER NEW email mentioning Amazon
→ Email sent individually to recruiting@amazon.com

Each recruiter gets a UNIQUE, PERSONALIZED email! 🎯
```

## 💰 Costs

- **Gmail SMTP**: FREE (500 emails/day limit)
- **Gemini API**: FREE (60 requests/minute)
- **Total Cost**: $0.00 💸

## 🚀 Future Enhancements (Ideas)

- [ ] Save successful company responses
- [ ] Email tracking (know when opened)
- [ ] Multiple CV versions for different roles
- [ ] Interview scheduling integration
- [ ] Response rate analytics

## 📞 Support

If you encounter issues:
1. Check all API keys are correct
2. Make sure Flask server is running
3. Verify internet connection
4. Check console logs for detailed errors

---

**Built with ❤️ for job seekers who want to work smarter, not harder!**

Enjoy sending unlimited personalized job applications! 🎉
