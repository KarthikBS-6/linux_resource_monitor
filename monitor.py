import psutil
import csv
from datetime import datetime

csv_file = 'cpu_memory.csv'

def log_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory.percent
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(csv_file, 'a', newline='') as f:

        writer = csv.writer(f)

        writer.writerow([timestamp, cpu, memory])

if __name__ == "__main__":
    log_metrics()
