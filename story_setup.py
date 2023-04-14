from helpers.tree import Tree
from helpers.node import Node

main_story = Tree(
    title='Main Horror Story',
    start_node=Node(0,"You see two paths."))

main_story.add_node(
    root_id = 0,
    data = {
        'title':'go left',
        'description':'You enter a dark dark dark room.'
    })

main_story.add_node(
    root_id = 0,
    data = {
        'title':'go right',
        'description':'You enter a room and it fills you with light.'
    })

main_story.add_node(
    root_id = 0,
    data = {
        'title':'stay put',
        'description':"You don't move and dance."
    })

main_story.add_node(
    root_id = 1,
    data = {
        'title':'Slowly punch the air for precaution.',
        'description':'As you wind up your arm, bats swarm you and drink your blood.'
    })

