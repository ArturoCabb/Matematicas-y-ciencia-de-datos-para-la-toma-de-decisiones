import pandas as pd

print('Ejercicio 1')
df = pd.read_csv("Automobile_data.csv")
print(df.head(5)) # Ejercicio 1
print(df.tail(5)) # Ejercicio 1

print('Ejercicio 2')
df = pd.read_csv("Automobile_data.csv", na_values={ # Ejercicio 2
    'price':["?","n.a"],                            # Ejercicio 2
    'stroke':["?","n.a"],                           # Ejercicio 2
    'horsepower':["?","n.a"],                       # Ejercicio 2
    'peak-rpm':["?","n.a"],                         # Ejercicio 2
    'average-mileage':["?","n.a"]})                 # Ejercicio 2
print (df)                                          # Ejercicio 2
df.to_csv("Automobile_data.csv")                    # Ejercicio 2

print('Ejercicio 3')
df = pd.read_csv("Automobile_data.csv")                    # Ejercicio 3
df = df [['company','price']][df.price==df['price'].max()] # Ejercicio 3
print(df)                                                  # Ejercicio 3

print('Ejercicio 4')
df = pd.read_csv("Automobile_data.csv")          # Ejercicio 4
car_Manufacturers = df.groupby('company')        # Ejercicio 4
toyotaDf = car_Manufacturers.get_group('toyota') # Ejercicio 4
print(toyotaDf)                                  # Ejercicio 4

print('Ejercicio 5')
df = pd.read_csv("Automobile_data.csv") # Ejercicio 5
print(df['company'].value_counts())     # Ejercicio 5

#print('Ejercicio 6')
#df = pd.read_csv("Automobile_data.csv")              # Ejercicio 6
#car_Manufacturers = df.groupby('company')            # Ejercicio 6
#priceDf = car_Manufacturers['company','price'].max() # Ejercicio 6
#print(priceDf)                                       # Ejercicio 6

#print('Ejercicio 7')
#df = pd.read_csv("Automobile_data.csv")                           # Ejercicio 7
#car_Manufacturers = df.groupby('company')                         # Ejercicio 7
#mileageDf = car_Manufacturers['company','average-mileage'].mean() # Ejercicio 7
#print(mileageDf)                                               # Ejercicio 7

print('Ejercicio 8')
carsDf = pd.read_csv("Automobile_data.csv")                              # Ejercicio 8
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False) # Ejercicio 8
print(carsDf.head(5))                                                    # Ejercicio 8

print('Ejercicio 9')
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}          # Ejercicio 9
carsDf1 = pd.DataFrame.from_dict(GermanCars)                                                                     # Ejercicio 9
                                                                                                                 # Ejercicio 9
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]} # Ejercicio 9
carsDf2 = pd.DataFrame.from_dict(japaneseCars)                                                                   # Ejercicio 9
                                                                                                                 # Ejercicio 9
carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])                                                # Ejercicio 9
print(carsDf)                                                                                                    # Ejercicio 9

print('Ejercicio 10')
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]} # Ejercicio 10
carPriceDf = pd.DataFrame.from_dict(Car_Price)                                                       # Ejercicio 10
                                                                                                     # Ejercicio 10
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]} # Ejercicio 10
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)                                            # Ejercicio 10
                                                                                                     # Ejercicio 10
carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")                                        # Ejercicio 10
print(carsDf)                                                                                        # Ejercicio 10
