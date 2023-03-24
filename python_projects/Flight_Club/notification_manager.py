from twilio.rest import Client
import smtplib
from data_manager import DataManager
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()



class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ.get("account_sid")
        self.auth_token = os.environ.get("auth_token")
        self.my_email = os.environ.get("my_email")
        self.my_password = os.environ.get("my_password")
        self.data_manager = DataManager()

    def send_alert(self, data, departure, return_date):
        client = Client(self.account_sid, self.auth_token)
        alert = f"Low price alert! Only ${data['price']:.2f} to fly from {data['cityFrom']}-{data['flyFrom']} to " \
                f"{data['cityTo']}-{data['flyTo']}, from {departure} to {return_date}"
        message = client.messages \
            .create(
            body=alert,
            from_=os.environ.get("twilio_num"),
            to=os.environ.get("send_to")
        )

    def send_email(self, data, departure, return_date):
        alert = f"Low price alert! Only ${data['price']:.2f} to fly from {data['cityFrom']}-{data['flyFrom']} to " \
                f"{data['cityTo']}-{data['flyTo']}, from {departure} to {return_date}"

        emails = self.data_manager.get_emails()

        buy_url = f"https://www.google.com/flights?hl=en#flt={data['flyFrom']}.{data['flyTo']}.{departure}*{data['flyTo']}.{data['flyFrom']}.{return_date}"

        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=self.my_email, password=self.my_password)
        for client_email in emails:
            connection.sendmail(to_addrs=client_email["email"], from_addr=self.my_email, msg=f"Subject: Flight Club\n\n"
                                                                                             f"{alert}\n\n{buy_url}")
        connection.close()
