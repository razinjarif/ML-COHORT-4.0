def get_nid_info():
 name = input("Enter your name: ")
 present_address = input("Enter your present address: ")
 permanent_address = input("Enter your permanent addresss: ")
 date_of_birth = input("Enter your date od birth (dd-mm-yyyy): ")
 gender = input("Enter your age: ")
 
 #Store in dictionary
 nid ={
    "name": name,
    "present address":present_address,
    "permanent address":permanent_address,
    "date of birth":date_of_birth,
    "Gender":gender,
  }
 return nid
def show_nid_info(nid):
    print("------NID INFORMATION------")

    print("Name: ", nid["Name"])
    print("Present Address: ", nid["Present Address"])
    print("Permanent Address: ", nid["Permanent Addresss"])
    print("Date of Birth: ", nid["Date of Birth"])
    print("Gender: ", nid["Gender"])
    
data=get_nid_info()
show_nid_info(data)


