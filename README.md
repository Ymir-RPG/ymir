[![Build Status](https://travis-ci.org/skylerberg/ymir.svg?branch=master)](https://travis-ci.org/Ymir-RPG/ymir)

## YMIR: Tabletop RPG Campaign Management Ecosystem
### What is Ymir?
Ymir is the driver for the Ymir-RPG application ecosystem. All sub-applications/microservices in the ecosystem are modules that hook in to this driver to function. Ymir is designed to provide value to players of any table-top RPG, from Dungeons and Dragons to your own homebrew system. Microservices can be made to serve any specific tabletop universe, or made to the same generic specifications as the driver.

### The Universal Laws of Tabletop Games
Although these really aren't universal laws, these are characteristics that show up in nearly every tabletop RPG, and thus need to have core support in Ymir.

##### Campaigns
* Campaigns have a single dungeon master at one time.
  * Dungeon master can give away their role to another user involved in the campaign, but relinquishes their omniscience.
* A single user can be involved in multiple campaigns
* A single user can have multiple characters in a single campaign
* Question: can a single user have the same character across multiple campaigns?
  * Answer A: Clone the character. Should be easy to do, clear use case for that.
  * Answer B: Persistent, updating character involved in two campaigns. Harder to implement, not sure of use case.


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
  
