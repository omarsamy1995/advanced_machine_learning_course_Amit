# Task_1

# number_1
#_________
e_mail = "Amit_ml@gmail.edu"
# to ensure the email contains exactly one "@" symbol using (.count)
# to ensure the email contains exactly one "@" symbol using (.split('')[1])
if e_mail.count('@') == 1 and '.' in e_mail.split('@')[1]:
    print("Valid email")
else:
    print("Invalid email")
#__________________________________________________________________________________
# number_2
#_________
username = e_mail.split('@')[0]
print("Username:", username)
# __________________________________________________________________________________
# number_3
#_________
domain = e_mail.split('@')[1].split('.')[0]
print("Domain:",domain)
#__________________________________________________________________________________
# number_4
#_________
if e_mail.split('gmil')[1] == ".com":
    print("Commercial Domain")
elif e_mail.split('gmil')[1] == ".edu":
    print("Educational Domain")
else:
    print("Other Domain")