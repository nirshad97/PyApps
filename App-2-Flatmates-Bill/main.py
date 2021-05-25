from flat import Bill, Flatmate
from reports import PdfReport

bill_amount = float(input("Hello, what is your bill amount: "))
billed_period = input("Which period this bill is for: ")
flatmate1_name = input("What is your name?: ")
flatmate1_days = int(input("How many days did you stay?: "))
flatmate2_name = input("What is the name of your roommate?: ")
flatmate2_days = int(input("How many days did your roommate stay?: "))

bill = Bill(bill_amount, billed_period)
fm1 = Flatmate(flatmate1_name, flatmate1_days)
fm2 = Flatmate(flatmate2_name, flatmate2_days)

pdf_report = PdfReport(filename=f"{bill.period}.pdf")
pdf_report.generate(flatmate1=fm1, flatmate2=fm2, bill=bill)