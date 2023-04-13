class Node():
    def __init__(self, id, title="", description=""):
        self.id = id
        self.branches = []   
        self.title=title
        self.description = description

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

class Story():
    def __init__(self, title,start_node):
        self.title = title
        self.start_node = start_node
        self.current_node = start_node
        self.num_nodes = 0

    def add_node(self, root_id,data):
        self.num_nodes += 1
        get_node = self.start_node.find(root_id)

        newNode = Node(
            id = self.num_nodes,
            title=data['title'],
            description=data['description']
        )

        get_node.branches.append(newNode)

    def get_current_options(self):
        return self.current_node.branches

    def advance_story(self,next_id):
        self.current_node = self.current_node.find(next_id)

    def is_end(self):
        return len(self.current_node.branches) == 0
    



