Ref_Arquivo= open("/Users/Win 10/Downloads/TcCLB.506717.80.fasta") #Abre o arquivo fazendo uma associacao com Ref_Arquivo
Arquivo_fasta= Ref_Arquivo.read() # le o arquivo
print("Arquivo Original: " "\n"+Arquivo_fasta) #Arquivo sem o tratamento. Linha desnecessaria
cabecalho= Arquivo_fasta.split('\n')[0][1:] # [0] primeira linha / [1:] esta comecando da segunda coluna para ignorar o ">" e indo ate o final. O metodo .split fragmenta a string
sequencia= ''.join(Arquivo_fasta.split('\n')[1:]) # [1:]Segunda linha indo ate o final. Join esta juntando os fragmentos de string
print("Identificador: %s"%cabecalho) # tabulacao %s"% fica bom, mas nao sei como funciona
print(sequencia)
print("Tamanho da sequencia: %s"%len(sequencia)) # funcao len() retorna comprimento de um string ou lista
Ref_Arquivo.close() # bom fechar o arquivo que foi executado
