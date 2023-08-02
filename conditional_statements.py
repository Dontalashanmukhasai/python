spamwords = ["buy now", "subscribe this", "click this"]
email = input("enter ur mail:")
for x in spamwords:
    if x in email:
        print("the email u have got is spam")
        break
else:
    print("nothing")