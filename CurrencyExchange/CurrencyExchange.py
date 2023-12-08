import requests

# Create a class called CurrencyExchange
class CurrencyExchange:
    # Initialize the class with an API key and a base currency
    def __init__(self):
        self.api_key = open(r"C:\Users\DELL\Desktop\API_access_key.txt","r").readline() # Add ur Api key into text file and define the path according to it.
        self.base_currency = "INR" # Default base currency

    # Function to make an HTTP request and handle exceptions
    def do_request(self,url):
        try:
            # Send an HTTP GET request with the provided URL and API key in headers
            res = requests.get(url,headers={"apikey": self.api_key})
            res.raise_for_status() # Raise an exception for HTTP errors
            return res.json() # Parse the JSON response and return it
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return None
        
    # Function to display the current base currency
    def show_base_currency(self):
        return f"Base Currency: {self.base_currency}"

    # Function to set a new base currency
    def set_base_currency(self,base_currency):
        self.base_currency = base_currency
        return f"Base currency set to {self.base_currency}"

    # Function to retrieve and display available currency symbols
    def show_symbols(self):
        response = self.do_request("https://api.apilayer.com/fixer/symbols")
        output = []
        for key,value in response["symbols"].items():
            output.append(f"{key} = {value}")
        return output
    
    # Function to retrieve and display the latest exchange rates
    def latest_rates(self):
        base = input("Enter the three-letter currency code of your preferred base currency.(example:eur) : ")
        symbols = input("Enter a list of comma-separated currency codes "
                        "to limit output currencies.(example:gbp,jpy,eur): ")
        response = self.do_request(f"https://api.apilayer.com/fixer/latest?symbols={symbols}&base={base}")
        return f"Date:{response['date']} \nBase Currency : {response['base']} \nRates:{response['rates']}"

    # Function to perform currency conversion
    def convert(self):
        convert_from = input("Enter the three-letter currency code of the currency you would like to convert "
                             "from.(example:eur) :")
        convert_to = input("Enter the three-letter currency code of the currency you would like to convert to.("
                           "example:gbp,jpy,eur):")
        amount = int(input("Enter the amount to be converted."))
        response = self.do_request(
            f"https://api.apilayer.com/fixer/convert?to={convert_to}&from={convert_from}&amount={amount}")
        return f"From: {response['query']['from']}\nTo: {response['query']['to']}\nAmount: {response['query']['amount']}\nResult:{response['result']}"

    # Function to retrieve and display exchange rates for a specific date
    def rates_on_date(self):
        date = input("Enter the date of your preferred timeframe in format (yyyy-mm-dd): ")
        base = input("Enter the three-letter currency code of your preferred base currency.(example:eur) : ")

        symbols = input("Enter a list of comma-separated currency codes "
                        "to limit output currencies.(example:gbp,jpy,eur): ")
        response = self.do_request(f"https://api.apilayer.com/fixer/{date}?symbols={symbols}&base={base}")
        return f"Base Currency: {response['base']}\nDate: {response['date']}\nResult: {response['rates']}"

    # Function to retrieve and display historical exchange rates within a specified time frame
    def timeseries(self):
        start_date = input("Enter the start date of your preferred timeframe in format (yyyy-mm-dd): ")
        end_date = input("Enter the end date of your preferred timeframe in format (yyyy-mm-dd): ")
        response = self.do_request(
            f"https://api.apilayer.com/fixer/timeseries?start_date={start_date}&end_date={end_date}&base={self.base_currency}")
        return f"Start Date = {response['start_date']}\nEnd date= {response['end_date']}\nBase Currency= {response['base']}\nResult= {response['rates']}"

    # Function to retrieve and display exchange rate fluctuations within a specified time frame
    def fluctuation(self):
        start_date = input("Enter the start date of your preferred timeframe in format (yyyy-mm-dd): ")
        end_date = input("Enter the end date of your preferred timeframe in format (yyyy-mm-dd): ")
        response = self.do_request(
            f"https://api.apilayer.com/fixer/fluctuation?start_date={start_date}&end_date={end_date}&base={self.base_currency}")
        return f"Start Date= {response['start_date']}\nEnd Date= {response['end_date']}\nBase Currency= {response['base']}\nResult= {response['rates']}"

# Create an instance of the CurrencyExchange class
c = CurrencyExchange()

# Create a menu for the user to choose options
while True:
    print("""Choose one of the below options:
                1.Set Base currency. Default base currency is INR.
                2.Show Base Currency.
                3."/symbols" Returns all available currencies.
                4."/latest" Returns real-time exchange rate data for all available or a specific set of currencies.
                5."/convert" Allows for conversion of any amount from one currency to another.
                6."/{date}" Returns historical exchange rate data for all available or a specific set of currencies.
                7."/timeseries" Returns daily historical exchange rate data between two specified dates for all available or a specific set of currencies.
                8."/fluctuation" Returns fluctuation data between two specified dates for all available or a specific set of currencies.
                9. Exit.
    """)
    option = int(input("Enter a number: "))
    if option == 1:
        currency = input("Enter the base currency: ")
        c.set_base_currency(currency)
    elif option == 2:
        print(c.show_base_currency())
    elif option == 3:
        print(c.show_symbols())
    elif option == 4:
        print(c.latest_rates())
    elif option == 5:
        print(c.convert())
    elif option == 6:
        print(c.rates_on_date())
    elif option == 7:
        print(c.timeseries())
    elif option == 8:
        print(c.fluctuation())
    elif option == 9:
        break # Exit the loop if the user chooses option 9