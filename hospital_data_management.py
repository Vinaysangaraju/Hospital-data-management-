from collections import deque
class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __str__(self):
        return f"Patient: {self.name}, Age: {self.age}, Disease: {self.disease}"
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.queue = deque()  # Queue for patients

    def add_patient(self, patient):
        self.queue.append(patient)

    def next_patient(self):
        if self.queue:
            return self.queue.popleft()
        return "No patients in queue"

    def show_patients(self):
        return list(self.queue)
class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = {}  # Dictionary for quick lookup

    def add_doctor(self, name, specialization):
        doctor = Doctor(name, specialization)
        self.doctors.append(doctor)
        print(f"Doctor {name} added.")

    def add_patient(self, name, age, disease):
        patient = Patient(name, age, disease)
        self.patients[name] = patient  # store in hash map
        print(f"Patient {name} added.")

    def assign_patient(self, patient_name, doctor_name):
        patient = self.patients.get(patient_name)
        if not patient:
            print("Patient not found!")
            return
        for doc in self.doctors:
            if doc.name == doctor_name:
                doc.add_patient(patient)
                print(f"Assigned {patient_name} to Dr. {doctor_name}")
                return
        print("Doctor not found!")

    def search_patient(self, name):
        return self.patients.get(name, "Patient not found")

    def show_doctor_patients(self, doctor_name):
        for doc in self.doctors:
            if doc.name == doctor_name:
                return doc.show_patients()
        return "Doctor not found"
