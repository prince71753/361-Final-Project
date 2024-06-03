import numpy as np
from scipy.optimize import minimize

\
#have to go through and state which items cannot be with with other items

#Name	0: AD	1: AP	2: AS	3:CRIT	4: (MAG, LETH) PEN 	5: H+S POWER	6: LIFE + ONIVAMP STEAL	 7:HASTE	8:MANA	9:MANA REG	10:HEALTH	11:HEALTH REGEN	 12: MOVESPEED	13:ARMOR	14:MR	15:TENACITY	 16:COST	17:GOLD GEN	 18:CRIT DMG	19:UTILITY					
# !!!! TOOK OUT THE STARTER SUPPORT ITEMS!
items = {
"Zhonya's Hourglass":	[0,	120,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	50,	0,	0,	3250,	0,	0,	100],
"Zeke's Convergence":	[0,	0,	0,	0,	0,	0,	0,	10,	0,	0,	300,	0,	0,	25,	25,	0,	2200,	0,	0,	40],
"Yun Tal Wildarrows":	[65,	0,	0,	25,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3200,	0,	0,	60],
"Youmuu's Ghostblade": 	[60,	0,	0,	0,	18,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2700,	0,	0,	30],
"Wit's End":	[0,	0,	55,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	50,	20,	2800,	0,	0,	10],
"Winter's Approach":	[0,	0,	0,	0,	0,	0,	0,	15,	500,	0,	550,	0,	0,	0,	0,	0,	2400,	0,	0,	20],
"Warmog's Armor":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1000,	100,	5,	0,	0,	0,	3100,	0,	0,	40],
"Voltaic Cyclosword":	[55,	0,	0,	0,	18,	0,	0,	15,	0,	0,	0,	0,	0,	0,	0,	0,	2900,	0,	0,	10],
"Void Staff":	[0,	80,	0,	0,	40,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3000,	0,	0,	10],
"Vigilant Wardstone":	[0,	20,	0,	0,	0,	0,	0,	0,	0,	0,	250,	0,	0,	25,	30,	0,	2300,	0,	0,	80],
"Unending Despair":	[0,	0,	0,	0,	0,	0,	0,	10,	0,	0,	400,	0,	0,	55,	0,	0,	2800,	0,	0,	60],
"Umbral Glaive":	[50,	0,	0,	0,	15,	0,	0,	15,	0,	0,	0,	0,	0,	0,	0,	0,	2600,	0,	0,	50],
"Trinity Force":	[45,	0,	33,	0,	0,	0,	0,	20,	0,	0,	300,	0,	0,	0,	0,	0,	3333,	0,	0,	30],
"Trailblazer":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	200,	0,	5,	40,	0,	0,	2500,	0,	0,	10],
"Titanic Hydra":	[50,	0,	0,	0,	0,	0,	0,	0,	0,	0,	550,	0,	0,	0,	0,	0,	3300,	0,	0,	80],
"Thornmail":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	350,	0,	0,	70,	0,	0,	2700,	0,	0,	30],
"The Collector":	[60,	0,	0,	25,	12,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3200,	0,	0,	40],
"Terminus":	[35,	0,	35,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3000,	0,	0,	30],
"Sunfire Aegis":	[0,	0,	0,	0,	0,	0,	0,	10,	0,	0,	350,	0,	0,	50,	0,	0,	2700,	0,	0,	80],
"Sundered Sky":	[45,	0,	0,	0,	0,	0,	0,	15,	0,	0,	450,	0,	0,	0,	0,	0,	3100,	0,	0,	30],
"Stridebreaker":	[50,	0,	30,	0,	0,	0,	0,	0,	0,	0,	450,	0,	0,	0,	0,	0,	3300,	0,	0,	60],
"Stormsurge":	[0,	95,	0,	0,	10,	0,	0,	0,	0,	0,	0,	0,	8,	0,	0,	0,	2900,	0,	0,	40],
"Sterak's Gage":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	400,	0,	0,	0,	0,	20,	3200,	0,	0,	30],
"Statikk Shiv":	[55,	0,	45,	0,	0,	0,	0,	0,	0,	0,	0,	0,	7,	0,	0,	0,	2880,	0,	0,	25],
"Staff of Flowing Water":	[0,	40,	0,	0,	0,	8,	0,	15,	0,	125,	0,	0,	0,	0,	0,	0,	2300,	0,	0,	40],
"Spirit Visage":	[0,	0,	0,	0,	0,	0,	0,	10,	0,	0,	450,	100,	0,	0,	60,	0,	2900,	0,	0,	35],
"Rabadon's Deathcap":	[0,	140,	0,	0,	0,	0,	0,	0,	0,	0,	350,	0,	0,	75,	0,	0,	3600,	0,	0,	25],
"Randuin's Omen":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2700,	0,	0,	25],
"Rapid Firecannon":	[0,	0,	35,	25,	0,	0,	0,	0,	0,	0,	0,	0,	7,	0,	0,	0,	2600,	0,	0,	30],
"Ravenous Hydra":	[70,	0,	0,	0,	0,	0,	12,	20,	0,	0,	0,	0,	0,	0,	0,	0,	3300,	0,	0,	55],
"Redemption":	[0,	0,	0,	0,	0,	15,	0,	15,	0,	100,	200,	0,	0,	0,	0,	0,	2300,	0,	0,	40],
"Riftmaker":	[0,	80,	0,	0,	0,	0,	8,	15,	0,	0,	350,	0,	0,	0,	0,	0,	3100,	0,	0,	30],
"Rod of Ages":	[0,	50,	0,	0,	0,	0,	0,	0,	400,	0,	400,	0,	0,	0,	0,	0,	2600,	0,	0,	50],
"Runaan's Hurricane":	[0,	0,	40,	25,	0,	0,	0,	0,	0,	0,	0,	0,	7,	0,	0,	0,	2600,	0,	0,	20],
"Rylai's Crystal Scepter":	[0,	75,	0,	0,	0,	0,	0,	0,	0,	0,	400,	0,	0,	0,	0,	0,	2600,	0,	0,	20],
#"Seraph's Embrace":	[0,	80,	0,	0,	0,	0,	0,	25,	1000,	0,	0,	0,	0,	0,	0,	0,	2900,	0,	0,	25],
"Serpent's Fang":	[55,	0,	0,	0,	15,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2500,	0,	0,	15],
"Serylda's Grudge":	[45,	0,	0,	0,	15,	0,	0,	15,	0,	0,	0,	0,	0,	0,	0,	0,	3200,	0,	0,	15],
"Shadowflame":	[0,	120,	0,	0,	12,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3200,	0,	0,	40],
"Shurelya's Battlesong":	[0,	50,	0,	0,	15,	0,	0,	0,	0,	125,	0,	0,	5,	0,	0,	0,	2200,	0,	0,	20],
"Spear of Shojin":	[55,	0,	0,	0,	0,	0,	0,	20,	0,	0,	300,	0,	0,	0,	0,	0,	3100,	0,	0,	15],
"Profane Hydra":	[60,	0,	0,	0,	18,	0,	0,	20,	0,	0,	0,	0,	0,	0,	0,	0,	3300,	0,	0,	20],
"Phantom Dancer":	[0,	0,	60,	25,	0,	0,	0,	0,	0,	0,	0,	0,	12,	0,	0,	0,	2600,	0,	0,	5],
"Overlord's Bloodmail":	[40,	0,	0,	0,	0,	0,	0,	0,	0,	0,	500,	0,	0,	0,	0,	0,	3300,	0,	0,	10],
"Opportunity":	[55,	0,	0,	0,	18,	0,	0,	0,	0,	0,	0,	0,	5,	0,	0,	0,	2700,	0,	0,	10],
"Navori Flickerblade":	[0,	0,	40,	25,	0,	0,	0,	0,	0,	0,	0,	0,	7,	0,	0,	0,	2600,	0,	0,	15],
"Nashor's Tooth":	[0,	90,	50,	0,	0,	0,	0,	15,	0,	0,	0,	0,	0,	0,	0,	0,	3000,	0,	0,	15],
"Muramana":	[35,	0,	0,	0,	0,	0,	0,	15,	860,	0,	0,	0,	0,	0,	0,	0,	2900,	0,	0,	15],
"Mortal Reminder":	[40,	0,	0,	25,	35,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3000,	0,	0,	20],
"Morellonomicon":	[0,	90,	0,	0,	0,	0,	0,	15,	0,	0,	0,	0,	0,	0,	0,	0,	2200,	0,	0,	20],
"Moonstone Renewer":	[0,	30,	0,	0,	0,	0,	0,	20,	0,	125,	250,	0,	0,	0,	0,	0,	2200,	0,	0,	20],
"Mikael's Blessing":	[0,	0,	0,	0,	0,	12,	0,	15,	0,	100,	250,	0,	0,	0,	0,	0,	2300,	0,	0,	10],
"Mercurial Scimitar":	[40,	0,	0,	0,	0,	0,	10,	0,	0,	0,	0,	0,	0,	0,	50,	0,	3300,	0,	0,	10],
"Mejai's Soulstealer":	[0,	20,	0,	0,	0,	0,	0,	0,	0,	0,	100,	0,	0,	0,	0,	0,	1500,	0,	0,	25],
"Maw of Malmortius":	[0,	70,	0,	0,	0,	0,	0,	15,	0,	0,	0,	0,	0,	0,	40,	0,	3100,	0,	0,	30],
"Manamune":	[35,	0,	0,	0,	0,	0,	0,	15,	500,	0,	0,	0,	0,	0,	0,	0,	2900,	0,	0,	15],
"Malignance":	[0,	80,	0,	0,	0,	0,	0,	25,	600,	0,	0,	0,	0,	0,	0,	0,	2700,	0,	0,	20],
"Horizon Focus":	[0,	90,	0,	0,	0,	0,	0,	20,	0,	0,	0,	0,	0,	0,	0,	0,	2700,	0,	0,	15],
"Hubris":	[60,	0,	0,	0,	18,	0,	0,	15,	0,	0,	0,	0,	0,	0,	0,	0,	3000,	0,	0,	15],
"Hullbreaker":	[65,	0,	0,	0,	0,	0,	0,	0,	0,	0,	350,	0,	5,	0,	0,	0,	3000,	0,	0,	20],
"Iceborn Gauntlet":	[0,	0,	0,	0,	0,	0,	0,	15,	0,	0,	300,	0,	0,	50,	0,	0,	2600,	0,	0,	10],
"Immortal Shieldbow":	[55,	0,	0,	25,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3000,	0,	0,	30],
"Imperial Mandate":	[0,	60,	0,	0,	0,	0,	0,	20,	0,	125,	0,	0,	0,	0,	0,	0,	2300,	0,	0,	10],
"Infinity Edge":	[80,	0,	0,	25,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3400,	0,	40,	0],
"Jak'Sho, The Protean":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	300,	0,	0,	50,	50,	0,	3200,	0,	0,	45],
"Kaenic Rookern":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	400,	150,	0,	0,	80,	0,	2900,	0,	0,	20],
"Knight's Vow":	[0,	0,	0,	0,	0,	0,	0,	10,	0,	0,	200,	100,	0,	40,	0,	0,	2200,	0,	0,	5],
"Kraken Slayer":	[500,	0,	40,	0,	0,	0,	0,	0,	0,	0,	0,	0,	7,	0,	0,	0,	3100,	0,	0,	10],
"Liandry's Torment":	[0,	90,	0,	0,	0,	0,	0,	0,	0,	0,	300,	0,	0,	0,	0,	0,	3000,	0,	0,	5],
"Lich Bane":	[0,	100,	0,	0,	0,	0,	0,	15,	0,	0,	0,	0,	8,	0,	0,	0,	3100,	0,	0,	20],
"Locket of the Iron Solari":	[0,	0,	0,	0,	0,	0,	0,	10,	0,	0,	200,	0,	0,	30,	30,	0,	2200,	0,	0,	15],
"Lord Dominik's Regards":	[45,	0,	0,	25,	40,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3000,	0,	0,	10],
"Luden's Companion":	[0,	95,	0,	0,	0,	0,	0,	25,	600,	0,	0,	0,	0,	0,	0,	0,	2900,	0,	0,	5],
"Hollow Radiance":	[0,	0,	0,	0,	0,	0,	0,	10,	0,	0,	450,	100,	0,	0,	40,	0,	2800,	0,	0,	5],
"Hextech Rocketbelt":	[0,	70,	0,	0,	0,	0,	0,	15,	0,	0,	300,	0,	0,	0,	0,	0,	2600,	0,	0,	5],
"Heartsteel":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	900,	200,	0,	0,	0,	0,	3000,	0,	0,	15],
"Guinsoo's Rageblade":	[35,	35,	25,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3000,	0,	0,	10],
"Guardian Angel":	[55,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	45,	0,	0,	3200,	0,	0,	30],
"Frozen Heart":	[0,	0,	0,	0,	0,	0,	0,	20,	400,	0,	0,	0,	0,	65,	0,	0,	2500,	0,	0,	10],
"Force of Nature":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	400,	0,	5,	55,	0,	0,	2800,	0,	0,	15],
"Fimbulwinter":	[0,	0,	0,	0,	0,	0,	0,	15,	860,	0,	550,	0,	0,	0,	0,	0,	2400,	0,	0,	10],
"Experimental Hexplate":	[55,	0,	25,	0,	0,	0,	0,	0,	0,	0,	300,	0,	0,	0,	0,	0,	3000,	0,	0,	20],
"Essence Reaver":	[70,	0,	0,	25,	0,	0,	0,	25,	0,	0,	0,	0,	0,	0,	0,	0,	3100,	0,	0,	15],
"Edge of Night":	[50,	0,	0,	0,	15,	0,	0,	0,	0,	0,	250,	0,	0,	0,	0,	0,	2800,	0,	0,	10],
"Eclipse":	[70,	0,	0,	0,	0,	0,	0,	15,	0,	0,	0,	0,	0,	0,	0,	0,	2800,	0,	0,	15],
"Echoes of Helia":	[0,	40,	0,	0,	0,	0,	0,	20,	0,	125,	200,	0,	0,	0,	0,	0,	2200,	0,	0,	20],
"Death's Dance":	[60,	0,	0,	0,	0,	0,	0,	15,	0,	0,	0,	0,	0,	40,	0,	0,	3200,	0,	0,	10],
"Dead Man's Plate":	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	300,	0,	5,	45,	0,	0,	2900,	0,	0,	10],
"Abyssal Mask":	[0,	0,	0,	0,	0,	0,	0,	10,	0,	0,	300,	0,	0,	0,	50,	0,	2300,	0,	0,	30],
"Archangel's Staff":	[0,	80,	0,	0,	0,	0,	0,	25,	600,	0,	0,	0,	0,	0,	0,	0,	2900,	0,	0,	20],
"Ardent Censer":	[0,	50,	0,	0,	0,	8,	0,	0,	0,	125,	0,	0,	8,	0,	0,	0,	2300,	0,	0,	15],
"Axiom Arc":	[55,	0,	0,	0,	18,	0,	0,	25,	0,	0,	0,	0,	0,	0,	0,	0,	3000,	0,	0,	10],
"Banshee's Veil":	[0,	120,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	50,	0,	3100,	0,	0,	5],
"Black Cleaver":	[55,	0,	0,	0,	0,	0,	0,	20,	0,	0,	400,	0,	0,	0,	0,	0,	3000,	0,	0,	20],
"Blackfire Torch":	[0,	90,	0,	0,	0,	0,	0,	25,	600,	0,	0,	0,	0,	0,	0,	0,	2800,	0,	0,	15],
"Blade of the Ruined King":	[55,	0,	30,	0,	0,	0,	10,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3200,	0,	0,	20],
"Bloodthirster":	[80,	0,	0,	0,	0,	0,	18,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3400,	0,	0,	5],
"Chempunk Chainsword":	[55,	0,	0,	0,	0,	0,	0,	0,	15,	0,	250,	0,	0,	0,	0,	0,	2800,	0,	0,	15],
"Cosmic Drive":	[0,	80,	0,	0,	0,	0,	0,	25,	0,	0,	250,	0,	5,	0,	0,	0,	3000,	0,	0,	15],
"Cryptbloom":	[0,	70,	0,	0,	30,	0,	0,	15,	0,	0,	0,	0,	0,	0,	0,	0,	2850,	0,	0,	25],
"Dawncore":	[0,	0,	60,	0,	0,	16,	0,	0,	0,	100,	0,	0,	0,	0,	0,	0,	2700,	0,	0,	5]
}

# Convert the items dictionary to a list for easier indexing
item_names = list(items.keys())
item_attributes = np.array(list(items.values()))

def objective(x):
    attributes = np.dot(x, item_attributes)
    utility = attributes[15] + attributes[12] + attributes[5] + attributes[7] + attributes[19]
    ap_dmg = 3 * attributes[1] + attributes[4] - attributes[0]
    ad_dmg = 3 * attributes[0] + attributes[2] + attributes[4]+ attributes[3] + attributes[18] 
    ad_damage_scale =  attributes[2]   + .5* attributes[6]
    gen_resource_scale = attributes[8] + attributes[9] + attributes[11]
    gold = attributes[17]
    tankiness = .3*attributes[10]  + attributes[14] + attributes[13]

    cost = attributes[16] + 1e-6  # avoid division by zero
      # We negate because we want to maximise since the function minimised
    #return   - ( ap_dmg + tankiness + utility) /cost # for mord top
    #return - ( ad_dmg + tankiness + utility) /cost # for ad tops
    #return - (ap_dmg + utility ) / cost # for mid
   #return - (ad_dmg + tankiness + ad_damage_scale)/ cost # for ad jg
    #return -(ad_dmg +  ad_damage_scale) /cost # for bot
    return - (utility + tankiness) / cost  # for support

# Define constraints: item counts must be non-negative integers and we must select exactly 6 items
def constraint_sum(x):
    return np.sum(x) - 6  # forces sum to be 6 which in conjunction with the constraints always outputs 6 items
# Max build is 6 items in the game

constraints = [{'type': 'eq', 'fun': constraint_sum}]

# Initial guess: random initial item counts
initial_guess = np.zeros(len(item_names))
initial_guess[:6] = 1
np.random.shuffle(initial_guess) # Starting with 0 or 1 items of each type and then to make the guess
# we shuffle that 1 around other wise, we can't enforce the above constraint 

# Bounds for each item: 0 or 1 (cannot have more than one of the same item in this example)
bounds = [(0, 1) for _ in range(len(items))]

# Optimize
result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

# Extract optimized solution
optimized_build = np.round(result.x).astype(int)
total_cost = np.dot(optimized_build, item_attributes[:, 16])

# Print optimized build
print("Optimized Build:")
for item, count in zip(item_names, optimized_build):
    if count > 0:
        print(f"{count} x {item}")
print(f"Total Cost of the Build: {total_cost}")

        
