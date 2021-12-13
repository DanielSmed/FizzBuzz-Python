print("A little game of FizzBuzz you are to put in 3 integers when promted and then the game will run.")

first = int(input("Fizz on numbers that are a multiple of: "))
second = int(input("Buzz on numbers that are a multiple of: "))
Last_number = int(input("Run until what number: "))

for i in range(1,Last_number+1):
    answer = ""
    if i % first == 0:
        answer += "Fizz"
    if i % second == 0:
        answer += "Buzz"
    if answer == "":
        answer = str(i)
    print(answer)
