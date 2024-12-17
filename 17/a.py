class Machine(object):
    def __init__(self, A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def combo_operand(self, operand):
        opval = None
        if operand >= 0 and operand <= 3:
            opval = operand
        elif operand == 4:
            opval = self.A
        elif operand == 5:
            opval = self.B
        elif operand == 6:
            opval = self.C
        elif operand == 7:
            assert(False)
        return opval

    def literal_operand(self, operand):
        return operand

    def run(self, program):
        output = []
        IP = 0
        while IP < len(program):
            op = program[IP]
            operand = program[IP+1]
            IP += 2
            
            if op == 0: # ADV
                self.A = self.A >> self.combo_operand(operand)
            elif op == 1: # BXL
                self.B = self.B ^ self.literal_operand(operand)
            elif op == 2: # BST
                self.B = self.combo_operand(operand) % 8
            elif op == 3: # JNZ
                if self.A != 0:
                    IP = self.literal_operand(operand)
            elif op == 4: # BXC
                self.B = self.B ^ self.C
            elif op == 5: # OUT
                #print(self.A,self.B,self.C)
                o = self.combo_operand(operand) % 8
                output.append(o)
            elif op == 6: # BDV
                self.B = self.A  >> self.combo_operand(operand)
            elif op == 7: # CDV
                self.C = self.A >> self.combo_operand(operand)
        return output


    def find_quine(self, program):
        IP = 0
        out = []
        while IP < len(program):
            op = program[IP]
            operand = program[IP+1]
            IP += 2
            
            if op == 0: # ADV
                self.A = int(self.A / (2**self.combo_operand(operand)))
            elif op == 1: # BXL
                self.B = self.B ^ self.literal_operand(operand)
            elif op == 2: # BST
                self.B = self.combo_operand(operand) % 8
            elif op == 3: # JNZ
                if self.A != 0:
                    IP = self.literal_operand(operand)
            elif op == 4: # BXC
                self.B = self.B ^ self.C
            elif op == 5: # OUT
                o = self.combo_operand(operand) % 8
                out.append(o)
                if program[len(program) - len(out):] == out:
                    continue
                else:
                    return len(out)
            elif op == 6: # BDV
                self.B = int(self.A / (2**self.combo_operand(operand)))
            elif op == 7: # CDV
                self.C = int(self.A / (2**self.combo_operand(operand)))
        return len(out)
"""
A = 117440 
B=0
C=0
program =[0,3,5,4,3,0]
machine = Machine(A,B,C)
output = machine.run(program)
print(','.join([str(i) for i in output]))
"""

print("A")
A = 0o61176574462
# A = 0o6562166052247155
B=0
C=0
program =[2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]
machine = Machine(A,B,C)
output = machine.run(program)
print(','.join([str(i) for i in output]))

"""
Program: 2,4, 1,3 ,7,5 ,1,5, 0,3, 4,3 ,5,5, 3,0
B  = A % 8
B = B ^ 0b11
C = A / 2 ** B
B = B ^ 0b101
B = B ^ C
out(B % 8)
A = A / 2 ** 3
goto start if A > 0

out (((A % 8) ^ 3 ^ 5)  ^ (A >> (A % 8 ^ 3))) % 8
A >> 3

"""

# note that A basically divides by 8
# then loops
print("B")
A = 0o656216605224
B=0
C=0
program =[2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]
# scan progr
besta =0
bestr= -1 
for sc in range(1,7):
    for a in range(8**(sc)):
        #ca = A * (8**(sc-1)) + a
        ca = A * (8**sc) + a
        machine = Machine(ca,0,0)
        r = machine.run(program)
        if program[len(program) - len(r):] == r:
            matchscore = len(r)
            if matchscore > bestr:
                print(oct(ca))
                bestr = matchscore
                besta = ca
print(besta)
print(bestr)
print(oct(besta))

print("btest")
machine = Machine(besta,B,C)
output = machine.run(program)
print(','.join([str(i) for i in output]))

