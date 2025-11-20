import unittest
from app import app 
import werkzeug

if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls): 
        cls.client = app.test_client()
    
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API is running"})

    def test_login(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

    def test_protected_no_token(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"items": ["item1", "item2", "item3"]})

    def test_protected_invalid_token(self):
        headers = {"Authorization": "Bearer invalid_token"}
        response = self.client.get('/protected', headers=headers)
        self.assertIn(response.status_code, [401, 422])

    def test_protected_with_valid_token(self):
        login_response = self.client.post('/login')
        token = login_response.json["access_token"]

        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get('/protected', headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Protected route"})



if __name__ == '__main__':
    unittest.main()