"""
Component Testing Script
Run this to test each component individually and diagnose issues.
"""

import os
from dotenv import load_dotenv


def test_environment():
    """Test that environment variables are loaded correctly."""
    print("\n" + "="*80)
    print("TEST 1: Environment Variables")
    print("="*80)
    
    load_dotenv()
    
    required_vars = [
        'NEWSAPI_KEY',
        'OPENAI_API_KEY',
        'EMAIL_SENDER',
        'EMAIL_PASSWORD',
        'EMAIL_RECIPIENTS'
    ]
    
    optional_vars = [
        'NEWS_TOPICS',
        'NEWS_LANGUAGE',
        'NEWS_COUNTRY',
        'MAX_ARTICLES'
    ]
    
    all_good = True
    
    print("\nRequired Variables:")
    for var in required_vars:
        value = os.getenv(var)
        if value:
            # Mask sensitive values
            if 'KEY' in var or 'PASSWORD' in var:
                display_value = value[:8] + "..." if len(value) > 8 else "***"
            else:
                display_value = value
            print(f"  ✓ {var}: {display_value}")
        else:
            print(f"  ✗ {var}: MISSING")
            all_good = False
    
    print("\nOptional Variables:")
    for var in optional_vars:
        value = os.getenv(var)
        if value:
            print(f"  ✓ {var}: {value}")
        else:
            print(f"  ⊘ {var}: Not set (will use default)")
    
    if all_good:
        print("\n✓ All required environment variables are set!")
    else:
        print("\n✗ Some required variables are missing. Check your .env file.")
    
    return all_good


def test_news_api():
    """Test the NewsAPI connection and data fetching."""
    print("\n" + "="*80)
    print("TEST 2: News API Connection")
    print("="*80)
    
    try:
        from news_fetcher import NewsFetcher
        
        api_key = os.getenv('NEWSAPI_KEY')
        if not api_key:
            print("✗ Cannot test - NEWSAPI_KEY not found")
            return False
        
        fetcher = NewsFetcher(api_key)
        
        # Test with a simple query
        print("\nFetching test articles for 'technology'...")
        articles = fetcher.fetch_top_headlines(['technology'], max_articles=3)
        
        if articles:
            print(f"\n✓ Successfully fetched {len(articles)} articles!")
            print("\nSample article:")
            sample = articles[0]
            print(f"  Title: {sample.get('title', 'N/A')}")
            print(f"  Source: {sample.get('source', {}).get('name', 'N/A')}")
            print(f"  URL: {sample.get('url', 'N/A')}")
            return True
        else:
            print("\n✗ No articles returned. Check your API key and quota.")
            return False
            
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_openai_api():
    """Test the OpenAI API connection and summarization."""
    print("\n" + "="*80)
    print("TEST 3: OpenAI API Connection")
    print("="*80)
    
    try:
        from ai_summarizer import AISummarizer
        
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("✗ Cannot test - OPENAI_API_KEY not found")
            return False
        
        summarizer = AISummarizer(api_key)
        
        # Create a test article
        test_article = {
            'title': 'Test Article: AI Makes Progress',
            'description': 'Artificial intelligence continues to advance rapidly.',
            'content': 'Researchers have made significant breakthroughs in AI technology.',
        }
        
        print("\nGenerating test summary...")
        summary = summarizer.summarize_article(test_article)
        
        if summary:
            print(f"\n✓ Successfully generated summary!")
            print(f"\nSummary: {summary}")
            return True
        else:
            print("\n✗ No summary generated. Check your API key.")
            return False
            
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_email_format():
    """Test email HTML formatting (without sending)."""
    print("\n" + "="*80)
    print("TEST 4: Email HTML Formatting")
    print("="*80)
    
    try:
        from email_sender import EmailSender
        from datetime import datetime
        
        # Create test sender (credentials not needed for formatting)
        sender = EmailSender("test@test.com", "password")
        
        # Create test articles
        test_articles = [
            {
                'title': 'Test Article 1',
                'url': 'https://example.com/1',
                'summary': 'This is a test summary for the first article.',
                'source': {'name': 'Test Source'},
                'topic': 'technology',
                'publishedAt': datetime.now().isoformat()
            },
            {
                'title': 'Test Article 2',
                'url': 'https://example.com/2',
                'summary': 'This is a test summary for the second article.',
                'source': {'name': 'Another Source'},
                'topic': 'AI',
                'publishedAt': datetime.now().isoformat()
            }
        ]
        
        print("\nGenerating HTML newsletter...")
        html = sender.format_newsletter_html(test_articles, "This is a test newsletter!")
        
        # Save to file for inspection
        with open('test_newsletter.html', 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"\n✓ Successfully generated {len(html)} characters of HTML!")
        print("✓ Saved to 'test_newsletter.html' - you can open this in a browser to preview")
        return True
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_email_send():
    """Test actual email sending (optional - asks for confirmation)."""
    print("\n" + "="*80)
    print("TEST 5: Email Sending (Optional)")
    print("="*80)
    
    response = input("\nDo you want to send a test email? (yes/no): ").lower()
    
    if response != 'yes':
        print("⊘ Skipping email send test")
        return None
    
    try:
        from email_sender import EmailSender
        from datetime import datetime
        
        sender_email = os.getenv('EMAIL_SENDER')
        password = os.getenv('EMAIL_PASSWORD')
        recipients = os.getenv('EMAIL_RECIPIENTS', '').split(',')
        
        if not sender_email or not password or not recipients or recipients == ['']:
            print("✗ Cannot test - Email configuration incomplete")
            return False
        
        sender = EmailSender(sender_email, password)
        
        # Create a simple test article
        test_articles = [{
            'title': 'Test Newsletter Article',
            'url': 'https://example.com',
            'summary': 'This is a test newsletter to verify email delivery.',
            'source': {'name': 'Test System'},
            'topic': 'testing',
            'publishedAt': datetime.now().isoformat()
        }]
        
        print(f"\nSending test email to: {', '.join(recipients)}")
        success = sender.send_newsletter(
            test_articles,
            recipients,
            "This is a test newsletter. If you received this, the email system is working!"
        )
        
        if success:
            print("\n✓ Test email sent successfully! Check your inbox.")
            return True
        else:
            print("\n✗ Failed to send test email. Check the error messages above.")
            return False
            
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("\n" + "="*80)
    print("AI-POWERED NEWS NEWSLETTER - COMPONENT TESTING")
    print("="*80)
    print("\nThis script will test each component individually.")
    print("Use this to diagnose issues before running the full application.")
    
    results = {}
    
    # Run tests
    results['Environment'] = test_environment()
    results['News API'] = test_news_api()
    results['OpenAI API'] = test_openai_api()
    results['Email Format'] = test_email_format()
    results['Email Send'] = test_email_send()
    
    # Summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    
    for test_name, result in results.items():
        if result is True:
            print(f"  ✓ {test_name}: PASSED")
        elif result is False:
            print(f"  ✗ {test_name}: FAILED")
        else:
            print(f"  ⊘ {test_name}: SKIPPED")
    
    # Overall result
    failed = [name for name, result in results.items() if result is False]
    
    print("\n" + "="*80)
    if not failed:
        print("✓ ALL TESTS PASSED!")
        print("You're ready to run the full newsletter generator!")
    else:
        print(f"✗ {len(failed)} TEST(S) FAILED:")
        for name in failed:
            print(f"  - {name}")
        print("\nPlease fix the issues above before running the full application.")
    print("="*80)


if __name__ == "__main__":
    main()


