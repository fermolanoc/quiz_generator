from db_manager import get_categories, get_topic_id


def display_all_categories():
    categories = get_categories()

    print("\nLIST OF CATEGORIES\n")
    categories_list = []
    for category in categories:
        categories_list.append(category['name'])

    return categories_list
