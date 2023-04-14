from .node import Node

class Tree():
    def __init__(self, start_node):
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

    def get_current_branches(self):
        return self.current_node.branches

    def set_current_node(self,next_id):
        self.current_node = self.current_node.find(next_id)

    def is_end(self):
        return len(self.current_node.branches) == 0

