from Bio.SubsMat import MatrixInfo


def score_match(pair, matrix):
    # return a score,

    if pair not in matrix:
        return matrix[(tuple(reversed(pair)))]
    else:
        return matrix[pair]

def score_matrix(pair,matrix):
    if pair[1] == pair[0]:
        return matrix['match']
    else:
        return matrix['mismatch']

def make_matrix(sizex, sizey):
    """Creates a sizex by sizey matrix filled with zeros."""
    return [[0] * sizey for i in xrange(sizex)]


def local_align(seq1, seq2, matrix, gap_open, gap_extend):
    # create a zero-filled matrix
    A = make_matrix(len(seq1) + 1, len(seq2) + 1)

    best = 0
    optloc = (0, 0)

    # fill in A in hte right order
    for i in xrange(1, len(seq1) + 1):
        for j in xrange(1, len(seq2) + 1):
            pair = (seq1[i - 1], seq2[j - 1])

            A[i][j] = max(
                # A[i - 1][j - 1] + score_match(pair, matrix),
                A[i - 1][j - 1] + score_matrix(pair, matrix),
                A[i][j - 1] + gap_open,
                A[i - 1][j] + gap_open,
                0
            )
            if A[i][j] >= best:
                best = A[i][j]
                optloc = (i, j)

    # track back
    '''
    alignment1 = ''
    alignment2 = ''
    i = len(seq1)
    j = len(seq2)
    while True:
        if A[i][j] == 0:
            if A[i - 1][j] < A[i][j - 1]:
                alignment1 += "-"
                alignment2 += seq2[i - 1]
                i -= 1
            else:
                alignment1 += seq1[i - 1]
                alignment2 += '-'
                j -= 1
        else:
            alignment1 += seq1[j - 1]
            alignment2 += seq2[i - 1]
            i -= 1
            j -= 1
    alignment1 = alignment1[::-1]
    alignment2 = alignment2[::-1]
    print alignment1
    print alignment2
    '''
    print "score table is :", matrix
    print "A matrix ="
    print_matrix(seq1, seq2, A)
    print "Optimal Score =", best
    print "Max location in matrix =", optloc
    # return the opt score and the best location
    return best, optloc

def global_align(seq1, seq2, matrix, gap_open, gap_extend):
    # create a zero-filled matrix
    A = make_matrix(len(seq1) + 1, len(seq2) + 1)

    best = 0
    optloc = (0, 0)

    # fill in A in hte right order
    for i in xrange(1, len(seq1) + 1):
        for j in xrange(1, len(seq2) + 1):
            pair = (seq1[i - 1], seq2[j - 1])

            A[i][j] = max(
                A[i - 1][j - 1] + score_match(pair, matrix),
                A[i][j - 1] + gap_open,
                A[i - 1][j] + gap_open
            )
            if A[i][j] >= best:
                best = A[i][j]
                optloc = (i, j)

    print "substitution matrix is :", matrix
    print "A matrix ="
    print_matrix(seq1, seq2, A)
    print "Optimal Score =", best
    print "Max location in matrix =", optloc
    # return the opt score and the best location
    return best, optloc

def print_matrix(x, y, A):
    """Print the matrix with the (0,0) entry in the top left
    corner. Will label the rows by the sequence and add in the
    0-row if appropriate."""

    # decide whether there is a 0th row/column
    if len(x) == len(A):
        print "%5s" % (" "),
    else:
        print "%5s %5s" % (" ", "*"),
        y = "*" + y

    # print the top row
    for c in x:
        print "%5s" % (c),
    print

    for j in xrange(len(A[0])):
        print "%5s" % (y[j]),
        for i in xrange(len(A)):
            print "%5.0f" % (A[i][j]),
        print


if __name__ == '__main__':
    # seq1 = 'ATAAATGTATTTATGATTGATGTATTTTTTTACATGGATTTTTTCGTCCCAAAAAGGG'
    # seq2 = 'ATAAATGTATTTATGATTGTTAACTTTTTTTAGGGGGATTTTTTCGTCCCAAAAAGGG'
    # seq1 = 'AAGT'
    # seq2 = 'AGCT'
    seq1 = 'COMSPARES'
    seq2 = 'REPAIRS'
    blosum = MatrixInfo.blosum62
    # print blosum
    pam = {
        ('A', 'A'): 2,
        ('C', 'A'): -7, ('C', 'C'): 2,
        ('G', 'A'): -5, ('G', 'C'): -7, ('G', 'G'): 2,
        ('T', 'A'): -7, ('T', 'C'): -5, ('T', 'G'): -7, ('T', 'T'): 2,
    }
    other = {
        'match' :2,
        'mismatch' :-1
    }
    gap_open = -1
    gap_extend = 0
    A = local_align(seq1, seq2, other, gap_open, gap_extend)
    # A = local_align(seq1, seq2, pam, gap_open, gap_extend)
    # global_align(seq1,seq2,pam,gap_open,gap_extend)
    # print make_matrix(len(seq1), len(seq2))
