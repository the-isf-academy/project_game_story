from story_setup import story_setup
from view import View

view = View()
main_story = story_setup()


view.start_game(main_story)

while main_story.is_finished() == False: 
    chosen_node = view.menu("[what will you do?]", main_story.get_current_children())
    main_story.set_current_node(chosen_node)
    view.show_current_description(chosen_node)

view.end_game()




