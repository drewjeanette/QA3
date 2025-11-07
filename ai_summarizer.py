"""
AI Summarizer Module
Uses OpenAI's GPT model to summarize news articles into concise summaries.
"""

import os
from typing import List, Dict
from openai import OpenAI


class AISummarizer:
    """
    Handles AI-powered summarization of news articles using OpenAI's API.
    """
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        Initialize the AI Summarizer.
        
        Args:
            api_key: Your OpenAI API key from https://platform.openai.com/
            model: The model to use (default: gpt-3.5-turbo for cost-effectiveness)
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model
    
    def summarize_article(self, article: Dict) -> str:
        """
        Summarize a single article using AI.
        
        Args:
            article: Dictionary containing article data (title, description, content, url)
            
        Returns:
            A concise summary string
        """
        try:
            # Extract relevant information from the article
            title = article.get('title', 'No title')
            description = article.get('description', '')
            content = article.get('content', '')
            
            # Build the text to summarize
            text_to_summarize = f"Title: {title}\n\n"
            if description:
                text_to_summarize += f"Description: {description}\n\n"
            if content:
                text_to_summarize += f"Content: {content}"
            
            # Create the prompt for the AI
            prompt = f"""Please provide a concise 2-3 sentence summary of the following news article. 
Focus on the key points and main takeaways:

{text_to_summarize}

Summary:"""
            
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
            
            # Extract the summary
            summary = response.choices[0].message.content.strip()
            return summary
            
        except Exception as e:
            print(f"Error summarizing article '{title}': {str(e)}")
            # Fallback to description if AI fails
            return article.get('description', 'Summary not available')
    
    def summarize_articles(self, articles: List[Dict]) -> List[Dict]:
        """
        Summarize multiple articles.
        
        Args:
            articles: List of article dictionaries
            
        Returns:
            List of articles with added 'summary' field
        """
        print(f"\nSummarizing {len(articles)} articles using AI...")
        
        summarized_articles = []
        
        for i, article in enumerate(articles, 1):
            print(f"  [{i}/{len(articles)}] Summarizing: {article.get('title', 'No title')[:60]}...")
            
            summary = self.summarize_article(article)
            
            # Add summary to article
            article['summary'] = summary
            summarized_articles.append(article)
            
            print(f"    ✓ Summary generated ({len(summary)} chars)")
        
        print(f"\n✓ All {len(summarized_articles)} articles summarized successfully!")
        return summarized_articles
    
    def create_newsletter_summary(self, articles: List[Dict]) -> str:
        """
        Create an overall summary of all articles for the newsletter intro.
        
        Args:
            articles: List of article dictionaries
            
        Returns:
            A brief overview of the newsletter content
        """
        try:
            topics = set(article.get('topic', 'General') for article in articles)
            topics_str = ", ".join(topics)
            
            prompt = f"""Write a brief, engaging 2-sentence introduction for a newsletter covering these topics: {topics_str}.
The newsletter contains {len(articles)} articles. Make it professional but friendly."""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a professional newsletter writer."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.8
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Error creating newsletter summary: {str(e)}")
            return f"Welcome to your personalized news newsletter featuring {len(articles)} articles on {topics_str}!"


def test_ai_summarizer():
    """
    Test function to verify the AI summarizer works correctly.
    Run this file directly to test: python ai_summarizer.py
    """
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("ERROR: OPENAI_API_KEY not found in .env file")
        return
    
    # Initialize the summarizer
    summarizer = AISummarizer(api_key)
    
    # Create sample article
    sample_article = {
        'title': 'Breakthrough in Artificial Intelligence: New Model Achieves Human-Level Performance',
        'description': 'Researchers have developed a new AI model that demonstrates human-level performance across multiple tasks.',
        'content': 'A team of researchers at a leading technology company has announced a breakthrough in artificial intelligence. The new model, which uses advanced neural network architectures, has achieved performance levels comparable to humans in various cognitive tasks including reasoning, problem-solving, and language understanding.',
        'url': 'https://example.com/article',
        'topic': 'artificial intelligence'
    }
    
    # Test summarization
    print("\n" + "="*80)
    print("TEST: AI SUMMARIZER")
    print("="*80)
    print(f"\nOriginal Article Title: {sample_article['title']}")
    print(f"Original Description: {sample_article['description']}")
    
    summary = summarizer.summarize_article(sample_article)
    
    print(f"\n{'='*80}")
    print("AI-Generated Summary:")
    print(f"{'='*80}")
    print(summary)
    
    # Test newsletter intro
    print(f"\n{'='*80}")
    print("Newsletter Introduction:")
    print(f"{'='*80}")
    intro = summarizer.create_newsletter_summary([sample_article])
    print(intro)


if __name__ == "__main__":
    test_ai_summarizer()

