#Se Jin Park   Section 201
comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
    }


dest = {
    "null": "000",
    "M": "001",
    "D": "010",
    "A": "100",
    "MD": "011",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
    }


jump = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
    }

symbol = {
    "R0":"0",
    "R1":"1",
    "R2":"2",
    "R3":"3",
    "R4":"4",
    "R5":"5",
    "R6":"6",
    "R7":"7",
    "R8":"8",
    "R9":"9",
    "R10":"10",
    "R11":"11",
    "R12":"12",
    "R13":"13",
    "R14":"14",
    "R15":"15",
    "SCREEN":"16384",
    "KBD":"24576",
    "SP":"0",
    "LCL":"1",
    "ARG":"2",
    "THIS":"3",
    "THAT":"4",
    }

global default
global checker
checker = True
default = 16

list = []
flag = True

while(flag):
    val = str(input())
    if val != "EOF":
        list.append(val)
    else:
        flag = False

#gets rid of all empty spaces in strings
def whiteline(list):
    listy = []
    for string in list:
        a = string.replace(" ", "")
        b = a.replace("\t", "")
        listy.append(b)
    return listy

#gets rid of all the empty space in the list
def emptyspace(list):
    list = [i for i in list if i]
    return list

#gets rid of commment lines in the beginning
semicleanlist = emptyspace(whiteline(list))
scl = []
for string in semicleanlist:
        if string[0] == "/":
            pass
        else:
            scl.append(string)

#gets rid of comment lines after the code
scl2 = []
for string in scl:
    if "/" in string:
        scl2.append(string[0:(string.index("/"))])
    else:
        scl2.append(string)
#scl2 is final code only list

#decides which instruction to use and calls
def instruction(line, ind):

        if line[0] == "@":

            return astruction(line)
        if line[0] == "(":
            temp = line[1:-1]
            symbol[temp] = ind[0]
            ind[0] -= 1
            return ""
        else:
            other = cstruction(line)

            return "111" + other
        
def astruction(line):
        global default
        global checker
        if line[1].isalpha():
            temp = line[1:]
            value = symbol.get(temp)
            if value == None:
                if checker:
                    return
                symbol[temp] = default
                default += 1

            value = int(symbol.get(temp))
            b = bin(value)[2:].zfill(16)
            return b
        else: #if it's number so @20
            a = int(line[1:])
            b = bin(a)[2:].zfill(16)
            return b
        
def nullcase(line):
    line = line
    if not "=" in line:
        line = "null=" + line
    if not ";" in line:
        line = line + ";null"
    return line

def cstruction(line):
    temp1 = nullcase(line)
    temp = temp1.split("=")
    dcode = str(dest.get(temp[0]))
    temp2 = temp[1].split(";")
    ccode = str(comp.get(temp2[0]))
    jcode = str(jump.get(temp2[1]))
    result = ccode + dcode + jcode
    return result

ind = [0]
for line in range(0,len(scl2)):
    instruction(scl2[line], ind)
    ind[0] += 1
checker = False
ind = [0]
for line in range(0,len(scl2)):
    string1 = instruction(scl2[line], ind)
    if string1 != "":
        print(string1)
    ind[0] += 1