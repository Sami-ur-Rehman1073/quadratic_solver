import psutil
import time
import csv

with open("cpu.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "cpu"])

    for i in range(60):
        writer.writerow([i, psutil.cpu_percent()])
        time.sleep(1)