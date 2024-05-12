
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
        self.modules     = list()
        self.consumables = list()
    
    def roll_attributes(self):
        raise NotImplementedError()

    def swap_attributes(self):
        raise NotImplementedError()
    
    def select_pilot(self):
        raise NotImplementedError()

    def select_record(self):
        raise NotImplementedError()

    def select_chassis(self):
        raise NotImplementedError()

    def select_callsign(self):
        raise NotImplementedError()

    def select_module(self):
        raise NotImplementedError()

    def select_starting_gear_or_credits(self):
        raise NotImplementedError()


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
