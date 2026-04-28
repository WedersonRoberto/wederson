#parametros com valor padrão (default)
def saudacao(nome,mensagem="Bem-vindo(a)!"):
    print(f"Olá,{nome}!{mensagem}")

saudacao("Ana") # Olá ,Ana ! Bem-vindo
saudacao("Bob","Bom dia")#Olá Bob ! Bom dia !

    # Argumentos nomeados (keyword args)

def criar_usuario(nome,idade,admim=False):
    print(f"{nome}|{idade} anos | admim={admim}")

criar_usuario(idade=30,nome="Carol")
criar_usuario("Dan",25,admim=True)   

              
              