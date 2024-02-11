def createTree():
    f = open("tree.txt", "r")
    tree = f.read()
    treelist = []
    for line in tree.splitlines():
        treelist.append([int(i) for i in line.split()])

    return treelist

def main():
    treelist = createTree()
    n = len(treelist)
    
    for i, line in enumerate(treelist[n-2::-1]):
        for j in range(len(line)):
            left = treelist[n-i-1][j]
            right = treelist[n-i-1][j+1]
            treelist[n-i-2][j] += max(left, right)
    
    print(treelist[0][0])
    
if __name__ == '__main__':
    main()