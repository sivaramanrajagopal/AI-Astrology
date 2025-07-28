#!/usr/bin/env python3
"""
Setup script for OpenAI API key configuration
"""

import os
import sys

def setup_api_key():
    """Interactive setup for OpenAI API key"""
    print("🔧 OpenAI API Key Setup")
    print("=" * 40)
    
    # Check if API key is already set
    try:
        from env_config import OPENAI_API_KEY
        if OPENAI_API_KEY != "your_openai_api_key_here":
            print("✅ API key is already configured!")
            print(f"Current key: {OPENAI_API_KEY[:10]}...{OPENAI_API_KEY[-4:]}")
            response = input("Do you want to update it? (y/n): ").lower()
            if response != 'y':
                return
    except ImportError:
        pass
    
    print("\n📋 Instructions:")
    print("1. Go to https://platform.openai.com/api-keys")
    print("2. Create a new API key or copy your existing one")
    print("3. Paste it below\n")
    
    # Get API key from user
    api_key = input("Enter your OpenAI API key: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Setup cancelled.")
        return
    
    if len(api_key) < 20:
        print("❌ API key seems too short. Please check and try again.")
        return
    
    # Update the env_config.py file
    try:
        with open('env_config.py', 'r') as f:
            content = f.read()
        
        # Replace the placeholder with the actual API key
        updated_content = content.replace(
            'OPENAI_API_KEY = "your_openai_api_key_here"',
            f'OPENAI_API_KEY = "{api_key}"'
        )
        
        with open('env_config.py', 'w') as f:
            f.write(updated_content)
        
        print("✅ API key configured successfully!")
        print("🔑 Your API key has been saved to env_config.py")
        print("\n🚀 You can now run the backend server:")
        print("   cd astro-backend")
        print("   python main.py")
        
    except Exception as e:
        print(f"❌ Error saving API key: {e}")
        print("Please manually update the OPENAI_API_KEY in env_config.py")

if __name__ == "__main__":
    setup_api_key() 