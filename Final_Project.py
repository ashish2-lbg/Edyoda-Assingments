import json
class Restaurent:
    def __init__(self):
        self.foods={}
        self.food_id=len(self.foods)
        self.personal_details={}
        self.personal_id=len(self.personal_details)


#***********************************************ADMIN_FUNCTIONALITY*************************************************************

    def food_items(self):
        self.name=input("Enter the name of food")
        self.quantity=int(input("Enter the quantity of food"))
        self.price=int(input("Enter the price of food : $"))
        self.discount=int(input("Enter the discount on food price: $"))
        self.stock=int(input("Enter the food stock: Kg"))
        self.item={"name":self.name,"quantity":self.quantity,"price":self.price,"discount":self.discount,"stock":self.stock}
        self.food_id=len(self.foods)+1
        self.foods[self.food_id]=self.item
        print(self.foods)
        with open("Food_items.json","w") as f:
            json.dump(self.foods,f)
        print("Food item has been added successfully")
        print("****************************************************************************************************")

    def remove_food_items(self):
        del self.foods[int(input("Enter the food id to be deleted"))]
        print("Remaining food items in list are",self.foods)

    def edit_food_items(self):
        f_id=int(input("Enter the food id which you want to be updated"))
        for i in self.foods[f_id]:
            self.foods[f_id][i]=input(f"Enter the {i} which you want to update")
            print(self.foods)
        with open("Food_items.json","w") as f:
            json.dump(self.foods,f)
        print("Food item has been updated successfully")
        print("*******************************************************************************************************")

    def view_food_items(self):
        print("The List of all food items is as follows")
        for i in self.foods:
            print("food_id:" ,i,"\n****************************")
            for j in self.foods[i]:
                    print(j,":",self.foods[i][j])
    print("*******************************************************************************************************")



        #*************************************************USER_FUNCTIONALITY***********************************************************

    def user_registration(self):
        self.full_name=input("Please enter your full name")
        self.phone_no=input("Please enter your phone number")
        import re
        Pattern = re.compile("[7-9][0-9]{9}")
        if Pattern.match(self.phone_no):
            print("Your phone no. is successfully registered")
        else:
            print("Invalid Mobile Number")
        self.email=input("Please enter your e mail address")
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'    
        if(re.search(regex,self.email)):   
            print("Your e mail address is successfully registered")   
        else:   
            print("Invalid Email")
        self.address=input("Please enter your correspondence address")
        self.password=int(input("Please enter your password"))
        self.detail={"full_name":self.full_name,"Phone no.":self.phone_no,"Email id":self.email,"Address":self.address,"Password":self.password}
        self.personal_id=len(self.personal_details)+1
        self.personal_details[self.personal_id]=self.detail
        print(self.personal_details)
        with open("personal_details.json","w") as d:
            json.dump(self.personal_details,d)
        print("Your details have been added successfully")
        print("*******************************************************************************************************")


    def login(self):
        i=0
        while i<=3:
            email=input("Please enter your email address")
            password=input("Please enter your password")
            if email==user_registration.email:
                if password==user_registration.password:
                    print("You have been successfully logged in")
                    break
                else:
                    print("Entered password is wrong , please enter correct password")
            else:
                print("This E mail address does not exists")
        print("*******************************************************************************************************")

    def place_order(self):
        order=[]
        print("Please enter 1 for Tandoori chicken(4 pieces)(INR 240)  ,   2 for Vegan burger(1 piece)(INR 320)    ,   3 for Truffle cake(500gm)(INR 900)")
        choice=int(input("Please enter your choice"))
        if choice==1:
            order.append("Tandoori chicken(4 pieces)(INR 240)")
        elif choice==2:
            order.append("Vegan burger(1 piece)(INR 320)")
        elif choice==3:
            order.append("Truffle cake(500gm)(INR 900)")
        else:
            print("Print enter the choice within currently available orders ")
        with open("Food_items.json","w") as f:
            json.dump(self.order,f)
        print("Food item has been ordered successfully")

        print("*******************************************************************************************************")

    def update_details(self):
        d_id=int(input("Enter the user id which you want to be updated"))
        for i in self.personal_details[d_id]:
            self.personal_details[d_id][i]=input(f"Enter the {i} which you want to update")
            print(self.personal_details)
        with open("personal_details.json","w") as d:
            json.dump(self.personal_details,d)
        print("Your detail has been updated successfully")
        print("*******************************************************************************************************")


        #*****************************************************LOGIN_SCREEN*************************************************************


print("Welcome to Barbeque nation")
while True:
    user_input=int(input("Please enter 1 for Admin , 2 for User"))
    if user_input==1:
        func=int(input("Please enter 1 for Adding food item ,2 for removing food items from list,3 for editing your food list 4 for viewing the list"))
        if func==1:
            x=Restaurent()
            x.food_items()
        elif func==2:
            x=Restaurent()
            x.remove_food_items()
        elif func==3:
            x=Restaurent()
            x.edit_food_items()
        elif func==4:
            x=Restaurent()
            x.view_food_items()
        else:
            print("Please enter the choice between 1 to 4 only")
    elif user_input==2:
        func=int(input("Please enter 1 for Signin ,2 for Login for already registered user,3 for placing order and 4 for updating the user details"))
        if func==1:
            x=Restaurent()
            x.user_registration()
        elif func==2:
            x=Restaurent()
            x.login()
        elif func==3:
            x=Restaurent()
            x.place_order()
        elif func==4:
            x=Restaurent()
            x.update_details()
        else:
            print("Please enter the choice between 1 to 4 only")
    else:
        print("Program Exit")
        exit()

            
    
   
                   
            
    
   
        

            
    
    
    
    
    



