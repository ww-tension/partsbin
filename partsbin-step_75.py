# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: PartsBin
def generate_validation_report(parts, suppliers):
    warnings = []
    errors = []
    supplier_names = set(s['name'] for s in suppliers)

    for part in parts:
        if not part.get('name'):
            errors.append(f"Part id {part.get('id')}: missing name")
        if part.get('quantity') is None:
            errors.append(f"Part '{part.get('name') or part.get('id')}': missing quantity")
        elif part['quantity'] < 0:
            errors.append(f"Part '{part.get('name') or part.get('id')}': negative quantity {part['quantity']}")
        if not part.get('reorder_point') is None and part['reorder_point'] < 0:
            errors.append(f"Part '{part.get('name') or part.get('id')}': negative reorder point")
        if part.get('reorder_point') is None:
            warnings.append(f"Part '{part.get('name') or part.get('id')}': no reorder point set")
        if part.get('supplier_id') is not None:
            supplier_id = part['supplier_id']
            matching = [s for s in suppliers if s['id'] == supplier_id]
            if not matching:
                errors.append(f"Part '{part.get('name') or part.get('id')}': unknown supplier_id {supplier_id}")
            elif matching and not matching[0].get('name'):
                warnings.append(f"Part '{part.get('name') or part.get('id')}': supplier has no name")
        if part.get('quantity', 0) <= part.get('reorder_point', 0) and part.get('reorder_point') is not None:
            warnings.append(f"Part '{part.get('name') or part.get('id')}': quantity {part['quantity']} is at or below reorder point {part['reorder_point']}")

    report = {"warnings": warnings, "errors": errors}
    return report
