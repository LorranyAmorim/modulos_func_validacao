import random
import func_cpf

senha_gerador=()
senha=()
nome=()
opcao=()
cpf=()

def get_nome(n):
    n=input("Digite seu nome:")
    if n == str and n != " ":
        return True
    else:
        return False 

def gerar(resposta):
    resposta=random.randint(0, 100)
    return resposta

def menu_principal ():
    print("========================")
    print("SISTEMA HOSPITALAR")
    print("ESCOLHA UMA OPÇÃO ABAIXO")
    print("1-Atendimento prioritário")
    print("2-Atendimento normal")
    print("3-Urgência/Emergência")



menu_principal()

while opcao != 9:
    opcao=input("Digite a opção desejada Ou digite 9 para sair:")
    
    try:
        opcao = int (opcao)

        if opcao == 1:
            get_nome(nome)
            cpf_documento=func_cpf.cpf_number(cpf) 

            if nome == False or cpf == False:
                 print("dados incorretos")
                 
               
            else:
                senha_gerador=gerar(senha)
                print("Sua senha de atendimento é:",senha_gerador)
            break

               
    
    except:
        print("Formato da opção é inválido")
    
      
   



