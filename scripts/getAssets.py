import requests
import os


def getLastVersionAvailable():
    response = requests.get(
        "https://ddragon.leagueoflegends.com/api/versions.json")

    data = response.json()

    return data[0]


def getChampProfilePicture(champName, patch):
    # Create a URL string.
    url = "https://cdn.communitydragon.org/" + \
        patch + "/champion/" + champName + "/square"

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

# def getItemPicture(itemName, patch)
    # todo


# TESTS
PATCH = getLastVersionAvailable()
getChampProfilePicture("yuumi", PATCH)
