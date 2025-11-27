import marshal
import zlib
import base64
import random
import binascii
from tqdm import tqdm

class Encryptor:
    def marshal_enc(self, content, iterations=1):
        try:
            code_obj = compile(content, '<ArPy>', 'exec')
            data = marshal.dumps(code_obj)
            script = f"#Compile By Zidan IDz\nimport marshal\nexec(marshal.loads({repr(data)}))"
            
            for _ in tqdm(range(iterations - 1), desc="Encrypting", unit="iter"):
                code_obj = compile(script, '<ArPy>', 'exec')
                data = marshal.dumps(code_obj)
                script = f"#Compile By Zidan IDz\nimport marshal\nexec(marshal.loads({repr(data)}))"
            return script
        except Exception: return None

    def zlib_enc(self, content, iterations=1):
        try:
            data = zlib.compress(content.encode('utf-8'))
            script = f"#Compile By Zidan IDz\nimport zlib\nexec(zlib.decompress({repr(data)}))"
            
            for _ in tqdm(range(iterations - 1), desc="Encrypting", unit="iter"):
                data = zlib.compress(script.encode('utf-8'))
                script = f"#Compile By Zidan IDz\nimport zlib\nexec(zlib.decompress({repr(data)}))"
            return script
        except Exception: return None

    def base64_enc(self, content, iterations=1):
        try:
            data = base64.b64encode(content.encode('utf-8')).decode()
            script = f"#Compile By Zidan IDz\nimport base64\nexec(base64.b64decode('{data}'))"
            
            for _ in tqdm(range(iterations - 1), desc="Encrypting", unit="iter"):
                data = base64.b64encode(script.encode('utf-8')).decode()
                script = f"#Compile By Zidan IDz\nimport base64\nexec(base64.b64decode('{data}'))"
            return script
        except Exception: return None

    def base32_enc(self, content, iterations=1):
        try:
            data = base64.b32encode(content.encode('utf-8')).decode()
            script = f"#Compile By Zidan IDz\nimport base64\nexec(base64.b32decode('{data}'))"
            
            for _ in tqdm(range(iterations - 1), desc="Encrypting", unit="iter"):
                data = base64.b32encode(script.encode('utf-8')).decode()
                script = f"#Compile By Zidan IDz\nimport base64\nexec(base64.b32decode('{data}'))"
            return script
        except Exception: return None

    def base16_enc(self, content, iterations=1):
        try:
            data = base64.b16encode(content.encode('utf-8')).decode()
            script = f"#Compile By Zidan IDz\nimport base64\nexec(base64.b16decode('{data}'))"
            
            for _ in tqdm(range(iterations - 1), desc="Encrypting", unit="iter"):
                data = base64.b16encode(script.encode('utf-8')).decode()
                script = f"#Compile By Zidan IDz\nimport base64\nexec(base64.b16decode('{data}'))"
            return script
        except Exception: return None

    def lambda_enc(self, content):
        try:
            key = random.randint(1, 255)
            encoded_ints = [ord(c) ^ key for c in content]
            script = (
                f"#Compile By Zidan IDz\n"
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
            script = f"#Compile By Zidan IDz\nexec(''.join({list_str}))"
            return script
        except Exception: return None

    def binhex_enc(self, content):
        try:
            compressed = zlib.compress(content.encode('utf-8'))
            huge_int = int.from_bytes(compressed, byteorder='big')
            script = (
                f"#Compile By Zidan IDz\n"
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
            return f"#Compile By Zidan IDz\nimport marshal\nexec(marshal.loads({repr(data)}))"
        except Exception: return None

    def revzlib_enc(self, content):
        try:
            rev = content[::-1]
            z = zlib.compress(rev.encode('utf-8'))
            b = base64.b64encode(z).decode()
            script = f"import zlib,base64;exec(zlib.decompress(base64.b64decode('{b}')).decode('utf-8')[::-1])"
            return script
        except Exception: return None
