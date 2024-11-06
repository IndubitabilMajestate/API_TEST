import requests


class Request:
    def __init__(self, site, auth):
        self.response = None
        self.site = site
        self.auth = auth

    def getAPIResponse(self,api_url):
        url = f"{self.site}/{api_url}"
        self.response = requests.get(url, headers=self.auth, verify=False)
        if self.response.status_code != 200:
            print(f"Error! ({self.response.status_code})")

    def prettifyResponse(self, size = 10):
        if self.response.status_code == 200:
            data = self.response.json()["data"]
            for data_index in range(size):
                print("==================================")
                for field in data[data_index]:
                    print(f"{field}:{data[data_index][field]}")
                print("==================================")


def main():
    site_url = "https://gorest.co.in/public-api"
    file = open(".auth","r")
    auth_token = file.readline()
    file.close()
    auth = {"Authorization": f"Bearer {auth_token}"}

    req = Request(site_url, auth)

    print("---------------------------Users------------------------------")

    req.getAPIResponse("/users")
    req.prettifyResponse(3)

    print("---------------------------Posts------------------------------")

    req.getAPIResponse("/posts")
    req.prettifyResponse(3)

    print("---------------------------Comms------------------------------")

    req.getAPIResponse("/comments")
    req.prettifyResponse(3)

    print("---------------------------Todos------------------------------")

    req.getAPIResponse("/todos")
    req.prettifyResponse(3)

if __name__ == "__main__":
    main()
