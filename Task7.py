from random import random
from Request import Request
from Print import prettifyData
from QueryGenerator import queryGenerator

def main():
    req = Request()
    query = queryGenerator("name","Apsara Patel")
    req.getAPIResponse("users",query)
    #prettifyData(req.response.json()["data"])
    user_id = req.response.json()["data"][0]["id"]
    user_name = req.response.json()["data"][0]["name"]
    user_email = req.response.json()["data"][0]["email"]
    print(user_id)
    print(user_name)
    print(user_email)
    post_title = f"Title {round(100 * random())}{round(100 * random())}"
    post_body = f"{post_title} and body {round(100 * random())}{round(100 * random())}"
    req.postAPIResponse(f"users/{user_id}/posts",{"title": f"{post_title}", "body": f"{post_body}"})
    req.getAPIResponse("posts")
    prettifyData(req.response.json()["data"])

    query = queryGenerator("title", "Title 857")
    req.getAPIResponse("posts",query)
    post_id = req.response.json()["data"][0]["id"]
    comm_body = f"{user_name} with {user_email} and body {round(100 * random())}{round(100 * random())}"
    req.postAPIResponse(f"posts/{post_id}/comments", {"name": f"{user_name}", "email": f"{user_email}", "body":f"{comm_body}"})
    req.getAPIResponse("comments")
    prettifyData(req.response.json()["data"])

    post_title = f"Title {round(100 * random())}{round(100 * random())}"
    todo_date = f"{round(12*random())}.{round(12*random())}.20{round(24+4*random())}"
    req.postAPIResponse(f"users/{user_id}/todos",{"title":f"{post_title}","due_on":f"{todo_date}","status":"pending"})
    req.getAPIResponse("todos")
    prettifyData(req.response.json()["data"])
if __name__ == "__main__":
    main()