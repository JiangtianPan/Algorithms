import argparse
import numpy as np
import os
# hyper parameter for training
parser = argparse.ArgumentParser()
parser.add_argument('-database_file', default = 'database.txt')
parser.add_argument('-k', default = 'k')
parser.add_argument('-max_iters', default = 'n')
parser.add_argument('-eps', default = 'e')
parser.add_argument('-output_file', default = 'output.txt')

args = parser.parse_args()

database_file = str(args.database_file)
k = int(args.k)
max_iters = int(args.max_iters)
eps = float(args.eps)
output_file = str(args.output_file)

def read_data(database_file):
    data = np.loadtxt(database_file)
    #print(data)
    num_row = data.shape[0]
    num_column = data.shape[1]
    #print(num_row, num_column)
    # 500 points, 550 features
    return data, num_row, num_column

def genKmeans(database, k, max_iters, eps, output_file):
    data, num_row, num_column = read_data(database)
    # randomly choose k centers, saved in the centroids (list)
    # number of features
    n = data.shape[1] # 550 features
    centroids = np.empty((k, n))
    for i in range(n):
        min_i = min(data[:, i])
        range_i = max(data[:, i] - min_i)
        # flatten the nested list
        centroids[:, i] = (min_i+range_i*np.random.rand(k, 1)).flatten()
    print(centroids.shape[0], centroids.shape[1])
    # 10, 500
    
    # repeat until the clusters are eps
    num_data = data.shape[0] # 500 points
    clusterAssment = np.zeros((num_data, 2))# [cluster number, distance]
    # 500, 2
    iteration = True
    for _ in range(max_iters):
        iteration = False
        for i in range(num_data):
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                numA = centroids[j, :] # one centroid
                numB = data[i, :] # one point
                # calculate the distance between data and the centroids
                dist = np.math.sqrt(sum(np.power(numA-numB, 2)))

                if dist < minDist:
                    minDist = dist
                    minIndex = j

            if clusterAssment[i, 0] != minIndex or clusterAssment[i, 1] > minDist**2:
                iteration =  True
                clusterAssment[i, :] = minIndex, minDist**2

        # if the clustering has converged, stop the iteration
        if not iteration:
            break
        for i in range(k):
            # obtain the index of the cluster
            index = clusterAssment[:, 0]
            value = np.nonzero(index == i)
            data_in_cluster = data[value[0]]
            # compute the mean value and update the centroids
            centroids[i, :] = np.mean(data_in_cluster, axis=0)
    #print(clusterAssment)
    # modify the clusterAssment into the required format
    clusterResult = [[] for _ in range(k)]
    print(clusterResult)
    for i in range(num_data):
        num_cluster = int(clusterAssment[i, 0])
        #print(num_cluster, i)
        clusterResult[num_cluster].append(i)

    print(clusterResult)

    # write the clusterResult into output file
    if os.path.exists(output_file):
        os.remove(output_file)
    
    file = open(output_file, 'w')
    for i in range(k):
        file.write(str(i)+': ')
        length = len(clusterResult[i])
        # load the clusterResult line by line and write it into the file
        for j in range(length):
            file.write(str(clusterResult[i][j]))
            file.write(' ')
        file.write('\n')
    file.close()

# the main function
def main():
    genKmeans(database_file, k, max_iters, eps, output_file)
    
if __name__ == '__main__':
    main() 

