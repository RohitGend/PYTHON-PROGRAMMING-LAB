# Telephone Directory
def find_num():
    key=input("Enter the name whose number you want to find: ")
    print("Number of ",key,"is",d[key])
def replace_val():
    k=input("Enter the name whose number is to be updated")
    v=int(input("Enter the new number: "))
    d[k]=v
def save():
    k=input("Enter the name: ")
    v=int(input("Enter the number: "))
    d[k]=v
def delete():
    k=input("Enter the name whose number you want to delete: ")
    try:
        d.pop(k)
    except:
        print("Entered key doesn't exist")
def help():
    print('''Choose the function you want to perform
                1. Find number
                2. Update a number
                3. Save a new number
                4. Delete existing number
                5. Display directory\n
                Enter any other key for this help
                Enter x to exit''')
def display():
    print(d)
d={"ROHIT":9503939238,
   "SAURABH":8485081891,
   "PRATHAMESH":9665130307,
   "ASHWIN":9080320394,
   "OM":9763240904,
   "PRAJWAL":9284064551,}
if __name__=='__main__':
    help()
    while(True):
        key=str(input("Enter your choice: "))
        if key=='1':
            find_num()
        elif key=='2':
            replace_val()
        elif key=='3':
            save()
        elif key=='4':
            delete()
        elif key=='5':
            display()
        elif key in "xX":
            print("Thank-you")
            break
        else:
            help()
