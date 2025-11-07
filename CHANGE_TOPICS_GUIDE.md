# How to Change Newsletter Topics

## 📍 Quick Answer for Your Demonstration

**"The topics are configured in the `.env` file using the `NEWS_TOPICS` variable. You simply edit this file, change the comma-separated topics, and the next time you run the newsletter generator, it will fetch news on your new topics."**

## 🎯 Step-by-Step Explanation

### 1. Where Topics Are Configured

**Location**: `.env` file in your project directory

**Variable Name**: `NEWS_TOPICS`

**Current Format**: Comma-separated list of topics

```
NEWS_TOPICS=technology,artificial intelligence,data science
```

### 2. How It Works in the Code

**File**: `newsletter_generator.py` (line 34)

```python
# Load news configuration
self.topics = os.getenv('NEWS_TOPICS', 'technology').split(',')
self.topics = [topic.strip() for topic in self.topics]  # Remove whitespace
```

**What this does:**
- Reads the `NEWS_TOPICS` value from `.env`
- Splits it by commas into a list
- Removes any extra spaces
- Uses this list to fetch articles for each topic

**File**: `news_fetcher.py` (line 49-75)

```python
for topic in topics:
    # Build API request for each topic
    params = {
        'q': topic,  # Search query = your topic
        'apiKey': self.api_key,
        'language': language,
        'sortBy': 'publishedAt',
        'pageSize': max_articles
    }
    # Makes API call to NewsAPI
```

**What this does:**
- Loops through each topic you specified
- Makes a separate API call to NewsAPI for each topic
- Combines all articles into one newsletter

### 3. How to Change Topics

#### Method 1: Edit `.env` File Directly (Recommended)

1. **Open `.env` file** in any text editor (Notepad, VS Code, etc.)

2. **Find this line:**
   ```
   NEWS_TOPICS=technology,artificial intelligence,data science
   ```

3. **Change to your desired topics:**
   ```
   NEWS_TOPICS=sports,football,basketball
   ```
   or
   ```
   NEWS_TOPICS=health,medicine,wellness
   ```
   or
   ```
   NEWS_TOPICS=cooking,recipes,food
   ```

4. **Save the file**

5. **Run the newsletter generator again:**
   ```bash
   python newsletter_generator.py
   ```

#### Method 2: Use the Helper Script

Run:
```bash
python change_topics.py
```

This will guide you through changing topics interactively.

### 4. Examples of Good Topics

**Technology Focus:**
```
NEWS_TOPICS=technology,software,programming,python,AI
```

**Business Focus:**
```
NEWS_TOPICS=business,finance,startups,economy
```

**Health Focus:**
```
NEWS_TOPICS=health,medicine,wellness,mental health
```

**Sports Focus:**
```
NEWS_TOPICS=sports,football,basketball,baseball
```

**Science Focus:**
```
NEWS_TOPICS=science,space,physics,chemistry
```

**Entertainment Focus:**
```
NEWS_TOPICS=entertainment,movies,music,television
```

### 5. Tips for Choosing Topics

✅ **Do:**
- Use specific keywords: "artificial intelligence" not just "AI"
- Use common terms that news sites write about
- Separate multi-word topics with commas: "machine learning, deep learning"
- Keep it to 3-5 topics for manageable newsletter size

❌ **Don't:**
- Use very obscure topics (may return no results)
- Use too many topics (will make newsletter very long)
- Use special characters or quotes
- Put spaces before/after commas (though the code handles this)

### 6. Testing Your Topics

Before generating a full newsletter, test if your topics work:

```bash
python news_fetcher.py
```

This will show you what articles are found for your current topics.

## 🎤 What to Say in Your Demonstration

### Short Answer (30 seconds):
> "The topics are configured in the `.env` configuration file. You simply edit the `NEWS_TOPICS` variable, which accepts a comma-separated list of topics. When you run the newsletter generator, it fetches articles for each topic from NewsAPI and combines them into one newsletter."

### Detailed Answer (2 minutes):

**Step 1: Show the Configuration**
> "Let me show you where topics are configured. Here in the `.env` file, you can see the `NEWS_TOPICS` variable on line 16. Currently it's set to 'technology, artificial intelligence, data science'."

**Step 2: Show How It's Used in Code**
> "In the `newsletter_generator.py` file, on line 34, the application reads this value and splits it into a list of topics. Then in `news_fetcher.py`, starting at line 49, it loops through each topic and makes an API call to NewsAPI for each one."

**Step 3: Demonstrate Changing It**
> "To change topics, I simply edit this line in the `.env` file. For example, if I wanted sports news, I'd change it to 'sports, football, basketball'. Then when I run the application again, it will fetch articles on these new topics."

**Step 4: Show It Working**
> "Let me demonstrate by changing it to 'sports' temporarily, running the news fetcher to show it works, then changing it back."

## 💡 Advanced: Programmatic Topic Changes

If asked about changing topics programmatically (not just in `.env`):

You could modify the code to:
1. Accept topics as command-line arguments
2. Read topics from a file
3. Use a web interface to change topics
4. Have different topic sets for different days

But for this project, editing `.env` is the simplest and most maintainable approach.

## 🔍 Troubleshooting Topics

**Problem**: No articles found for a topic
- **Solution**: Try a more general term or check spelling

**Problem**: Too many articles
- **Solution**: Reduce `MAX_ARTICLES` in `.env` (e.g., change from 5 to 3)

**Problem**: Not enough articles
- **Solution**: Use more general topics or increase `MAX_ARTICLES`

**Problem**: Articles not relevant
- **Solution**: Make topics more specific (e.g., "machine learning" instead of "technology")

## 📝 Quick Reference

| What | Where | How |
|------|-------|-----|
| **Change topics** | `.env` file | Edit `NEWS_TOPICS=...` |
| **Current topics** | `.env` line 16 | `NEWS_TOPICS=technology,artificial intelligence,data science` |
| **Code that reads topics** | `newsletter_generator.py` line 34 | `self.topics = os.getenv('NEWS_TOPICS').split(',')` |
| **Code that fetches by topic** | `news_fetcher.py` line 49 | `for topic in topics:` |
| **Test topics** | Run `python news_fetcher.py` | Shows articles found for each topic |

---

**Remember**: After changing topics in `.env`, just run `python newsletter_generator.py` again - no code changes needed! 🚀


