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
            m = re.search(r"exec\(''\.join\((\[.*?\])\)\)", content, re.DOTALL)
            if m:
                # We can safely eval this because we know it's just a list of chr(math)
                # produced by our encryptor
                list_str = m.group(1)
                # Basic validation to ensure it looks like our output
                if "chr(" in list_str and "True" in list_str:
                    decoded_list = eval(list_str)
                    return "".join(decoded_list)
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
            # Check for marker
            if "# ArPy Encrypted: CHARLEN" in content:
                # Extract the marshalled data
                m = re.search(r"exec\(marshal\.loads\((b'.*?')\)\)", content, re.DOTALL)
                if m:
                    byte_data = eval(m.group(1))
                    code_obj = marshal.loads(byte_data)
                    
                    # Inspect constants for the 'n' strings
                    found_strings = []
                    for const in code_obj.co_consts:
                        if isinstance(const, tuple):
                             for item in const:
                                 if isinstance(item, str) and set(item) == {'n'}:
                                     found_strings.append(item)
                        elif isinstance(const, str) and set(const) == {'n'} and len(const) > 0:
                            found_strings.append(const)
                    
                    if found_strings:
                        return "".join([chr(len(s)) for s in found_strings])
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
        """Try to decrypt based on marker or try all methods."""
        # Check for marker
        m = re.match(r"# ArPy Encrypted: ([A-Z0-9]+)", content)
        if m:
            method_name = m.group(1).lower()
            if method_name == 'marshal': return self.decrypt_marshal(content)
            elif method_name == 'zlib': return self.decrypt_zlib(content)
            elif method_name == 'base64': return self.decrypt_base64(content)
            elif method_name == 'base32': return self.decrypt_base32(content)
            elif method_name == 'base16': return self.decrypt_base16(content)
            elif method_name == 'lambda': return self.decrypt_lambda(content)
            elif method_name == 'bitwise': return self.decrypt_bitwise(content)
            elif method_name == 'binhex': return self.decrypt_binhex(content)
            elif method_name == 'charlen': return self.decrypt_charlen(content)
            elif method_name == 'revzlib': return self.decrypt_revzlib(content)
        
        # Fallback to trying all methods
        for method in [
            self.decrypt_base64,
            self.decrypt_base32,
            self.decrypt_base16,
            self.decrypt_zlib,
            self.decrypt_lambda,
            self.decrypt_binhex,
            self.decrypt_revzlib,
            self.decrypt_marshal, # Added marshal to fallback
        ]:
            result = method(content)
            if result != content:
                return result
        return content
