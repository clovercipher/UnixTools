#!/usr/bin/python
__author__ = 'coverton'

import hashlib
from optparse import OptionParser

def md5(file):

    f = open(file,'r')
    content = f.read()
    checksum = hashlib.md5(content).hexdigest()
    f.close()
    return checksum

def compare(hash,checksum):

    match = False
    if hash == checksum:
        match = True
    else:
        match = False
    return match

def main():

    parse = OptionParser()

    parse.add_option("-f", dest="filename", help="File used to calculate hash value")
    parse.add_option("-c", dest="checksum", help="Checksum value")
    (options, args) = parse.parse_args()

    hash = md5(options.filename)
    md5sum = options.checksum
    print "Match: " + str(compare(hash,md5sum))


if __name__=="__main__":
        main()



