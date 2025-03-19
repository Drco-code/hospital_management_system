# Hospital Management System

This is a Hospital Management System built with Django and Django REST framework. It provides functionalities to manage appointments, billing, departments, doctors, medical history, medication, notifications, patients, **prescriptions**, staff, and users.

## Table of Contents

- [Hospital Management System](#hospital-management-system)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running Tests](#running-tests)

---

## Introduction

The Hospital Management System is designed to streamline hospital operations, improve patient care, and enhance the overall healthcare experience. This system provides a robust and scalable platform for managing patient data, scheduling appointments, tracking billing and insurance, and more.

---

## Features

- **Patient Management**: Create, edit, and manage patient profiles, including demographic information, medical history, and insurance details.
- **Appointment Scheduling**: Schedule appointments for patients with doctors and other healthcare professionals.
- **Billing and Insurance**: Manage billing and insurance claims for patients, including payment tracking and insurance verification.
- **Doctor and Staff Management**: Create, edit, and manage doctor and staff profiles, including their schedules, specialties, and contact information.
- **Department Management**: Create, edit, and manage hospital departments, including their descriptions, contact information, and staff assignments.
- **Notification System**: Send notifications to patients, doctors, and staff about appointments, billing, and other important events.
- **Reporting and Analytics**: Generate reports and analytics on patient data, appointment schedules, billing, and other key metrics.

---

## Setup Instructions

### Prerequisites

- **Python**: 3.x
- **pip**: Python package installer
- **virtualenv**: Optional but recommended for creating isolated environments.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Drco-code/hospital_management_system.git
    cd hospital_management_system
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Populate initial data (if applicable):**

    ```bash
    python populate_data.py
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

### Running Tests

To run tests, use the following command:

```bash
python manage.py test

