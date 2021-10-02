from db_manager import Category, get_points, User, Results
import time


def get_user_info():
    # ask user to enter name
    user_name = input("What is your full name? ")

    # Create an instance of User object with user name
    return User(user_name)


def create_user(name):
    # user will be registered on DB and the id assigned automatically will be returned
    user_id = User.create_user(name)

    return user_id


def show_all_categories(categories):
    print("\nLIST OF CATEGORIES\n")

    categories_list = []  # empty list to store each category name

    # loop over categories object to get each category name
    for category in categories:
        # save category name into list
        categories_list.append(category['name'])

    # iterate over list to print each category name (topic)
    for topic in categories_list:
        print(topic)

    # get category chosen by user
    topic = choose_category(categories_list)
    return topic


def choose_category(list):
    # ask user category name to be chosen
    topic = input("\nChoose a topic\n")

    # if category doesn't exist, keep asking
    while topic.capitalize() not in list:
        topic = input("\nTopic not valid, try again\n")

    return topic  # return category chosen by user


def get_questions(user_id, user, topic):

    timestamp = 0  # initialize current time on 0

    # this will save total amount of points available for user depending on # of questions on chosen topic
    total_points_available = 0

    # save total amount of points earned by user depending on how many questions were answered right
    total_points_obtained = 0

    # get list of questions on chosen topic
    questions_list = Category.get_topic_id(topic)

    print(f"\nQUESTIONS: \nOk {user} here are the questions:\n")
    for question in questions_list:
        # for each question get id and current time
        question_id = question['id']
        timestamp = time.time()

        # initialize or reset # of points obtained for current question
        question_points_obtained = 0

        # get difficulty grade and how many points are available for current question
        difficulty, points_available = get_points(question['difficulty'])
        print(
            f"Difficulty: {difficulty}\tPoints available: {points_available}")

        # increase counter of total points available by summin current question's points available
        total_points_available += points_available

        # show question
        print(question['question'])
        print()

        # show possible answers
        print("Options:")
        print(
            f"1) {question['answer_1']}\t2) {question['answer_2']}\t3) {question['answer_3']}\t4) {question['answer_4']}")

        # ask user to choose an answer # based on 4 options
        user_answer = input("\nEnter number of answer: ")
        try:
            int(user_answer)
            while int(user_answer) < 0 or int(user_answer) > 4:
                user_answer = input(
                    "\nAnswer chosen must be between 1 and 4: ")

            user_answer_value = question[f'answer_{user_answer}']
            print(f'Answer chosen: {user_answer_value}')
            if user_answer_value == question['answer_1']:

                # give user all points available on this question and increase total count of points obtained so far as well
                question_points_obtained = points_available
                total_points_obtained += points_available
                print(f'That is Correct. {points_available} obtained\n\n')
            else:
                print(f"Wrong! Correct answer is {question['answer_1']}\n\n")

            # save results of current question on DB
            Results.save_record(
                timestamp, user_id, question_id, question_points_obtained)

        except ValueError as err:
            user_answer = input("\nAnswer chosen must be between 1 and 4: ")

    # return how many points were available from all questions and how many user obtained
    return total_points_available, total_points_obtained
