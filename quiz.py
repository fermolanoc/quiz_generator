"""
Program to show an user different kind of topics to choose from to answer questions
User can choose a topic from a menu and a series of questions will be asked offering user
4 answer options: 3 of them will be wrong and only one will be right

Once user has chosen answer, program will check on DB if user was correct or not and assign a corresponding value (points)
Points will vary per question depending on difficulty

Once user has answered all the questions available in the chosen category, program will show results 
and save them in DB as well.

"""
from ui import *


def main():
    menu_text = """
    1. Display categories
    2. Add new category
    3. Add question to an existing category
    4. Delete category 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            categories_list = display_all_categories()

            # print(categories_list)
            for item in categories_list:
                print(item)

            topic = input("\nChoose a topic\n")
            while topic not in categories_list:
                topic = input("\nChoose a topic\n")
            questions_list = get_questions(topic)

        # elif choice == '2':
        #     add_new_category()
        # elif choice == '3':
        #     results = find_player()

        #     if results:
        #         edit_existing_record(results)
        #     else:
        #         print(f'Player is not on our records\n')
        # elif choice == '4':
        #     delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


main()
