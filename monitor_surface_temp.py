import os
import json
import glob
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from threading import Thread

# Path to logs Elite Dangerous
LOG_DIR = os.path.expanduser(r'~\Saved Games\Frontier Developments\Elite Dangerous')

# Dictionary to keep track of calculated temperatures for each system
calculated_temperatures = {}
current_system = None

def get_latest_log_file():
    files = glob.glob(os.path.join(LOG_DIR, 'Journal.*.log'))
    if not files:
        print("[DEBUG] No logs!")
        return None
    latest_file = max(files, key=os.path.getctime)
    print(f"[DEBUG] Latest log file: {latest_file}")
    return latest_file

def parse_log_file(filepath):
    global calculated_temperatures, current_system

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                try:
                    data = json.loads(line)
                    event_type = data.get('event')

                    if event_type == 'FSSDiscoveryScan':
                        current_system = data.get('SystemName')
                        if current_system and current_system not in calculated_temperatures:
                            calculated_temperatures[current_system] = set()

                    elif event_type == 'Scan':
                        star_system = data.get('StarSystem')
                        temperature = data.get('SurfaceTemperature')
                        if star_system and temperature is not None:
                            if star_system not in calculated_temperatures:
                                calculated_temperatures[star_system] = set()
                            calculated_temperatures[star_system].add(float(temperature))

                except json.JSONDecodeError:
                    print("[ERROR] JSON decoding error")
                    continue

    except Exception as e:
        print(f"[ERROR] Error opening file: {e}")

def update_label(label):
    global current_system
    while True:
        latest_log = get_latest_log_file()
        if latest_log:
            parse_log_file(latest_log)
            if current_system and current_system in calculated_temperatures:
                total_temp = sum(calculated_temperatures[current_system])
                label.config(text=f"Sum of the temperatures of all suns & planets in system: {current_system} = {total_temp:.2f} K")
                print(f"[DEBUG] Current system: {current_system}, Sum of sun temperatures: {total_temp:.2f} K")
        time.sleep(3)

def main():
    root = tk.Tk()
    root.title("Overall System Temperature Monitor - E.D.")
    root.attributes('-topmost', True)  # Set window to always on top

    label = tk.Label(root, text="Waiting for data...", font=("Calibri", 12))
    label.pack(pady=20, padx=20)

    # Start update in new thread
    update_thread = Thread(target=update_label, args=(label,), daemon=True)
    update_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()
