dungeonsheets_version = "0.9.4"

name = 'Mira Cherryblossom'
player_name = "Katherine"

classes = ['Druid']
levels = [1] # ex: [10] or [3, 2]
subclasses = []  # ex: ['Necromacy'] or ['Thief', None]
background = 'Outlander'
race = 'WoodElf'
alignment = 'Neutral good'

xp = 0
hp_max = 9
inspiration = 0 # integer inspiration value

# Ability Scores

strength     = 12 # +1
dexterity    = 13 # +1
constitution = 13 # +1
intelligence = 13 # +1
wisdom       = 14 # +2
charisma     = 9  # -1



# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = (
  'Arcana', 'Nature', # Chosen
  'perception', # Druid
  'athletics', 'survival' # Outlander
)


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
languages = '''Common, Elvish'''

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 40
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ('Scimitar', 'Shortbow')  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = 'Leather Armor'  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment_items = []
equipment_items += ['Shortbow', 'Scimitar'] # Weapons
equipment_items += ['Leather Armor'] # Armor
equipment_items += ['Backpack', 'Bedroll', 'Hempen Rope (50 feet)', 
                    'Mess Kit', 'Tinderbox', 'Torches (10)',
                    'Rations (10)', 'Waterskin', 'Wooden Staff'] # Explorers Pack
equipment_items += ['Hunting Trap', 'Owlbear Bone Ring', 'Travelers Clothes',
                    'Belt pouch'] # Outlander supplies

equipment = ', '.join(equipment_items)

attacks_and_spellcasting = ''''''

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ('Produce Flame', 'Mending')  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = '''I have a lesson for every situation drawn from observing nature.'''

ideals = '''Nature: The natural world is more imprtant than all the contructs of civilization.'''

bonds = '''I suffer awful visions of a coming disaster and will do anything to prevent it.'''

flaws = '''I remember every insult I've ever received and and nurse a silent resentment toward anyone who's ever wronged me.'''

features_and_traits = ''''''
