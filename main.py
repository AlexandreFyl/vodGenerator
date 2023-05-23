# -------------------------------------------
# -------- MAIN SCRIPT VODGENERATOR ---------
# -------------------------------------------

# Scripts imports
from getAssets import *

# Execute full script

# Constants
CHAMP_NAME = "Yuumi"  # Do not forget to CAPS the first char
PATCH = getLastVersionAvailable()
REFINED_ITEMS_LIST = getItemsListAsJson(PATCH)
