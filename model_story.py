from model_node import Node

class Story():
    def __init__(self, title, first_id,first_option_title, first_description):
        # initializes a Story object with its attributes

        self.title = title # the title of your story
        self.first_node = Node(first_id, first_option_title, first_description) 
        self.current_node =  self.first_node  #the current Node of your story
        
    def get_current_node(self):
        # Returns the current node of the story.

        return self.current_node

    def get_current_children(self):
        # Returns the a list with the children of the current_node

        return self.current_node.children

    def set_current_node(self,chosen_node):
        # Sets the current_node to the chosen node

        self.current_node = chosen_node

    def add_new_child(self, parent_id, child_id, child_option_title, child_description):
        # Adds a new child Node to the parent_node with the given ID.

        parent_node = self.current_node.find(parent_id)

        new_child_node = Node(
            id = child_id,
            option_title = child_option_title,
            description= child_description
        )
        
        parent_node.add_child(new_child_node)
  
    def is_running(self):
        # checks if the story is still running

        return len(self.current_node.children) > 0
    