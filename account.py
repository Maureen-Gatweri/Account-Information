class Account:
    def __init__(self, number, amount,pin,is_frozen= False,transactions =[]):
        self.number= number
        self.__pin=pin
        self.balance=0
        self.set_overdraft=0
        self.is_frozen = is_frozen
        self.transactions=transactions
        self.amount=amount

    def show_balance(self,pin):
        if pin==pin:
            return self.balance
        else:
            return "wrong pin"
        
    def deposit(self,amount):
        if amount>50:
            self.balance+=amount
            return f" Deposited {amount}Ksh. Current balance is {self.balance}Ksh."
        else:
            return "Deposit amount must be greater than 50."
        
    def withdraw(self,amount):
        
        if amount>50:
            if self.balance>=amount:
                self.balance-=amount
                return f"Withdrew{amount}Ksh, your new balance is {self.balance}"
            else:
                return "Insufficient funds to withdraw"
    def view_account_details(self,pin):
        if pin==pin:
            return f"Your deposited {self.deposit} and your balance is {self.balance}"
        else:
            return "Kindly enter the correct pin number to view details"
        
    def set_overdraft(self,pin,new_limit):
        if pin==pin:
            self.set_overdraft=new_limit
            print ("Overdraft limit set successfuly.")
        else:
            print("Incorrect pin,re enter pin again")

    def calculate_interest(self,pin):
        if pin ==pin:
            interest_rate= 0.07
            interest = self.balance * interest_rate
            return interest
        else:
            return "Incorrect pin, unable to count interest"
        
    def freeze_account(self,pin):
        if pin==pin:
            self.is_frozen==True
            return "Account has been frozen"
        else:
            return "Incorrect pin. Unable to freeze the account"
        
    def add_transaction(self,transaction):
        self.transaction.append(transaction)

    def unfreeze_account(self,pin):
        if pin==pin:
            self.is_frozen=True
            return "Account has been unfrozen"
        else:
            return "Incorrect pin. Unable to unfreeze the account."

    def check_transaction(self,pin):
        if pin==pin:
            return self.transactions
        else:
            return "Incorrect password, unable to view the history"
        

    def set_minimum_balance(self,pin,min_balance):
        if pin==self.pin:
            self.min_balance=min_balance
            return f"Minimum balance set to ${self.min_balance}. "
        else:
            return "Incorrect pin. Put the corrrect pin to set the minimum balance"
        
    def transfer_funds(self,pin,receiver_account,amount):
        if pin==self.pin:
         if self.balance>=amount:
                self.balance=amount
                receiver_account.balance+=amount
                return f"${amount} transferred successfuly to the recipients account"
         

    def close_account(self,provided_pin):
        if self.pin ==provided_pin:
            print ("Successfully Closing the account")
            
        else:
            print ("Invalid pin, put the right pin for the account to be closed")
          
            


        

   
        
        



        

        



           
        
       
    
        

     