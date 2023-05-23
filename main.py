# -------------------------------------------
# -------- MAIN SCRIPT VODGENERATOR ---------
# -------------------------------------------

# Scripts imports
from scripts.getAssets import *

# Constants
CHAMP_NAME = "Aatrox"  # Do not forget to CAPS the first char
PATCH = getLastVersionAvailable()
REFINED_ITEMS_LIST = getItemsListAsJson(PATCH)
THREE_ITEMS_BUILD = ["Echoes of Helia",
                     "Vigilant Wardstone", "Rabadon's Deathcap"]
FILLER_ITEMS = ["Statikk Shiv", "Sterak's Gage"]
BOOTS = "Plated Steelcaps"

# ---------------------------------
# ----- Execute full script -------
# ---------------------------------


# -------------------
# Assets download
# -------------------


# Get both champ images
getChampProfilePicture(CHAMP_NAME)
getChampLoadingScreenPicture(CHAMP_NAME)

# Get boots image
if BOOTS != "":  # No boots for Yuumi & Cassio
    getItemPicture(BOOTS, PATCH, REFINED_ITEMS_LIST, "boots")

# Get 3 items spike
getThreeFirstItems(THREE_ITEMS_BUILD, PATCH, REFINED_ITEMS_LIST)

# Get filler items
getFillersItems(FILLER_ITEMS, PATCH, REFINED_ITEMS_LIST)
