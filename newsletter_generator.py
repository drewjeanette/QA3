"""
AI-Powered News Newsletter Generator - Main Application
Integrates news fetching, AI summarization, and email delivery.
"""

import os
from dotenv import load_dotenv
from news_fetcher import NewsFetcher
from ai_summarizer import AISummarizer
from email_sender import EmailSender
from datetime import datetime


class NewsletterGenerator:
    """
    Main application class that orchestrates the newsletter generation process.
    """
    
    def __init__(self):
        """
        Initialize the Newsletter Generator by loading configuration and setting up modules.
        """
        # Load environment variables from .env file
        load_dotenv()
        
        # Load and validate API keys
        self.newsapi_key = os.getenv('NEWSAPI_KEY')
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.email_sender = os.getenv('EMAIL_SENDER')
        self.email_password = os.getenv('EMAIL_PASSWORD')
        self.email_recipients = os.getenv('EMAIL_RECIPIENTS', '').split(',')
        
        # Load news configuration
        self.topics = os.getenv('NEWS_TOPICS', 'technology').split(',')
        self.topics = [topic.strip() for topic in self.topics]  # Remove whitespace
        self.language = os.getenv('NEWS_LANGUAGE', 'en')
        self.country = os.getenv('NEWS_COUNTRY', 'us')
        self.max_articles = int(os.getenv('MAX_ARTICLES', '5'))
        
        # Validate required configuration
        self._validate_config()
        
        # Initialize modules
        self.news_fetcher = NewsFetcher(self.newsapi_key)
        self.ai_summarizer = AISummarizer(self.openai_key)
        self.email_sender = EmailSender(self.email_sender, self.email_password)
        
        print("✓ Newsletter Generator initialized successfully!")
        print(f"  Topics: {', '.join(self.topics)}")
        print(f"  Max articles: {self.max_articles}")
        print(f"  Recipients: {len(self.email_recipients)}")
    
    def _validate_config(self):
        """
        Validate that all required configuration is present.
        Raises an error if any required values are missing.
        """
        errors = []
        
        if not self.newsapi_key:
            errors.append("NEWSAPI_KEY is missing")
        if not self.openai_key:
            errors.append("OPENAI_API_KEY is missing")
        if not self.email_sender:
            errors.append("EMAIL_SENDER is missing")
        if not self.email_password:
            errors.append("EMAIL_PASSWORD is missing")
        if not self.email_recipients or self.email_recipients == ['']:
            errors.append("EMAIL_RECIPIENTS is missing")
        
        if errors:
            error_msg = "Configuration errors found:\n  - " + "\n  - ".join(errors)
            error_msg += "\n\nPlease check your .env file and ensure all required values are set."
            raise ValueError(error_msg)
    
    def generate_and_send(self):
        """
        Main workflow: Fetch news → Summarize → Send email
        
        Returns:
            bool: True if newsletter was sent successfully, False otherwise
        """
        try:
            print("\n" + "="*80)
            print(f"AI-POWERED NEWS NEWSLETTER GENERATOR")
            print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*80)
            
            # Step 1: Fetch News Articles
            print("\n📰 STEP 1: Fetching News Articles")
            print("-" * 80)
            articles = self.news_fetcher.fetch_top_headlines(
                topics=self.topics,
                language=self.language,
                country=self.country,
                max_articles=self.max_articles
            )
            
            if not articles:
                print("✗ No articles found. Aborting newsletter generation.")
                return False
            
            print(f"\n✓ Step 1 Complete: Fetched {len(articles)} articles")
            
            # Step 2: Summarize Articles with AI
            print("\n🤖 STEP 2: Summarizing Articles with AI")
            print("-" * 80)
            summarized_articles = self.ai_summarizer.summarize_articles(articles)
            
            # Generate newsletter introduction
            intro_text = self.ai_summarizer.create_newsletter_summary(summarized_articles)
            
            print(f"\n✓ Step 2 Complete: All articles summarized")
            
            # Step 3: Send Email Newsletter
            print("\n📧 STEP 3: Sending Email Newsletter")
            print("-" * 80)
            success = self.email_sender.send_newsletter(
                articles=summarized_articles,
                recipient_emails=self.email_recipients,
                intro_text=intro_text
            )
            
            if success:
                print(f"\n✓ Step 3 Complete: Newsletter sent successfully")
                print("\n" + "="*80)
                print("✓ NEWSLETTER GENERATION COMPLETE!")
                print("="*80)
                return True
            else:
                print(f"\n✗ Step 3 Failed: Could not send newsletter")
                return False
                
        except Exception as e:
            print(f"\n✗ ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    def test_components(self):
        """
        Test each component individually to verify everything is working.
        Useful for debugging.
        """
        print("\n" + "="*80)
        print("TESTING INDIVIDUAL COMPONENTS")
        print("="*80)
        
        # Test 1: News Fetcher
        print("\n1. Testing News Fetcher...")
        print("-" * 80)
        try:
            test_articles = self.news_fetcher.fetch_top_headlines(
                topics=[self.topics[0]],
                max_articles=2
            )
            if test_articles:
                print(f"✓ News Fetcher working - Retrieved {len(test_articles)} articles")
            else:
                print("✗ News Fetcher returned no articles")
        except Exception as e:
            print(f"✗ News Fetcher error: {str(e)}")
        
        # Test 2: AI Summarizer
        print("\n2. Testing AI Summarizer...")
        print("-" * 80)
        try:
            if test_articles:
                sample = test_articles[0]
                summary = self.ai_summarizer.summarize_article(sample)
                print(f"✓ AI Summarizer working")
                print(f"   Sample: {summary[:100]}...")
            else:
                print("⊘ Skipping (no articles available)")
        except Exception as e:
            print(f"✗ AI Summarizer error: {str(e)}")
        
        # Test 3: Email Sender (format only, don't send)
        print("\n3. Testing Email Formatter...")
        print("-" * 80)
        try:
            if test_articles:
                # Add summary to article for testing
                test_articles[0]['summary'] = "This is a test summary."
                html = self.email_sender.format_newsletter_html(test_articles[:1])
                print(f"✓ Email Formatter working - Generated {len(html)} chars of HTML")
            else:
                print("⊘ Skipping (no articles available)")
        except Exception as e:
            print(f"✗ Email Formatter error: {str(e)}")
        
        print("\n" + "="*80)
        print("COMPONENT TESTING COMPLETE")
        print("="*80)


def main():
    """
    Main entry point for the application.
    """
    try:
        # Initialize the generator
        generator = NewsletterGenerator()
        
        # Generate and send the newsletter
        success = generator.generate_and_send()
        
        # Exit with appropriate code
        exit(0 if success else 1)
        
    except Exception as e:
        print(f"\n✗ FATAL ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)


if __name__ == "__main__":
    main()

