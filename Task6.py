from Request import Request
from Print import prettifyData
from QueryGenerator import queryGenerator
def returnUsersWithMiddleName(req, num_entries):
    users = []
    found_users = 0
    current_page = 1
    while found_users < num_entries:
        query = queryGenerator(["page", "per_page"], [f"{current_page}", f"{num_entries}"])
        req.getAPIResponse("users", query)
        if req.response.status_code != 200:
            print(f"Error processing request!(code: {req.response.status_code}")
            break
        for user in req.response.json()["data"]:
            if len(user["name"].split()) == 3:
                users.append(user)
                found_users += 1
                if found_users == num_entries:
                    return users
        current_page +=1
    return users


def main():
    req = Request()
    users = returnUsersWithMiddleName(req,20)
    prettifyData(users)

if __name__ == "__main__":
    main()