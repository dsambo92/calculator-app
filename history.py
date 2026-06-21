from datetime import datetime

history = []

def add_history(entry):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(f"{timestamp} | {entry}")

def get_history():
    return history
