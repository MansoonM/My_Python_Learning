import datetime

x = datetime.datetime.now()
# for exact time date everything
print(x)

# for name of month
print(x.strftime("%B"))

# for short Week name
print(x.strftime("%a"))

# for full Week name
print(x.strftime("%A"))
