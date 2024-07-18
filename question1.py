# Task 1

def format_itinerary(list_of_tuples):
    itinerary_count = 0
    formatted_string = ""
    for item in list_of_tuples:
        traveler_name, origin, destination = item
        itinerary_count += 1
        formatted_item = f"Itinerary {itinerary_count}: {traveler_name} - From {origin} to {destination}"
        formatted_string += ("\n" + formatted_item)
    return formatted_string

print(format_itinerary([("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]))