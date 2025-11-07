# Troubleshooting Guide

Common issues and their solutions.

## 🔴 Environment & Setup Issues

### "No module named 'requests'" / "No module named 'openai'"

**Problem**: Required packages not installed

**Solution**:
```bash
pip install -r requirements.txt
```

If that doesn't work, try:
```bash
python -m pip install requests openai python-dotenv
```

---

### "NEWSAPI_KEY not found" / "Environment variable not found"

**Problem**: .env file not properly configured

**Solutions**:

1. **Check file name**: Must be exactly `.env` (not `.env.txt` or `env` or `config.env`)
   
2. **Check file location**: Must be in the same directory as your Python files

3. **Check file format**: Should look like:
   ```env
   NEWSAPI_KEY=your_key_here
   OPENAI_API_KEY=sk-your_key_here
   ```
   (No quotes, no spaces around `=`)

4. **Windows hidden extensions**: 
   - Open File Explorer
   - View → Show → File name extensions
   - Make sure file is `.env` not `.env.txt`

---

## 🔴 NewsAPI Issues

### "No articles returned" / "Articles list is empty"

**Possible Causes & Solutions**:

1. **API Quota Exceeded**
   - Free tier: 100 requests/day
   - Check: https://newsapi.org/account
   - Solution: Wait 24 hours or upgrade

2. **Invalid API Key**
   - Verify key at: https://newsapi.org/account
   - Copy-paste carefully (no extra spaces)

3. **Topic too specific**
   - Try broader terms: "technology" instead of "quantum computing blockchain"
   - Use single words or short phrases

4. **Country/Language mismatch**
   - Not all topics available in all countries
   - Try: `NEWS_COUNTRY=us` and `NEWS_LANGUAGE=en`

---

### "HTTP Error 401: Unauthorized"

**Problem**: Invalid API key

**Solution**:
1. Go to https://newsapi.org/account
2. Copy your API key
3. Replace in .env file: `NEWSAPI_KEY=paste_here`
4. Make sure no extra spaces

---

### "HTTP Error 429: Too Many Requests"

**Problem**: Exceeded API rate limit

**Solution**:
- Free tier: 100 requests/day
- Each topic = 1 request
- If `MAX_ARTICLES=5` and 3 topics, that's still only 3 requests
- Wait 24 hours or upgrade account

---

## 🔴 OpenAI API Issues

### "Incorrect API key provided"

**Problem**: Invalid OpenAI key

**Solution**:
1. Go to: https://platform.openai.com/api-keys
2. Create a new key (starts with `sk-`)
3. Copy the ENTIRE key (it's long!)
4. Paste in .env: `OPENAI_API_KEY=sk-your_full_key_here`

---

### "You exceeded your current quota"

**Problem**: No credits in OpenAI account

**Solution**:
1. Go to: https://platform.openai.com/account/billing
2. Add credits ($5-10 is plenty)
3. Wait a few minutes for credits to activate

---

### "The model 'gpt-3.5-turbo' does not exist"

**Problem**: Model name changed or deprecated

**Solution**:
1. Check current models: https://platform.openai.com/docs/models
2. If needed, edit `ai_summarizer.py` line ~18:
   ```python
   def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
   ```
   Change to the current model name

---

## 🔴 Email Issues

### "SMTP Authentication Failed" (Most Common!)

**Problem**: Using regular password instead of app password

**Solution - For Gmail**:

1. **Enable 2-Factor Authentication**:
   - Go to: https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Generate App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" and your device
   - Copy the 16-character password (no spaces)
   - Paste in .env: `EMAIL_PASSWORD=your_16_char_password`

**Important**: Use the APP PASSWORD, not your regular Gmail password!

---

### "SMTPAuthenticationError: Username and Password not accepted"

**Solutions**:

1. **For Gmail**: Must use App Password (see above)

2. **For Other Emails**: 
   - Check if SMTP is enabled
   - Verify username is full email
   - Some providers need specific SMTP settings

3. **Edit email_sender.py** if using non-Gmail:
   ```python
   # For Outlook/Hotmail
   EmailSender(email, password, "smtp.office365.com", 587)
   
   # For Yahoo
   EmailSender(email, password, "smtp.mail.yahoo.com", 587)
   ```

---

### "Connection refused" / "Connection timed out"

**Possible Causes**:

1. **Firewall blocking SMTP**
   - Try different network
   - Check firewall settings
   - Port 587 must be open

2. **Wrong SMTP server**
   - Gmail: `smtp.gmail.com:587`
   - Verify your provider's SMTP settings

---

### "Email not received" (but no errors)

**Check**:

1. **Spam folder** - Check spam/junk
2. **Recipient email** - Verify correct address in .env
3. **Email formatting** - Check sent folder in Gmail
4. **Delivery delay** - Wait a few minutes

---

## 🔴 General Python Issues

### "Python is not recognized as a command"

**Problem**: Python not in PATH

**Solutions**:

**Option 1**: Use full path
```bash
C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe newsletter_generator.py
```

**Option 2**: Reinstall Python
- Download from: https://www.python.org/downloads/
- ✓ Check "Add Python to PATH" during installation

---

### "Permission denied"

**Problem**: File permissions or admin rights

**Solution**:
- Run PowerShell as Administrator
- OR check file isn't open in another program
- OR check antivirus isn't blocking

---

## 🔴 Runtime Errors

### "KeyError: 'title'" or "KeyError: 'description'"

**Problem**: Article missing expected fields

**Solution**: This is handled in the code with `.get()` methods, but if you see this:
1. Check which article is causing it
2. NewsAPI sometimes returns incomplete articles
3. The code should handle this - check you're using `.get('key', 'default')` not `['key']`

---

### "JSONDecodeError"

**Problem**: Invalid response from API

**Solutions**:
1. Check internet connection
2. API might be down - check status pages
3. API key might be invalid

---

### "ImportError: cannot import name 'OpenAI'"

**Problem**: Wrong version of openai package

**Solution**:
```bash
pip install --upgrade openai
```

Current code uses openai >= 1.0.0

---

## 🔴 Configuration Issues

### Newsletter shows "No summary available"

**Possible Causes**:

1. **OpenAI API failed** - Check console for errors
2. **No content in article** - NewsAPI free tier has limited content
3. **Rate limit hit** - Too many requests too fast

**Solution**: Check console output for specific error

---

### HTML email looks broken

**Possible Causes**:

1. **Email client doesn't support HTML** - Use web version
2. **Missing style tags** - Check `email_sender.py`

**Test**: Open `test_newsletter.html` in browser after running `test_components.py`

---

## 🛠️ Debugging Steps

### Step 1: Test Components Individually

```bash
python test_components.py
```

This will tell you exactly which component is failing.

---

### Step 2: Test Each Module

```bash
# Test news fetching
python news_fetcher.py

# Test AI summarization  
python ai_summarizer.py

# Test email sending
python email_sender.py
```

---

### Step 3: Check Environment Variables

```python
# Create a file check_env.py:
import os
from dotenv import load_dotenv

load_dotenv()

print("NEWSAPI_KEY:", "✓ Set" if os.getenv('NEWSAPI_KEY') else "✗ Missing")
print("OPENAI_API_KEY:", "✓ Set" if os.getenv('OPENAI_API_KEY') else "✗ Missing")
print("EMAIL_SENDER:", os.getenv('EMAIL_SENDER'))
```

```bash
python check_env.py
```

---

### Step 4: Enable Detailed Error Messages

The code already has try-except blocks. Look for error messages in console output.

---

### Step 5: Check API Status

- NewsAPI: https://newsapi.org/
- OpenAI: https://status.openai.com/
- Gmail: https://www.google.com/appsstatus

---

## 💡 Tips for Successful Troubleshooting

1. **Read error messages carefully** - They usually tell you what's wrong
2. **Test one thing at a time** - Use individual module tests
3. **Check API quotas** - Many issues are quota-related
4. **Verify API keys** - Copy-paste carefully, no extra spaces
5. **Use test_components.py** - It's designed to help debug
6. **Check .env file** - Most issues are configuration-related

---

## 📞 Still Having Issues?

### For Demonstration Purposes

If you can't get something working before your demo:

1. **Document the error** - Show you understand what's wrong
2. **Explain your debugging** - Show the steps you took
3. **Use test scripts** - Demonstrate what DOES work
4. **Have screenshots** - Show previous successful runs

Remember: You can earn partial credit by explaining errors and showing debugging efforts!

---

## ✅ Pre-Demo Checklist

Before your demonstration, verify:

- [ ] `python test_components.py` passes all tests
- [ ] You can run each module individually
- [ ] `.env` file has all required values
- [ ] You've received at least one test newsletter
- [ ] You understand each error message you've encountered
- [ ] You can explain the code in each module

---

**Most issues are simple configuration problems. Take your time, read error messages, and test components individually!**

