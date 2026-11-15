# === Stage 51: Add unit tests for search and filter behavior ===
# Project: PartsBin
def test_search_by_name():
    assert bin_search("bolt", items) == ["Bolt", "Machine Bolt"]
    assert bin_search("widget", items) == ["Widget"]


def test_search_case_insensitive():
    assert bin_search("BOLT", items) == ["Bolt", "Machine Bolt"]
    assert bin_search("bolt", items) == ["Bolt", "Machine Bolt"]


def test_search_no_match():
    assert bin_search("nonexistent", items) == []


def test_filter_by_reorder():
    assert bin_search("low", items) == ["Bolt", "Nut"]
    assert bin_search("high", items) == ["Widget"]


def test_filter_by_supplier():
    assert bin_search("acme", items) == ["Bolt", "Machine Bolt", "Screw"]
    assert bin_search("globex", items) == ["Nut", "Widget"]


def test_filter_by_quantity():
    assert bin_search("overstocked", items) == ["Screw"]
    assert bin_search("understocked", items) == ["Bolt", "Nut"]
