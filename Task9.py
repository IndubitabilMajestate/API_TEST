from Request import Request
from Print import prettifyData
from QueryGenerator import queryGenerator
from datetime import datetime

def compareDates(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%dT%H:%M:%S.%f%z')
    date2 = datetime.strptime(date_str2, '%Y-%m-%dT%H:%M:%S.%f%z')
    if date1 > date2:
        return 1
    elif date1 == date2:
        return 0
    else:
        return -1

def sortTodosAscendingByDate(data):
    for index_i in range(len(data) - 1):
        for index_j in range(index_i + 1, len(data)):
            a = data[index_i]["due_on"]
            b = data[index_j]["due_on"]
            res = compareDates(a, b)
            if res == 1:
                data[index_i], data[index_j] = data[index_j], data[index_i]
    return data


def main():
    req = Request()
    query = queryGenerator("per_page","20")
    req.getAPIResponse("todos",query)
    prettifyData(req.response.json()["data"])

    sorted_todos = sortTodosAscendingByDate(req.response.json()["data"])
    prettifyData(sorted_todos)

if __name__ == "__main__":
    main()