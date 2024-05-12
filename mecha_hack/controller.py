
import inquirer

from models import NewCharacter

from random import randint

def roll_attributes():
    attribute_results = dict()
    attributes = ['power', 'mobility', 'system', 'presence']
    attr_penalty = False
    for a in attributes:
        roll_1     = randint(1, 6)
        roll_2     = randint(1, 6)
        roll_3     = 3 if attr_penalty else randint(1, 6)
        results    = [roll_1, roll_2, roll_3]
        attr_score = sum(results)

        attr_penalty = True if attr_score >= 15 else False # need to test if two 15s in a row

        attribute_results[a] = {'roll': attr_score, 'results': results}

    return attribute_results


def swap_attributes():
    swap = {inquirer.Confirm('flag', message='Would you like to swap two attributes?', default=False)}
    swap_flag = inquirer.prompt(swap)
    if swap_flag['flag']:
        print('swap two attrs')
        attr_list = ['Power', 'Mobility', 'System', 'Presence', 'Cancel Swap']
        first_attr_list = [inquirer.List('attr', message='Please select the first attr', choices=['Power', 'Mobility', 'System', 'Presence', 'Cancel Swap'])]
        first_attr_resp = inquirer.prompt(first_attr_list)
        print(first_attr_resp['attr'])
    else:
        print('leave the attrs as is')

if __name__ == '__main__':
    # init our new character
    print('create a new character')
    new_character = NewCharacter()
    # roll the main stats
    print('roll the four stats')
    attributes = roll_attributes()
    # print out what's happening
    for a in attributes.keys():
        msg = '{} rolls: results {} [{} {} {}]'.format(a, attributes[a]['roll'], attributes[a]['results'][0], attributes[a]['results'][1], attributes[a]['results'][2])
        if attributes[a]['roll'] >= 15:
            msg += ' next attribute rolled as 2d6+3'
        print(msg)
        setattr(new_character, a, attributes[a]['roll'])
    print(new_character.__dict__)
    # prompt our used to swap stats
    print('CHOICE: swap zero or two stats')
    swap_attributes()
    print('choose a pilot')
    print('CHOICE: roll or choose a record')
    print('choose a chasis')
    print('CHOICE: roll or choose a callsign')
    print('choose a module')
    print('CHOICE: receive chasis starting gear or get 120 credits')
