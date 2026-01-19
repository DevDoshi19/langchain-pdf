"""
llm_factory.py
--------------

Provides a safe, minimal factory for creating LangChain LLM instances.

This module is intentionally isolated from the core library to keep
langchain_pdf LLM-agnostic.
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm(
    *,
    model: str = "gemini-2.5-flash-lite",
    temperature: float = 0.7,
):
    """
    Create and return a LangChain LLM instance.

    Environment variables required:
    - GOOGLE_API_KEY or GEMINI_API_KEY

    Parameters
    ----------
    model : str
        Gemini model name.
    temperature : float
        Sampling temperature.

    Returns
    -------
    ChatGoogleGenerativeAI
        Configured LLM instance.
    """
    # Load .env if present (safe to call multiple times)
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing Gemini API key.\n"
            "Set GOOGLE_API_KEY or GEMINI_API_KEY in your environment or .env file."
        )

    return ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        api_key=api_key
    )
