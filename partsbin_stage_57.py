# === Stage 57: Add structured result objects for command handlers ===
# Project: PartsBin
class BinResult:
    def __init__(self, ok, message):
        self.ok = ok
        self.message = message

    def to_dict(self):
        return {"ok": self.ok, "message": self.message}


class PartResult:
    def __init__(self, ok, message):
        self.ok = ok
        self.message = message

    def to_dict(self):
        return {"ok": self.ok, "message": self.message}


class SupplierResult:
    def __init__(self, ok, message):
        self.ok = ok
        self.message = message

    def to_dict(self):
        return {"ok": self.ok, "message": self.message}


class QuantityResult:
    def __init__(self, ok, message):
        self.ok = ok
        self.message = message

    def to_dict(self):
        return {"ok": self.ok, "message": self.message}
