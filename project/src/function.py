import numpy as np
import math


def Distances(data):
    # Empty multidimensional array (matriz) to distances
    distances = np.zeros((data.shape[0], data.shape[0]))
    # Calculate distance to all nodes to all nodes
    # for index, point in enumerate(data):
    #     distances[index] = np.sqrt(((data - point) ** 2).sum(axis=1))
    # return distances
    for i in range(data.shape[0]):
        for j in range(data.shape[0]):
            distances[j][i] = math.sqrt(
                ((data[i][0]-data[j][0])**2)+((data[i][1]-data[j][1])**2))
    return distances


"""
    Initialize ants - Get an array of random initial positions of the ants in space
    @arg
        {numpy.ndarray} space   -- The space
        {int} colony            -- Number of ants in the colony

    @return
        {numpy.ndarry}          -- An array of indexes of initial positions of ants in the space
"""


def initializeAnts(space, colony):
    # Indexes of initial positions of ants
    return np.random.randint(space.shape[0], size=colony)


def intializePheromone(space):
    pheromone = np.ones((space.shape[0], space.shape[0]))
    return pheromone


def moveAnt(postion, edges, alpha, beta, pheromoen):
    # create array of the path of the ant (size of cities number)
    path = np.zeros(edges.shape[0])
    # Position is the number of current city
    path[0] = postion
    for posAnt in range(0, edges.shape[0]-1):
        # array of proba
        ProbaForEachEdge = np.zeros(edges.shape[0])
        # Calculate the proba of all not visited
        for indexCity in range(edges.shape[0]):
            if (indexCity in path):
                ProbaForEachEdge[indexCity] = 0.0
                continue
            # Calculate proba of the edge between position( of ant ) and indexCity
            if edges[posAnt][indexCity] == 0:
                continue
            numerateur = (pheromoen[posAnt][indexCity] **
                          alpha) + (1/edges[posAnt][indexCity]**beta)
            denumerateur = (pheromoen[posAnt].sum() **
                            alpha) + (1/edges[posAnt].sum() ** beta)
            ProbaForEachEdge[indexCity] = (numerateur/denumerateur)
        posMax = 0
        maxVlue = ProbaForEachEdge[0]
        for i in range(1, ProbaForEachEdge.shape[0]):
            if ProbaForEachEdge[i] > maxVlue:
                posMax = i
        path[posAnt+1] = posMax
    path = np.append(path, postion)
    return path

# fgeurgfirgzeiugifg


def distensInPath(path, edges):
    d = 0
    for k in range(path.shape[0]-1):
        d = d + edges[int(path[k])][int(path[k+1])]
    return d


def pheromoneUpdat(pheromone, rho, lastPath, edges):
    d = distensInPath(lastPath, edges)
    for i in range(pheromone.shape[0]):
        for j in range(pheromone.shape[0]):
            if i == j:
                pheromone[i][j] = 0.0
                continue
            pheromone[i][j] = pheromone[i][j]*(1-rho)+(1/d)
    return pheromone
