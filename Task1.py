from Request import Request
from Print import prettifyData

def main():
    req = Request()
    print("---------------------------Users------------------------------")

    req.getAPIResponse("users")
    prettifyData(req.response.json()["data"])

    print("---------------------------Posts------------------------------")

    req.getAPIResponse("posts")
    prettifyData(req.response.json()["data"])

    print("---------------------------Comms------------------------------")

    req.getAPIResponse("comments")
    prettifyData(req.response.json()["data"])

    print("---------------------------Todos------------------------------")

    req.getAPIResponse("todos")
    prettifyData(req.response.json()["data"])


if __name__ == "__main__":
    main()