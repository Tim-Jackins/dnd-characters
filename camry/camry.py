dungeonsheets_version = "0.9.4"

name = "Camry Wheeze"
player_name = "Brandy"

# Be sure to list Primary class first
classes = ['Fighter']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1]  # ex: [10] or [3, 2]
subclasses = [None]  # ex: ['Necromacy'] or ['Thief', None]
background = "Noble"
race = "Human"
alignment = "Lawful neutral"

xp = 75
hp_max = 12
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 16
dexterity = 9
constitution = 15
intelligence = 11
wisdom = 13
charisma = 14

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('athletics', 'history', 'perception', 'persuasion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ('all armor', 'shields', 'simple weapons', 'martial weapons', 'playing cards')

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ('second wind')

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ('defense',)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Draconic, Dwarvish"""

# Inventory
cp = 4
sp = 9
ep = 0
gp = 44
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ('greataxe', 'javelin')  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "chain mail"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """Chain mail, greataxe, 3 javelins, backpack, blanket, tinderbox,
3 days of rations, waterskin, set of fine clothes, signet ring, scroll of pedigree,
shortbow, 5 arrows"""

attacks_and_spellcasting = ''''''

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
personality_traits = """My flattery makes those I talk to feel
wonderful and important. Also I don't like to get dirty, and
I won't be caught dead in unsuitable accomodations"""

ideals = """Responsibility. It's the duty of a noble to protect the common people, not bully them."""

bonds = """My Greataxe is a family heirloom, and it's by far my most precious possession."""

flaws = """I have a hard time resisting the allure of wealth, especially gold. Wealth can help me restore my legacy."""

features_and_traits = """"""
