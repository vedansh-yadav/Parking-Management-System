# Test Cases - Parking Management System

| INPUT | EXPECTED OUTPUT |
| :--- | :--- |
| **Test Case 1: Normal Input** | |
| Menu option 1 (Entry)<br>Vehicle: MH12AB1234<br>Type: car | Vehicle MH12AB1234 parked in slot 1.<br>Slots free: 4 |
| **Test Case 2: Boundary / Minimum Input** | |
| MH12AB1234 (car) is in slot 1<br>Menu option 2 (Exit)<br>Vehicle: MH12AB1234<br>Hours: 0.5 | Hours charged: 1 (minimum) \| Fee: 20<br>Slot 1 is now free. |
| **Test Case 3: Invalid Input** | |
| MH12AB1234 is parked<br>(a) Entry: MH12AB1234<br>(b) Entry: KA01XY9999, Type: truck<br>(c) Exit: XX00XX0000 | (a) Vehicle MH12AB1234 is already parked.<br>(b) Invalid type. Enter car or bike.<br>(c) Vehicle XX00XX0000 not found. |
| **Test Case 4: Different Valid Scenario** | |
| (a) Entry: KA01AB1111, Type: bike<br>(b) Exit: KA01AB1111, Hours: 2.5<br>(c) Option 3 (Status) | (a) Vehicle KA01AB1111 parked in slot 1.<br>(b) Hours charged: 3 (rounded up) \| Fee: 30<br>(c) Slots free: 5 of 5 |