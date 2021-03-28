import os
import _pickle as pickle
import json
from Classes import Product, ShopKeeper

fileName = "ProductList.txt"


dokandar = ShopKeeper(0.0)


def goToMenu():
    print("\n\nEnter any key to return to Menu")
    input()
    menu()


def menu():
    os.system("cls")
    option = input("Type The Operation Number You Want to Perform!\n1. Add Product\n2. Delete Product\n3. Buy a "
                   "Product\n4. Sell a Product\n5. Show List of All Products\n6. Show Current Balance\n"
                   "7. Exit The Program\n")

    if option == '1':
        addProduct()
    elif option == '2':
        updateProductList(isDelete=True)
    elif option == '3':
        buyProduct()
    elif option == '4':
        updateProductList(isSold=True)
    elif option == '5':
        showProductList()
    elif option == '6':
        print("Total Balance: " + str(dokandar.getBalance()))
        goToMenu()
    elif option == '7':
        exit
    else:
        menu()


def countLastId():
    with open(fileName, "r") as f:
        currentId = 0
        lastLine = ''
        for line in f:
            if line != '\n':
                lastLine = line
        obj = json.loads(lastLine)
        currentId = obj["id"]
    return currentId


def addProduct():
    os.system("cls")
    new_product = Product(
        input("Enter Product Name: "),
        float(input("Enter Product Buy Price: ")),
        float(input("Enter Product Sell Price: ")),
        int(input("Enter Product Availability: ")),
    )
    with open(fileName, "a") as f:
        json.dump({
            'id': countLastId() + 1,
            'name': new_product.name,
            'buy_price': new_product.buy_price,
            'sell_price': new_product.sell_price,
            'availability': new_product.availability,
            'total_profit': new_product.total_profit,
        }, f)
        f.write('\n')
    goToMenu()


def updateProductList(isDelete=False, isBought=False, isSold=False):
    os.system("cls")
    option = input(
        "Type Option Number from below\n1.Operation by ID\n2.Operation by Name\n")
    if option == '1':
        reference = int(input("Enter ID: "))
    elif option == '2':
        reference = input("Enter Name: ")
    json_lines = []
    isError = True
    with open(fileName, "r") as fp:
        for line in fp.readlines():
            product = json.loads(line)
            if not product["id"] == reference and not product["name"] == reference:
                json_lines.append(line)
            else:
                isError = False
                if isDelete:
                    pass
                elif isBought:
                    bought_amount = int(
                        input("Enter How Many of The Product You Want to Buy: "))
                    product["availability"] += bought_amount
                    dokandar.setBalance(
                        dokandar.getBalance() - (bought_amount *
                                                 product["buy_price"])
                    )
                    line = json.dumps(product)
                    line += "\n"
                    json_lines.append(line)
                elif isSold:
                    sold_amount = int(
                        input("How Many Items Do You Want to Sell: "))
                    while True:
                        if product["availability"] < sold_amount:
                            print(
                                "Invalid Amount! You Have Less Item Available Than You Entered\n")
                            sold_amount = int(
                                input("Enter Amount Again or Press 0 (Zero) to Exit: "))
                            if sold_amount == 0:
                                menu()
                                break
                            else:
                                continue
                        else:
                            product["availability"] -= sold_amount
                            product["total_profit"] += (sold_amount *
                                                        product["sell_price"])
                            dokandar.setBalance(
                                dokandar.getBalance() + (sold_amount *
                                                         product["sell_price"])
                            )
                            line = json.dumps(product)
                            line += "\n"
                            json_lines.append(line)
                            break
    with open(fileName, "w") as fp:
        fp.writelines(json_lines)
    if isError:
        print("ID or Name is not Matched!!")
    elif isDelete:
        print("Items Are Deleted Successfully\n")
    elif isBought:
        print("Items Are Bought Successfully\n")
    elif isSold:
        print("Items Are Sold Successfully\n")
    goToMenu()


def buyProduct():
    os.system("cls")
    option = input(
        "Select Option From Below:\n1.Buy New Product\n2.Buy Existing Product\n")
    if option == '1':
        addProduct()
    elif option == '2':
        updateProductList(isBought=True)


def showProductList():
    with open(fileName, "r") as f:
        for line in f:
            product = json.loads(line)
            print(f'ID: {product["id"]}\tName: {product["name"]}\tBuy Price: {product["buy_price"]}\tSell Price: {product["sell_price"]}\tAvailable Product: {product["availability"]}\tTotal Profit: {product["total_profit"]}')
    goToMenu()


menu()
