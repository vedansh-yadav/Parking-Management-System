# Parking Management System (PS No. 39)

A modular, terminal-driven Parking Management System built using Python 3. It automates vehicle check-in, slot assignment, tariff calculation, live occupancy monitoring, and crash-safe text file persistence using only standard built-in libraries.

---

## 1. Problem Statement

Build a console-based parking lot management application for a compact facility where incoming vehicles are assigned sequential slot numbers, tracked in real time, and billed accurately at checkout according to vehicle category and stay duration.

### Core Specifications & Constraints
* **Total Capacity:** 5 sequential parking slots (`Slot 1` to `Slot 5`).
* **Supported Vehicles & Hourly Rates:**
  * **Car:** ₹20 per hour
  * **Bike:** ₹10 per hour
* **Billing Rules:** 
  * Partial hours are always **rounded up** to the next full integer hour (e.g., `1.2` hours is charged as `2` hours).
  * A **minimum billing floor of 1 hour** is enforced for short stays (e.g., `0.3` hours is charged as `1` hour).
* **Data Persistence:** Current slot allocations must be persisted to `parking.txt` immediately after every entry or exit transaction.
* **Menu Options:** `1. Vehicle Entry`, `2. Vehicle Exit`, `3. Parking Status`, `4. Exit Program`.

---

## 2. Solution Architecture & Design

The implementation in `main.py` follows a clean procedural design built with fundamental Python constructs—**Lists, Dictionaries, Functions, Conditionals, Loops, and File I/O**—requiring zero third-party packages.

### Data Structures
1. **Slot Allocation Array (List):** A pre-allocated list `slots = [None] * 5` models the physical parking lot. Each index holds `None` when vacant or a vehicle dictionary when occupied.
2. **Vehicle Metadata Object (Dictionary):** Every active vehicle record is encapsulated as a dictionary:
   ```python
   {
       "vehicle_number": "CG04AB1234",
       "type": "car",
       "entry_time": "2026-11-13 16:30:00"
   }
   ```

### Key Functional Modules
* **`is_valid_vehicle_number(v_num)`**: Verifies Indian RTO registration syntax (e.g., `CG04AB1234`) by validating length, state letters, district digits, series letters, and plate digits.
* **`entry()`**: Verifies free capacity, validates plate format and vehicle category (`car`/`bike`), blocks duplicate check-ins, allocates the first empty slot, and saves state.
* **`calculate_fee(hours, v_type)`**: Applies ceiling rounding via integer truncation comparison (`int(hours)`), guarantees a 1-hour minimum, and computes the total tariff.
* **`exit_vehicle()`**: Searches for the registered plate, validates parked hours, generates a formatted receipt, releases the slot, and syncs `parking.txt`.
* **`status()`**: Prints a complete slot-by-slot occupancy report (`EMPTY` or `OCCUPIED` with check-in timestamp) followed by total, occupied, and free slot counts.
* **`save_data()` & `load_data()`**: Uses atomic file replacement via `parking.tmp` to prevent file corruption and automatically cleans invalid or duplicate entries during startup.

---

## 3. Data Persistence Format (`parking.txt`)

Active parking states are serialized in comma-separated format (`CSV` style) with one record per line:

```text
<slot_index>,<vehicle_number>,<vehicle_type>,<entry_timestamp>
```

**Example:**
```text
0,CG04AB1234,car,2026-11-13 15:30:00
2,DL01XY9876,bike,2026-11-13 15:45:12
```

---

## 4. How to Run the Project

### Prerequisites
* Python 3.x installed on your machine.

### Execution Steps
1. Open your terminal or command prompt inside the project folder.
2. Execute the main script:
   ```bash
   python main.py
   ```
3. Choose an action from the menu (`1` to `4`) to operate the parking lot.

---

## 5. Sample Console Output

```text
================================
     PARKING MANAGEMENT SYSTEM
================================

1. Vehicle Entry
2. Vehicle Exit
3. Parking Status
4. Exit Program
Enter your choice: 1
Enter vehicle number: CG04AB1234
Enter vehicle type (car/bike): car

Vehicle CG04AB1234 parked in slot 1 .
Slots free: 4
```