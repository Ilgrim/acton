"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from evennia.utils import ansi

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(player) -  when Player disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Player has disconnected"
                    to the room.
    at_pre_puppet - Just before Player re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "PlayerName has entered the game" to the room.

    """
    def at_object_creation(self):
        """
        Called only at initial creation. This is a rather silly
        example since ability scores should vary from Character to
        Character and is usually set during some character
        generation step instead.
        """
        # set a color config value
        self.db.config_color = True
        # set persistent attributes

        self.db.charisma = 8
        self.db.constitution = 8
        self.db.dexterity = 8
        self.db.intelligence = 8
        self.db.strength = 8
        self.db.wisdom = 8

        self.db.level = 0
        self.db.experience = 0

        self.db.levels = [20, 100, 500, 1000, 2000, 5000, 10000]


        self.db.power = 1
        self.db.combat_score = 1

    def get_abilities(self):
        """
        Simple access method to return ability
        scores as a tuple (str,agi,mag)
        """
        return (self.db.charisma, self.db.constitution, self.db.dexterity,
               self.db.intelligence, self.db.strength, self.db.wisdom)

    def return_appearance(self, looker):
        """
        The return from this method is what
        looker sees when looking at this object.
        """
        text = super(Character, self).return_appearance(looker)
        cscore = " (combat score: %s)" % self.db.combat_score
        if "\n" in text:
            # text is multi-line, add score after first line
            first_line, rest = text.split("\n", 1)
            text = first_line + cscore + "\n" + rest
        else:
            # text is only one line; add score to end
            text += cscore
        return text

    def msg(self, text=None, from_obj=None, session=None, options=None, **kwargs):
        "our custom msg()"
        if self.db.config_color is not None: # this would mean it was not set
            if not self.db.config_color:
                # remove the ANSI from the text
                text = ansi.strip_ansi(text)
        super(Character, self).msg(text=text, from_obj=from_obj,
                                             session=session, **kwargs)
