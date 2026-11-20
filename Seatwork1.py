
from pyscript import document, display


# all club member names
club_members = [
    "Joan Evangelista",
    "Rohan Tabasan",
    "John Doe",
    "Jane Doe",
    "Sabine Agacita"
]

def check_candidate(event):

    # FIRSTNAME
    first_name = document.getElementById("firstname").value.strip()
    # LASTNAME
    last_name = document.getElementById("lastname").value.strip()
    # fullname
    full_name = f"{first_name} {last_name}".strip()
    full_name_lower = full_name.lower()

    # lowercases every member's name
    members_lower = list(map(str.lower, club_members))

    # is member in the list?
    is_member = full_name_lower in members_lower
    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]

    # Boolean, true false
    display(messages[is_member], target="message")
