try:
    Total_value = float(input("Enter total value:"))
    Value = float(input("Enter value:"))

    if Total_value == 0:
        exit("Mathematical error")
    percentage = 100 * (Value/Total_value)

    print(f"percentage:{percentage}%")

except ValueError:
    print("Kindly enter a number")