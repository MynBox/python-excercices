name1 = input("What's your name? \n").lower()
name2 = input("What's their name? \n").lower()

t_counter = int(name1.count("t")) + int(name2.count("t"))
print(f"T occurs {t_counter} times")
r_counter = int(name1.count("r")) + int(name2.count("r"))
print(f"R occurs {r_counter} times")
u_counter = int(name1.count("u")) + int(name2.count("u"))
print(f"U occurs {u_counter} times")
e_counter = int(name1.count("e")) + int(name2.count("e"))
print(f"E occurs {e_counter} times")
total_true = e_counter + u_counter + r_counter + t_counter

print(f"Total is {total_true}")
print("\n")

l_counter = int(name1.count("l")) + int(name2.count("l"))
print(f"L occurs {l_counter} times")
o_counter = int(name1.count("o")) + int(name2.count("o"))
print(f"O occurs {o_counter} times")
v_counter = int(name1.count("v")) + int(name2.count("v"))
print(f"V occurs {v_counter} times")
e_counter = int(name1.count("e")) + int(name2.count("e"))
print(f"E occurs {e_counter} times")
total_love = l_counter + o_counter + v_counter + e_counter

print(f"Total is {total_love}")

love_score = str(total_true)+str(total_love)
print(f"\n Love score is {love_score}")

nls = int(love_score)

if nls < 10 or nls > 90: 
    print(f" Your score is {nls}, you go together like coke and mentos.")

elif   40 <= nls <= 50:
    print(f"Your score is {nls}, you are alright together.")
else:
    print (f"Your score is {nls}")


input("To exit press [Enter]")
