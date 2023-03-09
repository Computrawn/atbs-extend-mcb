#! python3
# mcb.pyw — Saves and loads pieces of text to the clipboard.
# Usage:    py.exe mcb.pyw save <keyword> — Saves keyword to clipboard.
#           py.exe mcb.pyw delete <keyword> — Removes keyword from mcb_shelf.
#           py.exe mcb.pyw <keyword> — Loads keyword to clipboard.
#           py.exe mcb.pyw list — Loads all keywords to clipboard.
#           py.exe mcb.pyw delete — Removes all keywords from mcb_shelf.


import shelve, pyperclip, sys

mcb_shelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()