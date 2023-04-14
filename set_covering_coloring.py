states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"]) 
stations["kthree"] = set(["or", "nv", "ca"]) 
stations["kfour"] = set(["nv", "ut"]) 
stations["kfive"] = set(["ca", "az"])


def set_covering_coloring(stations, states_needed):

    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            # AND between sets
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        final_stations.add(best_station)
        states_needed -= states_covered

    print (final_stations)

set_covering_coloring(stations, states_needed)