
ifile = "example.txt"

with open(ifile, mode="r") as f:
    arrival_estimate = int(f.readline())
    line2 = f.readline().strip()
    bus_ids = [int(i) for i in line2.split(",") if i.isnumeric()]
    bus_ids_with_offsets = [(index, int(i))
                            for index, i in enumerate(line2.split(","))
                            if i.isnumeric()]

departures = [((arrival_estimate // bus_id + 1) * bus_id, bus_id)
              for bus_id in bus_ids]

earliest_departure = departures[0]
for departure in departures:
    if departure[0] < earliest_departure[0]:
        earliest_departure = departure

departure_time, bus_id = earliest_departure

print(f"part1: {(departure_time - arrival_estimate) * bus_id}")

timestamp = 0
step_size = 1

for offset, bus_id in bus_ids_with_offsets:
    while (timestamp + offset) % bus_id != 0:
        timestamp += step_size
    step_size *= bus_id

print(f"part2: {timestamp}")
