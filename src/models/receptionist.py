from . import UserModel, Appointment


class Receptionist(UserModel, Appointment):
    pass

    def checkDoctorAvailability(self):
        pass

    def bookAppointment(self):
        pass

    def manageAppointment(self, action):
        pass

    def assignPatientToDoctor(self):
        pass


