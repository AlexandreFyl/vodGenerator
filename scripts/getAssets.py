import requests
import os

# CONSTANTS
PATCH = "13.10.1"  # To rework as dynamic or env var


def getChampProfilePicture(champName):
    # Create a URL string.
    url = "https://cdn.communitydragon.org/" + \
        PATCH + "/champion/" + champName + "/square"

    # Prepare the request.
    prepared_request = requests.Request("GET", url).prepare()

    # Send the request.
    response = requests.Session().send(prepared_request)

    # Get the response.
    data = response.content

    # Specify the temp assets folder path.
    temp_folder_path = "../assets/temp"

    # Create the folder if it doesn't exist.
    if not os.path.exists(temp_folder_path):
        os.makedirs(temp_folder_path)

    # Specify the file path.
    file_path = os.path.join(temp_folder_path, "champion-profile-icon.png")

    # Save the response to the file.
    with open(file_path, "wb") as f:
        f.write(data)


# TESTS

getChampProfilePicture("aatrox")
