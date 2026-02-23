import pandas as pd
import matplotlib.pyplot as plt

CONVERSION_COUNT = 8

#allows a number to be inputted for a menu within specified
def menuInput(first, last):
    try:
        choice = int(input())
    except:
        print("Please enter a number assigned to an option")

        choice = menuInput(first, last)
    else:
        if choice >= first and choice <= last:
            return choice
        else:
            print(f"Please enter a valid choice between {first} and {last}")

            choice = menuInput(first, last)
    

#The menu() function generates the UI the accepts and validates user choice
def menu():

    flag = True

    while flag:
        print("\n\n\n######################################################")
        print("What would you like to do today?")
        print("1. Currency Conversion")
        print("2. Pound Value")
        print("3. Currency performance")
        print("4. Exit")
        print("######################################################")

        choice = menuInput(1, 4)
        
        if choice == 1:
            print("\n\n\n######################################################")
            print("Which conversion would you like to make today?")
            print("1. Pound Sterling (GBP) to Euros (EUR)")
            print("2. Euros (EUR) to Pound Sterling(GBP)")
            print("3. Pound (GBP) to Australian Dollars (AUD)")
            print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
            print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
            print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
            print("7. Pound (GBP) to American Dollars (USD)")
            print("8. American Dollars (USD) to Pound (GBP)")
            print("######################################################")

            menu_choice = menuInput(1, 8)
            currency = get_currency(menu_choice)
            conversion_rate = get_conversion_rate(currency)
            conversion_amount = float(get_amount_to_convert(currency))
            perform_conversion(conversion_amount, conversion_rate, currency)
        
        elif choice == 2:
            currencies = ["EUR", "AUD", "JPY", "USD"]
            print("\n\n\n######################################################")
            for currency in range(0, CONVERSION_COUNT, 2):
                #prints the amount of 

                print(f"1 GBP is worth {get_conversion_rate(get_currency(currency+1))} {currencies[currency//2]}")
            print("######################################################")
        
        elif choice == 3:
            print("\n\n\n######################################################")
            df = pd.read_csv("ESP practice/#2/data.csv")

            plt.grid()
            plt.title("Date vs Currency conversion value")
            plt.xlabel('Date')
            plt.ylabel('Exchange Rate')
            

            # plots a line for every conversion rate
            for conversion in [get_currency(position) for position in range(1, CONVERSION_COUNT+1)]:
                plt.plot(df[conversion] , label = conversion, marker = "", linestyle = "solid", linewidth = 3)
            plt.legend()
            plt.savefig('ESP practice/#2/exchange_rates.png', dpi = 400)

            print("######################################################")
        
        elif choice == 4:
            break
                


        


#Gets the short version of the conversion information based on user menu choice
def get_currency(choice):
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GBP - JPY',
       '6': 'JPY - GBP',
       '7': 'GBP - USD',
       '8': 'USD - GBP'}
    
    return currencies.get(str(choice))


#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate(currency):
    df = pd.read_csv("ESP practice/#2/data.csv")
    
    #for changing date to correct order
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')

    # conversion rate is assigned the most recent value for the currency, because it has been sorted in the previous line
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate


#Accepts and validates user input for the amount they want to convert
def get_amount_to_convert(currency):
    print("You are converting: ",currency)
    
    flag = True
    
    while flag:
        conversion_amount = input("please enter the amount you wish to convert")
    
        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount  


#Performs the conversion and outputs the final values
def perform_conversion(conversion_amount, conversion_rate, currency):
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will receive {} in {}'.format(amount_recieved, currency[6:9]))

if __name__ == "__main__": 
    menu()