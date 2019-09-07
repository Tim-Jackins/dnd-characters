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
hp_max = 12
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
features = ()

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

equipment = """TODO: Buy some stuff at the start of the quest."""

attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

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
personality_traits = """TODO: Describe my personality traits."""

ideals = """TODO: What does your character believe in?"""

bonds = """TODO: Describe what debts your character has to pay,
and other commitments or ongoing quests they have."""

flaws = """TODO: Describe your characters interesting flaws.
"""

features_and_traits = """None."""
