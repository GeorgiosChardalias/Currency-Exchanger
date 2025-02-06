from tkinter import *
from tkinter.ttk import *
import requests
from ttkthemes import ThemedTk

# Create main window with 'ubuntu' theme
screen = ThemedTk(theme="ubuntu")
screen.title("Currency Converter")
screen.geometry('700x100')
screen.configure(themebg="ubuntu")
screen.resizable(False, False)

# Function to convert currency
def convert():
    global baseUrl
    global mainUrl

    # Get selected currencies from dropdown menus
    fromCurrency = Cur1.get()
    ToCurrency = Cur2.get()

    # Set API key and base URL
    apiKey = "K3MQO5ISZGAYC6NI"
    baseUrl = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    # Build the full API request URL
    mainUrl = baseUrl + "&from_currency=" + fromCurrency + "&to_currency=" + ToCurrency + "&apikey=" + apiKey
    print(mainUrl)  # For debugging

    # Send request to API
    req_obj = requests.get(mainUrl)

    # Get exchange rate from the API response
    result = req_obj.json()
    exchange_rate = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    # Get amount entered by user and calculate conversion
    ent = float(AmEntry.get())
    Fr = round(exchange_rate * ent, 2)

    # Display the converted amount
    FinalLbl.configure(text=str(Fr))









CE = Label(screen,text = "Currency Exchange",font = ('Arial',15))
CE.grid(row = 0 ,column = 0, columnspan = 4)

Amount = Label(screen,text = "Amount")
Amount.grid(row = 1,column = 0)
From = Label(screen,text = "From")
From.grid(row = 1,column = 1)
To = Label(screen,text = "To")
To.grid(row = 1,column =2)
Convertbutton = Button(screen, text ="Convert", command = convert)
Convertbutton.grid(row =2 ,column = 3)
Cur1 = Combobox(screen,state = 'readonly')
Cur1['values']= ('EUR','USD','JPY','GBP','CAD')
Cur1.grid(row = 2,column = 1)
Cur2 = Combobox(screen,state = 'readonly')
Cur2['values']= ('EUR','USD','JPY','GBP','CAD')
Cur2.grid(row = 2,column = 2)
AmEntry = Entry(screen)
AmEntry.grid(row = 2,column =0)
FinalLbl = Label(screen)
FinalLbl.grid(row= 2,column = 4 )











screen.mainloop()