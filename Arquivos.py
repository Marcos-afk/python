arquivo = open("palavras.txt" , "w")
arquivo.write('banana \n ')
arquivo.write('melancia \n ')
arquivo.write('manga \n ')
arquivo.close()

arquivo = open("palavras.txt" ,"r")
palavras = []
for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)
arquivo.close()
