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

def criar_perfil(nome,idade,cidade):
    print(f"{nome}, {idade} anos, {cidade}")
criar_perfil(cidade="Curitiba" , nome="Julia" , idade=25)
# Julia , 25 anos ,Curitiba - funciona independente da ordem !    

              
              