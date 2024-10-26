#input should be location of getting on and off and time, and output should where to stand to get in the train depending on where the capcity is lower

station_on_name = print("Which station are u getting on from:" + str(input()))
station_off_name = print("What is your desired destination:" + str(input()))


if (station_on_name and station_off_name ) in StationList.json:
    #we get the train schedule of all the trains that will be departing from there.
    