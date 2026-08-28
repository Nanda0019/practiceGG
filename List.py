Indian =["Samosa", "Biriyani", "Sambar"]
Italian =["Pizza", "Pasta", "Fries"]
Chinese =["Noodles", "Soup", "Ramen"]

dish = input ("Enter your dish: ")

if dish in Indian :
    print(f"{dish} is indian ")
elif dish in Chinese:
     print(f"{dish} is Chinese ")
elif dish in Italian:
     print(f"{dish} is Italian ")  
else:
     print("I don't know")        