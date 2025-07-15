number = int(input("Enter a number: "))
numberCopy = number
numberPalindrome = 0

while numberCopy > 0:
    digit = numberCopy % 10
    numberPalindrome = (numberPalindrome * 10) + digit 
    numberCopy //= 10

if numberPalindrome == number:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome, since it is equal to {numberPalindrome} when reversed")