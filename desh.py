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
    op = open("./shd.txt","w",encoding="utf8")
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
    op = open("./shd2.txt","w",encoding="utf8")
    op.write(sd)
    op.close()

def my_sort(slov,chas):
    for i in range(len(slov)):
        for j in range(0,len(slov)-1 - i):
            if chas[j] > chas[j+1]:
                chas[j+1],chas[j] = chas[j],chas[j+1]
                slov[j+1],slov[j] = slov[j],slov[j+1]
    return slov,chas

def chastotatr(path):
    chastota = []
    chas = []
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabetC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    s = init(path)
    op = open("./realtext.txt","r",encoding="utf8")
    rt = op.read()
    op.close()
    rtt = ""
    rt = rt.lower()
    for x in rt:
        if alphabet.count(x) != 0:
            rtt += x
    slov = []
    for x in alphabet:
        chas.append(float(rtt.count(x)/len(rtt)))
        slov.append(x)
    slov,chas = my_sort(slov,chas)
    sss = s.replace("Илюодсайэ вчьсдо вчнлыц ьчжйрвлъча жйрвлз Ъйедадвч ю адйьъдюыацз шлслъцз юолълз. Илсюшчьшч соё ючзцф юылэшйф швйиылчачойыйшлъ: сойач шлслългл юолъч 8.","").lower()
    ss = ""
    translate = {}
    for x in sss:
        if alphabet.count(x) != 0:
            ss += x
    for x in alphabet:
        chastota.append(float(ss.count(x)/len(ss)))
    for x in range(len(chastota)):
        i = 0
        if chastota[x] >= chas[len(chas)-1]:
            translate[alphabet[x]] = slov[len(chas)-1]
        else:
            while chastota[x] > chas[i]:
                i += 1
            else:
                if (chas[min(i+1,32)] - chastota[x]) < (chastota[x] - chas[i]):
                    translate[alphabet[x]] = slov[min(i-1,32)]
                else:
                    translate[alphabet[x]] = slov[min(i,32)]
    sd = ""
    for x in s:
        if alphabet.count(x) != 0:
            sd += translate[x]
        elif alphabetC.count(x) != 0:
            sd += str(str(translate[x.lower()]).upper())
        else:
            sd += x
    print(chas[slov.index("ф")])
    print(chas[slov.index("з")])
    print(chastota[alphabet.index("р")])
    print(translate["р"])
    print(slov)
    op = open("./shd3.txt","w",encoding="utf8")
    op.write(sd)
    op.close()
def cesarnew(path):
    translate = {}
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabetC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    s = init(path)
    ss = s.lower()
    sss = ""
    for x in ss:
        if alphabet.count(x) != 0:
            sss += x
    for i in range(int(len(alphabet)/2)):
        translate[alphabet[i]] = {}
        print(translate)
        for j in range(int(len(alphabet)/2)):
            translate[alphabet[i]][alphabet[j+i]] = alphabet[j]
def init(path):
    op = open(path,"r",encoding="utf8")
    s = op.read()
    op.close()
    return s
cesarnew(input(""))