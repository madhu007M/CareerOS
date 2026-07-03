# Software Requirements Specification (SRS)

# CareerOS

Version: 1.0

Author: Madhu U S

---

# 1. Introduction

## 1.1 Purpose

CareerOS is an AI-powered Career Operating System designed to automate and streamline the entire job and internship application lifecycle.

The system searches multiple job platforms, analyzes job descriptions, ranks opportunities based on the user's profile, generates tailored resumes and cover letters, automates application workflows where appropriate, tracks application progress, and provides analytics through a web dashboard.

---

## 1.2 Goals

The primary goals of CareerOS are:

- Reduce the manual effort involved in job searching.
- Support multiple job platforms.
- Generate AI-assisted resumes.
- Generate AI-assisted cover letters.
- Track every application.
- Provide a centralized dashboard.
- Notify users about new opportunities.
- Prepare users for interviews.

---

## 1.3 Target Users

- Students
- Fresh Graduates
- Working Professionals
- Career Switchers

---

## 1.4 Supported Platforms (Version 1)

Internship Platforms

- Internshala
- Unstop
- Wellfound

Job Platforms

- LinkedIn
- Naukri
- Foundit
- Indeed
- Google Jobs

Company Career Pages

- Google
- Microsoft
- Amazon
- Cisco
- IBM
- Intel
- Oracle
- Adobe
- SAP
- Accenture
- Infosys
- Wipro
- TCS
---

# 2. System Architecture

CareerOS follows a modular architecture.

Each module has one responsibility and communicates with other modules through well-defined interfaces.

## 2.1 High-Level Architecture

```
                        CareerOS

                           │

            ┌──────────────┼──────────────┐

            ▼              ▼              ▼

      Web Dashboard     REST API      Scheduler

            │              │              │

            └──────────────┼──────────────┘

                           ▼

                    Application Core

                           │

 ┌────────────┬─────────────┬─────────────┬─────────────┐

 ▼            ▼             ▼             ▼

Collectors    AI Engine   Browser Engine Database

 │             │             │             │

 ▼             ▼             ▼             ▼

Notifications Resume Engine Cover Letters Analytics

```

---

## 2.2 Core Modules

### Module 1 — Collectors

Responsible for discovering internships and jobs.

Supported Platforms:

- LinkedIn
- Internshala
- Unstop
- Wellfound
- Indeed
- Naukri
- Foundit
- Google Jobs
- Company Career Pages

---

### Module 2 — AI Engine

Responsible for:

- Resume Matching
- ATS Score
- Skill Gap Detection
- Resume Selection
- Resume Tailoring

---

### Module 3 — Browser Engine

Responsible for:

- Login
- Upload Resume
- Fill Forms
- Submit Applications

---

### Module 4 — Notification Engine

Responsible for:

- Email
- WhatsApp
- Dashboard Alerts

---

### Module 5 — Dashboard

Responsible for displaying:

- Jobs
- Applications
- Analytics
- Resume Library
- Notifications
