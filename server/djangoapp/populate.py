from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology",
            "year_founded": 1933},
        {"name": "Mercedes", "description": "Great cars. German technology",
            "year_founded": 1926},
        {"name": "Audi", "description": "Great cars. German technology",
            "year_founded": 1910},
        {"name": "Kia", "description": "Great cars. Korean technology",
            "year_founded": 1944},
        {"name": "Toyota", "description": "Great cars. Japanese technology",
            "year_founded": 1937},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'], description=data['description'],
            year_founded=data['year_founded']))

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "Qashqai", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "XTRAIL", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "A-Class", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 2},
        {"name": "C-Class", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 2},
        {"name": "E-Class", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1], "dealer_id": 2},
        {"name": "A4", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 3},
        {"name": "A5", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 3},
        {"name": "A6", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2], "dealer_id": 3},
        {"name": "Sorrento", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[3], "dealer_id": 4},
        {"name": "Carnival", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[3], "dealer_id": 4},
        {"name": "Cerato", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[3], "dealer_id": 4},
        {"name": "Corolla", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 5},
        {"name": "Camry", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 5},
        {"name": "Kluger", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[4], "dealer_id": 5},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            dealer_id=data['dealer_id']  # Add the dealer_id here
        )
