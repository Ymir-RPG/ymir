## YMIR - Tabletop RPG World Builder and Campaign Manager
<hr>
### What is Ymir?
Ymir is the driver for the Ymir-RPG application ecosystem. All sub-applications/microservices in the ecosystem are modules that hook in to this driver to function. Ymir is designed to provide value to players of any table-top RPG, from Dungeons and Dragons to your own homebrew system. Microservices can be made to serve any specific tabletop universe, or made to the same generic specifications as the driver.

### The Universal Laws of Tabletop Games
Although these really aren't universal laws, these are characteristics that show up in nearly every tabletop RPG, and thus need to have core support in Ymir.

##### Characters
* Personal story and background
* Various statistics
  * Core statistics (Constitution, Dexterity, Strength, etc.)
  * Multi-dependence statistics (Armor Class, Perception, HP, etc.)
  * Trained skills (Athletics, Intimidation, etc.)
  * Temporary statistic deficiencies (Loss of HP, drunkenness, broken armor, etc.)
* Property
  * Equipped Armor and Weapons
  * Other possessions (Unequipped armor, food, rope, etc.)
  * Currency
* Actions (TODO: subcategories need better definition)
  * Attacks
  * Utility actions
  * Persistent spells
  * Tricks...?
##### The World
* Locations
* Maps
  * World map
  * Continent maps
  * Country/Kingdom maps
  * City maps... etc.
* Non-player Characters
  * Where did we meet these NPCs?
  * Other necessary info from Characters subsection
* Creature Encounters
  * Experience gain for killing certain creatures
  * HP tracking w/ varying granularity (i.e. numbers for DM, "bloodied" for players)
  * Hidden/exposed creatures

I'm quite sure there's more, but that's all I can think of for now. We'll be able to come back and add to the core API once this featureset is complete.
  
