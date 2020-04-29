def make_car(model, producer, **car_info):
    car = {}
    car['model'] = model
    car['producer'] = producer
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
