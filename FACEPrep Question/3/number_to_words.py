# this function is to convert from number to words
def convert_to_words(num):

    l = len(num) # length of number


    # it check wether given number is contain number or not
    if (l == 0):
        print("empty string")
        return

    # it check wether the given number is more than four length in size 
    if (l > 4):
        print("Length more than 4 is not supported")
        return

    # variable contain single digit number  in words
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven", "eight", "nine"]

    # The first string is not used,
    # this variable contain tenth digit in words
    two_digits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen",
                  "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    # The first two string are not used,
    # this variable contain hundredth digit in words
    tens_multiple = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty", "ninety"]

    # this variable contain thousandth number in digit
    tens_power = ["hundred", "thousand"]

    # print the number and colon then number converted in words
    # Example : 523 : five hundred twenty three
    print(num, ":", end=" ")

    # to print single digit number in words
    if (l == 1):
        # ord() provide ascii value of the given digit or character in
        print(single_digits[ord(num[0]) - 48]) # ascii value of 1 is 49  num=0
        return
    
    # to print four digit number contain thousand and hundred position '0'
    if(l==4):
        # print if first two digit is between 10 and 20
        first_two= int(num[0]+num[1])
        if (first_two>10 and first_two<20 and num[1]!='0'):
            print(two_digits[first_two-9]+" "+tens_power[0]+"\n")
            return
        
        # if first two digit greater than 19
        if (num[2] and num[3]== '0' and num[1]!='0'):
            print(tens_multiple[int(num[0])]+" "+single_digits[int(num[1])]+" "+tens_power[0]+"\n")
            return
        


    # Iterate while num is not '\0'
    x = 0
    while (x < len(num)):
        # Code path for first 2 digits
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                print(single_digits[ord(num[x]) - 48], end=" ")
                print(tens_power[l - 3], end=" ")
            
            # here len can be 3 or 4
            l -= 1

        # Code path for last 2 digits
        else:
            # Need to explicitly handle
            # 10 - 19. Sum of the two digits
            # is used as index of "two_digits"
            # array of strings
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 + ord(num[x + 1]) - 48)
                print(two_digits[sum])
                return

            # Need to explicitly handle 20
            elif (ord(num[x]) - 48 == 2 and ord(num[x + 1]) - 48 == 0):
                print("twenty")
                return

            # Rest of the two digit
            # numbers i.e., 21 to 99
            else:
                i = ord(num[x]) - 48
                if (i > 0):
                    print(tens_multiple[i], end=" ")
                else:
                    print("", end="")
                x += 1
                if (ord(num[x]) - 48 != 0):
                    print(single_digits[ord(num[x]) - 48])
        x += 1
    print()


convert_to_words("5200")
convert_to_words("6200")
convert_to_words("7200")
convert_to_words("5200")
convert_to_words("1100")
convert_to_words("1000")
convert_to_words("2000")
convert_to_words("523")
convert_to_words("89")
convert_to_words("01")
convert_to_words("0089")
convert_to_words("0")
convert_to_words("100")
convert_to_words("0100")
