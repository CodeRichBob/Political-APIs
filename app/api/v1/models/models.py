
PARTIES=[]


class PartiesModel():
    def __init__(self, name, logoUrl, id):
        self.name = name
        self.logoUrl = logoUrl
        self.id = id

    @staticmethod
    def view_all_parties():
        return PARTIES

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


