
# class bike:
#  def get(self,a,b):
#   # self.a=a
#   # self.b=b
#   print(self,a,b)
# (bike.get('gt 650',400000,'mitra dii bike'))


# class bike:
#  def __init__(self,a,b):
#   self.name=a
#   self.price=b
#   print(self.name,self.price)
# #  def get(self):
# #   self.name=input('enter bike name ')
# #   self.price=input('enter bike price ')
# b1=bike('splendor',100000)
# b2=bike('triumph 440',40000)

class bike:
 def __init__(self):
  pass
 def getval(self):
  self.name=input('enter bike name ')
  self.price=input('enter price ')
  print(self.name,self.price)
#  def get(self):
#   self.name=input('enter bike name ')
#   self.price=input('enter bike price ')
 def printv(self):
  print('this legend bike cost',self.name,'and it costs around',self.price)
b1=bike()
b2=bike()
b1.getval()
b2.getval()
b1.printv
b2.printv

 