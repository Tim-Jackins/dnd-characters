dungeonsheets_version = "0.9.4"

name = "Finnan Goodbarrel"
player_name = "Katie"

# Be sure to list Primary class first
classes = ['Rogue']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1]  # ex: [10] or [3, 2]
subclasses = [None]  # ex: ['Necromacy'] or ['Thief', None]
background = "Criminal"
race = "Lightfoot halfling"
alignment = "Neutral"

xp = 75
hp_max = 9
inspiration = 0  # integer inspiration value

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
skill_expertise = ('sneak attack')

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ('thieves cant', 'lucky', 'brave', 'halfling nimbleness', 'naturally stealthy', 'criminal contact')

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Elvish, Common, Draconic"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ('shortsword', 'shortbow')  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "leather armor"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """TODO: list the equipment and magic items your character carries"""

attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ()  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = """I never have a plan, but I'm great at
making things up as I go along. Also, the best way to get me to
do something is to tell me I can't do it."""

ideals = """People. I'm loyal to my friends, not to any ideals.
Everyone else can take a trip on the River Styx for all I care."""

bonds = """Qelline Alderlead, my aunt, has a farm in Phandilin.
I always give her some of my ill-gotten gains."""

flaws = """My aunt must never know the deeds I did as a member
of the Redbrands."""

features_and_traits = """TODO: Describe other features and abilities your
character has."""