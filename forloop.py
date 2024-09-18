##for i in range(5):
##    for i in range(i):
##        print(i)

un= "Eswanth"
pw= 5673
bal = 50000
cen = "State bank of India"
print(cen.center(75))
print("Enter your card")
pin = int(input("enter your pin : "))
if pin==pw:
    print("Hi ",un)
    print("deposit 1")
    print("withdraw 2")
    c=int(input("1 or 2 : "))
    if(c==1):
      print("enter the desposit amount : ")
      d=int(input())
    if(d>5000 and d<10000):
        tb=bal+d
        print("credited successfully")
        print("balnce: ",tb)
    else:
        print("deposite limit 5000 - 10000")
    if(c==2):
        print("enter the withdraw amount : ")
        dp=int(input())
    if(dp>500 and dp<1000):
        dt=bal-dp
        print("Your amount succfully debited")
        print("Blance: ",dt)
    else:
        print("debit limit only 500-1000")
else:
    print("Invalid pin")
