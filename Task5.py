from Request import Request
from Print import prettifyData
from QueryGenerator import queryGenerator
def main():
    req = Request()
    query = queryGenerator(["per_page", "status"], ["20", "active"])
    req.getAPIResponse("users",query)
    prettifyData(req.response.json()["data"])

if __name__ == "__main__":
    main()