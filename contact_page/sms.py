from twilio.rest import Client
def send_message(number , message) :
    client = Client('ACc0ec67d61822acc8c991ee9f3005e02d' , 'd9c964043b168900cd7d2f275d4c2519')
    message = client.messages.create(
        body=message,
        from_="+18305101816",
        to="+91"+number
    )
    print("Sent")