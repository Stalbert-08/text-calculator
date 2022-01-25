#Text based calculator

#Input for selecting method
method = input("Enter / (division), + (addition), - (subtraction) or * (multiplication).\n")

#+ Method
if method == "+":
  num1 = input("First number:\n")
  num2 = input("Second number:\n")
  int1 = int(num1)
  int2 = int(num2)
  answer = int1 + int2
  str_answer = str(answer)
  print("The answer is: " + str_answer)

#* Method
else:
  if method == "*":
    num1 = input("First number:\n")
    num2 = input("Second number:\n")
    int1 = int(num1)
    int2 = int(num2)
    answer = int1 * int2
    str_answer = str(answer)
    print("The answer is: " + str_answer)

  #/ Method
  else:
    if method == "/":
      num1 = input("First number:\n")
      num2 = input("Second number:\n")
      int1 = int(num1)
      int2 = int(num2)
      answer = int1 / int2
      str_answer = str(answer)
      print("The answer is: " + str_answer)
    
    #- Method
    else:
      if method == "-":
        num1 = input("First number:\n")
      num2 = input("Second number:\n")
      int1 = int(num1)
      int2 = int(num2)
      answer = int1 - int2
      str_answer = str(answer)
      print("The answer is: " + str_answer)
