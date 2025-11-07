"""
Email Sender Module
Formats and sends newsletter emails using SMTP.
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
from datetime import datetime


class EmailSender:
    """
    Handles formatting and sending newsletter emails via SMTP.
    """
    
    def __init__(self, sender_email: str, password: str, smtp_server: str = "smtp.gmail.com", smtp_port: int = 587):
        """
        Initialize the Email Sender.
        
        Args:
            sender_email: Email address to send from
            password: App password for the email account
            smtp_server: SMTP server address (default: Gmail)
            smtp_port: SMTP port (default: 587 for TLS)
        """
        self.sender_email = sender_email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
    
    def format_newsletter_html(self, articles: List[Dict], intro_text: str = None) -> str:
        """
        Format articles into an attractive HTML newsletter.
        
        Args:
            articles: List of article dictionaries with summaries
            intro_text: Optional introduction text for the newsletter
            
        Returns:
            HTML string for the email body
        """
        # Get current date
        current_date = datetime.now().strftime("%B %d, %Y")
        
        # Start building HTML
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f4f4f4;
                }}
                .container {{
                    background-color: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }}
                .header {{
                    text-align: center;
                    border-bottom: 3px solid #4CAF50;
                    padding-bottom: 20px;
                    margin-bottom: 30px;
                }}
                .header h1 {{
                    color: #4CAF50;
                    margin: 0;
                    font-size: 28px;
                }}
                .date {{
                    color: #666;
                    font-size: 14px;
                    margin-top: 10px;
                }}
                .intro {{
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-left: 4px solid #4CAF50;
                    margin-bottom: 30px;
                    font-style: italic;
                }}
                .article {{
                    margin-bottom: 30px;
                    padding-bottom: 20px;
                    border-bottom: 1px solid #eee;
                }}
                .article:last-child {{
                    border-bottom: none;
                }}
                .article-title {{
                    color: #2196F3;
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 10px;
                }}
                .article-title a {{
                    color: #2196F3;
                    text-decoration: none;
                }}
                .article-title a:hover {{
                    text-decoration: underline;
                }}
                .article-meta {{
                    color: #666;
                    font-size: 12px;
                    margin-bottom: 10px;
                }}
                .article-summary {{
                    color: #444;
                    line-height: 1.6;
                }}
                .topic-tag {{
                    display: inline-block;
                    background-color: #4CAF50;
                    color: white;
                    padding: 3px 10px;
                    border-radius: 3px;
                    font-size: 11px;
                    margin-right: 5px;
                    text-transform: uppercase;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 2px solid #eee;
                    color: #666;
                    font-size: 12px;
                }}
                .read-more {{
                    display: inline-block;
                    margin-top: 10px;
                    color: #2196F3;
                    text-decoration: none;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📰 AI-Powered News Newsletter</h1>
                    <div class="date">{current_date}</div>
                </div>
        """
        
        # Add introduction if provided
        if intro_text:
            html += f"""
                <div class="intro">
                    {intro_text}
                </div>
            """
        
        # Add each article
        for i, article in enumerate(articles, 1):
            title = article.get('title', 'No Title')
            url = article.get('url', '#')
            summary = article.get('summary', article.get('description', 'No summary available'))
            source = article.get('source', {}).get('name', 'Unknown Source')
            topic = article.get('topic', 'General')
            published_at = article.get('publishedAt', '')
            
            # Format published date
            if published_at:
                try:
                    pub_date = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                    published_str = pub_date.strftime("%B %d, %Y")
                except:
                    published_str = published_at
            else:
                published_str = 'Date unknown'
            
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
        
        # Add footer
        html += f"""
                <div class="footer">
                    <p>This newsletter was automatically generated using AI technology.</p>
                    <p>You received this email because you subscribed to AI-Powered News Newsletter.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def send_email(self, recipient_emails: List[str], subject: str, html_content: str) -> bool:
        """
        Send an email to recipients.
        
        Args:
            recipient_emails: List of recipient email addresses
            subject: Email subject line
            html_content: HTML content of the email
            
        Returns:
            True if email sent successfully, False otherwise
        """
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["From"] = self.sender_email
            message["To"] = ", ".join(recipient_emails)
            message["Subject"] = subject
            
            # Attach HTML content
            html_part = MIMEText(html_content, "html")
            message.attach(html_part)
            
            # Connect to SMTP server and send email
            print(f"\nConnecting to SMTP server: {self.smtp_server}:{self.smtp_port}")
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Enable TLS encryption
                print("Logging in...")
                server.login(self.sender_email, self.password)
                print("Sending email...")
                server.send_message(message)
            
            print(f"✓ Email sent successfully to {len(recipient_emails)} recipient(s)!")
            return True
            
        except Exception as e:
            print(f"✗ Error sending email: {str(e)}")
            return False
    
    def send_newsletter(self, articles: List[Dict], recipient_emails: List[str], intro_text: str = None) -> bool:
        """
        Format and send the newsletter.
        
        Args:
            articles: List of articles with summaries
            recipient_emails: List of recipient email addresses
            intro_text: Optional introduction text
            
        Returns:
            True if sent successfully, False otherwise
        """
        # Generate subject line with current date
        subject = f"Your AI News Digest - {datetime.now().strftime('%B %d, %Y')}"
        
        # Format the HTML
        html_content = self.format_newsletter_html(articles, intro_text)
        
        # Send the email
        return self.send_email(recipient_emails, subject, html_content)


def test_email_sender():
    """
    Test function to verify the email sender works correctly.
    Run this file directly to test: python email_sender.py
    """
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv()
    
    sender_email = os.getenv('EMAIL_SENDER')
    password = os.getenv('EMAIL_PASSWORD')
    recipients = os.getenv('EMAIL_RECIPIENTS', '').split(',')
    
    if not sender_email or not password:
        print("ERROR: EMAIL_SENDER or EMAIL_PASSWORD not found in .env file")
        return
    
    if not recipients or recipients == ['']:
        print("ERROR: EMAIL_RECIPIENTS not found in .env file")
        return
    
    # Initialize email sender
    email_sender = EmailSender(sender_email, password)
    
    # Create sample articles
    sample_articles = [
        {
            'title': 'AI Breakthrough in Natural Language Processing',
            'url': 'https://example.com/article1',
            'summary': 'Researchers have developed a new model that can understand context better than ever before, achieving state-of-the-art results on multiple benchmarks.',
            'source': {'name': 'Tech News'},
            'topic': 'artificial intelligence',
            'publishedAt': datetime.now().isoformat()
        },
        {
            'title': 'New Data Science Framework Released',
            'url': 'https://example.com/article2',
            'summary': 'A powerful new framework for data analysis has been released, promising to make complex statistical analyses more accessible to developers.',
            'source': {'name': 'Dev Journal'},
            'topic': 'data science',
            'publishedAt': datetime.now().isoformat()
        }
    ]
    
    intro_text = "Welcome to today's newsletter! Here are the latest updates in AI and technology."
    
    # Test sending
    print("\n" + "="*80)
    print("TEST: EMAIL SENDER")
    print("="*80)
    print(f"Sender: {sender_email}")
    print(f"Recipients: {', '.join(recipients)}")
    
    success = email_sender.send_newsletter(sample_articles, recipients, intro_text)
    
    if success:
        print("\n✓ Test email sent successfully! Check your inbox.")
    else:
        print("\n✗ Test email failed. Check your credentials and settings.")


if __name__ == "__main__":
    test_email_sender()

