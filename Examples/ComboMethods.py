from keker import *
# In this example we will take a look at all Combo classes/methods


combo = ['tufaah@gmail.com:123ya123', 'ksi:sdf44ggg', 'tufaah:oiio'
         'dkkvk:ff4gcvx@!', 'tufaah@gmail.com:123ya123', 'waleed@gmail.com:pass552525'
         'dfgdfgd', 'yahida366@yahoo.com:3vvv@!A', 'FDFDF@gmail.com:655544']
        # Let's say that we have this combo


# > (Extract) Class Methods
# Note: it just return new list it don't edit the main combo list!

print(Combo.extract(combo).users)
print(Combo.extract(combo).emails)
print(Combo.extract(combo).passwords)
# Its simple right ? ( just extract users/emails/passwords )
# Let's move to the next class

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# > (Edit) Class Methods
# Note: it do edit/effect the main class list

print("\nNormal combo:")
print(combo)

Combo.edit(combo).swap
# Swap the combo from right to lift or vice versa
print("\nAfter swap:")
print(combo)

Combo.edit(combo).shake
# Shake the combo ( Swapping indexes )
print("\nAfter shake:")
print(combo)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# > (Remove) Class Methods
# Note: it do edit/effect the main class list

Combo.remove(combo).duplicates
# Remove duplicates from combo
print("\nAfter removing duplicates:")
print(combo)

# Now i will take a copy of the combo
# Just for better explain
copy1, copy2 = combo.copy(), combo.copy()

Combo.remove(copy1).emails
# Remove email:pass from the combo
print("\nAfter removing emails:")
print(copy1)

Combo.remove(copy2).users
# Remove user:pass from the combo
print("\nAfter removing users:")
print(copy2)
print("\n\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# > Other Methods
new_combo = []

#Combo(new_combo).from_file("combo.text")
# Get a combolist from a text file and put it on new_combo list

#Combo(new_combo).from_api("https://.....")
# Get a combolist from an API and put it on new_combo list

Combo(new_combo).from_file(Main.input.combo())
# Get a combolist from a text file and put it on new_combo list
# And get the combo path from an input ( I will explain Main class later! )

# And last method is Combo.pop
# It have been explained in (Checker.py) on line [39]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #