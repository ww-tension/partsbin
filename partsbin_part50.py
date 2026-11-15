# === Stage 50: Add unit tests for import and export behavior ===
# Project: PartsBin
import json
import csv
import io
import os
import tempfile
import unittest

from partsbin import PartsBin, Part


class TestImportExport(unittest.TestCase):

    def setUp(self):
        self.bin = PartsBin()
        self.bin.add_part(Part("Screw M4", 120, 20, "FastenerCo"))
        self.bin.add_part(Part("Bolt M6", 45, 10, "HardwarePlus"))
        self.bin.add_part(Part("Washer", 500, 50, "SupplyHouse"))

    def _load(self, path):
        bin = PartsBin()
        bin.load(path)
        return bin

    def test_export_json_roundtrip(self):
        path = os.path.join(tempfile.gettempdir(), "partsbin.json")
        self.bin.export_json(path)
        reloaded = self._load(path)
        self.assertEqual(reloaded.items, self.bin.items)

    def test_export_csv_roundtrip(self):
        path = os.path.join(tempfile.gettempdir(), "partsbin.csv")
        self.bin.export_csv(path)
        reloaded = self._load(path)
        self.assertEqual(reloaded.items, self.bin.items)

    def test_export_in_memory_json(self):
        data = self.bin.export_json_string()
        reloaded = PartsBin.import_json(data)
        self.assertEqual(reloaded.items, self.bin.items)

    def test_export_in_memory_csv(self):
        data = self.bin.export_csv_string()
        reloaded = PartsBin.import_csv(data)
        self.assertEqual(reloaded.items, self.bin.items)

    def test_json_is_valid_json(self):
        data = self.bin.export_json_string()
        parsed = json.loads(data)
        self.assertEqual(len(parsed), 3)

    def test_csv_has_expected_header(self):
        data = self.bin.export_csv_string()
        reader = csv.reader(io.StringIO(data))
        header = next(reader)
        self.assertIn("name", header)
        self.assertIn("quantity", header)
        self.assertIn("reorder_point", header)
        self.assertIn("supplier", header)

    def test_export_creates_file(self):
        path = os.path.join(tempfile.gettempdir(), "partsbin_created.json")
        self.bin.export_json(path)
        self.assertTrue(os.path.exists(path))

    def test_export_updates_existing_file(self):
        path = os.path.join(tempfile.gettempdir(), "partsbin_update.json")
        self.bin.export_json(path)
        self.bin.add_part(Part("Nut", 300, 30, "SupplyHouse"))
        self.bin.export_json(path)
        reloaded = self._load(path)
        self.assertEqual(len(reloaded.items), 4)

    def test_reorder_field_names(self):
        reloaded = self._load(self.bin.export_json_string())
        for item in reloaded.items:
            self.assertEqual(item.reorder_point, item.reorder)
            self.assertEqual(item.supplier, item.supplier)


if __name__ == "__main__":
    unittest.main()
