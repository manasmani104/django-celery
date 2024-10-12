from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Company
import pdfkit
from django.template.loader import render_to_string
import matplotlib.pyplot as plt
import io
from django.core.files import File

@shared_task
def generate_company_report(company_id, recipient_email):
    print("tasssssssks")
    company = Company.objects.get(id=company_id)
    departments = company.departments.all()

    # Generate a simple pie chart using matplotlib for department distribution
    department_names = [dept.name for dept in departments]
    department_counts = [dept.employees.count() for dept in departments]  # Assuming departments have employees

    plt.figure(figsize=(6, 6))
    plt.pie(department_counts, labels=department_names, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

    # Save chart to a BytesIO object
    chart_image = io.BytesIO()
    plt.savefig(chart_image, format='png')
    plt.close()  # Close the figure to free memory
    chart_image.seek(0)

    # Render the HTML template
    html_string = render_to_string('company_report_template.html', {
        'company': company,
        'departments': departments,
    })

    # Generate PDF using pdfkit
    pdf = pdfkit.from_string(html_string, False)

    # Save the generated PDF to a file (optional)
    pdf_file_path = f'/tmp/{company.name}_report.pdf'
    with open(pdf_file_path, 'wb') as f:
        f.write(pdf)

    # Create the email message with HTML content
    email = EmailMessage(
        subject=f"{company.name} Report",
        body=html_string,  # Use the rendered HTML string as the body
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient_email]
    )
    
    # Set the content type to HTML
    email.content_subtype = 'html'

    # Attach the chart as an inline image for email
    email.attach('chart.png', chart_image.getvalue(), 'image/png')

    # Attach the PDF
    email.attach_file(pdf_file_path)

    # Send the email
    email.send(fail_silently=False)

    return "Report generated and email sent"
