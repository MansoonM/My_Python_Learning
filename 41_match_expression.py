# match expression  is a type of switch case
# ======syntax========
# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block


day = int(input("Enter a number from 1 to 7: "))
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")