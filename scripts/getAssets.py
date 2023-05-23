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
    file_path = os.path.join(TEMP_FOLDER_PATH + "/champ",
                             "champion-profile-picture.png")

    # Save the response to the file.
    with open(file_path, "wb") as f:
        f.write(data)


def getChampLoadingScreenPicture(champName):
    # please refers to first method comments
    # 0 refers to the base skin
    url = "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/" + \
        champName + "_0.jpg"

    prepared_request = requests.Request("GET", url).prepare()

    response = requests.Session().send(prepared_request)

    data = response.content

    file_path = os.path.join(
        TEMP_FOLDER_PATH + "/champ", "champion-loading-screen-picture.jpg")

    with open(file_path, "wb") as f:
        f.write(data)


def getItemsListAsJson(patchVersion):
    url = "https://ddragon.leagueoflegends.com/cdn/" + \
        patchVersion+"/data/en_US/item.json"

    prepared_request = requests.Request("GET", url).prepare()

    response = requests.Session().send(prepared_request)

    # We use only the needed data in returned json
    data = response.json()["data"]

    # We create a empty list where we'll refine the og data
    refined_items_list = []

    # Iterate over items
    for item_id, item_data in data.items():
        # Extract "name" and "full" keys from "image"
        name = item_data["name"]
        full = item_data["image"]["full"]

        # Create a dictionary with the extracted data
        extracted_item = {
            "id": item_id,
            "name": name,
            "full": full
        }

        # Append the extracted item to the list
        refined_items_list.append(extracted_item)

    return refined_items_list


def retrieveFullKeyFromName(itemName, refinedItemsList):
    for item in refinedItemsList:
        if item["name"] == itemName:
            return item["full"]


def getItemPicture(itemName, patch, refinedItemsList, pictureFileName):
    full = retrieveFullKeyFromName(itemName, refinedItemsList)

    url = "https://ddragon.leagueoflegends.com/cdn/" + patch + "/img/item/" + full

    prepared_request = requests.Request("GET", url).prepare()

    response = requests.Session().send(prepared_request)

    data = response.content

    file_path = os.path.join(
        TEMP_FOLDER_PATH + "/build", pictureFileName + ".png")

    with open(file_path, "wb") as f:
        f.write(data)


# TESTS
# Fake inputs
CHAMP_NAME = "Yuumi"
PATCH = getLastVersionAvailable()

getChampProfilePicture(CHAMP_NAME)
getChampLoadingScreenPicture(CHAMP_NAME)
REFINED_ITEMS_LIST = getItemsListAsJson(PATCH)
retrieveFullKeyFromName("Prowler's Claw", REFINED_ITEMS_LIST)  # 6693
getItemPicture("Prowler's Claw", PATCH, REFINED_ITEMS_LIST, "testItem")
