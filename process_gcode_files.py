import sys
import os

def remove_m73_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        new_lines = [line for line in lines if 'M73' not in line]

        with open(file_path, 'w') as file:
            file.writelines(new_lines)

        print(f"Datei erfolgreich bearbeitet: {file_path}")
    except Exception as e:
        print(f"Fehler beim Bearbeiten der Datei {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for file_path in sys.argv[1:]:
            if file_path.endswith('.gcode'):
                remove_m73_lines(file_path)
            else:
                print(f"{file_path} ist keine .gcode-Datei.")
    else:
        print("Bitte ziehen Sie eine .gcode-Datei auf das Skript.")
