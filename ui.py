from db_manager import get_categories, get_topic_id, get_points


def display_all_categories():
    categories = get_categories()

    print("\nLIST OF CATEGORIES\n")
    categories_list = []
    for category in categories:
        categories_list.append(category['name'])

    return categories_list


def get_questions(topic):
    questions_list = get_topic_id(topic)

    print("\nQUESTIONS:\n")
    for question in questions_list:
        difficulty, points_available = get_points(question['difficulty'])
        print(
            f"Difficulty: {difficulty}\tPoints available: {points_available}")
        print(question['question'])
        print()
        print("Options:")
        print(
            f"1) {question['answer_1']}\t2) {question['answer_2']}\t3) {question['answer_3']}\t4) {question['answer_4']}")
        user_answer = input("\nEnter number of option: ")
        try:
            user_answer_value = question[f'answer_{user_answer}']
            if user_answer_value == question['answer_1']:
                print("Correct\n\n")
            else:
                print("Wrong\n\n")
        except ValueError as err:
            print(err)
