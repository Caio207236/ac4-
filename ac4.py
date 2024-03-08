def ler_nome():


    return input("seu nome")


def ler_notas()
    
    ap1 = float (input("nota da ap1"))
    ap2 = float (input("nota da ap2"))
    asub = float (input("as"))
    ac = float (input(ac))
    return ap1, ap2, asub, ac

def analisar_substituição (ap1, ap2, ac)
       
       if asub > ap1 and sub > ap2:
            prova1 = azub

        else: prova1 = ap1 
       
if prova1 > ap2:
    prova2 = ap2 
else: 
     prova2 = prova1

     return prova1, prova2

def calcular_media(ap1, ap2, asub, ac):
    prova1, prova2 = analisar_substituicao (ap1, ap2, asub)
    media = (prova1 + prova2) * 0.4 + ac * 0.2
    return media 
def aluno_foi_aprovado(media):
   
    if media >= 7:
        return True
    else:
        return False

def notas_sao_validas(ap1, ap2, asub, ac):
    
    if (ap1 >= 0 and ap1 <= 10) and (ap2 >= 0 and ap2 <= 10) and (asub >= 0 and asub <= 10) and (ac >= 0 and ac <= 10):
        return True
    else:
        return False

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = calcular_media(ap1, ap2, asub, ac)
