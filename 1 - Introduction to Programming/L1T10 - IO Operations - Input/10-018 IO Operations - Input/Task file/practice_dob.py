def read_data_from_file(file):
    names = []
    birthdates = []

    with open("DOB.txt", 'r') as file:
        for line in file:
            data = line.strip().rsplit()
            name = " ".join(data[ :2])  # Combine all elements except the last one to get the full name
            birthdate = " ".join(data[-3: : ])  # The last element is the birthdate
            names.append(name)
            birthdates.append(birthdate)

    return names, birthdates

def print_data_in_sections(names, birthdates):
    print("Name")
    for name in names:
        print(name)

    print("\nBirthdate")
    for birthdate in birthdates:
        print(birthdate)

def main():
    file = "DOB.txt"  # Replace with the actual path to your "DOB.txt" file

    names, birthdates = read_data_from_file(file)

    # Print data in two different sections
    print_data_in_sections(names, birthdates)

if __name__ == "__main__":
    main()



