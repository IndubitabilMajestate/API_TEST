import requests
from warnings import filterwarnings
from FileManager import FileManager
filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Request:
    def __init__(self):
        with FileManager(".consts","r") as f:
            self.site = f.readline()
        with FileManager(".auth","r") as f:
            self.auth = {"Authorization": f"Bearer {f.readline()}"}
        self.response = None
        self.num_entries = None

    def getAPIResponse(self,api_url,query=""):
        url = f"{self.site}/{api_url}{query}"
        print("url = " + url)
        self.response = requests.get(url, headers=self.auth, verify=False)
        if self.response.status_code != 200:
            print(f"Error! ({self.response.status_code})")
        self.num_entries = self.response.json()["meta"]["pagination"]["total"]

    def postAPIResponse(self,api_url,data):
        url = f"{self.site}/{api_url}"
        print(url)
        print(data)
        self.response = requests.post(url,data=data, headers=self.auth, verify=False)
        if self.response.status_code != 201 and self.response.status_code != 200:
            print(self.response.json())
            raise ValueError(f"Error! ({self.response.status_code})")

    def validateResponse(self,api_url,prev_id):
        self.getAPIResponse(api_url)
        if self.response.json()["data"][0]["id"] == prev_id+1:
            print("Validation OK!")
        else:
            print(f"Expected {prev_id+1} but got {self.response.json()["data"][0]["id"]}")

    def returnFieldValue(self, api_url, query, field_name):
        self.getAPIResponse(api_url, query)
        if not self.response.json()["data"][0].get(field_name):
            print("Field is nonexistent!")
            return None
        else:
            return self.response.json()["data"][0].get(field_name)

    def patchResponse(self, api_url, data):
        url = f"{self.site}/{api_url}"
        self.response = requests.patch(url, data=data, headers=self.auth, verify=False)
        if self.response.status_code != 201 and self.response.status_code != 200:
            print(self.response.json())
            raise ValueError(f"Error! ({self.response.status_code})")
