from tabulate import tabulate
class Contact:
    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber

    def display(self):
        if self is not None:
            print(f'Contact First Name: {self.firstName}'f' Last Name: {self.lastName}'f' Phone Number: {self.phoneNumber}')
        else:
            print('no data found')


contactsList = [["eli","un","050"]]
# contact_1 = Contact('Elisheva1', 'maimon', '050-6543210')
# contact_2 = Contact('Elisheva2', 'ungar', '050-6543210')
# contact_3 = Contact('Elisheva3', 'ungar', '050-6543210')



# def addContact(contactToAdd):
#     contactsList.append(contactToAdd)
#     print('was added')

# addContact(contact_1)
# addContact(contact_2)
# addContact(contact_3)

def displayAllContacts():
    print(contactsList)
    list1=[ ['1', '2', '3'],['41', '42', '43'],['51', '52', '63']]
    print(tabulate(contactsList, headers=["First Name", "Last Name", "Phone Number"]))
  #  for contact in contactsList:
  #     contact.display()
displayAllContacts()
'''
def deleteContact(contactToRemove):
    contactsList.remove(contactToRemove)
    print('was deleted')


deleteContact(contact_3)
displayAllContacts()


# Search
# input("Enter your name:")
def search1(value):
    for x in contactsList:
        return x.firstName if x.firstName == value else x.lastName if x.lastName == value else 'nothing was found'


print('search1: ', search1('Elisheva1'))


def search(value):
    for contact in contactsList:
        if contact.firstName == value:
            return contact
        elif contact.lastName == value:
            return contact
    else:
        'nothing was found'


value = search('Elisheva1')


def update(attrName, ContactToSearch, valueToUpdate):
    setattr(search(ContactToSearch), attrName, valueToUpdate)


ContactToSearch = input("Enter first name:")
attribute = input("Enter attribute:")
newValue = input("Enter new value:")
update(attribute, ContactToSearch, newValue)
displayAllContacts()
'''