'''
 - Ler a entrada (caractere por caractere)
 - Se for um carectere de abertura '(', '[', '{', push
 - Se for um caractere de fechamento ')', ']', '}',:
    - Verificar se este caractere "combina" com o que está no top da pilha:
        - Caso esteja, é realizado um pop na pilha
        - Caso não esteja, a expressão não está balanceada
'''
open_list = ["[","{","("] 
close_list = ["]","}",")"] 

def is_balanced(s):

    stack = []

    for character in s:
        if character in open_list:
            stack.append(character)
        elif character in close_list:
            position = close_list.index(character)
            if ((len(stack) > 0 and (open_list[position] == stack[len(stack) - 1]))):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':

    expression = "[]"
    result = is_balanced(expression)
    print("Balanced?", result)
    