
import sys

# A fun multiple-choice story-line game.

print('''
    *                             |>>>                    +
+          *                      |                   *       +
                    |>>>      _  _|_  _   *     |>>>
           *        |        |;| |;| |;|        |                 *
     +          _  _|_  _    \\.    .  /    _  _|_  _       +
 *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|
               \\..      /    ||:+++. |    \\.    .  /           *
      +         \\.  ,  /     ||:+++  |     \\:  .  /
                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *
          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +
                 ||+++ ||.    .     .      . ||+++.|   *
+   *            ||: . ||:.     . .   .  ,   ||:   |               *
         *       ||:   ||:  ,     +       .  ||: , |      +
  *              ||:   ||:.     +++++      . ||:   |         *
     +           ||:   ||.     +++++++  .    ||: . |    +
           +     ||: . ||: ,   +++++++ .  .  ||:   |             +
                 ||: . ||: ,   +++++++ .  .  ||:   |        *
                 ||: . ||: ,   +++++++ .  .  ||:   |

''')

print('''
+ 
 * You are a knight sent out to rescue the princess. 
   She's stuck in a high castle guarded by an ancient dragon.
   Be wary of the dangers you may face on your journey! 
                                                      *
                                                      +
''')

character_name = input("What is your name? ")
divergence_in_the_road = input('''
You set out on your journey to rescue the princess. Two days into your travels, you come across a divergence in the road.
The path splits into two; one way going through the forest, the other going by sea. Which path do you take? 
''')

if divergence_in_the_road.lower() == "sea":
    input("You make it to the shoreline of the ocean. There is an old boat left behind by a fisherman. You board it and begin to set sail.")
elif divergence_in_the_road.lower() == "forest":
    quicksand_choice = input('''
You enter the forest. The underbrush is thick with twisting vines, shrubs, and reptiles. 
The canopy does not allow much sunlight in. While walking, your foot gets caught in a pool of quicksand. How do you proceed?
Type "S" if you wish to try and swim your way out. Type "V" if you latch onto a thin vine: ''')
    if quicksand_choice.upper() == "S":
        print("Excessive movement in quicksand accelerates how fast you sink. Wet sand fills your lungs. You die a slow and brutal death.")
        sys.exit()
    elif quicksand_choice.upper() == "V":
        print('''
You latch onto a vine. Your palms ache from how tightly you wrapped the vine around your hands.
Thankfully, you manage to pull yourself out from an unfortunate death. 
You trek through the remaining forest and find yourself at the shoreline of the sea. You find a small boat left behind by a fisherman.
You board it and set sail.''')
    else:
        print("That's not an option.")
        sys.exit()
else:
    print("That's not an option.")
    sys.exit()

cave_or_vent = input('''
After 3 days at sea, your provisions begin to dwindle. All you have left is a single bottle of fresh water.
However, you begin to see land, and in the far distance, you also see the white flag atop the castle where the princess resides.
Your morale boosts, and you feel a new sense of determination. However, your journey is far from over. 
You disembark from the boat and begin walking. After a few hours, you come across a ravine that you have no choice but to descend.

You steadily climb your way down, careful not to move any loose rocks in fear of them tumbling down on top of you.
At the bottom, you find a massive cave entrance. Upon inspection, you notice the footprints of a Charatex, a massive creature with the body of a lion and the head of a serpent.
Wary, you look for an alternative and see a long, winding dirt path that leads to the exit of the ravine. However, the path is riddled with earth vents that appear to be inactive.
How do you proceed? Type "C" to enter the cave and take your chances with the Charatex or "V" to take the path riddled with the vents.
''')

if cave_or_vent.upper() == "V":
    print('''
You make your choice and begin walking the path. Surprisingly, the earth vents were not inactive.
In fact, they release copious carbon monoxide; an odorless gas. 
However, you would never know this, as you die by asphyxiation before reaching the end of the path.''')
    sys.exit()
elif cave_or_vent.upper() == "C":
    print('''
You make your choice and enter the cave. The cave is eerily quiet and damp, with water droplets from the ceiling hitting the ground.
The ground is marred by the remains of other warriors who dared to challenge the Charatex. You make your way to the center and find the creature resting peacefully.
The creature is massive, far larger than you had imagined. It appears to have just finished a meal, as several bones litter the surrounding area.
You try to avoid any confrontation by inching your way around the animal as quietly as possible. Sweat beads down your face from fear and anxiety.
The cave exit is just up ahead, so you begin to run. This was a terrible mistake, as your foot kicks a bone, making a loud rattling sound that echoes through the cave.
The Charatex wakes up with deadly intent and begins chasing you at full speed. You run and keep running. Thankfully, you make it out of the cave in one piece with the Charatex far behind you.
''')
else:
    print("That's not an option.")
    sys.exit()

to_eat_or_not_to_eat = input('''
You are now only a few hours away from the castle. After barely surviving the Charatex, you sit and look for a place to rest.
You find an old tree with large leaves that give you some relief from the baking sun. As your adrenaline begins to calm, you realize your dire hunger.
You tiredly move your eyes back and forth, looking for something to eat. The tree you rest under bears fruit, ones you have never seen.
You are unsure if they are edible, but the forsaken plain you are currently in provides no other options. How do you proceed? Type "E" to eat the unknown fruit or "H" to continue your journey hungry. 
''')

if to_eat_or_not_to_eat.upper() == "H":
    print('''
You make your choice. After resting under the tree, you rise and continue trekking toward the castle. With the sun high at its meridian and your lack of food and water, you begin to tire quickly.
This will be the last choice you make. You fall to the ground and roll onto your back. With the sun beating down on your face and your body crying for nourishment, you die of starvation and dehydration.
Your body is left to the vultures; providing them with sustenance to survive.
''')
    sys.exit()
elif to_eat_or_not_to_eat.upper() == "E":
    print('''
You make your choice. You pick a single fruit and nibble on it. The flavor bursts in your mouth. 
You wait a few minutes to see if any adverse effects occur. They don't. You begin to pick the fruits from the tree with vigor and eat until you're full.
Now with a full stomach and plenty of rest, you continue your journey onward.
''')
else:
    print("That's not an option.")
    sys.exit()

print('''
After days of traveling, you finally reach the castle. Claw marks and blackened stone from fire riddle the castle walls. You take cautious steps forward. 
The entrance is blocked by an aged and heavy wooden door. You push the door open with all your might, causing a loud creak. 
Behind the door is nothing but a long, dark hallway and wax candles held up by wall sconces, dimly lit by weak flames. You enter, and the door closes with a loud thud.

At the end of the hall is another large door. You reach the door and slowly open it. You enter and find the princess locked inside a golden cage. 
She lifts her head and gazes upon you with somber eyes. You quickly make your way toward her. You notice a long metal chain attached to the top of the cage connected to a lever on the ground.
As you are about to introduce yourself and turn the lever, the princess viciously shakes her head and points to her ear. You realize she wishes you to stay silent and listen.
As you do, you hear heavy footsteps coming from the hallway you just exited. As they near, the ground begins to shake, and the princess begins to shed tears.
Quickly, you look for a place to hide and see steps that lead to a balcony. You run up the steps and hide. Just as your head begins to lower, the heavy door slams open, and the dragon enters with fury.

It circles the princess, flicking its tongue to taste the air. Its long tail begins to sway violently, indicating agitation. Its head turns to the princess, back facing toward you, and lets out a vicious roar that rattles the princess's cage.
Realizing this is your only chance, you jump from the balcony and land on the dragon's neck.

After a few minutes of struggle, you manage to defeat the dragon and rescue the princess from her prison.
''')

print(f"Congratulations, {character_name}. You've completed your quest.")



