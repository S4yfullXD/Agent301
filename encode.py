import urllib.parse

data = input("Enter query_id= or user= -> ")

try:
    result = urllib.parse.quote(data, safe='')
    print(f"\nResult -> {result}")

except Exception as e:
    print(f"An error ocured: {e}")


    