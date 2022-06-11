#CODE STARTS HERE===================

def dijkstraAlgApply(src, adjMat1): #Function to calculate the shortest distance
   distance_matrix = [] #Stores the final shortest distance between nodes
   finished_nodes = [] #Stores the nodes that are traversed
   for _ in range(nodes): #Initialize 999 as the distance between the nodes
      distance_matrix.append(max_int)
   distance_matrix[src] = 0

   for _ in range(nodes): #Initialize 0 to all nodes.
      finished_nodes.append(0)

   for x in range(nodes):
      current_node = 0
      min1 = max_int
      for n in range(nodes): #Starts with source node.
         if distance_matrix[n] < min1 and finished_nodes[n] == 0:
            min1 = distance_matrix[n]
            current_node = n

      finished_nodes[current_node] = 1
      for node in range(nodes): #Finds the node closest to source and updates the distance_matrix
         if adjMat1[current_node][node] > 0 and finished_nodes[node] == 0 and \
               distance_matrix[node] > distance_matrix[current_node] + adjMat1[current_node][node]:
            distance_matrix[node] = distance_matrix[current_node] + adjMat1[current_node][node]
   c = 0
   for x in distance_matrix: #printing the values
      print("For Vertex",c,", the minimum distance to vertex",src,"is ",x)
      c+=1

if __name__ == '__main__':

   max_int = 9999 #To initialize values to infinite
   nodes = 10 #Number of nodes
   adjMat = [[0, 3, 0, 0, 0, 0, 0, 12, 0, 0], #Adjacency matrix
           [3, 0, 5, 0, 0, 0, 0, 0, 4, 0],
           [0, 5, 0, 6, 0, 0, 3, 0, 0, 0],
           [0, 0, 6, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 10, 0, 0, 0, 7],
           [0, 0, 0, 0, 10, 0, 2, 0, 0, 0],
           [0, 0, 3, 0, 0, 2, 0, 4, 0, 1],
           [12, 0, 0, 0, 0, 0, 4, 0, 0, 0],
           [0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 7, 0, 1, 0, 0, 0]]
   source = 0
   print("Showing Dijikstra result for the node", source)
   dijkstraAlgApply(source, adjMat) #main function call
#CODE ENDS HERE=====================