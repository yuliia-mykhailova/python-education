"""Working with dictionaries"""

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

del phonebook["Jill"]
phonebook["Jake"] = 938273443

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
