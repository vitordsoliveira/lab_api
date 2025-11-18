import unittest
from app import app

class ItemsContentTypeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_items_json_response(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIsInstance(response.json, dict)
        self.assertIn('items', response.json)

if __name__ == '__main__':
    unittest.main()
