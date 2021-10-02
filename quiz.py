"""
Program to show an user different kind of topics to choose from to answer questions
User can choose a topic from a menu and a series of questions will be asked offering user
4 answer options: 3 of them will be wrong and only one will be right

Once user has chosen answer, program will check on DB if user was correct or not and assign a corresponding value (points)
Points will vary per question depending on difficulty

Once user has answered all the questions available in the chosen category, program will show results 
and save them in DB as well.

"""
import ui
from db_manager import User, Category


def main():

    menu_text = """
    1. Display categories
    2. Add new category
    3. Delete category 
    4. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            topic = display_all_categories()
            user_id, user_name = get_user_info()

            get_questions(user_id, user_name.user_name, topic.capitalize())

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
        elif choice == '4':
            break
        else:
            print('Not a valid selection, please try again')


def get_user_info():
    user_name = ui.get_user_info()
    user_id = User.find_user_by_name(user_name)

    if not user_id:
        user_id = User.create_user(user_name)
    else:
        print(f'{user_name.user_name} already exists')

    return user_id, user_name


def display_all_categories():
    categories = Category.get_categories()

    user_choice = ui.show_all_categories(categories)
    return user_choice


def get_questions(user_id, user_name, topic):
    points_available, points_obtained = ui.get_questions(
        user_id, user_name, topic)

    print(f"{user_name.title()} you obtained {points_obtained} out of {points_available}")


main()
