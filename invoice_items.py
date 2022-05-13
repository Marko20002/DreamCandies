import csv 

"""
with open ("INVOICE_ITEM.CSV", 'w', newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["INVOICE_CODE","ITEM_CODE","AMOUNT","QUANTITY"])
    writer.writerow(["IN0000001","MEIJI","75.60","100"])
    writer.writerow(["IN0000001","POCKY","10.40","250"])
    writer.writerow(["IN0000001","PUCCHO","19.50","40"])
    writer.writerow(["IN0000002","MEIJI","113.40","150"])
    writer.writerow(["IN0000002","PUCCHO","73.13","150"])
    writer.writerow(["IN0000003","POCKY","16.64","400"])
    writer.writerow(["IN0000003","PUCCHO","97.50","200"]) """

class Invoice_item:
    def __init__(self, invoice_code, item_code, amount,quantity):
        self.invoice_code=invoice_code
        self.item_code=item_code
        self.amount=amount
        self.quantity=quantity
    def getinvcode2(self):
        return self.invoice_code