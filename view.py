from InquirerPy import inquirer, get_style          # different menu package for windows compatibility


class View:

    def menu(self,prompt, options):
        '''This function creates an interactive Terminal menu.'''

        choice = inquirer.select(
            message= prompt,
            choices= options,
            qmark="",
            amark="",
            style= get_style({ 
                "answer": "#438fa8",
                "pointer": "#438fa8",
                "questionmark": "hidden"},

                ),
            ).execute()

        return choice
    

    def start_game(self, story_title,start_node):
        print(f"Title: {story_title}")
        print(f"\n{start_node.title}")
        print(f"{start_node.description}")


    def show_current_description(self,node):
        print(f"{node.description}")

