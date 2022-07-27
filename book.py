class Base:

    def __init__(self, add, see, update, delate):
        self.add = add
        self.see = see
        self.update = update
        self.delate = delate

    def add(file):
        print('New registration')
        file   
        ide = input('Enter id: ')
        name = input('Enter full name: ')
        number = input('Enter phone number: ')
        address = input('Enter adress: ')


        print('User added')

        file.write(f'Id: {ide}, Name: {name}, Number: {number} , Adress: {address} \n')
        file.close()

    def see():

        print('Saved records \n')
        file = open("dates.txt")
        print(file.read())
        file.close()

    def delate(ide):
        with open(r"C:\Users\57314\Documents\programacionPlatzi\Dev\proyect_DataBase\dates.txt", "r") as input:
            with open("dates.txt", "w") as output:
                for line in input:
                    if ide not in line.strip("\n"):
                        output.write(line)
      
class Run(Base):
    def __init__(self, add, see, update, delate):
        super().__init__(add, see, update, delate)
           
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
            print(Run.add(file= open("dates.txt", "a")))
        elif option == '2':
            print(Run.see())
        elif option == '3':
            print(Run.add(file= open("dates.txt", "w+")))
        elif option == '4':
            print(Run.delate(ide=input("Enter user Id to delate: ")))
        elif option == '5':
            sw = False
            print("completed program")            
    
        