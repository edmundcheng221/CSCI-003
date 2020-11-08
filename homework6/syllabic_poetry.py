"""
Homework #06
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-01

"""
import random


def generate_word(syllables):
    available_words = [
        ['age', 'roof', 'plain', 'slime', 'floor', 'fig', 'rode', 'oomph', 'flab', 'chit', 'creek', "we'll", 'brail', 'bay', 'big', 'salve', 'yaws', 'heal', 'bring', 'stir', 'bah', 'con', 'rone', 'team', 'nought', 'gill', 'rare', 'plains', 'bowls', 'wee', 'queue', 'gun', 'etch', 'set', 'mode', 'miss', 'ate', 'darn', 'rusk', 'mast', 'box', 'their', 'duds', 'depth', 'lien', 'rob', 'deek', 'word', 'quell', 'hark', 'home', 'pledge', 'brown', 'rune', 'pike', 'sprout', 'trace', 'cot', 'nob', 'nonce', 'dear', 'sense', 'sleek', 'poke', 'hut'],
        ['stunner', 'sucrose', 'begone', 'scorecard', 'humble', 'crouton', 'trimming', 'pudding', 'henchman', 'cackle', 'coffee', 'coma', 'aces', 'prudence', 'rematch', 'hipper', 'chopper', 'imprint', 'purple', 'second', 'lowbrow', 'faucet', 'bureau', 'commune', 'endive', 'stakeout', 'sourpuss', 'cave-in', 'shipyard', 'honors', 'kowtow', 'okra', 'haler', 'rattan'],
        ['echoless', 'fluidly', 'catchier', 'cathartic', 'lawnmower', 'physicist', 'huntedly', 'unzipping', 'centigrade', 'cheekily', 'tectonics', 'clearheaded', 'seditious', 'anodized', 'vehicle', 'sprightliest', 'prevention', 'vehement', 'mnemonics', 'steamroller', 'spikiest', 'persuasive', 'randomly', 'forensics', 'uneasy', 'dizziness', 'nonhuman', 'ethanol', 'connection', 'shrewishly', 'fingerprint'],
        ['nongalactic', 'lacerating', 'optometer', 'troglodytic', 'regradated', 'uniformize', 'chlorination', 'retotaling', 'acceptable', 'culmination', 'forbiddingness', 'immoveable', 'disconcerted', 'prosperity', 'vapourizing', 'profitably', 'envelopment', 'unsealable', 'librarian', 'transmissiveness', 'willowpattern', 'nationalise', 'devotedness', 'clangorously', 'likeableness', 'troubleshooting', 'weakheartedly', 'obsoleteness'],
        ['unsublimated', 'hyperanarchy', 'cylindrically', 'irrationally', 'quasipractical', 'sulfurization', 'undermeasuring', 'victoriously', 'disquietingly', 'metaphysical', 'quasihistoric', 'undesirably', 'soporiferous', 'underrespected', 'unsymmetrical', 'reliberating', 'curability', 'nonrevolution', 'nonscientific', 'marbleization', 'wearability', 'supervexation', 'misconjugating', 'inattentiveness', 'unruinable', 'incorporeal', 'stereoscopic', 'overpolicing', 'noncombustible', 'communicable', 'janitorial', 'etymologist', 'unconnectedness', 'personality', 'unmaintainable', 'geodesical', 'sociologist', 'fortitudinous', 'elimination'],
        ['disaffiliated', 'redeemability', 'misauthorization', 'renegotiated', 'zootomically', 'microbacteria', 'malleability', 'intermediaries', 'supportability', 'eliminatory', 'nonhierarchical', 'quasiadvantageous', 'palaeontology', 'typographically', 'radioactively', 'hyperpotassemic', 'collapsibility', 'selfdramatization', 'hallucinatory', 'megalomania', 'communicativeness', 'quasisatirical', 'nontechnological', 'electrosensitive', 'overintensity', 'excommunicating', 'fundamentality', 'photoelectrical', 'visualization', 'incommensurable', 'noncontinuity', 'etymological', 'overemotional'],
        ['electrometallurgist', 'discreditability', 'nonperfectibility', 'etherealization', 'inexhaustibility', 'unautomatically', 'overdeliberated', 'nonuniversality', 'encyclopaedically', 'paradoxicality', 'hieroglyphically', 'hypercivilization', 'biogenetically', 'incompatibility', 'unconstitutionalism', 'unutilitarian', 'overidealizing', 'transcendentalization']
        ]
    if syllables not in range(1,8):
        return None
    else:
        word = available_words[syllables-1][random.randint(1, len(available_words[syllables-1])-1)]
    return word


def generate_line(syllables_in_line):
    syllables = 0
    string = ''
    while syllables < syllables_in_line:
        new_num = syllables_in_line - syllables
        random_num = random.randint(1, new_num)
        string += generate_word(random_num)
        syllables += random_num
        string += ' '
    return string


def generate_lines(all_lines):
    poem = ''
    for i in range(len(all_lines)):
        poem += generate_line(all_lines[i])
        poem += '\n'
    return poem



# Generate a poem

choice = input('I would like to write some poetry for you. Would you like a... \n * (h)aiku \n * (t)anka \n * (r)andom '
               '5 line poem, or do you want to \n * (s)pecify lines and syllables for each line?\n> ')

if choice == 'h':
    print('Here is your poem (5-7-5) \n=====')
    print(generate_lines([5,7,5]))
elif choice == 't':
    print('Here is your poem (5-7-5-7-7) \n=====')
    print(generate_lines([5,7,5,7,7]))
elif choice == 'r':
    line1 = random.randint(1,7)
    line2 = random.randint(1,7)
    line3 = random.randint(1,7)
    line4 = random.randint(1,7)
    line5 = random.randint(1,7)
    print(f'Here is your poem ({line1}-{line2}-{line3}-{line4}-{line5}) \n=====')
    print(generate_lines([line1, line2, line3, line4, line5]))

elif choice == 's':
    count = 1
    specified_poem = ''
    while True:
        num_syllables = int(input(f'How many syllables for line(s) {count}?\n> '))
        yes_or_nah = input(f'There are currently {count} line(s). Add another line (y/n)?\n> ')
        specified_poem += generate_line(num_syllables)
        specified_poem += '\n'
        if yes_or_nah == 'y':
            count += 1
            # num_syllables = int(input(f'How many syllables for lines {count}?\n> '))
        else:
            break
    print(specified_poem)
else:
    print('ERROR')
    print('A crash reduces \nYour expensive computer \nTo a simple stone.')
