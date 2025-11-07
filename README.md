# AI-Powered News Newsletter Generator

An automated system that fetches the latest news articles, summarizes them using AI, and delivers personalized newsletters via email.

## 📋 Project Overview

This application automates the process of keeping users informed about the latest news by:
1. **Fetching News**: Retrieving articles from NewsAPI based on configured topics
2. **AI Summarization**: Using OpenAI's GPT model to create concise summaries
3. **Email Delivery**: Formatting and sending beautiful HTML newsletters via SMTP

## 🏗️ Project Structure

```
QA3/
├── newsletter_generator.py    # Main application - integrates all components
├── news_fetcher.py            # Fetches news from NewsAPI
├── ai_summarizer.py           # Summarizes articles using OpenAI
├── email_sender.py            # Formats and sends emails
├── test_components.py         # Test each component individually
├── requirements.txt           # Python dependencies
├── config.env.example         # Example environment configuration
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- API keys for:
  - [NewsAPI](https://newsapi.org/) - Free tier available
  - [OpenAI](https://platform.openai.com/) - Requires paid account
- Email account with app password (Gmail recommended)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `requests` - For API calls
- `openai` - For AI summarization
- `python-dotenv` - For environment variable management

### Step 2: Set Up API Keys

1. **Get NewsAPI Key**:
   - Go to https://newsapi.org/
   - Sign up for a free account
   - Copy your API key

2. **Get OpenAI API Key**:
   - Go to https://platform.openai.com/
   - Create an account and add billing
   - Navigate to API Keys section
   - Create a new API key

3. **Set Up Email**:
   - For Gmail: Enable 2-factor authentication
   - Generate an App Password: https://myaccount.google.com/apppasswords
   - Use this app password (not your regular password)

### Step 3: Configure Environment Variables

1. Copy the example configuration:
   ```bash
   copy config.env.example .env
   ```

2. Edit `.env` file with your actual values:
   ```env
   # API Keys
   NEWSAPI_KEY=your_actual_newsapi_key_here
   OPENAI_API_KEY=sk-your_actual_openai_key_here
   
   # Email Configuration
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password_here
   EMAIL_RECIPIENTS=recipient1@example.com,recipient2@example.com
   
   # News Configuration (customize as needed)
   NEWS_TOPICS=technology,artificial intelligence,data science
   NEWS_LANGUAGE=en
   NEWS_COUNTRY=us
   MAX_ARTICLES=5
   ```

### Step 4: Test Components

Before running the full application, test each component individually:

```bash
python test_components.py
```

This will:
- ✓ Verify environment variables are set
- ✓ Test NewsAPI connection
- ✓ Test OpenAI API connection
- ✓ Generate sample HTML newsletter
- ✓ Optionally send a test email

### Step 5: Run the Newsletter Generator

Once all tests pass, run the main application:

```bash
python newsletter_generator.py
```

The application will:
1. Fetch latest articles for your configured topics
2. Summarize each article using AI
3. Format them into a beautiful HTML newsletter
4. Send the newsletter to your configured recipients

## 🧪 Testing Individual Components

Each module can be tested independently:

### Test News Fetcher
```bash
python news_fetcher.py
```

### Test AI Summarizer
```bash
python ai_summarizer.py
```

### Test Email Sender
```bash
python email_sender.py
```

## ⚙️ Configuration Options

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `NEWSAPI_KEY` | Your NewsAPI key | - | ✓ |
| `OPENAI_API_KEY` | Your OpenAI API key | - | ✓ |
| `EMAIL_SENDER` | Sender email address | - | ✓ |
| `EMAIL_PASSWORD` | Email app password | - | ✓ |
| `EMAIL_RECIPIENTS` | Comma-separated recipient emails | - | ✓ |
| `NEWS_TOPICS` | Comma-separated topics to fetch | `technology` | ✗ |
| `NEWS_LANGUAGE` | Language code (e.g., en, es) | `en` | ✗ |
| `NEWS_COUNTRY` | Country code (e.g., us, uk) | `us` | ✗ |
| `MAX_ARTICLES` | Maximum articles per topic | `5` | ✗ |

## 🤖 Automating the Newsletter

### Windows (Task Scheduler)

1. Open Task Scheduler
2. Click "Create Basic Task"
3. Name it "AI News Newsletter"
4. Set trigger (e.g., Daily at 8:00 AM)
5. Action: "Start a program"
6. Program: `python`
7. Arguments: `C:\path\to\newsletter_generator.py`
8. Start in: `C:\path\to\QA3`

### macOS/Linux (Cron)

1. Edit crontab:
   ```bash
   crontab -e
   ```

2. Add daily task (e.g., 8:00 AM):
   ```cron
   0 8 * * * cd /path/to/QA3 && /usr/bin/python3 newsletter_generator.py
   ```

## 🎨 Features

- **Modular Design**: Each component (fetch, summarize, send) is separate and testable
- **Beautiful HTML Emails**: Professional newsletter template with responsive design
- **Error Handling**: Comprehensive error handling and logging
- **Configurable**: Easy configuration through environment variables
- **Testing Tools**: Individual component tests for debugging
- **Flexible Topics**: Support for multiple topics and keywords

## 🐛 Troubleshooting

### Common Issues

**"NEWSAPI_KEY not found"**
- Ensure `.env` file exists in the same directory
- Check that variable names match exactly
- No quotes needed around values in `.env`

**"No articles returned"**
- Check your NewsAPI quota (free tier: 100 requests/day)
- Verify your API key is valid
- Try broader search terms

**"OpenAI API error"**
- Ensure you have credits in your OpenAI account
- Check your API key is valid and active
- Verify you're using the correct model name

**"SMTP Authentication failed"**
- For Gmail: Use App Password, not regular password
- Enable 2-factor authentication first
- Check sender email is correct

**"No module named 'dotenv'"**
- Run: `pip install python-dotenv`

## 📊 Understanding the Code

### news_fetcher.py
- **Purpose**: Fetch articles from NewsAPI
- **Key Function**: `fetch_top_headlines(topics, language, country, max_articles)`
- **API Endpoint**: `https://newsapi.org/v2/everything`
- **Returns**: List of article dictionaries with title, description, URL, source, etc.

### ai_summarizer.py
- **Purpose**: Summarize articles using OpenAI
- **Key Function**: `summarize_articles(articles)`
- **Model Used**: GPT-3.5-turbo (cost-effective)
- **Returns**: Articles with added 'summary' field

### email_sender.py
- **Purpose**: Format and send HTML newsletters
- **Key Function**: `send_newsletter(articles, recipients, intro_text)`
- **Protocol**: SMTP with TLS encryption
- **Returns**: Boolean indicating success/failure

### newsletter_generator.py
- **Purpose**: Orchestrate the entire workflow
- **Process**: Fetch → Summarize → Send
- **Error Handling**: Validates config, handles failures gracefully

## 📝 Assignment Checklist

For your demonstration, be prepared to:

- [ ] Explain the three-step workflow (Fetch, Summarize, Send)
- [ ] Show how NewsAPI is used to fetch articles
- [ ] Demonstrate AI summarization with OpenAI
- [ ] Show email formatting and sending
- [ ] Run the application live
- [ ] Show the received email in your inbox
- [ ] Explain error handling in each module
- [ ] Point to specific code sections for each feature
- [ ] Discuss how you would automate it (Task Scheduler/Cron)

## 💡 Tips for Demonstration

1. **Test Before Demo**: Run `test_components.py` to ensure everything works
2. **Prepare .env**: Have all API keys ready and tested
3. **Show Step-by-Step**: Run each module individually first, then the full app
4. **Explain Code**: Be ready to show specific functions and explain their purpose
5. **Demo Email**: Have your email open to show the received newsletter
6. **Discuss Debugging**: Mention the modular design helps isolate errors

## 📚 Additional Resources

- [NewsAPI Documentation](https://newsapi.org/docs)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Python SMTP Documentation](https://docs.python.org/3/library/smtplib.html)
- [Gmail App Passwords](https://support.google.com/accounts/answer/185833)

## 🔒 Security Notes

- **Never commit `.env` file** - It contains sensitive API keys
- **Use app passwords** - Not your regular email password
- **Keep API keys secret** - Don't share or expose them
- **Monitor usage** - Check API quotas to avoid unexpected charges

## 📄 License

This project is for educational purposes as part of DS3850 Quarterly Assessment 3.

---

**Author**: Created for Tennessee Tech University DS3850  
**Date**: Fall 2025  
**Version**: 1.0
