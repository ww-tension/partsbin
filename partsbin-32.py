# === Stage 32: Add pagination helpers for long console output ===
# Project: PartsBin
def paginate(lines, page_size=20):
    """Yield chunks of `lines` as lists of strings."""
    for i in range(0, len(lines), page_size):
        yield lines[i:i + page_size]

def format_page_header(current, total):
    """Return a compact pagination status line."""
    return f"[Page {current + 1}/{total}]"

def print_paginated(lines, page_size=20):
    """Print `lines` to console in pages, showing progress between pages."""
    pages = list(paginate(lines, page_size))
    total = len(pages)
    for idx, page in enumerate(pages):
        print(format_page_header(idx, total))
        for line in page:
            print(line)
        if idx < total - 1:
            print()
