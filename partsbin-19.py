# === Stage 19: Add undo support for the last simple mutation ===
# Project: PartsBin
import bisect

class UndoStack:
    """Records the last mutation so it can be reversed."""
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def undo(self):
        if not self._stack:
            return None
        return self._stack.pop()

    @property
    def size(self):
        return len(self._stack)
