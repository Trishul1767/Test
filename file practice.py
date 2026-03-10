with open('to_do','w') as f:
    f.write("Car\nBike")
with open('to_do','r') as f:
    print(f.read())