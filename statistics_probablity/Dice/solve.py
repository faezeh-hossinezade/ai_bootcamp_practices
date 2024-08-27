# coding: utf-8
def solve(numb):
    import numpy as np
    totalprob=float(0)
    populationone =  np.array([1, 2, 3, 4, 5, 6])
    populationtwo =  np.array([1, 2, 3, 4, 5, 6])
    weights = [1/24,1/12, 1/6, 1/2, 1/8, 1/12]
    for i in range(len(populationone)):
        for j in range(len(populationtwo)):
            cal=populationone[i]*populationtwo[j]
            if cal>numb:
                totalprob+=weights[i]*weights[j]

    return(totalprob)
