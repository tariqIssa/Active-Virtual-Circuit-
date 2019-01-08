# Python program for Dijkstra's single source shortest
# path algorithm. The program is for adjacency matrix
# representation of the graph
 
from collections import defaultdict
 
#Class to represent a graph
class Graph:
 
    # A utility function to find the vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self,dist,queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1
        #from the dist array,pick one which has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
 
 
    # Function to print shortest path from source to j
    # using parent array
    def printPath(self, parent, j,path):
        if parent[j] == -1 : #Base Case : If j is source
            #print j,
            path.append(j)
            return
        self.printPath(parent , parent[j],path)
        #print j,
        path.append(j)

    '''Function that implements Dijkstra's single source shortest path
    algorithm for a graph represented using adjacency matrix
    representation'''
    def dijkstra(self, graph, src,dst,bdw):
 
        row = len(graph)
        col = len(graph[0])
 
        # The output array. dist[i] will hold the shortest distance from src to i
        # Initialize all distances as INFINITE 
        dist = [float("Inf")] * row
 
        #Parent array to store shortest path tree
        parent = [-1] * row
 
        # Distance of source vertex from itself is always 0
        dist[src] = 0
     
        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)
             
        #Find shortest path for all vertices
        while queue:
 
            # Pick the minimum dist vertex from the set of vertices
            # still in queue
            u = self.minDistance(dist,queue)  
            if u == dst:
                break   
            # remove min element 
            if u == -1 :
                print "there is no path"
                return
            queue.remove(u)
 
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is
                an edge from u to i, and total weight of path from
                src to i through u is smaller than current value of
                dist[i]'''
                if graph[u][i]<bdw and graph[u][i]!=0:
                    continue
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u  
         
 
        # print the constructed distance array
        path =[]
        self.printPath(parent,dst,path)
        return path
 

