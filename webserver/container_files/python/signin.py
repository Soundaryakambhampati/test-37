#!/usr/bin/python

import cgi
import MySQLdb
from hashlib import sha256

form = cgi.FieldStorage()

print('Content-Type: text/html\r\n')

conn = MySQLdb.connect(host="database", user="root", passwd="MEEP1234", db="webdata")
cursor = conn.cursor()

username = form.getvalue('username')
password = sha256(str(form.getvalue('password'))).hexdigest()

cursor.execute('select `UID`, `Password` from `User Store` where `UID` = "{}"'.format(username))

ret = cursor.fetchall()

if len(ret) == 0:
	print('Failed')
else:
	user = ret[0][0]
	passwd = ret[0][1]
	if passwd != password or user != username:
		print('Failed')
	else:
		print('Success')
