import csv


def main(): 

    # Takes input for the location of the Zoom Chat Text File
    directory = input("Enter location of the chat text file: ")

    attendance = ''

    # Stores all the contents of the text file in a string variable
    with open(directory, "r") as students:
        attendance += students.read()

    # Converts the string to lower case
    attendance = attendance.lower()

    # Variable stores the number of absentees
    absenteeCount = 0

    # 'students.csv' refers to the csv file containing the names of all the students
    # All the names from that file are checked with names from the chat
    with open("students.csv", "r") as students:

        reader = csv.reader(students)

        # names is a list. That's why there is an array traversal loop 
        for names in reader:

            for name in names:

                # Accounts for incorrect capitalization and leading and trailing spaces 
                if name.lower().strip() not in attendance:

                    # Edge case: If middle name is not present in the Chat text
                    if countSpace(name.strip()) >= 2:
                        if removeMidName(name).lower().strip() in attendance:
                            continue 

                    # Prints the name of absentee to console
                    # Alternatively output it to a file
                    print(name)
                    absenteeCount += 1
                    
    print(absenteeCount)

# Function for counting the number of spaces in string
def countSpace(text):
    count = 0
    for char in text:
        if char == " ":
            count += 1
    return count

# Function which returns only the first and last name, removing the middle name
def removeMidName(name):
    return name[:name.index(' ')] + name[name.rindex(' '):]

main()        