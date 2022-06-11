"""
Charles Denney
U9676-2161
Jashen Sambon
U2010-8775
Group 15
"""

#Dijkstra's Shortest Path Algorithm
def djkSpa(adjMat, source):
    source = source - 1
    length = len(adjMat)
    distance = []
    visited = []
    
    #Initialize distance and visited lists for appropriate length
    count = 0
    while count < length:
        visited.append(False)
        count += 1
    count = 0
    while count < length:
        distance.append(float("inf"))
        count += 1  

    #Start vertex distance is 0
    distance[source] = 0

    #Main traversal loop
    for vertex in range(length):
        closest = float("inf")
        current = 0
        #Gets next vertex
        for i in range(length):
            if distance[i] < closest and not visited[i]:
                closest = distance[i]
                current = i
        visited[current] = True

        #Finds closest vertex
        for vertex in range(length):
            if adjMat[current][vertex] > 0 and not visited[vertex] and distance[vertex] > distance[current] + adjMat[current][vertex]:
                #Updates closes distance
                distance[vertex] = distance[current] + adjMat[current][vertex]

    for vertex in range(length):
        print("For Vertex", vertex + 1, "the minimum distance to vertex", source + 1, "is", distance[vertex])


def main():
    
    #Reads in file
    file = open("adjMat.txt", "r")
    lines = file.readlines()
    adjMat=[]
    for line in lines:
        holder=[]
        for x in line.strip('\n').split(' '):
            holder.append(int(x))
        adjMat.append(holder)    
    file.close()         

    #Input loop
    while True:
        while True:
            source = int(input("Enter source Vertex 1-10 or enter 0 to exit: "))
            if source >= 0 and source <= 10:
                break
            print("Incorrect number")
        if source == 0:
            break
        print("Showing the Dijskstra result for the node" , source)
        djkSpa(adjMat, source)

if __name__ == "__main__":
    main()