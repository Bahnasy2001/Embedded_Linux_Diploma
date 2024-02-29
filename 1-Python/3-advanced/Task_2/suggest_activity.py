import requests

def suggest_activity():
    try:
        #send GET request to the boredapi URL
        response = requests.get("https://www.boredapi.com/api/activity")
        #Check if the request was successful (status code 200)
        if response.status_code == 200:
            #parse JSON response
            data = response.json()
            activity = data.get('activity')
            if activity:
                print("Here's an activity suggestion for you:", activity)
            else:
                print("No activity suggestion available.")
        else:
            print("Failed to retrieve activity suggestion. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred: ",e )


suggest_activity()