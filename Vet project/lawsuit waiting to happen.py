import pandas as pd
import datetime
import csv


# stored data
data = {'Owner': [],
        'Pet': [],
        'Item': [],
        'Quantity': [],
        'Price': [],
        'Total': [],
        'Date': [],
        'SubTotal': [],
        'VAT': [],
        'Total Invoice': [],
        }

filename = "vet.csv"

def menu():
    print("Please select an option:")
    print("1. Add another item")
    print("2. Create invoice")
    print("3. View transactions")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

def add_item():
    owner = input("Owner's name: ")
    if not owner:
        print("Please enter the owner's name.")
        return

    pet = input("Pet's name: ")
    if not pet:
        print("Please enter the pet's name.")
        return

    item = input("Item description: ")
    if not item:
        print("Please enter the item description.")
        return

    quantity = input("Quantity: ")
    if not quantity.isdigit():
        print("Please enter a valid quantity.")
        return
    quantity = int(quantity)

    price = input("Price: ")
    if not price.replace('.', '', 1).isdigit():
        print("Please enter a valid price.")
        return
    price = float(price)

    x = datetime.datetime.now()

    total = quantity * price

    data['Owner'].append(owner)
    data['Pet'].append(pet)
    data['Item'].append(item)
    data['Quantity'].append(quantity)
    data['Price'].append(price)
    data['Total'].append(total)
    data['Date'].append(x)

     # Write data to CSV file
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

    print("Item added successfully.\n")

def create_invoice():
    if not data['Item']:
        print("No items found.\n")
        return

    subtotal = sum(data['Total'])
    vat = subtotal * 0.2
    total = subtotal + vat

    data['SubTotal'].append(subtotal)
    data['VAT'].append(vat)
    data['Total Invoice'].append(total)

    # Display invoice as a table
    invoice_data = {'Item': data['Item'], 'Quantity': data['Quantity'], 'Price': data['Price'], 'Total': data['Total']}
    invoice_df = pd.DataFrame(invoice_data)
    invoice_df.loc[len(invoice_df.index)] = ['Subtotal', '', '', subtotal]
    invoice_df.loc[len(invoice_df.index)] = ['VAT', '', '', vat]
    invoice_df.loc[len(invoice_df.index)] = ['Total', '', '', total]

    print(invoice_df.to_string(index=False))
    print("\nInvoice created successfully.\n")

def view_transactions():
    if not data['Item']:
        print("No items found.\n")
        return

    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    print()

while True:
    choice = menu()
    
    if choice == '1':
        add_item()
    elif choice == '2':
        create_invoice()
    elif choice == '3':
        view_transactions()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.\n")

print("Exiting program. Goodbye!") 
