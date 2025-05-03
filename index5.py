# is_done = False
#
#
# if is_done:
#     print("turn the light off")
# else:
#     print("turn the light on")
# print("If ended")


# is_rich = True
# is_kind = True
#
# if is_rich and is_kind:
#     print("You can be my tenant")
# else:
#     print("You can't be my tenant")
#
# is_kind = False
# is_rich = False
#
# if is_kind or is_rich:
#     print("You can be my tenant")
# else:
#     print("You can't be my tenant")


word = input("Enter a word(n,N,y,Y): ")

if word == "y" or word == "Y":
    print("Yes")
elif word == "n" or word == "N":
    print("No")
else:
    print("No valid key")
