dungeonsheets_version = "0.9.4"

name = "Xanaphia (Xana)"
player_name = "Erin"

# Be sure to list Primary class first
classes = ['Wizard']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1]  # ex: [10] or [3, 2]
subclasses = [None]  # ex: ['Necromacy'] or ['Thief', None]
background = "Acolyte"
race = "High elf"
alignment = "Chaotic good"

xp = 75
hp_max = 8
inspiration = 0

# Ability Scores
strength = 10
dexterity = 15
constitution = 14
intelligence = 16
wisdom = 12
charisma = 8

# Select what skills you're proficient with
skill_proficiencies = ('arcana', 'insight', 'investigation', 'religion')

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
weapon_proficiencies = ()
_proficiencies_text = ()

# Proficiencies and languages
languages = """Common, Elvish, Draconic, Dwarfish, Goblin"""

# Inventory
cp = 4
sp = 9
ep = 0
gp = 4
pp = 2

weapons = ('shortsword')
magic_items = ()
armor = None
shield = None

equipment = """Shortsword, component pouch, spellbook, backpack, bottle
of ink, ink pen, 10 sheets of parchment, small knife, tome of historical
lore, holy symbol, prayer book, set of common clothes, pouch."""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ('mage hand', 'prestidigitation', 'ray of frost', 'shocking grasp', 'magic missile', 'mage armor')

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = '''I use polysyllabic words that convey the impression
of erudition. Also, I've spent so long in the temple that I have little
experience dealing with people on a casual basis.'''

ideals = '''Knowledge. The path to power and self-improvement is through
knowledge.'''

bonds = '''The tome I carry with me is the record of my life's work so far,
and no vault is secure enough to keep it safe.'''

flaws = '''I'll do just about anything to uncover historical secrets that
would add to my research.'''

features_and_traits = ''''''
