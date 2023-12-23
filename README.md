Class Diagram Revision

+-------------------+          +-------------------+            +-------------------+
|     UserModel     |          |      UserList     |            |      Doctor       |
+-------------------+          +-------------------+            +-------------------+
| - user_id: int     |          | - currentUser:    |            |                   |
| - username: str    |   1      |   UserModel       |            |                   |
| - password: str    |---------<| - users: List[     |            |                   |
| - role: str        |          |   UserModel]      |            |                   |
|-------------------|          |-------------------|            |                   |
| + login(username, |          | + addUser(user:   |            |                   |
|     password):    |          |     UserModel):    |            | + setAvailability()|
| + register():     |          | + countUsers():    |            | + viewAvailability()|
| + updateProfile():|          | + viewAllUsers():  |            | + cancelAvailability()|
| + __str__():      |          | + findUserByUserName()         | + viewMedicalRecords()|
| + __repr__():     |          |-------------------|            | + viewAssignedAppointments()|
|                   |          |                                   | + viewAssignedPatients()|
+-------------------+          +-------------------+            | + updatePatientRecord()|
                                   ^                               +-------------------+
                                   |
+------------------------+ +------------------------+             +----------------------+
|    Receptionist       | | SystemAdministrator    |             |     MedicalRecord    |
+------------------------+ +------------------------+             +----------------------+
|                        | |                        |             | - recordID: int      |
| + checkDoctorAvaila-  | | + userManagement()     |             | - patient: Patient   |
|   bility()            | | + manageMedicalHistory-|             | - data: string       |
| + bookAppointment()    | |   Tracking()           |             |                      |
| + manageAppointment()  | | + manageMedicalRecord()|             | + updateRecord(data) |
| + assignPatientToDoctor| | + manageAppointments()  |             +----------------------+
+------------------------+ +------------------------+
                                   ^
                                   |
+--------------------------+      +--------------------------+
|        Patient           |      |        Doctor            |
+--------------------------+      +--------------------------+
|                          |      |                          |
| + bookAppointment()      |      | + setAvailability()      |
| + manageAppointment()    |      | + viewAvailability()     |
| + viewMedicalRecords()   |      | + cancelAvailability()   |
| + viewAppointments()     |      | + viewMedicalRecords()   |
+--------------------------+      | + viewAssignedAppointments|
                                   | + viewAssignedPatients() |
                                   | + updatePatientRecord()  |
                                   +--------------------------+
                                                    ^
                                                    |
                                            +----------------------+
                                            |      Appointment     |
                                            +----------------------+
                                            | - appointment_id: int|
                                            | - patient: Patient   |
                                            | - time: string       |
                                            | - reason: string     |
                                            | - doctor: Doctor     |
                                            +----------------------+
                                            | + schedule()         |
                                            | + reschedule(time)   |
                                            | + cancel()           |
                                            | + view()             |
                                            +----------------------+
