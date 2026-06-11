""" Project 2 Christopher Schwartz """

import matplotlib.pyplot as plt

def get_altitude():

    while True:
        altitude = int(input("Enter cruise altitude in feet from 0 - 42,000 ft: "))
        if altitude < 0:
            print("Altitude cannot be negative. Please try again.")
        elif altitude > 42000:
            print("Altitude must be 42,000 ft or less. Please try again.")
        else:
            return altitude

def get_hours():
    while True:
        hours = float(input("Enter time spent at cruise altitude in hours: "))
        if hours <= 0:
            print("Time must be greater than 0 hours. Please try again.")
        else:
            return hours

def calculate_radiation(altitude, hours):
    if altitude <= 30000:
        dose_rate = 2.5
        altitude_risk = "LOW ALTITUDE EXPOSURE"
    elif altitude <= 35000:
        dose_rate = 3.9
        altitude_risk = "MODERATE ALTITUDE EXPOSURE"   
    elif altitude <= 40000:
        dose_rate = 4.8
        altitude_risk = "HIGH ALTITUDE EXPOSURE"
    else:
        altitude <=42000
        dose_rate = 6.6
        altitude_risk = "VERY HIGH ALTITUDE EXPOSURE"

    dose = dose_rate * hours
    percent_limit = (dose / 20000) * 100
    return dose_rate, altitude_risk, dose, percent_limit

print("Aircraft Cosmic Radiation Risk Analyzer")
print("---------------------------------------")

altitude = get_altitude()
hours = get_hours()
dose_rate, altitude_risk, dose, percent_limit = calculate_radiation(altitude, hours)

print("\nRadiation Risk Report")
print("---------------------")
print(f"Cruise Altitude: {altitude:,} ft")
print(f"Time at Cruise Altitude: {hours:.1f} hr")
print(f"Dose Rate: {dose_rate:.1f} µSv/hr")
print(f"Estimated Radiation Dose: {dose:.2f} µSv")
print(f"Radiation Risk: {altitude_risk}")
print(f"Percent of Annual 20 mSv Limit Used: {percent_limit:.2f}%")
if altitude <= 30000:
    print("Note: Radiation dose rate is 2.5 µSv/hr or less below 30,000 ft.")
elif altitude >= 42000:
    print("Note: Radiation above 42000 ft is 6.6 or more as altitude increases. ")

altitudes = [30000, 35000, 40000, 42000]
dose_rates = [2.5, 3.9, 4.8, 6.6]

plt.figure(figsize=(10,5))
plt.plot(altitudes, dose_rates, marker="o")
plt.title("Cosmic Radiation Dose Rate vs Cruise Altitude")
plt.xlabel("Cruise Altitude (ft)")
plt.ylabel("Dose Rate (µSv/hr)")
plt.grid(True)
plt.show()