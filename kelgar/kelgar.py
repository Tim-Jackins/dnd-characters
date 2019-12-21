dungeonsheets_version = "0.9.4"

name = "Kelgar Ironfist"
player_name = "Mike"

# Be sure to list Primary class first
classes = ['Druid']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1]  # ex: [10] or [3, 2]
subclasses = [None]  # ex: ['Necromacy'] or ['Thief', None]
background = "Wanderer"
race = "Hill Dwarf"
alignment = "Neutral"

xp = 0
hp_max = 13
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 12
dexterity = 13
constitution = 16
intelligence = 8
wisdom = 16
charisma = 10

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('Medicine', 'Nature', 'Religion', 'Survival')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ('WildShape')

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Druidic"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

weapons = ('club', 'sickle')  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "hide armor"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """Leather armor, longbow, 20 arrows, greatsword, backpack, bedroll,
messkit, tinderbox, 10 torches, 10 days of rations, waterskin, 50 feet of
hempen rope, carpenter's tools, shovel, iron pot, set of common clothes, pouch."""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ('druidcraft', 'shillelagh')

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

wild_shapes = ['Wolf']

# Backstory
# Describe your backstory here
personality_traits = """"""

ideals = """"""

bonds = """"""

flaws = """"""

features_and_traits = """"""
