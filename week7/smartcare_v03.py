import os
from enum import Enum

class AppointmentStatus(Enum):
    ACTIVE = "Active"
    CANCELLED = "Cancelled"


# DOMAIN ENTITIES


class Patient:

  def __init__(self, patient_id: str, name: str) -> None:
    if not name or not name.strip():
      raise ValueError("Patient name cannot be empty.")
    self.patient_id: str = patient_id
    self.name: str = name.strip()


class Practitioner:

  def __init__(self, practitioner_id: str, name: str) -> None:
    if not name or not name.strip():
      raise ValueError("Practitioner name cannot be empty.")
    self.practitioner_id: str = practitioner_id
    self.name: str = name.strip()


class Appointment:
  def __init__(self, appointment_id: str, patient: Patient, practitioner: Practitioner, time: str) -> None:
    if not time or not time.strip():
      raise ValueError("Appointment time cannot be empty.")

    self.appointment_id: str = appointment_id
    self.patient: Patient = patient
    self.practitioner: Practitioner = practitioner
    self.time: str = time.strip()
    self.status: AppointmentStatus = AppointmentStatus.ACTIVE

  def cancel(self) -> None:
    # Update state to cancelled without deleting the record from memory
    if self.status == AppointmentStatus.CANCELLED:
      print("Notice: Appointment is already cancelled.")
      return
    self.status = AppointmentStatus.CANCELLED

  def conflicts_with(self, practitioner_name: str, time: str) -> bool:
    # Assign responsibility to Appointment slot validation to prevent double-booking
    return (
            self.practitioner.name == practitioner_name
            and self.time == time
            and self.status == AppointmentStatus.ACTIVE
    )


# SYSTEM STATE


appointments: list[Appointment] = []
STORAGE_FILE: str = "appointments.csv"


# FILE SAVING/LOADING


def save_appointments() -> None:
  with open(STORAGE_FILE, "w") as file:
    file.write("AppointmentID,PatientName,PractitionerName,Time,Status\n")
    for appt in appointments:
      file.write(
          f"{appt.appointment_id},{appt.patient.name},{appt.practitioner.name},{appt.time},{appt.status.value}\n"
      )


def load_appointments() -> None:
  # Load saved appointments from the file back into memory
  if not os.path.exists(STORAGE_FILE):
    return

  try:
    with open(STORAGE_FILE, "r") as file:
      lines = file.readlines()
      if not lines:
        return

      # Skip the header row and process further records
      for line in lines[1:]:
        cleaned_line = line.strip()
        if not cleaned_line:
          continue

        parts = cleaned_line.split(",")
        if len(parts) == 5:
          appt_id, patient_name, practitioner_name, appt_time, status = parts

          patient = Patient(
              patient_id=f"P00{len(appointments) + 1}", name=patient_name
          )
          practitioner = Practitioner(
              practitioner_id=f"PR00{len(appointments) + 1}", name=practitioner_name
          )
          appt = Appointment(
              appointment_id=appt_id,
              patient=patient,
              practitioner=practitioner,
              time=appt_time,
          )

          # Use the enum value to check the loaded string, then assign the enum object
          if status == AppointmentStatus.CANCELLED.value:
            appt.status = AppointmentStatus.CANCELLED

          appointments.append(appt)

    print(f"Loaded {len(appointments)} record(s) from appointments.csv.")
  except FileNotFoundError:
    pass
  except Exception as e:
    print(f"Warning: Could not load stored records: {e}")


# CORE FUNCTIONS


def book_appointment(
    patient_name: str, practitioner_name: str, appointment_time: str
) -> None:
  # Use the appointment's built-in check to prevent double bookings
  for existing_appointment in appointments:
    if existing_appointment.conflicts_with(practitioner_name, appointment_time):
      print(
          f"Error: {practitioner_name} is already booked at"
          f" {appointment_time}."
      )
      return

  try:
    patient_id: str = f"P00{len(appointments) + 1}"
    practitioner_id: str = f"PR00{len(appointments) + 1}"
    appointment_id: str = f"A10{len(appointments) + 1}"

    new_patient = Patient(patient_id=patient_id, name=patient_name)
    new_practitioner = Practitioner(
        practitioner_id=practitioner_id, name=practitioner_name
    )

    new_appointment = Appointment(
        appointment_id=appointment_id,
        patient=new_patient,
        practitioner=new_practitioner,
        time=appointment_time,
    )

    appointments.append(new_appointment)
    save_appointments()
    print(
        f"Success: Appointment booked for {new_patient.name} with"
        f" {new_practitioner.name} at {new_appointment.time}."
    )

  except ValueError as e:
    print(f"Booking failed: {e}")


def display_appointments() -> None:
  if not appointments:
    print("No appointments recorded.")
    return

  print("\nCurrent Appointments:")
  for appointment in appointments:
    print(
        f"ID: {appointment.appointment_id} | Patient: {appointment.patient.name}"
        f" | Practitioner: {appointment.practitioner.name} | Time:"
        f" {appointment.time} | Status: {appointment.status.value}"
    )


def get_valid_input(prompt: str) -> str:
  while True:
    user_input: str = input(prompt)
    if user_input.strip():
      return user_input.strip()
    print("Invalid input. Field cannot be empty.")


# MAIN EXECUTION FLOW

if __name__ == "__main__":
  print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

  # Automatically load saved data on startup
  load_appointments()

  while True:
    print("\nMain Menu:")
    print("1. Book an Appointment")
    print("2. Display Appointments")
    print("3. Cancel an Appointment")
    print("4. Exit")

    choice: str = input("Select an option (1-4): ").strip()

    if choice == "1":
      print("\n--- Book Appointment ---")
      patient_name: str = get_valid_input("Enter patient name: ")
      practitioner_name: str = get_valid_input("Enter practitioner name: ")
      appointment_time: str = get_valid_input(
          "Enter appointment time (e.g., 2024-07-20 10:00 AM): "
      )
      book_appointment(patient_name, practitioner_name, appointment_time)

    elif choice == "2":
      display_appointments()

    elif choice == "3":
      print("\n--- Cancel Appointment ---")
      if not appointments:
        print("No appointments available to cancel.")
        continue

      appointment_id: str = get_valid_input("Enter the Appointment ID to cancel: ")
      found: bool = False

      for appt in appointments:
        if appt.appointment_id == appointment_id:
          appt.cancel()
          save_appointments()
          print(f"Appointment {appointment_id} has been cancelled.")
          found = True
          break

      if not found:
        print(f"Error: Appointment ID '{appointment_id}' not found.")

    elif choice == "4":
      print("Exiting SmartCare. Goodbye!")
      break

    else:
      print("Invalid selection. Please enter a number between 1 and 4.")