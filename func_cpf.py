def cpf_number(doc):
    doc=input("Digite seu cpf sem ponto e virgula:")
    if len(doc) == 11:
        return True
    else:
        return False