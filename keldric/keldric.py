dungeonsheets_version = "0.9.4"

name = "Keldric"
player_name = "David"

# Be sure to list Primary class first
classes = ['Fighter']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1]  # ex: [10] or [3, 2]
subclasses = [None]  # ex: ['Necromacy'] or ['Thief', None]
background = "Folk hero"
race = "Lightfoot halfling"
alignment = "Neutral"

xp = 75
hp_max = 9
inspiration = 0

# Ability Scores
strength = 8
dexterity = 16
constitution = 12
intelligence = 13
wisdom = 10
charisma = 16

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('acrobatics', 'deception', 'investigation', 'performance', 'sleight of hand', 'stealth')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ('Archery')

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = '''Common, Elvish'''

# Inventory
cp = 4
sp = 9
ep = 0
gp = 29
pp = 0

# Put your equipped weapons and armor here
weapons = ('greatsword', 'longbow')
magic_items = ()
armor = 'Leather armor'
shield = None

equipment = '''Leather armor, longbow, 20 arrows, greatsword, backpack, bedroll,
messkit, tinderbox, 10 torches, 10 days of rations, waterskin, 50 feet of
hempen rope, carpenter's tools, shovel, iron pot, set of common clothes, pouch'''

attacks_and_spellcasting = '''You can shoot your longbow 150 feet, or up to
600 feet with disadvantage on the attack roll.'''

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
personality_traits = '''When I set my mind to something, I follow through.
Also, I use long words in an attempt to sound smarter.'''

ideals = '''Sincerity, It's no good pretending to be something I'm not.'''

bonds = '''One day, Thundertree will be a prosperous town again. A
statue of me will stand in the town square.'''

flaws = '''I'm convinced of the significance of my destiny, and blind
to my shortcomings and the rick of failure.'''

features_and_traits = ''''''
