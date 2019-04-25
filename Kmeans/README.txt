python3 kmeans.py -database_file=database.txt -k=6 -max_iters=1000 -eps=0.1 -output_file=output.txt

In this programming assignment, we use two dimensional numpy array to save all the data.

In specific, centroids is a two dimensional numpy array, which saves the centroid of k clusters.

data is a numpy array directly read from databese file.

clusterAssment is a numpy array that saves the distance of each point to its cluster. It has a dimension of (500, 2), with the meaning of [cluster number, distance] in each row.

clusterResult is a list with dimension of (k, *). Each list in clusterResult represents the index of points that belongs to this cluster.