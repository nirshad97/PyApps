from fpdf import FPDF
import sqlite3
import random


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, card, seat):
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                ticket = Ticket(user=self.name, price=seat.get_price(), seat=seat)
                ticket.to_pdf()
                seat.occupy()
                return "Purchase successful"
            else:
                return "There was a problem with the card"

        else:
            return "Seat is taken"


class Seat:

    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id # This has to be an input


    def get_price(self):
        select_specific_query = """
        SELECT "price" FROM "Seat"
        WHERE "seat_id" = ?
        """

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(select_specific_query, [self.seat_id])
        result = cursor.fetchall()[0][0]
        connection.close()

        return result

    def is_free(self):
        select_specific_query = """
        SELECT "taken" FROM "Seat"
        WHERE "seat_id" = ?
        """

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(select_specific_query, [self.seat_id])
        result = cursor.fetchall()[0][0]
        connection.close()

        return not bool(result)

    def occupy(self):
        if self.is_free():
            update_query = """
            UPDATE "Seat" SET "taken"=1 WHERE "seat_id" = ?
            """
            connection = sqlite3.connect(self.database)
            connection.execute(update_query, [self.seat_id])
            connection.commit()
            connection.close()
            return "Purchase successful"
        else:
            return "Seat is not available"


class Card:

    database = "banking.db"

    def __init__(self, cardtype, number, cvc, holder):
        self.cardtype = cardtype
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        select_specific_query = """
        SELECT "balance" FROM "Card"
        """
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(select_specific_query)
        balance = cursor.fetchall()[0][0]
        connection.close()

        if balance > price:
            new_balance = balance - price
            update_query = """
            UPDATE "Card" SET "balance"=? WHERE "cvc" =? AND "number" =?
            """
            connection2 = sqlite3.connect(self.database)
            connection2.execute(update_query, [new_balance, self.cvc, self.number])
            connection2.commit()
            connection2.close()
            return True
        else:
            print("Your Balance in insufficient")
            return False


class Ticket:

    random_string = ""
    for i in range(12):
        random_string += random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"))

    def __init__(self, user, price, seat):
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self):

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Digital Ticket", border=0, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=100, h=40, txt="Name: ", border=0)
        pdf.cell(w=150, h=40, txt= self.user, border=0, ln=1)
        pdf.cell(w=100, h=40, txt="Ticket ID: ", border=0)
        pdf.cell(w=150, h=40, txt= self.random_string, border=0, ln=1)

        pdf.cell(w=100, h=40, txt="Price: ", border=0)
        pdf.cell(w=150, h=40, txt=str(self.price), border=0, ln=1)
        pdf.cell(w=100, h=40, txt="Seat Number: ", border=0)
        pdf.cell(w=150, h=40, txt=str(self.seat.seat_id), border=0, ln=1)

        pdf.output("sample.pdf")


name = input("Your full name: ")
seat_id = input("Seat number: ")
card_type = input("Your card type ")
card_number = input("You card number ")
card_cvc = input("Your cvc ")
card_holder = input('Card holder name ')

user = User(name=name)
seat = Seat(seat_id=seat_id)
card = Card(cardtype=card_type, number=card_number, cvc=card_cvc, holder=card_holder)

print(user.buy(seat=seat, card=card))
