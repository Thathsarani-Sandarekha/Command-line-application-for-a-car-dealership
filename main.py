import csv

# lists
make = ['Honda','Toyota']
model = ['Civic','CH-R']
year = ['2019','2020']
mileage = [58000,25000]
oldowner = ['Chamika','dilip']
askprice = [15000,20000]
sellprice = [20000,22500]
available = ['On Sale','On Sale']
buyername = [0]
buyername1 = ['']
buyertele = [0]
buyertele1 = ['']
telecopy = ['']
buyeraddress = ['']
buyertest = [0]
buyermaintain = ['' for x in range(1, 1000)]
buyermaintain1 = ['No Report Yet' for x in range(1, 1000)]
maintaincost = [0 for x in range(1, 1000)]
count = [0]
appointment = ['Pending' for x in range(1, 1000)]
carid = ['']
profit = [[0], [], [], [], [], [], [], [], [], [], [], [], []]
profit1 = [[0], [], [], [], [], [], [], [], [], [], [], [], []]


def prof(t):
    total = 0
    for k in t:
        if type(k) == list:  # checking i is list
            total = total + prof(k)
        else:
            total += k
    return total


while True:
    # MAIN MENU
    print('1 - i\'m from admin')
    print('2 - i\'m a customer')
    print('3 - i\'m from technical division')
    print('4 - i\'m a owner')
    User_Choice = input(
        '------------------------------------------------------\nPlease Enter your Choice from one of '
        'the above options|- ')
    if User_Choice == "1":
        # ADMIN MENU
        print('Choice 1: Add Vehicle to Inventory')
        print('Choice 2: Remove Vehicle from Inventory')
        print('Choice 3: View Current Inventory')
        print('Choice 4: Edit Vehicle Inventory')
        print('Choice 5: Export Current Car Inventory')
        print('Choice 6: Export Buyer Data')
        print('Choice 7: View Requested Test Drives')
        print('Choice 8: Give Appointments For Test Drives')
        print('Choice 9: View Exported Data')
        print('Choice 10: Confirm Deal')
        print('Choice 11: Main Menu')
        userchoice = input(
            '------------------------------------------------------\nPlease Enter your Choice from '
            'one of '
            'the above options|- ')
        if userchoice == "1":
            # ADD CAR TO INVENTORY
            make.append(input(" Make -"))
            model.append(input(" Model -"))
            year.append(int(input(" Year -")))
            mileage.append(int(input(" Mileage -")))
            oldowner.append(input(" Old owner -"))
            x = int(input(" Asking Price -"))
            askprice.append(x)
            y = int(input(" Selling Price -"))
            sellprice.append(y)
            available.append('On Sale')
            # add a vehicle
        elif userchoice == '2':
            # DELETE A CAR
            if len(model) < 2:
                print('Sorry there are no vehicles currently in inventory')
                continue
            Products = int(input('Please enter the number associated with the vehicle to be removed: '))
            if Products - 1 > len(model):
                print('This is an invalid number')
            else:
                del make[Products]
                del model[Products]
                del year[Products]
                del mileage[Products]
                del oldowner[Products]
                del askprice[Products]
                del sellprice[Products]
                del available[Products]
                print()
                print('This vehicle has been removed')
        elif userchoice == '3':
            # CAR LIST
            if len(model) < 2:
                print('Sorry there are no vehicles currently in inventory')
                continue
            else:
                counter = 0
                while counter < len(model):
                    print('CAR ID', [counter])
                    print('\t', 'MAKE =', make[counter], '\n\t', 'MODEL =', model[counter], '\n\t', 'YEAR =',
                          year[counter], '\n\t',
                          "MILEAGE =", mileage[counter], '\n\t', 'OLD OWNER =', oldowner[counter], '\n\t',
                          'ASKING PRICE =', askprice[counter], '\n\t', 'PRICE =', sellprice[counter], '\n\t',
                          'STATUS =', available[counter])
                    counter += 1
        elif userchoice == '4':
            # EDIT LISTING
            if len(model) < 2:
                print('Sorry there are no vehicles currently in inventory')
                continue
            counter = 1
            while counter < len(model):
                print('CAR ID', [counter])
                print('\t', 'MAKE =', make[counter], '\n\t', 'MODEL =', model[counter], '\n\t', 'YEAR =',
                      year[counter], '\n\t',
                      "MILEAGE =", mileage[counter], '\n\t', 'OLD OWNER =', oldowner[counter], '\n\t',
                      'ASKING PRICE =', askprice[counter], '\n\t', 'PRICE =', sellprice[counter], '\n\t',
                      'STATUS =', available[counter])
                counter += 1
            Products = int(input('Please enter the number associated with the vehicle to be edited: '))
            products1 = input("make")
            products2 = input('model')
            products3 = input("year")
            products4 = input("mileage")
            products5 = input("old owner")
            products6 = int(input('Asking Price'))
            products7 = int(input(" Selling Price -"))
            products8 = input('availability')
            if Products - 2 > len(model):
                print('This is an invalid number')
            else:
                del make[Products]
                del model[Products]
                del year[Products]
                del mileage[Products]
                del oldowner[Products]
                del askprice[Products]
                del sellprice[Products]
                del available[Products]
                make.insert(Products, products1)
                model.insert(Products, products2)
                year.insert(Products, products3)
                mileage.insert(Products, products4)
                oldowner.insert(Products, products5)
                askprice.insert(Products, products6)
                sellprice.insert(Products, products7)
                available.insert(Products, products8)
                print('-----------------------------')
                print('This vehicle has been updated')
                print('-----------------------------')
        elif userchoice == '5':
            # EXPORT CAR LIST
            if len(model) < 2:
                print('Sorry there are no vehicles currently in inventory')
                continue
            from itertools import zip_longest
            d = [make, model, year, mileage, oldowner, askprice, sellprice, available]
            data = zip_longest(*d, fillvalue='')
            with open('CAR LIST.csv', 'w', newline='') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(("MAKE", "MODEL", 'YEAR', 'MILEAGE', 'OLD OWNER', 'ASK PRICE', 'SELL PRICE', 'AVAILABILITY'))
                wr.writerows(data)
            myfile.close()
            print('The vehicle inventory has been exported to a file')
        elif userchoice == '6':
            # EXPORT CAR LIST
            if len(model) < 2:
                print('Sorry there are no customer information ')
                continue
            from itertools import zip_longest
            telecopy = [str(x) for x in buyertele1]
            d = [buyername1, telecopy, buyeraddress,carid]
            data = zip_longest(*d, fillvalue='')
            with open('CUSTOMER DATA.csv', 'w', newline='') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(("NAME", "TELEPHONE", 'ADDRESS', 'CAR ID'))
                wr.writerows(data)
            myfile.close()
            print('The vehicle inventory has been exported to a file')
        elif userchoice == '7':
            # VIEW REQUESTED TEST DRIVES
            if len(buyername) < 2:
                print('Sorry there are no test drive request currently ')
                continue
            counter = 1
            while counter < len(buyername):
                print('Customer id', [counter])
                print('\t', 'NAME =', buyername[counter], '\n\t', 'TELEPHONE =', buyertele[counter], '\n\t',
                      'REQUESTED CAR =',
                      buyertest[counter], '\n\t',
                      "APPOINTMENT =", appointment[counter])
                counter += 1
        elif userchoice == '8':
            # GIVE APPOINTMENT
            if len(buyername) < 2:
                print('Sorry there are no test drive request currently ')
                continue
            counter = 1
            while counter < len(buyername):
                print('Customer id', [counter])
                print('\t', 'NAME =', buyername[counter], '\n\t', 'TELEPHONE =', buyertele[counter], '\n\t',
                      'REQUESTED CAR =',
                      buyertest[counter], '\n\t',
                      "APPOINTMENT =", appointment[counter])
                counter += 1
            Products = int(input('Please enter the number associated with the customer to add appointment: '))
            products = input("please enter appointment details")
            if Products - 2 > len(buyername):
                print('This is an invalid number')
            else:
                del appointment[Products]
                appointment.insert(Products, products)
                print('appointment added')
        elif userchoice == '9':
            # EXPORT CAR LIST
            if len(model) < 2:
                print('Sorry there are no vehicles currently in inventory')
                continue
            else:
                f = open('CAR LIST.csv', 'r')
                with f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(row)
        elif userchoice == '10':
            # CLOSE DEAL
            if len(model) < 2:
                print('Sorry there are no vehicles currently in inventory')
                continue
            counter = 1
            while counter < len(model):
                print('CAR ID', [counter])
                print('\t', 'MAKE =', make[counter], '\n\t', 'MODEL =', model[counter], '\n\t', 'YEAR =',
                      year[counter], '\n\t',
                      "MILEAGE =", mileage[counter], '\n\t', 'OLD OWNER =', oldowner[counter], '\n\t',
                      'ASKING PRICE =', askprice[counter], '\n\t', 'PRICE =', sellprice[counter], '\n\t',
                      'STATUS =', available[counter])
                counter += 1
            Products = int(input('Please enter the number associated with the vehicle to be edited : '))
            products = int(input('Enter Month -'))
            products1 = '~ SOLD ~'
            if Products - 2 > len(model):
                print('This is an invalid number')
            else:
                x = askprice[Products]
                y = sellprice[Products]
                z = y - x
                profit[products].append(z)
                available.insert(Products, products1)
                print('Profit(monthly) =', prof(profit[products]))
                print('-----------------------------')
                print('This vehicle has been updated')
                print('-----------------------------')
    elif User_Choice == "2":
        # CUSTOMER MENU
        print('Choice 1: Request Test Drive')
        print('Choice 2: View Store')
        print('Choice 3: Buy Car')
        print('Choice 4: View Status Of Requested Test Drives')
        print('Choice 5: View Status Of Maintenance')
        print('Back To Main Menu')
        userchoice = input(
            '------------------------------------------------------\nPlease Enter your Choice from '
            'one of '
            'the above options|- ')
        if userchoice == "1":
            # REQUEST A TEST DRIVE
            if len(model) < 2:
                print('Sorry there are no vehicles currently in inventory')
                continue
            counter = 0
            while counter < len(model):
                print('Customer id', [counter])
                print('\t', 'NAME =', make[counter], '\n\t', 'MODEL =', model[counter], '\n\t', 'YEAR =',
                      year[counter], '\n\t',
                      "MILEAGE =", mileage[counter], '\n\t', 'PRICE =', sellprice[counter], '\n\t',
                      'STATUS =', available[counter])
                counter += 1
            buyertest.append(input("Car id of test drive -"))
            buyername.append(input("Name -"))
            buyertele.append(input("Telephone -"))
            print('Your Request Has Been Made')
        elif userchoice == '2':
            # STORE AND SORT IF NEEDED
            if len(model) < 2:
                print('Sorry there are no vehicles currently in inventory')
                continue
            counter = 0
            while counter < len(model):
                print('Car id', [counter])
                print('\t', 'NAME =', make[counter], '\n\t', 'MODEL =', model[counter], '\n\t', 'YEAR =',
                      year[counter], '\n\t',
                      "MILEAGE =", mileage[counter], '\n\t', 'PRICE =', sellprice[counter], '\n\t',
                      'STATUS =', available[counter])
                counter += 1
            print('Do You Want To Sort?')
            print('1.Yes\n2.No')
            choice = input('-')
            if choice == '1':
                print('Select Sort Method\n1.By Price\n2.By Mileage')
                x = input('-')
                if x == '1':
                    sortcarid = carid.copy()
                    sortsellprice = sellprice.copy()
                    sortmake = make.copy()
                    sortmodel = model.copy()
                    sortyear = year.copy()
                    sortmileage = mileage.copy()
                    sortavailable = available.copy()
                    neworder = list(zip(sortmake, sortsellprice, sortmodel, sortyear, sortmileage, sortavailable))
                    l = len(neworder)
                    for i in range(0, l):
                        for k in range(0, l - i - 1):
                            if (neworder[k][1] > neworder[k + 1][1]):
                                temporder = neworder[k]
                                neworder[k] = neworder[k + 1]
                                neworder[k + 1] = temporder
                    for ma, se, mo, ye, mi, av in neworder:
                        print(f'Make: {ma}')
                        print(f'Model: {mo}')
                        print(f'Year: {ye}')
                        print(f'Mileage: {mi}')
                        print(f'Price: {se}')
                        print(f'Status: {av}')
                        print(' \n-----------------\n ')
                if x == '2':
                    sortcarid = carid.copy()
                    sortsellprice = sellprice.copy()
                    sortmake = make.copy()
                    sortmodel = model.copy()
                    sortyear = year.copy()
                    sortmileage = mileage.copy()
                    sortavailable = available.copy()
                    neworder = list(zip(sortmake, sortmileage, sortmodel, sortyear, sortsellprice, sortavailable))
                    l = len(neworder)
                    for i in range(0, l):
                        for k in range(0, l - i - 1):
                            if (neworder[k][1] > neworder[k + 1][1]):
                                temporder = neworder[k]
                                neworder[k] = neworder[k + 1]
                                neworder[k + 1] = temporder
                    for ma, mi, mo, ye, se, av in neworder:
                        print(f'Make: {ma}')
                        print(f'Model: {mo}')
                        print(f'Year: {ye}')
                        print(f'Mileage: {mi}')
                        print(f'Price: {se}')
                        print(f'Status: {av}')
                        print(' \n-----------------\n ')
            if choice == '2':
                print('-----------------')
            else:
                print("Please Try Again")
        elif userchoice == '3':
            # BUY CAR
            if len(model) < 2:
                print('Sorry there are no vehicles currently in inventory')
                continue
            counter = 0
            while counter < len(model):
                print('Customer id', [counter])
                print('\t', 'NAME =', make[counter], '\n\t', 'MODEL =', model[counter], '\n\t', 'YEAR =',
                      year[counter], '\n\t',
                      "MILEAGE =", mileage[counter], '\n\t', 'PRICE =', sellprice[counter], '\n\t',
                      'STATUS =', available[counter])
                counter += 1
            Products = int(input('Please enter the number associated with the vehicle to be buy: '))
            products = input("please enter your name")
            products1 = int(input('please enter phone number'))
            products2 = input('please enter your address')
            if Products - 2 > len(model):
                print('This is an invalid number')
            else:
                del available[Products]
                available.insert(Products, "~RESERVED~")
                buyername1.append( products)
                buyertele1.append( products1)
                buyeraddress.append(products2)
                carid.insert(Products, Products)
                x = input("do you need service for this car?\n 1.Yes|2.No")
                if x == "1":
                    buyermaintain.insert(Products,[ products, products1, Products])
                    count.append('1')
                    print('---Your Order Has Been Received----')
                    print('---Admin Will Confirm Your Order Soon---')
                    print('---Thank you---')
                elif x == "2":
                    print('---Your Order Has Been Received----')
                    print('---Admin Will Confirm Your Order Soon---')
                    print('---Thank you---')
                else:
                    print('invalid number')
        elif userchoice == '4':
            # VIEW STATUS OF REQUESTED TEST DRIVE
            if len(buyername) < 1:
                print('Sorry there are no test drive requests currently')
                continue
            counter = 1
            while counter < len(buyername):
                print('Customer id', [counter])
                print('\t', 'NAME =', buyername[counter], '\n\t', 'TELEPHONE =', buyertele[counter], '\n\t', 'STATUS =',
                      appointment[counter])
                counter += 1
        elif userchoice == '5':
            # VIEW STATUS OF MAINTENANCE
            if len(count) < 2:
                print('Sorry there are service requests currently')
                continue
            counter = 1
            while counter < len(count):
                print('Customer id', [counter])
                print('\t', 'CUSTOMER AND CAR DETAILS =', buyermaintain[counter], '\n', '\t', 'MAINTENANCE REPORT =',
                      buyermaintain1[counter], '\n', '\t', 'COST =', maintaincost[counter])
                counter += 1
        else:
            print('Invalid Input')
    elif User_Choice == "3":
        # TECHNICIAN MENU
        print('Choice 1: View Requested Services')
        print('Choice 2: Add Maintenance Report And Cost')
        print('Choice 3: Main Menu')
        userchoice = input(
            '------------------------------------------------------\nPlease Enter your Choice from '
            'one of '
            'the above options|- ')
        if userchoice == '1':
            # VIEW REQUESTED MAINTENANCE SERVICES
            if len(count) < 2:
                print('Sorry there are service requests currently')
                continue
            counter = 0
            while counter < len(count):
                print('Order Number', [counter])
                print('\t', 'CUSTOMER AND CAR DETAILS\n\t(name,telephone,car id) =', buyermaintain[counter], '\n', '\t', 'MAINTENANCE REPORT =',
                      buyermaintain1[counter])
                counter += 1
        elif userchoice == '2':
            # ADD REPORT AND MAINTENANCE COST
            if len(count) < 2:
                print('Sorry there are maintain requests currently')
                continue
            counter = 1
            while counter < len(count):
                print('Order Number', [counter])
                print('\t', 'CUSTOMER AND CAR DETAILS\n\t(name,telephone,car id) =', buyermaintain[counter], '\n', '\t', 'MAINTENANCE REPORT =',
                      buyermaintain1[counter], '\n', '\t', 'COST =', maintaincost[counter])
                counter += 1
            if len(count) < 1:
                print('Sorry there are no request currently')
                continue
            edit = int(input('Order Number To Edit'))
            edit1 = input('Enter Your Report')
            edit2 = int(input('Enter Month'))
            edit3 = int(input('Add Maintenance Cost'))
            buyermaintain1.insert(edit, edit1)
            maintaincost.insert(edit, edit3)
            profit1[edit2].append(edit3)
        elif userchoice == '3':
            print('bye')

    elif User_Choice == "4":
        # OWNER MENU
        print('Choice 1: Generate Report')
        print('Choice 2: Add Maintained Report')
        print('Choice 3: Main Menu')
        userchoice = input(
            '------------------------------------------------------\nPlease Enter your Choice from '
            'one of '
            'the above options|- ')
        if userchoice == '1':
            print(' ~ Profit By Car Sales ~')
            print(' January   -', prof(profit[1]))
            print(' February  -', prof(profit[2]))
            print(' March     -', prof(profit[3]))
            print(' April     -', prof(profit[4]))
            print(' May       -', prof(profit[5]))
            print(' June      -', prof(profit[6]))
            print(' July      -', prof(profit[7]))
            print(' August    -', prof(profit[8]))
            print(' September -', prof(profit[9]))
            print(' October   -', prof(profit[10]))
            print(' November  -', prof(profit[11]))
            print(' December  -', prof(profit[12]))
            print('-----------------------------')
            print(' PROFIT  =', prof(profit),'\n-----------------------------\n\n')
            print(' ~ Profit By Services ~')
            print(' January   -', prof(profit1[1]))
            print(' February  -', prof(profit1[2]))
            print(' March     -', prof(profit1[3]))
            print(' April     -', prof(profit1[4]))
            print(' May       -', prof(profit1[5]))
            print(' June      -', prof(profit1[6]))
            print(' July      -', prof(profit1[7]))
            print(' August    -', prof(profit1[8]))
            print(' September -', prof(profit1[9]))
            print(' October   -', prof(profit1[10]))
            print(' November  -', prof(profit1[11]))
            print(' December  -', prof(profit1[12]))
            print('---------------------------------')
            print(' PROFIT  =', prof(profit1),
                  '\n---------------------------------\n\n')
            print(' ~ Total Profit Monthly ~')
            mothly = [x + y for x, y in zip(profit, profit1)]
            print(' January   -', prof(mothly[1]))
            print(' February  -', prof(mothly[2]))
            print(' March     -', prof(mothly[3]))
            print(' April     -', prof(mothly[4]))
            print(' May       -', prof(mothly[5]))
            print(' June      -', prof(mothly[6]))
            print(' July      -', prof(mothly[7]))
            print(' August    -', prof(mothly[8]))
            print(' September -', prof(mothly[9]))
            print(' October   -', prof(mothly[10]))
            print(' November  -', prof(mothly[11]))
            print(' December  -', prof(mothly[12]))
            print('------------------------------')
            print('   TOTAL ANNUAL PROFIT  = ', prof(profit) + prof(profit1), '\n------------------------------\n\n')
            print(' ~ Total Profit ~')
            print('Car Sales Profit = ',prof(profit))
            print('Services Profit  = ', prof(profit1))
            print('-----------------------------')
            print('   TOTAL PROFIT  = ',prof(profit)+prof(profit1),'\n-----------------------------\n\n')
            print(' ~ Most Sold Models ~ ')
            from collections import Counter
            c = Counter(model1)
            c.most_common(5)
            print("", c.most_common(5))
            x = c.most_common(5)
            for x in x:
                print(x)