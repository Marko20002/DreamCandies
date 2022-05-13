import csv
from customer import Customer
from invoice import Invoice
from invoice_items import Invoice_item
from customer_sample import Customer_sample






with open("CUSTOMER_SAMPLE.csv",'r') as f_customer_sample:
    csv_f_customer_sample=csv.reader(f_customer_sample)
    for row in csv_f_customer_sample:
        customer_sample=Customer_sample(str(row[0]))
       
       
       
        with open ("CUSTOMER.csv" , 'r') as f_customer:
            csv_f_customer=csv.reader(f_customer)
            for row2 in csv_f_customer:
                customer=Customer(row2[0],row2[1],row2[2])
                if(customer_sample.printeve()==customer.getcustomercode()):
                    with open ("NEW_CUSTOMER.CSV", 'a', newline="") as f:
                        writer=csv.writer(f)
                        writer.writerow([customer.customer_code])
                        writer.writerow([customer.name])
                        writer.writerow([customer.surname])
                    
                    
                    
                    with open ("INVOICE.csv" , 'r') as f_invoice:
                        csv_f_invoice=csv.reader(f_invoice)
                        for row3 in csv_f_invoice:
                            Inv=Invoice(row3[0],row3[1],row3[2],row3[3])
                            if(Inv.getcustomer()==customer_sample.printeve()):
                                with open ("NEW_INVOICE.CSV", 'a', newline="") as f1:
                                    writer1=csv.writer(f1)
                                    writer1.writerow([Inv.customer_code])
                                    writer1.writerow([Inv.invoice_code])
                                    writer1.writerow([Inv.amount])
                                    writer1.writerow([Inv.date])
                                
                                
                                
                                with open ("INVOICE_ITEM.csv" , 'r') as f_invoice_item:
                                    csv_f_invoice_item=csv.reader(f_invoice_item)
                                    for row4 in csv_f_invoice_item:
                                        Inv_item=Invoice_item(row4[0],row4[1],row4[2],row4[3])
                                        if(Inv.getinvcode()==Inv_item.getinvcode2()):
                                            with open ("NEW_INVOICE_ITEM.CSV", 'a', newline="") as f2:
                                                writer2=csv.writer(f2)
                                                writer2.writerow([Inv_item.invoice_code])
                                                writer2.writerow([Inv_item.item_code])
                                                writer2.writerow([Inv_item.amount])
                                                writer2.writerow([Inv_item.quantity])

