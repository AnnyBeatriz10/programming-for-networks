

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import psycopg2
import cgi

form = cgi.FieldStorage()

nome = form.getvalue("nome")
matricula = form.getvalue("matricula")
email = form.getvalue("email")
situacao = form.getvalue("situacao")
curso = form.getvalue("curso")
campus = form.getvalue("campus")

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect("dbname=postgres user=postgres host=127.0.0.1 password=123")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cria_database = ("CREATE DATABASE aluno;")
cur.execute(cria_database)
conn.close()
cur.close()

conn = psycopg2.connect("dbname=aluno user=postgres host=127.0.0.1 password=123")
cur = conn.cursor()
cria_tab = """ 
          CREATE TABLE dados(
		nome varchar(100) not null, 
		matricula int primary key not null unique,
		email varchar(100) not null,
		situacao char(30) not null,
		curso varchar(200) not null,
		campus varchar(200) not null
		);"""
cur.execute(cria_tab)
conn.commit()
conn.close()
cur.close()

inserindo = ("INSERT INTO dados(nome,matricula,email,situacao,curso,campus) Values ('{}','{}','{}','{}','{}','{}') ".format(nome,matricula,email,situacao.curso,campus))
cur.execute(inserindo)
conn.commit()



print("Content-type:text/html\n\n")
print("<html>")
print("<head>")
print("</head>")
print("<body><h1>Banco</h1></body>")
print("</html>")



