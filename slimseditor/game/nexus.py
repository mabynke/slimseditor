from reloadr import autoreload

from slimseditor.saveentry import RangedShort, Boolean, Integer


@autoreload
def get_nexus_items():
    return {
        "Bolt counts": [
            Integer("Number of Bolts", 0x105c),
            Integer("Number of Raritanium", 0x1060),
        ],
    }
