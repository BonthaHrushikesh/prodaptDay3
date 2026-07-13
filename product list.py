products=["Laptop","Mouse","Keyboard"]

#adding monitor
products.append("Monitor")
print("after adding :", products)

#new products added from another list
new_products=["Tablets","Webcam"]
products.extend(new_products)
print("new products added:" ,products)

#remove mouse
products.remove("mouse")

#count laptop
products.count("Laptop")
print("count of laptops :" , products)




