# Author: Ang Yinxi William
# Admin No: 201268Z

#Dictionary for drink options
drinks = {'IM':{'name': 'Iced Milo', 'quantity': 8, 'price': 1.5},
          'HM':{'name':'Hot Milo', 'quantity': 2, 'price': 1.2},
          'IC':{'name':'Iced Coffee', 'quantity': 5, 'price': 1.5},
          'HC':{'name':'Hot Coffee', 'quantity': 4, 'price': 1.2},
          '1P':{'name':'100 Plus', 'quantity': 3, 'price': 1.1},
          'CC':{'name':'Coca Cola', 'quantity': 5, 'price': 1.3}}

#Function to add drink
def add_drink_type(drink_id, name, quantity, price):
    drinks[drink_id] = {'name':name, 'quantity':quantity, 'price':price}

#Function to replenish drink inventory
def replenish_drink(drink_id, quantity):
    drinks[drink_id]['quantity'] += quantity


#An endless loop to ensure dictionary remains updated throughout
while True:
    #Whenever loop repeats, ensures no problem with the variables choice and vendor for future use
    vendor = 'monkey'
    choice = 'monkey'

    #Asks user whether they are a vendor and changes variable vendor accordingly
    #Ensures loop is repeated if they do not answer the question
    while True:
        vendor = input('Are you a vendor? (Y/N):')
        vendor = vendor.upper()
        if vendor == 'Y' or vendor == 'N':
            break
        else:
            print("Please enter only Y / N")

    #Greetings
    print('Welcome to ABC Vending Machine')
    print('Select from following choices to continue:')

    #If user is not a vendor, run this code
    if vendor == 'N':
        #selectdrink for number of drinks selected
        #selectprice for price of selected drinks combined
        selectdrink = 0
        selectprice = 0
        stock = {}

        #Creates a dictionary to ensure User does not subtract quantity of drink after cancelling purchase
        for x in drinks:
            stock[x] = drinks[x]['quantity']

        #Displays all drink options with its price
        for x in drinks:
            print(x + '.', drinks[x]['name'], '(' + 'S$' + str(drinks[x]['price']) + ')'
                  ,'   ', 'Qty:', drinks[x]['quantity'])
        print('0. Exit / Payment')

        #Loops till user chooses option 0
        while choice != '0':
            choice = input('Enter choice:').upper()
            isfound = False
            if choice == '0':
                break

            for x in drinks:
                if choice == x:
                    isfound = True

            #Only lets user buy the drink if it exists in the vending machine
            if isfound == True:
                for x in drinks:
                    if choice == x:
                        if stock[x] != 0:
                            stock[x] -= 1
                        else:
                            print('Drink is out of stock!')
                            break
                        selectdrink += 1
                        selectprice += drinks[x]['price']
                        print('No. of drinks selected =', str(selectdrink))
            else:
                print('Invalid option')

        #Payment
        if selectdrink != 0:
            if choice == '0':
                payment = 0
                #Loops if payment isn't enough for price
                while payment < selectprice:
                    print('Please pay: $%.2f' % selectprice)
                    print('Indicate your payment:')
                    while True:
                            try:
                                tennotes = int(input('Enter no. of $10 notes:'))
                                break
                            except:
                                print('Please enter valid number')
                    while True:
                            try:
                                fivenotes = int(input('Enter no. of $5 notes:'))
                                break
                            except:
                                print('Please enter valid number')
                    while True:
                            try:
                                twonotes = int(input('Enter no. of $2 notes:'))
                                break
                            except:
                                print('Please enter valid number')

                    #If user inputs no of notes < 0, set it to 0
                    if tennotes < 0:
                        tennotes = 0
                    if fivenotes < 0:
                        fivenotes = 0
                    if twonotes < 0:
                        twonotes = 0

                    payment = tennotes*10 + fivenotes*5 + twonotes*2
                    if payment < selectprice:
                        print('Not enough to pay for your drinks!')
                        print('Take back your cash!')
                        cancel = input('Do you want to cancel your purchase?(Y/N):').upper()
                        if cancel == 'Y':
                            print('Purchase is cancelled, thank you.')
                            break
                        elif cancel == 'N':
                            continue
                        #Because why not
                        else:
                            print('I will take that as a no')
                            continue

                #If payment is enough, calculate change and thank customer
                if payment > selectprice:
                    change = payment - selectprice
                    for x in drinks:
                        drinks[x]['quantity'] = stock[x]
                    print('Please collect your change: $%.2f' % change)
                    print('Drinks paid, thank you!')
                elif payment == selectprice:
                    for x in drinks:
                        drinks[x]['quantity'] = stock[x]
                    print('No change.')
                    print('Drinks paid, thank you!')

    #if user is vendor, run this code
    if vendor == 'Y':
        print('1. Add Drink Type')
        print('2. Replenish Drink')
        print('0. Exit')

        #Loops until user chooses option 0
        while choice != '0':
            choice = input('Enter choice:')
            if choice == '0':
                break

            if choice == '1':
                isfound = False
                drinkid = input('Enter drink id:').upper()

                for x in drinks:
                    if drinkid == x:
                        isfound = True

                #Lets user add a drink type if it doesn't exist
                if isfound == False:
                    drinkprice = 'monkey'
                    drinkquantity = 'monkey'
                    drinkname = input('Enter name of drink:')

                    #While loops to ensure input of price and quantity is a float/integer respectively
                    while isinstance(drinkprice,float) == False:
                        try:
                            drinkprice = float(input('Enter price of drink:'))
                        except:
                            continue
                    while isinstance(drinkquantity,int) == False:
                        try:
                            drinkquantity = int(input('Enter quantity of drink:'))
                        except:
                            continue
                    add_drink_type(drinkid,drinkname,drinkquantity,drinkprice)
                elif isfound == True:
                    print('Drink id exists!')

            if choice == '2':
                #Lists all drinks, their price and their quantities
                for x in drinks:
                    if drinks[x]['quantity'] > 0:
                        print(x + '.', drinks[x]['name'], '(' + 'S$' + str(drinks[x]['price']) + ')',
                        '  ','Qty :', drinks[x]['quantity'])
                    else:
                        print(x + '.', drinks[x]['name'], '(' + 'S$' + str(drinks[x]['price']) + ')',
                        '  ', '***out of stock***')

                isfound = False
                drinkid = input('Enter drink id:').upper()

                for x in drinks:
                    if drinkid == x:
                        isfound = True

                #Lets user replenish drinks only if they exist in the vending machine
                if isfound == False:
                    print('No drink with this drink id. Try again.')
                elif drinks[drinkid]['quantity'] > 5:
                    print('No need to replenish, quantity is greater than 5.')
                else:
                    drinkquantity = int(input('Enter quantity:'))
                    drinks[drinkid]['quantity'] += drinkquantity
                    print(drinks[drinkid]['name'], 'has been topped up!')

    #To set quantity of drinks to 0 if quantity is below 0
    for x in drinks:
        if drinks[x]['quantity'] < 0:
            drinks[x]['quantity'] = 0
