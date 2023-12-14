import requests
from bs4 import BeautifulSoup
import csv

url = "https://jobs.lever.co/xsolla?workplaceType=onsite&location=Kuala%20Lumpur&department=Research%20%26%20Development"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all job postings on the page
job_postings = soup.find_all('div', class_='posting')

# Create a list to store job data
job_data = []

# Loop through each job posting
for job_posting in job_postings:
    # Find the job title
    job_title_tag = job_posting.find('h5')
    job_title = job_title_tag.text.strip() if job_title_tag else "Job title not found"

    # Find the link to apply
    apply_link_tag = job_posting.find('a', class_='posting-btn-submit template-btn-submit hex-color')
    apply_link = apply_link_tag['href'] if apply_link_tag and 'href' in apply_link_tag.attrs else "Apply link not found"

    # Find the posting category
    posting_category_tag = job_posting.find('div', class_='posting-categories')
    posting_category = posting_category_tag.text.strip() if posting_category_tag else "Category not found"

    # Append the job data to the list
    job_data.append({
        'Job Title': job_title,
        'Apply Link': apply_link,
        'Posting Category': posting_category
    })

# Save the job data to a CSV file
csv_filename = 'xsolla_job.csv'
fields = ['Job Title', 'Apply Link', 'Posting Category']

with open(csv_filename, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    
    # Write the header
    writer.writeheader()
    
    # Write the job data
    writer.writerows(job_data)

print(f"Job data has been saved to {csv_filename}")
