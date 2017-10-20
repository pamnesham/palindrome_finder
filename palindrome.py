#!python3

#this function reverses characters in a string
def reverse(astring):
    mirror = ""
    for i in astring:
        mirror = i + mirror
    return mirror


#this function determines if a string is a palindrome
def ispalindrome():
    flag = "y"
    while flag == "y":
        stringy = input("Enter string: ")
        for each in stringy:
            if not each.isalpha() and not each.isnumeric():
                stringy = stringy.replace(each, "")
        stringy = stringy.lower()
        rev = reverse(stringy)
        if stringy == rev:
            print(stringy + " is a palindrome.")
        else:
            print(stringy +" is not a palindrome.")
        print("Continue? (y/n): ")
        flag = input()



#call functions
def main():
    ispalindrome()


if __name__ == '__main__':
    main()
