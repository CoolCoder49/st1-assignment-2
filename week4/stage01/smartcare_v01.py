# Part A - Understand the Problem

# What data must be stored?
# The system must store the patient's name, the practitioner's name, and the appointment time.

# What functions might be useful?
# book_appointment() to collect data and display_appointments() to format and show the results.

# What could go wrong?
# Users may submit empty strings or invalid data types, resulting in Garbage in, Garbage out (GIGO). Also, crashes may occur if exceptions like ValueError are not handled properly.

# What requirements are unclear?
# The business practices used to prevent duplicate bookings, and what external systems this system may need to integrate with.

# Part B - Build a Human-Written Prototype

# Task 1: Basic Input/Output and Sequence Structure
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name: str = 'Alice Smith'
practitioner1_name: str = 'Dr. John Doe'
appointment1_time: str = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name: str = 'Bob Johnson'
practitioner2_name: str = 'Dr. Jane Roe'
appointment2_time: str = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

# Task 1 Enhanced: Data Structures and Functions
appointments: list[dict[str, str]] = []


def book_appointment(patient_name: str, practitioner_name: str, appointment_time: str) -> None:
    # 1. Input Validation
    if not patient_name or not patient_name.strip():
        raise ValueError("Patient name cannot be empty.")

    if not practitioner_name or not practitioner_name.strip():
        raise ValueError("Practitioner name cannot be empty.")

    if not appointment_time or not appointment_time.strip():
        raise ValueError("Appointment time cannot be empty.")

    # 2. Conflict Detection
    for existing_appointment in appointments:
        if (existing_appointment["practitioner"] == practitioner_name and
                existing_appointment["time"] == appointment_time):
            print(f"Error: {practitioner_name} is already booked at {appointment_time}.")
            return

    # 3. Store valid booking if no conflict is found
    appointment: dict[str, str] = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)
    print(f"Success: Appointment booked for {patient_name} with {practitioner_name} at {appointment_time}.")


def display_appointments() -> None:
    if not appointments:
        print("No appointments recorded.")
        return

    print("\n--- Current Appointments ---")
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")


# Main Execution Flow
print("\nWelcome to SmartCare: Community Clinic Appointment Booking System! (Enhanced Version)")

# 1. Normal Bookings
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')

# 2. Testing Blank Patient Name Error Handling
print("\n--- Testing Blank Patient Input ---")
try:
    book_appointment('', 'Dr. John Doe', '2024-07-20 01:00 PM')
except ValueError as e:
    print(f"Caught Expected Error: {e}")

# 3. Testing Conflict Detection
print("\n--- Testing Practitioner Conflict ---")
book_appointment('Charlie Brown', 'Dr. John Doe', '2024-07-20 10:00 AM')

# Display stored records
display_appointments()

# 5 Limitations (previous to AI suggested changes update):

# 1. All appointment data is kept in appointments = []. Meaning as soon as the script finishes running, all saved appointments are lost.

# 2. The program does not check whether a practitioner is simultaneously booked for a specific date and time which may overlap with the new appointment.

# 3. The program uses no interactive inputs, and instead relies entirely on hardcoded values in the function calls rather than using input() to prompt the receptionist.

# 4. The program only implements the functions of creating and reading appointments, leaving out the ability to modify or cancel existing appointments if needed.

# 5. The program uses independent variables for every single appointment, which causes code duplication and creates a maintainability issue when scaling the program up to fit more appointments.

# Part F - Verify Behaviour

# Normal appointment:
# Worked correctly, it created the booking and displayed it without issues.

# Blank patient name:
# Raised a ValueError with the message "Patient name cannot be empty.", stopping the booking.

# Two appointments for the same practitioner/time:
# Detected the schedule conflict and printed an error message, blocking the second booking.

# Strange input such as patient_name=None or appointment_time=None:
# Triggered an error when checking .strip(), keeping the value out of the system.

# Part G - Improve One Thing

# Added a check for practitioner time slot conflicts to ensure no double bookings occur:

# for existing_appointment in appointments:
    # if (existing_appointment["practitioner"] == practitioner_name and
            # existing_appointment["time"] == appointment_time):
        # print(f"Error: {practitioner_name} is already booked at {appointment_time}.")
        # return