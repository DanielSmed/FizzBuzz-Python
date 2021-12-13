print("A little game of FizzBuzz. \n")

NumberOfTabels = int(input("Number of multiplecation tabels (int): "))
Words = []
Tabels = []


for i in range(NumberOfTabels):
    Tabels.append(int(input("Multiplecation tabel where numbers that are a multiple of (int): ")))
    Words.append(input("Word for the multiplecation tabel (string): "))
Last_number = int(input("\nRun until what number (int): "))

for i in range(1,Last_number+1):
    answer = ""
    for j in range(NumberOfTabels):
        if i % Tabels[j] == 0:
            answer += Words[j]
    if answer == "":
        answer = str(i)
    print(answer)
