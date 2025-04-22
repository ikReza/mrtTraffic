import xml.etree.ElementTree as ET
import pandas as pd

# Parse the tripinfo.xml file.
tree = ET.parse("tripinfo.xml")
root = tree.getroot()

# Extract data into a list.
trip_data = []
for trip in root.findall("tripinfo"):
    trip_info = {
        "Vehicle_ID": trip.get("id"),
        "Depart": float(trip.get("depart", 0)),
        "Arrival": float(trip.get("arrival", 0)),
        "Duration": float(trip.get("duration", 0)),
        "Waiting Time": float(trip.get("waitingTime", 0)),
        "Departure Delay": float(trip.get("departDelay", 0)),
        "Vehicle": trip.get("vType", 0)
    }
    trip_data.append(trip_info)

# Convert list to a DataFrame.
df = pd.DataFrame(trip_data)

# Save to Excel (or CSV) for further analysis.
df.to_excel("tripinfo.xlsx", index=False)
print("Trip information saved to tripinfo.xlsx")