class DisjointSet:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.components = n
        
    def union(self, x: int, y: int):
        px = self.find_recursive(x)
        py = self.find_recursive(y)

        if py != px:
            self.components -= 1
            self.parents[py] = px

    def find_recursive(self, x: int) -> int:
        if self.parents[x] == x:
            return x
            
        self.parents[x] = self.find_recursive(self.parents[x])
        return self.parents[x]
        
    def find(self, x: int) -> int:
        og_x = x
        while self.parents[x] != x:
            x = self.parents[x]
            
        while og_x != x:
            og_parent = self.parents[og_x]
            self.parents[og_x] = x
            og_x = og_parent
            
        return x
