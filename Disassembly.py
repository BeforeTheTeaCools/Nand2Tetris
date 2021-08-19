#Se Jin Park   Section 201
comp = {
    "0101010":"0",
    "0111111":"1",
    "0111010":"-1",
    "0001100":"D",
    "0110000":"A",
    "0001101":"!D",
    "0110001":"!A",
    "0001111":"-D",
    "0110011":"-A",
    "0011111":"D+1",
    "0110111":"A+1",
    "0001110":"D-1",
    "0110010":"A-1",
    "0000010":"D+A",
    "0010011":"D-A",
    "0000111":"A-D",
    "0000000":"D&A",
    "0010101":"D|A",
    "1110000":"M",
    "1110001":"!M",
    "1110011":"-M",
    "1110111":"M+1",
    "1110010":"M-1",
    "1000010":"D+M",
    "1010011":"D-M",
    "1000111":"M-D",
    "1000000":"D&M",
    "1010101":"D|M"
    }


dest = {
    "000":"null",
    "001":"M",
    "010":"D",
    "100":"A",
    "011":"MD",
    "101":"AM",
    "110":"AD",
    "111":"AMD"
    }


jump = {
    "000":"null",
    "001":"JGT",
    "010":"JEQ",
    "011":"JGE",
    "100":"JLT",
    "101":"JNE",
    "110":"JLE",
    "111":"JMP"
    }

list = []
flag = True

while(flag):
    val = str(input())
    if val != "EOF":
        list.append(val)
    else:
        flag = False

        
    
def disassembly(line):
    if line[0] == "0":
        return Assembly(line)
    else:
        return Cssembly(line)

def Assembly(line):
    a = str(int(line[1:], 2))
    return "@" + a

def Cssembly(line):
    
    ccode = str(comp.get(line[3:10]))
    dcode = ""
    jcode = ""
    if line[10:13] == "000" or line[13:] == "000" :
        if line[10:13] == "000":
            jcode = str(jump.get(line[13:]))
            return ccode + ";" + jcode
        if line[13:] == "000":
            dcode = str(dest.get(line[10:13]))
            return dcode + "=" + ccode
    else:
        jcode = str(jump.get(line[13:]))
        dcode = str(dest.get(line[10:13]))
        return dcode + "=" + ccode + ";" + jcode

for line in list:
    print(disassembly(line))