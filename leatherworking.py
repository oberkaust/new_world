def calculate_comprehensive_profit_with_materials():
    # Prices input
    rawhide_price = float(input("Enter the price of Rawhide: "))
    thick_hide_price = float(input("Enter the price of Thick Hide: "))
    iron_hide_price = float(input("Enter the price of Iron Hide: "))
    aged_tannin_price = float(input("Enter the price of Aged Tannin: "))

    course_leather_price = float(input("Enter the price of Course Leather: "))
    rugged_leather_price = float(input("Enter the price of Rugged Leather: "))
    layered_leather_price = float(input("Enter the price of Layered Leather: "))
    infused_leather_price = float(input("Enter the price of Infused Leather: "))

    # Calculating the cost of producing each type of leather
    # From raw materials
    cost_course_leather_from_raw = 4 * rawhide_price
    cost_rugged_leather_from_raw = 4 * cost_course_leather_from_raw + aged_tannin_price
    cost_layered_leather_from_raw = 6 * thick_hide_price + 2 * cost_rugged_leather_from_raw + aged_tannin_price
    cost_infused_leather_from_raw = 8 * iron_hide_price + 2 * cost_layered_leather_from_raw + aged_tannin_price

    # By buying lower-tier leather
    cost_rugged_leather_from_course = 4 * course_leather_price + aged_tannin_price
    cost_layered_leather_from_rugged = 6 * thick_hide_price + 2 * rugged_leather_price + aged_tannin_price
    cost_infused_leather_from_layered = 8 * iron_hide_price + 2 * layered_leather_price + aged_tannin_price

    # Determining the most profitable method for each leather type and required materials
    profitable_conversions = {}
    if course_leather_price > cost_course_leather_from_raw:
        profitable_conversions["Course Leather"] = (course_leather_price - cost_course_leather_from_raw, "4 Rawhide")
    if rugged_leather_price > cost_rugged_leather_from_raw and cost_rugged_leather_from_raw < cost_rugged_leather_from_course:
        profitable_conversions["Rugged Leather from Raw"] = (rugged_leather_price - cost_rugged_leather_from_raw, "4 Course Leather, 1 Aged Tannin")
    elif rugged_leather_price > cost_rugged_leather_from_course:
        profitable_conversions["Rugged Leather from Course Leather"] = (rugged_leather_price - cost_rugged_leather_from_course, "4 Course Leather, 1 Aged Tannin")
    if layered_leather_price > cost_layered_leather_from_raw and cost_layered_leather_from_raw < cost_layered_leather_from_rugged:
        profitable_conversions["Layered Leather from Raw"] = (layered_leather_price - cost_layered_leather_from_raw, "6 Thick Hide, 2 Rugged Leather, 1 Aged Tannin")
    elif layered_leather_price > cost_layered_leather_from_rugged:
        profitable_conversions["Layered Leather from Rugged Leather"] = (layered_leather_price - cost_layered_leather_from_rugged, "6 Thick Hide, 2 Rugged Leather, 1 Aged Tannin")
    if infused_leather_price > cost_infused_leather_from_raw and cost_infused_leather_from_raw < cost_infused_leather_from_layered:
        profitable_conversions["Infused Leather from Raw"] = (infused_leather_price - cost_infused_leather_from_raw, "8 Iron Hide, 2 Layered Leather, 1 Aged Tannin")
    elif infused_leather_price > cost_infused_leather_from_layered:
        profitable_conversions["Infused Leather from Layered Leather"] = (infused_leather_price - cost_infused_leather_from_layered, "8 Iron Hide, 2 Layered Leather, 1 Aged Tannin")

    # Displaying profitable scenarios and required materials
    if profitable_conversions:
        print("Profitable scenarios for crafting:")
        for leather, (profit, materials) in profitable_conversions.items():
            print(f"{leather} can be produced for a profit of {profit} per unit. Required materials: {materials}")
    else:
        print("No profitable scenarios with current prices.")

# Run the function
calculate_comprehensive_profit_with_materials()
