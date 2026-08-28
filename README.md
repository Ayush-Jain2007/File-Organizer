# 📁 Python File Organizer

A simple, interactive command-line tool built with Python to automatically categorize and clean up messy directories.

This project was built as a hands-on learning project to master core Python concepts—progressing from basic file handling (`os`, `shutil`) to **File I/O** and **Object-Oriented Programming (OOP)**.

---

## ✨ Features

- **Automated Categorization:** Scans directories and moves files into organized subfolders (`Images/`, `Documents/`, `Audio/`, `Videos/`, `Archives/`, `Others/`).
- **Execution Logging:** Tracks every file movement and run summary in a persistent `organizer_log.txt` file using standard File I/O.
- **Log History Viewer:** View past organization activity logs directly inside the terminal interface.
- **Path Validation:** Validates directory existence before running file operations to prevent runtime crashes.
- **Object-Oriented Design:** Encapsulated within a modular `FileOrganizer` class.

---

## 🛠️ Built With

- **Python 3.x** (Standard Library only — no external packages required!)
  - `os` (Directory traversal and path validation)
  - `shutil` (High-level file moving operations)
  - `datetime` (Timestamping log execution runs)

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.6+** installed on your system. You can verify this by running:

```bash
python --version