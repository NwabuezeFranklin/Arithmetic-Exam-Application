import random
n = 0
m = 0
affirm = ['yes', 'YES', 'y', 'Yes']
two =  "no yet"
while True:
    choice = input(f"Which level do you want? Enter a number:\
    1 - simple operations with numbers 2-9\
    2 - integral squares of 11-29")
    try:
        choice =int(choice)
        if choice == 1 or choice == 2:
            try:
                while n <= 5:
                    choice = int(choice)
                    if choice == 1 or choice == 2:
                        if choice == 1:
                            two = "simple operations with numbers 2-9"

                            num1 = random.randint(2, 9)
                            num2 = random.randint(2, 9)
                            operators = random.choice(["+", "-", "*"])
                            question = str(num1) + operators + str(num2)
                            print(question)
                            while True:
                                try:
                                    answer = int(input())
                                    if answer == eval(question):
                                        print("Right!")
                                        n += 1
                                        m += 1
                                        break
                                    else:
                                        print("Wrong!")
                                        n += 1
                                        break
                                except ValueError:
                                    print("Incorrect format.")
                                    continue

                        else:
                            two = 'integral squares of 11-29'

                            num = random.randint(11, 29)
                            operator = "*"
                            question = str(num) + operator + str(num)
                            print(num)
                            while True:
                                try:
                                    answer = int(input())
                                    if answer == eval(question):
                                        print("Right!")
                                        n += 1
                                        m += 1
                                        break
                                    else:
                                        print("Wrong!")
                                        n += 1
                                        break
                                except ValueError:
                                    print("Incorrect format.")
                                    continue

                    if n == 5:
                        print(f"Your mark is {m}/5. Would you like to save the result? Enter yes or no.")
                        save = input()
                        if save in affirm:
                            print(f"What is your name?")
                            name = input()
                            with open("results.txt",'a',encoding = 'utf-8') as f:
                                f.write(f"{name}: {m}/5 in level {choice} ({two})")
                            print("The results are saved in \"results.txt\".")
                        else:
                            break

                        break
                break
            except ValueError:
                print("Incorrect format.")

        else:
            print("Incorrect format.")
    except ValueError:
        print("Incorrect format.")
