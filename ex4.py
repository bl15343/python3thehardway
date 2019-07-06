#There are 100 cars
cars = 100

#Each car can hold 4 people
space_in_a_car = 4.0

#There are 30 drivers
drivers = 30

#There are 90 passengers
passengers = 90

#The number of cars not driven is the number of drivers
#subtracted from the total number of cars
cars_not_driven = cars - drivers

#The number of cars driven is the number of drivers
cars_driven = drivers

#The carpool capacity is the number of cars driven
#multiplied by the number of person spaces in a car
carpool_capacity = cars_driven * space_in_a_car

#The average passengers per car is the number of passengers
#divided by the number of cars driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Study drills 0
#The syntax error was because car_pool_capacity is not defined, the variable
#is carpool_capacity

#Study drills 1
#It is not necessary as you will not be able to transport a fraction
#of a person

