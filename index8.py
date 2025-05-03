# counter = 0
#
# while counter < 5:
#     print("While loop")
#     counter += 1
# print("While ended")

verbs = [1 , 2]
print("What to do now")

while True:
    answer = input("What you want me to do : ").lower()

    verbs.append(answer)

    if answer == "help":
        print('''
        - just write a verb and tell me what to do
        - plz dont tell me do the same thing
        - if you want me stop write 'rest' 
        ''')
    elif answer == "rest":
        print("Fine , Bye!")
        break
    else:
        if verbs[-1] != verbs[-2]:
            print(f"Ok, im {answer}ing , now")
        else:
            print(f"im tired of {answer}ing ")