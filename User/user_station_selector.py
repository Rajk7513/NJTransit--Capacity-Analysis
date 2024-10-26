#input should be location of getting on and off and time, and output should where to stand to get in the train depending on where the capcity is lower
from datetime import datetime

boarding_station = str(input("Enter your boarding station: "))
destination_station = str(input("Enter your destination station: "))
boarding_time = int(input("Enter your boarding time (HH:MM): "))
