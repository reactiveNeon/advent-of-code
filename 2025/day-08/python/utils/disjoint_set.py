class DisjointSet:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.components = n
        
    def union(self, x: int, y: int):
        px = self.find(x)
        py = self.find(y)

        if py != px:
            self.components -= 1
            self.parents[py] = px

    def find(self, x: int):
        temp_x = x
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        
        self.parents[temp_x] = x
        return x
