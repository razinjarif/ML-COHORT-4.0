""" Question: NID Information Program
Write a Python program that takes a user's name, present address, permanent address, date of birth,
and gender as input, stores them in a dictionary, and then prints all the stored information clearly. """

def get_nid_info():
    name = input("Enter your name: ")
    present_address = input("Enter your present address: ")
    permanent_address = input("Enter your permanent addresss: ")
    date_of_birth = input("Enter your date od birth (dd-mm-yyyy): ")
    gender = input("Enter your age: ")
 
#store in dictionary
    nid ={
    "Name":name,
    "Present Address":present_address,
    "Permanent Address":permanent_address,
    "Date of Birth":date_of_birth,
    "Gender":gender
 }
    return nid

def show_nid_info(nid):
    print("------NID INFORMATION------")

    print("Name: ", nid["Name"])
    print("Present Address: ", nid["Present Address"])
    print("Permanent Address: ", nid["Permanent Address"])
    print("Date of Birth: ", nid["Date of Birth"])
    print("Gender: ", nid["Gender"])
    
data=get_nid_info()
show_nid_info(data)


