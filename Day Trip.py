import random
def lists():
    destination_options = ["Orlando", "Miami", "Los Angeles", "Boston", "San Diego", "Seattle"]
    restaurant_options = ["Texas Roadhouse", "Olive Garden", "Cheesecake Factory", "Cracker Barrel", "Red Lobster", "McDonalds", "Chik-fil-a", "Popeyes", "Wendy's", "Subway"]
    mode_of_transportation = ["Airplane", "Train", "Bus", "Your own vehicle", "RV"]
    form_of_entertainment = ["iPhone", "Books", "Board Games", "Electronics", "Movies"]
    return (destination_options, restaurant_options, mode_of_transportation, form_of_entertainment)


def ask_for_options(first_list, second_list, third_list, fourth_list):
    print()
    options_confirmed = []
    random_options = [first_list, second_list, third_list, fourth_list]
    i = 0
    for i in range (i, len(random_options), 1):
        print()
        list = random_options[i]
        random_selection = random.choice(list)
        print("Your randomly selected option is ", random_selection)
        print()
        confirming = input("Do you like this option(yes or no)? ")
        while confirming == "no":
            if confirming == "no":
                    list.remove(random_selection)
                    random_selection = random.choice(list)
                    print()
                    print("Your new option is ", random_selection)
                    print()
                    confirming = input("Do you like this new option? ")
        options_confirmed.append(random_selection)
    return(options_confirmed)
    

def trip_confirmation(finalization):
    print()
    confirm_trip = input("Are you happy with the random selections? ")
    if confirm_trip == "yes":
        print()
        print(f"For your trip, you will be traveling to {finalization[0]} via {finalization[2]}. You will be eating at {finalization[1]} and you will keep yourself occupied with your {finalization[3]}.")
    
a, b, c, d, = lists()
final_options = ask_for_options(a, b, c, d)     
trip_confirmation(final_options)