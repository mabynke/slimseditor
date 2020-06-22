Slim's Editor
=============

A savegame editor for the Ratchet and Clank games, written in Python.

Currently under heavy development, **backup** your savegames before loading them into Slim's Editor.


About
-----

A more extended written description will be put here soon (tm).

For unsupported games/formats, please refer to https://github.com/maikelwever/rac-savegame-editor.


Supported file formats
----------------------

Currently supported:

 - Raw PS2 save data (.bin), can be extracted with MyMC+ or uLaunchELF.
 - PCSX2 Memory Cards (.ps2)
 - Decrypted PS3 savegame data (RPCS3 or decrypted with BruteForce)
 
 
Supported games
---------------

Currently supported:

 - PS2 and PS3
   - Ratchet and Clank
   - Ratchet and Clank 2 : Going Commando
   - Ratchet and Clank 3 : Up Your Arsenal
   - Ratchet: Deadlocked / Gladiator
 - PS3
   - Ratchet and Clank : Tools of Destruction
   - Ratchet and Clank : Quest for Booty
   - Ratchet and Clank : A Crack in Time
   - Ratchet and Clank : (Into the) Nexus
   
   
Roadmap
-------

Wishlist of features to port from the previous editor or add new:

 - PS Vita trilogy support
 - PS3 savegame decryption and proper re-encryption.


Installation
------------

For Windows, get the prebuilt versions from the Releases tab on GitHub.
Simply unzip the release, and run `slimseditor.exe`.

For Linux (package names are for Debian/Ubuntu):

Install `python3 python3-dev python3-venv build-essential`. 
Install `zenity` (or `kdialog` if you are on KDE).

```bash
git clone https://github.com/maikelwever/slimseditor
cd slimseditor
python -m venv env
env/bin/pip install -r requirements.txt
env/bin/python setup.py develop
env/bin/python -m slimseditor
```
