import json

class Base:

    def __init__(self, add, see_all, filter, delete):
        self.add = add
        self.see_all = see_all
        self.filter = filter
        self.delete = delete


    def add(file):
        print('New registration')
        file   
        ide = input('Enter id: ')
        name = input('Enter full name: ')
        number = input('Enter phone number: ')
        address = input('Enter adress: ')
        entry = {"Id": ide, "Name": name, "Number": number, "Address": address}

        with open('datos.json', 'r+') as file:
            data = json.load(file)
            data.append(entry)
            file.seek(0)
            json.dump(data, file)
        
        print('User added')


    def see_all():

        print('Saved records \n')
        with open('datos.json', 'r') as fp:
            data = json.load(fp)

            print(data)

    def filter():
        pass
       

    def delete(ide):
        pass

            
class Run(Base):
    def __init__(self, add, see, filter, delate):
        super().__init__(add, see, filter, delate)
           
if __name__ == '__main__':
    sw = True
    while sw:

        menu = '''What action do you wish to perform? 

            1. Add user 
            2. Show all users
            3. Update an user
            4. Remove all users
            5. Exit 

             Select an option: '''

        option = input(menu)
        if option == '1':
            print(Run.add())
        elif option == '2':
            print(Run.see_all())
        elif option == '3':
            print(Run.add(file= open("dates.txt", "w+")))
        elif option == '4':
            print(Run.filter())
        elif option == '5':
            print(Run.delete(ide=input("Enter user Id to delete: ")))
        elif option == '6':
            sw = False
            print("completed program")    
    
        
