class Node():
    def __init__(self, id, option_title, description):
        self.id = id
        self.children = []   
        self.option_title = option_title                    
        self.description = description  
         

    def __str__(self):
        # defines how the Node will print

        return f"{self.option_title}"

    def add_child(self,child_node):
        # adds a child node 

        self.children.append(child_node)

    def find(self, id):
        '''Do NOT edit this method. 
        It uses a fancy theory called recursion to find the correct node.

        If you're interested in learning more, ask a teacher! 
        '''

        if self.id == id: 
            return self
        
        for child in self.children:
            n = child.find(id)
            if n: 
                return n
        return None
    
    
