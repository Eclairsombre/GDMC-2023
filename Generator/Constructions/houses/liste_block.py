from gdpc import Editor, Block, geometry


air = Block('air')

stairs_devant = Block("oak_stairs", {"facing": "east"})
stairs_derriere = Block("oak_stairs", {"facing": "west"})
stairs_droite = Block("oak_stairs", {"facing": "north"})
stairs_gauche = Block("oak_stairs", {"facing": "south"})



stairs_quartz_devant = Block("quartz_stairs", {"facing": "east"})
stairs_quartz_derriere = Block("quartz_stairs", {"facing": "west"})
stairs_quartz_droite = Block("quartz_stairs", {"facing": "north"})
stairs_quartz_gauche = Block("quartz_stairs", {"facing": "south"})



door_east = Block("oak_door", {"facing": "east"})




oak_planks = Block("oak_planks")
oak_log = Block("oak_log")
spruce_wood= Block("spruce_wood")


glass = Block("glass")
black_stained_glass = Block("black_stained_glass")



white_concrete_powder = Block("white_concrete_powder")
white_concrete = Block("white_concrete")


