dungeonsheets_version = "0.9.4"

name = 'Marg'
player_name = 'Ben'

# Be sure to list Primary class first
classes = ['Cleric']
levels = [1]
subclasses = ['Life Domain']
background = 'Soldier'
race = 'Human'
alignment = 'Lawful Neutral'

xp = 0
hp_max = 10
inspiration = 0

# Ability Scores
strength = 14
dexterity = 11
constitution = 15
intelligence = 9
wisdom = 16
charisma = 13

skill_proficiencies = (
  # Background
  'athletics',
  'intimidation',
  # Class
  'medicine',
  'insight'
)

skill_expertise = ()

features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = (
  'Tool proficiency - Dice set',
  'Tool proficiency - Vehicles (Land)'
)

# Proficiencies and languages
languages = 'Celestial, Infernal, Common'

# Inventory
cp = 0
sp = 20
ep = 0
gp = 8
pp = 0

weapons = ('Mace', 'Light Crossbow')
magic_items = ()
armor = 'Chain mail'
shield = 'Shield'

equipment = ', '.join([
  'Mace',
  'Chain mail',
  'Light crossbow',
  '20 Bolts',
  'Shield',
  'Holy symbol (Eldath)',
  'Priest\'s pack',
  'Insignia of rank',
  'Piece of a banner (Trophy from fallen enemy)',
  'Set of bone dice',
  'Set of common clothes',
  'Pouch with coins',
])

attacks_and_spellcasting = '''
Mace:
  (Action, one-handed melee weapon)
  Hit: 1d20 + 4
  (Proficiency bonus + Strength modifier = 2 + 2 = 4)
  Damage: 1d6 + 2
  (Strength modifier = 2)
'''

spells_prepared = (
  # Cantrips
  'Light',
  'Mending',
  'Spare the Dying',

  # 1st level
  'Bless',
  'Cure Wounds',
  'Guiding Bolt',
  'Healing Word'
)

__spells_unprepared = (
  # Cantrips
  # 'Guidance',
  # 'Light',
  # 'Mending',
  # 'Resistance',
  # 'Sacred Flame',
  # 'Spare the Dying',
  # 'Thaumaturgy',

  # 1st
  'Bane',
  'Bless',
  'Command',
  'Create or Destroy Water',
  'Cure Wounds',
  'Detect Evil and Good',
  'Detect Magic',
  'Detect Poison and Disease',
  'Guiding Bolt',
  'Healing Word',
  'Inflict Wounds',
  'Protection from Evil and Good',
  'Purify Food and Drink',
  'Sanctuary',
  'Shield of Faith'
)

spells = spells_prepared + __spells_unprepared

# Backstory
# Describe your backstory here
personality_traits = '''
I am always polite and respectful.
'''

ideals = '''
Responsibility. I do what I must and obey just authority.
'''

bonds = '''
Those who fight beside me are those worth dying for.
'''

flaws = '''
I obey the law even if the law causes misery.
'''

features_and_traits = '''
Sanih is born and raised in Calimport. She has served in temple of Waukeen
and as healer in local army. She hopes to earn good amount of money as adventurer.

Hook: She heard the house of mercenaries are willing to pay 1000gp for the capture
(dead or alive) of "One-eye" the pirate.
'''
