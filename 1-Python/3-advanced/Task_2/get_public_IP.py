import requests

def get_public_IP():
    try:
        # Send GET request to the ipify URL
        response = requests.get("https://api.ipify.org/?format=json")
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            #parse JSON response
            data = response.json()
            ip_address = data.get('ip')
            if ip_address:
                print("Your public IP address is:", ip_address)
            else:
                print("Failed to retrieve public IP address.")
        else:
            print("Failed to retrieve public IP address. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)


get_public_IP()