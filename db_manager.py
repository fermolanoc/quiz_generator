from database import cursor

data = cursor.execute("Select * from questions")
# data = cursor.execute(
#     "Select distinct(c.name) from categories c inner join questions q on c.id = q.category_id where category_id = 2")
for result in data:
    print(result)
