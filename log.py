import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
logging.info("programstarted")
a=input("enter a value:")
logging.info("entered a vlaue")
b=input("Enter b value:")
logging.info("enterd b value")
logging.debug(f"a={a}, b={b}")
a=float(a)
b=float(b)
logging.info("a nd b converted successfully")
res=a/b
print("res=",res)
logging.debug("res=%s" % res)
def fun(x,y):
	print(f"x={x}, y={y}")
	res=x/y
	print("res=",res)
for i in range(-3,5):
	try:
		fun(10,i)
	except Exception as err: 
		logging.error("ERROR: %s" % err)
		print("issue: %s" % err)
logging.info("program ended")
