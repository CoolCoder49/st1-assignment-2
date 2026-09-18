class Patient:
    def __init__(self, patient_id: str, name: str) -> None:
        # Reject blank strings or whitespace for patient names
        if not name or not name.strip():
            raise ValueError("Patient name cannot be empty.")
        self.patient_id: str = patient_id
        self.name: str = name.strip()


class Practitioner:
    def __init__(self, practitioner_id: str, name: str) -> None:
        # Enforce data integrity before allowing the object to be created
        if not name or not name.strip():
            raise ValueError("Practitioner name cannot be empty.")
        self.practitioner_id: str = practitioner_id
        self.name: str = name.strip()


class Appointment:
    def __init__(self, appointment_id: str, patient: Patient, practitioner: Practitioner, time: str) -> None:
        # Validate that the appointment time is provided
        if not time or not time.strip():
            raise ValueError("Appointment time cannot be empty.")

        self.appointment_id: str = appointment_id
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.time: str = time.strip()
        # Track status natively inside the class
        self.status: str = "Active"

    def cancel(self) -> None:
        # Update state without deleting the record from memory
        self.status = "Cancelled"


if __name__ == "__main__":
    print("--- Testing SmartCare Domain Model ---")

    # 1. Create Core Entities
    patient_1 = Patient(patient_id="P001", name="John Doe")
    doc_1 = Practitioner(practitioner_id="D001", name="Dr. Sarah Connor")

    print(f"Patient Created: {patient_1.patient_id} - {patient_1.name}")
    print(f"Practitioner Created: {doc_1.practitioner_id} - {doc_1.name}")

    # 2. Create Appointment
    appt_1 = Appointment(
        appointment_id="A101",
        patient=patient_1,
        practitioner=doc_1,
        time="2026-10-05 09:00 AM"
    )
    print(f"Appointment Status: {appt_1.status}")

    # 3. Test Cancel Behavior
    appt_1.cancel()
    print(f"Updated Appointment Status: {appt_1.status}")

    # 4. Test Defensive Input Validation
    try:
        invalid_patient = Patient(patient_id="P002", name="   ")
    except ValueError as err:
        print(f"Validation Guard Check Passed: {err}")