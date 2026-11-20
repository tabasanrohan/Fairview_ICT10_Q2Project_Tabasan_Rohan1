from pyscript import document, display

#CLASSMATES
grade7 = {'Alex Cruz', 'Mia Reyes'}
grade8 = {'John Wick', 'Rohan Santos'}
grade9 = {'Logan Paul', 'Saint Nicolas'}
grade10 = {'Coco Martin', 'Jamie Lee'}


#ADD A MEMBER
def add_member(e):

    #FIRSTNAME
    firstname = document.getElementById('firstname').value.strip().title()
    #LASTANME
    lastname = document.getElementById('lastname').value.strip().title()
    #Full Name
    fullname = firstname + ' ' + lastname

    #If blank
    if not firstname or not lastname:
        document.getElementById('members').innerHTML = "Please enter both first and last names."
        return

    #Fullname
    fullname2 = {fullname}
    # Union
    members = grade7 | grade8 | grade9 | grade10 | fullname2

    display(f"Members: {members}", target="members")
    display(f"Total Members: {len(members)}", target="total")
