import json

def add():
    print('New registration')

    ide = input('Enter id: ')
    name = input('Enter full name: ')
    while True:
        try:
            number = int(input('Enter phone number: '))
            break
        except:
            print("**** enter numbers only***")
    address = input('Enter adress: ')
    entry = {"Id": ide, "Name": name, "Number": number, "Address": address}
    with open('dates.json', 'r+') as file:
        data = json.load(file)
        data.append(entry)
        file.seek(0)
        json.dump(data, file)
    return('User added')



def see_all():
    print('Saved records \n')
    with open('dates.json', 'r') as fp:
        data = json.load(fp)
        aux = ""
        for row in data:
            aux = aux + str(row) + "\n"
        return aux
    

def filter(ide):
    with open("dates.json", "r+") as fp:
        input_dict = json.load(fp)
    c = list(filter(lambda x: x["Id"] == ide, input_dict))
    return(c)


def delete(ide):
    obj = json.load(open("dates.json"))
    for i in range(len(obj)):
        if obj[i]["Id"] == ide:
            obj.pop(i)
    
    open("dates.json", "w").write(json.dumps(obj))
            
    return("Deleted user")
       
if __name__ == "__main__":

    while True:

        menu = '''What action do you wish to perform? 

            1. Add user 
            2. Show all users
            3. Search users by Id
            4. Delete a user by user id
            5. Exit 

             Select an option: '''

        option = input(menu)
        if option == '1':
            print(add())

        elif option == '2':
            print(see_all())

        elif option == '3':
            print(filter(ide = input("Enter user id: ")))

        elif option == '4':
            print(delete(ide = input("Enter user id to delete it: ") ))

        elif option == '5':
            print("completed program")  
            break 
    
        
