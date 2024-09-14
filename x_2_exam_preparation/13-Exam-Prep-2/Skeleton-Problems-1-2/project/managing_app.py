from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar

class ManagingApp:
    VALID_VEHICLE_TYPES = {'PassengerCar':PassengerCar,'CargoVan':CargoVan}
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self,first_name: str, last_name: str, driving_license_number: str):
        user = User(first_name,last_name,driving_license_number)
        match_lisense = next((u for u in self.users if u.driving_license_number == user.driving_license_number),None)
        if match_lisense:
            return f"{driving_license_number} has already been registered to our platform."
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self,vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPES.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."
        match_lisense = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        if match_lisense:
            return f"{license_plate_number} belongs to another vehicle."
        vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand,model,license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self,start_point: str, end_point: str, length: float):
        match_route = next((r for r in self.routes if r.start_point == start_point and r.end_point == end_point),None)
        if match_route:
            if match_route.length<length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if match_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        route = Route(start_point,end_point,length,len(self.routes)+1)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self,driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        route = next((r for r in self.routes if r.route_id == route_id), None)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

            return vehicle.__str__()



    def repair_vehicles(self,count: int):
        #Make it right
        dameget_veicles = [v for v in self.vehicles if v.is_damaged]
        dameget_veicles = sorted(dameget_veicles,key=lambda v:(v.brand,v.model))

        if len(dameget_veicles) > count:
            dameget_veicles = dameget_veicles[:count]
        for v in dameget_veicles:
            v.is_damaged = False
            v.recharge()
        return f"{len(dameget_veicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ''
        ordered_users = sorted(self.users,key=lambda u: -u.rating)
        users_result = '\n'.join([str(u) for u in ordered_users])
        return result




