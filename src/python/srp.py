# we have here a function that retrieves the total invoice.
# it accesses the database to get the invoice details
# calculate the invoice details
# returns the invoice total
def get_total_invoice(invoice_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="myusername",
        password="mypassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        F"SELECT * FROM invoices_details WHERE Invoice_Id = {invoice_id}")

    invoice_details = mycursor.fetchall()

    sum = 0

    for invoice_detail in invoice_details:
        sum = sum + invoice_detail.Amount

    return sum

# Class to create db connection


class DatabaseConnection():
    def build_connection():
        return mysql.connector.connect(
            host="localhost",
            user="myusername",
            password="mypassword",
            database="mydatabase")


# Class to handle accessing the database


class InvoiceStorage():
    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_invoice_details(self, invoice_id):
        mycursor = self.db_connection.cursor()

        mycursor.execute(
            F"SELECT * FROM invoice_details WHERE Invoice_Id = {invoice_id}")

        return mycursor.fetchall()

# class to handle invoice functionalities


class Invoice:
    def __init__(self, number):
        self.number = number
        self.db = InvoiceStorage()

    def get_total_invoice(self):
        invoice_details = self.db.get_invoice_details(self.number)

        return self.total(invoice_details)

    def total(invoice_details):
        sum = 0

        for invoice_detail in invoice_details:
            sum = sum + invoice_detail.Amount

        return sum


def get_total_invoice_srp(invoice_id):
    return Invoice(invoice_id).get_total_invoice()


print(get_total_invoice(10))
print(get_total_invoice_srp(10))
