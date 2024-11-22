from src.lead import Lead
from src.contact import Contact
from src.registrant import Registrant

def main():
    contacts = [
        Contact("Alice Brown", None, "1231112223"),
        Contact("Bob Crown", "bob@crowns.com", None),
        Contact("Carlos Drew", "carl@drewess.com", "3453334445"),
        Contact("Doug Emerty", None, "4564445556"),
        Contact("Egan Fair", "eg@fairness.com", "5675556667"),
    ]

    leads = [
        Lead(None, "kevin@keith.com", None),
        Lead("Lucy", "lucy@liu.com", "3210001112"),
        Lead("Mary Middle", "mary@middle.com", "3331112223"),
        Lead(None, None, "4442223334"),
        Lead(None, "ole@olson.com", None),
    ]

    registrants_data = [
        {"registrant": {"name": "Lucy Liu", "email": "lucy@liu.com", "phone": None}},
        {"registrant": {"name": "Doug", "email": "doug@emmy.com", "phone": "4564445556"}},
        {"registrant": {"name": "Uma Thurman", "email": "uma@thurs.com", "phone": None}},
    ]

    registrants = [Registrant(data["registrant"]) for data in registrants_data]
    for registrant in registrants:
        registrant.process(contacts, leads)


    print("Contacts:")
    for contact in contacts:
        print(contact)

    print("\nLeads:")
    for lead in leads:
        print(lead)



if __name__ =="__main__":
    main()
