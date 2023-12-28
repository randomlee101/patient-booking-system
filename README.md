# Patient Booking System


## UserModel

 - user_id: int     
 - username: str    
 - password: str    
 - role: str        
-------------------
 + login(username, password):    
 + register():     
 + updateProfile():
 + __str__():      
 + __repr__():     

## UserList     

 - currentUser:UserModel       
 - users: List[UserModel]      
-------------------
 + addUser(user:UserModel)   
 + countUsers()  
 + viewAllUsers() 
 + findUserByUserName()


##  Doctor
 + setAvailability()
 + viewAvailability()
 + cancelAvailability()
 + viewMedicalRecords()
 + viewAssignedAppointments()
 + viewAssignedPatients()
 + updatePatientRecord(patient:Patient)

## Patient     

                  
 + bookAppointment()
 + manageAppointment()


## Receptionist       

 + checkDoctorAvailability()            
 + bookAppointment()    
 + manageAppointment(action: string)  
 + assignPatientToDoctor


## SystemAdministrator    

 + userManagement()     
 + manageMedicalHistoryTracking()           
 + manageMedicalRecord()
 + manageAppointments(action: string)  


## MedicalRecord    

 - recordID: int      
 - patient: Patient   
 - data: [string]  
----------------------
 + updateRecord(patient: Patient,data: string) 
 + createRecord()
 + viewRecord(patient: Patient)


## Appointment     

 - appointment_id: int
 - patient: Patient   
 - time: string       
 - reason: string     
 - doctor: Doctor    
------------------------------
 + schedule()         
 + reschedule(time)   
 + cancel()           
 + view()             



