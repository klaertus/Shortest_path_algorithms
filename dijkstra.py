import numpy as np



test_matrix = np.array([
                #A,B,C,D,E,F,G,H,I,J
                [0,5,1,2,np.NAN,np.NAN,np.NAN,np.NAN,np.NAN,np.NAN], #A
                [5,0,3,np.NAN,1,np.NAN,3,np.NAN,np.NAN,np.NAN], #B
                [1,3,0,1,4,1,np.NAN,np.NAN,np.NAN,np.NAN], #C
                [2,np.NAN,1,0,np.NAN,1,np.NAN,np.NAN,3,np.NAN], #D
                [np.NAN,5,4,np.NAN,0,3,5,5,np.NAN,np.NAN], #E
                [np.NAN,np.NAN,1,1,3,0,np.NAN,5,1,np.NAN], #F
                [np.NAN,3,np.NAN,np.NAN,5,np.NAN,0,4,np.NAN,1], #G
                [np.NAN,np.NAN,np.NAN,np.NAN,5,5,4,0,5,2], #H
                [np.NAN,np.NAN,np.NAN,3,np.NAN,1,np.NAN,5,0,5], #I
                [np.NAN,np.NAN,np.NAN,np.NAN,np.NAN,np.NAN,1,2,5,0]  #J
                ])


def dijkstra(matrix):

    def neighbors(x):
        return [i for i in range(0,len(matrix[x])) if (not np.isnan(matrix[x][i]) and matrix[x][i] != 0)]

    def lengh(x,y):
        return matrix[x][y]

    # Initialization
    matrix = np.squeeze(np.asarray(matrix))
    output_matrix = []

    for point in range(0,len(matrix)):

        # Verticles
        S = []

        # Todo vertices
        X = [i for i in range(0,len(matrix[0]))]

        # Distance
        D =[]
        for i in range(0,len(matrix[0])):
            D.append(np.inf)
        D[point] = 0

        # Predecessor
        P = []
        for i in range(0,len(matrix[0])):
            P.append(0)

        i = 0
        while len(S) != len(X):

            x = D.index(min(D))
            temp = []
            if x in S:
                temp = [i for i in range(0,len(D)) if i not in S]
                x = min(temp)

            S.append(x)

            for y in neighbors(x):
                if D[y] >  D[x] + lengh(x,y):
                    D[y] =  D[x] + lengh(x,y)
                    P[y] = x

        output_matrix.append(D)

    return output_matrix


print(dijkstra(test_matrix))
