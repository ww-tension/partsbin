# === Stage 31: Add compact table rendering for long lists ===
# Project: PartsBin
import textwrap

def render_compact_table(headers, rows, max_width=80):
    """Render a compact table for long lists without overflow."""
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    col_widths = [min(w, max_width // len(headers)) for w in col_widths]

    lines = []
    for i, h in enumerate(headers):
        lines.append(("─" * col_widths[i]).center(col_widths[i]))
    lines.append("─" * sum(col_widths))
    for row in rows:
        line = ""
        for i, cell in enumerate(row):
            line += str(cell).ljust(col_widths[i])
        lines.append(line)
    return "\n".join(lines)
