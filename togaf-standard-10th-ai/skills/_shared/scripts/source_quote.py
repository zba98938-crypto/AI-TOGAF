"""Reject navigation text mistaken for substantive standard evidence."""
import re


def navigation_quote(text):
    if not isinstance(text, str):
        return False
    return bool(re.search(r'(?:\.\s*){4,}|…{2,}', text) or
                re.fullmatch(r'\s*(?:Index|Contents|Table of Contents|List of (?:Figures|Tables))\s*', text, re.I))
