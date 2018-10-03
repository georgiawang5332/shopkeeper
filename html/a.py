#!/usr/bin/env python
import cgi,cgitb,os,sys,json,base64
import random
import io
import requests
from datetime import datetime
import traceback
cgitb.enable()
print "Content-type: text/html; charset=utf-8"
print "\r\n\r\n"

ss=""

s=open("webone/shopkeeper/html/02_index.html").read()
ss+=s

s=open("webone/shopkeeper/html/01_menu.html").read()
ss+=s

s=open("webone/shopkeeper/html/02_body.html").read()
ss+=s

s=open("webone/shopkeeper/html/01_footer.html").read()
ss+=s

print ss