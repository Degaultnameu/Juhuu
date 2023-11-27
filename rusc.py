from twilio.rest import Client

account_sid = 'ACaef7fba3968fcda55ac4c87b1b228c57'
auth_token = '4d866c566ae13ea7d0391edb99dd5f5c'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+555195585947'
)

print(message.sid)
