from datetime import datetime
#inicijalizacija globalnih RCV vektora (CSR metod)
r=[0,0,0,0,0,0,0,0,0,0,0,0]#12 elemetana, sve vrste, suma, i poslenji u kojem cuvamo broj popunjenih polja
c=[]
v=[]
#inicijalizacija globalne matrice
m=[]
#recnici koji su potrebni zbog oznacavanja redova tj vrsta koje korisnik unosi
mapa={'1':1,"2":2, "3":3, "4":4, "5":5,"6":6,'kenta':7, 'ful':8, 'poker':9, 'jamb':10}
mapa1={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'kenta',8:'ful',9:'poker',10:'jamb'}
#lista u kojoj su precrtani elementi u rucnoj
rucna1=[]
#pokayivaci na dozvoljena polja u kolonama nadole i nagore
nagoreIndeks=10
nadoleIndeks=1

def inicijalizujTalon():#inicijalizuje talon tako sto smesta 0 0 0 u vrstu koja je oznacena sa "suma", kako to znaci da smo
    #dodali tri elementa, onda sve elemente u vektoru r inkrementiramo za tri
    for i in range(1, len(r)):
        r[i]=3
    r[0]=0
    #pokazivaci na tri kolone tri inicijalne sume
    c.append(0)
    c.append(1)
    c.append(2)
    #inicijalizacija vrednosti vrste suma za svaku kolonu
    v.append(0)
    v.append(0)
    v.append(0)

def setSeed(seed):
    #inicijalizacija seeda, poziva se u main
    global u
    u = seed

def randomD():
    #implementacija LKG algoritma, prema predavanjima
    global u
    u = 429493445 * u + 907633385
    return (u % 4294967296) / 4294967296

def rand10():
    #funkcija koja za random broj izmedju 0 i 1 vraca 0 ili 1
    i=randomD()
    if i>0.5:
        return 1
    else:
        return 0

def rand8():
    #funkcija koje okoristeci prethodnu vraca neki od brojeva od 1 do 8
    i=rand10()
    i=i*2+rand10()
    i = i * 2 + rand10()
    return i+1

def cube():
    #funkcija koja koriscenjem prethodne vraca broj od 1 do 6, izbegavanje rekurzije
    i=rand8()
    if i>6:
        while(i>6):
            i=rand8()
    return i

def sumaPojedinacnih(kockice, broj):#racuna sumu istih elemenata yadatkog broja u nizu kockice
    return sum([x for x in kockice if x == broj])
def jedinice(kockice):#fje koje vracaju sumu za odredjeni broj u nizu kockice
    return sumaPojedinacnih(kockice,1)
def dvojke(kockice):
    return sumaPojedinacnih(kockice,2)
def trojke(kockice):
    return sumaPojedinacnih(kockice,3)
def cetvorke(kockice):
    return sumaPojedinacnih(kockice,4)
def petice(kockice):
    return sumaPojedinacnih(kockice, 5)
def sestice(kockice):
    return sumaPojedinacnih(kockice,6)
def malaKenta(kockice):
    return 15 if tuple(sorted(kockice)) == (1, 2, 3, 4, 5) else 0
def velikaKenta(kockice):
    return 20 if tuple(sorted(kockice)) == (2, 3, 4, 5, 6) else 0
def kenta(potez):
    if potez==1:
        return 66
    elif potez==2:
        return 56
    else:
        return 46

def jamb(kockice):
    if len(set(kockice))==1:
        suma=sum(kockice)+50
        return suma
    else:
        return 0

def ful(kockice):
    if len(set(kockice))!=2:
        return 0
    elif (len(set(sorted(kockice[0:3])))==1 and len(set(sorted(kockice[3:])))==1) or (len(set(sorted(kockice[0:2])))==1 and len(set(sorted(kockice[2:])))==1):
        return sum(kockice)+30
    else:
        return 0

def poker(kockice):
    if len(set(kockice))!=2:
        return 0
    elif len(set(sorted(kockice[0:4])))==1:
        return sum(kockice[0:4])+40
    elif len(set(sorted(kockice[1:])))==1:
        return sum(kockice[1:]) + 40
    else:
        return 0


def bacanje():#funkcija koja simulira bacanje svih pet kockica i vraca niz dobijenih kockice tj. tu kombinaciju
    kockice = []
    global seed
    for i in range(5):
        kockice.append(cube())
    return kockice

def ponovo(kockice, keep):
    #funkcija koja ponovo baca kockice koje korisnik nije izabrao da zeli da sacuva
    for i in range(len(kockice)):
        if str(i) not in keep:
            kockice[i] = cube()
        print(kockice[i], end=' ')
    print()

def sumaOdElem(vrsta, kockice, potez):#funkcija koja za prosledjenu vrstu, niz kockice i potez vraca sumu pojednacnog elementa tj. vrste u nizu
    if vrsta=='1':
        return jedinice(kockice)
    if vrsta=='2':
        return dvojke(kockice)
    if vrsta=='3':
        return trojke(kockice)
    if vrsta=='4':
        return cetvorke(kockice)
    if vrsta=='5':
        return petice(kockice)
    if vrsta=='6':
        return sestice(kockice)
    if vrsta=='kenta':
        if malaKenta(kockice)!=0:
            return malaKenta(kockice)+kenta(potez)
        elif velikaKenta(kockice)!=0:
            return velikaKenta(kockice)+kenta(potez)
        else:
            return 0
    if vrsta=='ful':
        if ful(kockice)!=0:
            return ful(kockice)+30
        else:
            return 0
    if vrsta=='poker':
        if poker(kockice)!=0:
            return poker(kockice)+40
        return 0
    if vrsta=='jamb':
        if jamb(kockice)!=0:
            return jamb(kockice)+50
        return 0

def dodajElem(kolona, vrednost, vrsta):
    #funkcija koja dodaje element u vektore R C V, povecava krajnju sumu, povecava sve sve vrste nakon te vrste za 1, ubacuje kolonu
    #gde vrsta pokazuje i na isto to mesto y nizu V vrednost koja mu je prosledjena
    for i in range(1,len(r)):
        if i>vrsta:
            r[i]+=1

    c.insert(r[vrsta], kolona)
    v.insert(r[vrsta], vrednost)

    if kolona==0:
        v[0]+=vrednost
    if kolona==1:
        v[1]+=vrednost
    if kolona==2:
        v[2]+=vrednost

def popuni(x, y, kockice, potez):#vrsta, kolona, kockice, potez
    if x=="1":
        dodajElem(y,jedinice(kockice),1)
    elif x=="2":
        dodajElem(y, dvojke(kockice), 2)
    elif x=="3":
        dodajElem(y, trojke(kockice), 3)
    elif x=="4":
        dodajElem(y, cetvorke(kockice), 4)
    elif x=="5":
        dodajElem(y, petice(kockice), 5)
    elif x=="6":
        dodajElem(y, sestice(kockice), 6)
    elif x=='kenta':
        if malaKenta(kockice)!=0:
            dodajElem(y, malaKenta(kockice)+kenta(potez), 7)
        elif velikaKenta(kockice)!=0:
            dodajElem(y, velikaKenta(kockice)+kenta(potez), 7)
        else:
            dodajElem(y,0,7)

    elif x=='ful':
        if ful(kockice)!=0:
            dodajElem(y, ful(kockice), 8)
        else:
            dodajElem(y,0,8)
    elif x=='poker':
        if poker(kockice)!=0:
            dodajElem(y, poker(kockice), 9)
        else:
            dodajElem(y,0,9)
    elif x=='jamb':
        if jamb(kockice)!=0:
            dodajElem(y, jamb(kockice), 10)
        else:
            dodajElem(y,0,10)
    else:#ako korisnik ne unese vrstu kako je naznacena, ispisuje mu se neispravna opcija
        print('Neispravna opcija')


def pretvoriumatricu():#funkcija koja trenutni RCV odnosno retku matricu pretvara u obicnu standardnu matricu,
    global m
    #prvo inicijalizuje sve elemente na '-' tj oznacava ih kao nepopunjene ali nakon toga prolaskom kroz retku matricu menja vrednosti koje postoje
    for i in range(0,11):
        m.append(['-','-','-'])
    for i in range(0,len(r)-1):
        brojElVrste=r[i+1]-r[i]#prepisuje prve tri vrednosti u V tj. sume u prvi niz matrice
        if brojElVrste>0:
            for j in range(0,r[i+1]-r[i]):
                m[i][c[r[i]+j]]=v[r[i]+j]

def ispisiMatricu():#ispis standardne matrice tj talona
    global m
    print('\t\tNAGORE:\t\tNADOLE:\t\tRUCNA:')
    for i in range(1, len(m)):
        if mapa1[i]=='kenta' or mapa1[i]=='poker'or mapa1[i]=='jamb':
            print(str(mapa1[i]).upper()+'\t\t', end='')
        else:
            print(str(mapa1[i]).upper()+'\t\t\t', end='')
        print(str(m[i][0])+'\t\t\t'+str(m[i][1])+'\t\t\t'+str(m[i][2]))
    print('SUMA:\t\t' + str(m[0][0]) + '\t\t\t' + str(m[0][1]) + '\t\t\t' + str(m[0][2]))# 0.kolomu matrice smestamo sume iz V
    print()

def printVrste(x):# fja koja ispisuje vrstu u sve tri kolone, implementirana za retku matricu
    brojElVrste=r[x+1]-r[x]
    if brojElVrste==1:
        if c[r[x]]==0:
            print('\t'+str(v[r[x]])+'\t', end='')
        else:
            print('\t' + '-' + '\t', end='')
        if c[r[x]]==1:
            print('\t\t'+str(v[r[x]])+'\t', end='')
        else:
            print('\t\t' + '-'+ '\t', end='')
        if c[r[x]]==2:
            print('\t\t'+str(v[r[x]])+'\t', end='')
        else:
            print('\t\t' + '-' + '\t', end='')
        print()
    elif brojElVrste==2:
        c[r[x]:r[x] + 2]=sorted(c[r[x]:r[x]+2])
        if c[r[x]]==0:
            print('\t'+str(v[r[x]])+'\t', end='')
            if c[r[x]+1]==1:
                print('\t\t'+str(v[r[x]+1])+'\t', end='')
            else:
                print('\t\t' + '-' + '\t', end='')
            if c[r[x]+1]==2:
                print('\t\t'+str(v[r[x]+1])+'\t', end='')
        else:
            print('\t\t' + '-'+ '\t', end='')
            if c[r[x]]==1:
                print('\t\t'+str(v[r[x]])+'\t', end='')
                if c[r[x] + 1] == 2:
                    print('\t\t' + str(v[r[x] + 1]) + '\t', end='')
            else:
                print('\t\t' + '-' + '\t', end='')
        print()
    elif brojElVrste==3:
        c[r[x]:r[x] + 3] = sorted(c[r[x]:r[x] + 3])
        print('\t' + str(v[r[x]]) + '\t'+'\t\t'+str(v[r[x]+1])+'\t'+'\t\t'+str(v[r[x]])+'\t', end='')
        print()
    else:
        print('\t'+'-'+'\t\t\t'+'-'+'\t\t\t'+'-')


def talon():# fja koja ispisuje ceo talon RETKE matrica pozivajuci prethodnu funkciju za svaku vrstu
    print('\t\tNADOLE:\t\tNAGORE:\t\tRUCNA:')
    print('1\t\t', end='')
    printVrste(1)
    print('2\t\t', end='')
    printVrste(2)
    print('3\t\t', end='')
    printVrste(3)
    print('4\t\t', end='')
    printVrste(4)
    print('5\t\t', end='')
    printVrste(5)
    print('6\t\t', end='')
    printVrste(6)
    print('KENTA\t', end='')
    printVrste(7)
    print('FUL\t\t', end='')
    printVrste(8)
    print('POKER\t', end='')
    printVrste(9)
    print('JAMB\t', end='')
    printVrste(10)
    print('SUMA:\t\t'+str(v[0])+'\t\t\t'+ str(v[1])+'\t\t\t'+ str(v[2]))
    print()


def pomocprijatelja():#funkcija koja se poziva ukoliko korisnik izabere opciju pomoc prijatelja pre prvog bacanja kockice
    global nadoleIndeks,nagoreIndeks, m, r#pokazivaci na polja u nagore i nadole kolonama koja su na redu
    kockice=bacanje()#prvo bacanje za korisnika
    print('Kockice u prvom bacanju:', end=' ')
    for i in kockice:
        print(i, end=' ')
    print()
    #odavde pokrivamo opciju da upisemo vrednost koju dobijemo u prvom bacanju u kolonu rucna ako je ona nepopunjena cela tj
    #ako postoji kombinacija koju mozemo da upisemo i ako ta kombinacija nije 0
    #trazimu najvecu vrednost koja moze da se upise u kolonu rucna od svih polja koja su preostala u toj koloni
    maks = 0
    vrsta = 0
    if len(rucna1)<10:
        for i in range(1,11):
            if mapa1[i] not in rucna1:
                if sumaOdElem(mapa1[i],kockice,1)>maks:
                    maks=sumaOdElem(mapa1[i],kockice,1)
                    vrsta=mapa1[i]
        if maks!=0:
            rucna(vrsta,kockice)
    if len(rucna1)==10 or maks==0:
        #ovde pokrivamo drugi slucaj, ukoliko je kolona rucna puna ili je najveca kombinacija koja moze da se upise
        #u neko polje kolone rucna jednaka 0 a da su pritom polja u nagore i nadole oba u gornjoj polovini tabele, tada igramo za
        #najveci broj bacnih kockica koji smo dobili u prvom bacanju, zadrzavajuci njih i igrajuci jos dva puta za to polje
        #popunjavamo matricu jer u slucaju da je cela kolona rucna popunjena znamo da ima vise od 11 elemenata i da smo presli na standardne matrice
        if nagoreIndeks<7 and nadoleIndeks<7:
            if maksBrojIstih(kockice,nadoleIndeks)>=maksBrojIstih(kockice,nagoreIndeks):
                keep=[str(x) for x in range(0,len(kockice)) if kockice[x]==nadoleIndeks]
                print('Drugo bacanje:',end=' ')
                ponovo(kockice,keep)
                if maksBrojIstih(kockice,nadoleIndeks)==5:
                    if r[-1]<11:
                        popuni(mapa1[nadoleIndeks],0,kockice,2)
                        nadoleIndeks += 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nadoleIndeks],0,kockice,2)
                        nadoleIndeks += 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                        r[-1] += 1
                else:
                    keep = [str(x) for x in range(0, len(kockice)) if kockice[x] == nadoleIndeks]
                    print('Trece bacanje:', end=' ')
                    ponovo(kockice,keep)
                    if r[-1]<11:
                        popuni(mapa1[nadoleIndeks],0,kockice,3)
                        nadoleIndeks += 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nadoleIndeks],0,kockice,3)
                        nadoleIndeks += 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 3)
                        nadoleIndeks += 1
                        r[-1] += 1
            else:
                keep = [str(x) for x in range(0, len(kockice)) if kockice[x] == nagoreIndeks]
                print('Drugo bacanje:', end=' ')
                ponovo(kockice,keep)
                if maksBrojIstih(kockice, nagoreIndeks) == 5:
                    if r[-1]<11:
                        popuni(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks-=1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                        r[-1] += 1

                else:
                    keep = [str(x) for x in range(0, len(kockice)) if kockice[x] == nagoreIndeks]
                    print('Trece bacanje:', end=' ')
                    ponovo(kockice,keep)
                    if r[-1]<11:
                        popuni(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks-=1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                        r[-1] += 1

        elif nagoreIndeks<7 and nadoleIndeks>=7:
            if verovatnoca(kockice, nadoleIndeks)>0.03:
                keep=sacuvaj(kockice,nadoleIndeks)
                print(verovatnoca(kockice, nadoleIndeks))
                print('Drugo bacanje:', end=' ')
                ponovo(kockice, keep)
                if dobijena(kockice,nadoleIndeks)==True:
                    if r[-1]<11:
                        popuni(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                        r[-1] += 1
                else:
                    keep = sacuvaj(kockice, nadoleIndeks)
                    print('Trece bacanje:', end=' ')
                    ponovo(kockice, keep)
                    if r[-1]<11:
                        popuni(mapa1[nadoleIndeks], 0, kockice, 3)
                        nadoleIndeks += 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 3)
                        nadoleIndeks += 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 3)
                        nadoleIndeks += 1
                        r[-1] += 1
            else:
                keep = [str(x) for x in range(0, len(kockice)) if kockice[x] == nagoreIndeks]
                print('Drugo bacanje:', end=' ')
                ponovo(kockice, keep)
                if maksBrojIstih(kockice, nagoreIndeks) == 5:
                    if r[-1]<11:
                        popuni(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                        r[-1] += 1
                else:
                    keep = [str(x) for x in range(0, len(kockice)) if kockice[x] == nagoreIndeks]
                    print('Trece bacanje:', end=' ')
                    ponovo(kockice, keep)
                    if r[-1]<11:
                        popuni(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                        r[-1] += 1

        elif nagoreIndeks>=7 and nadoleIndeks>=7:
            if verovatnoca(kockice, nagoreIndeks)>=verovatnoca(kockice,nadoleIndeks):
                print(verovatnoca(kockice, nagoreIndeks))
                keep=sacuvaj(kockice,nagoreIndeks)
                print('Drugo bacanje:', end=' ')
                ponovo(kockice,keep)
                if dobijena(kockice,nagoreIndeks):
                    if r[-1]<11:
                        popuni(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                        r[-1] += 1
                else:
                    keep = sacuvaj(kockice, nagoreIndeks)
                    print('Trece bacanje:', end=' ')
                    ponovo(kockice, keep)
                    if r[-1]<11:
                        popuni(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                        r[-1] += 1
            else:
                keep = sacuvaj(kockice, nadoleIndeks)
                print('Drugo bacanje:', end=' ')
                ponovo(kockice, keep)
                if dobijena(kockice, nadoleIndeks):
                    if r[-1]<11:
                        popuni(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                        r[-1] += 1
                else:
                    keep = sacuvaj(kockice, nadoleIndeks)
                    print('Trece bacanje:', end=' ')
                    ponovo(kockice, keep)
                    if r[-1]<11:
                        popuni(mapa1[nadoleIndeks], 0, kockice, 3)
                        nadoleIndeks += 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 3)
                        nadoleIndeks += 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 3)
                        nadoleIndeks += 1
                        r[-1] += 1

        elif nagoreIndeks>=7 and nadoleIndeks<7:
            print(verovatnoca(kockice, nagoreIndeks))
            if verovatnoca(kockice, nagoreIndeks)>0.03:
                keep=sacuvaj(kockice,nagoreIndeks)
                print(keep)
                print('Drugo bacanje:', end=' ')
                ponovo(kockice, keep)
                if dobijena(kockice,nagoreIndeks)==True:
                    if r[-1]<11:
                        popuni(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 2)
                        nagoreIndeks -= 1
                        r[-1] += 1
                else:
                    keep = sacuvaj(kockice, nagoreIndeks)
                    print('Trece bacanje:', end=' ')
                    ponovo(kockice, keep)
                    if r[-1]<11:
                        popuni(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nagoreIndeks], 1, kockice, 3)
                        nagoreIndeks -= 1
                        r[-1] += 1
            else:
                keep = [str(x) for x in range(0, len(kockice)) if kockice[x] == nadoleIndeks]
                print('Drugo bacanje:', end=' ')
                ponovo(kockice, keep)
                print(nadoleIndeks, nagoreIndeks)
                print(keep)
                if maksBrojIstih(kockice, nadoleIndeks) == 5:
                    if r[-1]<11:
                        popuni(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                    elif r[-1]==11:
                        pretvoriumatricu()
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                        r[-1] += 1
                    else:
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 2)
                        nadoleIndeks += 1
                        r[-1] += 1
                else:
                    keep = [str(x) for x in range(0, len(kockice)) if kockice[x] == nadoleIndeks]
                    print('Trece bacanje:', end=' ')
                    ponovo(kockice, keep)
                    if r[-1]<11:
                        popuni(mapa1[nadoleIndeks], 0, kockice, 3)
                        nadoleIndeks += 1

                    elif r[-1]==11:
                        pretvoriumatricu()
                        print(m)
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 3)
                        r[-1] += 1
                        print(m)
                        nadoleIndeks += 1
                    else:
                        popunimatricu(mapa1[nadoleIndeks], 0, kockice, 3)
                        nadoleIndeks += 1
                        r[-1] += 1

def maksBrojIstih(kockice, vrsta):
    maks = 0
    for x in kockice:
        if (x== vrsta):
            maks += 1
    return maks


def sacuvaj(kockice,indeks):
    najcesci=max(set(kockice), key = kockice.count)
    keep=[]
    if indeks==7:
        skup=set(kockice)
        for i in skup:
            keep.append(str(kockice.index(i)))
    elif indeks==8:
        if len(set(kockice))==1:#ako su svi isti cuvamo prva tri
            keep.append('0')
            keep.append('1')
            keep.append('2')
        if len(set(kockice))==3:
            for i in range(len(kockice)):
                if kockice.count(kockice[i])==2:
                    keep.append(str(i))
        if len(set(kockice))==4:
            for i in range(len(kockice)):
                if kockice[i] == najcesci:
                    keep.append(str(i))
    elif indeks==9:
        for i in range(len(kockice)):
            if kockice[i]==najcesci:
                keep.append(str(i))
    elif indeks==10:
        for i in range(len(kockice)):
            if kockice[i]==najcesci:
                keep.append(str(i))
    return keep

def dobijena(kockice,indeks):
    if indeks==7:
        if malaKenta(kockice)>0 or velikaKenta(kockice)>0:
            return True
        else:
            return False
    if indeks==8:
        if poker(kockice)>30:
            return True
        else:
            return False
    if indeks==9:
        if ful(kockice)>40:
            return True
        else:
            return False
    if indeks==10:
        if jamb(kockice)>50:
            return True
        else:
            return False

def verovatnoca(kockice,indeks):
    novi=[]
    brojac=0
    keep1 = sacuvaj(kockice, indeks)
    keep=[kockice[int(x)] for x in keep1]
    for i in range(0, 100):
        for j in range(len(kockice) - len(keep)):
            x = cube()
            novi.append(x)
        novi.extend(keep)
        if dobijena(novi,indeks):
            brojac += 1
        novi = []
    return brojac/100

def poljenaredu(kolona, vrsta):#funkcija koja proverava da li je korisnik uneo validno poljetj validnu vrstu koju zeli da popuni
    #ako nije to polje na redu onda mu izbauje gresku da nije uneo polje koje je moguce popuniti
    global nadoleIndeks
    global nagoreIndeks
    if kolona==0:
        if mapa[vrsta]==nadoleIndeks:
            nadoleIndeks+=1
            return True
        else:
            return False
    else:
        if mapa[vrsta]==nagoreIndeks:
            nagoreIndeks-=1
            return True
        else:
            return False

def popunimatricu(vrsta, kolona, kockice, potez):
    global m
    #funkcija koja kada smo presli na matricu popunjava tu matricu standardno u zavisnosti od prosledjene vrste
    if vrsta=="1":
        m[1][kolona]=jedinice(kockice)
        m[0][kolona]+=jedinice(kockice)
    elif vrsta=="2":
        m[2][kolona]=dvojke(kockice)
        m[0][kolona] += dvojke(kockice)
    elif vrsta=="3":
        m[3][kolona]=trojke(kockice)
        m[0][kolona] += trojke(kockice)
    elif vrsta=="4":
        m[4][kolona]=cetvorke(kockice)
        m[0][kolona] += cetvorke(kockice)
    elif vrsta=="5":
        m[5][kolona]=petice(kockice)
        m[0][kolona] += petice(kockice)
    elif vrsta=="6":
        m[6][kolona]=sestice(kockice)
        m[0][kolona] += sestice(kockice)
    elif vrsta=='kenta':
        if malaKenta(kockice)!=0:
            m[mapa[vrsta]][kolona]=malaKenta(kockice)+kenta(potez)
            m[0][kolona] += malaKenta(kockice)+kenta(potez)
        elif velikaKenta(kockice)!=0:
            m[mapa[vrsta]][kolona]=velikaKenta(kockice)+kenta(potez)
            m[0][kolona] += velikaKenta(kockice) + kenta(potez)
        else:
            m[mapa[vrsta]][kolona]=0
    elif vrsta=='ful':
        if ful(kockice)!=0:
            m[mapa[vrsta]][kolona]=ful(kockice)
            m[0][kolona] += ful(kockice)
        else:
            m[mapa[vrsta]][kolona]=0
    elif vrsta=='poker':
        if poker(kockice)!=0:
            m[mapa[vrsta]][kolona]=poker(kockice)
            m[0][kolona] += poker(kockice)
        else:
            m[mapa[vrsta]][kolona]=0
    elif vrsta=='jamb':
        if jamb(kockice)!=0:
            m[mapa[vrsta]][kolona]=jamb(kockice)
            m[0][kolona] += jamb(kockice)
        else:
            m[mapa[vrsta]][kolona]=0
    else:
        print('Neispravna opcija')

def rucna(vrsta, kockice):#fja koja popunjava polje u koloni rucna ako ono vec nije u toj koloni
    if vrsta not in rucna1:
        rucna1.append(vrsta)
        if r[-1]<11:#ako je idalje retka matrica u upotrebi
            popuni(vrsta,2, kockice, 1)
        elif r[-1]==11:
            pretvoriumatricu()
            popunimatricu(vrsta,2,kockice,1)
            r[-1]+=1
        else:
            popunimatricu(vrsta,2,kockice,1)
            r[-1]+=1
    else:
        print('Polje je vec popunjeno!\n')

def meni3(kockice, potez):#meni koji daje korisniku opcije da popuni polaj koja su dozvoljena ili da ih precrat oznacivsi
    #ih sa 0 bodova, poziva se ukoliko korisnik ne unese polje u kolona nagore ili nadole, koje je na redu
    global nadoleIndeks, nagoreIndeks
    popunjeno=input('\nIzaberite koje polje zelite da popunite (upisom 1 za prvo dozvoljeno/ 2 za drugo dozvoljeno)\nDozvoljena polja su: Nadole:'+str(nadoleIndeks)+' Nagore:'+str(nagoreIndeks)+'\n')
    if r[-1]<11:
        if popunjeno=='1':
            popuni(mapa1[nadoleIndeks],0,kockice, potez)
            poljenaredu(0,mapa1[nadoleIndeks])
        if popunjeno=='2':
            popuni(mapa1[nagoreIndeks],1,kockice,potez)
            poljenaredu(1, mapa1[nagoreIndeks])
    elif r[-1]==11:
        pretvoriumatricu()
        if popunjeno=='1':
            popunimatricu(mapa1[nadoleIndeks],0,kockice,potez)
            poljenaredu(0, mapa1[nadoleIndeks])
            r[-1]+=1
        if popunjeno=='2':
            popunimatricu(mapa1[nagoreIndeks], 1, kockice, potez)
            poljenaredu(1, mapa1[nagoreIndeks])
            r[-1] += 1
    else:
        if popunjeno=='1':
            popunimatricu(mapa1[nadoleIndeks],0,kockice,potez)
            poljenaredu(0, mapa1[nadoleIndeks])
            r[-1]+=1
        if popunjeno=='2':
            popunimatricu(mapa1[nagoreIndeks], 1, kockice, potez)
            poljenaredu(1, mapa1[nagoreIndeks])
            r[-1] += 1


def meni(kockice):#GLAVNI MENI, za prosledjen niz kockice, daje korisniku mogucnost iybora da li zeli da upise neku vrednost u kolonu
    #rucna ili da ponovo baci kockice
    b = input('----------GLAVNI MENI------------\n'
        'Odaberite jednu od opcija:\n1.popunjavam kolonu "rucna"\n2.novo bacanje\n')
    b=int(b)
    if b == 1:
        vrsta=input('Odaberite koje polje kolone rucna zelite da popunite/precrtate (1-6, "kenta", "ful", "poker", "jamb")\n')
        rucna(vrsta, kockice)#popunjava kolonu rucna sa vrstom koju korisnik unosi
    elif b==2:
        keep=input('Odaberite koje kockice zelite da sacuvate navodjenjem njihovih indeksa (krecu od 0):\n')
        keep=keep.split()#keep je niz u kome se cuvaju vrednsoti koje korisnik zeli da ostanu iste prilikom sledeceg bacanja
        print('Drugo bacanje:')
        ponovo(kockice, keep)#ponovno bacanje, ispisuje nove kockice
        c=input('Odaberite jednu od opcija:\n1.novo bacanje\n2.popunjavanje polja na talonu\n')#opcije posle drugog bacanja
        c=int(c)
        if c==1:
            keep1=input('Odaberite koje kockice zelite da sacuvate navodjenjem njihovih indeksa (krecu od 0):\n')
            keep1 = keep1.split()
            print('Trece bacanje:')
            ponovo(kockice, keep1)
            #posle treceg bacanja mora se uneti neka suma u neko polje ili se neko polje prcrtati, stoga sledece opcije
            unos=input('Sada morate odbarati koje polje na talonu zelite da popunite/precrtate :(nadole-"0", nagore-"1"; 1-6, "kenta", "ful", "poker", "jamb")\n')
            kolona, vrsta=unos.split()#dajem korisniku mogucnost da kaze sam znajuci svoje kockice koje polje zeli da unese i u koju kolonu
            #ako ta polja nisu na redu, posto se rucna vise ne moze popunjavati, to se moze desiti, onda dobija novi meni koje ga ogranicava
            #da unese koju opciju od dve ponudjene tj koje polje od dva dozvolje yeli da unese, objasnjeno gore u meni3
            kolona=int(kolona)
            if poljenaredu(kolona,vrsta):#provera da li je polje zaista na redu
                if r[-1]<11:#broj 11 koji se vise puta ponavlja, dobija se formulom NNZ < (m (n − 1) − 1) / 2, tj. koristimo retke matrice dok je
                    #to isplativo, a isplativo je kada je manje od 11 po ovoj formuli, elemenata u retkoj matrici, nakon toga pretvaramo retku matricu
                    #u obicnu i na dalje popunjavamo nju
                    popuni(vrsta, kolona,kockice, 3)
                elif r[-1]==11:
                    pretvoriumatricu()
                    popunimatricu(vrsta,kolona,kockice,3)
                    r[-1]+=1
                else:
                    popunimatricu(vrsta,kolona,kockice,3)
                    r[-1]+=1
            else:
                print('Niste izabrali polje koje je moguce popuniti!')
                meni3(kockice,3)
            print('Kraj poteza\n')
        else:
            unos = input('Odaberite koje polje na talonu zelite da popunite/precrtate :(nadole-"0", nagore-"1"; 1-6, "kenta", "ful", "poker", "jamb")\n')
            kolona, vrsta=unos.split()
            kolona= int(kolona)
            if poljenaredu(kolona,vrsta):
                if r[-1]<11:
                    popuni(vrsta, kolona, kockice, 2)
                elif r[-1]==11:
                    pretvoriumatricu()
                    popunimatricu(vrsta,kolona,kockice,2)
                    r[-1]+=1
                else:
                    popunimatricu(vrsta,kolona,kockice,2)
                    r[-1]+=1#idalje u poslenjem elementu vektora r cuvamo broj popunjenih polja
            else:
                print('Niste izabrali polje koje je moguce popuniti!')
                meni3(kockice,2)
            print('Kraj poteza\n')
    else:
        print('Izabrali ste nevalidnu opciju.')


def meni2():#prekida program ako korisnik unese opciju kraj igre
    a=input('Izaberite jednu od ponudjenih opcija:\n1.novi potez\n2.kraj igre\n')
    if a=='2':
        return False
    else:
        return True
#main
setSeed(int(datetime.now().microsecond))#inicijalizacija seeda preko datetime biblio
a=input('Dobro dosli! Da li zelite da zapocnete igru i bacite kocku?(da/ne)\n')
if a!='da':
    print('Kraj igre')
else:
    #stvara prazan talon i inicijalizuje RCV vekore
    inicijalizujTalon()
    while True:#sve dok korisnik ne odabere opciju Kraj igre ili je talon popunjen
        x=input('Da li zelite pomoc prijatelja?(da/ne)\n')
        if x=='da':
            pomocprijatelja()
        else:
            print('Prvo bacanje:', end=' ')
            kockice=bacanje()
            for i in range(len(kockice)):
                print(kockice[i], end=" ")
            print()
            meni(kockice)
        print('\t\t\t\tTRENUTNI TALON:')
        if r[-1]<=11:#za retku matricu ispisuje talon na drugaciji nacin
            talon()
        else:
            ispisiMatricu()
        x=meni2()#ako je izabrana opcija Kraj igre
        if x==False:
            break
        if r[-1]==36:#ako su sva polja popunjena: kraj igre
            break
    #nakon while, kada je cela IGRA gotova, ispisuje konacnu sumu koju je korisnik ostvraio, sumira sve sume kolona nagore, nadole, rucna
    if r[-1]<11:
        print('KONACNA SUMA :', sum(v[0:3]), end="")
    else:
        print('KONACNA SUMA :', sum(m[0][0:3]), end="")

