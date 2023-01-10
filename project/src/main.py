import numpy as np
from function import *
# Algorithm Parameters
iterations = 10
colony = 20
alpha = 1
beta = 1
del_tau = 1.0
rho = 0.5
# Open input file
infile = open("../data/berlin52.tsp", 'r')
# Read instance
name = infile.readline().strip().split()[1]                     # NAME
type = infile.readline().strip().split()[1]                     # TYPE
comment = infile.readline().strip().split()[1]                  # COMMENT
dimension = infile.readline().strip().split()[1]                # DIMENSION
edge_weight_type = infile.readline().strip().split()[
    1]         # EDGE_WEIGHT_TYPE
# NODE_COORD_SECTION
node_coord_section = []
infile.readline()

# Read node coord section and store its x, y coordinates
for i in range(0, int(dimension)):
    x, y = infile.readline().strip().split()[1:]
    node_coord_section.append([float(x), float(y)])

# Close input file
infile.close()

# File as dictionary
data = {
    'name': name,
    'type': type,
    'comment': comment,
    'dimension': dimension,
    'edge_weight_type': edge_weight_type,
    'node_coord_section': node_coord_section
}


def displayTspHeaders(dict):
    print('\nName: ', dict['name'])
    print('Type: ', dict['type'])
    print('Comment: ', dict['comment'])
    print('Dimension: ', dict['dimension'])
    print('Edge Weight Type: ', dict['edge_weight_type'], '\n')


space = np.array(node_coord_section)
# print(initializeAnts(space, colony))
# Empty minimum distance and path
min_distance = None
min_path = None
p = intializePheromone(space)
for iteration in range(iterations):
    edge = Distances(space)
    ants = initializeAnts(space, colony)
    for ant in range(0, colony):
        path = moveAnt(ants[ant], edge, alpha, beta, p)
        dest = distensInPath(path, edge)
        if not min_distance or dest < min_distance:
            min_distance = dest
            min_path = path
        p = pheromoneUpdat(p, rho, path, edge)
print("min d :", min_distance)
print("path:", min_path)
