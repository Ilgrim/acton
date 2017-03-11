# mygame/world/rules.py

import random


# messages

def resolve_combat(combat_handler, actiondict):
    """
    This is called by the combat handler.
    actiondict is a dictionary with a list of two actions
    for each character:
    {char.id:[(action1, char, target), (action2, char, target)], ...}
    """
    flee = {} # track number of flee commands per character
    for isub in range(2):
        # loop over sub-turns
        messages = []
        #exchanges = {}
        for subturn in (sub[isub] for sub in actiondict.values()):
            # for each character, resolve the sub-turn
            action, char, target = subturn
            if target:
                taction, tchar, ttarget = actiondict[target.id][isub]
                #exchanges[char] = tchar
                #if not exchanges[tchar] == char:
                if action == "hit":
                    if taction == "parry" and ttarget == char:
                        msg = "|R%s|W tries to hit |G%s|W, but |G%s|W parries the attack!"
                        messages.append(msg % (char, tchar, tchar))
                    elif taction == "defend" and random < 0.5:
                        msg = "|G%s|W defends against the attack by |R%s|W."
                        messages.append(msg % (tchar, char))
                    elif taction == "flee":
                        msg = "|G%s|W stops |R%s|W from disengaging, with a hit!"
                        flee[tchar] = -2
                        messages.append(msg % (char, tchar))
                    else:
                        msg = "|G%s|W hits |R%s|W, bypassing their %s!"
                        messages.append(msg % (char, tchar, taction))
                elif action == "parry":
                    if taction == "hit":
                        msg = "|G%s|W parries the attack by |R%s|W."
                        messages.append(msg % (char, tchar))
                    elif taction == "feint":
                        msg = "|R%s|W tries to parry, but |G%s|W feints and hits!"
                        messages.append(msg % (char, tchar))
                    else:
                        msg = "|R%s|W attempts to parry |G%s|W, to no avail."
                        messages.append(msg % (char, tchar))
                elif action == "feint":
                    if taction == "parry":
                        msg = "|G%s|W feints past |R%s|W's parry, landing a hit!"
                        messages.append(msg % (char, tchar))
                    elif taction == "hit":
                        msg = "|R%s|W feints but is defeated by |G%s|W hit!"
                        messages.append(msg % (char, tchar))
                    else:
                        msg = "|R%s|W attempts to feint |G%s|W, to no avail."
                        messages.append(msg % (char, tchar))
            # This goes back here so that it will run regardless of if a target is set - which there shouldn't be.
            elif action == "defend":
                msg = "|w%s|W defends."
                messages.append(msg % char)
            elif action == "flee":
                if char in flee:
                    flee[char] += 1
                else:
                    flee[char] = 1
                msg = "|w%s|W tries to disengage (two subsequent turns needed)"
                messages.append(msg % char)

        # echo results of each subturn
        combat_handler.msg_all("\n".join(messages))

    # at the end of both sub-turns, test if anyone fled
    msg = "|w%s|W withdraws from combat."
    for (char, fleevalue) in flee.items():
        if fleevalue == 2:
            combat_handler.msg_all(msg % char)
            combat_handler.remove_character(char)