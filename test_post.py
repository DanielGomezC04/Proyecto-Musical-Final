import httpx

url = "http://127.0.0.1:8000/users/create"
data = {
    "username": "testuser",
    "email": "test@example.com"
}

print(f"Posting to {url}...")
try:
    response = httpx.post(url, data=data, follow_redirects=True)
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Response: {response.text}")
    else:
        print("Success!")
except Exception as e:
    print(f"Error: {e}")
