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

    print("------------------------ Choose a topic to take a quiz ------------------------")

    topic = display_all_categories()  # get topic chosen by user
    # also query database to get number of questions available for that topic, and ask user
    # to choose the number of questions they want to answer 
    
    user_id, user_name = get_user_info()  # get user basic info

    # from the topic chosen by user, get questions available
    get_questions(user_id, user_name.user_name, topic.capitalize())


def get_user_info():
    user_name = ui.get_user_info()  # returns an User object
    # user User object to find user id
    user_id = User.find_user_by_name(user_name)

    # if user_id was not found, then user object is created on db
    if not user_id:
        user_id = User.create_user(user_name)
    else:  # if user id is found, then let user know that registration already exists
        print(f'{user_name.user_name} you are already registered!')

    return user_id, user_name


def display_all_categories():   # this displays and asks the user to choose the category - so a more specifc name is better 
    # display_categories_get_user_choice() ? 

    # receives from DB an object with all categories
    categories = Category.get_categories()

    user_choice = ui.show_all_categories(categories)  # show_all_categories also asks for the choice, so use a more specifc name here too
    return user_choice


# can you be more specific with this method name? This gets results? 
def get_questions(user_id, user_name, topic):
    # receive how many points user earned and total points available, user id, user name and the category the user played
    points_available, points_obtained = ui.get_questions(
        user_id, user_name, topic)

    # show results to user
    print(f"{user_name.title()} you obtained {points_obtained} out of {points_available}")


if __name__ == '__main__':
    main()
