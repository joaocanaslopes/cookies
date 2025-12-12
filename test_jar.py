from jar import Jar          # Importa a classe Jar do ficheiro jar.py
import pytest                # Importa pytest, que permite testar erros facilmente

def test_init():             # Início do teste ao método __init__
    jar = Jar(10)            # Cria um frasco com capacidade 10
    assert jar.capacity == 10    # Verifica se a capacidade guardada é realmente 10
    with pytest.raises(ValueError):  # Testa se ocorre um erro quando a capacidade é inválida
        Jar(-1)              # Criar um frasco com capacidade negativa deve dar erro

def test_str():              # Testa o método __str__
    jar = Jar()              # Cria um frasco com capacidade padrão (12)
    jar.deposit(3)           # Adiciona 3 bolachas ao frasco
    assert str(jar) == "🍪🍪🍪"     # Verifica se a conversão para string mostra 3 bolachas

def test_deposit():          # Testa o método deposit
    jar = Jar(5)             # Cria um frasco com capacidade 5
    jar.deposit(3)           # Adiciona 3 bolachas
    assert jar.size == 3     # Verifica se o size é agora 3
    with pytest.raises(ValueError):  # Testa se depositar mais do que cabe dá erro
        jar.deposit(10)      # Este depósito deve falhar, pois ultrapassa a capacidade

def test_withdraw():         # Testa o método withdraw
    jar = Jar(5)             # Cria um frasco de capacidade 5
    jar.deposit(4)           # Adiciona 4 bolachas
    jar.withdraw(2)          # Retira 2
    assert jar.size == 2     # Agora o frasco deve ter 2 bolachas
    with pytest.raises(ValueError):  # Testa se retirar mais do que existe dá erro
        jar.withdraw(5)      # Tentar retirar 5 bolachas deve falhar
