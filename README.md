# INTERN ID : CITS3033
# NAME : VINISHA S
# NO.OF.WEEKS : 4 WEEKS

# PROJECT TITLE : Endpoint Detection & Response (EDR) Build

## Project Overview

Endpoint Detection & Response (EDR) Build is a cybersecurity monitoring application developed using Python. The project continuously monitors endpoint activities, detects suspicious behavior based on predefined rules, records security events, and displays threat information through an interactive dashboard.

The goal of this project is to demonstrate the core concepts of endpoint security, threat detection, event logging, and incident monitoring.

## Features

### Process Monitoring

* Monitors running processes on the endpoint.
* Detects blacklisted or suspicious processes.

### File Monitoring

* Tracks file creation, modification, and deletion events.
* Generates alerts for suspicious file activities.

### Threat Detection

* Uses predefined detection rules.
* Identifies potentially malicious activities.

### Alert Logging

* Stores detected threats in a SQLite database.
* Maintains historical records for analysis.

### Dashboard Visualization

* Displays detected threats.
* Shows threat statistics and severity levels.
* Provides a centralized monitoring interface.

---

## Technology Stack

* Python
* Streamlit
* SQLite
* Watchdog
* Psutil
* Pandas
* Plotly

---

## Project Structure

EDR_Project/

├── detector.py

├── file_monitor.py

├── dashboard.py

├── database.py

├── generate_alerts.py

├── alerts.db

└── README.md

---

## Installation

### Clone the Repository

git clone <repository-url>

cd EDR_Project

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install psutil watchdog streamlit pandas plotly



## Running the Project

### Initialize Database

python database.py

### Start Process Monitoring

python detector.py

### Start File Monitoring

python file_monitor.py

### Launch Dashboard

streamlit run dashboard.py



## Dashboard Features

* Threat Count
* Alert History
* Severity Classification
* Threat Visualization
* Real-Time Monitoring Display


## Future Enhancements

* Machine Learning Based Detection
* Email Alerting System
* Threat Intelligence Integration
* User Authentication
* Real-Time Notifications
* Network Traffic Monitoring
