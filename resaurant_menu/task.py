# Task 1 restaurant menu
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add key bev and two vals ex: water and sweat tea
restaurant_menu["Bevarages"] = "Water", "Sweet Tea"

print()
print(restaurant_menu)

# Update key steak to 17.99
restaurant_menu.update({"Steak": 17.99})

print()
print(restaurant_menu)

# Remove item bruschetta from menu
restaurant_menu["Starters"].pop("Bruschetta")

print()
print(restaurant_menu)