import json
import requests
url="http://127.0.0.1:5000/person" 
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
        response = requests.post(url,json=self.__dict__)
        print("JSON: ", person_json)
        print("2",response.text)
        # Hier Beispiel aus post_api.py ergänzen

    def put(self):
        url= "http://127.0.0.1:5000/person/122"
        data_json= json.dumps(self.__dict__)
        response = requests.put(url, data= data_json)
        print(self.__dict__)
        print(response.text)
        
    
    def update_email(self):
        url= "http://127.0.0.1:5000/person/"
        data_json= json.dumps(self.__dict__)
        response = requests.put(url, data= data_json)
        print(self.email)
        print(response.text)


if __name__ == "__main__":
    s1 = Subject("Simon", "Gabriel","male", "5","mci@test.at")
    s1.put()