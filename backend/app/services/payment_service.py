from datetime import datetime
import psycopg2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def payment_notification_service(data):

    data = {"user_id": ['user01', 'user02', 'user03']}

    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    sslmode = "require"
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()

    try:
        user_id = data['user_id']
        cursor.execute("SELECT users.email FROM users WHERE users.user_id = ANY(%s)", (user_id,))
        emails = cursor.fetchall()

        for email in emails:
            total_amount = 9000000
            print(f"Sending email to {email} for payment of {total_amount}")
            send_email(email, total_amount)

        cursor.close()
        conn.close()
        return ({"message": "Notification sent successfully"})
    except Exception as e:
        return ({"error": str(e)}), 500


def send_email(email, total_amount):
    smtp_server = 'smtp.gmail.com'  
    smtp_port = 587 
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_PASSWORD")

    for receiver_email in email:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = '[Notification from Meal Provider] You have a food pending payment of $' + str(total_amount)

        body = 'Hi there!\n\nThis is a reminder that you have a pending payment of $' + str(total_amount) + ' for your recent food order. Please make the payment at your earliest convenience.\n\nThank you!\n\nBest,\nMeal Provider Team'
        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()  
                smtp.login(sender_email, password) 
                text = message.as_string() 
                smtp.sendmail(sender_email, receiver_email, text)
                print(f'Email sent successfully to {receiver_email}!')
            except Exception as e:
                print(f'Failed to send email. Error: {e}')
# send_email(['boshwang.mg12@nycu.edu.tw', 'wangbosh0604@gmail.com'], 9000000)

def payment(data):
    
    order_id, customer_id, payment_method = data['order_id'], data['customer_id'], data['payment_method']
    
    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    sslmode = "require"
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()

    try:

        cursor.execute("UPDATE orders SET paid = 1, WHERE order_id = %s", (order_id,))
        result = cursor.fetchall()
        print(result)

        cursor.close()
        conn.close()
        return ({"message": "sucessfully paid via " + payment_method})
    except Exception as e:
        return ({"error": str(e)}), 500