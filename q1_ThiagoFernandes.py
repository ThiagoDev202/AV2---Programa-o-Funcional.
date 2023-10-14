clients_2_login = {
    "Manoel": "manoel1@mail.com",
    "Emmanoel": "emmanoel1@mail.com"
}
#Quero mapear os nomes dos clientes/usuários para os seus devidos endereços de e-mail já pré-setados aqui.

login_2_password = {
    "manoel1@mail.com": "123",
    "emmanoel1@mail.com": "1234"
}
#Quero mapeia os endereços de e-mail para as suas devidas senhas já pré-setadas aqui.

login_2_balance = {
    "manoel1@mail.com": 1000.0,
    "emmanoel1@mail.com": 1500.0
}
#Aqui eu já associo o saldo da conta no endereço de e-mail do meu usuário, para facilitar a checagem posteriormentes.

inside = lambda l, p, l2p : l2p[l] == p if l in l2p.keys() else False
#Quero fazer a verificação se o login/senha é válido com base no dicionário que informei acima.

c2l = clients_2_login
l2p = login_2_password
l2b = login_2_balance
#Reduzir as expresões de modo à ser mais prático e funcional durante a codificação do problema.

cl_is_reg = lambda name : (lambda l, p : cl_log_pass(l, p, l2p)) if name in c2l.keys() else "ERROR"
#Autenticação de registro.

cl_log_pass = lambda l, p, l2p : cl_logs_in() if inside(l, p, l2p) else (lambda l2, p2 : cl_log_pass(l2, p2, l2p))
#Realizando o login. Se deu certo, chama cl_logs_in, se não me retorna uma nova expressão lambda para tentar realizar o login novamente.

cl_logs_in = lambda: "SUCCESSFUL LOGIN! SETTINGS DISPLAYED"

withdraw = (
    lambda l, p, amount : withdraw_amount(l, p, amount, l2b)
    if inside(l, p, l2p) and can_withdraw(l, amount, l2b)
    else (lambda l, p, a : "Withdraw not allowed" if not inside(l, p, l2p) else withdraw(l, p, a))
)
#Aqui eu quero realizar um saque. Caso o login seja válido e o saque for permitido, chama o withdraw_amount.
#Caso não, me retorna uma expressão lambda indicando que o saque não é permitido.

withdraw_amount = lambda l, p, amount, l2b : update_balance(l, p, l2b[l] - amount) if can_withdraw(l, amount, l2b) else "Withdraw not allowed"
#Atualiza o saldo da conta se for permitido, se não da erro.

can_withdraw = lambda l, amount, l2b : True if l in l2b and amount <= l2b[l] else False

deposit = lambda l, p, amount : update_balance(l, p, l2b[l] + amount) if inside(l, p, l2p) else "Deposit not allowed"
#Aqui quero realizar um deposito, se o login for válido ele chama o update_balance para atualizar o saldo, se não o depósito não será permitido.

update_balance = lambda l, p, new_balance : f"Balance updated. New balance for {c2l[l]}: {new_balance}" if inside(l, p, l2p) else "Update not allowed"
#Aqui eu quero atualiza o saldo "anterior" e retornar uma mensagem indicando o novo saldo "posterior" à atualização.

start = cl_is_reg
#Iniciar o processo de autenticação de login.

print(start("Manoel")("manoel1@mail.com", "123"))
print(withdraw("Manoel", "manoel1@mail.com", 200))
print(deposit("Manoel", "manoel1@mail.com", 500))
print(withdraw("Manoel", "manoel1@mail.com", 800))



#Significado de algumas expressões usadas durante o código:
#cl = client
#log = login
#reg = registered
#pass = password
#c2l = client to login






