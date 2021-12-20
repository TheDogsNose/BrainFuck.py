import os
from dotenv import load_dotenv
from re import TEMPLATE, template

FILE = os.getenv('BFPATH')

#BrainFuck = open('Example.bf', 'r')
#CodeLines = BrainFuck.readlines
code = '>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.'
Memory = [0]
Pointer = 0


def right(p):
    global Pointer

    if p < (len(Memory) - 1):
        Pointer += 1
    else:
        Memory.append(0)
        Pointer += 1

def left(p):
    global Pointer

    if p > 0:
        Pointer -=1
    else:
        Pointer.insert(0, 0)

def loop(x):
    global Pointer
    for i in range(x, int(len(code) - 1)):
        if code[i] == '>':
            right(Pointer)
        elif code[i] == '<':
            left(Pointer)
        elif code[i] == '+':
            Memory[Pointer] += 1
        elif code[i] == '-':
            Memory[Pointer] -= 1
        elif code[i] == '.':
            print(Memory[Pointer])
        elif code[i] == ',':
            Memory[Pointer] = input()
        # elif code[i] == '[':
        #     loop(i)
        elif code[i] == ']':
            return i
        else:
            continue



# for i in CodeLines:
#     code.append(CodeLines[i])

iter_code = iter(range(len(code)))


for i in iter_code:
    if code[i] == '>':
        right(Pointer)
    elif code[i] == '<':
        left(Pointer)
    elif code[i] == '+':
        Memory[Pointer] += 1
    elif code[i] == '-':
        Memory[Pointer] -= 1
    elif code[i] == '.':
        print(Memory[Pointer])
    elif code[i] == ',':
        Memory[Pointer] = input()
    elif code[i] == '[':
        a = loop(i)
        for i in range(a+1):
            next(iter_code)
    else:
        continue


