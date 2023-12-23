# Patient Booking System


    UserModel

 - user_id: int     
 - username: str    
 - password: str    
 - role: str        
-------------------
 + login(username, 
     password):    
 + register():     
 + updateProfile():
 + __str__():      
 + __repr__():     


      UserList     

 - currentUser:UserModel       
 - users: List[UserModel]      
-------------------
 + addUser(user:   
   UserModel):    
 + countUsers():    
 + viewAllUsers():  
 + findUserByUserName()


      Doctor       

                   
 + setAvailability()
 + viewAvailability()
 + cancelAvailability()
 + viewMedicalRecords()
 + viewAssignedAppointments()
 + viewAssignedPatients()
 + updatePatientRecord()


      Patient     

                  
 + bookAppointment
 + manageAppointment
 + viewMedicalRecords()
 + viewAppointments()


    Receptionist       

 + checkDoctorAvailability()            
 + bookAppointment()    
 + manageAppointment()  
 + assignPatientToDoctor


    SystemAdministrator    

 + userManagement()     
 + manageMedicalHistoryTracking()           
 + manageMedicalRecord()
 + manageAppointments()  


     MedicalRecord    

 - recordID: int      
 - patient: Patient   
 - data: string  
----------------------
 + updateRecord(data) 


      Appointment     

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



