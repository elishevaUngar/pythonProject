import json
import ast
import pandas as pd
import globalMembers as g
from json import JSONEncoder


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

    def __str__(self):
        return f"firstName: {self.firstName}, lastName: {self.lastName}, phoneNumber: {self.phoneNumber}"


class ContactJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return {'firstName': obj.firstName,
                    'lastName': obj.lastName,
                    'phoneNumber': obj.phoneNumber}
            return JSONEncoder.default(self, obj)


def readJsonFile():
    with open('ContactData.json') as myJson:
        g.contactsListForJson = json.load(myJson)


def insertIntoFile(contactsListToJson):
    with open('ContactData.json', 'w') as myJson:
        json.dump(contactsListToJson, myJson, indent=4, sort_keys=True, ensure_ascii=False)


def encodeObject(contactToEncode):
    g.dicObJPerson = ast.literal_eval(ContactJsonEncoder().encode(contactToEncode))  # str to dict


def addContact(contactToAdd):
    readJsonFile()
    encodeObject(contactToAdd)
    try:
        if type(g.contactsListForJson) is dict:
            g.contactsListForJson['Contacts'].append(g.dicObJPerson)
            insertIntoFile(g.contactsListForJson)
            print("contact was added: ", g.dicObJPerson)
    except Exception as Error:
        print(Error)


def search(value):
    readJsonFile()
    for contact in g.contactsListForJson["Contacts"]:
        return contact['firstName'] if contact['firstName'] == value else contact['lastName'] \
            if contact['lastName'] == value else 'nothing was found'


def search1(value):
    readJsonFile()
    for contact in g.contactsListForJson["Contacts"]:
        if contact['firstName'] == value:
            return contact
        elif contact['lastName'] == value:
            return contact
        elif contact['phoneNumber'] == value:
            return contact
    else:
        'nothing was found'


def deleteContact(contactToDelete):
    readJsonFile()
    contactToDelete = search1(contactToDelete)
    encodeObject(contactToDelete)
    if type(g.contactsListForJson) is dict:
        try:
            g.contactsListForJson['Contacts'].remove(g.dicObJPerson)
            insertIntoFile(g.contactsListForJson)
            print("contact was deleted")
        except Exception as Error:
            print(Error)


def displayAllContacts():
    readJsonFile()
    if len(g.contactsListForJson) > 0 and len(g.contactsListForJson["Contacts"]) > 0:
        df = pd.DataFrame(g.contactsListForJson["Contacts"])
        print(df)
    else:
        print("no contacts in DB")

def displayAllContactsApp():
    readJsonFile()
    if len(g.contactsListForJson) > 0 and len(g.contactsListForJson["Contacts"]) > 0:
       return g.contactsListForJson["Contacts"]
    else:
      return "no contacts in DB"


def deleteAllContacts():
    if len(g.contactsListForJson) > 0:
        try:
            g.contactsListForJson["Contacts"].clear()
            insertIntoFile(g.contactsListForJson)
            print("all contacts were deleted")
        except Exception as Error:
            print(Error)
    else:
        print("no contacts in DB")


def updateContact(attrName, contactToSearch, valueToUpdate):
    try:
        contact = search1(contactToSearch)
        contact[attrName] = valueToUpdate
        insertIntoFile(g.contactsListForJson)
        print("contact was updated: ", contact)
    except Exception as Error:
        print(Error)
