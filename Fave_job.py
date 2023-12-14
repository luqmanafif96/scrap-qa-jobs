import requests

url = 'https://myfave.darwinbox.com/ms/candidateapi/job'
params = {
    'title': 'Test',
    'department': '5defee42aafd9',
    'location': '5def6482cf70b',
    'page': 1,
    'limit': 10
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',  # Replace with your user agent
    'Set-Cookie ' : '__cf_bm=uXg7bT7ynn6c3s6QDOkXfdZqHv8V1lW2YVDNgO5dCes-1702200007-1-AdWwIK8HXuKq4QjqtQqsbO23XG9gFBIutcu2Zg397H8os8299fo81wXAxtKzIjbz/6PGxW4dgbTkWcRbaJDlUUo=; path=/; expires=Sun, 10-Dec-23 09:50:07 GMT; domain=.darwinbox.com; HttpOnly; Secure; SameSite=None'
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    job_data = response.json()

    # Process the job data as needed
    for job in job_data.get('data', []):
        print(f"Job Title: {job.get('title')}")
        print(f"Department: {job.get('department')}")
        print(f"Location: {job.get('location')}")
        print("-----")

    # You can further process the job data or store it as needed

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
