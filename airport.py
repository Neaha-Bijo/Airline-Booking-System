import pickle as pic
import os

def viewallrecords():
    f=open('airportticket.dat','rb')
    try:
        while True:
            rec=pic.load(f)
            print(rec)
    except:
        pass
    f.close()


def viewseat():
    f=open('airportticket.dat','rb')
    v =input('Enter seat to be viewed: ')
    v1=v.upper()
    try:
        while True:
            rec=pic.load(f)
            for i in rec:
                if rec[0]==v1:
                    ls='Seat:'+rec[0]
                    lp='Price:'+str(rec[3])
                    lc='Class:'+rec[2]
                    la='ava='+rec[4]
                    lr='ROUTE:'+rec[1]
                    print(ls)
                    print(lr)
                    print(lc)
                    print(lp)
                    print(la)
                    break
    except:
        pass
    f.close()


def addseat():
    f=open('airportticket.dat','ab')
    l=[]
    s=input(('Enter New Seat:'))
    ss=s.capitalize()
    r=input('Enter route:')
    ru=r.upper()
    p=int(input('Enter Price:'))
    c=input('Enter Class:')
    cc=c.capitalize()
    a=input('Availability(y/n):')
    l.append(ss)
    l.append(ru)
    l.append(cc)
    l.append(p)
    l.append(a)
    print(l)
    pic.dump(l,f)
    print('RECORD ADDED')
    f.close()


def updateseat():
    f=open('airportticket.dat','rb')
    ft=open('temprecord.dat','ab')
    v=input('Enter seat no.: ')
    v1=v.upper()
    print('TICKET DETAILS')
    try:
        while True:
            rec=pic.load(f)
            if rec[0]==v1:
                ls='Seat:'+rec[0]
                lp='Price:'+str(rec[3])
                lc='Class:'+rec[2]
                la='ava='+rec[4]
                lr='ROUTE:'+rec[1]
                print(ls)
                print(lr)
                print(lc)
                print(lp)
                print(la)
                pc=input('Do you want to modify price (y/n):')
                pc1=pc.upper()
                if pc1=='Y':
                    p=int(input('Enter new price: '))
                    rec[3]=p
                elif pc1=='N':
                    pass
                cc=input('Do you want to modify class (y/n):')
                cc1=cc.upper()
                if cc1=='Y':
                    c=input('Enter new class: ')
                    c2=c.capitalize()
                    rec[2]=c2
                elif cc1=='N':
                    pass
                cc3=input('Do you want to modify availability (y/n):')
                pc3=cc3.upper()
                if pc3=='Y':
                    av=input('Enter availability change:')
                    rec[4]=av
                elif pc3=='N':
                    pass
                rec=[rec[0],rec[1], rec[2],rec[3],rec[4]]
                print('Your updated record is as follows')
                print(rec)
            pic.dump(rec,ft)
        
    except:
        pass
    f.close()
    ft.close()
    os.remove('airportticket.dat')
    os.rename('temprecord.dat','airportticket.dat')
        

def deleteseat():
    f=open('airportticket.dat','rb')
    f1 = open('temprecord.dat','ab')
    v = input('Enter the seat number to be deleted: ')
    v1=v.upper()
    try:
        while True:
            rec=pic.load(f)
            if rec[0] == v1:
                print('This record is deleted')
                continue
            elif rec[0] != v1:
                pic.dump(rec,f1)
                continue
    except:
        pass
    f.close()
    f1.close()
    os.remove('airportticket.dat')
    os.rename('temprecord.dat','airportticket.dat')


def bookingseats():
    f=open('airportticket.dat','rb')
    ft=open('temprecord.dat','ab')
    cd=input('Enter seat no.: ')
    cd1=cd.upper()
    print('TICKET DETAILS')
    try:
        while True:
            rec=pic.load(f)
            if rec[0]==cd1:
                ls='Seat:'+rec[0]
                lp='Price:'+str(rec[3])
                lc='Class:'+rec[2]
                la='ava='+rec[4]
                lr='ROUTE:'+rec[1]
                print(ls)
                print(lr)
                print(lc)
                print(lp)
                print(la)
                print('Do you want to confirm your booking?')
                confirm=input('Enter yes or no:')
                confirm2= confirm.upper()
                if confirm2=='YES':
                    rec[4]='n'
                    print('Your Booking is as follows')
                    la='ava='+rec[4]
                    print(ls)
                    print(lr)
                    print(lc)
                    print(lp)
                    print(la)
                elif confirm2=='NO':
                    print('Your booking will not be saved')
            rec=[rec[0],rec[1], rec[2],rec[3],rec[4]]
            pic.dump(rec,ft)
    except:
        pass
    f.close()
    ft.close()
    os.remove('airportticket.dat')
    os.rename('temprecord.dat','airportticket.dat')


def cancellingseats():
    f=open('airportticket.dat','rb')
    ft=open('temprecord.dat','ab')
    cd=input('Enter seat no.: ')
    cd1=cd.upper()
    print('TICKET DETAILS')
    try:
        while True:
            rec=pic.load(f)
            if rec[0]==cd1:
                ls='Seat:'+rec[0]
                lp='Price:'+str(rec[3])
                lc='Class:'+rec[2]
                la='ava='+rec[4]
                lr='ROUTE:'+rec[1]
                print(ls)
                print(lr)
                print(lc)
                print(lp)
                print(la)
                print('Do you want to confirm your cancellation?')
                confirm=input('Enter yes or no:')
                confirm2= confirm.upper()
                if confirm2=='YES':
                    rec[4]='y'
                elif confirm2=='NO':
                    print('Your cancellation will not be saved')
            rec=[rec[0],rec[1], rec[2],rec[3],rec[4]]
            pic.dump(rec,ft)
    except:
        pass
    f.close()
    ft.close()
    os.remove('airportticket.dat')
    os.rename('temprecord.dat','airportticket.dat')

print('I~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~I')
print('|__________WELCOME TO THE WORLD OF TRAVELLING__________|')
print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
print('|_________________________MENU_________________________|')
print('|                                                      |')
print('|        x------------MAINTENANCE------------x         |')
print('|        x   1 -<>- View All Records         x         |')
print('|        x   2 -<>- View Prices              x         |')
print('|        x   3 -<>- Add Seats                x         |')
print('|        x   4 -<>- Modify                   x         |')
print('|        x   5 -<>- Delete                   x         |')
print('|        x-----------TRANSACTION ------------x         |')
print('|        x   6 -<>- Booking Seats            x         |')
print('|        x   7 -<>- Cancelling Seats         x         |')
print('|        x-----------------------------------x         |')
print('|        x   8 -<>- Exit                     x         |')
print('|______________________________________________________|')
print('|---------------- BY XII - A 2021-2022 ----------------|')
print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
print()
print('Please pick Option')
n = 0
while n < 8:
    n = int(input('Enter the option: '))
    if n == 1:
        viewallrecords()
    elif n == 2:
        viewseat()
    elif n == 3:
        addseat()
    elif n == 4:
        updateseat()
    elif n == 5:
        deleteseat()
    elif n == 6:
        bookingseats()
    elif n == 7:
        cancellingseats()
    else:
        print('Exit')