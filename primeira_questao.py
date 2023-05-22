"""
O seguinte algoritmo tem como objetivo simular um autômato finito que seja capaz de validar se uma cadeia é aceita ou rejeitada.
"""
class Automato:
  """
  Classe Automato responsável por instanciar automatos que reconheçam a cadeia informada.
  """
  def __init__(self, estados, alfabeto, transicoes, estadoInicial, estadosFinais): # Método para inicialização da classe
    """
    Inicializa a classe Automato.

    Atributos:
      - estados: Uma lista de estados possíveis para o autômato.
      - alfabeto: Uma lista de símbolos que formam o alfabeto reconhecido pelo autômato.
      - transicoes: Um dicionário que define as transições permitidas entre os estados do autômato.
      - estadoInicial: O estado inicial do autômato.
      - estadosFinais: Uma lista de estados finais do autômato, representando a aceitação da palavra.
    """
    self._estados = estados
    self._alfabeto = alfabeto
    self._transicoes = transicoes
    self._estadoInicial = estadoInicial
    self._estadosFinais = estadosFinais

  def verificar_cadeia(self, cadeia):
    """
    Verifica se a cadeia fornecida é reconhecida pelo autômato.

    Parâmetros:
      - cadeia: Uma string contendo a cadeia de símbolos a ser verificada.

    Retorna:
      - True se a cadeia for aceita pelo autômato, False caso contrário.
    """
    conj_alfabeto = self._alfabeto
    conj_teste = set(cadeia)
    if not conj_teste - conj_alfabeto:  
      estado_atual = self._estadoInicial
      for simbolo in cadeia:
        estado_atual = self._transicoes.get((estado_atual, simbolo))
      return estado_atual in self._estadosFinais
    else:
      return False

'''
Definição de cada autômato, de "a" a "d", em que:
    Representação algébrica do autômato:
    - estados_x : estados do automato x 
    - alfabeto_x: alfabeto do automato x 
    Funções de transição do autômato definidas em tuplas como chaves do dicionário, onde o primeiro índice da tupla refere-se ao estado atual, 
    o próximo indice da tupla refere-se ao simbolo que é lido, e o valor refere-se ao estado que a transição leva:
    - transicoes_x: transições do autômato x no formato ('estado_origem','caractere'): 'estado_destino'
    Instanciando o automato com as caracteristicas especificadas:
    - automatoX = Automato(estados_x, alfabeto_x, transicoes_x, estadoInicial_x, estadosFinais_x)
'''

## Letra a: (ab*c*)*
estados_a = {'q0', 'q1', 'q2'}
alfabeto_a = {'a', 'b', 'c'} 
transicoes_a = { 
    ('q0',''): 'q0', #não é uma transição em vazio, apenas indica que o estado inicial também é final, aceitando a cadeia vazia
    ('q0','a'): 'q1',
    ('q1','b'): 'q1',  
    ('q1','c'): 'q2',
    ('q2','c'): 'q2',
}
estadoInicial_a = 'q0'
estadosFinais_a = {'q0', 'q1', 'q2'}
automatoA = Automato(estados_a, alfabeto_a, transicoes_a, estadoInicial_a, estadosFinais_a)

## Letra b: aaa(b|c)*|(b|c)*aaa
estados_b = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
alfabeto_b = {'a', 'b', 'c'} 
transicoes_b = {
  ('q0','a'): 'q1',
  ('q1','a'): 'q2',
  ('q2','a'): 'q3',
  ('q3','b'): 'q3',
  ('q3','c'): 'q3',
  ('q0','b'): 'q4',
  ('q0','c'): 'q4',
  ('q4','b'): 'q4',
  ('q4','c'): 'q4',
  ('q4','a'): 'q5',
  ('q5','a'): 'q6',
  ('q6','a'): 'q7'
}
estadoInicial_b = 'q0'
estadosFinais_b = {'q3', 'q7'}
automatoB = Automato(estados_b, alfabeto_b, transicoes_b, estadoInicial_b, estadosFinais_b)

## Letra c: a*b|ab*
estados_c = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
alfabeto_c = {'a','b'} 
transicoes_c = {
  ('q0', 'a'): 'q1',
  ('q0', 'b'): 'q5',
  ('q1', 'b'): 'q4',
  ('q4', 'b'): 'q4',
  ('q1', 'a'): 'q2',
  ('q2', 'a'): 'q2',
  ('q2', 'b'): 'q3'
}
estadoInicial_c = 'q0'
estadosFinais_c = {'q1', 'q3', 'q4', 'q5'}
automatoC = Automato(estados_c, alfabeto_c, transicoes_c, estadoInicial_c, estadosFinais_c)

## Letra d: a*b*(a|ac*)
estados_d = {'q0', 'q1', 'q2', 'q3'}
alfabeto_d = {'a', 'b', 'c'} 
transicoes_d = {
  ('q0', 'a'): 'q1',
  ('q0', 'b'): 'q3',
  ('q1', 'b'): 'q3',
  ('q1', 'a'): 'q1',
  ('q1', 'c'): 'q2',
  ('q2', 'c'): 'q2',
  ('q3', 'a'): 'q2',
  ('q3', 'b'): 'q3'
}
estadoInicial_d = 'q0'
estadosFinais_d = {'q1','q2'}
automatoD = Automato(estados_d, alfabeto_d, transicoes_d, estadoInicial_d, estadosFinais_d)

# Obtendo dados do usuário: informa o autômato desejado e cadeia a ser analisada

# Escolha do autômato
while True:
  escolheAut = int(input('''
1 - Autômato A: (ab*c*)*
2 - Autômato B: aaa(b|c)*|(b|c)*aaa
3 - Autômato C: a*b|ab*
4 - Autômato D: a*b*(a|ac*)
Informe o número do autômato que realizará a validação: '''))
  if escolheAut <= 0 or escolheAut >= 5:
    print('Erro! Escolha inválida.')
    continue
  break
  
# Escolha da cadeia
cadeiaTeste = input("Informe a cadeia a ser analisada: ")

# Validação da cadeia a partir de um autômato
if escolheAut == 1:
    verifica = automatoA.verificar_cadeia(cadeiaTeste)
elif escolheAut == 2:
    verifica = automatoB.verificar_cadeia(cadeiaTeste)
elif escolheAut == 3:
    verifica = automatoC.verificar_cadeia(cadeiaTeste)
else:
    verifica = automatoD.verificar_cadeia(cadeiaTeste)

if verifica:
   print("A cadeia é RECONHECIDA pelo autômato")
else:
   print("A cadeia é REJEITADA pelo autômato.")
   
# Testes automáticos: iterar uma lista de cadeias pré determinadas e indicar se o autômato escolhido as reconhece ou não
print('\n')
print(f"### Testes automáticos com o autômato {escolheAut} ###")
testes = [
    '','ac', 'a','abbbbc', 'abcc',                       
    'aaacbccb', 'aaabcbcbbcc', 'baaa', 'caaa', 'aaabcc', 
    'b', 'ab', 'aaaab','abbbbbb', 'aaaabbb',             
    'aaabbbac', 'bbaaaaccc', 'bba', 'aaaaaa', 'aabacc'   
]

for teste in testes:
    if escolheAut == 1:
        verifica = automatoA.verificar_cadeia(teste)
    elif escolheAut == 2:
       verifica = automatoB.verificar_cadeia(teste)
    elif escolheAut == 3:
       verifica = automatoC.verificar_cadeia(teste)
    else:
       verifica = automatoD.verificar_cadeia(teste) 
    if verifica:
        print(f"A cadeia {teste} é RECONHECIDA pelo autômato")
    else:
        print(f"A cadeia {teste} é REJEITADA pelo autômato.")   
