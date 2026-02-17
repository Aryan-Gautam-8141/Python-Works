list = ["Make a lot of money", "buy now", "subscribe this", "click this", "limited time offer"]

message=input("Enter your message: ")

if (message in list):
    print("This is spam message")
else:
    print("This is not spam message")