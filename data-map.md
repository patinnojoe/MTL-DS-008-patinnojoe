# NHS Referral to Treatment (RTT) Reference Guide

The NHS **Referral to Treatment (RTT)** framework measures the time non-emergency (consultant-led elective) patients wait from their initial referral through to the start of their definitive treatment.

---

## 1. Referral to Treatment (RTT)

- **Definition:** The operational and statistical framework used in NHS England to monitor waiting times for consultant-led elective care.
- **Core Purpose:** Tracks how long a patient waits from the point a hospital provider receives a referral until the patient begins their first definitive medical, surgical, or therapeutic treatment (or is discharged).

---

## 2. RTT Pathway

An **RTT pathway** is the continuous timeline of a single patient journey for a specific medical condition.

- **Clock Start:** The date the referral is received by the healthcare provider (typically from a GP or another clinician).
- **Clock Running:** The ongoing diagnostic and outpatient period (e.g., blood tests, scans, initial consultations, pre-op assessments).
- **Clock Stop:** The date the pathway officially concludes. This occurs when:
  - **First definitive treatment starts** (e.g., surgery, procedure, medication course), OR
  - **Clinical decision is made that no treatment is needed**, OR
  - The patient explicitly declines treatment or repeatedly fails to attend (DNA/discharge rules).

---

## 3. The 18-Week RTT Standard

- **The Target:** Under the NHS Constitution, at least **92%** of patients on active, non-completed pathways should be waiting **no longer than 18 weeks** (126 days) from referral to treatment.
- **Time Bands:** National waiting lists are aggregated into weekly buckets (e.g., `0 to 1 weeks`, `1 to 2 weeks`, ..., `17 to 18 weeks`, up to `52+ weeks`, `65+ weeks`, and `78+ weeks`) to track performance and excessive backlogs.

---

## 4. Incomplete Pathway

- **Definition:** A pathway where the clock is still **actively running**. The patient is currently on the waiting list and has not yet started treatment or been discharged.
- **Analytical Significance:** This is the primary dataset used to judge the **92% headline constitutional standard** ($\text{Incomplete Pathways } \le 18 \text{ weeks} / \text{Total Incomplete Pathways}$). It reflects the **active waiting list size (work in progress)**.

---

## 5. Admitted Pathway (Completed)

- **Definition:** A completed pathway where the clock stopped due to an **admission to an inpatient or day-case bed** for treatment.
- **Common Examples:** Elective hip/knee replacement, laparoscopic cholecystectomy (gallbladder removal), or cataract surgery in day surgery.
- **Analytical Role:** Measures completed surgical and procedural activity during the reporting month.

---

## 6. Non-Admitted Pathway (Completed)

- **Definition:** A completed pathway where the clock stopped **without requiring hospital admission**.
- **Common Examples:**
  - Starting prescription medication in an outpatient clinic.
  - Fitting an orthotic or hearing device.
  - Starting a course of therapy (physiotherapy, speech therapy).
  - A clinician deciding following diagnostic tests (e.g., MRI/CT) that watchful waiting or no medical treatment is required.
- **Analytical Role:** Measures completed outpatient and non-invasive elective activity.

---

## 7. Treatment Function Code (TFC) / Specialty

- **Definition:** A standardized NHS 3-digit numeric code classifying the specialized clinical service under which the patient is treated (rather than the individual clinician's job title).
- **Common Codes:**
  - `100`: General Surgery
  - `101`: Urology
  - `110`: Trauma & Orthopaedics (T&O)
  - `120`: ENT (Ear, Nose & Throat)
  - `130`: Ophthalmology
  - `300`: General Medicine
  - `320`: Cardiology
  - `410`: Rheumatology
  - `430`: Geriatric Medicine
- **Analytical Role:** Used as the primary clinical grouping dimension to compare backlogs, median wait times, and specialty-level pressures across organizations.

---

## 8. NHS Trust / Provider

- **Definition:** The legal and organizational entity (e.g., an acute hospital NHS Trust or Foundation Trust) responsible for delivering hospital services and elective care.
- **Key Identifiers:**
  - **ODS Code:** The 3-to-5 character alphanumeric organization code (e.g., `RRV` for University College London Hospitals NHS Foundation Trust, `RGT` for Cambridge University Hospitals NHS Foundation Trust).
- **Provider vs. Commissioner Perspective:**
  - **Provider Data:** All pathways treated or waiting at hospitals managed by that specific Trust, regardless of where the patient lives.
  - **Commissioner / ICB Data:** Pathways for patients belonging to a specific Integrated Care Board (ICB) geographic population, regardless of where they receive treatment.

---

## Quick Reference Summary

| Pathway Type / Concept       | Clock Status | Key Metric / Analytical Meaning                                                  |
| :--------------------------- | :----------- | :------------------------------------------------------------------------------- |
| **Incomplete Pathway**       | **Running**  | Active waiting list volume; judged against the **92% standard** ($\le 18$ weeks) |
| **Admitted Pathway**         | **Stopped**  | Elective surgical & day-case procedures completed that month                     |
| **Non-Admitted Pathway**     | **Stopped**  | Outpatient treatments, therapies, or clinical discharges completed that month    |
| **Treatment Function (TFC)** | N/A          | Clinical specialty dimension (e.g., `110` Trauma & Orthopaedics)                 |
| **NHS Trust (Provider)**     | N/A          | Hospital provider organizational dimension identified by ODS code                |
