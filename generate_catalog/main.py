def generate_catalog(item1, price1, item2, price2, item3, price3):
    
    print("Output:")
    print("Online Store")
    print("-" * 38)
    print("Product(S)" + " " * 33 + "Price")
    print(f"{item1:<45}{price1:.1f}")
    print(f"{item2:<45}{price2:.1f}")
    print(f"{item3:<45}{price3:.1f}")
    
    
    combo1 = price1 + price2
    combo2 = price1 + price3
    combo3 = price2 + price3
    print(f"Combo 1: {item1} + {item2:<27}{combo1 * 0.9:.1f}")
    print(f"Combo 2: {item1} + {item3:<27}{combo2 * 0.9:.1f}")
    print(f"Combo 3: {item2} + {item3:<28}{combo3 * 0.9:.1f}")

    
    
    gift_pack = price1 + price2 + price3
    print(f"Gift Pack: {item1} + {item2} + {item3:<17}{gift_pack * 0.75:.1f}")
    print("_" * 38)
    print("For delivery Contact: 98764678899")

generate_catalog("Orange", 1.0, "Apple", 1.0, "Strawberry", 0.3)
