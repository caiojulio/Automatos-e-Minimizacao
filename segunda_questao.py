"""
O seguinte algoritmo tem como objetivo simular um autômato finito que seja capaz de reconhecer
as ocorrências da palavra 'computador'.
Esse script utiliza o autômato criado como mecanismo para contar as ocorrências e posições
da palavra 'computador' dentro de um texto qualquer.
"""
class Automato:
  """
  Classe Automato responsável por instanciar automatos que reconheçam a palavra 'computador'.
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

  def texto_limpo(self, texto):
    """
    Remove pontuações do texto fornecido.

    Parâmetros:
      - texto: Uma string contendo o texto a ser limpo.

    Retorna:
      - Uma nova string com as pontuações removidas.
    """
    import re
    padrao = r'[.,:;?!]'
    texto_limpo = re.sub(padrao, '', texto)
    return texto_limpo
  
  def ocorrencia_posicao(self, texto):
    """
    Verifica as ocorrências e as posições da palavra 'computador' em um texto.

    Parâmetros:
      - texto: Uma string contendo o texto em que serão buscadas as ocorrências.

    Retorna:
      - Um tuple contendo o número de ocorrências encontradas e uma lista com as posições das ocorrências.
    """
    text_format = self.texto_limpo(texto)
    text_format = text_format.split()
    contadorOcorrencias = 0
    posicoesTexto = []
    for indice, cadeia in enumerate(text_format):
      if self.verificar_cadeia(cadeia):
        contadorOcorrencias += 1
        posicoesTexto.append(indice+1)
    return contadorOcorrencias, posicoesTexto
    

# Definindo representação algebrica do automato
estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10'}
alfabeto = {'c', 'o', 'm', 'p', 'u', 't', 'a', 'd','o', 'r'}

# Funções de transição do automato definidas em tuplas como chaves do dicionario, onde o primeiro indice da tupla refere-se ao estado atual, o proximo indice da tupla refere-se ao simbolo que é lido, e o valor refere-se ao estado que a transição leva.
transicoes = {
    ('q0', 'c'): 'q1',
    ('q1', 'o'): 'q2',
    ('q2', 'm'): 'q3',
    ('q3', 'p'): 'q4',
    ('q4', 'u'): 'q5',
    ('q5', 't'): 'q6',
    ('q6', 'a'): 'q7',
    ('q7', 'd'): 'q8',
    ('q8', 'o'): 'q9',
    ('q9', 'r'): 'q10'
}
estadoInicial = 'q0'
estadosFinais = {'q10'}

# Instanciando o automato com as caracteristicas especificadas
automatoComputador = Automato(estados, alfabeto, transicoes, estadoInicial, estadosFinais) 

# TESTE DO SCRIPT
texto1 = "No mundo moderno, o computador se tornou uma peça essencial no nosso cotidiano. Desde o momento em que acordamos até a hora de dormir, interagimos com computadores de diferentes formas."
texto2 = "A revolução digital foi impulsionada pelo surgimento e aprimoramento do computador. Esse dispositivo, inicialmente projetado para processar cálculos complexos, acabou se transformando em uma ferramenta multifuncional."
texto3 = "Quando se trata de inovação, a evolução do computador é um dos exemplos mais marcantes. Desde as antigas máquinas de calcular até os modernos computadores pessoais, testemunhamos uma revolução tecnológica sem precedentes."
texto4 = "Nos dias de hoje, os computadores são ferramentas indispensáveis em praticamente todas as áreas da sociedade. Na educação, eles estão presentes nas salas de aula, auxiliando professores e alunos."
texto5 = "O desenvolvimento da tecnologia de computadores tem revolucionado a forma como trabalhamos. Antes, a maioria das tarefas era feita manualmente, exigindo tempo e esforço significativos. Com o advento do computador."
texto6 = "Eu adoro passar horas navegando na internet no meu computador."
texto7 = "No parque, as crianças brincavam despreocupadas, sem a necessidade de um computador."
texto8 = "Os avanços tecnológicos revolucionaram a forma como utilizamos o computador no dia a dia."
texto9 = "O pintor contemplava a paisagem, buscando inspiração sem se importar com o mundo dos computadores."
texto10 = "No escritório, a máquina de escrever foi substituída pelo computador, trazendo mais eficiência e praticidade."
texto11 = """
Nos tempos modernos, o computador se tornou uma ferramenta indispensável em praticamente todas as áreas da vida. Seja no trabalho, nos estudos ou até mesmo no lazer, é difícil imaginar como seriam nossas vidas sem essa máquina incrível. O computador é capaz de processar informações em velocidades impressionantes e executar tarefas complexas em questão de segundos. Além disso, com o avanço da tecnologia, os computadores se tornaram cada vez mais compactos e portáteis, permitindo que as pessoas os levem para qualquer lugar. É inegável o impacto que o computador teve na sociedade moderna e as infinitas possibilidades que ele oferece.
"""
texto12 = """
Quando se trata da área médica, o computador desempenha um papel crucial. Os sistemas computadorizados permitem armazenar e acessar com facilidade os prontuários dos pacientes, agilizando o processo de diagnóstico e tratamento. Além disso, a tecnologia avançada dos computadores possibilita a realização de exames médicos de alta precisão, como tomografias e ressonâncias magnéticas, auxiliando os médicos no diagnóstico de doenças complexas. Os profissionais de saúde também utilizam computadores para acessar informações atualizadas sobre medicamentos, pesquisas e avanços na área médica. Em resumo, o computador revolucionou a prática da medicina, tornando-a mais eficiente e precisa.
"""
texto13 = """
Na atualidade, a telemedicina tem se tornado cada vez mais comum, e isso não seria possível sem a presença do computador. Através de videoconferências e plataformas online, médicos podem realizar consultas à distância, ampliando o acesso aos cuidados de saúde, principalmente em regiões remotas. Além disso, o uso de softwares médicos especializados permite a troca de informações e resultados de exames de forma rápida e segura. O computador se tornou uma ferramenta essencial para a prática da telemedicina, proporcionando uma nova forma de atendimento médico que beneficia pacientes e profissionais. Sem dúvida, a tecnologia continua a avançar, e o papel do computador na área médica continuará a se expandir, oferecendo novas possibilidades e soluções inovadoras.
"""
texto14 = """
No campo do desenvolvimento de software, o computador é uma ferramenta indispensável. Desde a codificação e depuração de programas até a execução de testes e análise de desempenho, o computador desempenha um papel central em todas as etapas do processo. Os desenvolvedores utilizam ambientes de desenvolvimento integrados (IDEs) para escrever e editar código, aproveitando recursos como sugestões de autocompletar e depuradores para identificar e corrigir erros. Além disso, o poder de processamento dos computadores modernos permite a criação de aplicativos cada vez mais complexos e robustos. O computador é a ferramenta essencial que impulsiona a inovação no desenvolvimento de software, capacitando os profissionais a criar soluções tecnológicas avançadas para atender às demandas do mundo digital.
"""
texto15 = """
No mundo do desenvolvimento de software, a colaboração entre equipes é facilitada pelo uso de computadores conectados em rede. As ferramentas de controle de versão, como o Git, permitem que vários desenvolvedores trabalhem em um mesmo projeto simultaneamente, realizando alterações e integrando seu código de forma organizada. Os computadores também são utilizados para hospedar repositórios de código-fonte, facilitando o compartilhamento e o controle de versões. Além disso, as equipes de desenvolvimento podem usar plataformas de comunicação online, como chats e videoconferências, para trocar ideias, discutir problemas e coordenar esforços. O computador se tornou o elo essencial que une desenvolvedores de software, permitindo uma colaboração eficiente e uma produção de alta qualidade.
"""

lista_textos = [texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8, texto9, texto10, texto11, texto12, texto13, texto14, texto15]

for indice, item in enumerate(lista_textos):
  print(f'TEXTO {indice + 1}:')
  ocorrencia, posicao = automatoComputador.ocorrencia_posicao(item)
  if ocorrencia == 0:
    print("Não houve ocorrencias")
  else:
    print(f'''
      Há {ocorrencia} ocorrências da palavra "computador" no texto informado. 
      as posições do aparecimento da palavra "computador" no texto são: {posicao} 
      ''')
  print('\n')