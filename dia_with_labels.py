from graphviz import Digraph

# Create a comprehensive SIH Hackathon Application Flow Diagram with visible labels
dot = Digraph("SIH_Rockfall_System_Labels", format="png")
dot.attr(rankdir="TB", size="24,20", bgcolor="white", dpi="600", 
         nodesep="1.8", ranksep="2.5", overlap="false", pad="1.0")
dot.attr('node', fontname="Arial Bold", fontsize="12", margin="0.5,0.4", 
         fixedsize="false")
dot.attr('edge', fontname="Arial", fontsize="10", minlen="3", 
         arrowsize="1.3", penwidth="2")

# Data Collection Layer
with dot.subgraph(name="cluster_0") as c:
    c.attr(label="DATA COLLECTION LAYER", style="filled", color="lightcyan", 
           fontsize="16", fontname="Arial Bold", margin="20")
    c.node("IoT_Sensors", "IoT SENSORS\\n━━━━━━━━━━━━━━\\nTemperature\\nHumidity\\nVibration\\nRainfall", 
           shape="box", style="filled,rounded", color="#87CEEB")
    c.node("Drone_DEM", "DRONE & DEM\\n━━━━━━━━━━━━━━\\nAerial Imagery\\nTerrain Mapping\\n3D Models", 
           shape="box", style="filled,rounded", color="#87CEEB")
    c.node("Weather_API", "WEATHER APIs\\n━━━━━━━━━━━━━━\\nRainfall Data\\nTemperature\\nForecasts", 
           shape="box", style="filled,rounded", color="#87CEEB")
    c.node("Miner_GPS", "MINER GPS\\n━━━━━━━━━━━━━━\\nReal-time Location\\nGeoJSON Data\\nTracking", 
           shape="box", style="filled,rounded", color="#87CEEB")
    c.node("Miner_Reports", "MINER REPORTS\\n━━━━━━━━━━━━━━\\nManual Rockfall\\nConfirmations\\nField Data", 
           shape="box", style="filled,rounded", color="#87CEEB")

# AI/ML Processing Layer
with dot.subgraph(name="cluster_1") as c:
    c.attr(label="AI/ML PROCESSING LAYER", style="filled", color="lightyellow", 
           fontsize="16", fontname="Arial Bold", margin="20")
    c.node("Rockfall_Model", "ROCKFALL PREDICTION\\n━━━━━━━━━━━━━━━━━━━━━━━━\\nRandom Forest\\nXGBoost\\nProbability Forecasting", 
           shape="ellipse", style="filled", color="#FFD700")
    c.node("Weather_Model", "WEATHER PREDICTION\\n━━━━━━━━━━━━━━━━━━━━━━━━\\nAI Models\\nRainfall & Temperature\\nForecast Engine", 
           shape="ellipse", style="filled", color="#FFD700")
    c.node("Risk_Analysis", "RISK ANALYSIS\\n━━━━━━━━━━━━━━━━━━━━━━━━\\nData Integration\\nRisk Assessment\\nThreat Evaluation", 
           shape="ellipse", style="filled", color="#FFA500")

# Backend Systems
with dot.subgraph(name="cluster_2") as c:
    c.attr(label="BACKEND SYSTEMS", style="filled", color="lightgreen", 
           fontsize="16", fontname="Arial Bold", margin="20")
    c.node("Flask_API", "FLASK/FASTAPI\\n━━━━━━━━━━━━━━━━━━━━\\nREST APIs\\nWebSocket\\nConnections", 
           shape="box", style="filled,rounded", color="#90EE90")
    c.node("MongoDB", "MONGODB\\n━━━━━━━━━━━━━━━━━━━━\\nGeospatial Queries\\nGeoJSON Storage\\nReal-time Data", 
           shape="cylinder", style="filled", color="#90EE90")
    c.node("NodeJS_Server", "NODE.JS SERVER\\n━━━━━━━━━━━━━━━━━━━━\\nWebSocket Comms\\nReal-time Updates\\nChat System", 
           shape="box", style="filled,rounded", color="#90EE90")

# Alert & Communication System
with dot.subgraph(name="cluster_3") as c:
    c.attr(label="ALERT & COMMUNICATION SYSTEM", style="filled", color="lightcoral", 
           fontsize="16", fontname="Arial Bold", margin="20")
    c.node("Alert_Engine", "ALERT ENGINE\\n━━━━━━━━━━━━━━━━━━━━\\nThreshold Detection\\nAutomated Triggers\\nRisk Monitoring", 
           shape="diamond", style="filled", color="#FFA500")
    c.node("Twilio_SMS", "TWILIO SMS\\n━━━━━━━━━━━━━━━━━━━━\\nInstant Alerts\\nMiners & Teams\\nEmergency Msgs", 
           shape="box", style="filled,rounded", color="#F08080")
    c.node("SMTP_Email", "EMAIL SYSTEM\\n━━━━━━━━━━━━━━━━━━━━\\nDetailed Reports\\nNotifications\\nDocumentation", 
           shape="box", style="filled,rounded", color="#F08080")
    c.node("Rescue_Team", "RESCUE TEAM\\n━━━━━━━━━━━━━━━━━━━━\\nEmergency Response\\nCoordination\\nField Operations", 
           shape="box", style="filled,rounded", color="#DC143C")

# Visualization & Interface Layer
with dot.subgraph(name="cluster_4") as c:
    c.attr(label="VISUALIZATION & INTERFACE LAYER", style="filled", color="lavender", 
           fontsize="16", fontname="Arial Bold", margin="20")
    c.node("Risk_Map", "INTERACTIVE RISK MAP\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━\\nReact + Leaflet\\nSafe/Moderate/High\\nZone Visualization", 
           shape="box", style="filled,rounded", color="#9370DB")
    c.node("ThreeJS_Sim", "3D SIMULATION\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━\\nThree.js + RocFall3\\nPath Visualization\\nImpact Analysis", 
           shape="box", style="filled,rounded", color="#9370DB")
    c.node("Scenario_Dashboard", "SCENARIO DASHBOARD\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━\\nWhat-if Analysis\\nReal-time Updates\\nData Visualization", 
           shape="box", style="filled,rounded", color="#9370DB")
    c.node("Miner_App", "MINER APP\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━\\nReal-time Chat\\nReports & Alerts\\nLocation Sharing", 
           shape="box", style="filled,rounded", color="#9370DB")

# LAYER 1: Data Collection to AI/ML
dot.edge("IoT_Sensors", "Rockfall_Model", label="◆ Sensor Data", color="#1E90FF", penwidth="3")
dot.edge("Drone_DEM", "Rockfall_Model", label="◆ Terrain Data", color="#1E90FF", penwidth="3")
dot.edge("Weather_API", "Weather_Model", label="◆ Weather Data", color="#1E90FF", penwidth="3")
dot.edge("Miner_Reports", "Risk_Analysis", label="◆ Manual Reports", color="#1E90FF", penwidth="3")
dot.edge("Miner_GPS", "MongoDB", label="◆ GPS Data", color="#1E90FF", penwidth="3")

# LAYER 2: AI/ML Internal Processing
dot.edge("Rockfall_Model", "Risk_Analysis", label="◆ Predictions", color="#FF8C00", penwidth="3")
dot.edge("Weather_Model", "Risk_Analysis", label="◆ Forecasts", color="#FF8C00", penwidth="3")

# LAYER 3: AI/ML to Backend
dot.edge("Risk_Analysis", "Flask_API", label="◆ Risk Assessment", color="#32CD32", penwidth="3")

# LAYER 4: Backend Internal Flow
dot.edge("Flask_API", "MongoDB", label="◆ Store Data", color="#32CD32", penwidth="3")
dot.edge("MongoDB", "NodeJS_Server", label="◆ Sync Data", color="#32CD32", penwidth="3")

# LAYER 5: Backend to Alert System
dot.edge("Flask_API", "Alert_Engine", label="◆ Trigger Alerts", color="#DC143C", penwidth="3")

# LAYER 6: Alert System Internal
dot.edge("Alert_Engine", "Twilio_SMS", label="◆ SMS", color="#DC143C", penwidth="3")
dot.edge("Alert_Engine", "SMTP_Email", label="◆ Email", color="#DC143C", penwidth="3")  
dot.edge("Alert_Engine", "Rescue_Team", label="◆ Emergency", color="#DC143C", penwidth="3")

# LAYER 7: Backend to Frontend
dot.edge("MongoDB", "Risk_Map", label="◆ Map Data", color="#8A2BE2", penwidth="3")
dot.edge("Flask_API", "Scenario_Dashboard", label="◆ Dashboard", color="#8A2BE2", penwidth="3")
dot.edge("NodeJS_Server", "Miner_App", label="◆ Real-time", color="#8A2BE2", penwidth="3")
dot.edge("Risk_Analysis", "ThreeJS_Sim", label="◆ Simulation", color="#8A2BE2", penwidth="3")

# Feedback Loops
dot.edge("Miner_App", "Miner_Reports", label="◇ Feedback", style="dashed", color="#696969", penwidth="2")
dot.edge("Scenario_Dashboard", "Risk_Analysis", label="◇ Testing", style="dashed", color="#696969", penwidth="2")
dot.edge("Rescue_Team", "Miner_App", label="◇ Updates", style="dashed", color="#696969", penwidth="2")

# Render the diagram
print("Creating labeled diagram...")
try:
    file_path = "SIH_Rockfall_System_WITH_LABELS"
    print(f"Rendering diagram to: {file_path}")
    dot.render(file_path, cleanup=True)
    print(f"Labeled diagram saved as: {file_path}.png")
    print("Success!")
except Exception as e:
    print(f"Error creating diagram: {e}")