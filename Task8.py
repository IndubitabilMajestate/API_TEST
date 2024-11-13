from random import random

from Request import Request
from Print import prettifyData
from QueryGenerator import queryGenerator

def main():
    req = Request()
    user_id = "7520591"
    query = queryGenerator("id",f"{user_id}")
    req.getAPIResponse("users",query)
    prettifyData(req.response.json()["data"])
    email = f"email_random{round(10*random())}{round(10*random())}@email.com"
    req.patchResponse(f"users/{user_id}",{"email":f"{email}"})
    req.getAPIResponse("users",query)
    prettifyData(req.response.json()["data"])

if __name__ == "__main__":
    main()