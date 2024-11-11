import requests
import warnings
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Data:
    def __init__(self, field_names, field_values):
        if isinstance(field_names, list) and isinstance(field_values, list):
            if len(field_names) != len(field_values):
                raise ValueError(f"Lists dont match in size! Field name list size: {len(field_names)}, field values list size: {len(field_values)}")
            self.data = dict(zip(field_names,field_values))
        elif isinstance(field_names, str) and not isinstance(field_values, list):
            self.data = {field_names : field_values}
        else:
            raise ValueError("Both need to be lists of same size or single element objects/types.")

class Request:
    def __init__(self, site, auth):
        self.response = None
        self.site = site
        self.auth = auth
        self.num_entries = None

    def getAPIResponse(self,api_url,params_name=None,params_value=None):
        if not params_name or not params_value:
            param_string = ""
        elif isinstance(params_name, list) and isinstance(params_value, list):
            if len(params_name) != len(params_value):
                raise ValueError("Lists do not have the same size!")
            param_string = "?"
            for param_index in range(len(params_name)):
                param_string+= params_name[param_index] + "=" + params_value[param_index] + "&"
            param_string = param_string[:-1]
        elif isinstance(params_name, str) and isinstance(params_value,(str,int)):
            param_string = f"?{params_name}={params_value}"
        else:
            raise ValueError("Types are invalid!")
        url = f"{self.site}/{api_url}{param_string}"
        self.response = requests.get(url, headers=self.auth, verify=False)
        if self.response.status_code != 200:
            print(f"Error! ({self.response.status_code})")
        self.num_entries = self.response.json()["meta"]["pagination"]["total"]

    def postAPIResponse(self,api_url,data):
        url = f"{self.site}/{api_url}"
        self.response = requests.post(url,data=data, headers=self.auth, verify=False)
        if self.response.status_code != 201 and self.response.status_code != 200:
            print(self.response.json())
            raise ValueError(f"Error! ({self.response.status_code})")

    def validateResponse(self,api_url):
        self.getAPIResponse(api_url)
        url = f"{self.site}/{api_url}"
        validate_response = requests.get(url, headers=self.auth, verify=False)
        if validate_response.json()["meta"]["pagination"]["total"] == self.num_entries+1:
            print("Validation OK!")
        else:
            print(f"Expected {self.num_entries+1} but got {validate_response.json()["meta"]["pagination"]["total"]}")
            #raise ValueError("Could not validate response! User already exists or cannot be created.")

    def returnField(self, api_url, params_name, params_value, field_name):
        self.getAPIResponse(api_url, params_name, params_value)
        if not self.response.json()["data"][0][field_name]:
            print("Field is nonexistent!")
            return None
        else:
            return self.response.json()["data"][0][field_name]

    def prettifyResponse(self, size = 100):
        if self.response.status_code == 200:
            meta = self.response.json()["meta"]
            print("pagination:")
            for field in meta["pagination"]:
                print(f"\t-{field}:{meta["pagination"][field]}")
            data = self.response.json()["data"]
            print("\n data:\n")
            for data_index in range(min(size,len(data))):
                for field in data[data_index]:
                    print(f"\t-{field}:{data[data_index][field]}")
                print('='*40)


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

    #print("-------------------------New  User----------------------------")

    #req_data = Data(["name","email","gender","status"],["John Doe Sr","John_DoeSr@test.example","male","active"])
    #req.postAPIResponse("/users",req_data.data)
    #req.validateResponse("/users")


    #req.getAPIResponse("/users", list(req_data.data.keys()), list(req_data.data.values()))
    #req.prettifyResponse()

    print("-------------------------Find User----------------------------")
    print(f"Id:{req.returnField("/users","name","John Doe Sr","id")}")

    print("-----------------------Active Users---------------------------")
    req.getAPIResponse("/users",["per_page","status"],["20","active"])
    req.prettifyResponse()
if __name__ == "__main__":
    main()
