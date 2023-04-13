from story_setup import main_story
from view import View

view = View()
story_running = True

view.start_game(main_story.title,main_story.start_node)

while story_running:
  
    choice = view.menu("\n[what will you do?]", main_story.get_current_options())

    main_story.advance_story(choice.id)

    view.show_current_description(main_story.current_node)

    if main_story.is_end():
        story_running = False

print('\n','-'*50)
print('END')
    

