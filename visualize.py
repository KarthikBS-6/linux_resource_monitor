import matplotlib.pyplot as plt
import csv
from datetime import datetime
import os

timestamps = []
cpu_usage = []
memory_usage = []

# Read the CSV file
csv_path = "cpu_memory.csv"
if not os.path.exists(csv_path):
    print(f"CSV file not found: {csv_path}")
    exit(1)

with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) != 3:
            continue
        try:
            timestamps.append(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
            cpu_usage.append(float(row[1]))
            memory_usage.append(float(row[2]))
        except ValueError:
            continue  # Skip malformed rows

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(timestamps, cpu_usage, label='CPU Usage (%)', color='pink')
plt.plot(timestamps, memory_usage, label='Memory Usage (%)', color='orange')

plt.xlabel('Timestamp')
plt.ylabel('Usage (%)')
plt.title('System Resource Usage Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)

# Save the graph to a file
output_path = os.path.join(os.getcwd(), "usage_graph.png")
plt.savefig(output_path, bbox_inches='tight')
print(f"Graph saved successfully: {output_path}")
