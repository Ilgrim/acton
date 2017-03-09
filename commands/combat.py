# mygame/commands/combat.py

from evennia import Command


class CmdHit(Command):
    """
    Hit an enemy.

    Usage:
      hit <target>

    Strikes the given enemy with your current weapon.
    """
    key = "hit"
    aliases = ["strike", "slash"]
    help_category = "combat"

    def func(self):
        """Implements the command"""
        if not self.args:
            self.caller.msg("Usage: hit <target>")
            return
        target = self.caller.search(self.args)
        if not target:
            return
        ok = self.caller.ndb.combat_handler.add_action("hit",
                                                       self.caller,
                                                       target)
        if ok:
            self.caller.msg("You add 'hit' to the combat queue")
        else:
            self.caller.msg("You can only queue two actions per turn!")

        # tell the handler to check if turn is over
        self.caller.ndb.combat_handler.check_end_turn()


class CmdParry(Command):
    """
    Parry an enemy.

    Usage:
      parry <target>

    Parries the given enemy with your current weapon.
    """
    key = "parry"
    help_category = "combat"

    def func(self):
        """Implements the command"""
        if not self.args:
            self.caller.msg("Usage: parry <target>")
            return
        target = self.caller.search(self.args)
        if not target:
            return
        ok = self.caller.ndb.combat_handler.add_action("parry",
                                                       self.caller,
                                                       target)
        if ok:
            self.caller.msg("You add 'parry' to the combat queue")
        else:
            self.caller.msg("You can only queue two actions per turn!")

        # tell the handler to check if turn is over
        self.caller.ndb.combat_handler.check_end_turn()


class CmdFeint(Command):
    """
    Feint an enemy.

    Usage:
      feint <target>

    Feints the given enemy with your current weapon.
    """
    key = "feint"
    help_category = "combat"

    def func(self):
        """Implements the command"""
        if not self.args:
            self.caller.msg("Usage: feint <target>")
            return
        target = self.caller.search(self.args)
        if not target:
            return
        ok = self.caller.ndb.combat_handler.add_action("feint",
                                                       self.caller,
                                                       target)
        if ok:
            self.caller.msg("You add 'feint' to the combat queue")
        else:
            self.caller.msg("You can only queue two actions per turn!")

        # tell the handler to check if turn is over
        self.caller.ndb.combat_handler.check_end_turn()


class CmdDefend(Command):
    """
    Defend against an enemy.

    Usage:
      defend <target>

    Defends against the given enemy with your current weapon.
    """
    key = "defend"
    help_category = "combat"

    def func(self):
        """Implements the command"""
        if not self.args:
            self.caller.msg("Usage: defend <target>")
            return
        target = self.caller.search(self.args)
        if not target:
            return
        ok = self.caller.ndb.combat_handler.add_action("defend",
                                                       self.caller,
                                                       target)
        if ok:
            self.caller.msg("You add 'defend' to the combat queue")
        else:
            self.caller.msg("You can only queue two actions per turn!")

        # tell the handler to check if turn is over
        self.caller.ndb.combat_handler.check_end_turn()


class CmdDisengage(Command):
    """
    Disengage an enemy.

    Usage:
      disengage <target>

    Disengages the given enemy.
    """
    key = "disengage"
    help_category = "combat"

    def func(self):
        """Implements the command"""
        if not self.args:
            self.caller.msg("Usage: disengage <target>")
            return
        target = self.caller.search(self.args)
        if not target:
            return
        ok = self.caller.ndb.combat_handler.add_action("disengage",
                                                       self.caller,
                                                       target)
        if ok:
            self.caller.msg("You add 'disengage' to the combat queue")
        else:
            self.caller.msg("You can only queue two actions per turn!")

        # tell the handler to check if turn is over
        self.caller.ndb.combat_handler.check_end_turn()


from evennia import create_script


class CmdAttack(Command):
    """
    Initiates your target.

    Usage:
      attack <target>

    This will initiate combat with <target>. If <target> is
    already in combat, you will join the combat.
    """
    key = "attack"
    help_category = "General"

    def func(self):
        """Handle command."""
        if not self.args:
            self.caller.msg("Usage: attack <target>")
            return
        target = self.caller.search(self.args)
        if not target:
            return
        # set up combat
        if target.ndb.combat_handler:
            # target is already in combat - join it
            target.ndb.combat_handler.add_character(self.caller)
            target.ndb.combat_handler.msg_all("%s joins combat!" % self.caller)
        else:
            # create a new combat handler
            chandler = create_script("combat_handler.CombatHandler")
            chandler.add_character(self.caller)
            chandler.add_character(target)
            self.caller.msg("You attack %s! You are in combat." % target)
            target.msg("%s attacks you! You are in combat." % self.caller)



class CmdEndAll(Command):
    """
    Ends the battle instantly.

    Usage:
      endbattle
    """
    key = "endbattle"

    def func(self):
        """Handle command."""
        self.ndb.combat_handler.msg_all("Combat has ended")
        self.ndb.combat_handler.stop()


from evennia import CmdSet
from evennia import default_cmds


class CombatCmdSet(CmdSet):
    key = "combat_cmdset"
    mergetype = "Replace"
    priority = 10
    no_exits = True

    def at_cmdset_creation(self):
        self.add(CmdHit())
        self.add(CmdParry())
        self.add(CmdFeint())
        self.add(CmdDefend())
        self.add(CmdDisengage())
        self.add(default_cmds.CmdPose())
        self.add(default_cmds.CmdSay())