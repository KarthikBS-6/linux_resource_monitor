# Linux Resource Monitor

A Python-based tool that collects CPU and memory usage from a Linux server every 10 minutes, logs the data to a CSV file, and visualizes performance trends using Matplotlib. Designed for automation via Jenkins and built with clarity and modularity for portfolio visibility.

---

## 🔧 Features

- Collects system metrics using 'psutil'
- Logs CPU and memory usage with timestamps to a CSV file
- Generates clean time-series graphs using Matplotlib
- Saves visualizations as PNG for easy sharing
- Automates data collection via Jenkins or cron
- Modular script design for clarity and scalability

---

## 🛠️ Tech Stack

- Python 3  
- psutil  
- Matplotlib  
- Jenkins   
- Linux (Ubuntu tested)

---

## 📂 Project Structure

linux_resource_monitor/
├── monitor.py             # Collects CPU and memory usage every 10 minutes
├── visualize.py           # Reads CSV and generates usage graphs
├── system_usage.csv       # Stores timestamped CPU and memory metrics
├── requirements.txt       # Lists Python dependencies (psutil, matplotlib)
├── screenshots/
│   └── usage_graph.png    # Saved graph image for portfolio and README
├── README.md              # Project documentation

## 🚀 How It Works

### 1. **Data Collection**
Run 'monitor.py` every 10 minutes via Jenkins or cron:

python3 monitor.py


2. Visualization
Generate a graph from the collected data:

python3 visualize.py

Graph is saved as screenshots/usage_graph.png.

📸 Sample Output:

https://github.com/KarthikBS-6/linux_resource_monitor/usage_graph.png

🔁 Jenkins Integration

• 	Schedule monitor.py every 10 minutes.
• 	Optionally run visualize.py daily.
• 	Archive system_usage.csv and graph as build artifacts


🧠 What I Learned:

• 	Structuring Python scripts for automation and clarity
• 	Using Matplotlib to visualize system metrics
• 	Automating tasks via Jenkins on Linux
• 	Documenting technical work for GitHub and interviews


