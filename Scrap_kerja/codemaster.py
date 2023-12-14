import requests
import csv

url = 'https://www.ea.com/jobs-feed/filter/city=Kuala%20Lumpur'

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

# Make the HTTP request with the specified user agent
response = requests.get(url, headers={'User-Agent': user_agent})

# Check the response
if response.status_code == 200:
    job_data = response.json().get("jobs", [])
    print(job_data)

    # Extract job information and store in CSV
    csv_file_path = "codemaster_jobs.csv"
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["Title", "job_url", "location"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for job in job_data:
            position = job.get("title", "")
            job_url = job.get("detailUrl","")
            location = job.get("locations",[{}])[0].get("city" ,"")
            writer.writerow({
                "Title": position,
                "job_url": job_url,
                "location": location
            })

    print(f"Job information has been saved to {csv_file_path}")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
