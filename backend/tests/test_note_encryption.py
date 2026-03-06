import unittest
from backend.notes.encryption import encrypt, decrypt

class TestEncryption(unittest.TestCase):
    def test_roundtrip(self):
        original = 'Secret message 123!'
        token = encrypt(original)
        self.assertIsInstance(token, str)
        recovered = decrypt(token)
        self.assertEqual(original, recovered)

if __name__ == '__main__':
    unittest.main()
