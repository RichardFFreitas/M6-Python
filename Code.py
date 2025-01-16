
class ArquivoTexto:
    def __init__(self, arquivo: str):
        """Inicializa a classe e preenche o atributo `self.conteudo` como uma lista de linhas do arquivo."""
        self.arquivo = arquivo
        self.conteudo = []  # Inicialmente uma lista vazia
        self.extrair_conteudo()  # Preenche `self.conteudo`

    def extrair_conteudo(self):
        """Lê o conteúdo do arquivo e preenche o atributo `self.conteudo`."""
        try:
            with open(self.arquivo, mode='r', encoding='utf8') as file:
                # Preenche a lista `self.conteudo` com cada linha do arquivo
                self.conteudo = [linha for linha in file.readlines()]
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.arquivo}' não encontrado.")
            self.conteudo = []

    def extrair_linha(self, numero_linha: int):
        """Retorna o conteúdo da linha especificada (primeira linha é 1)."""
        # Ajusta o índice porque o número da linha começa em 1
        indice = numero_linha - 1
        if 0 <= indice < len(self.conteudo):
            return self.conteudo[indice]
        else:
            return f"Erro: Linha {numero_linha} não existe no conteúdo do arquivo."


# Testando a classe
arquivo_texto = ArquivoTexto(arquivo='/data/musica.txt')

# Verificando o tamanho da lista
print(f"Tamanho da lista: {len(arquivo_texto.conteudo)}")  # Deve ser 28 ou 29

# Exibindo o conteúdo da lista para verificar
print(arquivo_texto.conteudo)

# Testando a extração de linhas
print(arquivo_texto.extrair_linha(1))  # Deve retornar a primeira linha
print(arquivo_texto.extrair_linha(len(arquivo_texto.conteudo)))  # Deve retornar a última linha
print(arquivo_texto.extrair_linha(30))  # Deve retornar mensagem de erro

