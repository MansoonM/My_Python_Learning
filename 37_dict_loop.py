thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# only keys
for i in thisdict:
    print(i)

# only values
for x in thisdict:
  print(thisdict[x])

# both keys and values , "items()""
for m,n in thisdict.items():
   print(m,n)