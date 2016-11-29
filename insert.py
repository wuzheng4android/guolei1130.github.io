#!/usr/bin/python
#coding:utf-8
import os
import sys

# print sys.argv[1]
filePath = "./source/_posts/"

filename = sys.argv[1] + ".md";

file = open(filePath + filename,"a");
file.writelines("<Excerpt in index | 首页摘要>\n")
file.writelines("---删除本行，在下面编写内容---")
file.writelines("\r\n\r\n")
file.writelines("---删除本行，在上面编写内容---\n")

file.writelines("+ <!-- more -->\n")
file.writelines("<The rest of contents | 余下全文>\n")