# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: PartsBin
CONFIRM = False


def clear_state():
    global CONFIRM
    if CONFIRM:
        parts = []
        suppliers = []
        with open(PARTS_FILE, "w"):
            pass
        with open(SUPPLIERS_FILE, "w"):
            pass
        CONFIRM = False
        print("PartsBin state cleared.")
    else:
        print("A destructive command requires confirmation. Re-run with --confirm.")
