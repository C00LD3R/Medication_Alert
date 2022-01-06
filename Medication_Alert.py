from twilio.rest import Client
import datetime
times = {}
for i in range(int(input("how much times you takes medecines a day : "))):
    x = input("Enter the time : ")
    times[x] = input("Enter the medication name : ")

number = input("Enter your phone number with international code: ")

for time in times.keys():
    bol = True
    while bol:
        timo = datetime.datetime.now()
        now = timo.strftime("%H:%M:%S")    
        if now in time:
            account_sid = 'Paste your account sid here' 
            auth_token = 'Paste your auth_token here' 
            client = Client(account_sid, auth_token) 
            message = client.messages.create(
                messaging_service_sid='Paste your messagin_service_sid here',
                body="It's time to take "+times[time],      
                to=number 
            )
            bol = False
