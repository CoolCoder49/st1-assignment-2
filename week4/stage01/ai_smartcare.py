# Part D - Generate an Alternative

# A simple in‑memory list to store appointments
appointments = []

def book_appointment(patient_name: str, practitioner_name: str, appointment_time: str):
    """Store a basic appointment using only Python variables and a list."""
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)
    print("Appointment booked successfully!")

# Example usage
book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

print(appointments)
