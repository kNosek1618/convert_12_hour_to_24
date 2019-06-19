
# convert time from 12 hour to 24 hour format
def convert(str1):
    #checking if AM and 12 format
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # checking if PM and 12 format
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:

        # add 12 hours to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]

print(convert("08:05:45 PM"))