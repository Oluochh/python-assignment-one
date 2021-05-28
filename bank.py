class Bank:
    def __init__(self,id,accountType,branch):
         self.id=id
         self.accountType=accountType
         self.branch=branch
    def deposit(self):
            return f"Timothy went to {self.branch} and kept money from {self.accountType} with  id number{self.id} which was not his"
    def withdraw(self):
            return f" Billy could not recall his{self.accountType} and his {self.id} number,he went to the nearest{self.branch}"
               
