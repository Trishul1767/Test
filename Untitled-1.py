A=['Virtus', 'Santa Cruze', 'Specialized', 'Trek', 'porsche', 'AstonMartin Vantage', 'Ferrari Laferrari', 'McLaren P1', 'McLaren720s', 'Ducati Panigale V4']
with open('My_Garage', 'w') as f:
    for i in A:
        f.write(f"I will own a {i} one day\n")