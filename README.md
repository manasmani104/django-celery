# Company Report Generator

A Django application that generates company reports, including department distribution charts, and sends them via email in PDF format.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Email Settings](#email-settings)
- [Celery Setup](#celery-setup)
- [Contributing](#contributing)
- [License](#license)

## Features
- Generate PDF reports containing company information and employee details.
- Create and attach departmental distribution charts.
- Send reports via email with HTML content and attachments.

## Technologies Used
- Python
- Django
- Celery
- pdfkit
- Matplotlib
- Django Templates
- SQLite/PostgreSQL (Database)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/company-report-generator.git
   cd company-report-generator
