from database import cursor


def get_categories():
    all_categories = cursor.execute("Select name from categories")

    # print(all_categories)
    return all_categories


def get_questions(topic_id):
    questions = cursor.execute(
        f'Select * from questions q inner join categories c on q.category_id = c.id where q.category_id = {topic_id}')

    questions_list = []
    for item in questions:
        single_question = {}
        text = item['question']
        correct_answer_1 = item['correct_answer']
        wrong_answer_2 = item['wrong_answer_1']
        wrong_answer_3 = item['wrong_answer_2']
        wrong_answer_4 = item['wrong_answer_3']

        # print(text, option_1, option_2)

        single_question['question'] = text,
        single_question['answer_1'] = correct_answer_1
        single_question['answer_2'] = wrong_answer_2
        single_question['answer_3'] = wrong_answer_3
        single_question['answer_4'] = wrong_answer_4

        # print(single_question)
        questions_list.append(single_question)
    # print(questions_list)
    return questions_list


def get_topic_id(topic):
    topic_id = cursor.execute(
        f'Select id from categories where categories.name = \'{topic}\'')

    for row in topic_id:
        questions_list = get_questions(row['id'])
        # print(questions_list)
        return questions_list


get_topic_id('Entertainment')
