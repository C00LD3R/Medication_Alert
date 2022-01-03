import vonage
import datetime
times = {}
for i in range(int(input("how much times you takes medecines a day : "))):
    x = input("Enter the time : ")
    times[x] = input("Enter the medication name : ")

number = input("Enter your phone number with international code: ")

number = number.replace("+", "")

for time in times.keys():
    bol = True
    while bol:
        timo = datetime.datetime.now()
        now = timo.strftime("%H:%M:%S")    
        if now in time:
            client = vonage.Client(key="Enter your key here", secret="Enter your secret code here")
            sms = vonage.Sms(client)
            responseData = sms.send_message(
                {
                    "from": "My Doctor",
                    "to": number,
                    "text": "It's time to take "+times[time],
                }
            )
            bol = False
