"""
1. positive values: sum(10,20): 30
2. negative values: sum(-10,9):-1
3. sum(str1,str2): str1str2
4. sum(10, str1): None
5. sum(str1, 20): None
"""
from main import sum_fun
import unittest
class TestSum(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("Log in to app")
		print("prepare intial setup")

	@classmethod
	def tearDownClass(cls):
		print("SIgnout process")
		print("clear initial setup")
	def setUp(self):
		print("to provide resources to test")
		print("insert")
	def tearDown(self):
		print("to remove resource after test")
		print("delete")

	def test_10_20(self):
		print("running test_10_20 test")
		act=sum_fun(10,20)
		exp=30
		self.assertEqual(act,exp,"test_10_20 failed")
		print("done test_10_20 test")
	def test_n10_9(self):
		print("running test_n10_9 test")
		act=sum_fun(-10,9)
		exp=-1
		self.assertEqual(act, exp, "test_n10_9 failed")
		print("done test_n10_9 test")
	def test_str1_str2(self):
		print("running test_str1_str2 test")
		act=sum_fun("str1","str2")
		exp = "str1str2"
		self.assertEqual(act, exp, "test_str1_str2 failed")
		print("done test_str1_str2 test")

	def test_10_str2(self):
		print("running test_10_str2 test")
		act=sum_fun(10, "str2")
		exp = None
		self.assertEqual(act, exp, "test_10_str2 failed")
		print("done test_10_str2 test")

	def test_str1_20(self):
		print("running test_str1_20 test")
		act=sum_fun("str1", 20)
		exp = None
		self.assertEqual(act, exp, "test_str1_20 failed")
		print("done test_str1_20 test")

if __name__ == "__main__":
	unittest.main()
