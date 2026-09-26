password = input("Enter a password to test: ")

length_ok = len(password) >= 8

has_number = False
for letter in password:
    if letter.isdigit():
        has_number = True

has_capital = False
for letter in password:
    if letter.isupper():
        has_capital = True

symbols = "!@#$%^&*"
has_symbol = False
for letter in password:
    if letter in symbols:
        has_symbol = True

score = 0
if length_ok:
    score = score + 1
if has_number:
    score = score + 1
if has_capital:
    score = score + 1
if has_symbol:
    score = score + 1

if length_ok:
    print("Length (8+ characters): PASS")
else:
    print("Length (8+ characters): FAIL")

if has_number:
    print("Has a number: PASS")
else:
    print("Has a number: FAIL")

if has_capital:
    print("Has a capital letter: PASS")
else:
    print("Has a capital letter: FAIL")

if has_symbol:
    print("Has a symbol (!@#$%^&*): PASS")
else:
    print("Has a symbol (!@#$%^&*): FAIL")
print("Score:", score, "out of 4")

if score == 4:
    print("Result: STRONG password!")
elif score == 3:
    print("Result: MEDIUM password. Try to fix the FAIL above.")
else:
    print("Result: WEAK password. Please improve it.")
