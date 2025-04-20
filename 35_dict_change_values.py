# change the year
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)


# using update() change the year
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.update({"year": 2020})
print(this_dict)