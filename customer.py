import csv 

""" with open ("CUSTOMER.CSV", 'w', newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["CUSTOMER_CODE","FIRSTNAME","LASTNAME"])
    writer.writerow(["CUST0000010231","Maria","Alba"])
    writer.writerow(["CUST0000010235","George","Lucas"])

"""


class Customer:
    def __init__(self,customer_code,firstname,lastname):
      self.customer_code=customer_code
      self.name=firstname
      self.surname=lastname
    def getcustomercode(self):
      return self.customer_code
    
    
