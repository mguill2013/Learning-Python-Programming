def calculate_gift_tax():
    """
    Calculates the Finnish gift tax based on the provided tax table.
    Assumes gifts are from a close relative/family member.
    """
    try:
        gift_value = int(input("Value of gift:"))
        
        tax_amount = 0.0
        
        if gift_value < 5000: 
            print("No tax!")
            return
        
        elif 5000 <= gift_value <= 25000:
            tax_amount = 100 + (gift_value - 5000) * 0.08
        
        elif 25000 < gift_value <= 55000:
            tax_amount = 1700 + (gift_value - 25000) * 0.10
        
        elif 55000 < gift_value <= 200000:
            tax_amount = 4700 + (gift_value - 55000) * 0.12
        
        elif 200000 < gift_value <= 1000000:
            tax_amount = 22100 + (gift_value - 200000) * 0.15
        
        elif gift_value > 1000000:
            tax_amount = 142100 + (gift_value - 1000000) * 0.17
        
        print(f"Amount of tax: {tax_amount:.2f} euros")
    
    except ValueError:
        print("Invalid input. Please enter a whole number for the gift value.")
    except Exception as e:
        print(f"An unexpected error ocurred: {e}")
    
if __name__ == "__main__":
    calculate_gift_tax()