from App.rocket import Rocket
from Database import database
import sqlite3


rocket_chars = []
rocket_calcs = []


# introduces program to user
def intro():
    print("Hi and welcome to the rocket simulator!"
          "\nHere we can calculate a variety of rocket-related features including:")

    info()

    print("At any time, type info to repeat the information, intro to see the introduction,"
          "\nor quit to end the operation")


def info():
    options = ("Initial (wet) Mass", "Exhaust Velocity", "Area", "Lift-Off Weight",
               "Resultant Force", "Acceleration", "Burnout Velocity (ft. Stages 1 & 2)",
               "Burnout Height (ft. Stages 1 & 2)")
    for o in options:
        print(o)

    print("Type any of the above options to access information about the rocket.")


# gathers rocket info from user via console input
def rocket_attributes():
    print("To access any of the rocket-specific equations, we'll need some information from you first.")
    name = input("What's the name of the rocket?: ")
    thrust = float(input("What's the rocket's thrust (in kgs)?: "))
    fuel_burn = float(input("Rocket fuel burn rate?: "))
    spec_impulse = int(input("Total specific impulse?: "))
    stage1_burn_t = int(input("First stage burn time?: "))
    stage2_burn_t = int(input("Second stage burn time?: "))
    stage1_struct_mass = float(input("First stage dry mass?: "))
    stage2_struct_mass = float(input("Second stage dry mass?: "))
    rocket_diameter = float(input("Diameter?: "))
    length = float(input("Length?: "))
    print("One last question...we promise!")
    fuel_mass = float(input("Finally, what's the total fuel mass?: "))

    # deposits rocket info into dictionary
    rocket_info = {"name": name, "thrust": thrust, "fuel_burn": fuel_burn,
                   "spec_impulse": spec_impulse, "stage1_burn_t": stage1_burn_t,
                   "stage2_burn_t": stage2_burn_t, "stage1_struct_mass": stage1_struct_mass,
                   "stage2_struct_mass": stage2_struct_mass, "diameter": rocket_diameter,
                   "length": length, "fuel_mass": fuel_mass}

    return rocket_info


# executes all rocket calculation choices
def rocket_choices(choice, rocket_model):
    if "initial mass" in choice.lower() or 'wet mass' in choice.lower():
        print(f"The {rocket_model.rocket_name()}'s initial mass (wet mass) is: {rocket_model.initial_mass()}")

    elif "exhaust" in choice.lower():
        print(f"The {rocket_model.rocket_name()}'s exhaust velocity is: {rocket_model.exhaust_velocity()}")

    elif "area" in choice.lower():
        print(f"The {rocket_model.rocket_name()}'s area is: {rocket_model.rocket_area()}")

    elif "lift-off" in choice.lower():
        print(f"The {rocket_model.rocket_name()}'s lift-off weight is: {rocket_model.lift_off_weight()}")

    elif "resultant" in choice.lower():
        print(f"The {rocket_model.rocket_name()}'s resultant force is: {rocket_model.resultant_force()}")

    elif "acceleration" in choice.lower():
        print(f"The {rocket_model.rocket_name()}'s acceleration is: {rocket_model.acceleration()}")

    elif "burnout velocity" in choice.lower():
        stage = input("Which stage do you want the burnout velocity for (1/2 or both)?: ")

        if stage == "both":
            print(
                f"The {rocket_model.rocket_name()}'s first stage burnout velocity is: {rocket_model.burn_velocity(1)}")
            print(
                f"The {rocket_model.rocket_name()}'s second stage burnout velocity is: {rocket_model.burn_velocity(2)}")
        # elif statement uses string checks instead of int due to type conversion (between both and/or 1, 2)
        elif "1" in stage or "2" in stage:
            print(f"Stage {stage} rocket burnout velocity is: {rocket_model.burn_velocity(stage)}")
        else:
            print("Sorry, wrong input (must be 1, 2, or both)")

    elif "burnout height" in choice.lower():
        stage = input("Which stage do you want the burnout height for (1/2 or both)?: ")

        if "both" in stage.lower():
            print(f"The {rocket_model.rocket_name()}'s first stage burnout height is: {rocket_model.burn_height(1)}")
            print(f"The {rocket_model.rocket_name()}'s second stage burnout height is: {rocket_model.burn_height(2)}")
        elif "1" in stage or "2" in stage:
            print(f"Stage {stage} rocket burnout velocity is: {rocket_model.burn_height(stage)}")
        else:
            print("Sorry, wrong input (must be 1, 2, or both)")

    elif 'q' not in choice.lower() and choice.lower() != "info" and choice.lower() != "intro":
        print("Sorry that is not a choice, try again")


def main():
    # initializes game count
    global game_count
    game_count = 0

    # bulk of game logic
    intro()
    while True:
        if game_count < 1:
            user_input = input("Do you want to continue (Y/N)?: ")
        else:
            user_input = input("Do you want to use another rocket (Y/N)?: ")

        # breaks loop
        if 'n' in user_input.lower():
            print("Okay, bye!")
            break

        # retrieves data from user
        rocket_attrs = rocket_attributes()

        # creates new rocket object
        user_rocket = Rocket(rocket_attrs["thrust"], rocket_attrs["fuel_burn"], rocket_attrs["name"],
                                 rocket_attrs["spec_impulse"], rocket_attrs["stage1_burn_t"],
                                 rocket_attrs["stage2_burn_t"], rocket_attrs["stage1_struct_mass"],
                                 rocket_attrs["stage2_struct_mass"], rocket_attrs["diameter"],
                                 rocket_attrs["length"], rocket_attrs["fuel_mass"])

        storage_option = input("Would you like to store your rocket's information (Y/N)?: ")
        if 'y' in storage_option.lower():
            storage_option = "yes"
            # creates new tuple for rocket data
            rocket_data = (rocket_attrs["thrust"], rocket_attrs["fuel_burn"], rocket_attrs["name"],
                           rocket_attrs["spec_impulse"], rocket_attrs["stage1_burn_t"],
                           rocket_attrs["stage2_burn_t"], rocket_attrs["stage1_struct_mass"],
                           rocket_attrs["stage2_struct_mass"], rocket_attrs["diameter"],
                           rocket_attrs["length"], rocket_attrs["fuel_mass"])

            # appends rocket info into list for database input
            rocket_chars.append(rocket_data)

        # monitors exit intent
        while 'q' not in user_input.lower():
            user_input = input("What's next?: ")
            rocket_choices(user_input, user_rocket)

            if "info" in user_input.lower():
                info()

            elif "intro" in user_input.lower():
                intro()

        if storage_option == "yes":
            # stores rocket calculations in a tuple
            store_rocket_calcs = (user_rocket.rocket_name(), user_rocket.initial_mass(),
                                  user_rocket.exhaust_velocity(), user_rocket.rocket_area(),
                                  user_rocket.lift_off_weight(), user_rocket.resultant_force(),
                                  user_rocket.acceleration(), user_rocket.burn_velocity(1),
                                  user_rocket.burn_velocity(2), user_rocket.burn_height(1),
                                  user_rocket.burn_height(2))
            # deposits a tuple into a list
            rocket_calcs.append(store_rocket_calcs)

        game_count += 1

    # database entries and commitments
    conn = sqlite3.connect("rocket_data.db")
    c = conn.cursor()

    c.executemany("INSERT INTO rocket_values VALUES (?,?,?,?,?,?,?,?,?,?,?)", rocket_chars)
    c.executemany("INSERT INTO rocket_calculations VALUES (?,?,?,?,?,?,?,?,?,?,?)", rocket_calcs)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
