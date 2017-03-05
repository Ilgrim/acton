"""
Commands

Commands describe the input the player can do to the game.

"""

from evennia import Command as BaseCommand
# from evennia import default_cmds


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_command(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_command(): Extra actions, often things done after
            every command, like prompts.

    """
    pass

#------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
#------------------------------------------------------------

#from evennia.utils import utils
#class MuxCommand(Command):
#    """
#    This sets up the basis for a MUX command. The idea
#    is that most other Mux-related commands should just
#    inherit from this and don't have to implement much
#    parsing of their own unless they do something particularly
#    advanced.
#
#    Note that the class's __doc__ string (this text) is
#    used by Evennia to create the automatic help entry for
#    the command, so make sure to document consistently here.
#    """
#    def has_perm(self, srcobj):
#        """
#        This is called by the cmdhandler to determine
#        if srcobj is allowed to execute this command.
#        We just show it here for completeness - we
#        are satisfied using the default check in Command.
#        """
#        return super(MuxCommand, self).has_perm(srcobj)
#
#    def at_pre_cmd(self):
#        """
#        This hook is called before self.parse() on all commands
#        """
#        pass
#
#    def at_post_cmd(self):
#        """
#        This hook is called after the command has finished executing
#        (after self.func()).
#        """
#        pass
#
#    def parse(self):
#        """
#        This method is called by the cmdhandler once the command name
#        has been identified. It creates a new set of member variables
#        that can be later accessed from self.func() (see below)
#
#        The following variables are available for our use when entering this
#        method (from the command definition, and assigned on the fly by the
#        cmdhandler):
#           self.key - the name of this command ('look')
#           self.aliases - the aliases of this cmd ('l')
#           self.permissions - permission string for this command
#           self.help_category - overall category of command
#
#           self.caller - the object calling this command
#           self.cmdstring - the actual command name used to call this
#                            (this allows you to know which alias was used,
#                             for example)
#           self.args - the raw input; everything following self.cmdstring.
#           self.cmdset - the cmdset from which this command was picked. Not
#                         often used (useful for commands like 'help' or to
#                         list all available commands etc)
#           self.obj - the object on which this command was defined. It is often
#                         the same as self.caller.
#
#        A MUX command has the following possible syntax:
#
#          name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#        The 'name[ with several words]' part is already dealt with by the
#        cmdhandler at this point, and stored in self.cmdname (we don't use
#        it here). The rest of the command is stored in self.args, which can
#        start with the switch indicator /.
#
#        This parser breaks self.args into its constituents and stores them in the
#        following variables:
#          self.switches = [list of /switches (without the /)]
#          self.raw = This is the raw argument input, including switches
#          self.args = This is re-defined to be everything *except* the switches
#          self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                     no = is found, this is identical to self.args.
#          self.rhs: Everything to the right of = (rhs:'right-hand side').
#                    If no '=' is found, this is None.
#          self.lhslist - [self.lhs split into a list by comma]
#          self.rhslist - [list of self.rhs split into a list by comma]
#          self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#          All args and list members are stripped of excess whitespace around the
#          strings, but case is preserved.
#        """
#        raw = self.args
#        args = raw.strip()
#
#        # split out switches
#        switches = []
#        if args and len(args) > 1 and args[0] == "/":
#            # we have a switch, or a set of switches. These end with a space.
#            switches = args[1:].split(None, 1)
#            if len(switches) > 1:
#                switches, args = switches
#                switches = switches.split('/')
#            else:
#                args = ""
#                switches = switches[0].split('/')
#        arglist = [arg.strip() for arg in args.split()]
#
#        # check for arg1, arg2, ... = argA, argB, ... constructs
#        lhs, rhs = args, None
#        lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#        if args and '=' in args:
#            lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#            lhslist = [arg.strip() for arg in lhs.split(',')]
#            rhslist = [arg.strip() for arg in rhs.split(',')]
#
#        # save to object properties:
#        self.raw = raw
#        self.switches = switches
#        self.args = args.strip()
#        self.arglist = arglist
#        self.lhs = lhs
#        self.lhslist = lhslist
#        self.rhs = rhs
#        self.rhslist = rhslist
#
#        # if the class has the player_caller property set on itself, we make
#        # sure that self.caller is always the player if possible. We also create
#        # a special property "character" for the puppeted object, if any. This
#        # is convenient for commands defined on the Player only.
#        if hasattr(self, "player_caller") and self.player_caller:
#            if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                # caller is an Object/Character
#                self.character = self.caller
#                self.caller = self.caller.player
#            elif utils.inherits_from(self.caller, "evennia.players.players.DefaultPlayer"):
#                # caller was already a Player
#                self.character = self.caller.get_puppet(self.session)
#            else:
#                self.character = None
#

class CmdAbilities(Command):
    """
    List abilities.

    Usage:
      abilities

    Displays a list of your current ability values.
    """
    key = "abilities"
    aliases = ["abi"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        "implements the actual functionality"

        cha, con, dex, int, str, wis = self.caller.get_abilities()
        string = ("CHA: %s\nCON: %s\nDEX: %s\nINT: %s\nSTR: %s\nWIS: %s" %
                 (cha,con, dex, int, str, wis))
        self.caller.msg(string)

from evennia import Command

class CmdEditCharacter(Command):
    """
    Set a trait of the character.

    Usage:
      character <field> = <value>

    Example:
      character strength = 10

    Allowed fields:
      |gcharisma|W, |gconstitution|W, |gdexterity|W,
      |gintelligence|W, |gstrength|W, |gwisdom|W

    This sets different abilities of the current character. This can only be
    used during character generation. You have a total of |w64|W ability points
    to assign. Each field must have at least |w8|W ability points in it, and
    you may not raise an ability higher than |w14|W(not right now, at least!).
    """

    key = "character"
    help_category = "general"

    def parse(self):
        "simple split of the = sign"
        field, value = None, None
        if "=" in self.args:
            self.field, self.value = [part.strip()
                             for part in self.args.rsplit("=", 1)]

    def func(self):
        "this performs the actual command"

        # the list of allowed fields
        allowed = ["charisma", "constitution", "dexterity", "intelligence",
                   "strength", "wisdom"]
        # make sure the variables are not None
        if not self.field or not self.value:
            self.caller.msg("Usage: character <field> = <value>")
            return
        # make sure the value can be converted to an int
        if not isinstance(int(self.value), int):
            self.caller.msg("The value must be a valid number.")
            return
        # convert the value to an int
        self.value = int(self.value)
        # make sure the field is allowed
        if not self.field in allowed:
            self.caller.msg("The allowed fields are: |g%s|W"
                            % "|W, |g".join(allowed))
            return
        # make sure the value is within range
        if self.value < 8 or self.value > 14:
            self.caller.msg("Abilities must have a value greater than or equal"
                            " to |w8|W and less than or equal to |w14|W!")
            return
        total, new_total = 0, 0
        # get the total of all the abilities combined
        for abil in allowed:
            total += int(self.caller.attributes.get(abil))
        # get what the new total would be if we added this new value
        new_total = (total - int(self.caller.attributes.get(self.field))
            + self.value)
        # make sure the new total does not exceed the maximum of 64
        if new_total > 64:
            self.caller.msg("You have exceeded your maximum ability points!"
                            " You only have |w%s|W left. Try reducing another"
                            " ability score first." % (64 - total))
            return
        # assuming everything is fine, set the new value to the field
        self.caller.attributes.add(self.field, self.value)
        self.caller.msg("Set |g%s|W to |w%s|W. You have |w%s|W ability points"
        " remaining." % (self.field, self.value, 64 - new_total))
        # if they have used up all of their points, let them know
        if new_total == 64:
            self.caller.msg("You have used up all of your ability points!"
                            " Either type `|wfinish|W` to exit character"
                            " creation, or lower one of your abilities"
                            " to customize them more.")


import random

class CmdAttack(Command):
    """
    Issues an attack.

    Usage:
      +attack

    This will calculate a new combat score based on your Power.
    Your combat score is visible to everyone in the same location.
    """
    key = "+attack"
    help_category = "mush"

    def func(self):
        "calculate the random score between 1-10*Power"
        caller = self.caller
        power = caller.db.power
        if not power:
            # this can happen if caller is not of
            # our custom Character typeclass
            power = 1
        combat_score = random.randint(1, 10 * power)
        caller.db.combat_score = combat_score

        # announce
        message = "%s +attack%s with a combat score of %s!"
        caller.msg(message % ("You", "", combat_score))
        caller.location.msg_contents(message %
                                     (caller.key, "s", combat_score),
                                     exclude=caller)

from evennia import create_object

class CmdCreateNPC(Command):
    """
    Create a new NPC.

    Usage:
      +createnpc <name>

    Creates a new, named NPC. The NPC will start with a Power of 1.
    """
    key = "+createnpc"
    aliases = ["+createNPC"]
    locks = "call:not perm(nonpcs)"
    help_category = "mush"

    def func(self):
        "creates the object and names it"
        caller = self.caller
        if not self.args:
            caller.msg("Usage: +createnpc <name>")
            return
        if not caller.location:
            # may not create NPC when OOC
            caller.msg("You must have a location to create an NPC.")
            return
        # make name always start with capital letter
        name = self.args.strip().capitalize()
        # create npc in caller's location
        npc = create_object("characters.Character",
                key=name,
                location=caller.location,
                locks="edit:id(%i) and perm(Builders);call:false()" % caller.id)
        # announce
        message = "%s created the NPC '%s'."
        caller.msg(message % ("You", name))
        caller.location.msg_contents(message % (caller.key, name),
                                                exclude=caller)

class CmdEditNpc(Command):
    """
    Edit an existing NPC.

    Usage:
      +editnpc <name>[/<attribute> [= value]]

    Examples:
      +editnpc mynpc/power = 5
      +editnpc mynpc/power    - displays power value
      +editnpc mynpc          - shows all editable
                                attributes and values

    This command edits an existing NPC. You must have
    permission to edit the NPC to use this.
    """
    key = "+editnpc"
    aliases = ["+editNPC"]
    locks = "cmd:not perm(nonpcs)"
    help_category = "mush"

    def parse(self):
        "we need to do some parsing here"
        args = self.args
        propname, propval = None, None
        if "=" in args:
            args, propval = [part.strip() for part in args.rsplit("=", 1)]
        if "/" in args:
            args, propname = [part.strip() for part in args.rsplit("/", 1)]
        # store, so we can access it below in func()
        self.name = args
        self.propname = propname
        # a propval without a propname is meaningless
        self.propval = propval if propname else None

    def func(self):
        "do the editing"
        allowed_propnames = ("power", "attribute1", "attribute2")

        caller = self.caller
        if not self.args or not self.name:
            caller.msg("Usage: +editnpc name[/propname][=propval]")
            return
        npc = caller.search(self.name)
        if not npc:
            return
        if not npc.access(caller, "edit"):
            caller.msg("You cannot change this NPC.")
            return
        if not self.propname:
            # this means we just list the values
            output = "Properties of %s:" % npc.key
            for propname in allowed_propnames:
                propvalue = npc.attributes.get(propname, default="N/A")
                output += "\n %s = %s" % (propname, propvalue)
            caller.msg(output)
        elif self.propname not in allowed_propnames:
            caller.msg("You may only change %s." %
                        ", ".join(allowed_propnames))
        elif self.propval:
            # assigning a new propvalue
            # in this example, the properties are all integers...
            intpropval = int(self.propval)
            npc.attributes.add(self.propname, intpropval)
            caller.msg("Set %s's property '%s' to %s" %
                        (npc.key, self.propname, self.propval))
        else:
            # propname set, but not propval - show current value
            caller.msg("%s has property %s = %s" %
                       (npc.key, self.propname,
                       npc.attributes.get(self.propname, default="N/A")))

class CmdNPC(Command):
    """
    Controls an NPC.

    Usage:
      +npc <name> = <command>

    This causes the NPC to perform a command as itself. It will do so
    with its own permissions and accesses.
    """
    key = "+npc"
    locks = "call:not perm(nonpcs)"
    help_category = "mush"

    def parse(self):
        "simple split of the = sign"
        name, cmdname = None, None
        if "=" in self.args:
            name, cmdname = [part.strip()
                             for part in self.args.rsplit("=", 1)]
        self.name, self.cmdname = name, cmdname

    def func(self):
        "run the command"
        caller = self.caller
        if not self.cmdname:
            caller.msg("Usage: +npc <name> = <command>")
            return
        npc = caller.search(self.name)
        if not npc:
            return
        if not npc.access(caller, "edit"):
            caller.msg("You may not order this NPC to do anything.")
            return
        # send the command order
        npc.execute_cmd(self.cmdname, sessid=self.caller.sessid)
        caller.msg("You told %s to do '%s'." % (npc.key, self.cmdname))

class CmdConfigColor(Command):
    """
    Configures your color

    Usage:
      @togglecolor on|off

    This turns ansii-colors on/off.
    Default is on.
    """

    key = "@togglecolor"
    aliases = ["@setcolor"]

    def func(self):
        "Implements the command"
        if not self.args or self.args not in [" on", " off"]:
            self.caller.msg("Usage: @setcolor on|off")
            return
        if self.args == " on":
            self.caller.db.config_color = True
            self.caller.msg("Color was turned |won|W.")
        else:
            self.caller.db.config_color = False
            self.caller.msg("Color was turned off.")
