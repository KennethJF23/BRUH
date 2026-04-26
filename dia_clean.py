from graphviz import Digraph

# Create a clean, professional SIH Rockfall Prediction System Flow Diagram
dot = Digraph("SIH_Rockfall_System", format="png")
dot.attr(rankdir="TB", size="18,14", bgcolor="white", dpi="300", 
         nodesep="1.5", ranksep="2.0", overlap="false", pad="0.5")
dot.attr('node', fontname="Arial", fontsize="10", margin="0.3,0.2", 
         style="filled", shape="box")
dot.edge_attr.update(fontname="Arial", fontsize="8", arrowsize="0.8", 
                     penwidth="2")

# Define consistent colors for each layer
colors = {
    'data': '#E3F2FD',      # Light Blue
    'ai': '#FFF3E0',        # Light Orange  
    'backend': '#E8F5E8',   # Light Green
    'alert': '#FFEBEE',     # Light Red
    'frontend': '#F3E5F5'   # Light Purple
}

# =========================
# LAYER 1: DATA COLLECTION
# =========================
dot.node("iot", "IoT Sensors\n────────────\n• Temperature\n• Humidity\n• Vibration\n• Rainfall", 
         color=colors['data'])

dot.node("drone", "Drone & DEM\n────────────\n• Aerial Imagery\n• Terrain Maps\n• 3D Models", 
         color=colors['data'])

dot.node("weather", "Weather APIs\n────────────\n• Rainfall Data\n• Temperature\n• Forecasts", 
         color=colors['data'])

dot.node("gps", "Miner GPS\n────────────\n• Live Location\n• GeoJSON\n• Tracking", 
         color=colors['data'])

dot.node("reports", "Miner Reports\n────────────\n• Manual Input\n• Confirmations\n• Field Data", 
         color=colors['data'])

# =========================
# LAYER 2: AI/ML PROCESSING  
# =========================
dot.node("rockfall_ai", "Rockfall Prediction\n═══════════════════\n• Random Forest\n• XGBoost\n• Risk Probability", 
         color=colors['ai'], shape="ellipse")

dot.node("weather_ai", "Weather Prediction\n═══════════════════\n• AI Models\n• Rainfall Analysis\n• Forecasting", 
         color=colors['ai'], shape="ellipse")

dot.node("risk_engine", "Risk Analysis Engine\n═══════════════════\n• Data Integration\n• Risk Assessment\n• Threat Evaluation", 
         color=colors['ai'], shape="ellipse")

# =========================
# LAYER 3: BACKEND SYSTEMS
# =========================
dot.node("api", "Flask/FastAPI\n───────────────\n• REST APIs\n• WebSocket\n• Connections", 
         color=colors['backend'])

dot.node("database", "MongoDB\n───────────────\n• Geospatial Queries\n• GeoJSON Storage\n• Real-time Data", 
         color=colors['backend'], shape="cylinder")

dot.node("nodejs", "Node.js Server\n───────────────\n• WebSocket Comms\n• Real-time Updates\n• Chat System", 
         color=colors['backend'])

# =========================
# LAYER 4: ALERT SYSTEM
# =========================
dot.node("alert_engine", "Alert Engine\n▲▲▲▲▲▲▲▲▲▲▲▲▲\n• Threshold Detection\n• Auto Triggers\n• Risk Monitoring", 
         color=colors['alert'], shape="diamond")

dot.node("sms", "SMS Alerts\n─────────────\n• Twilio API\n• Instant Alerts\n• Emergency Msgs", 
         color=colors['alert'])

dot.node("email", "Email System\n─────────────\n• SMTP Service\n• Detailed Reports\n• Notifications", 
         color=colors['alert'])

dot.node("rescue", "Rescue Team\n─────────────\n• Emergency Response\n• Coordination\n• Field Operations", 
         color='#FFCDD2')

# =========================
# LAYER 5: USER INTERFACES
# =========================
dot.node("risk_map", "Interactive Risk Map\n▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼\n• React + Leaflet\n• Zone Visualization\n• Safe/Moderate/High", 
         color=colors['frontend'])

dot.node("simulation", "3D Simulation\n▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼\n• Three.js + RocFall3\n• Path Visualization\n• Impact Analysis", 
         color=colors['frontend'])

dot.node("dashboard", "Scenario Dashboard\n▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼\n• What-if Analysis\n• Real-time Updates\n• Data Visualization", 
         color=colors['frontend'])

dot.node("miner_app", "Miner Mobile App\n▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼\n• Real-time Chat\n• Reports & Alerts\n• Location Sharing", 
         color=colors['frontend'])

# ==============================
# CONNECTIONS (Layer by Layer)
# ==============================

# Layer 1 to Layer 2: Data to AI
dot.edge("iot", "rockfall_ai", label="sensor data", color="#2196F3")
dot.edge("drone", "rockfall_ai", label="terrain data", color="#2196F3")
dot.edge("weather", "weather_ai", label="weather data", color="#2196F3")
dot.edge("reports", "risk_engine", label="manual reports", color="#2196F3")

# Layer 2: AI Internal Processing
dot.edge("rockfall_ai", "risk_engine", label="predictions", color="#FF9800")
dot.edge("weather_ai", "risk_engine", label="forecasts", color="#FF9800")

# Layer 2 to Layer 3: AI to Backend
dot.edge("risk_engine", "api", label="risk assessment", color="#4CAF50")
dot.edge("gps", "database", label="location data", color="#4CAF50")

# Layer 3: Backend Internal
dot.edge("api", "database", label="store data", color="#4CAF50")
dot.edge("database", "nodejs", label="sync data", color="#4CAF50")

# Layer 3 to Layer 4: Backend to Alerts
dot.edge("api", "alert_engine", label="trigger alerts", color="#F44336")

# Layer 4: Alert System Internal
dot.edge("alert_engine", "sms", label="SMS alerts", color="#F44336")
dot.edge("alert_engine", "email", label="email alerts", color="#F44336")
dot.edge("alert_engine", "rescue", label="emergency", color="#F44336")

# Layer 3 to Layer 5: Backend to Frontend
dot.edge("database", "risk_map", label="map data", color="#9C27B0")
dot.edge("api", "dashboard", label="dashboard data", color="#9C27B0")
dot.edge("nodejs", "miner_app", label="real-time comms", color="#9C27B0")

# Layer 2 to Layer 5: Direct AI to Frontend
dot.edge("risk_engine", "simulation", label="simulation params", color="#9C27B0")

# Feedback Loops (Dashed lines)
dot.edge("miner_app", "reports", label="user feedback", style="dashed", color="#757575")
dot.edge("dashboard", "risk_engine", label="scenario testing", style="dashed", color="#757575")
dot.edge("rescue", "miner_app", label="status updates", style="dashed", color="#757575")

# Render the diagram
print("Creating professional SIH Rockfall Prediction System diagram...")
try:
    file_path = "SIH_Rockfall_Prediction_System_Flow"
    print(f"Rendering diagram to: {file_path}")
    dot.render(file_path, cleanup=True)
    print(f"Professional diagram saved as: {file_path}.png")
    print("Success!")
except Exception as e:
    print(f"Error creating diagram: {e}")
    print("You need to install Graphviz on your system.")
    print("Visit: https://graphviz.org/download/ to download and install Graphviz")
    print("Or run: choco install graphviz (if you have Chocolatey)")
    print("Make sure to add Graphviz to your system PATH after installation.")