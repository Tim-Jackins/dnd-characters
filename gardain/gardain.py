"""This file describes the heroic adventurer Fighter1.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Gardain"
player_name = "Ben"

# Be sure to list Primary class first
classes = ['Fighter']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1]  # ex: [10] or [3, 2]
subclasses = []  # ex: ['Necromacy'] or ['Thief', None]
background = 'Acolyte'
race = 'Mountain dwarf'
alignment = 'Lawful Good'

xp = 0
hp_max = 13
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 17
dexterity = 10
constitution = 16
intelligence = 13
wisdom = 12
charisma = 8

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = (
  'insight',
  'religion',
  'athletics',
  'history'
)

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()


# Dwarven Combat Training

features = ('great-weapon fighting')

# feature_choices = ('great-weapon fighting')

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ("Artisan's tools: Mason", )  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = ', '.join([
  # Race
  'Common',
  'Dwarvish',
  # Background
  'Halfling',
  'Orc'
])

# Inventory
cp = 0
sp = 20
ep = 0
gp = 8
pp = 0

weapons = ('maul', 'halberd', 'light crossbow')
magic_items = ()
armor = "chain mail"
shield = '' # Eg "shield"

equipment = ', '.join([
  'Chain mail'
  'Maul'
  'Halberd'
  'Light crossbow'
  '20 bolts'
  'Dungeoneer\'s pack'
  'Holy symbol'
  'Prayer book'
  '5 Sticks of incense'
  'Vestments'
  'Set of common clothes'
  'Pouch with coins'
])

attacks_and_spellcasting = '''
Maul:
  (Action, two-handed melee weapon)
  Hit: 1d20 + 5
  (Proficiency bonus + Strength modifier = 2 + 3 = 5)
  Damage: 2d6 + 3
  (Strength modifier = 3)
'''

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
I am tolerant of other faiths and respect the worship of other gods.
'''

ideals = '''
Tradition. "The ancient traditions of worship and sacrifice must be preserved and upheld."
'''

bonds = '''
I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.
'''

flaws = '''
I am suspicious of strangers and expect the worst of them.
'''

features_and_traits = '''
Gardain is born and raised in city of Telos. He has spent most of his life as
guard in local temple. He is very dedicated to find and learn about ancient
temples and holy relics.
'''
