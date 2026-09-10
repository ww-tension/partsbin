# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: PartsBin
def search_inventory(self, query, field="name"):
    query = query.strip().lower()
    if not query:
        return [item for item in self._inventory.values()]
    results = []
    for key, item in self._inventory.items():
        for search_field in field, "name", "description", "sku", "category", "unit", "supplier_name":
            val = item.get(search_field, "")
            if query in str(val).lower():
                results.append(item)
                break
    return results
