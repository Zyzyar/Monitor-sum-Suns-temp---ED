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

def get_latest_log_file():
    files = glob.glob(os.path.join(LOG_DIR, 'Journal.*.log'))
    if not files:
        print("[DEBUG] No logs!")
        return None
    latest_file = max(files, key=os.path.getctime)
    print(f"[DEBUG] Latest log file: {latest_file}")
    return latest_file

def parse_log_file(filepath):
    system_temperatures = {}
    current_system = None

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in reversed(lines):
                try:
                    data = json.loads(line)
                    event_type = data.get('event')
                    
                    if event_type == 'FSSDiscoveryScan':
                        current_system = data.get('SystemName')
                        if current_system not in system_temperatures:
                            system_temperatures[current_system] = []
                    
                    elif event_type == 'Scan' and data.get('StarSystem') == current_system:
                        temperature = data.get('SurfaceTemperature')
                        if temperature is not None:
                            system_temperatures[current_system].append(float(temperature))
                
                except json.JSONDecodeError:
                    print("[ERROR] JSON decoding error")
                    continue
    
    except Exception as e:
        print(f"[ERROR] Error opening file: {e}")
    
    return system_temperatures

def update_label(label):
    while True:
        latest_log = get_latest_log_file()
        if latest_log:
            system_temperatures = parse_log_file(latest_log)
            if system_temperatures:
                current_system = list(system_temperatures.keys())[0]  # We assume that the system is one at a time
                total_temp = sum(system_temperatures[current_system])
                label.config(text=f"Sum of temperatures all suns in 1 system: {current_system} = {total_temp:.2f} K")
                print(f"[DEBUG] Sum of sun temperatures: {total_temp:.2f} K")
        time.sleep(3)

def main():
    root = tk.Tk()
    root.title("Monitor Suns Surface Temp`s - ED")
    root.attributes('-topmost', True)  # Set window to always on top

    label = tk.Label(root, text="Waiting for data...", font=("Calibri", 12))
    label.pack(pady=20, padx=20)

    # Start update in new thread
    update_thread = Thread(target=update_label, args=(label,), daemon=True)
    update_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()
