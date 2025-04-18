import json
import requests

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name =  last_name
        self.id = last_name[0:3]+first_name[0:3]

class Subject(Person):
    def __init__(self,first_name,last_name, sex, age, email):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.age = age
        self.email=email

    def post(self):
        person_json = json.dumps(self.__dict__)
        print("JSON: ", person_json)

        # Hier Beispiel aus post_api.py ergänzen

    def put(self):
        url="https://127.0.0.1:5000"
        data={"first_name":self.first_name}
        response = requests.post(url, json=data)
        return response.status_code
    
    def update_email(self):
        url = "http://127.0.0.1:5000...."
        data = {"email": self.email}
        response = requests.post(url, json=data)
        return response.status_code

if __name__ == "__main__":
    s1 = Subject("Simon", "Gabriel","male", "567","gs56@gmail.at")
    s1.post()