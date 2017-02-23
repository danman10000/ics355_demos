#Demo: Crypt

#Required
#pip install pycrypto
#pip install crcmod

###############################################################
###############################################################
###############################################################
#MD5
import hashlib
print hashlib.md5("whatever your string is").hexdigest()

###############################################################
###############################################################
###############################################################

#Shows the number of key combinations in a readable format
key_size_in_bits=112
"{:,}".format(2**key_size_in_bits)

###############################################################
###############################################################
###############################################################

#DES Example
#http://www.umich.edu/~x509/ssleay/des-weak.html
from Crypto.Cipher import DES
from Crypto import Random
iv = Random.new().read(DES.block_size)
plaintext = b'ICS355 DES Test!' #Multiple of 16

skey="01fe01fe01fe01fe" #8 bytes
key= str(bytearray.fromhex(skey))
cipher = DES.new(key, DES.MODE_OFB, iv)
#msg = iv + cipher.encrypt(plaintext)
msg = cipher.encrypt(plaintext)
msg

skey="ffffffffffffffff"
key= str(bytearray.fromhex(skey))
cipher = DES.new(key, DES.MODE_OFB, iv)
#msg = iv + cipher.encrypt(plaintext)
msg = cipher.encrypt(plaintext)
msg
mydecrypt= cipher.decrypt(msg)
mydecrypt

skey="0000000000000000"
key= str(bytearray.fromhex(skey))
cipher = DES.new(key, DES.MODE_OFB, iv)
#msg = iv + cipher.encrypt(plaintext)
msg = cipher.encrypt(plaintext)
msg
mydecrypt= cipher.decrypt(msg)
mydecrypt


skey="01fe01fe01fe01fe"
key= str(bytearray.fromhex(skey))
cipher = DES.new(key, DES.MODE_OFB, iv)
#msg = iv + cipher.encrypt(plaintext)
msg = cipher.encrypt(plaintext)
msg
mydecrypt= cipher.decrypt(msg)
mydecrypt

###############################################################

#DES Weak Key Example
#Semi-Weak Key Demo based on EK1(EK2(x))=x
#Must use ECB mode for demo
#Reference for keys: http://www.umich.edu/~x509/ssleay/des-weak.html
#Reference http://crypto.stackexchange.com/questions/12214/can-you-explain-weak-keys-for-des
from Crypto.Cipher import DES
from Crypto import Random
iv = Random.new().read(DES.block_size)
plaintext = b'ICS355 DES Test!' #Multiple of 16
desmode=DES.MODE_ECB #[DES.MODE_CBC, DES.MODE_CFB, DES.MODE_ECB, DES.MODE_OFB, DES.MODE_OPENPGP]: #DES.MODE_CTR requires a counter

SemiWeakKeys=[["01FE 01FE 01FE 01FE", "FE01 FE01 FE01 FE01"],
              ["1FE0 1FE0 0EF1 0EF1", "E01F E01F F10E F10E"],
              ["01E0 01E0 01F1 01F1", "E001 E001 F101 F101"],
              ["1FFE 1FFE 0EFE 0EFE", "FE1F FE1F FE0E FE0E"],
              ["011F 011F 010E 010E", "1F01 1F01 0E01 0E01"],
              ["E0FE E0FE F1FE F1FE", "FEE0 FEE0 FEF1 FEF1"]]
for key1,key2 in SemiWeakKeys:
    skey=key1
    key= str(bytearray.fromhex(skey))
    cipher = DES.new(key, desmode, iv)
    #msg = iv + cipher.encrypt(plaintext)
    ctext = cipher.encrypt(plaintext)
    print "Key1:",ctext
    skey=key2
    key= str(bytearray.fromhex(skey))
    cipher = DES.new(key, desmode, iv)
    msg= cipher.encrypt(ctext)
    print "Key2:",msg