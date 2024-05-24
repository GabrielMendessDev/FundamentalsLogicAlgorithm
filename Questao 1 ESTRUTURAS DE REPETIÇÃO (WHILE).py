senha=(input("Digite a senha:"))
senha_correta='20p@ssword21'

while(senha!=senha_correta):
    print("Senha incorreta!")
    print("-")
    senha=(input("Digite a senha novamente:"))
else:
    print("-")
    print("Acesso concedido.")
