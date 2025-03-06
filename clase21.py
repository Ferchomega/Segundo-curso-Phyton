collections = ("nescafe", "houseblen", "raro")
Coffee = collections.NamedTuple("Coffe",("size", "bean", "price"))
def get_coffee(coffee_type):
    if coffee_type == "houseblend":
        return Coffee ("large", "premium", "10")