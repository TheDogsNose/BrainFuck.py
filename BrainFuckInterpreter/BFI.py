import os
from re import TEMPLATE, template
from dotenv import load_dotenv
from dotenv import dotenv_values

#BFPATH = os.getenv('BFPATH')
config = dotenv_values()
BFPATH = config['BFPATH']


BrainFuck = open(BFPATH,  'r')
CodeLines = BrainFuck.readlines()
codeF = ''
if len(CodeLines) > 0:
    for i in CodeLines:
        codeF = codeF + i
#code = '>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.'
#code = '+++[>+++<-]>.'
code = ',[<++>-]<.'

class BF ():

    Memory = [0, 0, 0]
    MPointer = 0
    CPointer = 1
    Looper = 0
    #loopm = 0

    def __init__(self, Code: str) -> None:
        self.Code = Code

    def run(self):
        print(self.Code)
        while self.CPointer <= len(self.Code):
            self.checkC(self.CPointer)

    def checkC (self, c):
        if self.Code[c - 1] == '>':
            self.right(self.MPointer)
        elif self.Code[c - 1] == '<':
            self.left(self.MPointer)
        elif self.Code[c - 1] == '+':
            self.Memory[self.MPointer] = int(self.Memory[self.MPointer]) + 1
        elif self.Code[c - 1] == '-':
            self.Memory[self.MPointer] -= 1
        elif self.Code[c - 1] == '.':
            if self.Memory[self.MPointer] >= 0:
                print('output:', self.Memory[self.MPointer], ', ', chr(self.Memory[self.MPointer]))
            else:
                print('output', self.Memory[self.MPointer])
        elif self.Code[c - 1] == ',':
            k = input()
            try:
                self.Memory[self.MPointer] = int(k)
            except ValueError:
                self.Memory[self.MPointer] = ord(k)
            except:
                self.Memory[self.MPointer] = 0
        elif self.Code[c - 1] == '[':
            #self.loopm = self.MPointer
            self.loop(c - 1, self.MPointer)
        elif self.Code[c - 1] == ']':
            pass
        else:
            return
        self.CPointer += 1

    def right(self, M):
        if M < (len(self.Memory) - 1):
            self.MPointer += 1
        else:
            self.Memory.append(0)
            self.MPointer += 1

    def left(self, M):
        if M > 0:
            self.MPointer -= 1
        else:
            self.Memory.insert(0, 0)
            #self.loopm += 1


    def loop(self, c, m):
        #while self.Memory[m] != 0:
        if self.Memory[m] <=0:
            while True:
                if self.Code[self.CPointer] == ']':
 #                   print('b')
                    self.CPointer += 1
                    return
                else:
                    self.CPointer += 1
                    continue

        else:    
            while True: 
                if self.Code[self.CPointer] == '>':
                    self.right(self.MPointer)
                elif self.Code[self.CPointer] == '<':
                    if not (self.MPointer > 0):
                        m += 1
                    self.left(self.MPointer)
#                    print('pointer', self.MPointer)
                elif self.Code[self.CPointer] == '+':
                    self.Memory[self.MPointer] += 1
 #                   print('we did + on', self.MPointer, "now it's", self.Memory[self.MPointer])
                elif self.Code[self.CPointer] == '-':
                    self.Memory[self.MPointer] -= 1
#                    print('we did - on', self.MPointer, "now it's", self.Memory[self.MPointer])
                elif self.Code[self.CPointer] == '.':
                    if self.Memory[self.MPointer] >= 0:
                        print('output:', self.Memory[self.MPointer], ', ', chr(self.Memory[self.MPointer]))
                    else:
                        print('output', self.Memory[self.MPointer])
                elif self.Code[self.CPointer] == ',':
                    k = input()
                    try:
                        self.Memory[self.MPointer] = int(k)
                    except ValueError:
                        self.Memory[self.MPointer] = ord(k)
                    except:
                        self.Memory[self.MPointer] = 0
                # elif self.Code[self.CPointer - 1] == '[':
                #     self.CPointer += 1
                elif self.Code[self.CPointer] == ']':
                    if self.Memory[m] <= 0:
 #                       print('b')
                        self.CPointer += 1
                        return
                        break
                    else:

                        self.CPointer = c
     #                   print('c')
                        continue
                else:
       #             print(self.Code[self.CPointer])
                    self.CPointer += 1
                    continue

                self.CPointer += 1




bf = BF(codeF)
bf.run()
