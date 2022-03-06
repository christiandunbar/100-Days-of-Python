import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
result = response.json()
print(result)

if result['completed'] == True:
    print("Result is completed")
else:
    print("Result is not completed")