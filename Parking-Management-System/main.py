import os

FILE_NAME = "parking.txt"

TOTAL_SLOTS = 5
CAR_RATE = 20
BIKE_RATE = 10

slots = [None] * TOTAL_SLOTS


def check_number(number):
    number = number.strip().upper()

    if len(number) < 6 or len(number) > 10:
        return False

    if not number[:2].isalpha() or not number[2:4].isdigit():
        return False

    remaining = number[4:]

    if len(remaining) < 2 or len(remaining) > 6:
        return False

    letters = 0
    digits = 0

    for ch in remaining:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1
        else:
            return False

    return 1 <= letters <= 2 and 1 <= digits <= 4


def check_existing(number):
    for vehicle in slots:
        if vehicle is not None:
            if vehicle["number"] == number:
                return True
    return False


def free_slots():
    count = 0

    for vehicle in slots:
        if vehicle is None:
            count += 1

    return count


def save_data():
    try:
        with open(FILE_NAME, "w") as file:
            for i in range(TOTAL_SLOTS):
                if slots[i] is not None:
                    vehicle = slots[i]
                    file.write(
                        str(i) + "," +
                        vehicle["number"] + "," +
                        vehicle["type"] + "\n"
                    )
        return True

    except OSError:
        print("Error saving parking details.")
        return False


def load_data():
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 3:
                    continue

                try:
                    slot = int(parts[0])
                except ValueError:
                    continue

                number = parts[1].strip().upper()
                v_type = parts[2].strip().lower()

                if slot < 0 or slot >= TOTAL_SLOTS:
                    continue

                if not check_number(number):
                    continue

                if v_type not in ["car", "bike"]:
                    continue

                if slots[slot] is not None:
                    continue

                if check_existing(number):
                    continue

                slots[slot] = {
                    "number": number,
                    "type": v_type
                }

    except OSError:
        print("Error loading parking details.")


def vehicle_entry():

    if free_slots() == 0:
        print("Parking is full!")
        return

    number = input("Enter vehicle number: ").strip().upper()

    if not check_number(number):
        print("Invalid vehicle number!")
        return

    if check_existing(number):
        print("Vehicle is already parked.")
        return

    v_type = input("Enter vehicle type (car/bike): ").strip().lower()

    if v_type not in ["car", "bike"]:
        print("Invalid vehicle type!")
        return

    slot_number = -1

    for i in range(TOTAL_SLOTS):
        if slots[i] is None:
            slot_number = i
            break

    if slot_number == -1:
        print("Parking is full!")
        return

    slots[slot_number] = {
        "number": number,
        "type": v_type
    }

    if save_data():
        print("Vehicle parked successfully!")
        print("Parking slot:", slot_number + 1)
        print("Free slots:", free_slots())
    else:
        slots[slot_number] = None


def parking_fee(hours, v_type):

    billed_hours = int(hours)

    if hours > billed_hours:
        billed_hours += 1

    if billed_hours < 1:
        billed_hours = 1

    if v_type == "car":
        fee = billed_hours * CAR_RATE
    else:
        fee = billed_hours * BIKE_RATE

    return billed_hours, fee


def vehicle_exit():

    number = input("Enter vehicle number: ").strip().upper()

    if not check_number(number):
        print("Invalid vehicle number!")
        return

    found_slot = -1

    for i in range(TOTAL_SLOTS):
        if slots[i] is not None:
            if slots[i]["number"] == number:
                found_slot = i
                break

    if found_slot == -1:
        print("Vehicle not found.")
        return

    vehicle = slots[found_slot]

    try:
        hours = float(input("Enter parking hours: "))
    except ValueError:
        print("Invalid parking hours.")
        return

    if hours < 0 or hours == float("inf") or hours != hours:
        print("Invalid parking hours.")
        return

    billed_hours, fee = parking_fee(hours, vehicle["type"])

    print("\nParking hours charged:", billed_hours)
    print("Total parking fee: Rs.", fee)

    slots[found_slot] = None

    if save_data():
        print("Vehicle removed successfully!")
        print("Slot", found_slot + 1, "is now free.")
        print("Free slots:", free_slots())
    else:
        slots[found_slot] = vehicle


def parking_status():

    print("\n--------- PARKING STATUS ---------")

    parked = False

    for i in range(TOTAL_SLOTS):
        if slots[i] is not None:
            parked = True
            print("Slot", i + 1, "-", slots[i]["number"])
        else:
            print("Slot", i + 1, "- Empty")

    if not parked:
        print("No vehicles are parked.")
        return

    number = input("\nEnter vehicle number for details: ").strip().upper()

    if not check_number(number):
        print("Invalid vehicle number!")
        return

    for i in range(TOTAL_SLOTS):
        if slots[i] is not None:
            if slots[i]["number"] == number:
                print("\n------ VEHICLE DETAILS ------")
                print("Vehicle Number:", number)
                print("Vehicle Type:", slots[i]["type"])
                print("Parking Slot:", i + 1)
                return

    print("Vehicle is not currently parked.")


def main():

    print("\n    PARKING MANAGEMENT SYSTEM")

    load_data()

    while True:

        print("\n1. Vehicle Entry")
        print("2. Vehicle Exit")
        print("3. Parking Status")
        print("4. Exit Program")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            vehicle_entry()

        elif choice == "2":
            vehicle_exit()

        elif choice == "3":
            parking_status()

        elif choice == "4":
            print("Thank you for using Parking Management System!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()