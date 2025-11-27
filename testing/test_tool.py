import os
import sys
import unittest

# Add parent directory to path to allow importing main modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main.encrypt import Encryptor
from main.decrypt import Decryptor

class TestArPy(unittest.TestCase):
    def setUp(self):
        self.encryptor = Encryptor()
        self.decryptor = Decryptor()
        self.content = "print('Hello, ArPy Testing!')"
        self.methods = [
            'marshal', 'zlib', 'base64', 'base32', 'base16', 
            'lambda', 'bitwise', 'binhex', 'charlen', 'revzlib'
        ]

    def test_encryption_decryption(self):
        print(f"\nOriginal content: {self.content}")
        print("-" * 50)
        
        for method in self.methods:
            with self.subTest(method=method):
                print(f"Testing method: {method}")
                
                # Encrypt
                enc_func = getattr(self.encryptor, f"{method}_enc")
                encrypted = enc_func(self.content)
                
                self.assertIsNotNone(encrypted, f"Encryption failed for {method}")
                self.assertNotEqual(encrypted, self.content, f"Encryption did not change content for {method}")
                print(f"  Encryption successful. Length: {len(encrypted)}")
                
                # Decrypt
                dec_func = getattr(self.decryptor, f"decrypt_{method}")
                decrypted = dec_func(encrypted)
                
                # Handle one-way methods
                if method == 'marshal':
                    self.assertIn("# Bytecode detected", decrypted, "Marshal should return warning message")
                    print(f"  [EXPECTED] Marshal is one-way")
                else:
                    self.assertEqual(decrypted, self.content, f"Decryption failed for {method}")
                    print(f"  [SUCCESS] Decryption successful")
                
                # Test Auto Decrypt
                if method != 'marshal':
                    auto_decrypted = self.decryptor.decrypt_auto(encrypted)
                    self.assertEqual(auto_decrypted, self.content, f"Auto Decryption failed for {method}")
                    print(f"  [SUCCESS] Auto Decryption successful")
                
                print("-" * 50)

if __name__ == "__main__":
    unittest.main()
