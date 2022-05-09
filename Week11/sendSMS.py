import twilio
#print(twilio.__version__)

from twilio.rest import Client
#from moduleName.folder import class name

# Your Account Sid and Auth Token from twilio.com/console
account_sid = "#"
auth_token = "#"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+668#",
    body="Student name (5805001111 | Put Phapon)")

print(message.sid)