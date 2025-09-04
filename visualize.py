import matplotlib.pyplot as plt
import csv
from datetime import datetime

timestamps = []
cpu_usage = []
memory_usage = []

with open("cpu_memory.csv', 'r') as f:

    reader = csv.reader(f)

    for row in reader:

        if len(row) != 3:
            continue

        timestamps.append(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
        cpu_usage.append)float(row[1]))
        memory_usage.append(float(row[2]))

plt.figure(figsize=(10,5))

plt.plot(timestamps, cpu_usage, label='CPU Usage (%)', color='pink')
plt.plot(timestamps, memory_usage, label='Memory Usagae (%)', color='orange')

plt.xlabel('Timestamp')
plt.ylable('Usage (%)')

plt.title('System Resource Usage Over Time')

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.grid(True)

plt.savefig("usage_graph.png")
