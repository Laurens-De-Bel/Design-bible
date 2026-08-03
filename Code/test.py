# Example: install the package first with:
# pip install requests

import requests

response = requests.get("https://httpbin.org/get")
print("Status:", response.status_code)
