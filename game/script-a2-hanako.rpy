label en_H2:
    
    scene bg school_miyagi 
    show hanako emb_downsmile_close 
    with dissolve#None

    play sound sfx_doorknock2

    show hanako emb_timid_close 
    with charachange
    
    "As we are setting up the pieces, there is a noise at the door."
    
    play sound sfx_dooropen

    show bg school_miyagi at bgright 
    show hanako emb_timid_close at tworight 
    with charamove

    show lilly basic_smileclosed at twoleft 
    with charaenter

    li "Ah, you're both here, as I expected." #says the blind girl

    play music music_lilly fadein 4.0

    show hanako emb_emb_close at tworight 
    with charachange

    ha "Lilly…"

    hi "Oh, hey there Lilly. Are you finished?"
    
    show lilly basic_smile at twoleft 
    with charachange

    li "Yes. Our teacher managed to round up some extra help, so I was able to leave. Have you been here since you left?"

    hi "Pretty much, we've just been playing a bit of chess."
    
    show hanako emb_smile_close at tworight
    with charachange

    ha "W-would you like a cup of tea?"
    
    show lilly basic_weaksmile at twoleft 
    with charachange
    
    li "Actually, I think it may be a good idea to go outside for a little while…"

    show hanako def_worry_close at tworight
    with charachange

    "The instant drop in Hanako's face shows her objection to this plan, yet she says nothing."

    "I feel strangely compelled to speak for her."

    hi "I… I kinda think that we should just stay here…"
    
    show lilly basic_surprised at twoleft 
    with charachange

    li "Really? It's so crowded here that I was thinking we should leave the school and head for the local teahouse."
    
    show hanako emb_blushtimid_close at tworight
    with charachange

    ha "You mean the S-Shanghai?"

    show lilly basic_smileclosed at twoleft
    with charachange

    li "Of course; with everyone at the festival it should be practically empty."

    hi "Tea house?"
    
    show lilly basic_weaksmile at twoleft
    with charachange
    
    li "Oh, that's right, you probably don't know of it."
    #Odds are fairly good he does instead; damn Shangai Amnesia will be a fucking headache to check for in final release. Note to self: check. -SC
    
    show lilly basic_smile at twoleft
    with charachange

    li "There is a tea house not far from here, we go there quite often."

    li "Well, perhaps \"tea house\" isn't the correct word, but that is what the place calls itself."

    li "\"Café\" would be more appropriate, I believe."
    
    "Lilly's attempt at an explanation is leaving me a little befuddled. A café that calls itself a teahouse..."
    
    "Aren't they the same thing?"

    hi "I… don't quite follow you, to be honest, but I'm game, I suppose."

    hi "Hanako, what do you think?"
    
    show hanako defarms_shock_close at tworight
    with Dissolve(0.2)

    show hanako def_worry_close at tworight
    with charachange

    "Hanako jumps a little at being forced into the conversation, but at least she seems less distraught than before."
    
    show hanako cover_bashful_close at tworight
    with charachange

    ha "If… if it's the Shanghai, I think it'll be nice."
    
    show lilly basic_planned at twoleft
    with charachange

    li "Well then, it's settled. Let's be on our way."
    
    show hanako basic_bashful at tworight
    with charadistant

    "Hanako and I rise from the table and our preempted chess game."

    "Before I can do anything, Hanako has poured the pieces into the small container and put the board away."

    hi "Looks like we're ready now. Please, lead on."
    
    stop music fadeout 8.0

    scene bg school_hallway3 
    with locationchange

    show hanako emb_smile at Position(xanchor=0.5, xpos=0.58) 
    show lilly basic_smileclosed at Position(xanchor=0.5, xpos=0.42) 
    with charaenter

    "Hanako moves to Lilly's side and we venture onto the school's corridors."
    
    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')

    play ambient sfx_crowd_outdoors fadein 1.0

    scene bg school_gate_ss 
    with locationskip

    "The pair leads me through a series of unfamiliar doors, and we emerge on the side of the building opposite to the festival grounds."

    "Insulated by the heavy stone of the building, the noise from the crowd has faded to a murmur."

    #"Even around the gate there is only a limited amount of human traffic heading into the grounds."
    #I don't think that would be in sight from this angle. Need2check comparative geography. -SC

    hi "Strange; I thought by now that most people would be beginning to leave…"
    
    show hanako emb_downtimid_ss at Position(xanchor=0.5, xpos=0.58) 
    show lilly basic_smile_ss at Position(xanchor=0.5, xpos=0.42) 
    with charaenter

    li "They're probably here to view the fireworks."

    hi "Fireworks?"
    
    show lilly basic_weaksmile_ss at Position(xanchor=0.5, xpos=0.42)
    with charachange

    li "Yes, apparently the school puts on quite a show."

    li "A lot of people come from town just to watch it."

    "Lilly's decision to leave the school grounds seems to make sense now. Hanako would probably have a hard time with the whole town descending onto the school."

    "I wonder if they do this every year to avoid the inevitable crowd?"

    stop ambient fadeout 7.0
    play music music_tranquil fadein 3.0

    scene bg school_road_ss 
    with locationchange
    
    "For the second time since arriving at Yamaku I find myself walking down this road with Lilly."
    #Again need2check flow, but this seems likely to be true. -SC
    
    "Only now that I can't hear the incessant noise of the festival do I realize how loud it was. In the still evening air I can hear my ears ringing slightly as they recover from the day's assault on them."

    show hanako emb_emb_ss at Position(xanchor=0.5, xpos=0.58) 
    show lilly basic_smileclosed_ss at Position(xanchor=0.5, xpos=0.42) 
    with charaenter

    "Hanako clings to Lilly, but still manages to guide her along the road. That, and avoiding the occasional gaze from curious pedestrians, appears to totally sap her constitution."
    
    "She rarely raises her focus from the ground in front of her, nor does she utter a word."

    "Lilly seems to be a little less comfortable here than in the school, as well. Her cane waves in an arc to her front faster here than it does in the school."
    
    "Once you leave our insulated world it's impossible to change." 

    "Inside, everyone is \"special\", which negates the \"special-ness\" of it."

    "But once we venture outside the school gates, we are returned to the status of \"outsider\" and generic labels."

    "Especially when we are still in school uniform. It's like hanging a sign around your neck challenging people to figure out what is wrong with you."

    "I'm surprised that so many of the students keep it on. Then again, with canes and wheelchairs common amongst the students, I guess it's not really that much of a giveaway."
    
    "Or maybe I'm the only one that sees this as a stigma? Maybe you get used to it after a time, like any other school uniform."

    scene bg suburb_shanghaiext_ss
    with locationskip
    
    "The tea house seems fairly standard from the outside; just an ordinary building with typical signs decorating the entrance."
    #Writing from here on might need major refurbishing, as above. -SC

    "It looks like the type of place you'd walk by without a thought, just another generic café in a sea of thousands."
    
    "If Hanako hadn't steered Lilly into the entrance I would have continued on down the road without ever knowing that it existed."
    
    play sound sfx_storebell

    scene bg suburb_shanghaiint at Fullpan(5.0, dir="right") 
    with locationchange

    stop music fadeout 6.0
    
    "Inside the tea house it takes on a more traditional feel. Everything seems to have been made from the same lump of timber, from the counter and benches to the high-backed booths around the walls." 
    
    "But the most striking feature of the room is the lack of life. I think I can faintly hear something bubbling away in the background, but otherwise the room is silent."

    "Without any direction, we simply wait near the entrance, politely obeying the \"Please wait to be seated\" sign."

    hi "Er, is this place closed or something?"
    
    stop music
    play sound sfx_impact2

    show yuukoshang panic_up at Transform(xalign=0.5, yanchor=1.0, ypos=1.5, alpha=0.0)
    with None
    
    show yuukoshang panic_up at Transform(xalign=0.5, yanchor=1.0, ypos=1.0, alpha=1.0)
    show bg suburb_shanghaiint at right 
    with Dissolvemove(0.3)

    with vpunch

    "The sound of a chair falling over echoes through the empty room, and a head shoots up from inside a booth."

    play music music_comedy fadein 0.5

    show yuukoshang neurotic_up
    with charachange

    yu "I wasn't asleep and welcome to the Shanghai!"

    "Yuuko, dressed in a pastel apron and clutching a menu, rushes to greet us. Her misaligned glasses and ruffled hair cast suspicion on her previous statement."

    "But whether she was asleep or not isn't the first question that leaps to my mind."
    
    hi "You work here now? What happened to the library?"
    
    show yuukoshang smile_down 
    with charachange

    yu "What? Lilly? Hisao?"
    
    show yuukoshang neurotic_up 
    with charachange

    yu "Welcome to the Shanghai!"
    
    show yuukoshang noglasses_up at Position(ypos=1.25) 
    with Dissolvemove(0.2)

    play sound sfx_dropglasses

    with Pause(0.3)

    show yuukoshang noglasses_up at center 
    with charamove
    
    "Yuuko, still waking up, jerks into a violent bow, dislodging her glasses in the process."

    yu "Uweh!? My glasses…"

    "As I pick up her spectacles off the floor, Lilly offers an explanation."
    
    show yuukoshang noglasses_up at tworight 
    show bg suburb_shanghaiint at center 
    with charamove

    show lilly basic_weaksmile at twoleft 
    with charaenter

    li "Yuuko works here part-time when she's not at the library. It's one of the reasons we like to come here."
    
    show yuukoshang neurotic_up at tworight
    with charachange
    
    "Yuuko takes her glasses from my hands, shakily putting them back on."

    yu "Yes… that's right… thanks…"
    
    show yuukoshang neutral_down at tworight
    with charachange

    yu "Shall I show you to your table?"
    
    show yuukoshang worried_up at tworight
    with charachange

    yu "There's no-one else here so you can sit wherever you like and order whatever you like, but there may be a delay as I will have to make it myself…"

    show lilly basic_smile at twoleft 
    with charaenter

    li "It's alright Yuuko, you can calm down. Just a pot of black tea and a plate of sandwiches will be fine."
    
    show yuukoshang happy_down at tworight
    with charachange

    yu "Right! I'll get right onto that!"
    
    hide yuukoshang 
    with charaexit

    show lilly basic_smile at center 
    show bg suburb_shanghaiint at bgright 
    with charamove

    "Yuuko hurries off to the back of the café, leaving us still standing at the entrance."

    "She pushes the swinging half-doors open before realizing that she hasn't seated us."

    yu "I'm sorry! I'm sorry! Please, sit where you'd like! I'll be right back!"
    
    stop music fadeout 3.0

    hide lilly 
    with charaexit

    show bg suburb_shanghaiint at bgleft 
    with charamove

    "Following her advice, I lead Lilly to the nearest booth, and Hanako follows."
    
    show lilly invis at twoleft
    show hanako invis at tworight
    with None
    
    show lilly basic_smileclosed at twoleftsit
    show hanako basic_normal at tworightsit
    with dissolvecharamove

    "As I begin to sit myself next to Lilly, I realize the appropriateness of this place for Hanako."

    "The high-backed booths totally separate you from the rest of the room, and it doesn't look like it gets all that many customers."
    
    "All of the furnishings, from the cushions on the benches to the condiment holders, look dated but aren't overly worn."

    "I wonder if Lilly deliberately selects places like this to take Hanako?"

    "She seems like the type that would go to lengths to cater to Hanako's unique predicament."
    
    play music music_another fadein 4.0

    show lilly basic_weaksmile at twoleftsit
    with charachange

    li "So, Hisao, I didn't know you played chess…"

    hi "Well, not very well, but I know how to play."
    
    show lilly basic_smile at twoleftsit
    with charachange

    li "Now, don't keep me waiting… who won?"

    "Lilly's innocent smile makes me hesitate. I don't really want to look like I'm lording my victory over Hanako."
    
    show hanako cover_bashful at tworightsit
    with charachange
    
    ha "H-Hisao did."
    
    hi "Yes… but not by much…"
    
    "Damn. Saying that out loud makes me feel like I've done something terrible."
    
    show lilly basic_giggle at twoleftsit
    with charachange

    li "Well then, congratulations are in order. Good job, Hisao."

    hi "Er, thanks. But I haven't played in ages. It felt kinda good to play again."
    
    show hanako basic_smile at tworightsit
    with charachange
    
    ha "Y…yes it did."
    
    "Hanako fidgets with her hair a little and looks away as she replies, but a small smile emerges."

    "It's a little more extreme of a reaction than I expected, but still kind of cute in a Hanako-esque way."
    
    show hanako defarms_shock at Position(xpos=0.8, ypos=1.15) 
    show lilly basic_surprised at Position(xpos=0.2, ypos=1.15) 
    with Dissolvemove(0.5)

    show yuukoshang worried_up
    with charaenter

    "It throws me a little off guard, and only Yuuko's cataclysmic re-entry shocks me back into conversation."

    hi "Are you alright there, Yuuko? Do you want a hand?"
    
    show yuukoshang neurotic_up 
    show hanako def_worry at Position(xpos=0.8, ypos=1.15) 
    with charachange

    yu "I'm fine I'm fine I'm fine. I have to do this properly, it's my job."
    
    show yuukoshang worried_up 
    with charachange

    "Concentration plays across her face as she stares at the tray in her hands, as if simply looking at its contents will hold them in place."
    
    show yuukoshang neurotic_down # tremble # what is that supposed to be? replaced with "neurotic_down" for now [str]
    with charachange

    "Sadly, this doesn't prove all that effective; the cups and saucers slowly dance around, occasionally clattering as they collide with one another."

    show yuukoshang worried_up at Position(ypos=1.1) 
    with ease

    show yuukoshang worried_up at center 
    with ease

    "With great care, Yuuko sets the tray down on the table with only the subtlest of crashes."

    show yuukoshang happy_down 
    with charachange

    yu "There, see!"

    hi "Er, well done?"
    
    show lilly basic_weaksmile at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Thank you, as always, Yuuko."
    
    show yuukoshang neutral_down at Position(ypos=1.2) 
    with Dissolvemove(0.2)
    
    with Pause(0.2)

    show yuukoshang neutral_down 
    with ease

    "Yuuko's head rockets downwards in her distinctive bow before answering."
    
    show yuukoshang closedhappy_down 
    with charachange

    yu "You're very welcome."
    
    show lilly basic_smile at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Would you like to join us? I would like to discuss those books we were going over the other day…"

    "Ah, that's right. Lilly and Yuuko were discussing a pile of books when I first met Hanako."
    
    "Something about Lilly helping with the braille…"
    
    show yuukoshang neurotic_up 
    with charachange

    yu "Ah… yes. We didn't get the chance to go through them, did we?"
    
    show yuukoshang neurotic_up at centersit
    with charamove

    "Yuuko hastily sits down next to Hanako."

    "Apparently her dedication to this job only goes as far as her concentration; once it is broken, she suddenly loses it."
    
    show yuukoshang smile_down at centersit
    with charachange

    yu "I'll be in the library tomorrow afternoon if you'd like to try again then…"
    
    show lilly basic_cheerful at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "That sounds perfect, I'll meet you there after classes."

    show hanako emb_timid at Position(xpos=0.8, ypos=1.15) 
    with charachange

    ha  "Um… L-Lilly…"

    show lilly basic_oops at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Oh dear, that's right. Tomorrow is Monday, how could I have forgotten?"

    "I'm starting to feel a little left out of the loop here. Then again that's to be expected; I have been here for barely a week so it's impossible to know everyone's schedule."

    show lilly basic_weaksmile at Position(xpos=0.2, ypos=1.15) 
    with charachange
    
    li "Well, perhaps we could come to some other arrangement."
    
    show lilly basic_smile at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Yuuko, will you be in the library later in the week?"

    show yuukoshang worried_up at centersit
    with charachange

    yu "Hmm, maybe, but this is already overdue…"
    
    show hanako emb_downsad at Position(xpos=0.8, ypos=1.15) 
    with charachange

    ha "A-and I am out of supplies…"
    
    show lilly basic_listen at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "This is quite the dilemma."

    "Lilly ponders for a second before discovering the answer."

    show lilly basic_planned at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Hisao! Hisao could do it!"

    hi "Um, do what? You lost me quite some time ago…"
    
    "Being volunteered for something without even having the slightest idea what is going on isn't really my thing."
    
    "And here I thought I had finally escaped the clutches of the Student Council and their repeated attempts to recruit me."
    
    show lilly basic_smileclosed at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Oh, of course. The other day I was helping Yuuko sort the new Braille books in the library."
    
    show lilly basic_weaksmile at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "But Hanako and I usually go shopping on Monday afternoons; it's quieter on that day than on weekends."
    
    li "Last week we couldn't go because I was busy with the festival. I managed to slip away later in the week but Hanako couldn't make it."
    #Again, need2check if this is flow-conditional or not. -SC
    
    hi "Well, since I can't read Braille, I'm assuming you'd like me to go shopping with Hanako?"
    
    show lilly basic_smile at Position(xpos=0.2, ypos=1.15) 
    show hanako emb_timid at Position(xpos=0.8, ypos=1.15) 
    with charachange

    li "Correct. You were a great help to me the other day."

    hi "I think I can handle that. Hanako, what do you think?"

    show hanako basic_smile at Position(xpos=0.8, ypos=1.15) 
    with charachange

    ha "I-if you wouldn't mind…"

    hi "Of course not. I'm still not familiar with all the stores in the area, so it sounds like a good idea."
    
    show hanako basic_bashful at Position(xpos=0.8, ypos=1.15) 
    with charachange

    ha "O-okay."
    
    show lilly basic_smileclosed at Position(xpos=0.2, ypos=1.15) 
    with charachange

    li "Well, now that everything is all sorted out, shall we have some tea?"

    li "It's been getting cold all this time…"

    show yuukoshang panic_up at centersit
    with charachange

    yu "It's my fault! Let me pour that for you…"

    "Yuuko reaches out with shaking hands, but I intercept her."

    "She looks in no state to be handling hot liquids."

    hi "It's alright, I've got it. Besides, you've already made the tea and sandwiches, hence have fulfilled your duties, right?"

    show yuukoshang neurotic_up at centersit
    with charachange
    
    yu "I… I guess."
    
    "Yuuko relaxes a little, but still watches eagerly as I share out the assortment."
    
    stop music fadeout 1.0
    play ambient sfx_fireworks

    show white 
    with Dissolve(0.1)

    hide white 
    show fireshine 
    show hanako defarms_shock at Position(xpos=0.8, ypos=1.15) 
    show yuukoshang panic_up at centersit
    show lilly basic_surprised at Position(xpos=0.2, ypos=1.15) 
    with charachange

    "As I am about to bite into the sandwich, a low, loud rumble can be heard, along with a flash of light from outside."
    
    show lilly basic_weaksmile at Position(xpos=0.2, ypos=1.15) 
    show yuukoshang smile_down at centersit
    show hanako emb_timid at Position(xpos=0.8, ypos=1.15) 
    with charachange

    li "Ah, I take it the show has started."
    
    hide fireshine 
    show bg misc_sky_ni as front 
    show fireworks 
    with locationchange

    "Only now looking outside, I realize that dusk has come and gone, leaving us in the peak of twilight."

    "Sparking tracers arc upwards ready to explode in the floral colors of fireworks."

    hide fireworks 
    hide front 
    show fireshine 
    show yuukoshang happy_down at centersit
    with locationchange

    yu "Let's go watch!"
    
    show yuukoshang panic_up at centersit
    with charachange

    yu "Oh… sorry Lilly…"
    
    show lilly basic_ara at Position(xpos=0.2, ypos=1.15)
    with charachange
    
    #show hanako_shanghaifw behind bg
    show hanako_fireshine behind bg
    #at Zoom((800,600),(40, 30, 720, 540),(0, 0, 800, 600),22.0, time_warp=_ease_time_warp, xalign=0.5, yalign=0.5)
    show ev hanako_shanghaiwindow behind hanako_fireshine
    with None

    li "Please, don't miss the show on my account."

    li "From what I've heard, this isn't such a bad place to watch them from…"
    
    play music music_serene fadein 4.0

    hide fireshine 
    hide bg 
    hide hanako 
    hide lilly 
    hide yuukoshang 
    with locationskip

    "With the exception of Lilly, we rush to the window of the small tea house to watch the show."

    "The strobe of colored lights play across Hanako and Yuuko's smiling faces, and for a second I forget to look out the window."

    "In this totally new world, there are a few things that don't change."

    "I think that's why the school makes such a fuss over this festival. It's a chance to show the similarities between everyone."
    
    stop ambient fadeout 3.0
    
    hide hanako_fireshine
    hide hanako_shanghaifw 
    with Dissolve(1.0)

    "The show is over all too quickly; fireworks are expensive, even for the most well-funded schools."
    
    scene bg suburb_shanghaiint at bgright 
    with locationchange

    "Before we return to our tea and sandwiches, Hanako turns to me."

    show hanako emb_downsmile_close 
    with charaenter

    ha "Um, t-thanks for today."
    
    show hanako emb_smile_close 
    with charachange

    ha "… and tomorrow."

    hi "That's okay; I don't think that I could have faced those crowds either."

    hi "On days like this it's more relaxing to spend some time away from everyone, don't you think?"
    
    show hanako basic_normal_close 
    with charachange

    ha "Y-yeah."

    hi "Anyway, we've been delaying this tea for far too long now, let's get back."
    
    show hanako basic_bashful_close 
    with charachange

    ha "S-sure."
    
    stop music fadeout 6.0

    hide hanako 
    with charaexit

    show bg suburb_shanghaiint at bgleft 
    with charamove

    show lilly basic_smileclosed at leftsit
    show yuukoshang neutral_down at centersit
    with locationchange

    show hanako invis at right
    with None
    
    show hanako basic_smile at rightsit
    with dissolvecharamove

    "We return to the booth and our light meal."
    
    show lilly basic_smile at leftsit
    with charachange

    li "That sounded impressive. Bigger than last year at least…"
    
    show yuukoshang happy_down at centersit
    with charachange

    yu "Yeah it was great! I've never seem them put on such a show."

    yu "It gets better every year!"
    
    show lilly basic_weaksmile at leftsit
    with charachange

    li "I'm afraid, however, that during that time, the tea has gone cold."

    show yuukoshang panic_up at center 
    with Dissolvemove(0.2)
    
    play music music_ease fadein 0.5

    yu "Oh no! Let me make some more! This is my fault!"

    hi "Calm down, Yuuko, it's no-one's fault."

    "I take a sip from my cup, just to prove the point."

    hi "This tea isn't too bad cool, anyway. It's like an iced tea."

    show yuukoshang worried_up 
    with charachange

    yu "Really?"

    hi "Yes, really. If you add a bit of sugar it's kinda nice."
    
    show yuukoshang neurotic_up 
    with charachange

    yu "Are you sure?"

    hi "I'm positive. Now why don't you sit down and we'll finish this together?"

    show yuukoshang smile_down 
    with charachange

    yu "O-okay."

    show yuukoshang smile_down at centersit 
    with charamove

    "Yuuko doesn't seem convinced, but sits down regardless."

    "She carefully measures out about five teaspoons of sugar and adds them to her tea."

    hi "Er, I said a bit of sugar…"
    
    show yuukoshang neutral_down at centersit
    with charachange

    yu "I know, but I like my tea sweet anyway."

    "Curiously I peer into her cup. As expected, hardly any of the sugar dissolves in the cold liquid."

    "She stirs it twice before upturning the cup and drinking the contents, sugar and all, in a single mouthful."

    show yuukoshang happy_down at centersit
    with charachange

    yu "You're right! That's not bad at all!"

    hi "Er, that's good…"

    "I look back to Lilly and Hanako, both of whom have finished their meal as I witnessed Yuuko's personality in action."

    "Not wanting to hold anyone up, I use her tactic and finish the remainder of my tea in a single swill."

    hi "Well then, it seems we're all finished."
    
    show lilly basic_smile at leftsit
    with charachange

    li "Should we head back now or do we want seconds?"

    show yuukoshang neurotic_up at centersit
    with charachange

    "Yuuko's expression shows that this is quite clearly not a good idea."

    hi "I think that it would be best if we got back soon."

    hi "We do have to get back before curfew, after all."
    
    show lilly basic_smileclosed at leftsit
    with charachange

    li "Oh, that is a good point."
    
    show lilly basic_smile at leftsit
    with charachange

    li "I'll see you tomorrow, Yuuko."
    
    show yuukoshang neutral_down at centersit
    with charachange

    yu "Okay, have a safe trip everyone and thank you for coming."

    stop music fadeout 9.0

    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')
    play ambient sfx_cicadas fadein 0.5

    scene bg suburb_shanghaiext_ni 
    with locationchange

    "We make our way out of the small tea house and into the dark of the night."
    
    $ renpy.music.set_volume(0.40000000000000002, 1.0, channel='ambient')
    scene bg suburb_roadcenter_ni 
    with locationchange

    "Lilly and Hanako once again take point, but under the cover of darkness Hanako seems slightly less stressed than she did on the trip here."

    "We move against the occasional group of people emptying the school grounds, but Hanako seems to lead us along a few minor roads, avoiding the bulk of the crowd."

    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')

    scene bg school_dormext_full_ni 
    with locationskip

    "Outside the dorms the school seems strangely quiet when compared to the noise of the day."

    hi "Well then, thank you both for today. I think I learned a lot."
    
    show hanako emb_timid_ni at Position(xanchor=0.5, xpos=0.59) 
    show lilly basic_weaksmile_ni at Position(xanchor=0.5, xpos=0.41) 
    with charaenter

    li "You're most welcome, but I'm afraid that I really must be going."

    li "Today really wore me out."

    "That's right; Lilly would have spent all of today on her feet, and I can imagine that walking outside of the school would be pretty tiring for her."
    
    "I feel a pang of guilt as I remember that I was probably the only one in the school that got up around ten this morning."

    hi "Sure thing."

    hi "Well, I'll see you both tomorrow. Goodnight."
    
    show lilly basic_cheerful_ni at Position(xanchor=0.5, xpos=0.41) 
    with charachange

    li "Goodnight, Hisao."
    
    show hanako basic_smile_ni at Position(xanchor=0.5, xpos=0.59) 
    with charachange

    ha "N…night."
    
    hide hanako 
    hide lilly 
    with charaexit
    
    stop ambient fadeout 4.0

    "The girls return to their dorm, and I to mine."

    "Actually, now that I consider it, today tired me out as well."

    #Fade through black to the next scene.
    #I also know that this is a late request, but I think that this is a good place to put the Act 2 Card.
    return

    #---------------------------------------------------------

label en_H3:
    
    window hide None

    scene black 
    with dissolve

    $ renpy.music.set_volume(0.0, 0.0, channel='ambient')
    play sound sfx_alarmclock

    with Pause(1.2)

    play sound sfx_impact2

    window show
    
    "My alarm blares some cheesy pop tune into my ears, only to be swiftly silenced by my fist."
    
    scene bg school_dormhisao 
    with openeye

    "My body switches into auto-mode, carrying my subconsciousness out of bed and into my uniform."
    
    scene bg school_scienceroom at bgright 
    with locationskip
        
    "Before I know it, I'm opening the door to class 3-3, glad to see that I'm not the only one who seems to be a little hung-over from festival week."

    "Every face in the classroom looks gaunt. With the festival now over, it's as if everyone's life dreams have been achieved."

    "With nothing left to live for, the students have relied on instincts alone to guide them to class."

    "Or maybe I'm just looking into it too much."

    "I slowly make my way to my seat, and it's only then that I realize why the room is so peaceful."
    
    "The seats beside mine are blissfully empty; the world's loudest interpreter-for-the-deaf has yet to arrive."
    
    play sound sfx_doorslam
    play music music_running

    show misha invis at Position(xanchor=0.0, xpos=1.0)
    with None
    
    show misha hips_grin at right
    with Dissolvemove(0.3)
    with vpunch

    "Just as I am about to sit down, the door flies open, revealing a resplendent Misha; her drills bob from the dramatic entrance and arms stretched towards the sky."

    show misha hips_laugh at right 
    with charachange
    
    mi "Ya-hooo! It's all over!"

    "It would appear that not everyone is affected by the post-festival depression."

    "The rest of the class glare at her, obviously thinking the same thing I am."
    
    show misha sign_confused at right
    with charachange

    "Misha, still frozen in the doorway with her arms still in the air, nervously looks around."

    "It's obvious that she senses the foul mood, but can't work out exactly what to do."
    
    show misha sign_confused
    with ease_decel

    "Suddenly, she jerks forward."
    
    show misha perky_sad 
    with charachange

    mi "Hey!"
    
    show shizu invis behind misha at Position(xanchor=0.5, xpos=1.0)
    with None

    show misha perky_sad at twoleft 
    show bg school_scienceroom at center 
    show shizu adjust_happy at tworight 
    with dissolvecharamove

    "As she stumbles into the classroom, she reveals Shizune, arm still extended from where she shoved Misha."
    
    show shizu basic_normal at tworight 
    with charachange

    shi "…"

    hi "Thanks for the entertainment, but shouldn't you two take your seats?"
    
    show shizu behind_frown at tworight 
    with charachange

    shi "…"

    "Still slightly embarrassed, Misha takes a few seconds to realize she has to translate."
    
    show misha sign_smile at twoleft 
    with charachange

    mi "Oh! Yeah! Shizu-chan says she's not happy with you ditching us last week."
    
    show misha cross_frown at twoleft 
    with charachange

    mi "We were really busy!"

    hi "Is that so? What about all the work I did for you two?"
    
    show shizu cross_angry at tworight 
    with charachange

    shi "…"
    
    show misha hips_grin at twoleft 
    with charachange

    mi "She says that only counts for Council members. Since you declined, she doesn’t owe you anything."
    
    show misha hips_grin_close at twoleft 
    with characlose

    "Misha leans closer, and whispers conspiratorially into my ear."

    mi "Actually, I think she's just a little sore that you didn’t spend the day with her."
    
    show misha hips_smile_close at twoleft 
    with charachange

    mi "She's really thankful for your work last week though."
    
    show shizu behind_frustrated at tworight 
    with charachange

    "Sensing that she is being talked about, Shizune lightly raps her fingers on her desk until Misha turns around to face her."
    
    show misha sign_smile at twoleft 
    with charadistant

    show shizu basic_angry at tworight 
    with charachange

    show misha hips_grin at twoleft 
    with charachange

    show shizu adjust_blush at tworight 
    with charachange

    "I can't understand any of the fast-paced signing that's going on, but from Shizune's slightly embarrassed expression, and Misha's poorly contained laughter, I can guess."

    stop music fadeout 8.0
    
    "While this exchange is happening, the door opens once again, but this time at a much more reasonable pace."
    
    show hanako invis at offscreenright 
    with None

    show bg school_scienceroom at bgleft 
    show shizu basic_normal at Position(xpos=0.42) 
    show misha hips_smile at Position(xpos=0.18) 
    show hanako emb_downtimid at right 
    with dissolvecharamove

    "Hanako quietly enters the room, and pulls the door closed behind her."
    
    show hanako emb_timid at right
    with charachange

    "Peering out from under her hair, she quickly scans the classroom."

    "Our eyes meet, and she suddenly stiffens. She closes her eyes, takes a deep breath, and then walks over to my desk."
    
    show hanako cover_distant at right
    with charachange

    ha "G…good morning Hisao."

    hi "Morning Hanako. You're a little late, aren't you?"

    "In fact, this is the first time I can remember coming in before Hanako."
    
    show hanako basic_normal at right
    with charachange

    ha "I… was talking to Lilly."
    
    show hanako basic_worry at right
    with charachange

    ha "A-about today."

    hi "Ah, so you've got her list then? We can leave straight after classes in that case."
    
    show hanako emb_smile at right
    with charachange

    ha "S-sure."

    hi "I'm looking forward to it."

    "Hanako briefly flashes her embarrassed smile at me then hurries off to her seat."
    
    scene bg school_scienceroom at bgright 
    with shorttimeskip

    play music music_normal fadein 3.0

    "During classes, it becomes apparent that it's not only the students that are a little despondent now that the festival is over."

    "Mutou simply gives us a list of exercises from the textbook and then sits behind his desk."

    "For a moment I totally forget the brief lunch period, such is the banality of the day."
    
    play sound sfx_normalbell

    "It's mind-numbing, and everyone seems surprised when the bells signal the end of the lessons."
    
    show shizu basic_normal at tworight 
    show misha perky_smile at twoleft 
    with charaenter

    "As I am packing up my bags, Shizune and Misha flank and entrap me."
    
    show misha hips_grin at twoleft 
    with charachange

    mi "Say, Hicchan, it's still not too late to join up. There's a lot of post-festival paperwork for us to complete…"

    hi "Er, sorry Misha, I've… got plans…"
    
    show hanako invis at offscreenright 
    with None

    show bg school_scienceroom at center 
    show shizu basic_normal at Position(xpos=0.42) 
    show misha hips_grin at Position(xpos=0.18) 
    show hanako cover_distant at right 
    with dissolvecharamove

    "As if sensing her cue, Hanako appears behind me, holding a small bag, and trying to avoid eye contact with the world."
    
    show misha cross_laugh at Position(xpos=0.18) 
    with charachange

    "Misha's eyes open wide, then she bursts into laughter."

    mi "BWHAHAHA! Hicchan, you move fast, don't you? We won't disturb your date any further! Bwahahaha!"
    
    show shizu behind_blank at Position(xpos=0.42)
    with charachange

    "Behind the roaring Misha, I see Shizune taking far too little interest in the scene. I might be taking this the wrong way, but I think she's deliberatly ignoring me."

    show hanako emb_downtimid_close at right
    with characlose
    
    "I feel a gentle tug on my shirt, and turn to see Hanako, eyes fixed firmly on the floor."
    
    show hanako emb_timid_close at right
    with charachange

    ha "L…let's…"

    hi "Got ya. Shizune, Misha, I'll see you later."

    hi "And I'm still not interested in the council."
    
    show misha cross_grin at Position(xpos=0.18) 
    with charachange

    mi "Spoilsport."
    
    stop music fadeout 2.0

    hide misha 
    hide shizu 
    with charaexit

    show bg school_scienceroom at bgleft 
    show hanako emb_timid_close at center 
    with charamove

    "Misha and Shizune retreat into the hallway, happily signing to each other."

    hi "Got all your stuff? Let's head off."

    play music music_soothing fadein 4.0

    scene bg school_gate 
    with locationskip

    "Floods of students pour out of the school gates and onto the road into town."

    "It's a little weird. It's almost a scene from any other high school, but the illusion fades because of the occasional missing limb and wheelchair."

    "One thing I do notice is that no-one is alone."
    
    scene bg school_road 
    with locationchange

    show hanako emb_downsad_close at center 
    with charaenter

    "And, as Hanako and I pass through the gates, I notice that she closes the distance between us."

    "Not enough to be considered \"close\", but she certainly isn't at her usual just-a-little-far position."

    "I guess we're not familiar enough for her to get as close as she does to Lilly."

    "However, even though she has moved a little closer to me physically, mentally she seems to have traveled a mile."

    "Her hands clutched around the leather straps of her bag to the point of whitening her knuckles, her head down and her mouth pursed closed."

    "She almost looks like she's being walked to the Principal's office for the first time."

    "I try to stifle a giggle at the thought, but it is futile."
    
    show hanako emb_timid_close 
    with charachange

    ha "W-what's the matter…?"

    "I guess there's no point in hiding it…"

    hi "Sorry. For a second there it looked like you were getting in trouble."

    show hanako defarms_strain_close 
    with charachange

    ha "W-w-what do you mean?"

    hi "I think you need to relax a little. We're not going too far, and it's only students around, right?"
    
    show hanako def_worry_close 
    with charachange

    ha "R-right."

    "It bothers me a little to see Hanako so worked up."
    
    hi "And you do this every week, don't you?"
    
    show hanako basic_worry_close 
    with charachange
    
    ha "Y-yes. With Lilly."
    
    "Of course. \"With Lilly.\" I wonder, has she ever left the school without her?"
    
    "It doesn't seem like much at first glance, but Hanako's dependence on Lilly is absurdly heavy."
    
    "If she can't even handle leaving the school without her, how would she have managed to survive if the two had never met?"
    
    "Maybe I'm looking into it a little too much." 
    
    hi "Well, I'm here. Besides, we're not going far. It'll be over before you know it."

    show hanako emb_downsmile_close 
    with charachange

    "Hanako's knuckles slowly regain their color as she tries to hide a small smile, but the effort of that seems to prevent further conversation."
    
    "We walk, side-by-side, down the winding road towards the town. As we continue along the footpath the crowd of students thins."
    
    "Faster students rush ahead, and the less mobile ones fall behind, rarefying the crowd into nothingness."
    
    scene bg suburb_konbiniext 
    with locationskip
    
    "By the time we reach the convenience store we are practically alone."

    scene bg suburb_konbiniint
    with locationchange

    "Using me as a shield between herself and the attendant, Hanako moves through the narrow aisles, adding an assortment of items to her basket."

    "Bread, milk, tea. …thyme?"

    "What kind of convenience store sells herbs?"

    "Then again, nothing about this town seems normal, which may not be such a bad thing in retrospect."

    "Everything is so different and confronting; dwelling on such matters isn't really an option."
    #..."confronting"? Wtf did you mean by this, crud... -SC

    "When I think about, it reminds me of Hanako."

    "No matter how much you try, you can't escape her scars. They still interrupt my train of thought when I see them."

    "As much as I don't want to admit it, I think I'm forcing myself to ignore them."
    
    "But, in a way, they remind me that we're all in this place for a reason."

    "…"

    "Hanako throws one last item into her basket then sheepishly holds it out to me, along with a few bank notes."

    show hanako emb_downtimid_close
    with charaenter

    ha "C-c-could you p-please…"

    "It takes me a second to understand what she's trying to say."

    hi "Oh, you want me to pay for this?"
    
    show hanako emb_downsad_close 
    with charachange

    "She nods, but doesn't look up."

    "I guess this task falls to Lilly on the usual occasions."

    hi "Sure. Lemme just grab a couple of things…"

    "Hastily I grab a few essential items for myself and head for the counter with Hanako in close tow."

    "The attendant gives me an indifferent nod as he scans in the items."

    "I suppose just ignoring us is one way to deal with the anomalies of Yamaku. They must get a lot of students here, being the closest store to the school."
    
    "The staff must all have their own way of dealing with us. Or maybe they don't; maybe it's only me who thinks twice about my unique schoolmates."

    stop music fadeout 2.0

    scene bg suburb_konbiniext_ss 
    with locationchange
    
    "Our transaction complete, Hanako and I head back out onto the street."

    scene bg school_road_ss 
    with locationskip

    play music music_tranquil fadein 10.0

    "The road is pretty much abandoned now. The students that were heading out have already left, and no-one has started returning just yet."

    "And, with only the school ahead on the road, there doesn't seem to be anyone else around."
    
    show hanako def_worry_close_ss at center 
    with charaenter

    "The emptiness certainly reflects on Hanako; her arms by her sides each carrying a bag, her head no longer bowed, and back to the correct position…"

    "It's almost as if she were enjoying this walk."

    hi "So, why all these weird things? Thyme? I can barely say that, let alone know how to use it…"
    
    show hanako basic_normal_close_ss 
    with charachange

    ha "I… sometimes… like to m-make food."

    hi "Well, yeah, so do I but… Thyme?"

    hi "That's a little more advanced, don't you think?"

    show hanako emb_blushing_close_ss 
    with charachange

    ha "N-not really."

    hi "Well, I think it's cool. You'll have to teach me one day."

    show hanako emb_smile_close_ss 
    with charachange

    ha "S-sure."

    "She doesn't seem all that sure, but pushing the point doesn't seem all that wise."

    "At the very least, she seems a great deal happier than she did on the walk down here."

    "That alone makes me a little happier."

    scene bg school_dormext_full_ss 
    with shorttimeskip

    show hanako basic_normal_close_ss 
    with charaenter

    "Outside the girl's dorm, Hanako and I sort out the grocery bags with our respective purchases."

    "In comparison, my things look positively plain."

    hi "I tell you, you're putting me to shame here…"
    
    show hanako defarms_shock_close_ss 
    with charachange

    ha "N-no I'm not… I just…"

    hi "I'm only joking."
    
    show hanako def_worry_close_ss 
    with charachange

    hi "I have a stack of homework that I skipped last week, so I must leave now."

    hi "Will you be all right getting that to your room?"
    
    show hanako cover_bashful_close_ss 
    with charachange

    ha "Y-yeah."

    hi "Sure? Okay then. I'll see you tomorrow."
    
    show hanako basic_smile_close_ss 
    with charachange

    ha "B-bye."
    
    hide hanako 
    with charaexit

    stop music fadeout 7.0

    "We part ways, and I return to my room."

    scene bg school_dormhisao_ss 
    with locationskip

    "Piles of papers sit upon my desk, begging to be completed. With the entire ruckus of the last week, I've had barely any time to catch up."

    "I tried to keep up with my studies while I was in the hospital, but some of this stuff I've never seen before, even back in my old school."

    "Totally unprepared, I pop the top on a can of soda, and get to work."
    
    scene black 
    with dissolve

    return

    #---------------------------------------------------------
      
label en_H4:
    
    scene black 
    with None

    play music music_daily fadein 6.0

    scene bg school_dormhisao 
    with openeye #locationchange

    "The days are really starting to heat up."

    "This morning, I awoke covered in sweat, which is a little disappointing if you're alone."
    #What. -SC

    "By the time the student body starts leaving their dorms for breakfast and morning duties, the sun has taken full effect, and oddly that puts me in high spirits."

    "It's not even eight, yet I feel that this day is going to be one of those pleasant, tranquil warm ones."

    "If I weren't at a school that considered every absence from class as a sign of a life-threatening situation, I'd consider skipping the whole day and just relaxing on the hill near the track."

    "Yes, today will be a genuinely lazy day."
    
    "For a second, I stop, mid-stretch, and consider the Nurse's warning about exercise. Maybe I should have kept up those morning jogs."
    
    "Running with someone like Emi might have been a little testing, but if I worked at my own pace…"
    
    "Ah, who am I kidding? I couldn't stick to something like that without some kind of motivation."
    
    "It's not like I sit around all day. The walk to and from Auramart counts as exercise, right? Especially the walk back up the hill…"
    
    "Yeah, it's no big deal. Compared to months lying in a hospital bed I'm getting plenty of exercise."

    scene bg school_scienceroom 
    with shorttimeskip

    "It seems that I'm not alone in my appreciation of the day."

    "Nearly every member of the class is glancing through the window and into the tantalizing sky."

    "Even the steadfast Shizune seems to lack her usual vigor for schoolwork."

    "Misha, as brazen as ever, has even unbuttoned the top buttons of her shirt and is fanning herself with a note book."

    "I must have been staring, as she's now sticking her tongue out at me."

    "However, she shows no signs of halting her efforts, nor is she trying to hide the fact."
    
    play sound sfx_normalbell

    "The lunch bells seem to catch everyone by surprise, and the class empties at a much slower pace than usual."

    "The heat seems to be draining the need to rush from everyone."
    
    stop music fadeout 8.0

    "Well, almost everyone."
    
    show hanako emb_emb 
    with charaenter

    ha "H… Hisao?"

    hi "Hey there Hanako, what can I do for you today?"

    "Hanako already has a lunch-bag in hand."

    "I don't have to be a scholar to work out where this is going."
    
    show hanako emb_smile 
    with charaenter

    ha "Um… would you like to have lunch with us again?"
    
    show hanako basic_bashful 
    with charaenter

    ha "I… I brought enough for everyone…"

    hi "Awesome. You don't have to be so formal about it though."
    
    show hanako basic_normal 
    with charaenter

    ha "Ah… right."

    hi "I take it we're going to the tea room?"
    
    show hanako cover_worry 
    with charaenter

    ha "P…please."
    
    show hanako basic_normal 
    with charaenter

    ha "Lilly said she'll meet us in there, so we should… should…"

    hi "Should?"
    
    show hanako emb_smile at center 
    with charaenter

    ha "…should go ahead together…"

    hi "Sounds like a plan. This heat has made me pretty hungry."

    "Hanako breathes a sigh of relief, and I gather my things together."

    scene bg school_miyagi 
    with locationskip

    play music music_happiness fadein 1.0

    "As usual, the aura of the Tea Room is refreshing, isolated from the rest of the world."

    "Then again, the usual din of the school seems to be a bit subdued; most likely from laziness promoted by heat exhaustion."

    "Hanako slowly spreads her food on the table, intently focusing on every little movement, as if she's trying to keep her mind off other thoughts."

    "It's not much, but I can tell from her demeanor that she has specially prepared everything."

    hi "I guess Lilly isn't here yet. Should we start without her?"
    
    show hanako emb_timid at centersit
    with charaenter

    ha "S-she'll be here soon…"
    
    show hanako emb_downtimid at centersit
    with charachange
    
    "Hanako struggles with the lid of the container of rice."
    
    hi "Here, let me help with that..."
    
    "I take the container from Hanako's hands, and try to force open the lid."
    
    "Try as I might, it seems wedged shut."
    
    hi "Let me guess, did you put this in while the rice was still hot?"
    
    show hanako emb_sad at centersit
    with charachange
    
    ha "Y-yes. I was in a rush…"
    
    "I put the container on the table between us."
    
    hi "I thought so. It looks like this is wedged shut. We'll need some hot water to get it open."
    
    hi "But that could be a pain in here. We'd get water everywhere."
    
    li "Well, in that case, how about I contribute to today's meal?"

    show lilly invis at left 
    with None

    show hanako emb_smile at tworightsit
    show bg school_miyagi at bgright 
    show lilly basic_cheerful at twoleft 
    with dissolvecharamove

    "At the door, Lilly holds up a bag bulging with various buns and bread rolls."
    
    show lilly basic_smileclosed at twoleft
    with charachange

    li "Yuuko gave these to me as payment for helping her out yesterday."

    li "Since you two had a change of plans because of me, I thought I'd share the spoils…"

    hi "Lilly, you're a lifesaver. Here, let me get that for you…"
    
    show lilly basic_smileclosed at twoleftsit
    with charamove

    "With a little guidance, Lilly's bread assortment joins Hanako's rice-less platter. I hastily make some tea to complete the picture."

    hi "Well, I'm looking forward to this."

    show hanako emb_downtimid at tworightsit
    with charachange

    "As I take a bite, I notice Hanako trying her hardest to not look like she is looking at me."

    "It's nothing special, but then again I can't really complain. I'm pretty lazy when it comes to cooking for myself."

    hi "Not bad. Is this made with the stuff you bought yesterday?"
    
    show hanako emb_blushtimid at tworightsit
    with charachange

    ha "Y-yes."
    
    "Hanako's eyes shout at me, begging for some kind of feedback."

    hi "Well, it was clearly worth it. Thanks, Hanako."
    
    show hanako cover_bashful at tworightsit
    with charachange

    ha "I… I wanted to show you this… after yesterday…"

    hi "It's okay. I was just a little surprised at the stuff you were buying."
    
    show lilly basic_weaksmile at twoleftsit
    with charachange
    
    li "Hanako's always liked to experiment like that when it comes to food."

    li "I think it's good… most of the time…"

    "Whilst Lilly's smile doesn't waver, the slight change in her tone tells me that things have not gone so well in the past."

    "And it's not like Hanako has many people to sample her cooking…"
    
    stop music fadeout 7.0

    "Hang on… was Lilly waiting for me to go first? She didn't start eating until after I said it was alright…"

    "…It might be a good idea to start bringing a back-up lunch from now on."

    hi "Well, it's good, and that's all that counts, right?"
    
    show hanako basic_smile at tworightsit
    with charachange

    ha "R-right."
    
    show lilly basic_smileclosed at twoleftsit
    with charachange

    "Lilly, satisfied at not being the first to sample Hanako's creation, starts consuming her meal with clinical precision."
    
    "Her fingers dance gently around the containers, locating and retrieving portions of food like a UFO-catcher."
    
    "Not wanting to miss out, I start filling up myself."
    
    show hanako emb_downsmile at tworightsit
    with charachange
    
    "Hanako takes a different approach, waiting until Lilly and I have our hands clear before quickly snatching up her share."
    
    show hanako emb_smile at tworightsit
    with shorttimeskip

    play music music_dreamy fadein 4.0
    
    "Before long the containers are empty, save for the still-shut rice container."
    
    show lilly basic_smile at twoleftsit
    with charachange
    
    li "Well, thank you Hanako, that was filling."
    
    show hanako basic_smile at tworightsit
    with charachange

    ha "N-no… thank you for the bread…"

    hi "Yes, it was quite the treat."
    
    show lilly basic_planned at twoleftsit
    with charachange

    li "You're both welcome."
    
    show lilly basic_weaksmile at twoleftsit
    with charachange

    li "But now, I must be getting back. It is far too easy to be late after eating here."

    hi "Yes, I see what you mean. I think we'll just clean up here and then head off."
    
    show lilly basic_smileclosed at twoleft 
    with dissolvecharamove

    li "Well then, good day."
    
    hide lilly 
    with charaexit
    
    show hanako basic_smile at centersit
    show bg school_miyagi at center 
    with charamove

    "Lilly leaves, her cane tapping away down the quiet hallway."

    "Hanako and I quickly pack our things and stay seated, waiting for the bell."
    
    $ renpy.music.set_volume(0.5, 1.0, channel='music')

    scene bg misc_sky at Fullpan(20.0) 
    with locationchange

    "Together, we stare out the window and into the endless azure sky."
    
    play sound sfx_warningbell
    
    "If it weren't for the pealing of the bells, I would have sworn that time had stopped."

    "The urge to skip class rises in my gut."

    "I shoot a glance at Hanako, who shows no signs of moving either."

    ha "Not… just yet…"
    
    $ renpy.music.set_volume(1.0, 3.0, channel='music')

    scene bg school_miyagi 
    show hanako basic_smile at centersit
    with shorttimeskipsilent

    "The interval between the warning bells and the end of lunch bells passes in the blink of an eye."

    hi "We really should go… people will freak out and start a search party if we skip…"
    
    show hanako basic_distant at centersit
    with charachange

    "Hanako sighs."
    
    show hanako basic_normal at centersit
    with charachange

    ha "You're right."
    
    show hanako basic_normal 
    with charamove

    "Slowly, she rises to her feet, and I follow suit."
    
    scene bg school_staircase2 
    with locationskip

    "Silently, we make our way up the old stairs to the third floor of the school building and then to our classroom."
    
    scene bg school_hallway3 
    with locationchange

    play sound sfx_dooropen

    "At the door, I take charge and open the door ahead of Hanako, bowing my head down in apology in advance."
    
    scene bg school_scienceroom at center 
    with locationchange

    stop music fadeout 5.0

    hi "I'm sorry we're late, teacher."
    
    play sound sfx_doorclose

    "I am greeted not by stern words, nor an angered instruction to take my seat, but simply silence created by fifteen or so students trying not to laugh."

    show misha hips_grin
    with charaenter
    
    mi "Pff… pffwa…"

    "Make that about fourteen students trying, and one student failing."
    
    play music music_comedy

    show misha cross_laugh 
    with charachange

    mi "pftBwahahaha! The lovers return~!"
    
    show misha hips_laugh 
    with charachange

    "I quickly figure out what's going on."

    "Mutou, ever tardy, has yet to arrive."

    "However, the fact that Hanako and I have arrived together is blatantly obvious."

    mi "WAHAHAHA!"

    hi "Yeah, thanks. You can calm down now…"
    
    hide misha 
    show hanako invis at Position(xpos=1.0)
    with charaexit

    show bg school_scienceroom at bgleft 
    show hanako emb_downsad_close at Position(xpos=0.8)
    with dissolvecharamove

    "I step into the door, and realize that Hanako is almost firmly pressed against my back, hiding herself from the class."
    
    show hanako invis at Position(xpos=0.7)
    with dissolvecharamove

    "As I near my seat, she bolts for her desk at the back of the class and hides her face in her arms."
    
    scene bg school_scienceroom at bgright 
    with charamove

    "Quickly checking the door for any signs of the teacher's arrival, I make a trip to Hanako's desk and whisper in her ear."

    hi "Don't worry about Misha, she's always like this. I enjoyed myself today. Don't sweat it, okay?"

    "Hanako nods her head behind her folded arms, but still doesn't show her face."
    
    play sound sfx_dooropen

    show muto invis at tworight 
    with None

    show muto normal 
    show bg school_scienceroom at center 
    with dissolvecharamove

    "I yearn to stay and console her more, but Mutou picks this exact moment to enter the class, half-way through his lecture, as if he started it in the hallway."

    show muto smile
    with charaenter
    
    mu "…which, of course, is directly proportional to the charge but inversely proportionally to the square of the distance…"
    
    hide muto 
    with charaexit

    play sound sfx_doorclose

    "He's so engrossed in his speech that he doesn't even notice me sneaking back into my seat from Hanako's desk."

    return

#-----------------------------

label en_H5:
    
    $ renpy.music.play(music_comedy, fadein=0.5, if_changed=True)
    
    scene bg school_scienceroom
    with None
    
    "Whilst Muto's spiel rambles on, Misha leans over to me."

    show misha invis at offscreenleft 
    with None

    show misha perky_smile_close at Position(xanchor=0.5, xpos=0.16)
    with dissolvecharamove

    mi "The teacher may not have noticed your tardiness, but I did."

    "That much is obvious from the show you just put on."
    
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "I have been instructed to let you off the hook for today, but only on one condition."

    hi "Oh? And what would that be?"

    show misha sign_smile_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "You have to help us this afternoon!"

    "I crane my neck to look over Misha's shoulder."

    "Shizune is conveniently not making eye contact with me."

    "I'm guessing that she would be whistling nonchalantly right now, if that was possible."
    
    hi "Fine. Just for today."
        
    hi "I've already told you I'm not joining the council, remember?"
    
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.16)
    with charachange
        
    mi "Of course! Doing so could be considered… um, considered…"
    
    show misha perky_confused_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    "She looks down at her notebook, obviously looking for her place in her script."
    
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "…under duress and hence would be against regulations."

    hi "How very strange of you to be considerate of the regulations now."
    
    show misha sign_smile_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "Things should be done by the book!"
    
    show misha perky_smile_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    mi "It's just that the book hasn't been written for every situation, so there are times when it can be ignored."

    hi "And yet, you two wonder why no-one else wants to be in the student council…"

    #maybe a Misha sprite with her sticking out her tongue cold be useful
    
    stop music fadeout 3.0

    show misha hips_frown_close at Position(xanchor=0.5, xpos=0.16)
    with charachange

    with Pause(0.3)

    show misha invis at offscreenleft 
    with dissolvecharamove

    hide misha 
    with None
    
    #how'd that request work out for you, crud?

    "After poking her tongue out at me, Misha returns to her workbook, and we battle our way through the latter half of the school day."

    #SFX bells
    
    with shorttimeskip

    play sound sfx_normalbell

    show shizu invis at offscreenright 
    show misha invis at offscreenleft 
    with None

    show misha hips_smile_close at twoleft 
    show shizu behind_blank_close at tworight 
    with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

    "Before I can even stand up, Misha and Shizune have placed their hands on both my shoulders."

    hi "Hey, I said I'd help out, damn…"
    
    play music music_shizune fadein 1.0

    show misha hips_grin_close at twoleft
    with charachange

    mi "This is just insurance, Hisao, insurance!"
    
    show hanako invis at offscreenright behind shizu 
    with None

    show misha hips_smile_close at Position(xpos=0.17) 
    show shizu behind_blank_close at Position(xpos=0.5) 
    show bg school_scienceroom at bgleft 
    show hanako emb_timid at Position(xanchor=0.5, xpos=0.9)
    with dissolvecharamove

    ha "H-Hisao?"

    "Hanako timidly tries to leave the room by circling around us and I suddenly realise that this may be my one chance to escape."

    hi "Oh hey Hanako. What's up?"
    
    show shizu basic_angry_close at Position(xpos=0.5) 
    with charachange

    shi "…"
    
    show misha hips_frown_close at Position(xpos=0.17) 
    with charachange

    mi "Hey, what makes you think you've got time to chat?"

    hi "Oh relax, this won't take long… Sorry Hanako, you were saying?"
    
    show hanako emb_downtimid at Position(xanchor=0.5, xpos=0.9)
    with charachange

    ha "I… I was going to go to the library, and… and I thought…"

    "Hanako's thumbs dance around each other and her eyes flit around the room, looking everywhere but at us."
    
    show misha sign_smile_close at Position(xpos=0.17) 
    with charachange
    
    mi "Sorry Hanako, but Hisao has to come with us. He's got work to do."
    
    show shizu behind_smile_close at Position(xpos=0.5) 
    with charachange

    shi "…"
    
    show misha hips_grin_close at Position(xpos=0.17) 
    with charachange

    mi "Oh! But you can help too if you'd like."
    
    show hanako cover_worry at Position(xanchor=0.5, xpos=0.9)
    with charachange

    ha "Um…"
    
label en_choiceH5:
menu:
    with menueffect

    mi "So, how about it Hisao?"

    "What do you think, Hanako?":
        return m1

    "I've done enough work for the council already.":
        return m2

label en_H5_1:
    #-----------------------    
    
    show bg school_scienceroom at bgleft 
    show hanako cover_worry at Position(xanchor=0.5, xpos=0.9)
    show shizu behind_smile_close at Position(xanchor=0.5, xpos=0.5) 
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.17) 
    with None
    
    hi "What do you say Hanako? If we all help it shouldn't take long at all."
    
    show hanako emb_timid at Position(xanchor=0.5, xpos=0.9)
    with charachange

    "Hanako's fidgeting answers my question before she can even form the words."
    
    show hanako emb_downtimid at Position(xanchor=0.5, xpos=0.9)
    with charachange

    ha "I… I really need to go…"

    "Well, that was to be expected. Looks like it's just me and the Council girls again."

    "It's easier to resign myself to another afternoon's work in the small Council office."

    hi "I'll catch up with you later, okay?"
    
    show hanako emb_smile at Position(xanchor=0.5, xpos=0.9)
    with charachange

    ha "O-okay."
    
    stop music fadeout 3.0

    show misha hips_grin_close at twoleft 
    show shizu behind_smile_close at tworight 
    show hanako invis at offscreenright 
    show bg school_scienceroom at center 
    with dissolvecharamove

    show misha hips_smile_close at twoleft 
    hide hanako 
    with charachange

    mi "Right! Now that the farewells are over, it's work time!"
    
    scene bg school_hallway3 
    with locationchange

    "Misha and Shizune frog-march me to the Student Council office, never once letting go of my shoulders."

    "I feel a little bad for ditching Hanako like this, but if this is the price of getting Misha off her back, so be it."

    scene bg school_council
    with locationchange

    hi "So then, what are we up to today?"
    
    show misha sign_smile
    with charaenter

    play music music_ease fadein 8.0

    mi "Debrief!"

    hi "Huh? Isn't that supposed to happen after something?"
    
    show misha hips_grin 
    with charachange

    mi "Yup."

    mi "We have to collate all of the information from the festival so that Shizune can debrief the teachers."
    
    show misha hips_grin at twoleft 
    show bg school_council at bgleft 
    with charamove

    show shizu adjust_happy at tworight 
    with charaenter

    "Shizune drops a large pile of paperwork on the desk in front of me, and smiles succinctly."
    
    show misha hips_smile at twoleft 
    with charachange

    mi "You need to sort those out into two piles."
    
    show misha sign_smile at twoleft 
    with charachange

    mi "One for financial stuff, like receipts, one for feedback, one for positive feedback, maybe one for things that look like they could be problems next year, one for problems that probably won't be able to be fixed…"

    hi "That's a few more than two piles…"

    show misha perky_confused at twoleft
    with charachange

    mi "Huh? Oh, right. Yeah, I thought it would be only two piles."

    mi "My bad."

    hi "Right. While I am doing this, what will you two be doing?"

    show misha hips_grin at twoleft
    show shizu adjust_smug at tworight
    with charachange

    mi "Well, we missed lunch because we were collecting all of these reports, so we're going to go get some food!"

    "Why didn't you just sort them out while you were collecting them…"

    "Thankfully my self-defense mechanism kicks in and prevents me from opening my mouth and further deepening my situation."

    show misha perky_confused at twoleft
    with charachange

    mi "Eh?!"

    show misha perky_sad at twoleft
    with charachange

    mi "How is that fair?"
    
    show shizu behind_blank at tworight
    with charachange

    shi "…"

    "I was fretting over the unfair distribution of work so much that I didn't notice that Shizune had kept on signing."

    "If it weren't for Misha's outburst, I probably wouldn't have noticed at all."
    
    show shizu adjust_smug at tworight
    with charachange

    show shizu basic_normal at tworight
    with charachange

    show shizu behind_blank at tworight
    with charachange

    "Shizune seems to be delivering a fairly long string of commands to Misha, and none of them look good."
    
    show misha sign_sad at twoleft
    with charachange

    show misha perky_sad at twoleft
    with charachange

    show misha perky_sad at twoleftsit
    with charamove

    "Reaching a conclusion, Misha signs a couple of words back to Shizune, and then sits down at the desk next to me."
    
    show shizu adjust_happy at tworight
    with charachange

    hide shizu 
    with charaexit

    show misha perky_sad at centersit
    show bg school_council at center 
    with charamove

    "Shizune waves to the both of us before disappearing out the door."

    hi "What was all that about?"
    
    show misha perky_confused at centersit
    with charachange

    mi "Shizune was worried that you'd get it all wrong unless you were supervised."
    
    show misha perky_sad at centersit
    with charachange

    mi "And since she can't tell you how you are messing things up, she's making me stay."

    show misha cross_smile at centersit
    with charachange

    mi "But she is going to bring us back some food!"
    
    show misha cross_grin at centersit
    with charachange

    mi "How good is that!"

    "Misha's flippancy is out of this world. From down in the dumps to on top of the world over a little food."

    "It's hard to imagine how anyone could operate at that level."

    hi "Well, it could have been worse."

    hi "So what are we supposed to be doing?"
    
    show misha sign_smile at centersit
    with charachange

    mi "Collation."

    hi "I gathered that."
    
    show misha hips_smile at centersit
    with charachange

    mi "Well, let's just start making piles. We'll work out what the piles mean later."

    hi "Right…"
    
    show misha perky_smile at centersit
    with charachange

    "We start to separate all of the papers into increasingly complex piles."

    "At first it's just simple categories; financial, feedback, incident reports…"

    "Then they split apart into the good and bad reports, and further still, until it starts to look like we've just thrown the papers onto the desk."
    
    hi "This is hopeless."
    
    show misha perky_confused at centersit
    with charachange
        
    mi "Huh? Why? We're doing what we were told, right?"

    hi "Yes, but it looks like we're just making a mess."
    
    show misha hips_grin at centersit
    with charachange 

    mi "Ah, never mind that. That's Shizune's problem."
    
    show misha cross_grin at centersit
    with charachange 

    mi "So I think we can stop about here then."

    "It's almost like Misha's common sense left the room with Shizune."

    "Still, there's no point in arguing."

    show misha perky_smile at centersit
    with charachange

    mi "Anyway…"
    
    show misha cross_smile at centersit
    with charachange

    mi "What's the deal with you and Hanako?"

    hi "Deal?"
    
    show misha hips_smile at centersit
    with charachange 

    mi "You were hanging out with her today, weren't you?"
    
    show misha hips_grin at centersit
    with charachange 

    mi "Have there been any fireworks? Any gossip that you're withholding from me?"

    hi "If I told you about my own circumstances, it wouldn’t be gossip, would it?"

    show misha perky_confused at centersit
    with charachange

    mi "Er… I guess not…"

    hi "We're just friends I guess."

    hi "Why are you so interested? I thought you and Shizune didn't like her…"

    show misha cross_frown at centersit
    with charachange

    mi "It's not really like that. You know Shizune and Lilly don't get along well."

    mi "And since you can't really get Hanako away from Lilly, we don't talk to her much."
    
    show misha sign_smile at centersit
    with charachange

    mi "But that doesn't mean that I can't be concerned for her."

    hi "What is there to be concerned about?"
    
    show misha perky_sad at centersit
    with charachange

    mi "Well, she never seems to connect with anyone."

    "If Shizune and Lilly dislike each other because \"their personalities are different\" then I hate to think how Misha and Hanako would get along…"

    show misha perky_confused at centersit
    with charachange
    
    mi "I mean, in one way or the other, we're all in the same boat here, right?"

    #But Misha's different...

    hi "Well, I guess."
    
    show misha sign_smile at centersit
    with charachange

    mi "This one time, when she left class half-way through, Shizune went to the teacher and asked what was going to be done about it."

    show misha sign_confused at centersit
    with charachange
    
    mi "They said that every student here has special needs, and that Shizune shouldn't worry herself about it."
    
    show misha perky_confused at centersit
    with charachange

    mi "She never does any group work; she just runs off."

    mi "Isn't that enough to be concerned about?"

    hi "I guess you're right. She still hardly says a word when we're talking."
    
    show misha perky_sad at centersit
    with charachange

    mi "Well, that's more than I have been able to do. Shicchan and I both tried when she started, but she got scared and ran off."

    "I consider telling Misha that exactly the same thing happened with me, but she seems caught up in thought."

    "Listening to Misha without Shizune's influence is… interesting."
    
    show misha cross_frown at centersit
    with charachange

    mi "I think she needs to realize that people here don't care what she looks like, and that she can trust us."
    
    show misha cross_smile at centersit
    with charachange

    mi "If she could, I'd feel a lot better about her."

    "It strikes me that, without Shizune around, Misha is almost like a different person."

    "Also, I think it's the longest I have seen her without watching her sign."

    "When she's with Shizune, she is constantly waving her hands about, explaining the world to Shizune."

    "That amount of effort probably places a strain on even the brightest mind."

    "And let's face it; Misha isn't the world's brightest spark."

    hi "Well, I'll keep an eye on her for you."

    hi "But you should probably apologize for earlier. I don't think Hanako is cut out for that kind of joke."

    show misha perky_confused at centersit
    with charachange

    mi "Oh? Oh!"
    
    show misha perky_sad at centersit
    with charachange

    mi "I didn't even notice. Sorry."

    hi "Don't say it to me, just mention it to her."
    
    show misha perky_smile at centersit
    with charachange

    mi "Alright. First thing tomorrow, I'll speak to her."
    
    hi "Good."
    
    play sound sfx_doorslam
    with vpunch
        
    "A cacophony from the door heralds the return of Shizune."

    "I guess she can't really tell how much noise she is making."

    show misha hips_grin at centersit
    with charachange

    mi "Oh, Shizune! You're back!"
    
    show shizu invis at Position(xanchor=0.5, xpos=1.0) 
    with None

    show misha hips_grin at twoleftsit
    show shizu behind_blank at tworight 
    show bg school_council at bgleft 
    with dissolvecharamove

    #So tempted to put in a "What took you so long thing to use the epic sprite, but will
    #refrain

    "Shizune appears completely laden with goods from Aura Mart."
    
    show shizu basic_normal2 at tworight 
    with charachange

    shi "…"
    
    show misha sign_smile at twoleftsit
    with charachange

    mi "There was some surplus left from the festival. Since this is officially festival business, I've splurged a little."
    
    show misha hips_grin at twoleftsit
    with charachange

    mi "Nice idea Shizune, ten points."

    hi "Is that really allowed?"
    
    show shizu cross_angry at tworight 
    with charachange

    shi "…"
    
    show misha cross_frown at twoleftsit
    with charachange

    mi "For someone who refuses to join us, you seem to take an unhealthy interest in the politics of this council."
    
    show misha cross_grin at twoleftsit
    show shizu adjust_smug at tworight 
    with charachange

    mi "I shall punish your insolence by rationing your portion of the feast."

    hi "Fine, fine, I get it."
    
    show misha perky_smile at twoleftsit
    show shizu adjust_happy at tworightsit
    with dissolvecharamove

    "Misha slides the multiple stacks of paper to one side to make room for the avalanche of food Shizune is spreading out."

    "As I watch my hard, yet misdirected, work become wasted, I realize that it's little wonder why these two need help."

    "The convenience store meal isn't overly tasty, but at the very least it's filling."
    
    show shizu behind_smile at tworightsit
    with charachange

    shi "…"
    
    show misha sign_smile at twoleftsit
    with charachange

    mi "Thanks for helping today. Most of the time we just make up the reports for the staff."
    
    show misha perky_smile at twoleftsit
    with charachange

    mi "This year we can at least make up some relevant headings on the debrief."

    hi "Are you sure this isn't a corrupt organization?"
    
    show misha hips_grin at twoleftsit
    with charachange

    mi "Not at all, not at all. We're by the book. It's not our fault if the book isn't specific enough."

    hi "I thought that was the definition of corruption…"
    
    show misha hips_smile at twoleftsit
    with charachange

    mi "You think too much!"

    hi "You know what? You're probably right."

    hi "Anyway, I must be off…"

    hi "…that is, if I'm allowed to leave."

    show shizu adjust_smug at tworightsit
    with charachange

    shi "…"
    
    show misha hips_grin at twoleftsit
    with charachange

    mi "Your work has been deemed sufficient. You may leave."

    hi "Well, thank you."

    hi "You know, if you stressed the \"free meal\" side of things over the \"endless workload\" side, you'd probably end up with more recruits."

    stop music fadeout 6.0

    show misha sign_smile at twoleftsit
    with charachange

    show shizu behind_blank at tworightsit
    with charachange

    mi "You might just have a point."

    hi "Well, think about it."

    hi "And think about what we talked about… you don't have to tell that to Shizune if you don't want."
    
    show misha perky_confused at twoleftsit
    with charachange

    mi "What? Oh, right. I'll try to see her tomorrow."
    
    show misha perky_smile at twoleftsit
    with charachange

    mi "G'night, Hisao."

    hi "Night Misha, Shizune."
    
    scene black 
    with dissolve

    return
    
    #-------------
label en_H5_2:
    
    show bg school_scienceroom at bgleft 
    show hanako cover_worry at Position (xanchor=0.5, xpos=0.9)
    show shizu behind_smile_close at Position(xanchor=0.5, xpos=0.5) 
    show misha hips_grin_close at Position(xanchor=0.5, xpos=0.17) 
    with None
    
    hi "Hey, Shizune. I know I said I'd help, but I forgot I'd already made plans. Besides, I helped out more than my fair share last week, didn't I?"

    hi "I promise I'll make it up to you some other time."
    
    show misha sign_confused_close at Position(xanchor=0.5, xpos=0.17) 
    with charachange

    show shizu basic_frown_close at Position(xanchor=0.5, xpos=0.5) 
    with charachange

    show misha perky_smile_close at Position(xanchor=0.5, xpos=0.17) 
    with charachange

    show shizu behind_blank_close at Position(xanchor=0.5, xpos=0.5) 
    with charachange

    "Shizune and Misha release their grip on me and have a long, deep, and silent conversation."
    
    show misha sign_smile_close at Position(xanchor=0.5, xpos=0.17) 
    with charachange

    mi "Well, you have a point there. To be honest, we were only going to spend the rest of the budget on cakes."
    
    show misha cross_laugh_close at Position(xanchor=0.5, xpos=0.17) 
    with charachange

    mi "So, if you're not there, it works out better for us. More cake for us! Wahahaha!"
    
    stop music fadeout 6.0

    show shizu invis at offscreenleft 
    with dissolvecharamove

    show misha invis at offscreenleft 
    with dissolvecharamove

    hide shizu 
    hide misha 
    with None

    "Shizune about-faces and marches out the door, and Misha skips out after her."

    hi "Well, that was a lot easier than I thought it was going to be. Last week those two were like bloodhounds. Or prison guards."

    hi "Or maybe prison guards bred from bloodhounds…"

    "I can't believe I just thought that, let alone saying it out loud. I think I need to move away from Kenji."
    
    hi "…nevermind. Anyway, should we go to the library?"
    
    show hanako basic_smile at Position (xanchor=0.5, xpos=0.9)
    with charachange
        
    ha "S-sure."
    
    play ambient sfx_crowd_indoors fadein 0.5

    scene bg school_hallway3 
    show crowd 
    with locationchange

    "Hanako follows me through the still-crowded halls to the library, using me as a shield."

    stop ambient fadeout 0.5
    play music music_happiness fadein 2.0

    scene bg school_library 
    show hanako invis at offscreenright 
    show yuuko neutral_down
    with locationchange

    show hanako basic_worry at tworight 
    with dissolvecharamove

    "As soon as we are through the door, Hanako makes a bolt for the counter, where Yuuko is stacking books."
    
    show hanako emb_emb at tworight 
    with charachange

    "Before I can catch up, Hanako has whispered something to her."

    show yuuko neurotic_up 
    with charachange

    yu "Um, you'd find that in Non-Fiction, but I don't know where, exactly. If you want I can look it up…"
    
    show hanako emb_downsad at tworight 
    with charachange

    ha "N-nevermind."

    hi "Hey Yuuko, what's all this about?"
    
    show yuuko neutral_down 
    with charachange

    yu "Oh, Hisao… Hanako was just looking for a book on…"
    
    show hanako emb_blushing at tworight 
    with charachange

    ha "N-nothing…"

    hi "A book on nothing? In the Non-Fiction section?"

    show hanako def_strain at tworight 
    with charachange

    ha "I… I was just…"
    
    show yuuko neurotic_up 
    with charachange

    "I shoot a glance at Yuuko. She looks like she's about to burst from the pressure of keeping Hanako's secret request."

    hi "Yuuko, what did…"

    show yuuko happy_down 
    with charachange

    yu "Chess! She's looking for a chess book!"

    "I make a mental note to never entrust Yuuko with any important information."
    
    show hanako defarms_shock at tworight 
    with charachange

    ha "Y-Yuuko…"
    
    show yuuko panic_up 
    with charachange

    yu "I'm sorry Hanako… It just slipped out…"

    hi "Well, it's not a secret anymore. Come on, I'll give you a hand. I should really brush up on my skills, too."
    
    show hanako def_worry at tworight 
    with charachange

    ha "O...okay."

    hide yuuko 
    with charaexit

    show hanako def_worry
    show bg school_library at bgleft 
    with charamove

    "Yuuko disappears behind the counter in shame as Hanako and I wander into the depths of the Non Fiction section."

    "I know there is supposed to be a system for categorising these books, but I don't see how anyone can decipher it without spending half of their life researching it."

    "That's probably why all the librarians I know are neurotic."

    #Dewey Decimal for Chess is 794.1, between magic tricks and educational games.

    "Towards the end of the aisle, between a book on card tricks and some book on kid's games, stands a single book bearing the title \"Chess tactics for Champions\"."

    show hanako basic_bashful 
    with charachange
    
    "Before I can reach for it, Hanako has the book in her hands, clutching it to her chest."

    hi "Well, I guess that's yours then. Mind if I borrow it when you're finished?"

    show hanako cover_worry
    with charachange

    ha "S-sure. I… I just haven't played against anyone before, so I thought…"

    "Damn. It's not like I was trying to beat Hanako deliberately or anything, but she seems to have taken it to heart."

    "Then again, at least this means she wants to play me again. That's a plus, right?"

    hi "Ha, well it's not like I'm a master or anything. I played a bit before…"

    "It occurs to me that I haven't told Hanako about my condition. I falter for a second, deciding to cover my tracks. This is a conversation for another day."

    hi "…before I came here."

    "I don't want to tell Hanako that the only real time I played was when I was lying in a hospital bed, against some of the other kids in the children's ward."

    "They weren't exactly good competition either; the next oldest child was barely 15."

    stop music fadeout 6.0

    show hanako cover_distant 
    with charachange

    #To be replaced with "concern" if it gets made.

    ha "Are… are you alright?"

    hi "Yeah, I was just remembering something…"

    "When I think about it, I shouldn't be afraid to tell Hanako about being in hospital. Judging by her scars, she probably spent a fair amount of time in a hospital bed."

    "But, for some reason, I can't bring it up. At least not today, and not on short notice."

    "Eager to break off the conversation, I grab a random book from the shelf."

    #791.068 – Amusement parks

    "It's some book on the world's fastest roller coasters…"

    "…published in 1982. Well, not entirely accurate, but it should at least be interesting."

    hi "Well, we've both got books now, should we go sit down?"

    show hanako cover_bashful
    with charachange

    "Hanako seems to accept my bluff, and we head to the reading nook at the back of the library."
    
    hide hanako 
    with charaexit

    "Neither of us says a word; we simply open our books and start reading."

    "I try to read my book, but it would seem that in 1982 roller coasters weren't nearly as large as the ones built in the decades since."

    "Most of the ones listed are made of wood. Something about that doesn't seem safe to me."

    "If I'm going to ride on something potentially dangerous, I want it to be made out of steel, or some kind of space-age alloy that has big words like \"titanium\" and \"Ruthenium\"."

    "I quickly lose interest, and my eyes wander across the reading area to rest on Hanako."
    
    show ev hana_library_read
    with locationskip

    "Hanako seems absorbed in her book, flicking back and forth through the pages, as if confirming what she just read. I wonder how effective that is, or if she's just overloading herself."

    "She unconsciously brushes her hair from her face, temporarily revealing her scar tissue."

    "I'm still not sure about the protocol here. Is it right to ask her about her scars? Or her past? How long was she in hospital? Does she still visit the doctor?"

    "These all seem like the questions that you'd ask someone who just transferred to your school, translated into the local language."

    "But, to date, no-one has directly asked me any of them. Well, except Rin, but I don't think I should use her as a guide to proper social behaviour."

    "For the time being, I'll just keep my mouth shut. If someone wants you to know something, then they'll tell you. Trying to force the issue might drive Hanako back into herself."

    scene bg school_library_ss 
    show yuuko worried_up_ss at center 
    with shorttimeskip

    yu "Um… sorry to interrupt, but I have to close the library now."
    
    play music music_tranquil fadein 3.0

    hi "Already?"

    "I check my watch. Somehow, as I was lost in thought, nearly two hours have passed."
    
    show yuuko smile_down_ss 
    with charachange

    yu "Do you want to check out those books? I can do it on the way out…"
    
    show hanako invis at Position(xpos=0.9, xanchor=0.5, ypos=1.17, yanchor=1.0)
    with None

    show hanako basic_worry_ss at Position (xpos=0.7)
    show bg school_library_ss at bgleft 
    show yuuko smile_down_ss at twoleft 
    with dissolvecharamove

    ha "P-please."

    hi "I'm alright. I'll drop this one back on the way through. It wasn't as interesting as I first thought."
    
    show hanako emb_timid_ss at tworight 
    with dissolvecharamove
        
    "Hanako marks her place with a slip of paper and stands up. The girls head to the counter and I return my book to what I think is the right shelf."

    show yuuko neurotic_up_ss at twoleft 
    with charachange
    
    "Yuuko scans Hanako's book with practiced precision, yet still manages to fumble it."
    
    show yuuko neutral_down_ss at twoleft 
    with charachange

    yu "Oh… there we go. Third time lucky. Since this is a non-fiction book, you can only have it for a week."

    show hanako basic_smile_ss at tworight
    with charachange

    ha "T-that's okay."
    
    scene bg school_hallway2 
    with locationchange

    "Yuuko shuts down the library's computer and herds us out the door."

    show yuuko panic_up at twoleft 
    show hanako def_worry at tworight 
    with charaenter

    yu "Argh! I didn't think it was this late already…!"

    hi "But you're the one that told us you had to close…"
    
    show yuuko worried_up at twoleft
    with charachange

    yu "Yes but, I know but, that was before I looked at the time!"
    
    show yuuko neurotic_up at twoleft
    with charachange

    yu "I'll see you later."

    hide yuuko 
    with easeoutleft

    "Yuuko bolts down the hall, her handbag trailing behind her like an awkward streamer."
    
    show hanako def_worry
    show bg school_hallway2 at bgleft 
    with dissolvecharamove

    hi "I guess all librarians really are neurotic."
    
    show hanako emb_timid 
    with charachange

    ha "Huh?"

    hi "Ah, never mind. I was just thinking that I've never met a librarian that can organise their time, no matter how good they are with their books."

    show hanako basic_smile
    with charachange

    ha "Oh… heh… I k-know what you mean…"

    #Geh I need to know how to verbalise a short laugh without using "heh"

    "What? Did Hanako just laugh? It wasn't meant to be a joke, but I must have reminded her of some other librarian… or something…"
    
    show hanako cover_worry 
    with charachange

    ha "I… I have to get back."

    hi "Yeah, me too. I didn't realise it was this late. Thanks for letting me hang out with you."
    
    show hanako basic_bashful 
    with charachange

    ha "N-no problem."

    hi "Say, how about I walk you back to the dorms? The girl's dorm is on the way, anyway."

    show hanako emb_blushing
    with charachange

    ha "O-okay."
    
    hide hanako 
    with charaexit

    "Hanako sets of ahead of me, and I need to jog a little to reach her side."

    scene bg school_dormext_full_ss 
    with locationchange

    show hanako def_worry_ss 
    with charaenter
    
    stop music fadeout 6.0

    "We walk through the gardens, eventually arriving in front of the dorm buildings."

    hi "Here you go. See you in class tomorrow?"
    
    show hanako emb_smile_ss 
    with charachange

    ha "S-sure."

    hide hanako 
    with charaexit

    "Hanako waves a short goodbye before pushing her way through the dorm's doors."
    
    scene black 
    with dissolve

    return


#-------------------------------

label en_H6:
    
    scene bg school_dormhisao 
    with openeye

    "Chirping birds."

    "Normally, this will be a good time to reflect upon the beauties of nature."

    "But it is 6 am."
    
    play sound sfx_pillow

    scene black 
    with Dissolve(0.2)

    "Covering my head with my pillow, I slam my face into the mattress, hoping that the impact will send me instantly back to sleep."

    "Futile."

    "I toss and turn, but sleep simply won't return to me."
    
    play music music_daily fadein 10.0

    scene bg school_dormhisao 
    with locationchange

    "Alright nature, you've won. See? I'm getting up now…"

    "The lack of sleep weighs my mind down, and there's only one remedy for this; a nice, hearty breakfast."

    $ renpy.music.set_volume(0.29999999999999999, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 0.5

    scene bg school_cafeteria 
    with locationchange

    "It would be nice to be the first person here."

    "To be the first to dig into a piping hot pile of food, to sit wherever I desire…"

    "It would have been nice."

    "But even my exceptionally early start has put me behind the most diligent students."

    "I guess there are quite a few people that have early starts here, for one reason or another."

    "A group of students in sports clothes huddle around one table, eagerly discussing game plans between inhaling great gulps of food."

    "Scattered around the hall are a number of bleary-eyed students, probably suffering from the same ailment as myself - noisy birds."

    "And, of course, the there are people that actually enjoy getting up this early, the ones with their bags stuffed with textbooks and completed homework."

    "It's hard to not want to despise people like that, even more so when you're tired yourself."

    "Picking out a familiar face from the thin crowd, I head towards the nearest table."

    "Lilly sits alone, delicately feeling her way around a small plate of eggs."

    "It's almost a shame to interrupt her and her clockwork movements."

    "I wonder, is this how a blind person zones out? Simply moving in pre-determined patterns learned over the years, just like how a sighted person would eat whilst reading a newspaper."

    hi "Good morning, Lilly. I didn't expect you to be here this early."

    show lilly basic_surprised at centersit
    with charaenter

    li "Oh, Hisao, you startled me. I didn't know you took breakfast this early…"

    hi "I don't. This is an exception to the rule. I'd much prefer to be late to school than early to breakfast."

    show lilly basic_weaksmile at centersit
    with charachange

    li "Ah. Well, \"A change is as good as a holiday\", or so they say."

    hi "\"They\" say a lot of things…"
    
    show lilly basic_ara at centersit
    with charachange

    li "That is also true."

    "My mind isn't cut out for conversation at this hour. I need sustenance or else my mind will shut down totally."

    "Commence shoveling."
    
    show lilly basic_weaksmile at centersit
    with charachange

    "Lilly continues playing out her mechanical-action eating process."

    "Each short motion lacks energy. I suppose this is similar to letting your eyes wander whilst performing any ordinary chore."

    "But after a few repetitions of the find-food-then-eat it-cycle, Lilly puts down her fork and dabs her lips with a napkin."
    
    #maybe spelling things out a little too much here.
    #also might be a little too perceptive for dipshit Hisao
    # It's okay.

    stop music fadeout 6.0
    stop ambient fadeout 6.0

    show lilly basic_concerned at centersit
    with charachange

    li "Hisao, do you mind if I ask you a question?"

    "Damn. All I want is a little food and about four hours of sleep. And nobody says \"can I ask you a question\" for a simple question."

    hi "Sure."
    
    show lilly basic_listen at centersit
    with charachange

    li "Do you think of Hanako as a friend?"

    "Huh, this seems like a leading question."

    hi "I… guess so. Why do you ask?"
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "No real reason."
    
    show lilly basic_displeased at centersit
    with charachange

    play music music_serene fadein 8.0

    li "Why?"

    li "I mean, why do you think of her as a friend?"

    "This is well above my level. What is she expecting from me?"

    hi "I'm not really sure. I guess it's because she's a little different in the way she deals with people…"
    
    show lilly basic_reminisce at centersit
    with charachange

    li "Hmm. Since I've known her, she hasn't really connected with anyone."
    
    show lilly basic_concerned at centersit
    with charachange

    li "She doesn't seem interested in other people, and I think people are a little scared off by her appearance."

    hi "Really? I thought that kind of thing was, well, discouraged here. Discriminating and such."

    show lilly basic_listen at centersit
    with charachange

    li "Hmm, if I were to put it one way..."

    "She furrows her brow in thought, a move which makes me slightly anxious as to what she's plucking from her mind."
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "I'd say that you're a little naive."

    "Naive? I'd be insulted if not for the slight grin on her face."

    hi "I... see."
    
    show lilly basic_reminisce at centersit
    with charachange

    li "While Yamaku has a stronger sense of community compared to other schools, it's far from being free of conflict."

    "That's something I've noticed, actually."

    "People avoiding each other in the hallways and such."
    
    "The deaf and blind acting almost like rival gangs without ever exchanging a word."

    "Even Lilly and Shizune could be considered bitter rivals, even though they both seem like fairly accepting people."

    "Well, at least the Misha-tinted Shizune does. Who knows what actually goes on behind her glasses?"
    
    hi "I guess you're right. But when I first came here, everything was a bit of a shock. I kept on making mistakes, or at least thinking I was making a mistake. Like when I said \"See you later\" to you."

    hi "I didn't know if that was considered rude or anything, so I tried to just put it in the back of my mind. Treating people any differently and that kinda thing."

    hi "So I didn't. I told myself that Hanako and yourself and everyone else was just normal, and I tried to ignore the obvious."
    
    hi "I talked to Hanako as if she were any other person, and so we became friends." 
    
    hi "At least, that's how I think it happened."

    show lilly basic_smileclosed at centersit
    with charachange

    li "Hisao, I think you are naive, but I also think that you are a good person. It's perhaps one of your better sides."

    hi "Um, thanks."
    
    show lilly basic_smile at centersit
    with charachange

    li "Are you free tonight?"

    hi "If you don't count homework, then I'm as free as the breeze."
    
    show lilly basic_cheerful at centersit
    with charachange

    li "In that case, would you care to join myself and Hanako for tea?"

    hi "Er, I don't really have that much money at the moment, so going out isn't really…"
    
    show lilly basic_smile at centersit
    with charachange

    li "Oh, I didn't mean going out. Just here, this evening."

    hi "You can access the classrooms in the evening here?"

    show lilly basic_giggle at centersit
    with charachange

    li "No, that's not allowed. But I do have a small setup in my room that we can use. Please feel free to drop by after dusk."

    hi "Er, sure."

    hi "What's your room number?"
    
    show lilly basic_smileclosed at centersit
    with charachange
    
    li "214, it's on the second floor."

    hi "Okay, sure."
    
    show lilly basic_cheerful at center 
    with dissolvecharamove

    li "Well then, I had best be off. I have morning duties to attend to. Until this evening, Hisao."

    hi "Yeah, catch you later."
    
    hide lilly 
    with charaexit

    stop music fadeout 8.0

    "What just happened?"

    "Was I just invited to a girl's room after dark?"

    "Is that even allowed?"

    "There is the curfew here, but I've never heard any rules about visitors in the dorm rooms."

    "Even still, this is enough to get my sleep-deprived brain jump-started."

    "Add that to a lukewarm breakfast and you have one hell of a pick-me-up."

    "Now, to go through the routine and make it through classes…"
    
    return
    
#---------------------------------    

label en_H7:
    
    scene bg school_girlsdormhall 
    play sound sfx_time
    with shorttimeskipsilent
    
    with Pause(0.3)

    play sound sfx_doorknock2

    "I nervously rap on the door marked 214, checking my watch once again."

    li "Is that you, Hisao? I'll be with you in just a moment."

    "Lilly's voice lilts through the door and soothes my nerves."

    "This is the first time I've been invited to a girl's room after dark."

    "Even though I know there is no ulterior motive behind this invitation, it doesn't stop my mind running wild with possibilities."

    "One guy. Two girls. In a dorm room. With a tea set."

    "When I put it like that it sounds a little dodgy."

    "Before I can continue this train of thought the door makes a clicking sound and opens a crack."

    li "Please, do come in."

    play sound sfx_dooropen

    window hide

    scene white 
    with dissolve

    with Pause(0.1)

    play music music_one fadein 10.0

    scene ev lilly_bedroom at Zoom((800,600),(40, 30, 720, 540),(0, 0, 800, 600),15.0, time_warp=_ease_time_warp, xalign=0.5, yalign=0.5)
    with Dissolve(4.0)

    window show

    "The door opens completely and I catch glimpse of Lilly's room."

    "Her furniture looks almost antique, but the bare walls and flat surfaces are barely decorated at all. In the center of the room sits a small table."

    "It seems that everything in this room has its place."

    "My eyes finish their quick sweep of the room, before returning their position onto the girls."
    
    scene ev lilly_bedroom_large at Move((-130,-400),(-130,-600), 3.0, time_warp=acdc_warp, subpixel=True)
    with flash

    "To my immediate front, Lilly sits next to the small table, wearing very dark blue pajamas."
    
    show ev lilly_bedroom_large at Move((-130,-600),(-830,-300), 1.0, time_warp=_ease_time_warp, subpixel=True)
    with None
    
    with Pause(1.0)
    
    show ev lilly_bedroom_large at Move((-830,-300),(-830,0), 10.0, time_warp=acdc_warp, subpixel=True)
    with None

    "Behind her, Hanako is kneeling beside a low table and adorned in light pink gown."

    "Her hands are firmly fixed between her legs, her shoulders forward, and her head down, as if trying to hide herself in her gown."

    "It would be easy for her to do; it looks about two sizes too big for her."

    "Folds of flannel flow from her frame, making her look like a child playing dress-up in their parent's clothes."

    "She looks up to confirm my identity, and a thin smile creeps across her face."
    
    show ev lilly_bedroom_large at Move((-830,0),(-130,-400), 1.0, time_warp=_ease_time_warp, subpixel=True)
    with None

    li "A little lost for words, are we?"

    "I guess it doesn't take a sense of sight to realize when someone is gawking."

    hi "Um, no, I… you both look nice."

    "Hanako blushes and looks away, but her smile stays."

    li "Well now, there's no point in you standing in the doorway. Please, take a seat."
    
    scene bg school_dormlilly 
    show lilly basic_smile_paj at twoleftsit
    show hanagown distant at tworightsit
    with locationchange

    play sound sfx_doorclose
    stop music fadeout 10.0

    "I take a step into the room, closing the door behind me."

    "As she turns back toward the room, she bumps into me and grasps my arm."

    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Oh, I'm sorry. This really is a small room with the three of us. Would you like to take a seat?"

    "I slowly walk to the table and sit down, trying my hardest not to disturb anything along the way."

    "I also can't help but steal a quick glance into Lilly's top as I sit."

    "To be robbed of sight would be a most terrible fate."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    li "Well now, how about some tea. Hanako, could you please pour?"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "S…sure. His…sao… Would…"
    
    show hanagown distant_blush at tworightsit
    with charachange

    ha "…would you…"

    show hanagown worry_blush at tworightsit
    with charachange

    ha "…would you like…"

    hi "I would love some tea. Do you need a hand?"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "N… no I'm fine…"
    
    show hanagown smile at tworightsit
    with charachange

    ha "Thank you…"

    play music music_dreamy fadein 2.0

    show lilly basic_giggle_paj at twoleftsit
    with charachange

    li "It's not like you to be nervous here Hanako… or is our guest making you uncomfortable?"
    
    show hanagown distant at tworightsit
    with charachange

    ha "N…no. It's just… just…"

    hi "It's just been a tiring day?"
    
    show hanagown smile at tworightsit
    with charachange

    ha "Y..yeah."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    "I take up my position at the table, with my back to the door."

    "To my left is the blue-clad Lilly and to my right sits the pink Hanako."
    
    show teaset alpha at Position(xalign=0.5, yanchor=0.5, ypos=0.6)
    with None
    
    show teaset at Position(xalign=0.5, yanchor=0.5, ypos=0.5)
    with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

    "The tea set on the table looks cute as well as practical; painted red with a floral motif."

    "It looks odd when contrasted with Lilly's plain but generally sophisticated-looking furniture, which leads me to think that Hanako might have picked it out."

    "There is a slight 'ting' as Hanako accidentally clips the teapot on a cup as she is pouring."
    
    show hanagown worry at tworightsit
    show lilly basic_displeased_paj at twoleftsit
    with None
    
    show teaset alpha at Position(xalign=0.5, yanchor=0.5, ypos=0.6)
    with Dissolvemove(0.5, time_warp=_ease_out_time_warp)
    
    hide teaset
    with None

    "She breathes in sharply; she must be really nervous, as it's not the kind of thing anyone would worry about."

    show hanagown worry_blush at tworightsit
    with charachange
    
    "Hanako quivers at her mistake."

    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "There is really no need to be nervous…"

    show hanagown normal at tworightsit
    with charachange

    "Hanako seems to find some confidence in Lilly's words and deftly pours the next two cups."
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "Here you are, Hisao… Lilly."

    "Hanako gently places a cup and saucer in front of Lilly and myself."

    "I could get used to service like this."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Thank you, Hanako."

    hi "Yeah, thanks."
    
    show hanagown smile at tworightsit
    with charachange

    ha "Y-you're welcome."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    "Lilly searches for her cup, and upon finding it, sips gently."

    "I do the same. This tea tastes somewhat better than the tea we usually have in the school."

    hi "This is nice, it's like it's not even tea at all…"
    
    show lilly basic_ara_paj at twoleftsit
    show hanagown normal_blush at tworightsit
    with charachange

    li "Looks like you picked the right one, Hanako."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    li "You've done well, even if it was a bold move."

    hi "Yeah… it's… awesome. I've never had tea like this before…"

    show hanagown smile at tworightsit
    with charachange

    "Hanako's smile returns, redoubled."

    "Even with her blighted face, her shy smile couldn't be called anything but \"cute\"."
    
    show hanagown distant_blush at tworightsit
    with charachange

    ha "I'm glad you like it…"

    "Hanako, finally beginning to relax, sips from her cup."

#--------------------
label en_H7a:
    
    "I think back to my chat with Misha the other day."

    "Is Hanako's behavior something to be concerned about, or is she just shy?"

    "And then there was Lilly earlier this morning."

    "The concern from both of them seemed to be genuine, and they know the situation better than I."

    "But, really, how could I possibly help?"

    "I'm no plastic surgeon, so I can't really help her appearance. Nor am I a psychologist that can make her more sociable."

    "So what the hell do Lilly and Misha want me to do?"

    "It's frustrating. Hanako and I are quickly becoming friends of our own accord, and because of that, it's like everyone wants me to solve all her problems."

    "And I have no idea how to do that."

    "No-one can cure my heart, nor Lilly's eyes, nor Misha's…"

    "…whatever is wrong with Misha."

    "However, I see no harm in becoming better friends with Hanako. Now that she's warming up to me I kind of enjoy hanging out with her."

#------------------------    

label en_H7b:
    
    "Something about this makes me think about Lilly's question at breakfast."

    "Why am I friends with Hanako?"

    "Lilly seems genuinely concerned for Hanako's well being, but it's not like I can do anything to help her."

    "As far as I can tell, her scars don't hold her back physically, and everyone I've met seems to have overcome their disabilities to some extent."

    "I don't have any ulterior motives to hang out with Hanako, we just share similar interests."

    "Isn't that enough?"



#-----------------

label en_H7c:
    
    show lilly basic_smile_paj at twoleftsit
    with charachange
    
    li "So, Hisao, are you enjoying this experience?"

    "Lilly's words break me out of my reverie, and I take a second to reconsider where I am."

    "I'm in a room with two girls in their bedclothes. This is something to be enjoyed."

    hi "Yes, it's relaxing. Almost like I'm not in the school anymore. Do you do this often?"
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Quite often, but not as often as we take tea in the school building."

    li "If you do something like this every day, it stops being a treat and starts to become a chore."

    hi "I suppose you have a point there, but I think it would take some time for me to think of this as a chore."

    "I'm estimating around forty years for that to happen."

    "All too soon, I find my cup empty."

    hi "That was delicious. Thank you Hanako, Lilly."
    
    show hanagown smile at tworightsit
    with charachange

    ha "You're welcome."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Yes, you are most welcome, Hisao."

    li "It's nice to have a third person here."

    hi "Well, any time you need someone to fill that position, I'm always available."

    hi "Always."

    "One must be sure to get your point across in these circumstances."

    stop music fadeout 8.0
    show lilly basic_sleepy_paj at twoleftsit
    with charachange

    "Lilly lets loose a yawn, which she unsuccessfully hides with her hand."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Oh, excuse me, I think I'm a little tired."
    
    show hanagown distant at tworightsit
    with charachange

    ha "I think we're all a little tired…"
    
    show lilly basic_ara_paj at twoleftsit
    with charachange

    li "My my, how astute we are tonight, Hanako."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "We really should head to bed, we all have class tomorrow."

    hi "Yeah… I should go."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange
    
    li "Thank you for your presence, Hisao."
    
    show hanagown normal at tworightsit
    with charachange
        
    ha "Th..thanks. You'll come again?"
           
    hi "Not even a whole army could stop me."

    show lilly basic_cheerful_paj at twoleftsit
    with charachange

    li "That's some determination there, Hisao."

    hi "Well, you know what I mean. But I think I really should get going; it's getting late."

    ha "Yeah, it's getting late."

    "I stand up, and make for the door."
    
    show hanagown normal at tworight 
    with dissolvecharamove

    "Hanako gingerly stands up behind me."

    "I stop and face her."

    hi "Are you coming with me?"
    
    play music music_comedy fadein 0.5

    show hanagown normal_blush at tworight
    with charachange

    "Hanako instantly blossoms into full blush."
    
    show hanagown distant_blush at tworight
    with charachange

    ha "No… I… not… this room… isn't…."

    hi "It's okay, I was only joking."
    
    show hanagown smile at tworight
    with charachange

    ha "Oh… okay… goodnight…"
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    li "Goodnight, Hanako, Hisao."

    hi "Night all."

    "And with that, our tea party finishes."

    scene bg school_girlsdormhall 
    with locationchange

    "I'm still not sure what it is that Lilly wants me to do for Hanako, but I don't want to let her down."

    "I wait until the door has closed behind us before turning to Hanako."
    
    show hanagown distant_blush 
    with charaenter

    hi "Hey, Hanako, you know, you don't have to be nervous around me or anything."

    hi "I mean, we're friends, right?"

    show hanagown normal_blush 
    with charachange

    ha "R-right. We're… friends."

    hi "If you ever want to hang out or anything, just let me know. We still need to have that chess rematch, remember?"
    
    show hanagown distant 
    with charachange

    ha "S-sure…"
    
    show hanagown normal 
    with charachange

    ha "B-but I don't think you'll win…"

    hi "It wouldn't be any fun if it was easy."
    
    show hanagown smile 
    with charachange

    "Hanako seems to give a muted laugh, but she could have just as easily been exhaling."

    ha "G-good night Hisao…"
    
    show hanagown smile at tworight 
    with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

    hide hanagown
    with Dissolve(0.2)

    stop music fadeout 5.0

    "With that, Hanako quickly retreats into her room, located next to Lilly's."

    "I start to walk back to my dorm, but the simple act of walking seems to drain me of my energy."
    
    scene bg school_dormhisao 
    with locationskip

    "I barely make it to my room before I am hit by a wave of exhaustion."
    
    play sound sfx_switch

    scene bg school_dormhisao_ni 
    with Dissolve(0.2)

    "I kick off my shoes and fall into bed and fall asleep by the time my head hits the pillow."
    
    scene black 
    with dissolve

    return


#-----------------
label en_H8:
    
    scene bg school_dormhallway 
    with locationchange

    "I pull my door closed, ready for another day of classes."
    
    show kenji invis at twoleft 
    with None

    show kenji neutral_close at center 
    with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

    ke "Sleep well?"

    play music music_kenji fadein 0.5

    "Kenji's sudden arrival makes me jump, and I narrowly avoid butting heads with him."

    "I know he has poor eyesight, but he knows who I am now. Does he still have to stand this close?"
    
    show kenji neutral 
    with charadistant

    hi "Oh. Yeah. Like a baby."

    show kenji tsun
    with charachange

    ke "Damn, why do people say that? Have you ever heard a baby sleep?"

    ke "They scream. All night. Every night. Babies don't sleep well, ever."

    "Well, there goes my restful state. I have to remember to never use figures of speech with Kenji."

    hi "Alright, I get your point. It was a figure of speech."

    show kenji neutral
    with charachange

    ke "Yeah, sure, whatever. Where were you last night? I had a favor to ask but you weren't around."

    "For a split second I consider telling Kenji the truth; that I was spending time with Hanako and Lilly."

    "Thankfully, that split second passes as soon as it came."

    hi "I was just out. Checking out the local area and stuff. You know, recon."

    show kenji happy
    with charachange

    ke "Good man, good. I knew you were the type to plan ahead…"

    hi "Anyway, what was this favor you wanted?"
    
    show kenji neutral 
    with charachange

    ke "I was going to get some take-out, but I needed change."

    hi "Wait, what? I gave you money last week and you still haven't paid me back!"

    show kenji tsun
    with charachange

    ke "Tch, and I was starting to think you were cool."

    "Kenji fishes around in his pocket and produces his wallet."

    "As he counts out the 420 yen he owes me, I can clearly see at least two 10,000 yen notes."

    hi "Hey, what the hell? Why are you borrowing money off me when you've got that much cash?"

    "Kenji hisses a little, realising that he's been had."

    ke "Get off my case, man. It's bad luck to break a big note for anything less than half its value. It's the tycoon's rule."

    ke "Last night's dinner is going to cost me seven years of bad luck. Seven years!"
    
    show kenji happy 
    with charachange

    ke "Don't you think that's enough cause to help someone out?"

    ke "You'd get a shorter sentence if you just stole the stuff."

    "My common sense screams at me to say something to him, but thankfully I restrain myself."

    "Arguing a point like this with Kenji will just lead to further and more complicated discussions."

    hi "Yeah, I guess you're right. Maybe you should plan these things a little better?"
    
    show kenji neutral
    with charachange

    ke "Yeah man, I know. But I've just got so much stuff to do, it's hard. And you're never around anymore so I'm on my own."

    ke "We're supposed to be brothers in brotherhood, remember?"

    hi "Yeah yeah, I get you. Global conspiracy and such. I'll keep my ear to the ground."
    
    show kenji neutral_close 
    with charachange

    "Kenji draws close enough for me to get a clear whiff of his garlic-tainted breath."
    
    show kenji tsun_close 
    with charachange

    ke "You'd better man. Already you're spending less time here. That's the first thing they do."

    ke "They'll try to split us up. Divide and conquer. Sun Tzu said that."

    hi "Roger that. Now, I've got to be going. I've got classes. You coming?"
    
    show kenji neutral_close 
    with charachange

    ke "Nah, I'm tired. I stayed up all night just to make sure nothing was going to happen after splitting that note."

    hi "As rational as ever, I see."
    
    show kenji tsun_close 
    with charachange

    ke "Whatever. Night."

    stop music fadeout 3.0

    show kenji invis at twoleft 
    with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

    "Kenji scurries back into his room, and I hear him throwing his locks as I walk down the hallway."
    
    return
    #--------------
    
label en_H9:
    
    scene bg school_dormhallway 
    with None

    scene bg school_scienceroom 
    show muto smile at center 
    with shorttimeskip

    play music music_daily fadein 4.0

    mu "And that is why some people can't roll their tongue, or why their second toe is longer than their big toe."

    "Mutou beams a half-moon smile at us, obviously proud of his explanation of recessive genes."

    "However, no matter how impressed he is at the molecules that define who we are, the classroom seems to be reduced to a stupor."

    "Why is it that a bad explanation can make even the most interesting thing seem worthless?"

    show muto irritated 
    with charachange

    "I can see Mutou deflate as he realizes that nothing he's said in the past half hour has sunk in."
    
    $ renpy.music.set_volume(0.29999999999999999, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 4.0

    "Whispered conversations start to break the silence, and like an avalanche, the noise level in the class starts to rise."
    
    show muto normal 
    with charachange

    "Defeated, Mutou identifies some questions from the text book and sets to clearing off the blackboard."

    hide muto 
    with charaexit

    "Almost as if expected, Hanako packs up her things and leaves as soon as people start talking and laughing amongst themselves."

    "The initial shock of seeing someone go truant so blatantly has started to fade, but it doesn't stop me from wondering."

    "Is she leaving because she doesn't want people to speak to her? Or is it just the thought of people around her shattering her peace?"
    
    play sound sfx_normalbell
    $ renpy.music.set_volume(1.0, 4.0, channel='ambient')

    "Before I can think about the topic any further, the lunch bells ring. I wonder if she was simply taking the opportunity to leave early."

    "The usual clamor of students exchanging books for lunch reverberates around the room, and while Misha is distracted I grab my lunch and head out the door."

    stop ambient fadeout 1.0

    scene bg school_miyagi 
    show lilly basic_smileclosed at centersit
    with locationskip
    
    "Lilly already sits in the tearoom, setting out her lunch alone."

    hi "So, Hanako's not here then?"
    
    show lilly basic_smile at centersit
    with charachange

    li "Oh, Hisao, how are you? No, I haven't seen Hanako since this morning."

    "That's right, Hanako and Lilly live next to each other."

    "Somehow I think their morning conversations are slightly more realistic than Kenji's ramblings."

    hi "That's strange. She left class early, so I figured that she'd come here."

    show lilly basic_displeased at centersit
    with charachange

    li "Oh, is she still doing that? Leaving class early?"

    hi "Huh? Yeah, I've seen her do it a few times."
    
    show lilly basic_sad at centersit
    with charachange

    stop music fadeout 7.0

    "Lilly drops her head a little, like someone who is used to hearing bad news."

    li "I was sure that she'd stop doing that now that you two are becoming friends."
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "I suppose these things take time."

    hi "Well, I was wondering about that today. Why exactly does she leave?"

    show lilly basic_reminisce at centersit
    with charachange

    li "I'm not entirely sure myself. I personally think it's because she doesn't want to be put in a situation where she has to answer someone."

    "I have a flashback of my first meeting with her, when I thought she looked like a cornered animal. Maybe I wasn't far from the truth."

    hi "But she seems fine with talking to you, and with me a bit…"
    
    show lilly basic_displeased at centersit
    with charachange

    li "Well, it's a little more complex than that. I imagine that the first thing most people ask her about is her scars, and what happened."

    li "She rarely talks about it with me, but I can tell that she doesn't like to remember that incident."
    
    show lilly basic_reminisce at centersit
    with charachange

    li "So leaving class and running away from discussions is her pre-emptive strike, if you will."
    
    hi "Huh… so then how does that explain her talking to me?"
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "You said it yourself yesterday at breakfast; you tried to ignore her scars. Once she saw that you weren't going to ask her about that, she opened herself up to you."

    li "I think she wants friends more than anything else, but her fear of the past is holding her back."

    hi "Hrm, I guess you're right. Maybe. I dunno. You know her better so I'll take your word for it."
    
    play music music_normal fadein 3.0

    show lilly basic_giggle at centersit
    with charachange

    li "I wouldn't worry about that. I'm sure you'll come to know her as well as I do soon enough."
    
    show lilly basic_smileclosed at centersit
    with charachange

    li "I've known her long enough to realize that she is excited at the prospect of a new friend. And the two of you have such similar interests…"

    hi "Well, I hardly count reading as a team sport, but it's good to have company."
    
    show lilly basic_smile at centersit
    with charachange

    li "That's my point. Hanako is still a person. She also wants company at times like that."

    hi "Huh, I see. I think. To be honest both of you still confuse me a little."
    
    show lilly basic_smileclosed at centersit
    with charachange

    li "That's only natural, Hisao. We've only known each other for a few days; it's unreasonable to expect you to understand us, just as we can't understand you."

    show lilly basic_weaksmile at centersit
    with charachange
    
    li "But that is half the fun of becoming friends, right?"

    hi "Yes, yes it is."

    show lilly basic_cheerful at centersit
    with charachange

    li "I hope you don't mind, but I'm going to start eating."

    hi "No, go ahead, I think I'll eat something too. I've got some books I want to drop back at the library before classes start so I'd better get a move on."

    show lilly basic_smileclosed at centersit
    with charachange
    
    li "You'll probably find Hanako there as well. If you do see her, can you tell her to stop by my room later tonight? I'd like to talk to her."

    hi "So, you're not coming?"
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "Unfortunately I have a class representative's meeting later, so I'll be gone as soon as I've finished my lunch."

    hi "Okay then, if I don't see her in the library then I'll tell her in class. I'm sure she'll be back after lunch."

    "We fall silent as we start to eat, and I take a second to reflect on our conversation."

    "I've always thought that Hanako's shyness was simply due to her being self conscious of her scars."

    "But that is a pretty superficial way of looking at her."

    "Just when I thought I was able to see through the fog of Lilly and Hanako, I realize that I'm more lost than when I started."

    "Lilly quickly finishes her lunch, acutely aware of her meeting. I don't blame her."

    "Shizune is most likely going to be there, and I doubt she wants to give her the satisfaction of another argument."
    
    show lilly basic_smile at centersit
    with charachange

    li "I must be off. Same time tomorrow?"

    hi "Same time, same channel. I'd better head off too; I don't want to risk being late."
    
    show lilly cane_smileclosed at centersit
    with charachange

    show lilly cane_smileclosed at center 
    with charamove

    stop music fadeout 4.0

    "Lilly smiles gently, picks up her cane and walks into the hall."

    return

    #----------
    
label en_H10:

    scene bg school_hallway2 
    with locationchange

    "I turn my back on Lilly as we head in opposite directions. For some reason I find myself hoping she doesn't get in another fight with Shizune."

    "As much as I like Lilly, Shizune and Misha have been pretty helpful in helping me adjust, even if half of our conversations are thinly-veiled recruitment attempts."

    "Then again, I barely know either of them. Maybe they were previously leaders of some kind of secret society, but their love for each other drove them apart…"

    "Man, I need to stop reading cheap fiction. It's rotting my brain. Either that or I've got to move away from Kenji and his bad influence."

    "It's sad that I can't tell the two apart anymore."

    scene bg school_library at right 
    with locationskip

    play music music_happiness fadein 2.0

    "I slide my books down the return chute and they crash into the cart with a pleasant thud."

    play sound sfx_impact2

    show yuuko panic_up 
    with vpunch
 
    "Yuuko, however, doesn't seem as impressed as I."

    yu "H-Hisao! You scared me!"

    hi "Sorry, I thought you would be used to that by now. Or is the literacy level here so low that no-one borrows any books?"

    show yuuko worried_up 
    with charachange

    yu "Huh? No I think everyone here can read fine…"

    hi "Yeah… never mind."

    "There are some battles that you can never win. Trying to explain jokes are one of them. My Dad taught me that the hard way."

    hi "Say, Yuuko, have you seen Hanako about? She left class early but she wasn't in her usual hiding place."
    
    show yuuko closedhappy_down 
    with charachange

    yu "I think I saw her sneak in before lunch…"

    show yuuko panic_up
    with charachange
         
    yu "Oh! But I'm not supposed to tell anyone that!"

    hi "I just told you that I saw her leave, no need to stress out…"

    show yuuko smile_down
    with charachange

    yu "Oh… of course. She's probably up the back."

    hi "Thanks. Get any new books in recently?"
    
    show yuuko worried_up 
    with charachange

    yu "No, sorry. I'll let you know when we do though."

    hi "Okay."

    "If there's one thing I know about librarians, part-time or otherwise, it's that they appreciate people that take a genuine interest in their work."

    hide yuuko 
    with charaexit

    show bg school_library at Fullpan(10.0, dir="left") 
    with None

    "I walk the now-familiar path to Hanako's reading nook, picking out a few titles along the way."

    "Sometimes I find it hard to discover a book that will interest me amongst the shelves. An author's name and a two-word title don't mean much in a sea of similar words."

    "For that reason, I sometimes re-read books that I read in the past. Better to bet on the favorite than the new runner."

    "An unfamiliar title from a familiar author peeks out among the spines of its neighbors, so I remove it from the shelf."

    "At least I'm not going over old material."

    scene ev hana_library_read_std 
    with locationskip

    "As expected, Hanako sits on her beanbag, buried deep in a copy of “Dance! Dance! Dance!”"

    hi "Hi Hanako. How's it going?"

    "I fight back the urge to ask why she left class early. If Lilly's suspicions were right, then asking her about that could have the opposite effect."

    "Best to leave it for the time being. Sometimes the best way to get an answer from someone is to never ask the question."
    
    show ev hana_library_smile_std 
    with charachange

    ha "H-Hisao. I'm fine."

    hi "Good to hear. How's that book? I've heard it's a trip."

    ha "I-it's good… I think."
    
    ha "I've only j-just started it, so I d-don't really know."

    hi "Fair enough. Let me know how it goes. I might borrow it once you're done."

    ha "S-sure."

    "There's a good fifteen minutes left in lunch. Not enough to really get into a book, but too much to stand around doing nothing."
    
    show ev hana_library_read_std 
    with charachange

    "And Hanako's already returned to her reading, so I doubt I'll get much conversation from her."

    "Oh well, I'd better make myself comfortable."

    play sound sfx_pillow

    "I slouch into a beanbag and crack open my book."

    "The familiar style of the author leaps out at me from the very first line. As the sentences turn into paragraphs I start to relax a little."
    
    stop music fadeout 8.0

    "But, no matter how I try, I can't seem to get myself into the atmosphere of the book."

    "This is partly due to the lack of time, but the more distracting item is Hanako."
    
    show ev hana_library_std 
    with charachange

    show ev hana_library_read_std 
    with charachange

    "Every ten or so seconds she peers over the top of her book, but when our eyes meet she quickly ducks behind the covers."

    "I guess she did want to talk about something after all."
    
    scene bg school_library 
    with locationskip

    hi "What's up? You look like a prairie dog on lookout."

    show hanako emb_blushing at centersit
    with charaenter

    ha "N-… it's nothing."

    hi "I've told you before, \"nothing\" means \"something\" when you say it like that."

    show hanako cover_worry at centersit
    with charachange

    "Hanako squirms a little in her beanbag, hoping that by changing her position she'll find the words she's looking for."
    
    show hanako emb_downsad at centersit
    with charachange

    ha "I… I was in an accident."

    hi "Accident? Just now? Are you alright?"
    
    show hanako emb_sad at centersit
    with charachange

    "Hanako shakes her head, her hair flowing around her shoulders in wisps of amethyst on a background of pale and dark flesh."
    
    show hanako emb_downsad at centersit
    with charachange

    ha "N-no. When I was y-younger."
    
    play music music_hanako
    
    "Realization crashes into me like a semi trailer."
    #I want to change this metaphor, but the minute I thought 'truck' I also added 'berzerker' in my head. Fuck. -SC

    hi "It's alright Hanako, you don't have to tell me anything if you don't want to…"

    "Again she shakes her head."
    
    show hanako emb_sad at centersit
    with charachange

    ha "N-no. I want… I have to tell you."
    
    scene ev hanako_crayon1
    show hanako_crayon2 behind ev
    with locationskip

    ha "When I was young… I was in a fire."

    ha "M-my house b-burnt down, and I nearly… I nearly didn't make it."

    hide ev hanako_crayon1
    with charaexit

    ha "A-after that… I was alone…"
    
    scene bg school_library 
    show hanako emb_downsad_close at centersit
    with locationskip

    "Hanako's eyes glisten in the dim light of the library, and I reach out to grasp her hand."

    hi "It's okay Hanako, you don't have to keep going."
    
    show hanako emb_sad_close at centersit
    with charachange

    ha "B-but… I have to…"

    hi "Why? What brought this on?"

    show hanako cover_distant_close at centersit
    with charachange

    ha "L-last night Lilly t-told me about your heart…"
    #Continuity check needed. -SC
    #Lilly finds out about Hisao's heart in A03b; I'm 90$% sure you can't get the H path without seeing A30b, but worth a check 
    show hanako cover_worry_close at centersit
    with charachange

    ha "A-and I… I didn't think it was f-fair."

    hi "Fair?"
    
    show hanako emb_blushing_close at centersit
    with charachange

    ha "T-that I knew about you b-but you didn't know about me…"

    "I squeeze Hanako's hand a little."

    hi "Don't be silly. But yes, I have arrhythmia."

    "I lean a little closer to Hanako."
    
    hi "What I didn't tell Lilly is that I had my first attack when a girl confessed to me."

    "I smile a little to break the tension."

    show hanako cover_worry_close at centersit
    with charachange

    ha "R-really?"

    hi "Really. I haven't heard from her for a while though so I guess it's all over."

    hi "So now, we both know a little more about each other. But you don't have to talk about things if you don't want to."

    "In fact, I feel a little bad even thinking about that whole incident. I can almost smell the hospital's disinfectant burning the back of my sinuses again."

    "I imagine Hanako is going through the same thing now."

    "When I was in the hospital I went to the burns ward once, and only once. I was bored, so I went for a walk through all of the wards."

    "I went through oncology and thought I could take it, but when I got to the burns ward I turned around and went back to my bed."

    "To think that Hanako would have spent months in a place like that, smelling nothing but corrupted skin, strong disinfectant and sterilised air."

    "The really bad cases were kept in isolated pods that no foreign objects could enter. That would have meant no reading."

    "I would have gone insane if I didn't have my books in the hospital."

    "And she said she was alone… Did her parents die? I'll have to ask Lilly about it. I can imagine myself saying something dumb unintentionally."

    show hanako emb_timid_close at centersit
    with charachange
    
    ha "T-thank you Hisao."
    
    show hanako emb_downtimid_close at centersit
    with charachange
    
    ha "I… I haven't told many people about this."

    hi "To be honest, I haven't told many people about my… circumstances either."

    show hanako cover_smile_close at centersit
    with charachange

    ha "T-then I won't tell a-anyone either."

    hi "Deal."
    
    play sound sfx_warningbell

    "I change my grip on Hanako's hand into a handshake as the warning bells chime through the window."

    hi "Well then, we'd better head back to class, eh?"
    
    show hanako basic_bashful_close at centersit
    with charachange

    ha "S-sure."

    $ renpy.music.set_volume(1.0, 0.0, channel='music')

    window hide

    return

#-------------

    
