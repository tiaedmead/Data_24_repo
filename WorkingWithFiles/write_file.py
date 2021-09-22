with open("order.txt", "w") as file:

    order_items = ["wings", "pizza", "juice"]

    for item in order_items:
        file.write(item)