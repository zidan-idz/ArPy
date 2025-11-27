#!/usr/bin/env python3
"""
ArPy - Python Obfuscation Tool
Author: Zidan IDz
"""

import sys
import os
import argparse
import webbrowser
import codecs
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
from main import __version__, __author__, __github__, __issues__
from main.encrypt import Encryptor
from main.decrypt import Decryptor
from main.utils import read_file, save_file
from main.constants import BANNER
from main.color import success, error, info, warning, Color
from main.features import Features

def main():
    parser = argparse.ArgumentParser(
        prog='ArPy',
        description=f'ArPy - Python Obfuscation Tool v{__version__}',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  python run.py -e base64 -i 5 script.py
  python run.py -e marshal script.py -o output.py
  python run.py -d base64 encrypted.py
  python run.py -d auto encrypted.py
  python run.py --list
  python run.py --report
  python run.py --update

Author: {__author__}
Github: {__github__}
        """
    )
    
    parser.add_argument('-e', '--encrypt', metavar='METHOD', 
                        help='Encryption method (marshal, zlib, base64, base32, base16, lambda, bitwise, binhex, charlen, revzlib)')
    parser.add_argument('-d', '--decrypt', metavar='METHOD',
                        help='Decryption method (same as encrypt + auto)')
    parser.add_argument('-i', '--iterations', type=int, default=1, metavar='N',
                        help='Number of iterations (max 50, default: 1)')
    parser.add_argument('-o', '--output', metavar='FILE',
                        help='Output file path (default: input_enc.py or input_dec.py)')
    parser.add_argument('--list', action='store_true',
                        help='List all available methods')
    parser.add_argument('--report', action='store_true',
                        help='Open GitHub issues page to report bugs')
    parser.add_argument('--update', action='store_true',
                        help='Update the tool to the latest version')
    parser.add_argument('-v', '--version', action='version', 
                        version=f'ArPy v{__version__} by {__author__}')
    parser.add_argument('file', nargs='?', help='Input file to process')
    
    args = parser.parse_args()
    
    # Show banner
    print(BANNER)
    
    # Report bug
    if args.report:
        print(info(f"Opening GitHub issues page..."))
        print(f"{Color.CYAN}{__issues__}{Color.RESET}\n")
        try:
            webbrowser.open(__issues__)
            print(success("Browser opened successfully"))
        except Exception as e:
            print(warning(f"Could not open browser: {e}"))
            print(info(f"Please manually visit: {__issues__}"))
        return
    
    # Update tool
    if args.update:
        Features().update_tool()
        return
    
    # List methods
    if args.list:
        print(f"{Color.CYAN}Available Encryption Methods:{Color.RESET}")
        methods = [
            "marshal    - Compile to bytecode",
            "zlib       - Compress using zlib",
            "base64     - Encode using Base64",
            "base32     - Encode using Base32",
            "base16     - Encode using Base16",
            "lambda     - Lambda + XOR obfuscation",
            "bitwise    - Boolean/Bitwise arithmetic",
            "binhex     - Massive integer encoding",
            "charlen    - Character length encoding",
            "revzlib    - Reverse + Zlib + Base64"
        ]
        for m in methods:
            print(f"  {Color.YELLOW}•{Color.RESET} {m}")
        print(f"\n{Color.CYAN}Decryption Methods:{Color.RESET}")
        print(f"  {Color.YELLOW}•{Color.RESET} All encryption methods + 'auto' (auto-detect)")
        return
    
    # Validate arguments
    if not args.file:
        print(error("No input file specified"))
        parser.print_help()
        sys.exit(1)
    
    if not args.encrypt and not args.decrypt:
        print(error("Must specify either --encrypt or --decrypt"))
        parser.print_help()
        sys.exit(1)
    
    if args.encrypt and args.decrypt:
        print(error("Cannot use both --encrypt and --decrypt"))
        sys.exit(1)
    
    # Check file exists
    if not os.path.isfile(args.file):
        print(error(f"File not found: {args.file}"))
        sys.exit(1)
    
    # Read file
    print(info(f"Reading file: {args.file}"))
    content = read_file(args.file)
    if not content:
        print(error("Could not read file"))
        sys.exit(1)
    
    # Process
    encryptor = Encryptor()
    decryptor = Decryptor()
    result = None
    
    if args.encrypt:
        method = args.encrypt.lower()
        iterations = min(args.iterations, 50)
        
        print(info(f"Encrypting with method: {method} (iterations: {iterations})"))
        
        if method == 'marshal':
            result = encryptor.marshal_enc(content, iterations)
        elif method == 'zlib':
            result = encryptor.zlib_enc(content, iterations)
        elif method == 'base64':
            result = encryptor.base64_enc(content, iterations)
        elif method == 'base32':
            result = encryptor.base32_enc(content, iterations)
        elif method == 'base16':
            result = encryptor.base16_enc(content, iterations)
        elif method == 'lambda':
            result = encryptor.lambda_enc(content)
        elif method == 'bitwise':
            result = encryptor.bitwise_enc(content)
        elif method == 'binhex':
            result = encryptor.binhex_enc(content)
        elif method == 'charlen':
            result = encryptor.charlen_enc(content)
        elif method == 'revzlib':
            result = encryptor.revzlib_enc(content)
        else:
            print(error(f"Unknown encryption method: {method}"))
            print(info("Use --list to see available methods"))
            sys.exit(1)
        
        suffix = "_enc"
    
    elif args.decrypt:
        method = args.decrypt.lower()
        
        print(info(f"Decrypting with method: {method}"))
        
        if method == 'marshal':
            result = decryptor.decrypt_marshal(content)
        elif method == 'zlib':
            result = decryptor.decrypt_zlib(content)
        elif method == 'base64':
            result = decryptor.decrypt_base64(content)
        elif method == 'base32':
            result = decryptor.decrypt_base32(content)
        elif method == 'base16':
            result = decryptor.decrypt_base16(content)
        elif method == 'lambda':
            result = decryptor.decrypt_lambda(content)
        elif method == 'bitwise':
            result = decryptor.decrypt_bitwise(content)
        elif method == 'binhex':
            result = decryptor.decrypt_binhex(content)
        elif method == 'charlen':
            result = decryptor.decrypt_charlen(content)
        elif method == 'revzlib':
            result = decryptor.decrypt_revzlib(content)
        elif method == 'auto':
            result = decryptor.decrypt_auto(content)
        else:
            print(error(f"Unknown decryption method: {method}"))
            print(info("Use --list to see available methods"))
            sys.exit(1)
        
        suffix = "_dec"
    
    # Save result
    if result and result != content:
        if args.output:
            output_path = args.output
        else:
            output_path = save_file(args.file, result, suffix=suffix)
        
        if output_path:
            if not args.output:
                # save_file already saved it
                print(success(f"Saved to: {output_path}"))
            else:
                # Manual save
                try:
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(result)
                    print(success(f"Saved to: {output_path}"))
                except Exception as e:
                    print(error(f"Could not save file: {e}"))
                    sys.exit(1)
        else:
            print(error("Could not save file"))
            sys.exit(1)
    else:
        print(error("Operation failed or no changes detected"))
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{warning('Interrupted by user')}")
        sys.exit(0)
