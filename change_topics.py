"""
Interactive script to help change newsletter topics easily.
Run this script to update topics in your .env file.
"""

import os
import re
from pathlib import Path


def read_env_file():
    """Read the .env file and return its contents."""
    env_path = Path('.env')
    
    if not env_path.exists():
        print("ERROR: .env file not found!")
        print("Please make sure you're in the project directory and have a .env file.")
        return None
    
    with open(env_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_env_file(content):
    """Write content back to .env file."""
    env_path = Path('.env')
    with open(env_path, 'w', encoding='utf-8') as f:
        f.write(content)


def get_current_topics(env_content):
    """Extract current topics from .env content."""
    match = re.search(r'NEWS_TOPICS=(.+)', env_content)
    if match:
        topics_str = match.group(1).strip()
        topics = [t.strip() for t in topics_str.split(',')]
        return topics
    return []


def update_topics(env_content, new_topics):
    """Update NEWS_TOPICS in .env content."""
    # Join topics with commas
    topics_str = ','.join(new_topics)
    
    # Replace the NEWS_TOPICS line
    pattern = r'NEWS_TOPICS=.+'
    replacement = f'NEWS_TOPICS={topics_str}'
    
    new_content = re.sub(pattern, replacement, env_content)
    return new_content


def main():
    """Main interactive function."""
    print("=" * 80)
    print("CHANGE NEWSLETTER TOPICS")
    print("=" * 80)
    print()
    
    # Read .env file
    env_content = read_env_file()
    if env_content is None:
        return
    
    # Get current topics
    current_topics = get_current_topics(env_content)
    
    print(f"Current topics: {', '.join(current_topics) if current_topics else 'None found'}")
    print()
    
    # Get new topics from user
    print("Enter your new topics (comma-separated):")
    print("Example: technology,artificial intelligence,data science")
    print("Or: sports,football,basketball")
    print()
    
    user_input = input("New topics: ").strip()
    
    if not user_input:
        print("No topics entered. Exiting without changes.")
        return
    
    # Split and clean topics
    new_topics = [topic.strip() for topic in user_input.split(',') if topic.strip()]
    
    if not new_topics:
        print("No valid topics found. Exiting without changes.")
        return
    
    print()
    print(f"New topics will be: {', '.join(new_topics)}")
    print()
    
    # Confirm
    confirm = input("Save these topics? (yes/no): ").lower()
    
    if confirm != 'yes':
        print("Cancelled. No changes made.")
        return
    
    # Update .env file
    updated_content = update_topics(env_content, new_topics)
    write_env_file(updated_content)
    
    print()
    print("✓ Topics updated successfully!")
    print()
    print("You can now run the newsletter generator:")
    print("  python newsletter_generator.py")
    print()
    print("Or test the topics first:")
    print("  python news_fetcher.py")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
    except Exception as e:
        print(f"\nError: {str(e)}")

