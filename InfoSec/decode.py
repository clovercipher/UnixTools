#!/usr/bin/env python
__author__='cl0v3r'
"""
decode.py
Program that will take command line input from a user and decode
or encode the data.
"""
import binascii
from optparse import OptionParser

payload = ''

def decodeHex(h):
    payload = h
    payload = binascii.unhexlify(payload)
    return payload

def decodeBase64(b):
    payload = b
    payload = binascii.b2a_uu(binascii.a2b_base64(payload))
    return payload

def encodeHex(d):
    payload = d
    payload = binascii.hexlify(payload)
    return payload

def encodeBase64(d):
    payload = d
    payload = binascii.b2a_base64(binascii.a2b_uu(payload))
    return payload

def main():
    parser = OptionParser()
    parser.add_option("-d", dest="data", help="Data that needs to be decoded/encoded.")
    parser.add_option("-t", dest="type", help="Type of decoding/encoding.")
    parser.add_option("-e", dest="encode", action="store_true", help="Encode data.")
    (options, args) = parser.parse_args()

    data = str(options.data)
    data = data.replace(' ', '')
    type = options.type
    type = str(type)

    if type=='hex':
        data = decodeHex(data)
    elif type=='base64':
        data = decodeBase64(data)
    elif type=='hex' and options.encode==True:
        data = encodeHex(data)
    elif type=='base64' and options.encode==True:
        data = encodeBase64(data)
    else:
        print "Invalid Type"
        return
    print data

if __name__=='__main__':
    main()