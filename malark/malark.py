dungeonsheets_version = "0.9.4"

name = "Malark"
player_name = "Ben"


classes = ['Rogue']
levels = [1]
subclasses = ['']
background = 'Criminal'
race = 'Lightfoot Halfling'
alignment = 'Chaotic Good'

xp = 0
hp_max = 10
inspiration = 0

# Ability Scores
strength = 11
dexterity = 16
constitution = 14
intelligence = 9
wisdom = 13
charisma = 15

skill_proficiencies = (
  # Background
  'stealth',
  'deception',
  # Class
  'acrobatics',
  'sleight of hand',
  'performance',
  'persuasion'
)

skill_expertise = (
  # Background
  'stealth',
  'deception'
)

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
# Disguise Kit, Forgery Kit, Thieves' Tools
# simple, Crossbow, hand, Longsword, Rapier, Shortsword
weapon_proficiencies = ()
_proficiencies_text = ('Dice Set', 'Thieves\' Tools')

# Proficiencies and languages
languages = ', '.join([
  'Halfling',
  'Thieves\' Cant',
  'Common'
])

# Inventory
cp = 0
sp = 30
ep = 0
gp = 12
pp = 0


weapons = ('shortsword', 'dagger', 'shortbow')
magic_items = ()
armor = 'Leather Armor'
shield = ''

equipment = ', '.join([
  'Leather armor',
  '2x Shortsword'
  '2x Dagger'
  'Thieves\' tools'
  'Dungeoneer\'s pack'
  'Crowbar'
  'Set of dark common clothes including a hood'
  'Pouch with coins'
])

attacks_and_spellcasting = '''
Shortsword:
  (Action, one-handed melee weapon)
  Shortsword has "finesse" attribute so dexterity modifier is used for attack and damage rolls.
  Hit: 1d20 + 5
  (Proficiency bonus + Dexterity modifier = 2 + 3 = 5)
  Damage: 1d6 + 3
  (Dexterity modifier = 3)

Shortsword:
  (Bonus action, one-handed melee weapon)
  Shortsword has "finesse" attribute so dexterity modifier is used for attack and damage rolls.
  Shortsword has "light" attribute so it can be used as bonus action.
  Hit: 1d20 + 5
  (Proficiency bonus + Dexterity modifier = 2 + 3 = 5)
  Damage: 1d6
  (Dexterity modifier not addeed for bonus action)
'''

# Backstory
# Describe your backstory here
personality_traits = '''
I would rather make new friend than new enemy.
'''

ideals = '''
Freedom. "Chains are meant to be broken, as those who would forge them."
'''

bonds = '''
My ill-gotten gains go to support my family.
'''

flaws = '''
An innocent person is in prison for a crime that I commited. I'm okay with that.
'''

features_and_traits = '''
Malark is born and raised in city of Baldur's Gate. He established connections
to local criminals at young age. He has travelled lot and made living by
smuggling narcotics between harbour towns.

Hook: Malark is search of more money when he here's that the house of mercenaries are willing to pay 1000gp for the capture
(dead or alive) of "One-eye" the pirate.
'''
