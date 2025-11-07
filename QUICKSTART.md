# Quick Start Guide

Get your AI-Powered News Newsletter running in 5 minutes!

## Step 1: Install Python Packages (1 minute)

Open PowerShell in this directory and run:

```powershell
pip install -r requirements.txt
```

## Step 2: Get Your API Keys (2 minutes)

### NewsAPI (Free)
1. Go to: https://newsapi.org/register
2. Sign up with your email
3. Copy the API key shown

### OpenAI (Paid - but cheap)
1. Go to: https://platform.openai.com/signup
2. Create account and add $5-10 in credits
3. Go to: https://platform.openai.com/api-keys
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)

### Gmail App Password (Free)
1. Enable 2-factor auth: https://myaccount.google.com/security
2. Create app password: https://myaccount.google.com/apppasswords
3. Select "Mail" and your device
4. Copy the 16-character password

## Step 3: Create .env File (1 minute)

1. Copy `config.env.example` to a new file named `.env`
2. Open `.env` in Notepad
3. Replace the placeholder values:

```env
NEWSAPI_KEY=paste_your_newsapi_key_here
OPENAI_API_KEY=paste_your_openai_key_here
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=paste_16char_app_password_here
EMAIL_RECIPIENTS=your_email@gmail.com
NEWS_TOPICS=technology,AI,data science
MAX_ARTICLES=3
```

**Important**: Use your own email as a recipient for testing!

## Step 4: Test Everything (1 minute)

```powershell
python test_components.py
```

When prompted to send test email, type `yes`.

✓ If all tests pass, you're ready!  
✗ If any fail, check the error messages.

## Step 5: Generate Your First Newsletter!

```powershell
python newsletter_generator.py
```

Watch the magic happen:
1. Fetches latest news articles
2. AI summarizes each one
3. Sends beautiful email newsletter

Check your inbox! 📧

## Common First-Time Issues

### "No module named 'requests'"
Run: `pip install -r requirements.txt`

### "NEWSAPI_KEY not found"
Make sure your file is named exactly `.env` (not `.env.txt`)

### "SMTP Authentication failed"
- Use App Password, not your regular Gmail password
- Make sure 2-factor auth is enabled on your Google account

### "Insufficient credits" (OpenAI)
Add credits at: https://platform.openai.com/account/billing

## Costs

- **NewsAPI**: FREE (100 requests/day)
- **OpenAI**: ~$0.002 per article summary (~$0.01 per newsletter)
- **Email**: FREE

Running daily = ~$0.30/month 💰

## Next Steps

1. Customize topics in `.env` file
2. Add more recipients
3. Set up automation (see README.md)
4. Prepare for your demonstration!

## Need Help?

- Check the full README.md
- Run individual module tests (see README)
- Review error messages carefully
- Make sure all API keys are correct

---

**You're all set! 🚀**

