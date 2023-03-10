import pandas as pd




class data_Set():
    def __init__(self, arquivo):
        self.arquivo = arquivo
        pass

    # Ler o arquivo csv
    def ler_arquivo(self):
        tabela = pd.read_csv(self.arquivo)
        return tabela
    

    # Retorna o pokemon com maior poder de ataque
    def pokemon_maior_ataque(self):
        tabela = pd.read_csv(self.arquivo)
        id_com_maior_valor = tabela['attack'].idxmax()
        resultado = tabela.loc[id_com_maior_valor]
        return f"O pokemon com maior poder de ataque é {resultado['name']} com {resultado['attack']} pontos."
    
    # Retorna o pokemon com menor poder de ataque
    def pokemon_menor_ataque(self):
        tabela = pd.read_csv(self.arquivo)
        id_com_maior_valor = tabela['attack'].idxmin()
        resultado = tabela.loc[id_com_maior_valor]
        return f"O pokemon com menor poder de ataque é {resultado['name']} com {resultado['attack']} pontos."

    # Retorna o pokemon com a maior pontuação em defesa
    def pokemon_maior_defesa(self):
        tabela = pd.read_csv(self.arquivo)
        id_com_maior_valor = tabela['defense'].idxmax()
        resultado = tabela.loc[id_com_maior_valor]
        return f"O pokemon com maior quantidade de pontos em defesa é {resultado['name']} com {resultado['attack']} pontos."


    # Retorna o pokemon com a menor pontuação em defesa
    def pokemon_menor_defesa(self):
        tabela = pd.read_csv(self.arquivo)
        id_com_maior_valor = tabela['defense'].idxmin()
        resultado = tabela.loc[id_com_maior_valor]
        return f"O pokemon com menor quantidade de pontos em defesa é {resultado['name']} com {resultado['attack']} pontos."
    
    #Retorna o pokemon com a maior pontuação geral
    def pokemon_superior(self):
        tabela = pd.read_csv(self.arquivo)
        id_com_maior_valor = tabela['total'].idxmax()
        resultado = tabela.loc[id_com_maior_valor]
        return f"O Pokemon mais forte é {resultado['name']} com {resultado['total']} de poder."   

    #Retorna o pokemon com a menor pontuação geral
    def pokemon_inferior(self):
        tabela = pd.read_csv(self.arquivo)
        id_com_maior_valor = tabela['total'].idxmin()
        resultado = tabela.loc[id_com_maior_valor]
        return f"O Pokemon mais fraco é {resultado['name']} com {resultado['total']} de poder." 
    
    #Retorna o pokemon mais rápido
    def pokemon_mais_rapido(self):
        tabela = pd.read_csv(self.arquivo)
        id_com_maior_valor = tabela['speed'].idxmax()
        resultado = tabela.loc[id_com_maior_valor]
        return f"O Pokemon mais rapido é {resultado['name']} com {resultado['total']} de speed." 

data_sets = data_Set('pokemon.csv')
print(data_sets.ler_arquivo())
print(data_sets.pokemon_maior_ataque())
print(data_sets.pokemon_menor_ataque())
print(data_sets.pokemon_maior_defesa())
print(data_sets.pokemon_menor_defesa())
print(data_sets.pokemon_superior())
print(data_sets.pokemon_inferior())
print(data_sets.pokemon_mais_rapido())