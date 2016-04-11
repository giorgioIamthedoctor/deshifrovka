import statistics

def atbash(path):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabetC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    sd = ""
    s = init(path)
    for x in s:
        if alphabet.count(x) != 0:
            sd += alphabet[len(alphabet) - 1 - alphabet.index(x)]
        elif alphabetC.count(x) != 0:
            sd += alphabetC[len(alphabetC) - 1 - alphabetC.index(x)]
        else:
            sd += x
    op = open("./shd.txt","w")
    op.write(sd)
    op.close()
def cesar(path):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabetC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    sd = ""
    s = init(path)
    sdvig = int(len(alphabet)/2 - (alphabet.index("ш") - alphabet.index("и")) - 1)
    print(sdvig)
    for x in s:
        if alphabet.count(x) != 0:
            sd += alphabet[alphabet.index(x) + sdvig]
        elif alphabetC.count(x) != 0:
            sd += alphabetC[alphabetC.index(x) + sdvig]
        else:
            sd += x
    op = open("./shd2.txt","w")
    op.write(sd)
    op.close()

def my_sort(slov,chas):
    for i in range(len(slov)):
        for j in range(i,len(slov)-1):
            if chas[j] > chas[j+1]:
                chas[j+1],chas[j] = chas[j],chas[j+1]
                slov[j+1],slov[j] = slov[j],slov[j+1]
    return slov,chas

def chastotatr(path):
    chastota = []
    chas = []
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    s = init(path)
    op = open("./chas.txt","r")
    rd = op.readlines()
    op = open(path,"r")
    rt = op.read()
    rtt = ""
    rt = rt.lower()
    for x in rt:
        if alphabet.count(x) != 0:
            rtt += x
    op.close()
    slov = []
    for x in alphabet:
        chas.append(float(rtt.count(x)/len(rtt)))
        slov.append(x)
    slov,chas = my_sort(slov,chas)
    s = s.lower()
    ss = ""
    translate = {}
    for x in s:
        if alphabet.count(x) != 0:
            ss += x
    for x in alphabet:
        chastota.append(float(ss.count(x)/len(ss)))
        print(x,float(ss.count(x)/len(ss)))
    for x in range(len(chastota)):
        i = 0
        if chastota[x] > 0.928:
            translate[alphabet[x]] = 'о'
        else:
            while chastota[x] <= chas[i]:
                i += 1
            else:
                if (chas[i] - chastota[x]) < (chas[x] - chas[i-1]):
                    translate[alphabet[x]] = slov[i]
                else:
                    translate[alphabet[x]] = slov[i-1]
    sd = ""
    for x in s:
        if alphabet.count(x) != 0:
            sd += translate[x]
        else:
            sd += x
    op = open("./shd3.txt","w")
    op.write(sd)
    op.close()

def init(path):
    op = open(path,"r")
    s = op.read()
    op.close()
    return s
chastotatr(input("Введите путь до файла с шифром :"))