import yagmail
import pandas
from news import NewsFeed

df = pandas.read_excel('people.xlsx')
df = df.dropna(how="all").drop(columns=["Unnamed: 4"]) # Removing the NA values and row


for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], language="en")
    email = yagmail.SMTP(user="your.email@gmail.com", password="your.password")
    email.send(to=row['email'],
               subject=f"Your {row['interest']}'s news for today",
               contents=f"Hi {row['name']}, Check out the news about {row['interest']}, today!\n {news_feed.get()}\nNIKO")