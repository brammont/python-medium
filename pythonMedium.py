#list conhension
days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
newlist = []

for i in days:
  if "a" in i:
    newlist.append(i)

print(newlist) #["martes", "sabado"]

#List Comprehension

days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

newlist = [i for i in days if "a" in i]

print(newlist) # ["martes", "sabado"]
