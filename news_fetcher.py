"""
News Fetcher Module
Fetches the latest news articles from NewsAPI based on configured topics.
"""

import requests
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class NewsFetcher:
    """
    Handles fetching news articles from NewsAPI.
    Documentation: https://newsapi.org/docs
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the NewsFetcher with an API key.
        
        Args:
            api_key: Your NewsAPI key from https://newsapi.org/
        """
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"
    
    def fetch_top_headlines(
        self, 
        topics: List[str], 
        language: str = 'en',
        country: str = 'us',
        max_articles: int = 5
    ) -> List[Dict]:
        """
        Fetch top headlines for specified topics.
        
        Args:
            topics: List of topics/keywords to search for
            language: Language code (e.g., 'en' for English)
            country: Country code (e.g., 'us' for United States)
            max_articles: Maximum number of articles to fetch per topic
            
        Returns:
            List of article dictionaries containing title, description, url, source, etc.
        """
        all_articles = []
        
        for topic in topics:
            try:
                print(f"Fetching news for topic: {topic}")
                
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
                
                # Check if request was successful
                if response.status_code == 200:
                    data = response.json()
                    
                    if data['status'] == 'ok':
                        articles = data.get('articles', [])
                        
                        # Add topic to each article for context
                        for article in articles:
                            article['topic'] = topic
                            all_articles.append(article)
                        
                        print(f"  ✓ Found {len(articles)} articles for '{topic}'")
                    else:
                        print(f"  ✗ API returned error: {data.get('message', 'Unknown error')}")
                else:
                    print(f"  ✗ HTTP Error {response.status_code}: {response.text}")
                    
            except Exception as e:
                print(f"  ✗ Error fetching news for '{topic}': {str(e)}")
                continue
        
        print(f"\nTotal articles fetched: {len(all_articles)}")
        return all_articles
    
    def fetch_everything(
        self,
        query: str,
        from_date: Optional[str] = None,
        language: str = 'en',
        max_results: int = 10
    ) -> List[Dict]:
        """
        Fetch all articles matching a query.
        
        Args:
            query: Search query
            from_date: Date string in format YYYY-MM-DD (defaults to 7 days ago)
            language: Language code
            max_results: Maximum number of articles to return
            
        Returns:
            List of article dictionaries
        """
        try:
            # Default to last 7 days if no date specified
            if from_date is None:
                from_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
            
            params = {
                'q': query,
                'apiKey': self.api_key,
                'from': from_date,
                'language': language,
                'sortBy': 'publishedAt',
                'pageSize': max_results
            }
            
            url = f"{self.base_url}/everything"
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'ok':
                    return data.get('articles', [])
            
            return []
            
        except Exception as e:
            print(f"Error fetching articles: {str(e)}")
            return []


def test_news_fetcher():
    """
    Test function to verify the news fetcher works correctly.
    Run this file directly to test: python news_fetcher.py
    """
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv('NEWSAPI_KEY')
    if not api_key:
        print("ERROR: NEWSAPI_KEY not found in .env file")
        return
    
    # Initialize the fetcher
    fetcher = NewsFetcher(api_key)
    
    # Load topics from .env file (same as main application)
    topics_str = os.getenv('NEWS_TOPICS', 'technology,artificial intelligence')
    topics = [topic.strip() for topic in topics_str.split(',')]
    max_articles = int(os.getenv('MAX_ARTICLES', '3'))
    
    print(f"\nUsing topics from .env file: {', '.join(topics)}")
    
    articles = fetcher.fetch_top_headlines(topics, max_articles=max_articles)
    
    # Display results
    print("\n" + "="*80)
    print("TEST RESULTS")
    print("="*80)
    
    for i, article in enumerate(articles[:5], 1):
        print(f"\n{i}. {article.get('title', 'No title')}")
        print(f"   Topic: {article.get('topic', 'N/A')}")
        print(f"   Source: {article.get('source', {}).get('name', 'Unknown')}")
        print(f"   URL: {article.get('url', 'No URL')}")
        print(f"   Description: {article.get('description', 'No description')[:100]}...")


if __name__ == "__main__":
    test_news_fetcher()

