# Quick Reference: Changing Topics in Your Demo

## 🎤 **30-Second Answer** (Short Version)

> "Topics are configured in the `.env` file using the `NEWS_TOPICS` variable. You edit this file, change the comma-separated topics, and the next run will fetch news on your new topics."

## 🎤 **2-Minute Answer** (Detailed Version)

### Step 1: Show Where It's Configured (30 sec)
> "Topics are stored in the `.env` configuration file. Here on line 16, you can see `NEWS_TOPICS=technology,artificial intelligence,data science`. This is where all topics are defined."

**Action**: Open `.env` file, point to `NEWS_TOPICS` line

### Step 2: Show How Code Reads It (30 sec)
> "In `newsletter_generator.py` on line 34, the application reads this value using `os.getenv('NEWS_TOPICS')`, splits it by commas into a list, and removes any extra spaces. Then it passes this list to the news fetcher."

**Action**: Open `newsletter_generator.py`, point to line 34

### Step 3: Show How It's Used (30 sec)
> "In `news_fetcher.py`, starting at line 49, there's a loop that goes through each topic. For each topic, it makes an API call to NewsAPI with that topic as the search query. All the articles from all topics are then combined into one newsletter."

**Action**: Open `news_fetcher.py`, point to line 49-75 (the loop)

### Step 4: Demonstrate Changing It (30 sec)
> "To change topics, I simply edit the `.env` file. For example, if I wanted sports news, I'd change it to `NEWS_TOPICS=sports,football,basketball`. Then when I run the application, it automatically uses the new topics - no code changes needed!"

**Action**: Show editing `.env`, change topics, run `python news_fetcher.py` to test

## 📝 **Live Demo Steps**

### Option A: Quick Demo (1 minute)
1. Open `.env` in editor
2. Change `NEWS_TOPICS=technology,artificial intelligence,data science` to `NEWS_TOPICS=sports,football`
3. Save file
4. Run: `python news_fetcher.py`
5. Show it fetches sports articles instead

### Option B: Use Helper Script (1 minute)
1. Run: `python change_topics.py`
2. Enter new topics when prompted
3. Show it updates `.env` automatically
4. Run: `python news_fetcher.py` to verify

## 🔍 **Code Locations to Point To**

### 1. Configuration File
- **File**: `.env`
- **Line**: Look for `NEWS_TOPICS=`
- **What to say**: "This is where topics are configured - just a simple text file"

### 2. Code That Reads Configuration
- **File**: `newsletter_generator.py`
- **Line**: 34
- **Code**: `self.topics = os.getenv('NEWS_TOPICS', 'technology').split(',')`
- **What to say**: "This line reads the topics from the environment variable and splits them into a list"

### 3. Code That Fetches Articles
- **File**: `news_fetcher.py`
- **Line**: 49-75
- **Code**: The `for topic in topics:` loop
- **What to say**: "This loop iterates through each topic and makes an API call to NewsAPI for each one"

## 💡 **Example Topics for Demo**

**Sports Example:**
```
NEWS_TOPICS=sports,football,basketball
```

**Health Example:**
```
NEWS_TOPICS=health,medicine,wellness
```

**Science Example:**
```
NEWS_TOPICS=science,space,physics
```

## ⚡ **Quick Test Command**

After changing topics, test immediately:
```bash
python news_fetcher.py
```

This shows what articles will be fetched without generating a full newsletter.

## 🎯 **Key Points to Emphasize**

1. ✅ **No code changes needed** - Just edit `.env` file
2. ✅ **Easy to configure** - Comma-separated list
3. ✅ **Flexible** - Any topics that NewsAPI supports
4. ✅ **Immediate** - Changes take effect on next run
5. ✅ **Testable** - Can test topics with `news_fetcher.py` first

## 📋 **If Asked "Can you change it programmatically?"**

**Answer**: 
> "The current implementation uses the `.env` file for simplicity and ease of use. However, you could extend this to accept command-line arguments, read from a file, or even create a web interface. But for this project, editing the configuration file is the standard approach - it's simple, doesn't require code changes, and follows best practices for configuration management."

## 🚀 **Perfect Demo Flow**

1. **Show current topics** in `.env`
2. **Point to code** that reads them (`newsletter_generator.py` line 34)
3. **Point to code** that uses them (`news_fetcher.py` line 49)
4. **Change topics** in `.env` (live edit)
5. **Test it** with `python news_fetcher.py`
6. **Show results** - new topics fetch different articles

**Total time**: ~2 minutes, shows complete understanding! ✅


