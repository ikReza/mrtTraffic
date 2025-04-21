# 🛣️ SUMO Network Creation Documentation

**Project:** Traffic Simulation During Metro Rail Construction  
**Location:** Bangladesh (Left-Hand Driving)  
**Author:** Ibrahim Kaiser  
**Last Updated:** [Insert Date]

---

## 📁 Files Overview

This documentation outlines the manually created files required to build a SUMO road network using `netconvert`, along with the conversion command.

---

1. **`nodes.nod.xml`:** Defines all junction points and intersections in the network.
2. **`edges.edg.xml`:** Specifies the road segments (edges) connecting the nodes.
3. **`connections.con.xml`:** Defines how lanes are connected at intersections. Required for custom or complex junctions.

### 🔄 Network Conversion Command

Use the following netconvert command to generate the SUMO network file:

```xml
netconvert --node-files=nodes.nod.xml --edge-files=edges.edg.xml --connection-files=connections.con.xml --output-file=network.net.xml --lefthand
```

4. **`routes.rou.xml`:** This file defines vehicle types, routes, and traffic flow within the simulation.
5. **`simulation.sumocfg`:** This is the main configuration file that tells SUMO how to run the simulation - it's basically the control center that connects all files (network, routes, output, and settings).
