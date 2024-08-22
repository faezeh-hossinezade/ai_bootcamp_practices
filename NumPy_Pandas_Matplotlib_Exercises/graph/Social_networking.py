import numpy as np

def calculate_percentages(l):
    def is_in_box(a, b):
        return ([a, b] in l) or ([b, a] in l)
    names = np.unique(np.array(l).flatten())
    namescopy = names.copy()

    nmc = np.zeros(len(names), dtype=int)
    for i, name in enumerate(names):
        nmc[i] = np.sum([is_in_box(name, other) for other in names])

    sorted_indices = np.argsort(nmc)[::-1]
    sorted_names = names[sorted_indices][:10]

    nmp1 = [[name] for name in namescopy]
    for i, name in enumerate(namescopy):
        for other in namescopy:
            if is_in_box(name, other):
                nmp1[i].append(other)

    nmp2 = [[name] for name in sorted_names]
    for i, name in enumerate(sorted_names):
        for other in namescopy:
            if is_in_box(name, other):
                nmp2[i].append(other)
                
    nmp2 = sorted(nmp2, key=lambda x: (-len(x), x[0]))          

    sl1 = nmp2[:5]
    sl2 = nmp2[5:10]
    # print(sl1)
    # print(sl2)

    sl12 = np.unique(np.concatenate(sl1))
    # print(sl12)
    sl22 = np.unique(np.concatenate(sl2))
    # print(sl22)
    percentage1 = len(sl12) / len(namescopy)
    percentage2 = len(sl22) / len(namescopy)

    return round(percentage1, 3), round(percentage2, 3)

l = [['Zahra','Mona'], ['Saeed','Reza'], ['Amin','Narges'], ['Milad','Armin'], ['Majid', 'Mona'], ['Mona', 'Reza'], ['Zahra', 'Sara'], ['Sara', 'Amin'], ['Narges', 'Saeed'], ['Sara', 'Majid'], ['Ahmad', 'Abbas'], ['Abbas', 'Mona'], ['Saman', 'Reza'], ['Sara', 'Ahmad'], ['Iman', 'Ahmad'], ['Javad', 'Abbas'], ['Kamand', 'Sara'], ['Narges', 'Matin'], ['Saghi', 'Narges'], ['Omid', 'Reza'], ['Omid', 'Iman'], ['Abbas', 'Omid'], ['Javad', 'Omid'], ['Ahmad', 'Saghi']] 

print(calculate_percentages(l))