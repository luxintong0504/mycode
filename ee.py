#!/usr/bin/python3
# -*- coding:utf-8 -*-

import codecs
import sys

if len(sys.argv) > 1:
    FILE=sys.argv[1]
else:
    FILE="harry-potter.txt"

fp = codecs.open(FILE, 'r', 'gb18030')
texts = fp.read()
fp.close()

print(texts)
a = open("hahaha.txt","w")
a.write(texts)