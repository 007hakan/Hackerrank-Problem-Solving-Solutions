def timeConversion(s):
    if "12:00:00" in s:
        if "PM" in s:
            print("12:00:00")
        else:
            print("00:00:00")
    elif "PM" in s :
        a=s.split("PM")
        a=a[0].split(":")
        a.insert(0,str(int(a[0])+12))
        a.pop(1)
        x=":".join(a)
        print(x)

    elif "AM" in s:
        b=s.split("AM")
        print((b[0]))





s=input("saat giriniz:")
timeConversion(s)