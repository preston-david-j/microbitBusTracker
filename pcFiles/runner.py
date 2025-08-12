import os

filename = "savedstops.txt"

def addStop(newStop):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write(newStop)
        print(f"File did not exist; created and wrote stop: {newStop}")
        return

    with open(filename, "r") as file:
        lines = file.readlines()

    if not any(line.strip() for line in lines):
        with open(filename, "w") as file:
            file.write(newStop)
        print(f"File was empty; overwrote with stop: {newStop}")
    else:
        with open(filename, "a") as file:
            file.write(f"\n{newStop}")
        print(f"Appended new stop: {newStop}")

def getStops():
    with open(filename, "r") as file:
        return file.readlines()
    
if __name__ == "__main__":
    addStop("sasha")
    
