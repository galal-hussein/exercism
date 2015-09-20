def distance(dna_1, dna_2):
    d = 0
    for i in range(min(len(dna_1), len(dna_2))):
        if dna_1[i] != dna_2[i]:
            d += 1
    return d
