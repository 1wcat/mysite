class Car:
    def __init__(self, name, w, cap, mileage, price):
        self.name = name
        self.w = w
        self.cap = cap
        self.mileage = mileage
        self.price = price
    def info(self):
        fmt = '{:10}{:10}{:10}{:10}{:10}'
        return fmt.format(self.name, self.w, self.cap, self.mileage, self.price)

def print_cars(cars):
    for car in cars:
        print(car.info())

def selectWeightLessEqual(cars, w):
    chosen = []
    for car in cars:
        if car.w <= w:
            chosen.append(car)
    return chosen

def select_price_range(cars, low, high):
    chosen = []
    for car in cars:
        if car.price >= low and car.price <= high:
            chosen.append(car)
    return chosen

def read_cars():
    fmt = '{:10}{:10}{:10}{:10}{:10}'
    with open('car.txt') as f1:
        line = f1.readline()
        line = line.strip()
        ts = line.split()
        print(fmt.format(ts[0], ts[1], ts[2], ts[3], ts[4]))
        cars = []
        for line in f1:
            line = line.strip()
            ts = line.split()
            car = Car(ts[0], float(ts[1]), float(ts[2]), float(ts[3]), float(ts[4]))
            cars.append(car)
        
        print('select weight less equal:')
        chosen_cars = selectWeightLessEqual(cars, 500)
        print_cars(chosen_cars)

        print('select price in range:')
        chosen_cars = select_price_range(cars, 200000, 300000)
        print_cars(chosen_cars)

        print('select by two conditions')
        chosen1 = selectWeightLessEqual(cars, 500)
        chosen2 = select_price_range(chosen1, 200000, 300000)
        print_cars(chosen2) 
read_cars()