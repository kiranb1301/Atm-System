#Create application which demonstrates the ATM Functionalities

class Atm:
    def __init__(self):
        self.pin = 0
        self.balance = 0
        self.menu()
    def menu(self):
        print("Welcome to the Virtual Atm system Made By Kiran....  How Can i Help you !!!!!!")
        while True:
            print("""---------- Main Menu -----------
            1. 1 -> Create Pin
            2. 2 -> Deposit Amount
            3. 3 -> Withdraw Amount 
            4. 4 -> Check Balance 
            5. 5 -> Exit 
                """)
            user_ip = int(input("Select your option to proceed: ")) 
            if user_ip == 1:
                self.create_pin()
            elif user_ip == 2:
                self.deposit_amount()
            elif user_ip == 3:
                self.withdraw_amount()
            elif user_ip == 4:
                self.check_balance()
            elif user_ip == 5:
                print("Thank you! Have a nice day!")
                break
            else:
                print("Invalid input. Please enter a valid option.")
    def create_pin(self):
        MAX_ATTEMPTS = 3
        attempts = 0
        while attempts < MAX_ATTEMPTS:
            self.pin = input("Enter your new PIN (4 digits): ")
            if len(self.pin) == 4:
                self.pin = int(self.pin)
                print("PIN set successfully")
                return  # Exit the loop if the PIN is set successfully
            else:
                print("Invalid format. PIN should be a 4-digit number.")
                attempts += 1
        print("Exceeded maximum attempts. Please try again later.")
   
    def deposit_amount(self):
        max_attempt = 3
        attempt = 0
        while attempt < max_attempt:
            users_pin = int(input("Enter your pin(4-digit pin): ")) 
            if users_pin == self.pin:
                amount = int(input("Enter your amount to deposit : ")) 
                self.balance += amount 
                print("Your deposit is successful")
                return
            else:      
                print("Invalid PIN!")
                print("please enter correct pin : ")    
            attempt += 1      
        print("You reached maximum range of limits") 
       
    def withdraw_amount(self):
        max_attempts = 3 
        attempts = 0 
        while attempts < max_attempts:
            temp = int(input("Enter your PIN: "))
            if temp == self.pin:
                amount = int(input("Enter the amount you want to withdraw: "))
                if amount <= self.balance:
                    self.balance -= amount
                    print("Withdrawal successful")
                    return
                else: 
                    print("Insufficient balance")
                    return 
            else: 
                print("Incorrect Pin !!!") 
                print("Please enter the valid pin") 
            attempts += 1 
        print("You reached maximum range of limits")

    def check_balance(self):
        max_attempts = 3 
        attempts = 0 
        while attempts < max_attempts:
            temp = int(input("Enter your PIN: "))
            if temp == self.pin:
                print("Your account balance is: ", self.balance)
                return
            else:
                print("Incorrect PIN")
                print("Enter a correct pin") 
            attempts +=1 
        print("You have reached maximum range of limits")
# Creating an instance of the Atm class
Obj_BOM = Atm()