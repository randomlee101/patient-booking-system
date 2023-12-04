import string
from . import Patient


class MedicalRecord:
    def __init__(self, recordID: int, patient: Patient, data: string):
        self.recordID = recordID
        self.patient = patient
        self.data = data

    def updateRecord(self, data):
        self.data = data
