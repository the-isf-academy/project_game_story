from .tree import Tree

class Story(Tree):
    def __init__(self, start_node):
        self.__init__super()
        
        self.start_node = start_node
        self.current_node = start_node
        self.num_nodes = 0