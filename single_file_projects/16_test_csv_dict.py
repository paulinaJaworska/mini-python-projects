import csv
import os


test_dict = {"user": "iwona", "surname": "jawoska"}
# Imports user stories data from a csv file.
# The filename comes as an argument, but by default it's
# "database/user_stories.csv".  Each new row is a new line in csv file
# The file format is plain text with comma separated values (CSV).
def import_user_stories(filename="user_stories.csv"):
    with open(filename, 'r') as f:
        read_d = csv.DictReader(f)
        result = []
        for row in read_d:
            result.append(dict(row))
        return result

print(import_user_stories())

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "database/user_stories.csv". The file format is the same plain text
# with comma separated values (CSV).
def save_user_stories(story, filename="user_stories.csv"):
    exists = os.path.isfile('user_stories.csv')
    with open(filename, "a+") as f:
        fieldnames = ["id", "user", "surname"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        if  not exists:
            writer.writeheader()
        writer.writerow(story)

save_user_stories({"id": 3, "user": "jane", "surname": "smith"})



def sort_list_of_dict(list_of_dictionaries, sort_by, order):
    '''
    Sorts list of dictionaies by given parameter in ascending or descending order.
    :param list_of_dictionaries:
    :param sort_by: key by which we want to sort by
    :param order: boolean (True or False)  True = descending
    :return: sorted list of dicts
    '''
    return sorted(list_of_dictionaries, key=lambda i: i[str(sort_by)], reverse=order)


def prepare_data_for_questions_data(question_data_from_form):
    next_id = "5"
    submission_time = "3242384223"
    view_number = "not implemented"
    vote_number = "not implemented"
    image = "no image"
    generated_automatically = {'id': next_id, "submission_time": submission_time, "view_number": view_number, "vote_number": vote_number,"image": image}
    question_data_from_form.update(generated_automatically)
    return question_data_from_form

data_dict = {"title": "asked question", "message": "My very important question"}
prepared_data = prepare_data_for_questions_data(data_dict)
print(prepared_data)


def prepare_data_for_questions_data(question_data_from_form):
    """
    Append necessary data, which is not enter by user, to data from question form filled by user.
    :param question_data_from_form: dictionary
    :return: dictionary
    """
    next_id = id_generator()
    submission_time = date_generator()
    view_number = "not implemented"
    vote_number = "not implemented"
    image = "no image"
    generated_automatically = {'id': next_id, "submission_time": submission_time, "view_number": view_number,
                               "vote_number": vote_number, "image": image}
    question_data_from_form.update(generated_automatically)
    return question_data_from_form

