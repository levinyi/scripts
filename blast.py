

def score(a, b):
    score = 0
    lst = ['AC', 'GT', 'CA', 'TG']
    if a == b:
        score += 2
    elif a + b in lst:
        score += -5
    else:
        score += -7
    return score


def BLAST(seq1, seq2):
    l1 = len(seq1)
    l2 = len(seq2)
    GAP = -5
    scores = []
    point = []
    for j in range(l2 + 1):
        print j
        if j == 0 :# first position
            line1 = [0]
            line2 = [0]
            for i in range(1,l1+1):
                line1.append(GAP*i)
                line2.append(2)
        else:
            line1 = []
            line2 = []
            line1.append(GAP*j)
            line2.append(3)
        scores.append(line1)
        point.append(line2)
    print scores
    print point

    for j in range(1,l2+1):
        letter2 = seq2[j-1]
        print letter2
# a = 'ATAAATGTATTTATGATTGATGTATTTTTTTACATGGATTTTTTCGTCCCAAAAAGGG'
# b = 'ATAAATGTATTTATGATTGTTAACTTTTTTTAGGGGGATTTTTTCGTCCCAAAAAGGG'
a = 'ATAAATGTAT'
b = 'ATAATTCTAT'
BLAST(a,b)