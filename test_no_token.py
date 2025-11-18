import unittest
from app import app

class ProtectedNoTokenTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_protected_no_token(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)

    def test_protected_invalid_token(self):
        response = self.client.get(
            '/protected',
            headers={"Authorization": "Bearer invalidtoken"}
        )
        self.assertEqual(response.status_code, 422)  # JWT inválido

if __name__ == '__main__':
    unittest.main()
