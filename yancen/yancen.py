"""This file describes the heroic adventurer Fighter1.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Yancen Leatop"
player_name = "Jack T."

# Be sure to list Primary class first
classes = ['Rogue']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1]  # ex: [10] or [3, 2]
subclasses = ['Thief']  # ex: ['Necromacy'] or ['Thief', None]
background = 'Acolyte'
race = 'Lightfoot Halfling'
alignment = 'Chaotic Neutral'

xp = 0
hp_max = 13
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 7
dexterity = 14
constitution = 12
intelligence = 8
wisdom = 15
charisma = 10

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = (
  # Acolyte
  'insight',
  'religion',
  # Rogue
  'Acrobatics',
  'Perception',
  'Sleight of Hand',
  'Stealth',
)

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()


# Dwarven Combat Training
features = ()

# feature_choices = ('great-weapon fighting')

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ("thieves' tools", )  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = ', '.join([
  # Race
  'Common',
  'Halfling',
  # Background
  'Goblin',
  'Dwarvish',
])

# Inventory
cp = 0
sp = 0
ep = 0
gp = 15
pp = 0

weapons = ('rapier', 'dagger', 'shortbow')
magic_items = ()
armor = 'leather armor'
shield = '' # Eg "shield"

equipment = '''
Rapier
Short bow
20 Arrows
Burglar's Pack
Leather Armor
Two daggers
Thieves' Tools
Velvet Mask Stained Red
A prayer book
5 sticks of incense
Vestments
Common clothes
Belt Pouch
'''

attacks_and_spellcasting = ''

# List of known spells
spells_prepared = ()

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()

# Backstory
# Describe your backstory here
personality_traits = '''
I quote (or misquote) sacred texts and proverbs in almost every situation.
'''

ideals = '''
Aspiration. I seek to prove myself worthy of my god's favor by matching my actions against his or her teachings. (Any)
'''

bonds = '''
Everything I do is for the common people.
'''

flaws = '''
In order to feel closer to my god I have an intense urge to rob and thief from everyone.
'''

features_and_traits = '''

'''
