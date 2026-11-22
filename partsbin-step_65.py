# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: PartsBin
import os
import re
from collections import OrderedDict


def _normalize(name):
    return re.sub(r'[^A-Za-z0-9]', '_', name.strip().lower()).strip('_')


def _dedupe_imports(existing, new_names):
    seen = set(existing)
    merged = OrderedDict()
    for name in existing + new_names:
        key = _normalize(name)
        if key not in seen:
            seen.add(key)
            merged[key] = name
    return [merged[k] for k in sorted(merged.keys())]


def _extract_imports(text):
    imports = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        if stripped.startswith('import '):
            body = stripped[len('import '):]
            for part in body.replace(',', ' ').split():
                if not part.startswith('#'):
                    imports.append(part)
        elif stripped.startswith('from '):
            match = re.match(r'from\s+([\w\.]+)\s+import\s+(.+)', stripped)
            if match:
                module = match.group(1)
                names = [n.strip() for n in match.group(2).replace(',', ' ').split()]
                for name in names:
                    imports.append(f'{module}.{name}')
    return imports


def _build_import_block(existing, new_names):
    merged = _dedupe_imports(existing, new_names)
    block = ['import ' + ', '.join(merged)]
    for name in merged:
        if '.' in name and not name.startswith('import '):
            module, _, imported = name.partition('.')
            block.append(f'from {module} import {imported}')
    return '\n'.join(block)


def merge_imports(path, new_names):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    existing = _extract_imports(text)
    merged_block = _build_import_block(existing, new_names)
    if merged_block and merged_block not in text:
        additions = '\n' + merged_block
        new_text = text.replace('\n', additions, 1)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_text)
