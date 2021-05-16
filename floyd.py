import numpy as np



test_matrix = np.array([
                #A,B,C,D,E,F,G,H,I,J
                [0,5,1,2,np.NAN,np.NAN,np.NAN,np.NAN,np.NAN,np.NAN], #A
                [5,0,3,np.NAN,5,np.NAN,3,np.NAN,np.NAN,np.NAN], #B
                [1,3,0,1,4,1,np.NAN,np.NAN,np.NAN,np.NAN], #C
                [2,np.NAN,1,0,np.NAN,1,np.NAN,np.NAN,3,np.NAN], #D
                [np.NAN,5,4,np.NAN,0,3,5,5,np.NAN,np.NAN], #E
                [np.NAN,np.NAN,1,1,3,0,np.NAN,5,1,np.NAN], #F
                [np.NAN,3,np.NAN,np.NAN,5,np.NAN,0,4,np.NAN,1], #G
                [np.NAN,np.NAN,np.NAN,np.NAN,5,5,4,0,5,2], #H
                [np.NAN,np.NAN,np.NAN,3,np.NAN,1,np.NAN,5,0,5], #I
                [np.NAN,np.NAN,np.NAN,np.NAN,np.NAN,np.NAN,1,2,5,0]  #J
                ])


def floyd(matrix):

    def neighbors(x):
         return [i for i in range(len(matrix[x])) if (not np.isnan(matrix[x][i]) and matrix[x][i] != 0)]

    # Shortest path matrix
    M = np.array(np.ones((len(matrix), len(matrix))) * np.inf)
    for i in range(len(matrix)):
        M[i][i] = 0
        for j in neighbors(i):
            M[i][j] = matrix[i][j]


    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):

                if M[i][k] + M[k][j] < M[i][j]:
                    M[i][j] = M[i][k] + M[k][j]

    return M


floyd(test_matrix)
