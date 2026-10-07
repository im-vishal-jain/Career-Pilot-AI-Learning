"""
Groq API client — wrapper around Groq's chat completions
Supports streaming, caching, and rate-limit handling
"""

import streamlit as st
import time
from groq import Groq, RateLimitError, APIError

MODEL = "llama-3.3-70b-versatile"
FALLBACK_MODEL = "llama-3.1-8b-instant"


def get_client() -> Groq:
    key = st.session_state.get("groq_api_key", "")
    if not key:
        raise ValueError("Groq API key not set. Please login with a valid key.")
    return Groq(api_key=key)


def chat(
    messages: list[dict],
    system_prompt: str = "",
    temperature: float = 0.7,
    max_tokens: int = 2048,
    model: str = MODEL,
    retries: int = 2,
) -> str:
    """
    Send a chat request to Groq and return the response text.
    Automatically falls back to a smaller model on rate-limit errors.
    """
    client = get_client()
    full_messages = []
    if system_prompt:
        full_messages.append({"role": "system", "content": system_prompt})
    full_messages.extend(messages)

    for attempt in range(retries + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=full_messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content.strip()

        except RateLimitError:
            if attempt < retries:
                time.sleep(2 ** attempt)
                model = FALLBACK_MODEL  # fall back on retry
            else:
                raise

        except APIError as e:
            raise RuntimeError(f"Groq API error: {e}") from e


def stream_chat(
    messages: list[dict],
    system_prompt: str = "",
    temperature: float = 0.7,
    max_tokens: int = 2048,
    model: str = MODEL,
):
    """
    Stream a chat response from Groq.
    Yields text chunks for use with st.write_stream or manual display.
    """
    client = get_client()
    full_messages = []
    if system_prompt:
        full_messages.append({"role": "system", "content": system_prompt})
    full_messages.extend(messages)

    try:
        stream = client.chat.completions.create(
            model=model,
            messages=full_messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta
    except RateLimitError:
        yield "\n\n⚠️ Rate limit reached. Please wait a moment and try again."
    except APIError as e:
        yield f"\n\n⚠️ API Error: {e}"


def quick_analysis(prompt: str, temperature: float = 0.5, max_tokens: int = 1500) -> str:
    """Convenience wrapper for single-prompt analysis calls."""
    return chat(
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
