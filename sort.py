import json


def sort_routes(grade, sort):
    with open("problems.json") as f:
        raw_data = json.load(f)

    data = raw_data["data"]
    problem_list = [i for i in data if i["grade"] == grade.upper()]
    if sort == "rating":
        problem_list = sorted(problem_list, key=lambda x: x["userRating"], reverse=True)

    elif sort == "repeats":
        problem_list = sorted(problem_list, key=lambda x: x["repeats"], reverse=True)

    return problem_list
