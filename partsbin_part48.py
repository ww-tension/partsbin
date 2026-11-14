# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: PartsBin
import unittest


class TestPartsBinHelpers(unittest.TestCase):

    def setUp(self):
        self.parts = {
            "screw": {"sku": "S001", "name": "Screw", "quantity": 100, "reorder_point": 10, "supplier": "Ace"},
            "bolt": {"sku": "B002", "name": "Bolt", "quantity": 5, "reorder_point": 10, "supplier": "Nuts"},
        }

    def test_add_item(self):
        add_item(self.parts, "bolt", 5)
        self.assertEqual(self.parts["bolt"]["quantity"], 10)

    def test_add_new_item(self):
        add_item(self.parts, "wire", 3)
        self.assertEqual(self.parts["wire"]["quantity"], 3)

    def test_add_existing_item(self):
        add_item(self.parts, "screw", 10)
        self.assertEqual(self.parts["screw"]["quantity"], 110)

    def test_add_invalid_quantity(self):
        with self.assertRaises(ValueError):
            add_item(self.parts, "screw", -1)

    def test_add_invalid_supplier(self):
        with self.assertRaises(ValueError):
            add_item(self.parts, "screw", 1, supplier="Ghost")

    def test_remove_item(self):
        remove_item(self.parts, "bolt")
        self.assertNotIn("bolt", self.parts)

    def test_remove_missing_item(self):
        remove_item(self.parts, "wire")
        self.assertIn("wire", self.parts)

    def test_is_reorder_needed(self):
        self.assertTrue(is_reorder_needed(self.parts["bolt"]))
        self.assertFalse(is_reorder_needed(self.parts["screw"]))

    def test_is_supplier_available(self):
        self.assertTrue(is_supplier_available(self.parts["bolt"]["supplier"]))
        self.assertFalse(is_supplier_available("Ghost"))

    def test_get_supplier(self):
        self.assertEqual(get_supplier("S001"), "Ace")
        self.assertIsNone(get_supplier("X000"))


if __name__ == "__main__":
    unittest.main()
