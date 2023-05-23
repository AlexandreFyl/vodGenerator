import requests
import os

# CONSTANTS
TEMP_FOLDER_PATH = "../assets/temp"


def getLastVersionAvailable():
    response = requests.get(
        "https://ddragon.leagueoflegends.com/api/versions.json")

    data = response.json()

    # Return last version number
    # So we ensure to get updated data at any moment
    return data[0]


def getChampProfilePicture(champName):
    # Create a URL string.
    url = "http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/" + champName + ".png"

    # Prepare the request.
    prepared_request = requests.Request("GET", url).prepare()

    # Send the request.
    response = requests.Session().send(prepared_request)

    # Get the response.
    data = response.content

    # Specify the file path.
    file_path = os.path.join(TEMP_FOLDER_PATH, "champion-profile-picture.png")

    # Save the response to the file.
    with open(file_path, "wb") as f:
        f.write(data)

# please refers to first method comments


def getChampLoadingScreenPicture(champName):
    url = "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/" + \
        champName + "_0.jpg"

    prepared_request = requests.Request("GET", url).prepare()

    response = requests.Session().send(prepared_request)

    data = response.content

    file_path = os.path.join(
        TEMP_FOLDER_PATH, "champion-loading-screen-picture.jpg")

    with open(file_path, "wb") as f:
        f.write(data)

# def getItemPicture(itemName, patch)
    # todo


# TESTS
PATCH = getLastVersionAvailable()
getChampProfilePicture("Yuumi")
getChampLoadingScreenPicture("Yuumi")
