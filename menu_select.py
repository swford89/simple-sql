

def menu_select():
    """get user to choose their database task"""

    user_menu = {
        1: 'Create a table.',
        2: 'Add data to a table.',
        3: 'Read data from a table.',
        4: 'Delete data from a table.',
        6: 'Done.'
    }

    for key, value in user_menu.items():
        print(f'{key}. {value}')

    user_choice = int(input('// Database Menu\n// Enter the number of the task you would like to perform:'))
    return user_choice