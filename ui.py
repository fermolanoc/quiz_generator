from db_manager import get_topic_id, get_points, User


def get_user_info():
    user_name = input("What is your name? ")

    return User(user_name)


def create_user(name):
    user_id = User.create_user(name)

    return user_id


def show_all_categories(categories):
    print("\nLIST OF CATEGORIES\n")
    categories_list = []
    for category in categories:
        categories_list.append(category['name'])

    for topic in categories_list:
        print(topic)

    topic = choose_category(categories_list)
    return topic


def choose_category(list):
    topic = input("\nChoose a topic\n")
    while topic.capitalize() not in list:
        topic = input("\nTopic not valid, try again\n")

    return topic


def get_questions(user, topic):

    total_points_available = 0
    total_points_obtained = 0

    questions_list = get_topic_id(topic)

    print(f"\nQUESTIONS: \nOk {user} here are the questions:\n")
    for question in questions_list:
        difficulty, points_available = get_points(question['difficulty'])
        print(
            f"Difficulty: {difficulty}\tPoints available: {points_available}")
        total_points_available += points_available

        print(question['question'])
        print()
        print("Options:")
        print(
            f"1) {question['answer_1']}\t2) {question['answer_2']}\t3) {question['answer_3']}\t4) {question['answer_4']}")

        user_answer = input("\nEnter number of answer: ")
        try:
            int(user_answer)
            while int(user_answer) < 0 or int(user_answer) > 4:
                user_answer = input(
                    "\nAnswer chosen must be between 1 and 4: ")

            user_answer_value = question[f'answer_{user_answer}']
            print(user_answer_value)
            if user_answer_value == question['answer_1']:
                total_points_obtained += points_available
                print("Correct\n\n")
            else:
                print("Wrong\n\n")

        except ValueError as err:
            user_answer = input("\nAnswer chosen must be between 1 and 4: ")

    return total_points_available, total_points_obtained
