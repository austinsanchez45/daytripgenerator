import random
destination_options = ["Orlando", "Miami", "Los Angeles", "Boston", "San Diego", "Seattle"]
restaurant_options = ["Texas Roadhouse", "Olive Garden", "Cheesecake Factory", "Cracker Barrel", "Red Lobster", "McDonalds", "Chik-fil-a", "Popeyes", "Wendy's", "Subway"]
mode_of_transportation = ["Airplane", "Train", "Bus", "Your own vehicle", "RV"]
form_of_entertainment = ["iPhone", "Books,", "Board Games", "Electronics", "Movies"]


def ask_for_destination(destination_list):
    print()
    random_destination = random.choice(destination_list)
    print("Your randomly selected destination is: " , random_destination)
    print()
    destination_confirming = input("Do you like this destination? ")
    while destination_confirming == "no":
        if destination_confirming == "no":
            destination_list.remove(random_destination)
            random_destination = random.choice(destination_list)
            print()
            print("Your new destination is ", random_destination)
            print()
            destination_confirming = input("Do you like this new destination? ")
    destination_confirmed = random_destination
    return(destination_confirmed)



def ask_for_restaurant(restaurant_list):
    print()
    random_restaurant = random.choice(restaurant_list)
    print("Your randomly selected restaurant is: " , random_restaurant)
    print()
    restaurant_confirming = input("Do you like this restaurant? ")
    while restaurant_confirming == "no":
        if restaurant_confirming == "no":
            restaurant_list.remove(random_restaurant)
            random_restaurant = random.choice(restaurant_list)
            print()
            print("Your new restaurant is ", random_restaurant)
            print()
            restaurant_confirming = input("Do you like this new restaurant? ")
    restaurant_confirmed = random_restaurant
    return(restaurant_confirmed)
    

def ask_for_transportation(transportation_list):
    print()
    random_transportation = random.choice(transportation_list)
    print("Your randomly selected mode of transportation is: " , random_transportation)
    print()
    transportation_confirming = input("Do you like this mode of transportation? ")
    while transportation_confirming == "no":
        if transportation_confirming == "no":
            transportation_list.remove(random_transportation)
            random_transportation = random.choice(transportation_list)
            print()
            print("Your new mode of transportation is ", random_transportation)
            print()
            transportation_confirming = input("Do you like this new mode of transportation? ")
    transportation_confirmed = random_transportation
    return(transportation_confirmed)


def ask_for_entertainment(entertainment_list):
    print()
    random_entertainment = random.choice(entertainment_list)
    print("Your randomly selected form of entertainment is: " , random_entertainment)
    print()
    entertainment_confirming = input("Do you like this form of entertainment? ")
    while entertainment_confirming == "no":
        if entertainment_confirming == "no":
            entertainment_list.remove(random_entertainment)
            random_entertainment = random.choice(entertainment_list)
            print()
            print("Your new form of entertainment is ", random_entertainment)
            print()
            entertainment_confirming = input("Do you like this new form of entertainment? ")
    entertainment_confirmed = random_entertainment
    return(entertainment_confirmed)


def trip_confirmation(destination, restaurant, transportation, entertainment):
    print()
    confirm_trip = input("Are you happy with the random selections? ")
    if confirm_trip == "yes":
        print()
        print(f"You will be arriving at",destination,"via",transportation,". You will be eating at",restaurant,"and you will keep yourself occupied with your",entertainment,".") 
        

destination_choice = ask_for_destination(destination_options)
restaurant_choice = ask_for_restaurant(restaurant_options)
transportation_choice = ask_for_transportation(mode_of_transportation)
entertainment_choice = ask_for_entertainment(form_of_entertainment)
trip_confirmation(destination_choice, restaurant_choice, transportation_choice, entertainment_choice)