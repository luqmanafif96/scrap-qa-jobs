import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

def strip_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

def get_seamoney_link(job_id):
    return f"https://careers.seamoney.com/job-detail?id={job_id}&source_from=1"

def get_shopee_link(job_id):
    return f"https://careers.shopee.com.my/job-detail/{job_id}/1?channel=10001"

# Define the URL
url = "https://ats.workatsea.com/ats/api/v1/user/job/list/?limit=50&offset=0&search_content=QA&city_ids=17&department_ids=9&department_ids=11&department_ids=6&employment_ids=2&employment_ids=1"

# Define the user agent (you can replace this with an actual user agent string)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

# Make the HTTP request with the specified user agent
response = requests.get(url, headers={'User-Agent': user_agent})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    try:
        # Try to parse the JSON data
        data = response.json()
        # Extract job_list directly if it's under the key 'job_list'
        jobs = data.get('data', {}).get('job_list', [])

        # Remove HTML tags from job_description and requirements fields
        for job in jobs:
            job['job_description'] = strip_html_tags(job.get('job_description', ''))
            job['requirements'] = strip_html_tags(job.get('requirements', ''))

    except Exception as e:
        print(f"Failed to parse JSON data. Error: {e}")
        jobs = []

    if jobs:
        # Create a DataFrame with relevant information
        df = pd.DataFrame({
            'Job ID': [job.get('job_id') for job in jobs],
            'Position Name': [job.get('job_name') for job in jobs],
            'Job Description': [job.get('job_description') for job in jobs],
            'SeaMoney Application Link': [get_seamoney_link(job.get('job_id')) for job in jobs],
            'Shopee Application Link': [get_shopee_link(job.get('job_id')) for job in jobs]
        })

        # Save the DataFrame to a CSV file
        df.to_csv("jobs_data.csv", index=False)

        print("Data has been successfully scraped and saved to 'jobs_data.csv'")
    else:
        print("No job data found in the response.")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
