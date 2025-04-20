thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
print(x)


# get()
y = thisdict.get("model")
print(y)


# =================
# dict name car

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

# print only name of keys
x = car.keys()

print(x) #before the change

# add a new key
car["color"] = "white"
print(x) #after the change

print(car)