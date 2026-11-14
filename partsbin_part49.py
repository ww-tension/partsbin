# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: PartsBin
def setUp(self):
    self.bin = {'name': 'Screws', 'qty': 5, 'reorder': 10, 'supplier': 'Acme'}
    self.store = {'Screws': self.bin}

def test_delete_missing_raises(self):
    with self.assertRaises(KeyError):
        delete_item(self.store, 'Nope')

def test_update_missing_raises(self):
    with self.assertRaises(KeyError):
        update_item(self.store, 'Nope', qty=1)

def test_update_zero_qty(self):
    update_item(self.store, 'Screws', qty=0)
    self.assertEqual(self.store['Screws']['qty'], 0)

def test_update_reorder_below_qty(self):
    update_item(self.store, 'Screws', reorder=3)
    self.assertEqual(self.store['Screws']['reorder'], 3)

def test_delete_removes_key(self):
    delete_item(self.store, 'Screws')
    self.assertNotIn('Screws', self.store)

def test_update_preserves_supplier(self):
    update_item(self.store, 'Screws', qty=99)
    self.assertEqual(self.store['Screws']['supplier'], 'Acme')
