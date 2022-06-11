def djkSpa(adjMat1, src):
    distance_matrix = [] #Stores the final shortest distance between nodes
    finished_nodes = [] #Stores the nodes that are traversed
    nodes = len(adjMat1)
    max_int = float("inf")
    for _ in range(nodes): #Initialize 999 as the distance between the nodes
      distance_matrix.append(max_int)
    distance_matrix[src] = 0

    for _ in range(nodes): #Initialize 0 to all nodes.
      finished_nodes.append(False)

    for x in range(nodes):
      current_node = 0
      min1 = max_int
      for n in range(nodes): #Starts with source node.
         if distance_matrix[n] < min1 and finished_nodes[n] == False:
            min1 = distance_matrix[n]
            current_node = n

      finished_nodes[current_node] = True
      for node in range(nodes): #Finds the node closest to source and updates the distance_matrix
         if adjMat1[current_node][node] > 0 and finished_nodes[node] == False and \
               distance_matrix[node] > distance_matrix[current_node] + adjMat1[current_node][node]:
            distance_matrix[node] = distance_matrix[current_node] + adjMat1[current_node][node]
    c = 0
    for x in distance_matrix: #printing the values
      print("For Vertex",c,", the minimum distance to vertex",src,"is ",x)
      c+=1

def main():
   
    file = open("adjMat.txt", "r")
    lines = file.readlines()
    adjMat=[]
    for line in lines:
        holder=[]
        for x in line.strip('\n').split(' '):
            holder.append(int(x))
        adjMat.append(holder)             

    #node = int(input("Enter node 1-10: "))
    #print("Showing the Dijskstra result for theh node" , node)
    djkSpa(adjMat, 0)

if __name__ == "__main__":
    main()