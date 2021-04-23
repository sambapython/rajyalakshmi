import requests
import unittest
url = "https://reqres.in/api/users/?page=2"
# get, post, put,delete, patch
class TestAPI(unittest.TestCase):

	def test_post(self):
		url="https://reqres.in/api/users/"
		data = {
			    "name": "jayaram",
			    "job": "software engineer"

			}
		resp = requests.post(url, data=data)
		self.assertEqual(resp.status_code, 201)
		resp_data = resp.json()
		self.assertEqual(resp_data.get("name"),"jayaram")
		self.assertEqual(resp_data.get("job"), "software engineer")
		self.assertTrue("id" in resp_data)
	def test_post_neg(self):
		url="https://reqres.in/api/users/"
		data = {   
			}
		resp = requests.post(url, data=data)
		self.assertEqual(resp.status_code, 201)
		resp_data = resp.json()
		self.assertIsNone(resp_data.get("name"))
		self.assertIsNone(resp_data.get("job"))
		self.assertTrue("id" in resp_data)

	# @classmethod
	# def setUpClass(cls):
	# 	cls.username="username"
	# 	cls.password="password"
	# 	resp = requests.get("/login", auth=(cls.username, cls.password))
	# 	cls.token = resp.json().get("token")
	# 	cls.headers = {"toekn":"Token %s" % cls.token}
	# def test_1(self):
	# 	#resp = requests.get(url, auth=(self.username, self.password))
	# 	#resp= requests.get(url, headers={"Authorization":"Token %s" % self.token})
	# 	resp = requests.get(url, headers=headers)
	# 	self.assertEqual(resp.status_code,200," API failed")

if __name__ == "__main__":
	unittest.main()