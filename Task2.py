from random import random

from Request import Request
from Print import prettifyData

def main():
    req = Request()
    user_name = "user_nou" + f"{round(100 * random())}" + f"{round(100 * random())}"
    user_email = f"{user_name}@email.com"
    req.postAPIResponse("users", {"name": f"{user_name}", "email": f"{user_email}", "gender": "female", "status": "active"})
    req.getAPIResponse("users")
    prettifyData(req.response.json()["data"])

if __name__ == "__main__":
    main()