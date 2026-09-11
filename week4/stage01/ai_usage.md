# AI Feedback:

# 🧩 What your code does
The program builds a tiny appointment‑booking system with three main parts:
Initial output — It prints a welcome message and displays two hard‑coded appointments using simple variables.
Stores appointments — It creates an empty list called appointments that will hold dictionaries, each representing one appointment.
Books appointments — The book_appointment() function:
Validates that the patient name isn’t empty
Builds a dictionary with "patient", "practitioner", and "time"
Appends that dictionary to the global appointments list
Displays appointments — The display_appointments() function:
Prints a message if no appointments exist
Otherwise loops through the list and prints each appointment
Main flow — It prints another welcome message, books two appointments using the function, and then displays them.
This is a solid beginner‑level structure: variables → data structure → functions → main execution.
# ⚠️ Three limitations in your current design
No time conflict checking — The system will happily book two appointments at the same time with the same practitioner.
No practitioner validation — You validate patient names but not practitioner names, so empty or invalid practitioner names could slip through.
Global state dependency — The appointments list is global. As your program grows, global state becomes harder to manage, test, and debug.
These are common limitations in early appointment‑booking exercises.
# 🔧 Improvements you can make (without rewriting the whole app)
Add conflict detection — Before appending a new appointment, scan the list to ensure the practitioner isn’t already booked at that time.
Validate practitioner names — Mirror your patient‑name validation for practitioners.
Encapsulate data — Wrap the list and functions inside a small class like AppointmentSystem. This avoids global state and keeps related logic together.
These changes keep your program simple but make it more realistic and maintainable.
# 📝 Two questions to test your understanding
If you added conflict detection, what information would you need to compare to decide whether two appointments clash?
Why might using a class to store appointments be better than relying on a global list?