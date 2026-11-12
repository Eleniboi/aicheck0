"""Checkpoint 01: Primitives, String Manipulation & Prompt Formatting

Repository: github.com/maddox-bayn/aicheck0
Contains 10 production-grade exercises for Checkpoint 01.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, AsyncIterator, Callable, Iterable, Iterator
import ast
import asyncio
import hashlib
import json
import math
import os
import re
import secrets
import sqlite3
import time
import numpy as np
from pydantic import BaseModel, Field, field_validator, model_validator


# Exercise 01.01: format_system_prompt
def format_system_prompt(role: str, context: str, query: str) -> str:
    """Format prompt string stripping whitespace from all inputs: 'Role: {role}\nContext: {context}\nQuery: {query}'."""
    # TODO: 

    role = role.strip()
    context = context.strip()
    query = query.strip()
    
    return f'Role: {role}\nContext: {context}\nQuery: {query}'
    raise NotImplementedError('Implement Exercise 01.01: format_system_prompt')


# Exercise 01.02: estimate_tokens
def estimate_tokens(text: str) -> int:
    """Estimate token count using 1 token ~= 4 chars, rounded up. Return 0 for empty string."""
    # TODO: Implement Exercise 01.02
    if text == "":
        return 0
    return math.ceil(len(text) / 4)    
    
    raise NotImplementedError('Implement Exercise 01.02: estimate_tokens')


# Exercise 01.03: clean_generation
def clean_generation(raw_output: str, stop_token: str = '<|endoftext|>') -> str:
    """Remove all occurrences of stop_t
    oken and truncate everything at/after '### END', then strip."""
    # TODO: Implement Exercise 01.03

    raise NotImplementedError('Implement Exercise 01.03: clean_generation')


# Exercise 01.04: calculate_call_cost
def calculate_call_cost(prompt_tokens: int, completion_tokens: int, input_price_per_m: float, output_price_per_m: float) -> float:
    """Compute total USD cost given per-1M-token rates, rounded to 6 decimal places."""
    # TODO: Implement Exercise 01.04
    raise NotImplementedError('Implement Exercise 01.04: calculate_call_cost')


# Exercise 01.05: extract_code_block
def extract_code_block(llm_response: str, language: str = 'python') -> str:
    """Extract raw code inside ```{language} ... ``` or generic ``` ... ``` fences, or stripped string."""
    target_fence = f"```{language}"

    # 1. Check for specific language fence: ```{language}
    if target_fence.lower() in llm_response.lower():
        # Find where the fence starts (case-insensitive)
        idx = llm_response.lower().find(target_fence.lower())
        after_open = llm_response[idx + len(target_fence):]
        # Drop the rest of the fence header line (e.g. newline)
        if "\n" in after_open:
            after_open = after_open.split("\n", 1)[1]
        # Slice up to the closing fence
        if "```" in after_open:
            return after_open.split("```", 1)[0].strip()

    # 2. Check for generic fence: ```
    if "```" in llm_response:
        after_open = llm_response.split("```", 1)[1]
        if "\n" in after_open:
            after_open = after_open.split("\n", 1)[1]
        if "```" in after_open:
            return after_open.split("```", 1)[0].strip()

    # 3. Fallback: plain text without fences
    return llm_response.strip()

# Exercise 01.06: clamp_temperature
def clamp_temperature(temp: float | int) -> float:
    """Validate numeric type (reject bool/str with TypeError) and clamp to [0.0, 2.0]."""
    # TODO: Implement Exercise 01.06
    raise NotImplementedError('Implement Exercise 01.06: clamp_temperature')


# Exercise 01.07: wrap_untrusted_input
def wrap_untrusted_input(user_text: str, tag: str = 'user_input') -> str:
    """Escape existing <tag> or </tag> as &lt;tag&gt; and &lt;/tag&gt; and wrap in <tag>...</tag>."""
    # TODO: Implement Exercise 01.07
    raise NotImplementedError('Implement Exercise 01.07: wrap_untrusted_input')


# Exercise 01.08: contains_flagged_keyword
def contains_flagged_keyword(prompt: str, banned_csv: str) -> bool:
    """Check if prompt contains any whole word from comma-separated banned_csv (case-insensitive)."""
    # TODO: Implement Exercise 01.08
    raise NotImplementedError('Implement Exercise 01.08: contains_flagged_keyword')


# Exercise 01.09: middle_truncate
def middle_truncate(text: str, max_chars: int) -> str:
    """If len(text) > max_chars, keep first max_chars//2 and last max_chars//2 joined by '...[TRUNCATED]...'."""
    # TODO: Implement Exercise 01.09
    raise NotImplementedError('Implement Exercise 01.09: middle_truncate')


# Exercise 01.10: parse_model_id
def parse_model_id(model_string: str) -> tuple[str, str, str]:
    """Parse 'provider/model-YYYY-MM-DD' into (provider, model_family, version_date). Default version_date='latest'. Raise ValueError if '/' missing."""
    # TODO: Implement Exercise 01.10
    raise NotImplementedError('Implement Exercise 01.10: parse_model_id')

