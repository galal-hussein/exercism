def word_count(line):
    d = dict()
    for w in line.split():
        d[w] = d.get(w, 0) + 1
    return d
