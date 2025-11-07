# Quick Demo Code Reference
## Exact Lines to Point To During Your Presentation

Use this as a cheat sheet during your demo. Each section tells you exactly which file and line numbers to open.

---

## 📋 **QUICK OVERVIEW** (30 seconds)

**File**: `newsletter_generator.py`  
**Lines**: 76-138

**What to Say:**
> "The main workflow is in the `generate_and_send` method. You can see the three steps clearly marked: Step 1 fetches news, Step 2 summarizes with AI, and Step 3 sends the email."

---

## 📰 **STEP 1: FETCHING DATA**

### Where It's Called
**File**: `newsletter_generator.py`  
**Lines**: 89-97

```python
# Step 1: Fetch News Articles
print("\n📰 STEP 1: Fetching News Articles")
print("-" * 80)
articles = self.news_fetcher.fetch_top_headlines(
    topics=self.topics,
    language=self.language,
    country=self.country,
    max_articles=self.max_articles
)
```

**Point to**: Line 92 - `self.news_fetcher.fetch_top_headlines(...)`

---

### Where Topics Come From
**File**: `newsletter_generator.py`  
**Lines**: 33-34

```python
self.topics = os.getenv('NEWS_TOPICS', 'technology').split(',')
self.topics = [topic.strip() for topic in self.topics]
```

**Point to**: Line 34 - Shows how topics are loaded from `.env`

---

### The API Call
**File**: `news_fetcher.py`  
**Lines**: 54-64

```python
# Build the request parameters
params = {
    'q': topic,
    'apiKey': self.api_key,
    'language': language,
    'sortBy': 'publishedAt',
    'pageSize': max_articles
}

# Make the API request
url = f"{self.base_url}/everything"
response = requests.get(url, params=params)
```

**Point to**: 
- Line 55 - `'q': topic` (the search query)
- Line 64 - `requests.get(url, params=params)` (the actual API call)

---

### Processing the Response
**File**: `news_fetcher.py`  
**Lines**: 67-76

```python
if response.status_code == 200:
    data = response.json()
    
    if data['status'] == 'ok':
        articles = data.get('articles', [])
        
        # Add topic to each article for context
        for article in articles:
            article['topic'] = topic
            all_articles.append(article)
```

**Point to**:
- Line 68 - `response.json()` (parsing JSON response)
- Line 71 - `articles = data.get('articles', [])` (extracting articles)
- Line 75 - `article['topic'] = topic` (adding topic context)

---

## 🤖 **STEP 2: SUMMARIZING DATA**

### Where It's Called
**File**: `newsletter_generator.py`  
**Lines**: 105-111

```python
# Step 2: Summarize Articles with AI
print("\n🤖 STEP 2: Summarizing Articles with AI")
print("-" * 80)
summarized_articles = self.ai_summarizer.summarize_articles(articles)

# Generate newsletter introduction
intro_text = self.ai_summarizer.create_newsletter_summary(summarized_articles)
```

**Point to**: Line 108 - `self.ai_summarizer.summarize_articles(articles)`

---

### OpenAI Client Setup
**File**: `ai_summarizer.py`  
**Lines**: 24-25

```python
self.client = OpenAI(api_key=api_key)
self.model = model
```

**Point to**: Line 24 - `OpenAI(api_key=api_key)` (initializing OpenAI client)

---

### Building the Prompt
**File**: `ai_summarizer.py`  
**Lines**: 50-56

```python
# Create the prompt for the AI
prompt = f"""Please provide a concise 2-3 sentence summary of the following news article. 
Focus on the key points and main takeaways:

{text_to_summarize}

Summary:"""
```

**Point to**: Lines 51-56 - The prompt template (explain prompt engineering)

---

### The API Call
**File**: `ai_summarizer.py`  
**Lines**: 59-67

```python
# Call OpenAI API
response = self.client.chat.completions.create(
    model=self.model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes news articles concisely."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150,
    temperature=0.7
)
```

**Point to**:
- Line 59 - `chat.completions.create(...)` (the API call)
- Line 62 - System message (sets AI's role)
- Line 63 - User message (contains our prompt)
- Line 65 - `max_tokens=150` (limits summary length)
- Line 66 - `temperature=0.7` (controls randomness)

---

### Extracting the Summary
**File**: `ai_summarizer.py`  
**Lines**: 69-71

```python
# Extract the summary
summary = response.choices[0].message.content.strip()
return summary
```

**Point to**: Line 70 - Extracting the AI's response from the API result

---

### Adding Summary to Article
**File**: `ai_summarizer.py`  
**Lines**: 95-99

```python
summary = self.summarize_article(article)

# Add summary to article
article['summary'] = summary
summarized_articles.append(article)
```

**Point to**: Line 98 - `article['summary'] = summary` (adding summary to article dict)

---

## 📧 **STEP 3: EMAIL FORMATTING AND SENDING**

### Where It's Called
**File**: `newsletter_generator.py`  
**Lines**: 115-122

```python
# Step 3: Send Email Newsletter
print("\n📧 STEP 3: Sending Email Newsletter")
print("-" * 80)
success = self.email_sender.send_newsletter(
    articles=summarized_articles,
    recipient_emails=self.email_recipients,
    intro_text=intro_text
)
```

**Point to**: Line 118 - `self.email_sender.send_newsletter(...)`

---

### HTML Formatting Function
**File**: `email_sender.py`  
**Lines**: 34-223

**Key Section - Building HTML Structure** (Lines 49-156):
```python
# Start building HTML
html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        /* CSS styles */
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📰 AI-Powered News Newsletter</h1>
            <div class="date">{current_date}</div>
        </div>
"""
```

**Point to**: 
- Line 54 - CSS styles (explain professional styling)
- Line 153 - Header with newsletter title

---

### Adding Articles to HTML
**File**: `email_sender.py`  
**Lines**: 167-195

```python
# Add each article
for i, article in enumerate(articles, 1):
    title = article.get('title', 'No Title')
    url = article.get('url', '#')
    summary = article.get('summary', article.get('description', 'No summary available'))
    source = article.get('source', {}).get('name', 'Unknown Source')
    topic = article.get('topic', 'General')
    
    html += f"""
        <div class="article">
            <div class="article-title">
                <a href="{url}" target="_blank">{i}. {title}</a>
            </div>
            <div class="article-meta">
                <span class="topic-tag">{topic}</span>
                {source} • {published_str}
            </div>
            <div class="article-summary">
                {summary}
            </div>
            <a href="{url}" class="read-more" target="_blank">Read full article →</a>
        </div>
    """
```

**Point to**:
- Line 170 - `summary = article.get('summary', ...)` (uses AI summary)
- Line 180 - Article title as clickable link
- Line 185 - Topic tag display
- Line 189 - AI-generated summary displayed

---

### Creating Email Message
**File**: `email_sender.py`  
**Lines**: 143-151

```python
# Create message
message = MIMEMultipart("alternative")
message["From"] = self.sender_email
message["To"] = ", ".join(recipient_emails)
message["Subject"] = subject

# Attach HTML content
html_part = MIMEText(html_content, "html")
message.attach(html_part)
```

**Point to**:
- Line 143 - `MIMEMultipart("alternative")` (allows HTML email)
- Line 150 - `MIMEText(html_content, "html")` (attaching HTML content)

---

### SMTP Connection and Sending
**File**: `email_sender.py`  
**Lines**: 153-160

```python
# Connect to SMTP server and send email
print(f"\nConnecting to SMTP server: {self.smtp_server}:{self.smtp_port}")
with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
    server.starttls()  # Enable TLS encryption
    print("Logging in...")
    server.login(self.sender_email, self.password)
    print("Sending email...")
    server.send_message(message)
```

**Point to**:
- Line 155 - `smtplib.SMTP(...)` (connecting to SMTP server)
- Line 156 - `server.starttls()` (enabling TLS encryption)
- Line 159 - `server.login(...)` (authenticating)
- Line 161 - `server.send_message(message)` (sending email)

---

## 🎯 **KEY TALKING POINTS BY STEP**

### Step 1: Fetching
- **REST API**: Uses HTTP GET requests
- **API Key Authentication**: Secure access to NewsAPI
- **Error Handling**: Continues if one topic fails
- **Data Structure**: Returns list of dictionaries

### Step 2: Summarizing
- **Prompt Engineering**: Carefully crafted prompts for best results
- **Token Limits**: `max_tokens=150` keeps summaries concise
- **Temperature**: Controls AI creativity vs consistency
- **Fallback**: Uses description if AI fails

### Step 3: Email
- **HTML Email**: Professional formatting with CSS
- **SMTP Protocol**: Standard email transmission protocol
- **TLS Encryption**: Secure email transmission
- **Multi-part Messages**: Supports HTML formatting

---

## 🔍 **DEMONSTRATION CHECKLIST**

- [ ] Open `newsletter_generator.py` - show overall structure
- [ ] Show Step 1 in `newsletter_generator.py` (line 89-97)
- [ ] Show `news_fetcher.py` - API call (line 64)
- [ ] Show response processing (line 68-76)
- [ ] Show Step 2 in `newsletter_generator.py` (line 105-111)
- [ ] Show `ai_summarizer.py` - prompt (line 50-56)
- [ ] Show API call (line 59-67)
- [ ] Show Step 3 in `newsletter_generator.py` (line 115-122)
- [ ] Show `email_sender.py` - HTML formatting (line 167-195)
- [ ] Show SMTP sending (line 153-160)
- [ ] Show received email in inbox

---

## 💡 **PRO TIPS**

1. **Use split screen**: Show code on one side, terminal/email on other
2. **Run commands live**: Actually execute the code during demo
3. **Point with cursor**: Use your mouse to highlight specific lines
4. **Explain as you go**: Don't just show code, explain what it does
5. **Show the flow**: Trace data from one function to the next

---

**Print this page and keep it next to your computer during the demo!** 📄

