class Jar:             # Define a classe Jar
    def __init__(self, capacity=12):                 # Construtor, recebe capacidade opcional
        if not isinstance(capacity, int) or capacity < 0:  # Verifica se capacity é int não negativo
            raise ValueError("Capacity must be a non-negative int")  # Se não for, lança erro
        self._capacity = capacity      # Guarda a capacidade internamente
        self._cookies = 0              # Começa com 0 bolachas no frasco

    def __str__(self):                 # Método especial para converter o jar em string
        return "🍪" * self._cookies    # Devolve um número de emojis igual ao número de bolachas

    def deposit(self, n):              # Método para adicionar n bolachas
        if self._cookies + n > self._capacity:   # Se ultrapassar a capacidade
            raise ValueError("Too many cookies") # Lança erro
        self._cookies += n             # Caso contrário, adiciona as bolachas

    def withdraw(self, n):             # Método para remover n bolachas
        if n > self._cookies:          # Se tentar remover mais do que existe
            raise ValueError("Not enough cookies")   # Lança erro
        self._cookies -= n             # Caso contrário, retira as bolachas

    @property                          # Torna capacity um atributo de leitura
    def capacity(self):                # Devolve a capacidade máxima
        return self._capacity

    @property                          # Torna size um atributo de leitura
    def size(self):                    # Devolve o número atual de bolachas
        return self._cookies
