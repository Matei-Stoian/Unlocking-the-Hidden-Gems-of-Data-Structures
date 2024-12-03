class DisjointSet:
    def __init__(self,n:int):
        """
        Initialize a disjoint set with 'n' elements. Each element is initially its own parent.

        Parameters:
            n (int): The number of elements in the set disjoined set.
        """
        
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self,x:int) -> int:
        """
        Find the root of the set containing the element 'x', with path compression.

        Parameters:
            x (int): The element whoes set representative is to be found.
        
        Return:
            int: The root of the set containing 'x'.
        """

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x:int,y:int):
        """
        Merge two sets containing elements 'x' and 'y'

        Parameters:
            x (int): First element.
            y (int): Second element.
        """        
        
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


if __name__ == '__main__':
    ds = DisjointSet(5)
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)
    print(ds.find(0))  # Output: 0 (or the root of the set containing 0)
    print(ds.find(1))  # Output: 0
    print(ds.find(2))  # Output: 0
    print(ds.find(3))  # Output: 3 (or the root of the set containing 3)
    print(ds.find(4))  # Output: 3