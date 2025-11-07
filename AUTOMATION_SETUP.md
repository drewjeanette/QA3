# Automation Setup Guide

How to schedule your newsletter to run automatically every day.

## Windows Task Scheduler (Recommended for Windows)

### Step-by-Step Setup

#### 1. Open Task Scheduler

- Press `Win + R`
- Type: `taskschd.msc`
- Press Enter

#### 2. Create a New Task

1. Click **"Create Basic Task"** in the right panel
2. Name: `AI News Newsletter`
3. Description: `Daily automated news newsletter with AI summaries`
4. Click **Next**

#### 3. Set the Trigger (When to Run)

1. Select: **"Daily"**
2. Click **Next**
3. Set start date: Today's date
4. Set time: `08:00:00 AM` (or your preferred time)
5. Recur every: `1` days
6. Click **Next**

#### 4. Set the Action (What to Run)

1. Select: **"Start a program"**
2. Click **Next**
3. Program/script: `python`
   - Or full path: `C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe`
4. Add arguments: `newsletter_generator.py`
5. Start in: `C:\Users\drewj\OneDrive - Tennessee Tech University\_SENIOR\Fall 2025\DS3850\QA3\QA3`
   - (Your project folder - use your actual path!)
6. Click **Next**

#### 5. Review and Finish

1. Check **"Open the Properties dialog"**
2. Click **Finish**

#### 6. Advanced Settings (Optional but Recommended)

In the Properties dialog:

**General Tab**:
- ✓ Run whether user is logged on or not
- ✓ Run with highest privileges

**Conditions Tab**:
- ✓ Start only if the computer is on AC power (uncheck if laptop)
- ✓ Wake the computer to run this task

**Settings Tab**:
- ✓ Allow task to be run on demand
- ✓ If the task fails, restart every: 1 hour
- Attempt to restart up to: 3 times

Click **OK** to save.

### Testing Your Scheduled Task

1. Find your task in Task Scheduler Library
2. Right-click → **Run**
3. Check your email for the newsletter
4. Check **History** tab to see if it ran successfully

### Common Issues

**"The task is currently running"**
- Task is working! Check email.

**"Last Run Result: 0x1"**
- Python path is wrong
- Right-click task → Properties → Actions → Edit
- Use full Python path

**Task doesn't run when computer is asleep**
- Properties → Conditions → ✓ Wake computer to run

**Permission errors**
- Properties → General → ✓ Run with highest privileges

---

## Alternative: Using Batch Script

### Option A: Create a Scheduled Task with the Batch File

1. Follow steps above
2. Instead of `python` and arguments, use:
   - Program/script: `C:\Users\drewj\OneDrive - Tennessee Tech University\_SENIOR\Fall 2025\DS3850\QA3\QA3\run_newsletter.bat`
   - Leave arguments blank
   - Leave "Start in" blank

### Option B: Manual Daily Run

- Double-click `run_newsletter.bat` each morning
- Simple but not automated

---

## macOS/Linux (Using Cron)

### Edit Crontab

```bash
crontab -e
```

### Add Daily Task

```cron
# Run at 8:00 AM every day
0 8 * * * cd /path/to/QA3 && /usr/bin/python3 newsletter_generator.py >> /path/to/newsletter.log 2>&1
```

### Cron Syntax Explained

```
* * * * * command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-7, Sunday = 0 or 7)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

### Examples

```cron
# Every day at 8:00 AM
0 8 * * * cd /path/to/QA3 && python3 newsletter_generator.py

# Every weekday at 9:00 AM
0 9 * * 1-5 cd /path/to/QA3 && python3 newsletter_generator.py

# Every Monday at 7:00 AM
0 7 * * 1 cd /path/to/QA3 && python3 newsletter_generator.py

# Twice daily: 8 AM and 8 PM
0 8,20 * * * cd /path/to/QA3 && python3 newsletter_generator.py
```

### View Your Cron Jobs

```bash
crontab -l
```

### Remove a Cron Job

```bash
crontab -e
# Delete the line and save
```

---

## Testing Automation

### Test 1: Run Manually First

Before automating, make sure it works:

```bash
python newsletter_generator.py
```

### Test 2: Run from Scheduler

1. Set up task with a time 2 minutes from now
2. Wait and check email
3. Verify it worked
4. Change to your desired time

### Test 3: Check Logs

**Windows Task Scheduler**:
- Task → History tab
- Look for "Task completed" events

**Cron (Linux/Mac)**:
- Add logging to cron job:
  ```cron
  0 8 * * * cd /path/to/QA3 && python3 newsletter_generator.py >> ~/newsletter.log 2>&1
  ```
- Check log: `cat ~/newsletter.log`

---

## Monitoring & Maintenance

### Daily Checks

Your newsletter should arrive daily. If it doesn't:

1. Check Task Scheduler/Cron status
2. Check API quotas (NewsAPI: 100/day limit)
3. Check OpenAI credits
4. Check email spam folder

### Weekly Maintenance

- Monitor API usage and costs
- Update topics if needed
- Clean up old test emails

### Monthly Review

- Review OpenAI costs (~$7-10/month)
- Check if NewsAPI free tier is sufficient
- Update Python packages: `pip install --upgrade -r requirements.txt`

---

## Cost Considerations

### Free Tiers

- **NewsAPI**: 100 requests/day (plenty for daily newsletter)
- **Email (Gmail)**: Unlimited (essentially)

### Paid Services

- **OpenAI**: ~$0.01 per newsletter
  - Daily: ~$0.30/month
  - Cost example: 5 articles × $0.002/summary = $0.01/day

### Reducing Costs

1. **Fewer articles**: `MAX_ARTICLES=3` instead of `MAX_ARTICLES=5`
2. **Fewer topics**: 2-3 topics instead of 5+
3. **Less frequent**: Weekly instead of daily
4. **Use GPT-3.5**: Already using the cheapest model

---

## Advanced Scheduling Ideas

### Weekdays Only

**Windows**: 
- Trigger → Weekly
- Select Mon, Tue, Wed, Thu, Fri

**Cron**:
```cron
0 8 * * 1-5 cd /path/to/QA3 && python3 newsletter_generator.py
```

### Different Topics on Different Days

Create multiple scripts/configs:

**Monday-Wednesday**: AI & Technology
```env
NEWS_TOPICS=artificial intelligence,technology
```

**Thursday-Friday**: Data Science & Python
```env
NEWS_TOPICS=data science,python programming
```

### Multiple Newsletters Per Day

**Morning Brief** (7 AM): Quick 3 articles
**Evening Digest** (6 PM): Detailed 10 articles

Set up two separate scheduled tasks.

---

## Troubleshooting Automation

### Task Runs But No Email

1. Check Task Scheduler History for errors
2. Run manually to see error messages
3. Check .env file is in correct location
4. Verify API keys haven't expired

### Task Doesn't Run at All

1. Verify task is **Enabled**
2. Check trigger is set correctly
3. Ensure computer is on at scheduled time
4. Check wake settings if computer sleeps

### "Cannot find file" Error

- Start in directory must be project folder
- Use absolute paths
- Check Python path is correct

---

## For Your Demonstration

When explaining automation:

> "I've set up Windows Task Scheduler to run this script daily at 8 AM. The scheduler calls Python with the path to newsletter_generator.py, and the script runs in the project directory where the .env file is located. I've configured it to wake the computer if needed and retry if it fails."

**Show**:
- Open Task Scheduler
- Show your task configuration
- Show the trigger (daily at 8 AM)
- Show the action (runs Python script)
- Optional: Show history of successful runs

---

## Quick Reference

### Windows Task Scheduler Command

```
Program: python
Arguments: newsletter_generator.py
Start in: C:\path\to\your\QA3\folder
```

### Cron One-liner

```bash
0 8 * * * cd /path/to/QA3 && python3 newsletter_generator.py >> ~/newsletter.log 2>&1
```

### Find Python Path (Windows)

```cmd
where python
```

### Find Python Path (Mac/Linux)

```bash
which python3
```

---

**Your newsletter is now fully automated! 🎉**


