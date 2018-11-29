

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

def PAM_matrix_score(a,b):
    score = 0

    return score

def Blosum_matrix_score(a,b):


    score = 0
    lst = []
    
    if sss:
        lanbuda = 4
    else:
        lanbuda = 20
    S = (1/lanbuda)log(pij/qi*qj)
    return score

def BLAST(seq1, seq2):
    l1 = len(seq1)
    l2 = len(seq2)
    GAP = -5
    scores = []
    point = []
    for j in range(l2 + 1):
        # print j
        if j == 0:  # first position
            line1 = [0]
            line2 = [0]
            for i in range(1, l1 + 1):
                line1.append(GAP * i)
                line2.append(2)
        else:
            line1 = []
            line2 = []
            line1.append(GAP * j)
            line2.append(3)
        scores.append(line1)
        point.append(line2)

    for j in range(1, l2 + 1):
        letter2 = seq2[j - 1]
        # print letter2
        for i in range(1, l1 + 1):
            letter1 = seq1[i - 1]
            diagonal_score = score(letter1, letter2) + scores[j - 1][i - 1]
            # print diagonal_score
            left_score = GAP + scores[j][i - 1]
            up_score = GAP + scores[j - 1][i]
            max_score = max(diagonal_score, left_score, up_score)
            scores[j].append(max_score)

            if scores[j][i] == diagonal_score:
                point[j].append(1)
            elif scores[j][i] == left_score:
                point[j].append(2)
            else:
                point[j].append(3)
    # print "scores: ", scores
    # print "point: ", point
    alignment1 = ''
    alignment2 = ''
    i = l2
    j = l1
    print "scores = ", scores[i][j]
    while True:
        if point[i][j] == 0:
            break
        elif point[i][j] == 1:
            alignment1 += seq1[j - 1]
            alignment2 += seq2[i - 1]
            i -= 1
            j -= 1
        elif point[i][j] == 2:
            alignment1 += seq1[j - 1]
            alignment2 += '-'
            j -= 1
        else:
            alignment1 += '-'
            alignment2 += seq2[i - 1]
            i -= 1
    alignment1 = alignment1[::-1]
    alignment2 = alignment2[::-1]
    print "the best alignment : "
    print alignment1
    print alignment2
a = 'ATAAATGTATTTATGATTGATGTATTTTTTTACATGGATTTTTTCGTCCCAAAAAGGG'
b = 'ATAAATGTATTTATGATTGTTAACTTTTTTTAGGGGGATTTTTTCGTCCCAAAAAGGG'
# a = 'ATAAATGTAT'
# b = 'ATAATTCTAT'

BLAST(a, b)
