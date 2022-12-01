import csv
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from get_crypto_data import get_history

key = "Exiq4NbNJg6m9z5N"
days = get_history("ALB", key)['day']
albireo = get_history("ALB", key)['value']
bharani = get_history("BHA", key)['value']
castula = get_history("CAS", key)['value']
dubhe = get_history("DUB", key)['value']    
elgafar = get_history("ELG", key)['value']
fawaris = get_history("FAW", key)['value']
xuange = get_history("XUA", key)['value']

def alice():
    current_portfolio_value = -0
    money_left = 1000000
    for i in range(len(albireo)):
        day = i
        stockprice = albireo[i]
        if stockprice < 1500 and money_left != 0:
            amount_stocks = money_left / stockprice
            money_left = 0
            current_portfolio_value = current_portfolio_value + amount_stocks * stockprice
        if stockprice > 1600 and amount_stocks != 0:
            current_portfolio_value  = 0.99 * (amount_stocks * stockprice)
            money_left = current_portfolio_value
            amount_stocks = 0
        if i == 364:
            if amount_stocks > 0:
                current_portfolio_value  = 0.99 * (amount_stocks * stockprice)
            money_left = current_portfolio_value
            amount_stocks = 0
    return "{:.2f}".format(current_portfolio_value)

def frank():
    current_portfolio_value = 0
    money_left = 1000000
    for i in range(len(fawaris)):
        day = i
        stockprice = fawaris[i]
        if day == (1) and money_left !=0:
            amount_stocks = money_left / stockprice
            money_left = 0
            current_portfolio_value = current_portfolio_value + amount_stocks * stockprice
        if stockprice == stockprice * 1.2 and amount_stocks !=0:
            current_portfolio_value  = 0.99 * (amount_stocks * stockprice)
            money_left = current_portfolio_value
            amount_stocks = 0

        if stockprice == stockprice *0.8 and money_left != 0:
            amount_stocks = money_left / stockprice
            money_left = 0
            current_portfolio_value = current_portfolio_value + amount_stocks*stockprice
        if i == 364:
            current_portfolio_value  = 0.99 * (amount_stocks * stockprice)
            money_left = current_portfolio_value
            amount_stocks = 0
    return "{:.2f}".format(current_portfolio_value)  
    

def bob():
    current_portfolio_value = -0
    money_left = 1000000
    for i in range(len(bharani)):
        day = i
        stockprice = bharani[i]
        if stockprice < 1000 and money_left != 0:
            amount_stocks = money_left / stockprice
            money_left = 0
            current_portfolio_value = current_portfolio_value + amount_stocks * stockprice
        if stockprice > 1100 and amount_stocks != 0:
            current_portfolio_value  = 0.99 * (amount_stocks * stockprice)
            money_left = current_portfolio_value
            amount_stocks = 0
        if i == 364:
            if  amount_stocks > 0:
                current_portfolio_value  = 0.99 * (amount_stocks * stockprice)
            money_left = current_portfolio_value
            amount_stocks = 0
    return "{:.2f}".format(current_portfolio_value)

def eve():
    current_portfolio_value = 0
    money_left = 1000000
    for i in range(len(elgafar)):
        day = i
        stockprice = elgafar[i]
        if str(day).endswith("1") and money_left !=0:
            amount_stocks = money_left / stockprice
            money_left = 0
            current_portfolio_value = current_portfolio_value + amount_stocks * stockprice
        if str(day).endswith("5") and amount_stocks !=0:
            current_portfolio_value  = 0.99 * (amount_stocks * stockprice)
            money_left = current_portfolio_value
            amount_stocks = 0
        if i == 364:
            current_portfolio_value  = 0.99 * (amount_stocks * stockprice)
            money_left = current_portfolio_value
            amount_stocks = 0
    return "{:.2f}".format(current_portfolio_value)

def ups_downs(crypto):
    lup = 0
    ldown = 0
    temp_lup = 0
    temp_ldown =  0
    up_days = 0
    down_days = 0
    current_value = ''
    prev_value = ''

    for i in range(len(crypto)):
        if i == 0:
            current_value = crypto[i]
            prev_value = 0
        elif i > 0:
            prev_value = crypto[i-1]
            current_value = crypto[i]
            if prev_value > current_value:
                down_days +=1
            elif prev_value < current_value:
                up_days +=1
    return [up_days, down_days]


table = PrettyTable()
table.field_names = ["Name","AVG", "MIN", "MAX", "SD", "Q1", "Q2", "Q3", "RNG", "IQR", "UPS", "DOWNS"]
table.add_row(["Albireo", np.average(albireo), np.min(albireo), np.max(albireo), np.std(albireo), np.percentile(albireo, 25), np.percentile(albireo, 50), np.percentile(albireo, 75), np.ptp(albireo), np.subtract(*np.percentile(albireo, [75, 25])), ups_downs(albireo)[0], ups_downs(albireo)[1]])
table.add_row(["Bharani", np.average(bharani), np.min(bharani), np.max(bharani), np.std(bharani), np.percentile(bharani, 25), np.percentile(bharani, 50), np.percentile(bharani, 75), np.ptp(bharani), np.subtract(*np.percentile(bharani, [75, 25])), ups_downs(bharani)[0], ups_downs(bharani)[1]])
table.add_row(["Castula", np.average(castula), np.min(castula), np.max(castula), np.std(castula), np.percentile(castula, 25), np.percentile(castula, 50), np.percentile(castula, 75), np.ptp(castula), np.subtract(*np.percentile(castula, [75, 25])), ups_downs(castula)[0], ups_downs(castula)[1]])
table.add_row(["Dubhe", np.average(dubhe), np.min(dubhe), np.max(dubhe), np.std(dubhe), np.percentile(dubhe, 25), np.percentile(dubhe, 50), np.percentile(dubhe, 75), np.ptp(dubhe), np.subtract(*np.percentile(dubhe, [75, 25])), ups_downs(dubhe)[0], ups_downs(dubhe)[1]])
table.add_row(["Elgafar", np.average(elgafar), np.min(elgafar), np.max(elgafar), np.std(elgafar), np.percentile(elgafar, 25), np.percentile(elgafar, 50), np.percentile(elgafar, 75), np.ptp(elgafar), np.subtract(*np.percentile(elgafar, [75, 25])), ups_downs(elgafar)[0], ups_downs(elgafar)[1]])
table.add_row(["Fawaris", np.average(fawaris), np.min(fawaris), np.max(fawaris), np.std(fawaris), np.percentile(fawaris, 25), np.percentile(fawaris, 50), np.percentile(fawaris, 75), np.ptp(fawaris), np.subtract(*np.percentile(fawaris, [75, 25])), ups_downs(fawaris)[0], ups_downs(fawaris)[1]])
table.add_row(["Xuange", np.average(xuange), np.min(xuange), np.max(xuange), np.std(xuange), np.percentile(xuange, 25), np.percentile(xuange, 50), np.percentile(xuange, 75), np.ptp(xuange), np.subtract(*np.percentile(xuange, [75, 25])), ups_downs(xuange)[0], ups_downs(xuange)[1]])
print(table)


plt.rcParams["figure.autolayout"] = True
fig, axs = plt.subplots(sharey=True)
plt.title("Line graph of multuple currencies")
plt.xlabel("Day")
plt.ylabel("Price (euro)")
axs.plot(days, bharani, color='red', label="Bharani")
axs.plot(days, albireo, color='purple', label="Albireo")
axs.plot(days, castula, color="green", label="Castula")
axs.plot(days, dubhe, color="blue", label="Dubhe")
axs.plot(days, elgafar, color="cyan", label="Elgafar")
axs.plot(days, fawaris, color="magenta", label="Fawaris")
axs.legend()
fig.tight_layout()
plt.show()

print("alice:", alice())
print("bob:", bob())
print("eve:", eve())
print("frank:", frank())
