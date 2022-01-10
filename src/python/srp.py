class Invoice:
    def __init__(self, number):
        self.number = number
        self.db = InvoiceDB()

    def get_total_invoice(self):
        invoice_details = self.db.get_invoice_details(self.number)
        
        return total(invoice_details)
        
    def total(invoice_details):
        sum = 0
    
        for invoice_detail in invoice_details:
            sum = sum + invoice_detail.Amount
        
        return sum

class InvoiceDB():
    def __init__(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="myusername",
            password="mypassword",
            database="mydatabase")
    
    def get_invoice_details(self, invoice_id):
        mycursor = mydb.cursor()

        mycursor.execute(F"SELECT * FROM invoice_details WHERE Invoice_Id = {invoice_id}")

        return mycursor.fetchall()


def get_total_invoice_srp(invoice_id):
    return Invoice(invoice_id).get_total_invoice()
    
def get_total_invoice(invoice_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="myusername",
        password="mypassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute(F"SELECT * FROM invoices_details WHERE Invoice_Id = {invoice_id}")

    invoice_details = mycursor.fetchall()

    sum = 0
    
    for invoice_detail in invoice_details:
        sum = sum + invoice_detail.Amount
        
    return sum
    
print(get_total_invoice(10))
print(get_total_invoice_srp(10))