import random

def genPopulasi(nPop,nKrom):
    pop = [[int(round(random.random())) for i in range(nKrom)] for j in range(nPop)]
    return pop

def randomParent(nPop):
    return int(round(random.uniform(0,nPop)))

def hitungFitness(krom,weight,value,max):
    w = 0
    v = 0
    for i in range(len(krom)):
        if krom[i] == 1:
            w = w + weight[i]
            v += value[i]
    if w > max:
        fitness = 0
    else:
        fitness = v
    return  fitness

if __name__ == '__main__':

    barang = ['Nila','Gurame','Kakap','Lele','Mujair']
    weight = [2,7,4,1,1]
    value = [50000,70000,60000,15000,25000]
    max = 12

    nPop = 4
    nGen = 10
    nKrom = len(barang)

    pop = genPopulasi(nPop,nKrom)
    print pop

    pCross = 0.8
    pMutasi = 0.1



    for i in range(nGen):
        anak = []
        fitness = []
        for j in range(nPop/2):
            parent1 = randomParent(nPop-1)
            parent2 = randomParent(nPop-1)

            anak1 = pop[parent1][:]
            anak2 = pop[parent2][:]

            # crossover
            rand = random.random()
            titik = int(round(random.uniform(0,nKrom-1)))
            if rand <= pCross:
                for k in range(titik):
                    anak1[k],anak2[k] = anak2[k],anak1[k]

            # mutasi
            rand = random.random()
            titik = int(random.uniform(0, nKrom - 1))
            if rand <= pMutasi:
                if anak1[titik] == 0:
                    anak1[titik]=1
                else:
                    anak1[titik]=0

            rand = random.random()
            titik = int(random.uniform(0, nKrom - 1))
            if rand <= pMutasi:
                if anak2[titik]==0:
                    anak2[titik]=1
                else:
                    anak2[titik]=0
            anak.append(anak1)
            anak.append(anak2)

        # print anak
        gab = pop + anak
        for j in range(len(gab)):
            fitness.append(hitungFitness(gab[j],weight,value,max))
        print fitness
        steadyState = sorted(range(len(fitness)),key=lambda k:fitness[k],reverse=True)
        print steadyState

        pop = []
        for j in range(nPop):
            pop.append(gab[steadyState[j]])
        print pop

print "Jumlah nilai :", fitness[steadyState[0]]
for i in range(nKrom):
    if pop[0][i] == 1:
        print barang[i],