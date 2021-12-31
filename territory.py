from config import *

# maybe we can dictate a defense and production value based off of the territory_type?
# ocean and mountain can be impassable but the others like forest plains or swamp dictate the defense and production value?
# we can also generate it to some random int within a range to keep things interesting


class Territory:
    def __init__(self, territory_type):
        self.type = territory_type
