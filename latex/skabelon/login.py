import cgi, cgitb, random

cgitb.enable()

print "Content-type: text/html; charset=utf-8"


# Dette er eksempelkode til inkludering i LaTeX og IKKE et rigtigt program OG dette er i øvrigt en meget meget meget lang linje


navn   = "foobar"
passwd = "snake"


import sqlite3
conn = sqlite3.connect("foobar.db")
cursor = conn.cursor()


conn.execute('SELECT * FROM brugere WHERE brugernavn = ? AND adgangskode = ?', (navn, adgangskode))

for row in cursor.fetchall():
  print row
