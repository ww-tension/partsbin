# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: PartsBin
def repair_data(path, min_qty=0):
    rows = []
    with open(path) as f:
        header = f.readline().split()
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != len(header):
                parts += [''] * (len(header) - len(parts))
                parts = parts[:len(header)]
            fields = {}
            for i, name in enumerate(header):
                name = name.strip()
                value = parts[i].strip()
                if name == 'name':
                    value = value.strip('"')
                if name == 'supplier':
                    value = value.strip('"')
                fields[name] = value
            if fields['name'] == '':
                fields['name'] = 'Unknown'
            qty = fields.get('quantity', '0')
            try:
                qty = int(qty)
            except ValueError:
                qty = 0
            fields['quantity'] = qty
            if qty < min_qty:
                fields['quantity'] = min_qty
            rows.append(fields)
    with open(path, 'w') as f:
        f.write(','.join(header) + '\n')
        for r in rows:
            name = r['name']
            supplier = r['supplier']
            f.write(','.join([
                '"' + str(name) + '"',
                str(r['part_number']),
                str(r['quantity']),
                str(r['reorder_point']),
                '"' + str(supplier) + '"'
            ]) + '\n')
    return len(rows)
