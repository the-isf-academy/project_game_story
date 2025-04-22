from story_setup import main_story # stores the Story object in main_story
from view import View

view = View() # creates a View object
         
# show the start message
view.start_game(main_story)

# loops while game is running
while main_story.is_running() == True:    
    chosen_node = view.menu("[what will you do?]", main_story.get_current_children())
    main_story.set_current_node(chosen_node)
    view.show_node_description(chosen_node)

# show the end message
view.end_game()




