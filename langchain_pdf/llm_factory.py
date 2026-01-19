"""
llm_factory.py
--------------

Factory for creating LLM instances.
This file lives INSIDE the package so CLI works after installation.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_llm():
    """
    Lazily create and return an LLM instance.

    Currently supports Google Gemini via LangChain.
    """
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
    except ImportError as e:
        raise ImportError(
            "langchain-google-genai is required for --topic generation.\n"
            "Install it via: pip install langchain-google-genai"
        ) from e

    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY or GEMINI_API_KEY not found in environment."
        )

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.9,
    )
