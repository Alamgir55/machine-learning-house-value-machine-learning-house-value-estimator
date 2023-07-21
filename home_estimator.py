def estimate_home_value(size_in_sqft, number_of_bedrooms):
    value = 50000
    
    value = value + (size_in_sqft*92)
    
    value = value + (number_of_bedrooms * 10000)
    
    return value

value = estimate_home_value(3800, 5)

print("Estimated valued: ")
print(value)
    