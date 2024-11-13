from Request import Request
from Print import prettifyData
from QueryGenerator import queryGenerator
def main():
    req = Request()
    query = queryGenerator("name", "user_nou209")
    print(query)
    req.getAPIResponse("users",query)
    prettifyData(req.response.json()["data"])
    user_id = req.response.json()["data"][0]["id"]
    print(f"User_id = {user_id}")

if __name__ == "__main__":
    main()