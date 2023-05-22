"""
O seguinte algoritmo tem como objetivo simular uma Máquina de Moore que considera uma sequência 
de moedas de 25 e 50 centavos, juntamente com moedas de 1 real, é estabelecido que uma lata de 
refrigerante será disponibilizada somente quando o valor total atingir ou ultrapassar 1 real. 
Cada moeda inserida terá um resultado específico, podendo ser 0, indicando que a lata não pode 
ser liberada (ainda), ou 1, sinalizando que a lata deve ser liberada.
"""
class MaquinaRefri:
    """
    Classe MaquinaRefri responsável por instanciar um transdutor do tipo Máquina de Moore
    que retorna uma saída de 0 para valores inferiores a 1 real e 1 para valores iguais
    ou superiores a 1 real. Baseado em uma sequencia de moedas de 25 e 50 centavos, e 1 real.
    """
    def __init__(self):
        """
        Inicializa a Máquina de Moore do refrigerante.
        
        Atributos:
        - estados: Um dicionário que associa cada estado do transdutor a uma descrição.
        - transicoes: Um dicionário que define as transições permitidas entre os estados do transdutor.
        - estado_corrente: O estado atual do transdutor.
        - saidas: Um dicionário que associa cada estado do transdutor a uma saída correspondente.
        """
        self.estados = {
          '0': "Estado 0 cents",
          '25': "Estado 25 cents",
          '50': "Estado 50 cents",
          '75': "Estado 75 cents",
          '100': "Estado 100 cents",
          '125': "Estado 125 cents",
          '150': "Estado 150 cents",
          '175': "Estado 175 cents"
        }
        # Funções de transição para o transdutor
        self.transicoes = {
            '0': {'25': '25', '50': '50', '100': '100'},
            '25': {'25': '50', '50': '75', '100': '125'},
            '50': {'25': '75', '50': '100', '100': '150'},
            '75': {'25': '100', '50': '125', '100': '175'},
            '100': {'25': '25', '50': '50', '100': '100'},
            '125': {'25': '50', '50': '75', '100': '125'},
            '150': {'25': '75', '50': '100', '100': '150'},
            '175': {'25': '100', '50': '125', '100': '175'}
        }
        self.estado_corrente = '0'
        # Saídas correspondentes para cada estado do transdutor
        self.saidas = {
            '0': '0',
            '25': '0',
            '50': '0',
            '75': '0',
            '100': '1',
            '125': '1',
            '150': '1',
            '175': '1'
        }
    
    def transitando(self, input):
        """
        Realiza a transição do transdutor de acordo com a entrada fornecida.
        
        Parâmetros:
        - input: Uma string que representa a moeda inserida (25, 50 ou 100).
        
        Retorna:
        - A saída correspondente ao estado atual após a transição, ou 'Nr' se a entrada for inválida.
        """
        if input not in ('25', '50', '100'):
            return 'Nr'
        proximo_estado = self.transicoes[self.estado_corrente][input]
        self.estado_corrente = proximo_estado
        return self.saidas[self.estado_corrente]
    
    def ligar(self, list_valores):
        """
        Executa a Máquina de Moore para uma sequência de moedas fornecida.
        
        Parâmetros:
        - list_valores: Uma lista de strings que representa a sequência de moedas inseridas.
        
        Retorna:
        - Uma string contendo as saídas correspondentes a cada transição do transdutor.
        """
        saidas = ''
        for valor in list_valores:
            saidas += self.transitando(valor)
        return saidas

# TESTE DO SCRIPT
lista_sequencias = [['25', '50', '100'], ['100', '25', '50'], ['50', '100', '25'], ['25', '100', '50'], ['50', '25', '100'], ['100', '50', '25'], ['25', '50', '100', '25'], ['25', '100', '50', '100'], ['50', '100', '25', '50'], ['100', '25', '50', '100'], ['25', '50', '100', '25', '50'], ['25', '100', '50', '100', '25'], ['50', '100', '25', '50', '100'], ['100', '25', '50', '100', '25'], ['25', '50', '100', '25', '50', '100'], ['25', '100', '50', '100', '25', '50'], ['50', '100', '25', '50', '100', '25'], ['100', '25', '50', '100', '25', '50'], ['25', '50', '100', '25', '50', '100', '25'], ['25', '100', '50', '100', '25', '50', '100']]

for sequencia in lista_sequencias:
  maquina = MaquinaRefri() # Uma nova máquina é criada a cada nova sequência testada.
  output_sequence = maquina.ligar(sequencia)
  print(f'Sequencia: {sequencia}')
  print(f'Saida: {output_sequence}')
  print('\n')