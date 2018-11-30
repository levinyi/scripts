from Bio.SubsMat import MatrixInfo


def score_match(pair, matrix):
    # return a score,

    if pair not in matrix:
        return matrix[(tuple(reversed(pair)))]
    else:
        return matrix[pair]


def score_pairwise(seq1, seq2, matrix, gap_s, gap_e):
    # create a zero-filled matrix
    for i in xrange(1,len(seq1)+1):
        pair = (seq1[i], seq2[i])
        


def make_matrix(sizex, sizey):
    """Creates a sizex by sizey matrix filled with zeros."""
    return [[0] * sizey for i in xrange(sizex)]

def local_align(x, y, score=ScoreParam(10, -5, -7)):
    """Do a local alignment between x and y with the given scoring parameters.
    We assume we are MAXIMIZING."""

    # create a zero-filled matrix
    A = make_matrix(len(x) + 1, len(y) + 1)

    best = 0
    optloc = (0,0)

    # fill in A in the right order
    for i in xrange(1, len(x)+1):
        for j in xrange(1, len(y)+1):

            # the local alignment recurrance rule:
            A[i][j] = max(
               A[i][j-1] + score.gap,
               A[i-1][j] + score.gap,
               A[i-1][j-1] + score.matchchar(x[i-1], y[j-1]),
               0
            )

            # track the cell with the largest score
            if A[i][j] >= best:
                best = A[i][j]
                optloc = (i,j)

    print "Scoring:", str(score)
    print "A matrix ="
    print_matrix(x, y, A)
    print "Optimal Score =", best
    print "Max location in matrix =", optloc
    # return the opt score and the best location
    return best, optloc
if __name__ == '__main__':
    seq1 = 'ATAAATGTATTTATGATTGATGTATTTTTTTACATGGATTTTTTCGTCCCAAAAAGGG'
    seq2 = 'ATAAATGTATTTATGATTGTTAACTTTTTTTAGGGGGATTTTTTCGTCCCAAAAAGGG'
    blosum = MatrixInfo.blosum62

    gap_s = -5
    gap_e = 0.5
    print score_pairwise(seq1, seq2, blosum, gap_s, gap_e)
    print make_matrix(len(seq1), len(seq2))
