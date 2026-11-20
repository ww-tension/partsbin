# === Stage 61: Add performance timing for core list and search operations ===
# Project: PartsBin
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end - start
    return wrapper


class PerformanceTracker:
    def __init__(self):
        self.timings = {}

    def record(self, name, duration):
        self.timings[name] = self.timings.get(name, 0.0) + duration

    def report(self):
        for name, duration in self.timings.items():
            print(f"{name}: {duration:.6f}s")

    def reset(self):
        self.timings = {}


def time_operations(parts_list, query=None):
    tracker = PerformanceTracker()
    if query:
        start = time.perf_counter()
        results = [p for p in parts_list if query in p['name'].lower()]
        tracker.record("search", time.perf_counter() - start)
    start = time.perf_counter()
    count = len(parts_list)
    tracker.record("list", time.perf_counter() - start)
    return tracker, results if query else count
