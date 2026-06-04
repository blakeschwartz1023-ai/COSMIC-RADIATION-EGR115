""" Project 1"""

print("\n T64 Engine Power Performance")
print("------------------------")

missions = [] 
# LIST OF MARGINS STORED IN AN EMPTY LIST 

for flight in range(1, 3): 
    # RANGE OF FLIGHTS WE WILL EVALUATE (2) 
    print(f"\nFlight {flight}") 
    #PRINTING FLIGHT NUMBER AND A NEW LINE AFTER 

    while True:

        oat = float(input("Enter the Outside Air Temperature (C): ")) 
        # INPUT OF OAT IN C 
        alt = float(input("Enter the Pressure Altitude (ft): "))
         # INPUT OF ALT IN FT
        torque = float(input("Enter the required Torque (%): ")) 
        # INPUT OF TORQUE PERCENT
    
        if oat < -40 or oat > 50:
            print("Temperature must be between -40C and 50C")
        elif alt < 0 or alt > 40000:
            print("Altitude must be between 0 and 40000 ft")
        elif torque < 0 or torque > 100:
            print("Torque must be between 0 percent and 100 percent ")
        else:
            break
        
    power_available = 100 
    # 100% POWER AVAILABLE AT START 
    standard_temp = 15 - (2 * alt / 1000) 
    # calculate standard temp at your alt 
    density_altitude = alt + (120 * (oat - standard_temp)) 
    # calc density alt
    power_available = 100 - (density_altitude / 1000 * 3) 
    # estimate of engine power 

    if power_available > 100:
        power_available = 100 # cant have more than 100% power

    margin = power_available - torque # final margine clac

    missions.append(margin) 
    # ADDING MARGINS OF FLIGHTS TO OUR MISSION LIST FROM ABOVE 


    
print(" \nSTATUS REPORT ")
print("------------------------")

flight = 1

for margin in missions: 
    # for loop to group flights with corresponding margines and status

    print(f"\nFlight {flight}")

    print(f"Power Margin: {margin:.2f}%")

    flight += 1
    
    if margin >= 15:
        print("Status: Running well within Limits") 
        # PRINTS THIS IF MARGIN IS GREATER THAN OR EQUAL TO 15% OR RUNNING AT PORPER POWER LEVEL 
    elif margin >= 0:
        print("Status: Caution low power") 
        # PRINTS THIS IS MARGIN IS CAUSING LOW POWER 
    else:
        print("Status: WARNING insufficient power available") 
        # PRINTS THIS IF ENGINE IS NO LONGER PRODUCING POWER 
