import unittest
from app import app

class LoginTokenFormatTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_token_format(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)
        token = response.json['access_token']
        self.assertIsInstance(token, str)
        self.assertTrue(len(token.split('.')) == 3)  # formato JWT: header.payload.signature

if __name__ == '__main__':
    unittest.main()
