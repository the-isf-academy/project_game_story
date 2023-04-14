class Node():
    def __init__(self, id, title="", description=""):
        self.id = id
        self.branches = []   
        self.title=title                    # primary text?
        self.description = description      #secondary text? 

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"({str(self.id)}) {self.title}"

    def find(self, id):
        if self.id == id: 
            return self
        
        for node in self.branches:
            n = node.find(id)
            if n: return n
        return None