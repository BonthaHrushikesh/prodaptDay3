# Initial inventory
products = ["Laptop", "Mouse", "Keyboard"]

# 1. Insert urgent product
products.append("Monitor")
print("After adding Monitor:", products)

# 2. Combine products from another warehouse
new_products = ["Tablet", "Webcam"]
products.extend(new_products)
print("After combining:", products)

# 3. Remove discontinued product (Mouse)
products.remove("Mouse")
print("After removing Mouse:", products)

# 4. Process shipped product (last product)
shipped = products.pop()
print("Shipped product:", shipped)
print("Inventory:", products)

# 5. Count occurrences of Laptop
print("Laptop count:", products.count("Laptop"))

# 6. Find position of Monitor
print("Monitor index:", products.index("Monitor"))

# 7. Sort products
products.sort()
print("Sorted inventory:", products)

# 8. Reverse display order
products.reverse()
print("Reversed inventory:", products)

# 9. Create a backup copy
backup_inventory = products.copy()
print("Backup:", backup_inventory)

# 10. Clear temporary inventory
temp_inventory = products.copy()
temp_inventory.clear()
print("Temporary inventory after clear:", temp_inventory)