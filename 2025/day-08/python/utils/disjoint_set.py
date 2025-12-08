class DisjointSet:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        
    def union(self, x: int, y: int):
        px = self.parents[x]
        py = self.parents[y]
        
        if px != py:
            self.parents[y] = x
    
    def find(self, x: int):
        if self.parents[x] == x:
            return x
        
        return self.find(self.parents[x])
    