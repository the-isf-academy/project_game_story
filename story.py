from node import Node

class Story():
    def __init__(self, title, start_id, start_option_title, start_description):
        self.title = title
        self.current_node = Node(start_id, start_option_title, start_description)
        self.first_node = self.current_node
        

    def add_new_child(self, parent_id, child_id, child_option_title, child_description):
        # finds the parent node, creates a new node
        # sets the new node as teh found parent's node

        parent_node = self.current_node.find(parent_id)

        new_child_node = Node(
            id = child_id,
            option_title = child_option_title,
            description= child_description
        )

        parent_node.add_child(new_child_node)

    def get_current_children(self):
        # returns all of the children of the current node

        return self.current_node.children

    def set_current_node(self,chosen_node):
        # sets the current node as the chosen_node

        self.current_node = chosen_node
  
    def is_finished(self):
        # returns True if there are no children of the current node
        # else, returns False

        return len(self.current_node.children) == 0
    






    




