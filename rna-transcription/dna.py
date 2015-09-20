def to_rna(dna_strand):
    dna_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join([dna_rna[x] for x in dna_strand])
