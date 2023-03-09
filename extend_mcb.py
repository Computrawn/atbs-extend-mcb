#! python3
# mcb.pyw — Saves and loads pieces of text to the clipboard.
# Usage:   py.exe mcb.pyw save <keyword> — Saves clipboard text as keyword.
#          py.exe mcb.pyw delete <keyword> — Removes keyword and associated text from mcb_shelf.
#          py.exe mcb.pyw <keyword> — Loads text associated with keyword to clipboard.
#          py.exe mcb.pyw list — Loads list of existing keywords to clipboard.
#          py.exe mcb.pyw delete — Uses .clear method to empty mcb_shelf of keywords and associated text.

import shelve
import sys
import pyperclip

mcb_shelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print(f"Saving text: {pyperclip.paste()}")
# Delete keyword and associated text from database.
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords
    if sys.argv[1].lower() == "list":
        key_list = str(list(mcb_shelf.keys()))
        pyperclip.copy(key_list)
        print(key_list)
    # Clear database
    elif sys.argv[1].lower() == "delete":
        mcb_shelf.clear()
    # Load text associated with keyword to clipboard.
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
