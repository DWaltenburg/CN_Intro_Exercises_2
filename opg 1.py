def thefunc():
    strw = input('Enter width:')
    strh = input('Enter height:')

    if strw.isnumeric() and strh.isnumeric():  # hvis begge er tal
        print("Width: " + strw + " meter(s)")
        print("Height: " + strh + " meter(s)")

    else:  # ellers bedes der om at prøve igen med tal
        print("Please use numbers!")
        thefunc()


thefunc()
