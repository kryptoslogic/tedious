#!/usr/bin/python3

"""
This can be used to decrypt and view config files

Note: this script contains Paterva proprietary keys! Not for redistribution...

Example usage:
python3 ./config_fs_crypt.py d < ~/.maltego/v4.1.13/config/Maltego/Servers/paterva\ public.tas 
"""

import glob
import os.path
import sys
from Crypto.Cipher import DES3

CONFIG_BASE = glob.glob(os.path.expanduser("~/.maltego/*/config"))[0]
KEY_SEED = b"0nsblYkwEgniNimeld1sleke"
IV_SEED = b"b0l@amBr"


# Military-grade key obfuscation
def generate_bytes(length, seed):
	seed = CONFIG_BASE.encode() + seed
	key = bytearray(length)
	for i, x in enumerate(seed):
		key[i%length] ^= x
	return bytes(key)


def unpad(data): # super naive implementation of PKCS5
	return data[:-data[-1]]


def pad(data):
	padlen = 8-(len(data)%8)
	return data + bytes([padlen]*padlen)


def usage():
	print("USAGE: python3 {} [e]ncrypt/[d]ecrypt <input_file >output_file".format(sys.argv[0]))
	print(__doc__)
	exit()


if len(sys.argv) != 2:
	usage()

data = sys.stdin.buffer.read()
key = generate_bytes(24, KEY_SEED)
iv = generate_bytes(8, IV_SEED)
des = DES3.new(key, DES3.MODE_CBC, iv)

if sys.argv[1].lower() in ["e", "encrypt"]:
	sys.stdout.buffer.write(des.encrypt(pad(data)))
elif sys.argv[1].lower() in ["d", "decrypt"]:
	sys.stdout.buffer.write(unpad(des.decrypt(data)))
else:
	usage()
