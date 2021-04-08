"""
print("this is main")
import b,a
print(a.x)
print(b.name)
print(a.add(100,200))
print(b.person())
print("main ended")
"""
"""
import a,b
print(a.x)
print(b.name)
"""
#import mod1
#from mod1 import f1 as file1
"""
from mod1 import f1, f2
f1.fun1()
f2.fun2()
"""
#import mod1
#from mod1 import f1,f2
#from purchase import supplier
import sys
#sys.path.append("C:\\Users\\Lenovo\\Desktop\\")
sys.path.insert(0,"C:\\Users\\Lenovo\\Desktop\\")
print(sys.path, type(sys.path))
from purchase import supplier
supplier.create_supplier()
