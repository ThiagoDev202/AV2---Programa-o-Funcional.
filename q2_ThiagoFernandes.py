from flask import Flask, request

app = Flask(__name__)

read_users = lambda : dict(line.strip().split(",") for line in open("usuarios.txt").readlines())
#Aqui eu quero ler um arquivo txt com as informações do usuário. Formatando-o com "," para separar-lo em pares chave-valor.

check_credentials = lambda login, password, users : users.get(login) == password
#Aqui eu quero verificar se as informações do usuário é igual as informações que eu armazenei no arquivo .txt

users = read_users()

reqresp = (
    lambda : 'SUCESSO' if check_credentials(request.form["username"], request.form["password"], users) else 'FRACASSO'
) if request.method == 'POST' else None
#Se o método da requisição for POST, ela verifica as credenciais usando check_credentials e retorna 'SUCESSO' ou 'FRACASSO' com base no resultado.
#Caso contrário, reqresp é definido como None.

app.add_url_rule('/index/', 'index', reqresp, methods=['POST'])
(lambda : (app.run(host='0.0.0.0', port=8080) if __name__ == '__main__' else None))()
#app.run(host='0.0.0.0', port=8080)

#OBS: Tenha primeiramente o arquivo .txt com a informação de log para poder executar o código.

#Código do arquivo usuarios.txt:
#sam2584,123
#robs61286,1234

#Código do arquivo index.html:
#<!DOCTYPE html>
#<html>
#<head>
#<title>Login Page</title>
#</head>
#<body>
#<h1>Login</h1>
#<form method="POST">
#<label for="username">Username:</label>
#<input type="text" id="username" name="username" required><br><br>
#<label for="password">Password:</label>
#<input type="password" id="password" name="password" required><br><br>
#<input type="submit" value="Login">
#</form>
#</body>
#</html>


