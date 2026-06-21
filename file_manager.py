import os
import csv

def save_txt(path, history):
    with open(path, "a") as f:
        for entry in history:
            f.write(entry + "\n")

def save_csv(path, history):
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)

        if f.tell() == 0:
            writer.writerow(["Timestamp", "Calculation"])

        for entry in history:
            time_part, calc_part = entry.split(" | ")
            writer.writerow([time_part, calc_part])

def ensure_folder(path):
    os.makedirs(path, exist_ok=True)
