import os
from getpass import getpass
from langchain_google_genai import ChatGoogleGenerativeAI

def setup_langchain():
    os.environ["GOOGLE_API_KEY"] = getpass("Enter your Google AI API key: ")
    
    # Set up the Google AI language model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    
    return llm