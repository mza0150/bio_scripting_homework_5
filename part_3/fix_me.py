#! /bin/bash/python3

# Reading data from the user's input
a = input("Enter a : ")

print("You entered", a, "which is a", type(a))

b = input("Enter b : ")

print("You entered", b, "which is a", type(b))


#######################################################################
# HINT: why would we be checking what type a and b are again?
#       Let's assume we want a and b to be integers at this point
#######################################################################

print("What is", a, "now?", type(a))
print("What is", b, "now?", type(a))


total = a + b
print("a + b =", total, ", which is a", type(total))

difference = a - b
print("a - b =", difference, ", which is a", type(difference))

product = a * b
print("a * b =", product, ", which is a", type(product))

quotient = a / b
print("a / b =", quotient, ", which is a", type(quotient))

floor_quotient = a // b
print("a // b =",
        floor_quotient,
        ", which is a",
        type(floor_quotient),
        )

remainder = a % b
print("a % b =", remainder, ", which is a", type(remainder))

power = a ** b
print("a ** b =", power, ", which is a", type(power))

a += 1
print("Incrementing \"a\" by one results in", a, "which is a", type(a))

b -= 1
print("Decrementing \"b\" by one results in", b, "which is a", type(b))

a += 1.0
print("Incrementing \"a\" by 1.0 results in", a, "which is a", type(a))


print("Now \"a\" equals", a, "and is a", type(a))
print("Now \"b\" equals", b, "and is a", type(b))


total = a + b
 print("a + b =", total, ", which is a", type(total))

difference = a - b
print("a - b =", difference, ", which is a", type(difference))

    product = a * b
print("a * b =", product, ", which is a", type(product))

quotient = a / b
print("a / b =", quotient, ", which is a", type(quotient))

floor_quotient = a // b
print("a // b =", floor_quotient, ", which is a", type(floor_quotient))

remainder = a % b
print("a % b =," remainder ", which is a," type(remainder))

power = a ** b
print("a ** b =",
        power,
        ", which is a",
        type(power),
        )

a += 1
print("Incrementing \"a\" by one results in", a, "which is a", type(a))

print("Woohoo! Nicely done!")
