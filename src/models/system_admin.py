from . import UserModel, Appointment, MedicalRecord


class SystemAdministrator(UserModel, Appointment, MedicalRecord):
    pass

    def userManagement(self):
        pass

    def manageMedicalHistoryTracking(self):
        pass

    def manageMedicalRecord(self):
        pass

    def manageAppointments(self, action):
        pass

