import re
import base64
import zlib
import marshal
import binascii

class Decryptor:
    def decrypt_auto(self, content):
        """Auto-detect and decrypt known patterns recursively."""
        original = content
        iterations = 0
        max_depth = 50
        
        while iterations < max_depth:
            iterations += 1
            new_content = self._try_decrypt_step(content)
            if new_content == content:
                break
            content = new_content
            
        return content

    def decrypt_marshal(self, content):
        """Decrypt Marshal bytecode."""
        try:
            # Pattern: exec(marshal.loads(b'...'))
            m = re.search(r"exec\(marshal\.loads\((b'.*?')\)\)", content, re.DOTALL)
            if m:
                byte_data = eval(m.group(1))
                code_obj = marshal.loads(byte_data)
                # Cannot decompile bytecode to source easily
                return f"# Bytecode detected (cannot fully decompile)\n# Original: {content[:100]}..."
        except: pass
        return content

    def decrypt_zlib(self, content):
        """Decrypt Zlib compression."""
        try:
            m = re.search(r"exec\(zlib\.decompress\((b'.*?')\)\)", content, re.DOTALL)
            if m:
                byte_data = eval(m.group(1))
                return zlib.decompress(byte_data).decode('utf-8')
        except: pass
        return content

    def decrypt_base64(self, content):
        """Decrypt Base64 encoding."""
        try:
            m = re.search(r"exec\(base64\.b64decode\(['\"]([^'\"]+)['\"]\)\)", content)
            if m:
                return base64.b64decode(m.group(1)).decode('utf-8')
        except: pass
        return content

    def decrypt_base32(self, content):
        """Decrypt Base32 encoding."""
        try:
            m = re.search(r"exec\(base64\.b32decode\(['\"]([^'\"]+)['\"]\)\)", content)
            if m:
                return base64.b32decode(m.group(1)).decode('utf-8')
        except: pass
        return content

    def decrypt_base16(self, content):
        """Decrypt Base16 encoding."""
        try:
            m = re.search(r"exec\(base64\.b16decode\(['\"]([^'\"]+)['\"]\)\)", content)
            if m:
                return base64.b16decode(m.group(1)).decode('utf-8')
        except: pass
        return content

    def decrypt_lambda(self, content):
        """Decrypt Lambda XOR obfuscation."""
        try:
            # Pattern: exec((lambda _, __: ''.join([chr(i ^ __) for i in _]))([...], 0x...))
            m = re.search(r"exec\(\(lambda _, __: ''.join\(\[chr\(i \^ __\) for i in _\]\)\)\((\[.*?\]), (0x[0-9a-fA-F]+)\)\)", content)
            if m:
                encoded_list = eval(m.group(1))
                key = int(m.group(2), 16)
                return ''.join([chr(i ^ key) for i in encoded_list])
        except: pass
        return content

    def decrypt_bitwise(self, content):
        """Decrypt Bitwise boolean arithmetic."""
        try:
            # Pattern: exec(''.join([chr(...), chr(...), ...]))
            # This is complex to reverse, we'll just detect it
            if "chr(True" in content or "chr((True<<" in content:
                return "# Bitwise encoding detected (complex to reverse)\n# Original: " + content[:100] + "..."
        except: pass
        return content

    def decrypt_binhex(self, content):
        """Decrypt BinHex massive integer encoding."""
        try:
            # Pattern: n = <huge_int>\nexec(zlib.decompress(n.to_bytes(...)))
            m = re.search(r"n = (\d+)\s*\nexec\(zlib\.decompress\(n\.to_bytes", content)
            if m:
                huge_int = int(m.group(1))
                compressed = huge_int.to_bytes((huge_int.bit_length() + 7) // 8, 'big')
                return zlib.decompress(compressed).decode('utf-8')
        except: pass
        return content

    def decrypt_charlen(self, content):
        """Decrypt CharLen encoding."""
        try:
            # This is wrapped in marshal, so first try to detect the pattern
            # d=[...] exec(''.join([chr(len(i)) for i in d]))
            if "chr(len(i)) for i in d" in content:
                return "# CharLen encoding detected (wrapped in marshal, cannot fully reverse)\n# Original: " + content[:100] + "..."
        except: pass
        return content

    def decrypt_revzlib(self, content):
        """Decrypt RevZlib (Reverse + Zlib + Base64)."""
        try:
            # Pattern: import zlib,base64;exec(zlib.decompress(base64.b64decode('...')).decode('utf-8')[::-1])
            m = re.search(r"exec\(zlib\.decompress\(base64\.b64decode\(['\"]([^'\"]+)['\"]\)\)\.decode\('utf-8'\)\[::-1\]\)", content)
            if m:
                b = m.group(1)
                z = base64.b64decode(b)
                rev = zlib.decompress(z).decode('utf-8')
                return rev[::-1]
        except: pass
        return content

    def _try_decrypt_step(self, content):
        """Try all decryption methods in sequence."""
        # Try each method
        for method in [
            self.decrypt_base64,
            self.decrypt_base32,
            self.decrypt_base16,
            self.decrypt_zlib,
            self.decrypt_lambda,
            self.decrypt_binhex,
            self.decrypt_revzlib,
        ]:
            result = method(content)
            if result != content:
                return result
        return content
