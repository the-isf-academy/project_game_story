from model_story import Story

main_story = Story(
    title='My First Story',
    first_id = 'cks',
    first_option_title = "You are in CKS",
    first_description= "It's the start of the day!",
)

main_story.add_new_child(
    parent_id = 'cks', 
    child_id = 'library',
    child_option_title='You enter the library',
    child_description="A teacher tells you to be quiet and food isn't allowed here.",
)

main_story.add_new_child(
    parent_id = 'cks', 
    child_id = 'b2',
    child_option_title='You walk up the stairs to B2',
    child_description="You a few students noodling on the piano.",
)

main_story.add_new_child(
    parent_id = 'b2', 
    child_id = 'makerspace',
    child_option_title='You turn left and enter the makerspace',
    child_description="You see a sea of 3D printers making noises and making art.",
)








