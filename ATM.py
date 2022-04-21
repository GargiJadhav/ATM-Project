class ATM :
    def __init__(self , name , ) :

        self.userName = name
        
        

    def greetings(self):
       
        print("Hello " , self.userName ,",", "Welcome to Gargi's Bank 👋")

    def getPinNo(self):
        PinNo = int(input("Enter your ATM Pin Number : "))
        if PinNo!=0:
            print("Great , Hold on till we generate the data")
        else :
            print("Please Enter the Pin Number")

    def userData(self):
         
         userInput=int(input("If you want to withdraw your money then enter 1 or If you want to deposit your money then enter 2 : "))
         if userInput==1:
             atm.withdrawMoney()
         elif userInput==2:
             atm.depositMoney()
         else :
              print("Invalid Option , Please Choose Again")
    def withdrawMoney(self):
        amount = int(50000)
        print("Your account balance is " , amount , "Rs" )
        inputUser = int(input("Enter the amount to be withdraw : "))
        LeftMoney = amount-inputUser
        print("You have withdraw money , The total money left is  , " , LeftMoney)
    
    def depositMoney(self):
        amount = int(50000)
        print("Your account balance is " , amount , "Rs" )
        inputUser = int(input("Enter the amount to be deposit : "))
        TotalMoney = amount+inputUser
        print("You have deposited money , The total money  is  , " , TotalMoney)

    
    



             


        

atm = ATM("Gargi")  
atm.greetings()
atm.getPinNo()  
atm.userData()
    
        