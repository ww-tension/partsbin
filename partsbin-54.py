# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: PartsBin
def colorize(text, code):
    return "\033[" + code + "m" + text + "\033[0m"

def print_parts_table(parts):
    if not parts:
        print(colorize("No parts found.", "90"))
        return
    header = "ID".ljust(5) + "Name".ljust(25) + "Qty".rjust(6) + "Reorder".rjust(9) + "Supplier"
    print(colorize(header, "1;4"))
    for p in parts:
        qty = colorize(str(p["qty"]), "32" if p["qty"] < p["reorder"] else "38")
        line = (str(p["id"]).ljust(5) + p["name"].ljust(25) +
                qty.rjust(6) + str(p["reorder"]).rjust(9) + str(p["supplier"]))
        print(colorize(line, "32" if p["qty"] < p["reorder"] else "38"))
    print(colorize("\n", "0"))
