

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import requests
import cgi


form = cgi.FieldStorage()
login = form.getvalue("Usuario")
senha = form.getvalue("Senha")

urls = { "token":"https://suap.ifrn.edu.br/api/v2/autenticacao/token/",
         "dados":"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"}


autenticacao = {
    "username": login,
    "password": senha
}


def getToken():
    response = requests.post(urls['token'], data=autenticacao)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))['token']
    return None

token = getToken()
cabecalho={'Authorization': 'JWT {0}'.format(token)}

def getInformacoes():
    response = requests.get(urls['dados'], headers=cabecalho)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None

if token == None:

	print("Content-type:text/html\n\n")
	print(" Tente Novamente! ")
	

else:

	informacoes = json.loads(getInformacoes())

	nome = informacoes['vinculo']['nome']
	nome_format = ""

	for i in nome:

		if i == 'á' :i='a'
		if i == 'é' :i='e'
		if i == 'í' :i='i'
		if i == 'ó' :i='o'
		if i == 'ú' :i='u'
		if i == 'à' :i='a'
		if i == 'â' :i='a'
		if i == 'ê' :i='e'
		if i == 'ô' :i='o'
		nome_format += i
		


	print("Content-type:text/html\n\n")
	print("<html>")
	print("<head>")
	print('<h2 style="color:white;"> <center>') 
	print("Seus Dados ")
	print(" </center> </h2>")
	print("<title>Dados-SUAP</title>")
	print("<meta charset='utf-8'>")
	print("<style type='text/css'>")
	print('body{background-image: url("https://elemento79.com.br/wp-content/uploads/2013/12/seamless-gold-greek-key-background-pattern-vector-1195683.jpg")')
	print("</style>")
	print("</head>")
	print("<body>")
	print("<section>")
	print("<fieldset id='field'>")
	print("<fieldset id='field2'>")

	if informacoes['tipo_vinculo'] == 'Aluno':
		print("<img src='https://suap.ifrn.edu.br{}' hspace='5' style='float:left;' width='90' height='120'/>".format(informacoes['url_foto_75x100']))
		print('<div id = "texto" style="color:white;">')
		print("Nome: <lib>{}</lib><br>".format(nome_format))
		print("Matricula: <lib>{}</lib><br>".format(informacoes['matricula']))
		print("Email: <lib>{}</lib><br>".format(informacoes['email']))
		print("Situacao: <lib>{}</lib><br>".format(informacoes['vinculo']['situacao']))
		print("Curso: <lib>{}</lib><br>".format(informacoes['vinculo']['curso']))
		print("Campus: <lib>{}</lib><br>".format(informacoes['vinculo']['campus']))
		print("Vinculo: <lib>{}</lib><br>".format(informacoes['tipo_vinculo']))
		print("<form action='banco_teste.py' method='post'>")
		print("<input type='hidden' id='nome' name='nome' value='{}'>".format(nome_format))
		print("<input type='hidden' id='matricula' name='matricula' value='{}'>".format(informacoes['matricula']))
		print("<input type='hidden' id='email' name='email' value='{}'>".format(informacoes['email']))
		print("<input type='hidden' id='situacao' name='situacao' value='{}'>".format(informacoes['vinculo']['situacao']))
		print("<input type='hidden' id='curso' name='curso' value='{}'>".format(informacoes['vinculo']['curso']))
		print("<input type='hidden' id='campus' name='campus' value='{}'>".format(informacoes['vinculo']['campus']))
		print("<input type='hidden' id='tipo_vinculo' name='tipo_vinculo' value='{}'>".format(informacoes['tipo_vinculo']))
		print("</br> <center><input type='submit' value='Savar no banco de dados'></center>")
		print("</form>")
		print('</div>')

	else:
		print("<img src='https://suap.ifrn.edu.br{}' hspace='5' style='float:left;' width='90' height='120'/>".format(informacoes['url_foto_75x100']))
		print('<div id = "texto" style="color:white;">')
		print("Nome: <lib>{}</lib><br>".format(nome_form))
		print("Matricula: <lib>{}</lib><br>".format(informacoes['vinculo']['matricula']))
		print("Email: <lib>{}</lib><br>".format(informacoes['email']))
		print("Campus: <lib>{}</lib><br>".format(informacoes['vinculo']['campus']))
		print("Diretoria: <lib>{}</lib><br>".format(informacoes['vinculo']['setor_suap']))
		print("Disciplina: <lib>{}</lib><br>".format(disciplina_form))
		print("<form action='banco_teste.py' method='post'>")
		print("<input type='hidden' id='nome' name='nome' value='{}'>".format(nome_form))
		print("<input type='hidden' id='matricula' name='matricula' value='{}'>".format(informacoes['vinculo']['matricula']))
		print("<input type='hidden' id='email' name='email' value='{}'>".format(informacoes['email']))
		print("<input type='hidden' id='campus' name='campus' value='{}'>".format(informacoes['vinculo']['campus']))
		print("<input type='hidden' id='diretoria' name='diretoria' value='{}'>".format(informacoes['vinculo']['setor_suap']))
		print("<input type='hidden' id='disciplina' name='disciplina' value='{}'>".format(disciplina_form))
		print("</br> <center><input type='submit' value='Savar no banco de dados'></center>")
		print("</form>")
		print('</div>')



	print("</fieldset>")
	print("</fieldset>")
	print("</section>")
	print("</body></html>")


