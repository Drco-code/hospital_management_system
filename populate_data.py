import os
import django
from datetime import datetime
import uuid
from datetime import date

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hospital_management_system.settings")
django.setup()

# Import models
from users.models import User
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Billing
from medication.models import Medication
from prescription.models import Prescription
from notification.models import Notification
from department.models import Department
from staff.models import Staff

def create_sample_data():
    # Create some users (patients, doctors, admin)
    admin_user = User.objects.create(username="admin", user_role="AD", password="test")
    doctor_user = User.objects.create(username="doctor1", user_role="DO", password="test")
    patient_user = User.objects.create(username="patient1", user_role="PA", password="test")
    User.objects.create(username="patient2", user_role="PA", password="test")
    User.objects.create(username="patient3", user_role="PA", password="test")
    User.objects.create(username="patient4", user_role="PA", password="test")
    User.objects.create(username="patient5", user_role="PA", password="test")
    User.objects.create(username="patient6", user_role="PA", password="test")
    User.objects.create(username="patient7", user_role="PA", password="test")
    User.objects.create(username="patient8", user_role="PA", password="test")
    User.objects.create(username="patient9", user_role="PA", password="test")
    User.objects.create(username="patient10", user_role="PA", password="test")
    User.objects.create(username="doctor2", user_role="DO", password="test")
    User.objects.create(username="doctor3", user_role="DO", password="test")
    User.objects.create(username="doctor4", user_role="DO", password="test")
    User.objects.create(username="doctor5", user_role="DO", password="test")

    # Create patients
    patient1 = Patient.objects.create(
        user=patient_user,
        first_name="Sophia",
        last_name="Miller",
        dob=datetime(1990, 5, 15),
        address="123 Main Street, City",
        contact="1234567890",
        email="sophia.miller@example.com",
        emergency_contact="9876543210",
        insurance_number="INS123456",
        blood_group="A+",
        medical_history="No significant medical history."
    )
    
    patient2 = Patient.objects.create(
        user=User.objects.get(username="patient2"),
        first_name="Olivia",
        last_name="Davis",
        dob=datetime(1992, 8, 20),
        address="456 Elm Street, City",
        contact="1234567891",
        email="olivia.davis@example.com",
        emergency_contact="9876543211",
        insurance_number="INS123457",
        blood_group="B+",
        medical_history="Asthma."
    )
    
    patient3 = Patient.objects.create(
        user=User.objects.get(username="patient3"),
        first_name="Isabella",
        last_name="Garcia",
        dob=datetime(1985, 2, 15),
        address="789 Oak Street, City",
        contact="1234567892",
        email="isabella.garcia@example.com",
        emergency_contact="9876543212",
        insurance_number="INS123458",
        blood_group="O+",
        medical_history="No significant medical history."
    )
    
    patient4 = Patient.objects.create(
        user=User.objects.get(username="patient4"),
        first_name="Liam",
        last_name="Jones",
        dob=datetime(1988, 4, 10),
        address="101 Pine Street, City",
        contact="1234567893",
        email="liam.jones@example.com",
        emergency_contact="9876543213",
        insurance_number="INS123459",
        blood_group="AB+",
        medical_history="High blood pressure."
    )
    
    patient5 = Patient.objects.create(
        user=User.objects.get(username="patient5"),
        first_name="Mason",
        last_name="Rodriguez",
        dob=datetime(1994, 7, 25),
        address="102 Maple Avenue, City",
        contact="1234567894",
        email="mason.rodriguez@example.com",
        emergency_contact="9876543214",
        insurance_number="INS123460",
        blood_group="A-",
        medical_history="No significant medical history."
    )
    
    patient6 = Patient.objects.create(
        user=User.objects.get(username="patient6"),
        first_name="Avery",
        last_name="Martinez",
        dob=datetime(1993, 1, 3),
        address="120 Cedar Road, City",
        contact="1234567895",
        email="avery.martinez@example.com",
        emergency_contact="9876543215",
        insurance_number="INS123461",
        blood_group="B-",
        medical_history="Mild diabetes."
    )
    
    patient7 = Patient.objects.create(
        user=User.objects.get(username="patient7"),
        first_name="Jackson",
        last_name="Hernandez",
        dob=datetime(1986, 12, 5),
        address="56 Birch Lane, City",
        contact="1234567896",
        email="jackson.hernandez@example.com",
        emergency_contact="9876543216",
        insurance_number="INS123462",
        blood_group="O-",
        medical_history="No significant medical history."
    )
    
    patient8 = Patient.objects.create(
        user=User.objects.get(username="patient8"),
        first_name="Charlotte",
        last_name="Lopez",
        dob=datetime(1991, 9, 16),
        address="78 Pine Avenue, City",
        contact="1234567897",
        email="charlotte.lopez@example.com",
        emergency_contact="9876543217",
        insurance_number="INS123463",
        blood_group="AB-",
        medical_history="Migraines."
    )
    
    patient9 = Patient.objects.create(
        user=User.objects.get(username="patient9"),
        first_name="Amelia",
        last_name="Gonzalez",
        dob=datetime(1992, 4, 8),
        address="150 Oak Drive, City",
        contact="1234567898",
        email="amelia.gonzalez@example.com",
        emergency_contact="9876543218",
        insurance_number="INS123464",
        blood_group="O+",
        medical_history="Anxiety."
    )
    
    patient10 = Patient.objects.create(
        user=User.objects.get(username="patient10"),
        first_name="Benjamin",
        last_name="Wilson",
        dob=datetime(1987, 6, 30),
        address="29 Maple Street, City",
        contact="1234567899",
        email="benjamin.wilson@example.com",
        emergency_contact="9876543219",
        insurance_number="INS123465",
        blood_group="A+",
        medical_history="No significant medical history."
    )

    # Create doctors - Save all as variables
    doctor1 = Doctor.objects.create(
        user=doctor_user,
        first_name="Dr. Ava",
        last_name="Brown",
        specialization="Cardiologist",
        qualification="MD",
        contact="0987654321",
        email="ava.brown@hospital.com",
        availability={"Monday": "9:00 AM - 5:00 PM", "Tuesday": "9:00 AM - 5:00 PM"}
    )
    
    doctor2 = Doctor.objects.create(
        user=User.objects.get(username="doctor2"),
        first_name="Dr. Ethan",
        last_name="Clark",
        specialization="Neurologist",
        qualification="MD",
        contact="0987654322",
        email="ethan.clark@hospital.com",
        availability={"Wednesday": "9:00 AM - 5:00 PM", "Thursday": "9:00 AM - 5:00 PM"}
    )
    
    doctor3 = Doctor.objects.create(
        user=User.objects.get(username="doctor3"),
        first_name="Dr. Olivia",
        last_name="Martinez",
        specialization="Pediatrician",
        qualification="MD",
        contact="0987654323",
        email="olivia.martinez@hospital.com",
        availability={"Monday": "9:00 AM - 5:00 PM", "Friday": "9:00 AM - 5:00 PM"}
    )
    
    doctor4 = Doctor.objects.create(
        user=User.objects.get(username="doctor4"),
        first_name="Dr. James",
        last_name="Lopez",
        specialization="Dermatologist",
        qualification="MD",
        contact="0987654324",
        email="james.lopez@hospital.com",
        availability={"Tuesday": "9:00 AM - 5:00 PM", "Saturday": "9:00 AM - 5:00 PM"}
    )
    
    doctor5 = Doctor.objects.create(
        user=User.objects.get(username="doctor5"),
        first_name="Dr. Emily",
        last_name="Williams",
        specialization="Gynecologist",
        qualification="MD",
        contact="0987654325",
        email="emily.williams@hospital.com",
        availability={"Thursday": "9:00 AM - 5:00 PM", "Sunday": "9:00 AM - 5:00 PM"}
    )

    # Create appointments
    appointment1 = Appointment.objects.create(
        patient=patient1,
        doctor=doctor1,
        appointment_date=datetime(2025, 3, 15, 14, 30),
        appointment_status="PN",  
        reason_visiting="Routine check-up"
    )
    
    appointment2 = Appointment.objects.create(
        patient=patient2,
        doctor=doctor2,
        appointment_date=datetime(2025, 3, 16, 10, 30),
        appointment_status="PN",
        reason_visiting="Follow-up check-up"
    )
    
    # Add more appointments for other patients
    appointment3 = Appointment.objects.create(
        patient=patient3,
        doctor=doctor3,
        appointment_date=datetime(2025, 3, 17, 11, 0),
        appointment_status="PN",
        reason_visiting="Annual physical"
    )
    
    appointment4 = Appointment.objects.create(
        patient=patient4,
        doctor=doctor4,
        appointment_date=datetime(2025, 3, 18, 14, 0),
        appointment_status="PN",
        reason_visiting="Skin rash examination"
    )
    
    appointment5 = Appointment.objects.create(
        patient=patient5,
        doctor=doctor5,
        appointment_date=datetime(2025, 3, 19, 9, 0),
        appointment_status="PN",
        reason_visiting="Routine check-up"
    )

    # Create billing data
    billing1 = Billing.objects.create(
        patient=patient1,
        appointment=appointment1,
        total_amount=200.00,
        payment_date=datetime(2025, 3, 15, 15, 30)
    )
    
    billing2 = Billing.objects.create(
        patient=patient2,
        appointment=appointment2,
        total_amount=150.00,
        payment_date=datetime(2025, 3, 16, 11, 30)
    )
    
    billing3 = Billing.objects.create(
        patient=patient3,
        appointment=appointment3,
        total_amount=180.00,
        payment_date=datetime(2025, 3, 17, 12, 0)
    )

    # Create medication data
    medication1 = Medication.objects.create(
        name="Aspirin",
        dosage="1 tablet daily",
        frequency="Once a day",
        manufacturer="Pharma Inc.",
        side_effects="Nausea, headache"
    )
    
    medication2 = Medication.objects.create(
        name="Ibuprofen",
        dosage="1 tablet daily",
        frequency="Once a day",
        manufacturer="Pharma Inc.",
        side_effects="Dizziness, stomach upset"
    )
    
    medication3 = Medication.objects.create(
        name="Amoxicillin",
        dosage="500mg",
        frequency="Three times a day",
        manufacturer="MedPharm",
        side_effects="Diarrhea, rash"
    )
    
    medication4 = Medication.objects.create(
        name="Lisinopril",
        dosage="10mg",
        frequency="Once daily",
        manufacturer="HealthMed",
        side_effects="Dry cough, dizziness"
    )

    # Create prescriptions
    prescription1 = Prescription.objects.create(
        appointment=appointment1,
        medication=medication1,
        instruction="Take after meals"
    )
    
    prescription2 = Prescription.objects.create(
        appointment=appointment2,
        medication=medication2,
        instruction="Take with water, avoid alcohol"
    )
    
    prescription3 = Prescription.objects.create(
        appointment=appointment3,
        medication=medication3,
        instruction="Take with food, complete full course"
    )

    # Create notifications
    notification1 = Notification.objects.create(
        user=patient_user,
        message="Your appointment with Dr. Ava Brown is confirmed for March 15, 2025.",
        notification_type="AP",  
        is_read=False
    )
    
    notification2 = Notification.objects.create(
        user=User.objects.get(username="patient2"),
        message="Your appointment with Dr. Ethan Clark is confirmed for March 16, 2025.",
        notification_type="AP",
        is_read=False
    )
    
    notification3 = Notification.objects.create(
        user=User.objects.get(username="patient3"),
        message="Your appointment with Dr. Olivia Martinez is confirmed for March 17, 2025.",
        notification_type="AP",
        is_read=False
    )

    # Create departments
    department1 = Department.objects.create(
        name="Cardiology",
        description="Department specializing in heart-related treatments."
    )
    
    department2 = Department.objects.create(
        name="Neurology",
        description="Department specializing in brain and nervous system treatments."
    )
    
    department3 = Department.objects.create(
        name="Pediatrics",
        description="Department specializing in child healthcare."
    )
    
    department4 = Department.objects.create(
        name="Dermatology",
        description="Department specializing in skin conditions and treatments."
    )
    
    department5 = Department.objects.create(
        name="Gynecology",
        description="Department specializing in women's reproductive health."
    )

    # Create staff members
    staff_member1 = Staff.objects.create(
        user=None,
        first_name="Rachel",
        last_name="Taylor",
        department=department1,
        role="NU",  
        contact="1234567890",
        email="rachel.taylor@hospital.com"
    )
    
    staff_member2 = Staff.objects.create(
        user=None,
        first_name="Daniel",
        last_name="Anderson",
        department=department1,
        role="AD",  
        contact="1234567891",
        email="daniel.anderson@hospital.com"
    )
    
    staff_member3 = Staff.objects.create(
        user=None,
        first_name="Jessica",
        last_name="Roberts",
        department=department2,
        role="NU",  
        contact="1234567892",
        email="jessica.roberts@hospital.com"
    )
    
    staff_member4 = Staff.objects.create(
        user=None,
        first_name="Michael",
        last_name="Johnson",
        department=department3,
        role="RE",  
        contact="1234567893",
        email="michael.johnson@hospital.com"
    )

    patient1 = Patient.objects.get(user__username="patient1")
    patient2 = Patient.objects.get(user__username="patient2")
    patient3 = Patient.objects.get(user__username="patient3")
    patient4 = Patient.objects.get(user__username="patient4")
    patient5 = Patient.objects.get(user__username="patient5")

    # Create medical history records with correct field names
    MedicalHistory.objects.create(
        patient=patient1,
        diagnosis="Hypertension",
        date_of_diagnosis=date(2015, 6, 10),
        notes="Regular blood pressure monitoring advised"
    )

    MedicalHistory.objects.create(
        patient=patient2,
        diagnosis="Asthma",
        date_of_diagnosis=date(2010, 9, 5),
        notes="Albuterol inhaler as needed. Avoid dust and strong odors."
    )

    MedicalHistory.objects.create(
        patient=patient3,
        diagnosis="Diabetes Type 2",
        date_of_diagnosis=date(2018, 3, 15),
        notes="Metformin 500mg twice daily. Follow a low-carb diet and regular exercise."
    )

    MedicalHistory.objects.create(
        patient=patient4,
        diagnosis="Migraines",
        date_of_diagnosis=date(2022, 7, 20),
        notes="Ibuprofen 400mg as needed. Avoid caffeine and excessive screen time."
    )

    MedicalHistory.objects.create(
        patient=patient5,
        diagnosis="Anxiety",
        date_of_diagnosis=date(2021, 11, 2),
        notes="Cognitive behavioral therapy recommended. Fluoxetine 20mg daily. Practice mindfulness."
    )

    print("Sample data has been created successfully.")

if __name__ == "__main__":
    create_sample_data()