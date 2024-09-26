import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    sandwich_size = "medium"
    order_ingredients = recipes[sandwich_size]["ingredients"]
    cost = recipes[sandwich_size]["cost"]

    if sandwich_maker_instance.check_resources(order_ingredients):
        payment = cashier_instance.process_coins()
        if cashier_instance.transaction_result(payment, cost):
            sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients)
            print("Enjoy your sandwich!")
        else:
            print("Sorry, that's not enough money.")
    else:
        print("Sorry, we don't have enough ingredients.")

if __name__=="__main__":
    main()
