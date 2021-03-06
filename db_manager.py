import sqlite3

db = './database/quizzes.db'  # works on my machine, fails on a PC. Always use os.path.join to join directories and files

# Connect to DB and create cursor to execute queries
with sqlite3.connect(db) as conn:
    conn.row_factory = sqlite3.Row  # Upgrade row_factory
    cursor = conn.cursor()


class User:

    def __init__(self, user_name, id=None):
        self.user_name = user_name
        self.id = id

    def find_user_by_name(user):

        find_user_by_name_sql = 'SELECT id from user where LOWER(user_name) = ?'
        user_name = user.user_name.lower()
        rows = cursor.execute(find_user_by_name_sql, (user_name,))
        user_data = rows.fetchone()

        if user_data:
            for user in user_data:
                return user
        else:
            print(
                # does this method have any control over creating an account? The error 
                # should relate to what specfically went wrong in this method
                f'User {user.user_name} not found.')
                # f'User {user.user_name} not found. We\'ll create an account for you')
            return None

    def create_user(user):
        insert_sql = 'INSERT INTO user (user_name) VALUES (?)'
        user_name = user.user_name.title()

        try:
            with sqlite3.connect(db) as conn:
                conn.row_factory = sqlite3.Row  # Upgrade row_factory
                cursor = conn.cursor()

                res = cursor.execute(
                    insert_sql, (user_name,))
                new_id = res.lastrowid  # Get the ID of the new row in the table
                user.id = new_id  # Set this book's ID  # book?
        except sqlite3.IntegrityError as e:
            # at least log or print the exception - all kinds of things
            # can go wrong in the try block and you'll have no idea what happened if 
            # all you see is "error"
            # Also be consistent with single vs double quotes - pick one and use throughout 
            print("error")
        finally:
            cursor.close()

        print(user.id, user.user_name)
        return user.id

    def user_exists(self, user):

        find_user_sql = 'SELECT * FROM user WHERE LOWER(user_name) = ?'

        res = cursor.execute(find_user_sql, (user))
        firs_user = res.fetchone()
        found = firs_user is not None

        return found


class Category:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def get_categories():
        all_categories = cursor.execute('Select name from categories')

        return all_categories

    def get_topic_id(topic):

        try:
            with sqlite3.connect(db) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()

                topic_id = cursor.execute(
                    f'Select id from categories where categories.name = \'{topic}\'')

                for row in topic_id:
                    questions_list = Question.get_questions(row['id'])
                    # print(questions_list)
                    return questions_list
        except sqlite3.IntegrityError as e:
            print("error")
        finally:
            cursor.close()


class Question:

    def __init__(self, question, correct_answer, wrong_answer_1, wrong_answer_2, wrong_answer_3, category_id, difficulty, id=None):
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_answer_1 = wrong_answer_1
        self.wrong_answer_2 = wrong_answer_2
        self.wrong_answer_3 = wrong_answer_3
        self.category_id = category_id
        self.difficulty = difficulty
        self.id = id

    def get_questions(topic_id):

        try:
            with sqlite3.connect(db) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()

                questions = cursor.execute(
                    # no format strings! use parameters! 
                    f'Select * from questions q inner join categories c on q.category_id = c.id where q.category_id = {topic_id}')

                questions_list = []
                for item in questions:

                    # why not use an instance of the Question class to store all the question data? 
                    # You've set the __init__ method up already
                    single_question = {}
                    question_id = item['id']
                    text = item['question']
                    correct_answer_1 = item['correct_answer']
                    wrong_answer_2 = item['wrong_answer_1']
                    wrong_answer_3 = item['wrong_answer_2']
                    wrong_answer_4 = item['wrong_answer_3']
                    difficulty = item['difficulty']

                    # print(text, option_1, option_2)

                    single_question['id'] = question_id
                    single_question['question'] = text
                    single_question['answer_1'] = correct_answer_1
                    single_question['answer_2'] = wrong_answer_2
                    single_question['answer_3'] = wrong_answer_3
                    single_question['answer_4'] = wrong_answer_4
                    single_question['difficulty'] = difficulty

                    # print(single_question)
                    questions_list.append(single_question)
        except sqlite3.IntegrityError as e:
            print("error")
        finally:
            cursor.close()

        # print(questions_list)
        return questions_list


class Results:

    def __init__(self, date_quiz, user_id, question_id, score):
        self.date_quiz = date_quiz
        self.user_id = user_id
        self.question_id = question_id
        self.score = score

    def save_record(timestamp, user_id, question_id, score):
        insert_sql = 'INSERT INTO results (date_quiz, user_id, question_id, score) VALUES (?, ?, ?, ?)'

        try:
            with sqlite3.connect(db) as conn:
                conn.row_factory = sqlite3.Row  # Upgrade row_factory
                cursor = conn.cursor()

                cursor.execute(
                    insert_sql, (timestamp, user_id, question_id, score))

        except sqlite3.IntegrityError as e:
            print("error")
        finally:
            cursor.close()


def get_points(difficulty):

    try:
        with sqlite3.connect(db) as conn:
            conn.row_factory = sqlite3.Row  # Upgrade row_factory
            cursor = conn.cursor()

            question_points = cursor.execute(
                f'Select * from difficulties d inner join questions q on d.id = q.difficulty where q.difficulty = {difficulty}')

            for row in question_points:
                score = row['score']
                difficulty = row['name']
                return difficulty, score
    except sqlite3.IntegrityError as e:
        print("error")
    finally:
        cursor.close()

# get_topic_id('Entertainment')
