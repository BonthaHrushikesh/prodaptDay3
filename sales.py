inventory={}
n=int(input("no.of.products:"))

for i in range(n):
    category=input("no.of categories :")
    product=input("no.of products :")

    quantity=int(input("enter quantity :"))

    if category not in inventory:
        inventory[category]={}
        inventory[category][product]=quantity

    print("\n inventory details")
    for category in inventory:
        print("\ncategory:",category)
        for product in inventory[category]:
            print(product,"-",inventory[category][product])