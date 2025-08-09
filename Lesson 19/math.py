import math

print("Ceiling rounds a decimal up, like 23.56 to", math.ceil(23.56))
print("Floor rounds a decimal down, like 23.56 to", math.floor(23.56))

print("It's time to switch the signs of two numbers")
x = 10
y = -15
print("10, after switching its sign with -15, becomes", math.copysign(x, y))

print("Absolute value is always a fun time")
print("Using math.fabs, we can convert any number into its absolute value, like -36 becoming", math.fabs(-36), end=" ")
print("or 52 becoming", math.fabs(52))

print("Sometimes, we want to know the greatest common factor, like when dealing with fractions or polynomials")
print("We can use math.gcd like so:")
print("Say we have two numbers, 18 and 36. Using math.gcd, we learn that the greatest common factor is", math.gcd(18, 36))

print("When dealing with circles, we have a constant: pi. Using math.pi, we get that it is", math.pi)

print("Euler's number is also common. We can use math.e to find that it is", math.e)

print("Sometime's we'll graph a exponential function. The base for which is e, and the function we can use", end=" ")
print("is math.exp to find the equation forsuch graphs, like e to the 5th is", math.exp(5))

print("Other times, we just deal with exponents. The exponential function, math.pow, is like so: 2^8 is", math.pow(2, 8))

print("Factorials, written as n!, can be done using math.factorial. Observe: 5! is", math.factorial(5))

print("Sometimes we have to check for if something is a real number and not imaginary. math.isnan checks for that.")
x = int(input("Enter something to check: "))
print(math.isnan(x), "meaning that it is a real number")