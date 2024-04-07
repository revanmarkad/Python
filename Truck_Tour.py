    # """
    # Finds the index of the petrol pump where a truck can start its tour
    # such that it can complete the entire circuit without running out of petrol.

    # Args:
    # - petrolpumps: A list of tuples representing petrol pumps, where each tuple
    #   contains two integers: (petrol, distance), where petrol is the amount of
    #   petrol available at the pump and distance is the distance to the next pump.

    # Returns:
    # - start_index: The index of the petrol pump where the truck can start its tour.
    #   If no such petrol pump exists, returns -1.
    # """
    
def truckTour(petrolpumps):
    total_petrol = 0
    total_distance = 0
    start_index = 0

    # Iterate through the petrol pumps
    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]

        # Calculate total petrol and total distance
        total_petrol += petrol
        total_distance += distance

        # If the total petrol is less than the total distance, update start index
        if total_petrol < total_distance:
            total_petrol = 0
            total_distance = 0
            start_index = i + 1

    return start_index


print(truckTour([(4, 6), (6, 5), (7, 3), (4, 5)]))

