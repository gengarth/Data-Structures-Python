##Homework 3.3
##Charles Denney
##U9676-2161

def read():
    file = open("HanoiTower.txt", "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew

def hanoiTower(n,  towerA, towerB, towerC):
    if n > 0:
        hanoiTower(n - 1, towerA, towerC, towerB)
        towerC.append(towerA.pop(0))
        hanoiTower(n - 1, towerB, towerA, towerC)
    

def main():
    towerA = read()
    towerB = []
    towerC = []
    n = len(towerA)
    hanoiTower(n, towerA, towerB, towerC)
    print(towerA, towerB, towerC)

if __name__ == "__main__":
    main()