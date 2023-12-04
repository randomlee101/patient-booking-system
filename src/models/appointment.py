import string
from . import Patient, Doctor


class Appointment:
    def __init__(self, appointment_id: int, patient: Patient, time: string, reason: string, doctor: Doctor):
        self.appointment_id = appointment_id
        self.patient = patient
        self.time = time
        self.reason = reason
        self.doctor = doctor

    def schedule(self):
        pass

    def reschedule(self, time):
        self.time = time
        self.schedule()

    def cancel(self):
        pass

    def view(self):
        print(
            f'Appointment: {self.appointment_id}, Date: {self.time} for Patient: {self.patient} with Doctor: {self.doctor} for Reason: {self.reason}')
