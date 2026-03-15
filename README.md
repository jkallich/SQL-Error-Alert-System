# SQL Error Alert System (SEAS)

---

Ever ran a SQL script and wished that you were graced with alerts better presented than what you see in your Workbench? Well, this system is exactly what you need!

---

> __CURRENT STATUS: IN PROGRESS__ <br>
> _The current content in this README are representative of what SEAS_ will _be when it is completed, but has not yet achieved it all._ 

---

## Table of Contents

[//]: # (- [Highlights]&#40;#Highlights&#41;)
- [Description](#Description)
- [Version 1 [CURRENT]](#Version 1)

## Description
Using Python, SEAS connects to a database that the user specifies, and runs SQL scripts that the user would like to run. If the script runs without error, then SEAS concludes its responsbilities with a printed notification that everything ran smoothly. If an error arises in the script, SEAS alerts the user of the error by alerting the user with information on the error through a format decided by the user.

[//]: # (## Highlights)

[//]: # (> What can you expect from this Markdown??)

[//]: # ()
[//]: # (- [x] A  description of what each version of SEAS does)

[//]: # (- [x] An explanation of how to utilize of SEAS)

[//]: # (- [x] Future plans for SEAS)

[//]: # (- [x] Any important updates on SEAS)

## Version 1 

> **CURRENT VERSION**

### Description
This version emails alerts to the user.

### Structure

#### SEAS' File Directory
> How is SEAS organized, and what purpose does each component serve? 

```
SQL_Error_Alert_System
│
├── main.py
│
├── config/
│   ├── __init__.py
│   ├── database_info.py
│   ├── 
│   └── load_env.py
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── sql_executor.py
│
├── alerts/
│   ├── __init__.py
│   ├── alert_manager.py
│   └── email_alert.py
│
├── monitoring/
│   ├── __init__.py
│   └── error_detector.py
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── error_formatter.py
│
├── sql/
│   └── job.sql
│
├── logs/
│   └── error.log
│
└── requirements.txt
```