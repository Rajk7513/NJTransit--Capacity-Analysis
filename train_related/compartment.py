import user_station_selector.py from user
def get_suggested_compartment(boarding_station, destination_station, time):
    # Find the appropriate train for the given boarding time and stations
    for train, schedule in station_schedule.items():
        stations = [s["station"] for s in schedule]
        if boarding_station in stations and destination_station in stations:
            # Get the time details for the boarding station
            station_info = next((s for s in schedule if s["station"] == boarding_station), None)
            if station_info and time_in_range(time, station_info["arrival"], station_info["departure"]):
                # Suggest the compartment with the lowest capacity
                compartments = train_stop_list[train]["compartments"]
                best_compartment = min(compartments, key=lambda x: x["capacity"])
                return f"Board Train {train} at {boarding_station}. Stand near Compartment {best_compartment['compartment']} (Capacity: {best_compartment['capacity']})."
    return "No suitable train found for the given time and stations."
