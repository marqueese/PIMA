import datetime
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime as dt

df = pd.read_csv('Core Employer Set Project - Task4A - Data - November 2021.csv', index_col='ID')
employee = df["Forename"].tolist()
region = df["Region"].tolist()

#main menu
def menu():
    print("\t\t****MAIN MENU****")
    print('1) Enter sales records')
    print('2) Run reports')
    print('3) View everything')
    print('4) See region data')
    y = input("")
    return y

#reports menu
def menu2():
    print("**** Reports Dashboard ****")
    print("1. Individual Employee Report")
    x = int(input(""))
    return x



def ind_emp_check(df_r, id, date1, date2):
    df_r = df_r.T[3:]
    df_r.reset_index(inplace=True)
    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')
    plt.plot(df_r['ID1'], df_r[id])
    plt.show()
    return df_r

y = menu()
while y == 1 or y == 2 or y == 3 or y == 4:
    if y == 1:
        try:
            ID = int(input("Enter the Staff ID "))
            if ID not in df.index.values:
                print('yes')

            date1 = input("Enter Date in dd/mm/yyyy: ")
            day, month, year = date1.split("/")
            date1 = datetime.date(int(year), int(month), int(day))

            if datetime.datetime.strptime(date1.strftime('%d/%m/%Y'), '%d/%m/%Y') > datetime.datetime.strptime(
                    dt.today().strftime('%d/%m/%Y'), '%d/%m/%Y'):
                print("Date is in the future")
            else:
                cost = float(input("Enter the cost : "))
                df.loc[ID, date1.strftime('%d/%m/%Y')] = cost
            # df.to_csv('test2.csv')
        except:
            print("\n\nError Occurred Please try again\n\n")
            y = menu()

    if y == 2:
        x = menu2()
        if x == 1:
            id = int(input("Enter the Employee Id : "))
            s_date = input("Enter Current Date in dd/mm/yyyy: ")
            day, month, year = s_date.split("/")
            s_date = datetime.date(int(year), int(month), int(day))

            e_date = input("Enter Date in dd/mm/yyyy: ")
            day, month, year = e_date.split("/")
            e_date = datetime.date(int(year), int(month), int(day))

            s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
            e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
            ind_emp_check(df, id, s_date, e_date)
        else:
            print("\n\nError Occurred Please try again\n\n")
            x = menu2()
    if y == 3:
        plt.plot(employee, region)
        plt.xticks("the data")
        plt.show()
        y = menu()
    if y == 4:
        print("Specify which region you wish to see")
        region = input()
        region_data = df.loc[df["Region"] == region]
        print(region_data)
        y = menu()
    else:
        y = menu()
else:
    menu()

