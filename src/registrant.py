from .contact import Contact

class Registrant:

    def __init__(self, data):
        self.name = data.get('name')
        self.email = data.get('email')
        self.phone = data.get('phone')


    def __repr__(self):
        return f'{self.name} / {self.email} / {self.phone}'


    def process(self, contacts, leads):
        contact = next((c for c in contacts if c.email == self.email), None)
        if contact:
            if not contact.phone and self.phone:
                contact.phone = self.phone
                return


        contact = next((c for c in contacts if c.phone == self.phone), None)
        if contact:
            if not contact.email and self.email:
                contact.email = self.email
                return


        lead = next((l for l in leads if l.email == self.email), None)
        if lead:
            leads.remove(lead)
            contacts.append(Contact(self.name or lead.name, self.email, self.phone or lead.phone))
            return


        lead = next((l for l in leads if l.phone == self.phone), None)
        if lead:
            leads.remove(lead)
            contacts.append(Contact(self.name or lead.name, self.email or lead.email, self.phone))
            return


        contacts.append(Contact(self.name, self.email, self.phone))


