import math

gip = int(input("vvedite gipotenuzu: "))
A = int(input("vvedite samii bolwoy ugol: "))
cat1 = int(input("vvedite pervii catet: "))
B = int(input("vvedite ugol naprotiv pervogo kateta: "))
cat2 = int(input("vvedite vtoroi catet: "))
C = int(input ("vvedite ugol naprotiv vtorogo kateta: "))

print("budem iskat' plowad vpisanoi okrujnosti!")
print("ispolzuem formulu S=pi*R^2")

R = ((cat1 + cat2 - gip)/2) * math.tanh(A/2)
print("nahodim R, R=", R)

print ("podstavlyaem R v formulu i poluchaem S=", math.pi * R**2)