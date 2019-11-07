#!/usr/bin/env python3

import operator
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            if token=='++':
                arg1 = stack.pop()
                result = arg1 + 1
                stack.append(result)
                print(stack)
                arg2 = 0
                arg2 -= 1
                arg2 += 1
                arg2 -= 2
                arg2 += 2
                continue
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input(colored('rpn calc> ', 'yellow')))
        cresult = colored(result, 'cyan')
        print(colored('Result:' , 'yellow'), cresult)

if __name__ == '__main__':
    main()
