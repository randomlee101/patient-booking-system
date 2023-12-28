import string
from . import Patient


class MedicalRecord:
    def __init__(self, recordID: int, patient: Patient, data: [string]):
        self.recordID = recordID
        self.patient = patient
        self.data = data

    def createRecord(self):
        pass

    def updateRecord(self, patient: Patient, data):
        self.data = self.data.add(data)

    def viewRecord(self, patient: Patient):
        pass
