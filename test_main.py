from fastapi.testclient import TestClient
from fastapi import FastAPI


def start_application():
    app = FastAPI()
    return app

client = TestClient(start_application())



def test_send_email():
    import smtplib

    FROM = "sinid.lei@gmail.com"
    TO = ["mock_email@mock.pt"]
    SUBJECT = "Alert Detected"
    TEXT = "ALERT"

    # Prepare actual message
    message = f"From: {FROM}\nTo: {TO}\nSubject: {SUBJECT}\n\n{TEXT}"

    print(message)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("sinid.lei@gmail.com", "kzwnxvsbvvrhtibm")
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
        assert True
    except:
        print('failed sent the mail')
        assert False