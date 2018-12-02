import sys


def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


ids = []
for line in sys.stdin:
    ids.append(line)

for i in range(0, len(ids)):
    for j in range(i + 1, len(ids)):
        dist = levenshteinDistance(ids[i], ids[j])
        if dist == 1:
            similars = []
            for k in range(0, len(ids[i])):
                if ids[i][k] == ids[j][k]:
                    similars.append(ids[i][k])
            print("".join(similars))
            sys.exit()
            


