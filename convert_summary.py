import xml.etree.ElementTree as ET
import pandas as pd

# Load and parse the summary XML file
tree = ET.parse("summary.xml")
root = tree.getroot()

# Each timestep element contains summary data
summary_data = []
for timestep in root.findall("step"):
    row = {
        "Time": float(timestep.get("time", 0)),
        "Departed": int(timestep.get("departed", 0)),
        "Arrived": int(timestep.get("arrived", 0)),
        "Running": int(timestep.get("running", 0)),
        "Waiting": int(timestep.get("waiting", 0)),
    }
    summary_data.append(row)

# Convert to a DataFrame and save to Excel
df = pd.DataFrame(summary_data)
df.to_excel("summary.xlsx", index=False)
print("Summary saved to summary.xlsx")