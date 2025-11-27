import marshal
import zlib
import base64
import random
import binascii
from tqdm import tqdm

class Encryptor:
    def marshal_enc(self, content, iterations=1):
        try:
            script = content
            for _ in tqdm(range(iterations), desc="Encrypting", unit="iter"):
                code_obj = compile(script, '<ArPy>', 'exec')
                data = marshal.dumps(code_obj)
                script = f"# ArPy Encrypted: MARSHAL\nimport marshal\nexec(marshal.loads({repr(data)}))"
            return script
        except Exception: return None

    def zlib_enc(self, content, iterations=1):
        try:
            script = content
            for _ in tqdm(range(iterations), desc="Encrypting", unit="iter"):
                data = zlib.compress(script.encode('utf-8'))
                script = f"# ArPy Encrypted: ZLIB\nimport zlib\nexec(zlib.decompress({repr(data)}))"
            return script
        except Exception: return None

    def base64_enc(self, content, iterations=1):
        try:
            script = content
            for _ in tqdm(range(iterations), desc="Encrypting", unit="iter"):
                data = base64.b64encode(script.encode('utf-8')).decode()
                script = f"# ArPy Encrypted: BASE64\nimport base64\nexec(base64.b64decode('{data}'))"
            return script
        except Exception: return None

    def base32_enc(self, content, iterations=1):
        try:
            script = content
            for _ in tqdm(range(iterations), desc="Encrypting", unit="iter"):
                data = base64.b32encode(script.encode('utf-8')).decode()
                script = f"# ArPy Encrypted: BASE32\nimport base64\nexec(base64.b32decode('{data}'))"
            return script
        except Exception: return None

    def base16_enc(self, content, iterations=1):
        try:
            script = content
            for _ in tqdm(range(iterations), desc="Encrypting", unit="iter"):
                data = base64.b16encode(script.encode('utf-8')).decode()
                script = f"# ArPy Encrypted: BASE16\nimport base64\nexec(base64.b16decode('{data}'))"
            return script
        except Exception: return None

    def lambda_enc(self, content):
        try:
            key = random.randint(1, 255)
            encoded_ints = [ord(c) ^ key for c in content]
            script = (
                f"# ArPy Encrypted: LAMBDA\n"
                f"exec((lambda _, __: ''.join([chr(i ^ __) for i in _]))"
                f"({encoded_ints}, {hex(key)}))"
            )
            return script
        except Exception: return None

    def bitwise_enc(self, content):
        try:
            encoded_chars = []
            for char in tqdm(content, desc="Encoding", unit="char"):
                val = ord(char)
                parts = []
                for i in range(8):
                    if (val >> i) & 1:
                        if i == 0: parts.append("(True)")
                        else: parts.append(f"(True<<{i})")
                expr = "+".join(parts)
                encoded_chars.append(f"chr({expr})")
            list_str = "[" + ",".join(encoded_chars) + "]"
            list_str = "[" + ",".join(encoded_chars) + "]"
            script = f"# ArPy Encrypted: BITWISE\nexec(''.join({list_str}))"
            return script
        except Exception: return None

    def binhex_enc(self, content):
        try:
            compressed = zlib.compress(content.encode('utf-8'))
            huge_int = int.from_bytes(compressed, byteorder='big')
            script = (
                f"# ArPy Encrypted: BINHEX\n"
                f"import zlib\n"
                f"n = {huge_int}\n"
                f"exec(zlib.decompress(n.to_bytes((n.bit_length() + 7) // 8, 'big')))"
            )
            return script
        except Exception: return None

    def charlen_enc(self, content):
        try:
            encoded_chars = []
            for char in tqdm(content, desc="Encoding", unit="char"):
                encoded_chars.append('n' * ord(char))
            
            script = f"d={encoded_chars}\nexec(''.join([chr(len(i)) for i in d]))"
            code_obj = compile(script, '<ArPy>', 'exec')
            data = marshal.dumps(code_obj)
            return f"# ArPy Encrypted: CHARLEN\nimport marshal\nexec(marshal.loads({repr(data)}))"
        except Exception: return None

    def revzlib_enc(self, content):
        try:
            rev = content[::-1]
            z = zlib.compress(rev.encode('utf-8'))
            b = base64.b64encode(z).decode()
            script = f"# ArPy Encrypted: REVZLIB\nimport zlib,base64;exec(zlib.decompress(base64.b64decode('{b}')).decode('utf-8')[::-1])"
            return script
        except Exception: return None
