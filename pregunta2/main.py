# References:
# https://en.wikipedia.org/wiki/Reverse_Polish_notation
# https://en.wikipedia.org/wiki/Polish_notation

from collections import deque
from enum import Enum


class MODE(Enum):
    PRE = 1
    POST = 2


OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2}


def prefix_eval(tokens):
    token = tokens.popleft()
    if token == '+':
        return prefix_eval(tokens) + prefix_eval(tokens)
    elif token == '-':
        return prefix_eval(tokens) - prefix_eval(tokens)
    elif token == '*':
        return prefix_eval(tokens) * prefix_eval(tokens)
    elif token == '/':
        return prefix_eval(tokens) / prefix_eval(tokens)
    else:
        try:
            return float(token)
        except ValueError:
            print("La expresión no es valida")
            return ""


def build(token, elems, mode):
    if token not in OPERATORS:
        elems.append((token, 0))
    else:
        if mode == MODE.PRE:
            lop, lp = elems.pop()
            rop, rp = elems.pop()
        else:
            rop, rp = elems.pop()
            lop, lp = elems.pop()
        p = OPERATORS[token]

        if lp < p and lp != 0:
            lop = '(' + lop + ')'

        if rp < p and rp != 0:
            rop = '(' + rop + ')'

        string = lop + " " + token + " " + rop
        elems.append((string, p))

    return elems


def to_infix(e, mode):
    stack = []
    tokens = e.split()

    if mode == MODE.PRE:
        for token in tokens[::-1]:
            build(token, stack, mode)
    else:
        for token in tokens:
            build(token, stack, mode)

    return stack.pop()[0]


def postfix_eval(e):
    stack = []
    for token in e.split():
        if token in OPERATORS:
            rop = stack.pop()
            lop = stack.pop()

            if token == "+":
                result = lop + rop
            elif token == "-":
                result = lop - rop
            elif token == "*":
                result = lop * rop
            elif token == "/":
                result = lop / rop
            stack.append(result)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                print("La expresión no es valida")
                return ""
    return stack.pop()


if __name__ == '__main__':
    while True:
        cmd = input()
        if len(cmd) == 0:
            continue

        cmd = cmd.split(' ')
        if cmd[0] == "SALIR":
            break

        if len(cmd) < 3:
            print("Instrucción desconocida")
            continue

        order = cmd[1]
        exp = " ".join(cmd[2::])

        if order.upper() == MODE.PRE.name:
            order = MODE.PRE
        elif order.upper() == MODE.POST.name:
            order = MODE.POST
        else:
            print("Orden inválida. Solo se admite PRE y POST")
            continue

        if len(exp) == 0:
            print("Expresión inválida")
            continue

        if cmd[0] == "EVAL":
            if order == MODE.PRE:
                print(prefix_eval(deque(exp.split())))

            if order == MODE.POST:
                print(postfix_eval(exp))

        if cmd[0] == "MOSTRAR":
            print(to_infix(exp, order))
