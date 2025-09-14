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
        return [str(p) for p in self.queue]


class Hospital:
    def __init__(self):
        self.doctors = {}
        self.patients = {}  

    def add_doctor(self, name, specialization):
        if name in self.doctors:
            print(f"Doctor {name} already exists.")
            return
        doctor = Doctor(name, specialization)
        self.doctors[name] = doctor
        print(f"Doctor {name} added.")

    def add_patient(self, name, age, disease):
        if name in self.patients:
            print(f"Patient {name} already exists.")
            return
        patient = Patient(name, age, disease)
        self.patients[name] = patient 
        print(f"Patient {name} added.")

    def assign_patient(self, patient_name, doctor_name):
        patient = self.patients.get(patient_name)
        if not patient:
            print("Patient not found!")
            return
        doctor = self.doctors.get(doctor_name)
        if not doctor:
            print("Doctor not found!")
            return
        doctor.add_patient(patient)
        print(f"Assigned {patient_name} to Dr. {doctor_name}")

    def search_patient(self, name):
        return self.patients.get(name, "Patient not found")

    def show_doctor_patients(self, doctor_name):
        doctor = self.doctors.get(doctor_name)
        if not doctor:
            return "Doctor not found"
        return doctor.show_patients()


def main():
    hospital = Hospital()

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Assign Patient to Doctor")
        print("4. Show Patients of a Doctor")
        print("5. Search Patient")
        print("6. Get Next Patient for a Doctor")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter doctor's name: ")
            specialization = input("Enter specialization: ")
            hospital.add_doctor(name, specialization)

        elif choice == "2":
            name = input("Enter patient's name: ")
            age = int(input("Enter age: "))
            disease = input("Enter disease: ")
            hospital.add_patient(name, age, disease)

        elif choice == "3":
            patient_name = input("Enter patient name: ")
            doctor_name = input("Enter doctor name: ")
            hospital.assign_patient(patient_name, doctor_name)

        elif choice == "4":
            doctor_name = input("Enter doctor name: ")
            patients = hospital.show_doctor_patients(doctor_name)
            if isinstance(patients, str):
                print(patients)
            else:
                if not patients:
                    print("No patients assigned.")
                else:
                    print("\n".join(patients))

        elif choice == "5":
            name = input("Enter patient name: ")
            patient = hospital.search_patient(name)
            print(patient)

        elif choice == "6":
            doctor_name = input("Enter doctor name: ")
            doctor = hospital.doctors.get(doctor_name)
            if not doctor:
                print("Doctor not found")
            else:
                print(doctor.next_patient())

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()