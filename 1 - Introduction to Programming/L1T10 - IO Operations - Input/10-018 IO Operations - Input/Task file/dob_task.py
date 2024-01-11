# Define the function to read data from the text file 
# Catorgorize names and birthdates with empty [] to hold the new values from our list
def read_data_from_file(file):
    names = []
    birthdates = []
# Open the text file
# Use a for loop to strip, slpit, join the data and to append what we want done with the data
    with open("DOB.txt", 'r') as file:
        for line in file:
            data = line.strip().rsplit()
            name = " ".join(data[ : 2])  
            birthdate = " ".join(data[-3: : ]) 
            names.append(name)
            birthdates.append(birthdate)

    return names, birthdates
# Now that the data is appended with a new defining function, organise the data in to the required catorgaries for printing
def print_data_in_sections(names, birthdates):
    print("Name")
    for name in names:
        print(name)

    print("\nBirthdate")
    for birthdate in birthdates:
        print(birthdate)

# with a new defining function declare that the file variable is = to the actual text file
# the names and birthdates list will be = to the actual data in the file
def main():
    file = "DOB.txt" 

    names, birthdates = read_data_from_file(file)

    # Print data in two different sections
    print_data_in_sections(names, birthdates)

if __name__ == "__main__":
    main()



