OFFICES = []

class OfficesModel():
    def __init__(self, name, type, id):
        self.name = name
        self.type = type
        self.id = id

    @staticmethod
    def view_all_offices():
        return OFFICES

    def saveoffice(self):
        office = {
            "name": self.name,
            "type": self.type,
            "id": self.id
        }
        OFFICES.append(office)

    @staticmethod
    def get_specific_office(id):
        return [office for office in OFFICES if office["id"] == id]

PARTIES=[]


class PartiesModel():
    def __init__(self, name, logoUrl, id):
        self.name = name
        self.logoUrl = logoUrl
        self.id = id

    @staticmethod
    def view_all_parties():
        return OFFICES

    def saveparty(self):
        party = {
            "name": self.name,
            "logoUrl": self.logoUrl,
            "id": self.id
        }
        PARTIES.append(party)

    @staticmethod
    def get_specific_party(id):
        return [party for party in PARTIES if party["id"] == id]


