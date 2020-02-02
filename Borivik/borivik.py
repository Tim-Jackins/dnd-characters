dungeonsheets_version = "0.9.4"

name = 'Borivik'
player_name = 'Jack Timmins'

classes = ['Sorceror']
levels = [1]
subclasses = ['Draconic Bloodline']
background = 'Acolyte'
race = 'Rashemi'
alignment = 'Lawful Neutral'

xp = 0
hp_max = 9
inspiration = 0

# Ability Scores
strength = 9
dexterity = 15
constitution = 14
intelligence = 12
wisdom = 10
charisma = 15

skill_proficiencies = ('arcana', 'insight', 'intimidation', 'religion')
skill_expertise = ()

features = ()
feature_choices = ()

weapon_proficiencies = ()
_proficiencies_text = ()

# Proficiencies and languages
languages = ', '.join([
    'Common',
    'Deep Speech',
    'Draconic',
    'Infernal',
    'Orc'
])

# Inventory
cp = 0
sp = 0
ep = 0
gp = 10
pp = 0

weapons = ('Dagger', 'Light Crossbow')
magic_items = ()
armor = 'No Armor'
shield = 'No Shield'

equipment = ', '.join([
    'Pouch (1)',
    'Clothes, common (1)',
    'Leather (1)',
    'Crossbow bolt (20)',
    'Waterskin (1)',
    'Bedroll (1)',
    'Incense (5)',
    'Rations (1 day) (10)',
    'Rope, hempen (1)',
    'Vestements (1)',
    'Tinderbox (1)',
    'Mess kit (1)',
    'Backpack (1)',
    'Torch (10)',
    'Explorer\'s Pack (1)',
    'Component pouch (1)',
    'A pendant with my holy symbol (1)'
])

attacks_and_spellcasting = ''

# List of known spells
spells_prepared = (
    # Cantrips
    'Chill Touch',
    'Fire Bolt',
    'True Strike',
    'Mold Earth',

    # 1st Level
    'False Life',
    'Ray of Sickness'
)
__spells_unprepared = ()

spells = spells_prepared + __spells_unprepared

# Backstory
# Describe your backstory here
personality_traits = '''Nothing can shake my optomistic attitude but what
lies underneath is a determination for vengence. While I am lawful
there are some evildoers who deserve to meet the gods.'''

ideals = '''I hope to rise above my station and gain enough power to become the
Zulkir of necromancy and defeat Aznar Thrul of Priador. My holy symbol
is a skelatal arm holding balanced scales (Kelemvor).'''

bonds = '''I owe my freedom to the mulan priest who saved me from
captivity and experimentation. I owe my power to a red dragon
whose blood runs through my veins.'''

flaws = '''Once I pick a goal, I become obsessed with it to the detriment
of my own life. I will sacrifice a great deal to obtain power.'''

features_and_traits = ''
