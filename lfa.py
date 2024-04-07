#Necessário instalar a biblioteca automathon
#!pip install automathon --upgrade

def afd(M, w):
    # 'extrai' os elementos da tupla M
    δ, q, F = M  # δ é a função de transição, q é o estado inicial, F é o conjunto de estados de aceitação

    expression = []  # Lista para armazenar a expressão matemática
    number = ''  # String para construir os números da expressão

    # Itera sobre os caracteres da entrada w (expressão matemática)
    for s in w:
        q = δ[(q, s)]  # Consulta a função de transição para obter o próximo estado

        if s in ['+', '-', '*', '/']: # Se o caractere s é um operador matemático (+, -, *, /)
            expression.append(number) # Se for um operador, adiciona o número atual à lista expression
            expression.append(s) # Adiciona o operador à lista expression
            number = '' # Reinicia a string number para construir o próximo número
        else:
            number += s # Se o caractere s é um dígito, adiciona ao número em construção (number)

    expression.append(number) # Adiciona o último número à lista expression

    # Verifica se o estado final (q) pertence ao conjunto de estados de aceitação (F)
    if q in F:
        postfix_expression = infix_to_postfix(expression) # Converte a expressão infix para postfix (notação pós-fixa)
        result = evaluate_postfix(postfix_expression) # Avalia a expressão postfix para obter o resultado da expressão matemática
        print("Resultado da expressão:", result) # Imprime o resultado da expressão
        return result

    return None # Se o estado final não estiver em F, a expressão é inválida; retorna None

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  # Dicionário que mapeia operadores para precedência

    def greater_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]  # Função que verifica se op1 tem precedência maior ou igual a op2

    stack = []  # Pilha para armazenar operadores temporariamente durante a conversão
    postfix = []  # Lista para armazenar a expressão na notação pós-fixa

    for token in expression:
        if token.isdigit():
            postfix.append(token)  # Se o token é um dígito, adiciona diretamente à lista postfix
        else:  # Se o token é um operador
            # Enquanto a pilha não estiver vazia e o topo da pilha não for um '(' e o operador no topo da pilha tiver precedência maior que o token atual
            while stack and stack[-1] != '(' and greater_precedence(stack[-1], token):
                postfix.append(stack.pop())  # Remove o operador do topo da pilha e adiciona à lista postfix
            stack.append(token)  # Adiciona o token à pilha

    # Depois de processar todos os tokens, esvazia a pilha e adiciona os operadores restantes à lista postfix
    while stack:
        postfix.append(stack.pop())

    return postfix  # Retorna a expressão na notação pós-fixa

def evaluate_postfix(expression):
    stack = []  # Pilha para armazenar operandos durante a avaliação da expressão

    # Itera sobre cada token na expressão na notação pós-fixa
    for token in expression:
        if token.isdigit():
            stack.append(int(token))  # Se o token é um dígito, converte para inteiro e adiciona à pilha
        else:
            # Quando encontra um operador, retira os dois operandos mais recentes da pilha
            operand2 = stack.pop()  # Segundo operando (topo da pilha)
            operand1 = stack.pop()  # Primeiro operando (segundo topo da pilha)

            # Realiza a operação com base no operador encontrado
            if token == '+':
                result = operand1 + operand2  # Soma
            elif token == '-':
                result = operand1 - operand2  # Subtração
            elif token == '*':
                result = operand1 * operand2  # Multiplicação
            elif token == '/':
                result = operand1 / operand2  # Divisão

            stack.append(result)  # Adiciona o resultado da operação de volta à pilha

    return stack[0]  # Retorna o resultado final da avaliação da expressão pós-fixa

δ = {
    ('q0', '0'): 'q0',
    ('q0', '1'): 'q0',
    ('q0', '2'): 'q0',
    ('q0', '3'): 'q0',
    ('q0', '4'): 'q0',
    ('q0', '5'): 'q0',
    ('q0', '6'): 'q0',
    ('q0', '7'): 'q0',
    ('q0', '8'): 'q0',
    ('q0', '9'): 'q0',
    ('q0', '+'): 'q1',
    ('q0', '-'): 'q1',
    ('q0', '*'): 'q1',
    ('q0', '/'): 'q1',
    ('q1', '0'): 'q2',
    ('q1', '1'): 'q2',
    ('q1', '2'): 'q2',
    ('q1', '3'): 'q2',
    ('q1', '4'): 'q2',
    ('q1', '5'): 'q2',
    ('q1', '6'): 'q2',
    ('q1', '7'): 'q2',
    ('q1', '8'): 'q2',
    ('q1', '9'): 'q2',
    ('q2', '0'): 'q2',
    ('q2', '1'): 'q2',
    ('q2', '2'): 'q2',
    ('q2', '3'): 'q2',
    ('q2', '4'): 'q2',
    ('q2', '5'): 'q2',
    ('q2', '6'): 'q2',
    ('q2', '7'): 'q2',
    ('q2', '8'): 'q2',
    ('q2', '9'): 'q2',
    ('q2', '+'): 'q1',
    ('q2', '-'): 'q1',
    ('q2', '*'): 'q1',
    ('q2', '/'): 'q1'
}

# AFD representado por uma 3-upla, ao invés de uma 5-upla
# O alfabeto e conjunto de estados podem ser inferidos da funcao de transicao
M = (δ, 'q0', ['q2'])

afd(M, "2+3*4*4*54*100")

from automathon import DFA

Q = {'q0', 'q1', 'q2'}
sigma = {'0', '1','2','3','4','5','6','7','8','9','+','-','*','/',}
delta = {'q0': {'0': 'q0', '1': 'q0', '2': 'q0', '3': 'q0', '4': 'q0', '5': 'q0', '6': 'q0', '7': 'q0', '8': 'q0', '9': 'q0', '+': 'q1', '-': 'q1', '*': 'q1', '/': 'q1'},
 'q1': {'0': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2'},
 'q2': {'0': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2', '+': 'q1', '-': 'q1', '*': 'q1', '/': 'q1'}}

initial_state = 'q0'
F = {'q2'}

automata = DFA(Q, sigma, delta, initial_state, F)

automata.is_valid()

automata.accept("2+3") #True

automata.accept("2+3+") #False

# estilo default
automata.view("afd01")

# estilo personalizado
automata.view(
    file_name="afd01_personalizado",
    node_attr={'fontsize': '20'},
    edge_attr={'fontsize': '20pt'}
)