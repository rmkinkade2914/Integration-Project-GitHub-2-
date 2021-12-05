# Reese Kinkade The integration project that I made is a puzzle story game that asks questions to solve the 
# puzzles/riddles. The website I used to help: 
# https://www.studytonight.com/post/the-sep-and-end-parameters-in-python-print-statement#:~:text=The%20end
# %20parameter%20The%20end%20parameter%20is%20used,specify%20the%20parameter%20end%20as%20%27%20%20%27. 
print("Welcome to my integration project!")
import sys


# The import sys makes it so that I can call upon system exit, so if the player decides not play they can leave the 
# program 
def main():
    answer0 = input("Would you like to play the hardest puzzle of your life? ")
    if answer0 == 'Yes' or 'yes':
        print("Ok lets continue")

    elif answer0 == 'No' or 'no':
        print("Ok have a great day!")
        sys.exit(0)
    else:
        main()


main()
name = input("What is your name?")
print("Hello my name is Avogadro")
print("As you probably know this is my test to determine the smartest of humans.")
print("You have a 0% chance of completing this test. This is because no one has passed my test")
start = input("Are ready for the hardest test of your life?")
# The input is the start of the test
print("Well lets get started")
print("The first step is to solve The Avogadro Puzzle")
print("Solve the first step to The Avogadro Puzzle")
print("What is the answer to 5+5?")
print(5 + 5)
print("Congratulations you have completed the first step!")
print("The second step to solve the Avogrado Puzzle is subtract 10-5, what is the solution to this equation?")
print(10 - 5)
print("Success, however it is only going to get progessively harder")
answer = input("Are you ready?:")
print("Multiply 25*25", not "12")
print(25 * 25)
print("Nice, now divide those two numbers")
print(25 / 25)
print("Next, Find the remainder of 30 divided by 7")
print(30 % 7)
print("Wow, I didn't think that you would get that one, find the exponent of 6 to the second power")
print(6 ** 2)
print("Im impressed can you find how many times 3 goes into 7 using floor division?")
print(7 // 3)
print("Now can you repeat Hello my name is Avogadro 10 times?")
print("Hello my name is Avogadro" * 10)
asnwer2 = input("Enter how many people do you think have tried and failed my test?")
print("Wrong I have had 100's in fact 152 people attempt this puzzle try and fail, not ONE has PASSED")
answer3 = input("What makes you think you are any different?")
answer4 = input("Well you will not pass anyway so lets get started again. Are you ready?")
answer5 = input("Who is the lead actor in Mission Impossible?")
answer6 = input("Who is my favorite actor in Mission Impossible?")
print("Ha you caught me my favorite actor has nothing to do with the test. I was just seeing if you would catch on")
print("Now lets continue, show me how to add two literal strings.")
a = "Hi "
b = "How are you"
# a and b make sure that you can add two strings
print(a + b)
print("Good now continue using these string literals without adding them")
print("Hi", end=' ')
print("How are you")
print("Great job now do it without adding and without end=:")
print("Hi", "How are you", sep=' ')
answer7 = input("Are you ready for the last question of the first part of the test?")
print("Great here is the question")
print("What is the answer to this equation? 10+5/5-2:")
print("9")
answer8 = input(
    "Good wow you have successfully have completed the first part of test! Only 80% of people continue to the second"
    " test"  ","  " but you will fail the next, how do you feel?")
secondPart = input("Are your ready to start the second test of the puzzle?")
# This starts the second part of the test/puzzle
print("Ok lets begin")
answer9 = input("What does i+=1 do?")
print("Correct now try that but with subtraction")
print("i-=1")
print("Very good I am suprised by how well you are doing, but you will not be so lucky")
print("Ok now find the range of positive numbers before 10")
range(10)
var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# This creates the range of the numbers before 10 
for x in range(10):
    print(x)

answer10 = input("What month is it?")
print("Ok what number month is October?")
print("10")
print("Good, now find out whether 10 is a prime or composite number using a while loop")


def inputData():
    answer11 = int(input("Enter a Number: ", 10))
    return number


# This enters a number 10 and then the program find out if it is prime
def validate_Answer11(answer11):
    n = 10
    while answer11 > n:
        if answer11 % n == 0 and n != answer11:
            print("This number is composite")
            break
        else:
            print("This number is prime")
            break
    return answer11

    inputData()
    validateAnswer11()


# This program uses the input 10 to determine if it is prime or composite, it is composite
print("Good you have found out how that 10 is a composite number")
answer12 = input("Now let's move past that, are you ready? ")
print("Good... Congratulations you have passed!")
print("Huh what do you mean?")
print("You passed the Avegadros Puzzle! It is was a game based on patience not on intelligence!")
print("The puzzle is made up to to test your patience and see if you would follow through.")
print("So congratulations!")
print("Oh ok. Was I the only one who passed?")
print("Yes, everyone else quit.")
print("You were the first to complete Avogadro's Puzzle!")
