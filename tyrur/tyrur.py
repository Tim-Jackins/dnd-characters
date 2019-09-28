dungeonsheets_version = "0.9.4"

name = "Tyrur Goldstein"
player_name = "Warren"

# Be sure to list Primary class first
classes = ['Cleric']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1]  # ex: [10] or [3, 2]
subclasses = [None]  # ex: ['Necromacy'] or ['Thief', None]
background = "Soldier"
race = "Hill dwarf"
alignment = "Neutral good"

xp = 75
hp_max = 11
inspiration = 0

# Ability Scores
strength = 14
dexterity = 8
constitution = 15
intelligence = 10
wisdom = 16
charisma = 12

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('athletics', 'intimidation', 'medicine', 'religion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ('discipline of life')

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Dwarvish"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 10
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ('warhammer', 'handaxe')  # Example: ('shortsword', 'longsword')
magic_items = ()
armor = 'chain mail'
shield = 'shield'

equipment = """chain mail*, shield, warhammer, 2 handaxes, holy symbol, backpack,
crowbar, hammer, 10 pitons, 10 torches, tinderbox, 10 days of rations waterskin,
50 feet of hempen rope, mason's tools, dagger taken from a fallen enemy as a trophy,
deck of playing cards, set of common clothes, pouch, rank insignia (sergeant)

While wearing this armor, you have disadvantage on Dexterity (Stealth) checks.
"""

attacks_and_spellcasting = """Prepared Spells. You can prepare 4 1st-level spells."""

# List of known spells
spells_prepared = ('light', 'sacred flame', 'thaumaturgy', 'bless', 'cure wounds')

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Backstory
# Describe your backstory here
personality_traits = """I'm always polite and respectful. Also, I don't my gut feelings, so I tend to wait for others to act."""

ideals = """Respect, People deserve to be treated with dignity and courtes1
6y."""

bonds = """I have 3 cousins - Gundren, Tharden, and Nundro Rockseeker - who are my friends and cherished clan members."""

flaws = """I secretly wonder whether the gods care about mortal affairs at all."""

features_and_traits = """"""
