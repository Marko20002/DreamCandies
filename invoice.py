import csv 

""" with open ("INVOICE.CSV", 'w', newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["CUSTOMER_CODE","INVOICE_CODE","AMOUNT","DATE"])
    writer.writerow(["CUST0000010231","IN0000001","105.50","01-Jan-2016"])
    writer.writerow(["CUST0000010235","IN0000002","186.53","01-Jan-2016"])
    writer.writerow(["CUST0000010231","IN0000003","114.14","01-Feb-2016"])
 """


class Invoice:
    def __init__(self,customer_code,invoice_code,amount,date):
        self.customer_code=customer_code
        self.invoice_code=invoice_code
        self.amount=amount
        self.date=date
    def getcustomer(self):
        return self.customer_code
    def getinvcode(self):
        return self.invoice_code