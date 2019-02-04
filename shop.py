####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Abdullah's dinner" #complete me!
signature_flavors = ["Cof & Te", "vanilla tuna", "coffee cupcake"] #complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print("Our menu:")
    for k, v in menu.items():
        #todo: try to change the num of decmial places 
        print("- \"%s\" (SAR %f)" %(k, v))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (SAR %s each):" % original_price)
    # your code goes here!
    for itm in original_flavors:
        print("- \"%s\"" %(itm))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (SAR %s each):" % signature_price)
    # your code goes here!
    for itm in signature_flavors:
        print("- \"%s\"" %(itm))


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu:
        return True
    else:
        # return False  this is mine
        for flavor in original_flavors:
            if order == flavor.lower():
                return True
        for flavor in signature_flavors:
            if order == flavor.lower():
                return True 
    return False 

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print("What's your order? (please enter the exact spelling of the\
item you want type \"Exit\" to end your order.)")

    while True:
        inn = input("").lower()
        if inn == "exit":
            break
        elif is_valid_order(inn) :
            order_list.append(inn)
        else:
            print("%s is not a valid order, please order again" %(inn))
            
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return "Total price is eligible for credit card payment"
    else:
        return "Sorry, the order is not eligible for credit card payment."


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for itm in order_list:
        if itm in menu:
            total += menu[itm]
        elif org in original_flavors:
            total += original_price
        else: 
            total += signature_price
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for itm in order_list:
        print("- \"%s\"" %(itm))

    total_price = get_total_price(order_list)
    print("The total will be: SAR %f" %(total_price))
    print(accept_credit_card(total_price))
    print("Thank you at shipping at {}".format(cupcake_shop_name))
