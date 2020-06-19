from reloadr import autoreload

from slimseditor.saveentry import RangedShort, Boolean, Integer


@autoreload
def get_gc_items():
    return {
        "Bolt counts": [
            Integer("Number of Bolts", 0x24),
            Integer("Number of Raritanium", 0x28),
            Integer("Total Bolts Collected", 0x48),
        ],
        "Item Unlocks": [
            Boolean("Heli-Pack", 0x292),
            Boolean("Thruster-Pack", 0x293),
            Boolean("Hydro-Pack", 0x294),
            Boolean("Mapper", 0x295),
            Boolean("Levitator", 0x298),
            Boolean("Swingshot", 0x29d),
            Boolean("Gravity Boots", 0x2a3),
            Boolean("Grindboots", 0x2a4),
            Boolean("Glider", 0x2a5),
            Boolean("Dynamo", 0x2b4),
            Boolean("Electrolyzer", 0x2b6),
            Boolean("Thermanator", 0x2b7),
            Boolean("Tractor Beam", 0x2be),
            Boolean("Biker Helmet", 0x2c0),
            Boolean("Quark Statuette", 0x2c1),
            Boolean("Box Breaker", 0x2c2),
            Boolean("Infiltrator", 0x2c4),
            Boolean("Charge Boots", 0x2c6),
            Boolean("Hypnomatic", 0x2c7),
        ],
        "Weapon Ammo": [
            RangedShort("Clank Zapper", 0x1c8, 30),
            RangedShort("Bomb Glove", 0x1c8, 40),
            RangedShort("Visibomb Gun", 0x1d8, 20),
            RangedShort("Decoy Glove", 0x1e8, 20),
            RangedShort("Tesla Claw", 0x1f0, 300),
            RangedShort("Chopper", 0x200, 35),
            RangedShort("Pulse Rifle", 0x204, 8),
            RangedShort("Seeker Gun", 0x208, 25),
            RangedShort("Hoverbomb Gun", 0x20c, 10),
            RangedShort("Blitz Gun", 0x210, 40),
            RangedShort("Minirocket Tube", 0x214, 25),
            RangedShort("Plasma Coil", 0x218, 15),
            RangedShort("Lava Gun", 0x21c, 200),
            RangedShort("Lancer", 0x220, 200),
            RangedShort("Synthenoid", 0x224, 12),
            RangedShort("Spiderbot Glove", 0x228, 8),
            RangedShort("Bouncer", 0x23c, 25),
            RangedShort("Miniturret Glove", 0x24c, 20),
            RangedShort("Zodiac", 0x254, 4),
            RangedShort("RYNO II", 0x258, 100),
            RangedShort("Shield Charger", 0x25c, 5),
        ],
        "Weapon Unlocks": [
            Boolean("Clank Zapper", 0x299),
            Boolean("Bomb Glove", 0x29c),
            Boolean("Visibomb Gun", 0x29e),
            Boolean("Sheepinator", 0x2a0),
            Boolean("Decoy Glove", 0x2a1),
            Boolean("Tesla Claw", 0x2a2),
            Boolean("Chopper", 0x2a5),
            Boolean("Pulse Rifle", 0x2a7),
            Boolean("Seeker Gun", 0x2a8),
            Boolean("Hoverbomb Gun", 0x2a9),
            Boolean("Blitz Gun", 0x2aa),
            Boolean("Minirocket Tube", 0x2ab),
            Boolean("Plasma Coil", 0x2ac),
            Boolean("Lava Gun", 0x2ad),
            Boolean("Lancer", 0x2ae),
            Boolean("Synthenoid", 0x2af),
            Boolean("Spiderbot Glove", 0x2b0),
            Boolean("Bouncer", 0x2b5),
            Boolean("Miniturret Glove", 0x2b9),
            Boolean("Zodiac", 0x2bb),
            Boolean("RYNO II", 0x2bc),
            Boolean("Shield Charger", 0x2bd),
            Boolean("Walloper", 0x2c5),
        ],
    }

