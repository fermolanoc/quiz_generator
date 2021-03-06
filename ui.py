from typing import Match
from db_manager import Category, get_points, User, Results
import time
import random


def get_user_info():
    # ask user to enter name
    user_name = input("What is your full name? ")

    while user_name.isnumeric() or user_name.strip() == "":
        user_name = input("Please enter your real full name? ")
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

    # There is a lot happening in this function - it should be broken into smaller, simpler parts
    # writing meaningfum unit tests for this would be very difficult 

    timestamp = 0  # initialize current time on 0

    # this will save total amount of points available for user depending on # of questions on chosen topic
    total_points_available = 0

    # save total amount of points earned by user depending on how many questions were answered right
    total_points_obtained = 0

    # get list of questions on chosen topic
    questions_list = Category.get_topic_id(topic)

    print(f"\nQUESTIONS: \nOk {user} here are the questions:\n")
    for question in questions_list:
        # get a list with all 4 possible answers unordered
        answers_list = get_possible_answers(
            question['answer_1'], question['answer_2'], question['answer_3'], question['answer_4'])

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
            f"1) {answers_list[0]}\t2) {answers_list[1]}\t3) {answers_list[2]}\t4) {answers_list[3]}")

        # ask user to choose an answer # based on 4 options
        user_answer = input("\nEnter number of answer: ")
        try:
            int(user_answer)
            while int(user_answer) < 0 or int(user_answer) > 4:
                user_answer = input(
                    "\nAnswer chosen must be between 1 and 4: ")

            # print(answers_list[int(user_answer)-1])
            user_answer_value = answers_list[int(user_answer)-1]
            print(f'Answer chosen: {user_answer_value}')
            if user_answer_value == question['answer_1']:

                # give user all points available on this question and increase total count of points obtained so far as well
                question_points_obtained = points_available
                total_points_obtained += points_available
                print(
                    f'That is Correct. {points_available} points obtained\n\n')
            else:
                print(f"Wrong! Correct answer is {question['answer_1']}\n\n")

            # save results of current question on DB
            Results.save_record(
                timestamp, user_id, question_id, question_points_obtained)

        except ValueError as err:
            user_answer = input("\nAnswer chosen must be between 1 and 4: ")

    # return how many points were available from all questions and how many user obtained
    return total_points_available, total_points_obtained


def get_possible_answers(ans_1, ans_2, ans_3, ans_4):
    answers_list = []
    unordered_answers_list = []  

    # answers_list.append(ans_1)
    # answers_list.append(ans_2)
    # answers_list.append(ans_3)
    # answers_list.append(ans_4)

    #  or 
    answers_list = [ ans_1, ans_2, ans_3, ans_4]

    # random.shuffle can do this for you, but nice to see you working through the logic 

    # print(answers_list)
    while len(answers_list) > 0:
        # select randomly an answer from list
        random_answer = random.choice(answers_list)

        # create an unordered list with 4 possible answers
        unordered_answers_list.append(random_answer)

        # delete answer from original list
        answers_list.remove(random_answer)

    return unordered_answers_list
