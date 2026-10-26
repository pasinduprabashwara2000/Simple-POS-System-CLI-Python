customer = []
products = ()

tmp_products = list(products)

def pos_menu():
    while True:
        print("=====================")
        print("POS Menu")
        print("=====================")
        print("1. Customer Management")
        print("2. Product Management")
        print("3. Exit")
        print("=====================")

        try:
            menu_choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if menu_choice == 1:
            customer_management()
        elif menu_choice == 2:
            product_management()
        elif menu_choice == 3:
            print("Program Closed")
            break
        else:
            print("Invalid Choice")

#Product Management
def product_management() :
    while True :
        print("====================")
        print("Product Management")
        print("====================")
        print("1. Add Products")
        print("2. Update Product")
        print("3. Delete Products")
        print("4. Read Products")
        print("5. Read All Products")

        try:
            choice = int(input("Enter Your Choice : "))
        except ValueError:
            print("Please Enter Valid Number")
            continue

        match choice:
            case 1 :
                create_product()
            case 4 :
                read_product()


def create_product() :
    print("====================")
    print("Add Product")
    print("====================")

    name = input("Enter Product Name : ")
    price = float(input("Enter Product Price : "))
    qty = int(input("Enter Product QTY : "))

    if not name or not price or not qty :
        print("All Fields Required")
        return

    if name.isdigit() :
        print("Name should be Texts")
        return


    tmp_products.append({"name": name, "price" : price, "qty": qty})
    print("Product Save Successfully")

def update_products() :
    print("===================")
    print("Update products")
    print("===================")

    index = int(input("Enter Your "))

def read_product() :
    print("====================")
    print("Read Product")
    print("====================")

    print(tmp_products)


#Customer Management
def customer_management():
    while True:
        print("=====================")
        print("Customer Management")
        print("=====================")
        print("1. Create Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. Read Customer")
        print("5. Read All Customers")
        print("6. Customers Summary")
        print("7. Back to POS Menu")
        print("=====================")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if choice == 1:
            create_customer()
        elif choice == 2:
            update_customer()
        elif choice == 3:
            delete_customer()
        elif choice == 4:
            read_customer()
        elif choice == 5:
            read_all_customers()
        elif choice == 6:
            customer_summary()
        elif choice == 7:
            break
        else:
            print("Invalid Choice")

def create_customer():
    print("=====================")
    print("Add Customer")
    print("=====================")

    name = input("Enter Your Name: ").strip()
    email = input("Enter Your Email: ").strip()

    if not name or not email:
        print("Name and Email are required")
        return

    if name.isdigit() or email.isdigit():
        print("Invalid Data Inputs")
        return

    customer.append({"name": name, "email": email})
    print("Customer Created Successfully")


def update_customer():
    print("=====================")
    print("Update Customer")
    print("=====================")

    if not customer:
        print("No customers")
        return

    try:
        index = int(input("Enter Your Customer ID: "))
    except ValueError:
        print("Please enter a valid number")
        return

    if index < 1 or index > len(customer):
        print("Invalid ID")
        return

    name = input("Enter Customer Name: ").strip()
    email = input("Enter Customer Email: ").strip()

    if not name or not email:
        print("Name and Email are required")
        return

    if name.isdigit() or email.isdigit():
        print("Invalid Data Types")
        return

    customer[index - 1]["name"] = name
    customer[index - 1]["email"] = email

    print("Customer Updated Successfully")


def delete_customer():
    print("=====================")
    print("Delete Customer")
    print("=====================")

    if not customer:
        print("No customers")
        return

    try:
        index = int(input("Enter Customer ID: "))
    except ValueError:
        print("Please enter a valid number")
        return

    if index < 1 or index > len(customer):
        print("Invalid Number")
        return

    customer.pop(index - 1)
    print("Customer Deleted Successfully")


def read_customer():
    print("=====================")
    print("Read Customer")
    print("=====================")

    if not customer:
        print("No Customers")
        return

    try:
        index = int(input("Enter Customer No: "))
    except ValueError:
        print("Please enter a valid number")
        return

    if index < 1 or index > len(customer):
        print("Invalid Number")
        return

    print("Name:", customer[index - 1]["name"])
    print("Email:", customer[index - 1]["email"])


def read_all_customers():
    print("=====================")
    print("All Customers")
    print("=====================")

    if not customer:
        print("No customers found")
        return

    for index, c in enumerate(customer, start=1):
        print(f"{index}. Name: {c['name']}, Email: {c['email']}")


def customer_summary():
    print("=====================")
    print("Customers Summary")
    print("=====================")
    print("Total Customers:", len(customer))

# Start the program
pos_menu()
