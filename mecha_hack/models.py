
class NewCharacter:

    def __init__(self):
        self.power       = 0
        self.mobility    = 0
        self.system      = 0
        self.presence    = 0
        self.pilot       = None
        self.chassis     = None
        self.modules     = list()
        self.credits     = 0
        self.record      = None
        self.callsign    = None
        self.consumables = list()

class Pilot:
    pass

class Chassis:
    pass

class Character:

    def __init__(self, new_character: NewCharacter):
        self.pilot    = new_character.pilot
        self.chassis  = new_character.chassis
        self.power    = new_character.power
        self.mobility = new_character.mobility
        self.system   = new_character.system
        self.presence = new_character.presence
