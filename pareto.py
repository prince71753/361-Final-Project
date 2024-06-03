import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

    #Name	0:Damage	1:Toughness	2:Control	3: Mobility	 4:Utility	 5:Classs	
characters = {
"AATROX":	[3,	3,	2,	2,	1.5,	5],
"AHRI":	[3,	1,	1.5,	3,	0.5,	2],
"AKALI":	[3,	0.5,	0,	2,	0,	3],
"AKSHAN":	[3,	1,	0,	3,	2,	1],
"ALISTAR":	[1,	3,	3,	1,	2,	4],
"AMUMU":	[2,	3,	3,	1,	1.5,	4],
"ANIVIA":	[3,	2,	3,	0,	1.5,	12],
"ANNIE":	[3,	1.5,	1.5,	1,	1,	2],
"APHELIOS":	[3,	0,	1.5,	0,	0.5,	1],
"ASHE":	[2,	0,	3,	0,	1.5,	1],
"AURELION SOL":	[3,	2,	2,	2,	1,	12],
"AZIR":	[3,	1.5,	2,	1.5,	0,	12],
"BARD":	[2,	1.5,	3,	2,	3,	11],
"BEL'VETH":	[3,	2,	2.5,	3,	0.5,	6],
"BLITZCRANK":	[1,	2.5,	3,	1,	1,	11],
"BRAND":	[3,	1,	2,	1,	1,	2],
"BRAUM":	[0,	3,	2,	1,	2,	10],
"BRIAR":	[2.5,	2,	3,	3,	1,	7],
"CAITLYN":	[3,	1,	2,	1,	0,	1],
"CAMILLE":	[3,	2,	2,	2,	0,	7],
"CASSIOPEIA":	[3,	1,	2,	1,	1,	12],
"CHO'GATH":	[2,	3,	2,	1.5,	1,	4],
"CORKI":	[2,	0,	0,	1,	0,	1],
"DARIUS":	[3,	2.5,	2.5,	1,	0,	5],
"DIANA":[3,	2,	2,	2,	1,	3],
"DR. MUNDO":	[2,	2.5,	0,	0,	0,	5],
"DRAVEN":	[3,	1,	0,	2,	0,	1],
"EKKO":	[3,	1.5,	2,	2.5,	0,	3],
"ELISE":	[2.5,	2,	1.5,	2,	1,	7],
"EVELYNN":	[3,	1,	0,	2,	1,	3],
"EZREAL":	[2,	0,	0,	2,	0,	12],
"FIDDLESTICKS":	[1.5,	2,	3,	1,	1,	12],
"FIORA":	[3,	2,	1,	3,	1,	6],
"FIZZ":	[3,	1.5,	2,	3,	1,	3],
"GALIO":	[2.5,	2.5,	3,	1,	1,	10],
"GANKPLANK":	[3,	1.5,	1,	2.5,	1,	6],
"GAREN":	[2.5,	3,	1,	1.5,	0,	5],
"GNAR":	[2,	2,	1,	2.5,	1,	6],
"GRAGAS":	[3,	2,	2,	2,	1,	4],
"GRAVES":	[3,	2.5,	1,	2.5,	2,	1],
"GWEN":	[2.5,	2.5,	1,	3,	0,	6],
"HECARIM":	[3,	2.5,	2,	3,	1,	7],
"HEIMERDINGER":	[3,	0,	2,	0,	2,	2],
"HWEI":	[3,	0,	3,	0,	2,	8],
"LLAOI":	[3,	2.5,	2,	0,	1,	5],
"IRELIA":	[3,	1.5,	2,	3,	1,	7],
"IVERN":	[1,	0,	2,	1.5,	2.5,	11],
"JANNA":	[0,	1,	3,	1.5,	3,	9],
"JARVAN IV":	[1.5,	2.5,	1.5,	1.5,	1.5,	7],
"JAX":	[2.5,	1.5,	2,	2,	1,	6],
"JAYCE":	[3,	1,	1,	2,	1.5,	8],
"JHIN":	[3,	1.5,	2,	1.5,	1,	1],
"JINX":	[2.5,	0,	2,	2,	0,	1],
"K'SANTE":	[2.5,	3,	3,	2,	2,	6],
"KAI'SA":	[3,	1,	1,	3,	1,	1],
"KALISTA":	[2,	0,	1,	3,	2,	1],
"KARMA":	[3,	1.5,	2,	1.5,	2,	9],
"KARTHUS":	[2.5,	1,	2,	0,	1.5,	12],
"KASSADIN":	[3,	1.5,	1,	3,	1,	3],
"KATERINA":	[3,	0,	1,	3,	1,	3],
"KAYLE":	[2.5,	1,	1,	1,	1.5,	1],
"KAYN":	[3,	2.5,	1.5,	3,	0,	6],
"KENNEN":	[2,	1.5,	3,	1.5,	1,	12],
"KHA'ZIX":	[3,	1,	0,	1.5,	1,	3],
"KINDRED":	[3,	1,	2,	3,	2,	1],
"KLED & SKAARL":	[2,	2.5,	1,	3,	1,	6],
"KOG'MAW":	[2,	0,	0,	0,	0,	1],
"LEBLANC":	[3,	1,	2,	3,	1,	3],
"LEE SIN":	[3,	2.5,	2,	3,	1,	7],
"LEONA":	[2,	3,	3,	0,	2,	4],
"LILLIA":	[2.5,	2,	2,	2,	2,	6],
"LISSANDRA":	[2,	2,	3,	1.5,	1.5,	12],
"LUCIAN":	[3,	1,	1,	3,	1,	1],
"LULU":	[1.5,	1,	2,	0,	3,	9],
"LUX":	[2.5,	0,	2,	0,	1.5,	8],
"MALPHITE":	[2,	3,	3,	0,	0,	4],
"MALZAHAR":	[3,	1,	3,	1,	2,	12],
"MAOKAI":	[1.5,	3,	3,	1,	2,	4],
"MASTER YI":	[3,	2,	0,	1.5,	1,	6],
"MILIO":	[0,	0,	2,	3,	3,	9],
"MISS FORTUNE":	[3,	0,	0,	2,	1.5,	1],
"MORDEKAISER":	[3,	3,	2,	0,	2,	5],
"MORGANA":	[2.5,	1,	3,	1,	2,	11],
"NAAFIRI":	[3,	1,	1,	3,	1,	3],
"NAMI":	[1.5,	1,	3,	1,	2,	9],
"NASUS":	[3,	3,	2,	1,	1.5,	5],
"NAUTILUS":	[2,	3,	3,	0,	1.5,	4],
"NEEKO":	[3,	1.5,	3,	1,	1,	2],
"NIDALEE":	[3,	1,	0,	3,	2,	8],
"NILAH":	[2.5,	1.5,	0,	3,	1,	6],
"NOCTURNE":	[3,	2,	2,	2,	2,	3],
"NUNU &  WILLUMP":	[1.5,	3,	2,	2,	2,	4],
"OLAF":	[2.5,	2.5,	2,	2,	1,	7],
"ORIANNA":	[2.5,	1,	2.5,	0.5,	2,	2],
"ORNN":	[1,	3,	3,	0.5,	2,	4],
"PANTHEON":	[3,	2,	2,	2,	0,	7],
"POPPY":	[1.5,	3,	3,	2,	0.5,	10],
"PYKE":	[2,	1,	3,	3,	1,	3],
"QIYANA":	[2.5,	1,	2,	2,	1,	3],
"QUINN":	[2,	0,	2,	3,	0,	1],
"RAKAN":	[1,	2,	3,	3,	3,	11],
"RAMMUS":	[0,	3,	3,	2,	1,	4],
"REK'SAI":	[2,	2,	2,	2,	2,	7],
"RELL":	[0,	3,	3,	2,	2,	4],
"RENATA":	[2,	0,	3,	0,	2,	9],
"RENEKTON":	[2.5,	2.5,	2.5,	2,	0,	7],
"RENGAR":	[3,	1,	1.5,	2,	0,	3],
"RIVEN":	[3,	2,	2,	3,	0.5,	6],
"RUMBLE":	[3,	1.5,	2,	0.5,	0,	12],
"RYZE":	[2,	1.5,	2,	0,	1,	12],
"SAMIRA":	[3,	1.5,	1,	3,	0,	1],
"SEJUANI":	[1,	3,	3,	2,	1,	4],
"SENNA":	[2,	1,	2,	1,	3,	1],
"SERAPHINE":	[2.5,	0,	3,	1,	2,	9],
"SETT":	[2,	2.5,	2,	1.5,	0,	5],
"SHACO":	[2.5,	0,	2,	2,	2,	3],
"SHEN":	[1.5,	3,	2,	1.5,	3,	10],
"SHYVANA":	[3,	2,	1,	2,	1,	5],
"SINGED":	[1,	2.5,	2,	2,	1,	11],
"SION":	[2,	3,	3,	1,	1,	4],
"SIVIR":	[3,	1,	0,	1.5,	2,	1],
"SKARNER":	[2,	3,	3,	2,	0,	4],
"SMOLDER":	[3,	0,	0,	0,	0,	1],
"SONA":	[1.5,	0,	2,	1.5,	2,	9],
"SORAKA":	[1,	0,	2,	1,	3,	9],
"SWAIN":	[2,	2.5,	1,	0,	0,	12],
"SYLAS":	[2.5,	2,	1,	1.5,	0,	6],
"SYNDRA":	[3,	2.5,	2,	0,	0.5,	2],
"TAHM KENCH":	[2.5,	3,	2,	1.5,	3,	10],
"TALIYAH":	[3,	1,	2,	1.5,	3,	12],
"TALON":	[3,	1.5,	0,	1.5,	0,	3],
"TARIC":	[0,	2.5,	2,	0.5,	3,	10],
"TEEMO":	[2,	0.5,	2,	0.5,	2,	1],
"THRESH":	[1,	2,	3,	1,	3,	11],
"TRISTANA":	[3,	1,	2, 	1.5,	1,	1],
"TRUNDLE":	[2,	3,	0,	0,	2,	5],
"TRYNDAMERE":	[3,	2,	0,	2,	0,	6],
"TWISTED FATE":	[2,	0,	1.5,	1.5,	2,	2],
"TWITCH":	[3,	1,	0,	2,	0,	1],
"UDYR":	[2.5,	3,	2,	2,	1.5,	5],
"URGOT":	[2.5,	2,	2,	1,	0,	5],
"VARUS":	[3,	1,	2,	0,	0,	1],
"VAYNE":	[3,	0.5,	2,	2,	0,	1],
"VEIGAR":	[3,	1,	3,	0,	0,	2],
"VEL'KOZ":	[3,	0,	2,	0,	0.5,	8],
"VEX":	[3,	2,	2,	2,	0,	2],
"VI":	[2,	2.5,	3,	2,	0,	7],
"VIEGO":	[3,	2,	2,	2,	0,	6],
"VIKTOR":	[3,	0.5,	2,	0.5,	0,	12],
"VLADIMIR":	[3,	2,	1.5,	1,	0,	12],
"VOLIBEAR":	[2,	3,	2,	2,	1,	5],
"WARWICK":	[2.5,	2,	2,	1,	1,	7],
"WUKONG":	[2.5,	2,	2,	2,	0,	7],
"XAYAH":	[3,	2,	3,	0.5,	0,	1],
"XERATH":	[3,	0,	2,	0,	1,	8],
"XIN ZHAO":	[2.5,	2,	2,	2,	0,	7],
"YASUO":	[3,	0,	2,	3,	1,	6],
"YONE":	[3,	2,	2,	3,	0.5,	6],
"YORICK":	[2,	2,	2,	2,	0.5,	5],
"YUUMI":	[0,	0,	0,	0,	3,	9],
"ZAC":	[2,	3,	3,	2,	1,	4],
"ZED":	[3,	1.5,	0,	3,	0,	3],
"ZERI":	[3,	1,	2,	3,	0,	1],
"ZIGGS":	[3,	0,	2,	2,	1,	8],
"ZILEAN":	[2.5,	0,	2,	2,	3,	12],
"ZOE":	[3,	0,	1.5,	1.5,	0,	2],
"ZYRA":	[3,	0,	3,	0,	0,	2]
}

# def dominates(character1, character2, weights):
#     weighted_char1 = [x * w for x, w in zip(character1, weights)]
#     weighted_char2 = [x * w for x, w in zip(character2, weights)]
#     return all(x >= y for x, y in zip(weighted_char1, weighted_char2)) and any(x > y for x, y in zip(weighted_char1, weighted_char2))

# def pareto_frontier(characters, attributes_indices, weights):
#     pareto_front = []
#     for character1, attributes1 in characters.items():
#         attributes1 = [attributes1[i] for i in attributes_indices]
#         is_dominated = False
#         for character2, attributes2 in characters.items():
#             attributes2 = [attributes2[i] for i in attributes_indices]
#             if character1 != character2 and dominates(attributes2, attributes1, weights):
#                 is_dominated = True
#                 break
#         if not is_dominated:
#             pareto_front.append((character1, attributes1))
#     return pareto_front

def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def dominates(character1, character2, weights):
    score1 = dot_product(character1, weights)
    score2 = dot_product(character2, weights)
    return score1 > score2

def pareto_frontier(characters, attributes_indices, weights):
    pareto_front = []
    for character1, attributes1 in characters.items():
        attributes1 = [attributes1[i] for i in attributes_indices]
        is_dominated = False
        for character2, attributes2 in characters.items():
            attributes2 = [attributes2[i] for i in attributes_indices]
            if character1 != character2 and dominates(attributes2, attributes1, weights):
                is_dominated = True
                break
        if not is_dominated:
            pareto_front.append((character1, attributes1))
    return pareto_front

def compare_pareto_frontiers(pareto1, pareto2, p3, p4, p5):
    pareto1_names = set(name for name, _ in pareto1)
    pareto2_names = set(name for name, _ in pareto2)
    p3_names = set(name for name, _ in p3)
    p4_names= set(name for name, _ in p4)
    p5_names= set(name for name, _ in p5)
    
    common_characters = pareto1_names.intersection(pareto2_names).intersection(p3_names).intersection(p4_names).intersection(p5_names)
    unique_to_pareto1 = pareto1_names - common_characters
    unique_to_pareto2 = pareto2_names - common_characters
    uniquetop3 = p3_names- common_characters
    uniquetop4 = p4_names- common_characters
    uniquetop5 = p5_names- common_characters
    
    return common_characters, unique_to_pareto1, unique_to_pareto2, uniquetop3, uniquetop4, uniquetop5

def plot_pareto_frontiers(characters, pareto_fronts, attributes_indices_list, titles):
    fig = plt.figure(figsize=(18, 8))
    
    num_plots = len(pareto_fronts)
    for idx in range(num_plots):
        attributes_indices = attributes_indices_list[idx]
        pareto_front = pareto_fronts[idx]
        title = titles[idx]
        
        ax = fig.add_subplot(1, num_plots, idx + 1, projection='3d')
        
        all_attributes = np.array([[attributes[i] for i in attributes_indices] for attributes in characters.values()])
        
        pareto_attributes = np.array([attributes for _, attributes in pareto_front])
        # all characters
        ax.scatter(all_attributes[:, 0], all_attributes[:, 1], all_attributes[:, 2], c='blue', label='Characters', alpha=0.3)
        # pareto characters but with higher opactity to cover the blue of the previous line
        ax.scatter(pareto_attributes[:, 0], pareto_attributes[:, 1], pareto_attributes[:, 2], c='red', label='Pareto Frontier')
        
        pareto_sorted = sorted(pareto_front, key=lambda x: (x[1][0], x[1][1], x[1][2]))
        pareto_sorted_attributes = np.array([attributes for _, attributes in pareto_sorted])
        ax.plot(pareto_sorted_attributes[:, 0], pareto_sorted_attributes[:, 1], pareto_sorted_attributes[:, 2], 'r--')
        
        for name, attr in pareto_front:
            ax.text(attr[0], attr[1], attr[2], name)
        
        for i, name in enumerate(characters.keys()):
            if name not in [name for name, _ in pareto_front]:
                ax.text(all_attributes[i, 0], all_attributes[i, 1], all_attributes[i, 2], name, color='blue')
        
        ax.set_xlabel(f'Attribute {attributes_indices[0] + 1}')
        ax.set_ylabel(f'Attribute {attributes_indices[1] + 1}')
        ax.set_zlabel(f'Attribute {attributes_indices[2] + 1}')
        ax.set_title(title)
        ax.legend()

    plt.tight_layout()
    plt.show()


top = [0, 1, 2]
top_weights = [2.5, 5, 1]
middle = [0,2, 3]
middle_weights = [7,1,-1]
junggler = [0,1,2,3]
junggler_weights = [1,1,1,1]
bottom = [0,1,3,4]
bottom_weights = [6, -2, 3,-3 ]
support = [0,1,2,4]
support_weights = [-.5,4,3, 2]

pareto_top = pareto_frontier(characters, top, top_weights)
pareto_middle = pareto_frontier(characters, middle, middle_weights)
pareto_junggler = pareto_frontier(characters, junggler, junggler_weights)
pareto_bottom = pareto_frontier(characters, bottom, bottom_weights)
pareto_support = pareto_frontier(characters, support, support_weights)

common_characters, u_to_top, u_to_mid, u_to_jg, u_to_bot, u_to_sup = compare_pareto_frontiers(pareto_top, pareto_middle,pareto_junggler,pareto_bottom, pareto_support)

print("Common characters in both lanes' Pareto frontiers:", common_characters)
print("Unique to TOP'S Pareto frontier:", u_to_top)
print("Unique to MID'S Pareto frontier:", u_to_mid)
print("Unique to JUNG'S Pareto frontier:", u_to_jg)
print("Unique to BOT'S Pareto frontier:", u_to_bot)
print("Unique to SUP'S Pareto frontier:", u_to_sup)

# print("Pareto characters for TOP:", [name for name, _ in pareto_top])
# print("Pareto characters for MID:", [name for name, _ in pareto_middle])

# Plotting the Pareto frontiers for both lanes
plot_pareto_frontiers(characters, [pareto_top, pareto_middle, pareto_junggler,pareto_bottom, pareto_support], [top, middle, junggler, bottom, support], [' Top', 'Mid', " Jungle",'Bot','Sup'])

# attributes_indices_lane1 = [1, 5, 2]  # Example: optimize for damage (index 1), tankiness (index 5), and third attribute (index 2)
# attributes_indices_lane2 = [3, 4, 2]  # Different example attributes for another lane

# weights_lane1 = [0.5, 1.5, 1.0]  # Weights for lane 1 attributes
# weights_lane2 = [1.0, 1.0, 2.0]  # Weights for lane 2 attributes

# pareto_front_lane1 = pareto_frontier(characters, attributes_indices_lane1, weights_lane1)
# pareto_front_lane2 = pareto_frontier(characters, attributes_indices_lane2, weights_lane2)



