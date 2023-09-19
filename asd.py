import pytest
import requests

class TestReqres:
    def test_get1(self):
        self.response = requests.get('https://reqres.in/api/users?page=2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200


    def test_get2(self):
        self.response = requests.get('https://reqres.in/api/users/2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

    def test_get3(self):
        self.response = requests.get('https://reqres.in/api/users/23')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 404

    def test_get4(self):
        self.response = requests.get('https://reqres.in/api/unknown')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

    def test_get5(self):
        self.response = requests.get('https://reqres.in/api/unknown/2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

    def test_get6(self):
        self.response = requests.get('https://reqres.in/api/unknown/23')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 404

    @pytest.mark.parametrize("email, job",[("morpheus", "leader")])
    def test_eval1(self, email,job):
        url = 'https://reqres.in/api/users'
        json = {
            "email":email,
            "job":job
        }
        self.response = requests.post(url, json = json)
        assert self.response.status_code == 201

    @pytest.mark.parametrize("email, job",[("morpheus", "zion resident")])
    def test_eval2(self, email,job):
        url = 'https://reqres.in/api/users/2'
        json = {
            "email":email,
            "job":job
        }
        self.response = requests.put(url, json = json)
        assert self.response.status_code == 200



    @pytest.mark.parametrize("email, job",[("morpheus", "zion resident")])
    def test_eval3(self, email,job):
        url = 'https://reqres.in/api/users/2'
        json = {
            "email":email,
            "job":job
        }
        self.response = requests.patch(url, json = json)
        assert self.response.status_code == 200




    def test_delete1(self):
        self.response = requests.delete('https://reqres.in/api/users/2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 204







    @pytest.mark.parametrize("email, password",[("eve.holt@reqres.in", "pistol"),("sydney@fife","")])
    def test_eval4(self, email,password):
        url = 'https://reqres.in/api/register'
        json = {
            "email":email,
            "password":password
        }
        self.response = requests.post(url, json = json)
        assert self.response.status_code == 200

    @pytest.mark.parametrize("email, password", [("eve.holt@reqres.in", "cityslicka"), ("peter@klaven", "")])
    def test_eval5(self, email, password):
        url = 'https://reqres.in/api/login'
        json = {
            "email": email,
            "password": password
        }
        self.response = requests.post(url, json=json)
        assert self.response.status_code == 200


    def test_get7(self):
        self.response = requests.get('https://reqres.in/api/users?delay=3')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

