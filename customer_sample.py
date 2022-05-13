""" import csv 
with open ("CUSTOMER_SAMPLE.CSV", 'w', newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["CUST0000010231"])
    writer.writerow(["CUST0000010235"])

 """
import csv


class Customer_sample:
    def __init__(self,customer_code):
        self.customer_code=customer_code
    def printeve(self):
        return self.customer_code

    
        
