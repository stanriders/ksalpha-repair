label en_R2:
    
    window hide None
    scene bg school_scienceroom
    with locationchange
    with Pause(1.0)

    play music music_pearly fadein 6.0
    
    window show dissolve

    "It's already half past eight, but this morning's class has not yet begun. We were supposed to have physics but the teacher is nowhere to be seen."
   #<Perhaps these two sentences can be compounded?>

    "Had I known this beforehand, I would have slept in too. How unfair."
    
    play sound sfx_dooropen
    with Pause(1.0)
    play sound sfx_doorslam    
    with vpunch

    "Suddenly the classroom door slams open and a troll-like creature grunts its morning greeting to us from the doorway."
    
    show muto normal at center with charaenter
    
    mu "Good morning everyone!"

    "Mutou looks like he really has woken up from under a bridge."

    "The stubble, his messier-than-normal hair and the stained dress shirt create a less than favorable impression."

    "I guess he had fun last night at the festival too."
    
    show muto irritated with charachange

    mu "Excuse my being late, I ran into unexpected problems."

    "He doesn't delve into these mysterious problems any further, but proceeds to take roll call and get the lesson started."
    
    show muto smile with charachange

    mu "All right, then, today's subject is {a=ismuth_R2_friction}friction{/a}…"
    
    scene bg school_scienceroom with shorttimeskip 

    "Before long, I have descended into a comfortable coma-like state along with the rest of the class, letting Mutou's rambling speeches pass through from one ear to another without leaving a trace."

    show muto normal 
    with charachange
    
    mu "Now, who could tell us the solution to this problem?"

    "He has written a rather easy equation on the blackboard and desperately tries to get the class to partake in the lesson."

    show muto irritated with charachange
    
    mu "Nobody? Come on now kids. Nakai, how about you?"

    "With my back pressed against the wall, I give an answer to him, causing his shaggy features twist into a genial smile that would scare little children senseless."
    
    show muto smile 
    with charachange

    mu "Precisely! Good work, Nakai!"

    "I'm both disturbed and honored by the fact that he can remember my name only two weeks after I transfer in."

    "After all, Mutou has serious trouble remembering anyone else's name in the class and most of my classmates have been here for three years already."

    play sound sfx_normalbell
    
    stop music fadeout 3.0

    "Not a minute too soon, the lunch bells ring."
    
    scene bg school_hallway3
    with locationchange
    
    play music music_running fadein 0.5

    mystery "MAKE WAY! IMPORTANT BUSINESS!"
#<Business? Sounds serious.>

    "I turn my head just in time to see other people scatter out of the way as someone charges from the far end of the corridor towards the stairwell."

    "It's too late to realize that I'm standing in the middle of the corridor, directly in the way of the incoming human projectile."

    "I leap back towards the doorway like the main character from a John Woo movie, but unfortunately the person running towards me dodges to the same direction."

    "In the following 0.2 seconds several things come to mind almost simultaneously."

    "First, I recognize that the girl who is on collision course with me is Emi. Of course."

    "Second, I contemplate Mr. Murphy and his law, the enemy of all humanity."

    "Third, why is Emi carrying a foot-tall stack of prints and running at the same time?"
    
    play sound sfx_pillow
    with vpunch

#CRASH!

    "Emi is on her knees on the floor, holding her forehead with both of her hands."
    
    "She didn't manage to slow down before the crash so I tumbled backwards and fell straight on my tailbone. {a=ismuth_R2_impact}It hurts like hell.{/a}"
    
    show emi sad_depressed at center with charamoveinbottom

    emi "Owie… Why does this always happen to me?"

    hi "Gee, I wonder. Could it possibly have anything to do with you running in the corridors like you were on fire?"

    show emi sad_shy with charachange
    
    "She whimpers regretfully and looks like a hurt puppy, making me regret my snappish comment the very instant it emerges from my lips."

    show emi sad_pout 
    with charachange
    
    emi "But… I was in a hurry."

    hi "I can tell you were, but you should try to be less reckless."
    
    stop music fadeout 4.0

    show emi sad_shyblush with charachange
    
    "Emi wails weakly one last time, which I interpret as a sign of consent."
    
    show emi sad_shy 
    with charachange
    
    "She rubs her forehead a few times as if to expel the ache while her gaze sweeps over the hallway floor."
    
    play music music_tranquil fadein 1.0

    "As she notices her neat stack of papers spread all over the floor in one big mess she lets out a horrified yelp."

    show emi excited_sad 
    with charachange
    
    emi "Aah! My prints! Oh no oh no, what am I going to do? Teacher will give me hell if they got dirty."
    
    hi "They are probably just fine. Let's gather them back to a neat pile, he won't notice a thing."

    "We quickly round up the papers and Emi tries to sort out the messy stack of prints in her hands back into the orderly pile it was."
    
    show emi basic_grin 
    with charachange

    emi "Where are you going?"

    hi "Nowhere in particular I guess. Didn't want to be left alone with Mutou in the classroom. I don't think he has a hangover, but something's wrong with him."

    #I took the next conversation from the final game, for continuity sake. - Kelper
    
    show emi sad_grin at center 
    with charaenter
   
    emi "By the way, Hisao…"

    "Her tone is way too sweet and soft to be sincere. I can sense the trap about to be sprung upon me by this miniature health-devil."

    "I know what she's about to say even before she continues, because I've been trying to avoid her all week."

    show emi excited_proud 
    with charachange

    emi "I still haven't seen you at the track this entire week."

    hi "Maybe I've been there when you haven't."

    show emi sad_annoyed 
    with charachange

    emi "That's impossible. I'm there all the time."

    hi "But you sleep and go to class."

    show emi basic_annoyed 
    with charachange

    emi "I do those at the same time as you do."

    hi "Yeah, I know, I know. I just… haven't been able to pick myself up."

    hi "Don't rat me out to the nurse, okay?"

    hi "Running just isn't my thing, and I haven't come up with a good alternative."

    show emi excited_happy 
    with charachange

    emi "Why don't you come to the track meet this weekend? Maybe you'll get inspired."

    hi "Track meet?"

    show emi basic_happy 
    with charachange

    emi "Yeah! People from a few other schools come here for some friendly track and field action. It's on Sunday afternoon."

    "I can't think of any reason not to go."

    hi "Sure. I'll come and cheer for you. I guess you'll be running?"

    show emi excited_proud 
    with charachange

    emi "Of course! You'll get to see me beat them all!"
    
    #End of snatched script. - Kelper
    
    show emi excited_happy 
    with charachange
    
    emi "Have you eaten lunch?"

    hi "Not yet, not feeling very hungry though."
    
    show emi basic_confused 
    with charachange

    "She looks at me incredulously, as if doubting the my sanity for letting such a thing out of my mouth, the gathers her wits."

    show emi basic_happy 
    with charachange
    
    emi "You should go to the roof! I promised Rin I would eat lunch with her. I bet she'd like company."

    "Oh dear. My lunches with Rin have been remarkably unsuccessful. Must be karmic law or something."

    "I know where this conversation is going and it's hard to not get drawn along, so I have little choice but to play ball."

    hi "Ok, I was actually going to buy some bread when you tackled me so I'll go pick that up firsrt"
    
    show emi basic_closedgrin 
    with charachange
    
    "Emi smiles brightly before I say anything further."
    
    show emi excited_amused 
    with charachange

    emi "Nono, I'll deliver these super quickly and buy you and me some lunch, and Rin too of course. Do you like curry bread?"

    hi "It's fine, you don't really need to…"
    
    show emi excited_proud 
    with charachange
   
    emi "Don't worry, it's all right. Take it as an apology. I'll be back before you know it."

    hide emi with charaexit
    
    "Emi starts walking along the corridor, not looking where she is going because she is talking to me at the same time."

    "I'm left standing powerlessly in front of the classroom."

    hi "That's what I'm worried about. Don't get into another accident."

    emi "I won't!"

    "Famous last words. She is already jogging down the stairs as she shouts the not-so-reassuring promise back to me."
    
    stop music fadeout 2.0
  
    scene bg school_staircase1
    with locationchange

    "Sighing quietly, I start plodding in her wake but instead of taking the stairs down, I start my climb upwards."

    "The stairwell up to the roof is unlit and just as creepy just as it was before."

    play sound sfx_dooropen
    
    "The door squeaks weakly in protest as I push it open to let myself out."
    play sound sfx_door_creak
    scene bg school_roof
    with whiteout
    play ambient sfx_rooftop fadein 2.0
    "Rin is there too like Emi said, for some reason lying spread-eagled at the other end of the pebble-covered rooftop."
    
    scene ev rin_roof_boredom with locationchange
    
    "Predicting something unnecessarily strange again, I walk as slowly as possible to her."
    
    show hisao_shadow with charaenter
    with Pause(1.0)
    
    show ev rin_roof_surprise with charachange
    
    rin "Helloooo."
    
    "She sounds very drowsy as she says that, stretching the end of the word with a blurred voice, but her eyes are wide open."

    "I look down at her, my shadow overlapping her face."

    hi "What are you doing?"

    show ev rin_roof_doubt with charachange
    
    "Rin raises an eyebrow, seemingly challenging the rationale of my perfectly valid question."

    rin "I thought you had a heart problem, not an eye problem."

    "She answers without turning her face towards me."

    "Rin's smartass comments are infuriating, and the worst thing is that I'm not sure if she is doing it on purpose or accidentally."

    hi "That's right. Let me rephrase, Miss Nitpick."
#<Miss Wright.>

    hi "Why are you lying on your back on the rooftop?"

    "She gives a lazy shrug and sniffs dismissively."
    
    show ev rin_roof_nonchalant with charachange

    rin "I'm trying the experience. People probably don't do this enough."

    hi "Why should people do this?"

    "She's playing dodgeball with me again, answering my inquiries with nothings and riddles."

    "But I don't want to ignore her either."
    
    show ev rin_roof_boredom with charachange
    
    rin "Because, everyone is too busy with their lives to pay attention to the really important things."

    hi "Like watching the sky?"

    show ev rin_roof_doubt with charachange
    
    "She tears her gaze away from the sky and finally looks straight at me. The penetrating deepness of her eyes once she focuses them on something is startling."

    rin "You know, if you were a girl I could see your {a=ismuth_R2_panties}panties.{/a}"
#<I'm so going to quote this out of context on IRC.>

    hi "If I was a girl, I wouldn't come this close to anyone who tries to sneak a peek at my panties."

    show ev rin_roof_nonchalant with charachange
    
    rin "I wouldn't either, but sometimes it can't be avoided. Like now, for example."

    "The worst thing one can do when conversing with Rin seems to be going along with her nonsensical, rambling speeches."

    "All that waits in that direction is madness and despair."

    show ev rin_roof_boredom with charachange
    
    hi "What subject you had in morning classes?"
      
    rin "I skipped class."

    hi "To do this?"

    rin "Well, I'm not actually doing what it looks like I am doing, or at least I think that what I am doing doesn't look like what I look like but from your perspective… "
    
    extend "I guess…"

    rin "Yeah, I skipped class to do this."
#<I sorta altered your meaning, but I think this'd look better with the line break here.

    hi "I guess your reason, whatever it is, as good as any."

    scene bg school_roof with locationchange
    
    play sound sfx_rustling
    
    "Giving in to the numbing sensation in my legs, I sit down on the roof next to Rin."
    
#<The bit about him sitting cross-legged is kinda extraneous.>

    "The pebbles are not the most comfortable bed in the world, but if she can stand it, then I should be able to as well."

    rin "What are you waiting for?"

    hi "Hmm?"

    rin "Try it."
    
    stop music fadeout 2.0

    "I bend my neck backwards too take a look where she is looking."
    
    hide bg
    scene bg misc_sky at Fullpan(40.0) onlayer kelpersux 
    with dissolve
    
    play music music_twinkle fadein 1.0

    "The silvery blue sky, dotted by herds of cloud-sheep fills my vision entirely."

    "While it's pretty, the view is nothing special even though the weather is fair."

    "I give a shrug, trying my best to imitate the nonchalant manner which Rin seems to have evolved to perfection and lie down on my back."

    "The stones prickle my back through my thin shirt whenever I shift my weight even a little, forcing me to keep as still as possible."

    "I try to ignore the rocks and myself, concentrating on the vastness over us."

    "Far above, the summer clouds drift soundlessly across the dome of the sky."

    "Neither of us has anything more to say thus silence covers the rooftop."

    "The subdued noise of students on their lunch break, cicadas in the trees and traffic buzzing past the school are humming pleasantly somewhere in the background."

    hi "Listen, I had a great time yesterday."

    "Rin turns to look at me as well, resting her cheek on the pebbles. She has an incredulous look on her face."

    rin "You did?"

    hi "Well to be honest, no. But I had fun."

    "I try to make the it sound as convincing as possible."

    rin "Ok."

    rin "Now that you mention it, I had fun too. More than I expected, which was none."

    hi "That's not really a compliment."

    rin "Did you expect one?"
    
    hi "Not really."

    "Both of us turn back to quietly observe the skies."

    "A cloud passes above us, casting its shadow on the school."

    "A chill surges through me, more from the sudden contrast of sunlight and shadow than the cold of the shade."

    "I realize that summer is not here quite yet."

    "…"

    "The only measure of time passing is the slow pace of the clouds moving towards the town."

    "Stray beams of golden sunlight leak through the gaps, blinding me for a moment whenever they hit in my eye directly."

    "The blue of the sky looks so unreachable."

    "This reminds me of the time I spent in hospital, I was bored out of my mind on a daily basis."

    "Somehow, it didn't matter in the end. I learned to appreciate different things than watching TV and talking crap with people you don't even like."

    "The comprehensive sensation of calmness spreads from my vision to my other senses, finally hitting my brain."

    "An airplane zooms across my field of vision, leaving two thin contrails in its wake like a pair of chalk lines drawn from one end of the sky to the other."

    "I wonder where it is heading to."

    "The low din of its engines carries all the way down to my ears, although it's barely audible over the racket from the quad." #formerly known as 'quadrangle' --TcDohl

    hi "I don't understand is why this is more important than going to class."

    rin "Isn't it nice to do something you like?"
    
    rin "Every once in a while?"

    stop music fadeout 2.0
    
    hi "Of course, but—{w=0.2}{nw}" #reminder for the potential {nw} break
    
    emi "What are you doing?"

    "Emi has snuck up on us without either noticing and is only a step away from me, holding several packages wrapped in plastic film on her arms."
    
    show emi excited_happy_close with charamoveinbottom 
    
    "She leans forwards and peeks over me, overshadowing my face almost exactly the same way I overshadowed Rin before."
    
    "I wonder how weird this looks, the two of us lying on our backs on the rooftop."

    hi "That's what I asked too."
    
    play music music_comedy fadein 0.5

    rin "I would be more concerned about what you are doing. If I was Emi, I wouldn't come that close to people who could see your panties."

    play sound sfx_pillow

    show emi sad_angry_close 
    with vpunch  

    emi "Rin!"
    
    show emi invis at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.15) with Dissolvemove(0.5)
    hide bg
    show bg school_roof behind emi with locationchange

    show emi basic_hes at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.0) with Dissolvemove(0.5)
    
    "Emi's voice is scandalized, but she quickly takes a step backwards and presses her hands against the front of her skirt so abruptly that the bread parcels she was carrying fall on the rooftop."

    "I quickly avert my eyes, and glance angrily at Rin. She pretends she is not seeing me."

    show emi basic_shock with charachange
    
    emi "Hisao is not like that, isn't that right?"

    hi "Of course I'm not."
           
    emi "See, Rin?"
    
    play sound sfx_rustling
    
    show emi basic_annoyed at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.15) with Dissolvemove(0.6)

    show emi basic_annoyed at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.0) with Dissolvemove(0.6)

    "Emi scowls at her and crouches down to pick up the bread parcels."
    
    show emi basic_grin_close 
    with characlose
      
    show emi basic_grin_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.12) with dissolvecharamove

    "She wipes the dust off them while skipping lithely around me to Rin's other side and sets herself down."

    emi "Anyway, here's your bread. Sorry it took a while."

    hi "No, thank you for treating me."

    "I pull myself up into a sitting position and accept the bread Emi is offering."

    "All three of us dig in the simple meal ravenously. The bread is surprisingly decent and fills my churning stomach readily."

    show rin invis at Position(xanchor=0.5, yanchor=1.0, xpos=1.0, ypos=1.2) with None
    show emi basic_grin_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.3, ypos=1.12) 
    show bg school_roof at bgleft 
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.9, ypos=1.07)
    with dissolvecharamove

    
    "I follow from the corner of my eye the skill with which Rin handles her bread between her feet."
    #Is he thinking what I think he's thinking?

    
    play sound sfx_warningbell
    show rin basic_absent_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.9, ypos=1.07)
    show emi basic_shock_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.3, ypos=1.12) 
    with charachange
  
    
    "We barely finish the lunch before the bells ring, calling us back to classrooms."

    "Where did my lunch hour disappear?"
   
    stop ambient fadeout 1.5
    scene bg school_scienceroom
    with locationskip

    
    show misha sign_smile at center 
    with charaenter
    
    mi "Hicchan!"
    
    "Misha waves at me as soon as I enter, and starts talking before I even make my way across the classroom."
    
    show misha hips_smile 
    with charachange
    
    mi "How was your festival? Did you have fun?"
    
    hi "Umm... still undecided on that."
    
    hi "Why?"
    
    show misha hips_grin 
    with charachange

    mi "Wahaha~, just asking, just asking!"
    
    "Her eyes glint in a way that tell me she's not just asking, although her motives I can't even start to guess."
    
    hide misha 
    with charaexit
  
    "As the well-timed entrace of the English teacher prevents us from talking further, Misha falls into plan B."
    
       
    show misha hips_grin_close at offscreenleft 
    with None
    
    window hide dissolve
    
    #show misha perky_smile_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.1, ypos=1.0)
    show misha perky_smile_close:
        xanchor 0.5 yanchor 1.0
        xpos 0.1 ypos 1.0
    show bg school_scienceroom at left 
    with charamove
    
    play sound sfx_paper
    $ fixedwritten_note(u"I was all day with Shicchan~! We had a lot of fun!")
    
    play sound sfx_paper
    $ fixedwritten_note(u"Weren't you supposed to be doing work?")
    
    show misha hips_grin_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.1, ypos=1.0) 
    with charachange
    
    play sound sfx_paper
    $ fixedwritten_note(u"Ehehe, don't worry! Everything went really well~")


    window show dissolve
    
    "..."
    
    "I don't reply to that and she leaves me alone after Shizune demands her attention."

    show misha invis at offscreenleft 
    with dissolvecharamove

    "My attention, on the other hand, is directed to the windows."
    
    "The sky is very small, looking at it from here, through the windowglass and the canopies just outside of it."
    
    "I catch only small glimpes of blue, everything else is left as a clutter of noise right in the middle of my field of vision."
    
    "What \"experience\" Rin wanted out of staring at the sky? Surely she has done it before, just like everyone."
    
    "So... there is nothing special."
    
    "..."
    
    stop music fadeout 10
    
    "It's no use trying to guess her mind, but if I don't do that I have no excuse to not concentrate on the lesson."
    
    "I look at the scribbles appearing on the blackboard, trying to figure out the meanings."
    
    "English really, really is not my favourite subject. We have a mutual and strong dislike for each other."
    
    "But I bear with this relationship."
    
    scene bg school_hallway3
    with shorttimeskip
    return

label en_R3:
    
    scene bg school_hallway3 with dissolve
    
    play sound sfx_normalbell
    
    play music music_normal fadein 2.0
    
    "Thick afternoon light invades the corridor, making the air feel heavy and lazy."
    
    "My body is feeling heavy too as I drag it two doors down the hallway to the art classroom."
    
    "This is maybe part of the reason why I didn't join any clubs before, afternoons just are not suited for activity."
     
    scene bg school_classroomart at left 
    with locationchange
     
    "The art classroom looks almost the same as our own, except with less seats and more paintings hanging on walls."
    
    "I end up sitting on the first seat my eyes land on right next to the door, before even scouting the room for a good place to sit."
    
    "A few other members are lounging in their seats, waiting for the teacher."
    
    "Nobody comes to greet me -maybe introductions are left for later?- so I settle just for silent observation as well."
    
    stop music fadeout 2.0
    play sound sfx_footsteps_hard fadein 0.2

    "The wait proves to be extremely short."
    
    play music music_happiness fadein 2.0

    show nomiya smile at center 
    with charaenter

    "Nomiya strides behind his desk with three long steps and gives a flamboyant greeting with a smile."
    
    show nomiya veryhappy 
    with charachange

    no "Good afternoon, everyone!"
    
    show nomiya talk 
    with charachange
    
    no "First things first, we have a new member so everyone get along with Hisao here."

    "He winks at me unsettlingly."

    "All eight club members me included, answer his greeting with considerably less enthusiasm, but people straighten up in their seats and pay attention to what he is saying next."
    
    show nomiya smile 
    with charachange

    no "All right, since we more or less completed those water color works last time, we'll start on something new."
    
    show nomiya talk 
    with charachange

    no "I was thinking that today, we could go over the details of a human face."
    
    show nomiya veryhappy 
    with charachange

    no "How does that sound?"

    "Nobody answers except with some unintelligible murmurs, which Nomiya apparently interprets as unanimous approval."
    
    show nomiya talk 
    with charachange

    no "So everyone, pick a partner and draw a portrait of each other."

    no "You should be able to complete this today but, if not, we can continue next time."
    
    show nomiya veryhappy 
    with charachange

    no "Remember to pay attention to lighting and shadow, and give it your best!"

    "Pairing up?"
    
    hide nomiya 
    with charaexit

    "People stand up from their seats and move them together."

    "Pretty quickly most of the class has paired when friends team up with each other, but I'm left standing in the middle of the room alone."

    "I see two girls from my class here, but I don't know either of them well enough and they already paired up with each other."

    "Then there is Rin."
    
    show bg school_classroomart at right 
    with charamove

    "Rin is sitting in the furthest corner of the classroom, staring out of the window seemingly uninterested in taking part of the class."

    "Since nobody else seems to be willing to pair up with her, I walk to her seat."

    "I can't see her face because her hair is covering most of it and she's looking away from me."

    hi "Rin?"

    "I call out her name. No response."

    hi "Hey, would you like to be my pair for this assignment? You are the only one I know from here."
    
    show rin basic_absent at center 
    with charaenter

    "She seems to finally acknowledge my presence and turns her head like a robot to see who is addressing her."

    "…"

    "Rin doesn't answer, and I don't want to repeat the question either. I'm sure she heard it on the first time."

    "…"

    "Why doesn't she say anything? It can't be such an awful fate to be paired up with me, can it?"

    "She's still not looking at my face but instead stares directly at my chest and stomach."

    "…"

    show rin basic_deadpan 
    with charachange
     
    rin "Oh ok, why not."

    "What took so long to decide?"

    "I grab a vacated chair and easel nearby and seat myself directly opposite to her."
    
    show rin negative_spaciness_close 
    with charachange
    
    stop music fadeout 0.8

    rin "Do you want me to do it with my foot or my mouth?"
#<Cue spit-take.>

    hi "What did you say?"
    
    play music music_another fadein 1.0
    
    show rin relaxed_surprised_close 
    with charachange

    "She tilts her head, her brows forming questioning arches as if she doesn't understand that I didn't understand the question."
    
    show rin basic_deadpan_close 
    with charachange

    rin "I don't mind drawing either way. You'll look better if I do it with the foot, though."

    "Is this the fate of a man? To interpret everything possible as innuendo?"

    hi "Oh, that. Er, with your foot then I guess."
    
    show rin basic_deadpannormal_close at center 
    with dissolvecharamove

    "Nodding to my answer, Rin gets up from her seat and sits down on the floor."
    
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with dissolvecharamove
    
    "Then she kicks off her sandals and removes the sock from her right foot with her left one."

    "In one fluid motion, Rin picks a pencil from the box on her desk between her toes and swings her other leg over her head to snatch the paper from the desk."

    "Although I was prepared for this, her display of dexterity is so prodigious that I just stare at her stunned."
    
    show rin negative_annoyed_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) 
    with charachange

    "When Rin raises her face to see if I'm ready I quickly turn my face away."
    
    show rin basic_deadpan_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) 
    with charachange

    "I pretend to contemplate my choice between two identical pieces of graphite, hoping she didn't notice my staring."

    "First Rin poses for me a few minutes so I can sketch her outlines and then we switch roles."
    
    show rin basic_deadpannormal_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) 
    with charachange

    "After she's happy with the rough sketch we both start drawing a more detailed portrait."
        
    hide rin with Dissolve(1.2)
    show bg school_classroomart at left with dissolvecharamove

    "I'm not especially artistically talented, so I'm scared my portrait will turn into something disfigured, especially when compared to my partner's skill."

    "Rin is not helping either."

    "She doesn't sit still for even ten seconds but instead tilts her head from side to side to judge her drawing, bites at her lower lip looking unsatisfied and constantly shuffles around like she is sitting on hot coals."

    "Just like when she was painting the mural, Rin becomes so engrossed with her drawing that it seems that she shuts out me, the classroom and the entire world away from her own little sphere of existence."

    "Her pencil moves across the sheet with confident strokes as she transfers my likeness onto paper."

    "Every now and then, she leans backwards seemingly to get some perspective while sometimes she bends forward and downward until her nose almost touches the paper."

    "The constant rocking back and forth looks silly."

    "Suddenly Rin proves she's not completely drifted into a world of her own and opens her mouth."
        
    rin "So, how's life for you?"
    show bg school_classroomart at right with dissolvecharamove
    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charaenter
    
    "She doesn't raise her eyes from the drawing, which is a good thing since I jolted from the surprising break of silence as if I was electrocuted."
    
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    hi "I…don't know. Fine, I guess."

    "I can't hear how she comments my answer because it seems she is suddenly having a private conversation in whispers with her sketch."

    "I don't understand how she can draw so well when she has the attention span of a butterfly."
    
    "As it seems she lost her interest, I go back to work with my drawing as well."
    
    hide rin with Dissolve(1.2)
    show bg school_classroomart at left with dissolvecharamove

    "I try to sketch Rin's hair, to somehow grasp the way the golden afternoon sun lights her bright red tousle aflame and transfer it to my paper in shades of black and grey."

    "Somehow my puny piece of graphite seems so inadequate."

    "Minutes pass but the sketch doesn't magically look any more like Rin than it did before. Her voice wakes me up from my despair."
        
     
    rin "I didn't mean it like that."
    show bg school_classroomart at right with dissolvecharamove
    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charaenter
      
    hi "Excuse me?"

    show rin basic_deadpannormal_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "What I meant was that if you are fine with this school and stuff like that."

    "It takes me a while to get that she is continuing from where she left fifteen minutes ago."

    "Rin pauses for a moment and glances up to me before continuing. Our eyes lock for a second, then she is staring at her drawing again."
    
    show rin basic_deadpansurprised_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange

    rin "You know, being sick like you are."

    rin "I've heard people who are terminally ill tend to have pretty different views on life than the rest of us."

    hi "Oh, right. Well, I'm not exactly terminally ill so I am not sure if I qualify. But sure, getting to know about the heart defect had me thinking."

    hi "While I was at the hospital, I thought a lot about stuff like that. I had four months doing nothing but lying in bed, so I guess that's just natural."
   
    "Rin raises her head to compare her drawing with the real me and frowns disapprovingly, as if she's not happy that the reality can't live up to her picture."
    
    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange

    rin "Did you come up an answer?"

    hi "Not really. In the end, I guess it all comes down to really deep stuff like the meaning of life, which you can't work out in your head."

    rin "Oh."

    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    "She turns her attention to the portrait again, ignoring me."

    "Rin doesn't say anything but I feel that I must continue my explanation."

    hi "I mean, everyone is in danger of dying every second of his or her life. You could get run over by a car tomorrow, or be murdered by some lunatic."

    show rin basic_deadpancontemplation_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "Yeah, or get struck by lightning, die in an alien invasion, or get spirited away by their vengeful ancestors."

    hi "Err… anyway. If everyone would just spend their days being scared of dying, there would be no sense to live at all."

    hi "I might have a higher chance of dying than most but I try not to think about it too much."

    show rin basic_deadpannormal_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "But you just said that you spent five months in hospital thinking of that."

    hi "Four months, and I did other things too, you know."
    
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange

    "She falls quiet again."

    "Something about the pressing silence makes me feel compelled to continue the explanation."

    "Maybe it's the way Rin is at the same time interested and totally nonchalant about whatever she asks me."

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    hi "In the end it all comes down to what you want to do with your life. Nobody knows what the meaning of life is but most people at least know how they want to spend it."

    hi "People who know they don't have much time left tend to rush to do whatever they have always wanted to do before it's too late."

    hi "Things like traveling around the world or whatever."
    
    show rin basic_deadpanamused_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange

    rin "I've always wanted to learn to play the balalaika."

    "Sigh."

#<Does this need to be capitalized?>

    #Took these out, seemed to come from nowhere. - Kelper
    
    #rin "I think I do. Isn't that the thing where you have no hope left anymore? Happens to me sometimes."

    #hi "No. Or yes, but no. It's the hospital ward for the terminally ill people who can't be cured by any means known to science, hence the nickname Lost Hope."

    #hi "People who are there have maybe half a year tops to live."

    #hi "Anyway, I heard a story from one of the nurses who took care of me when I was at the hospital."
    
    show rin basic_deadpancontemplation_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    "Rin raises her eyebrows appreciatively."
    
    #Next sentence was only "Would you do that?" or something of the sort. - Kelper
    
    rin "Would you do that? Do the things you have always wanted to do?"

    hi "I don't think I would do anything rash. But I decided I wanted to make the most out of my life"

    hi "You know, carpe diem and all that. That's why I wanted to come to this school. instead of being locked inside my house or the hospital."

    "I chuckle to myself and how weird this must sound."
   
    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
   
    hi "It's not like I suddenly have a burning passion to live life to its fullest, but I do try to make every day count for something."

    hi "So.."

    show rin basic_deadpannormal_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "So, you are not afraid?"
    
    "Of what? Dying?"

    hi "No, i don't think I am."
    
    show rin basic_deadpandelight_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange

    rin "That's good. I'm really happy for you."

    "From her outer lack of interest and monotone voice I can't deduct if Rin really meant that."
        
    show bg school_classroomart at left
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) 
    with dissolvecharamove
    show nomiya smile at left with charaenter
       
    no "Okay everyone, time's up! That's all for today, please turn in the drawings on my desk and see you all next Monday!"
    
    hide nomiya
    hide rin invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8)
    with charaexit
    
    "I glance at my portrait. It doesn't exactly look like Rin, but at least I have managed to capture her short hair and large eyes somewhat adequately."
    
    window hide dissolve
    
    show ev rinbyhisao at center with charamoveinbottom
       
    $ renpy.pause(1.0)
    
    window show dissolve
    
    "The nose and jaw look hideous though and the shadowing is terrible."
    
    show ev rinbyhisao at left 
    
    show bg school_classroomart at center 
    with dissolvecharamove  
    show rin basic_deadpannormal_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.85, ypos=1.0) with charaenter
    
    window show dissolve
    
    rin "That's not bad."

    "She has sneaked up behind me while I was lost in thought."

    "Damn it, I was hoping I could have smuggled the portrait to the teacher without Rin seeing it."

    hide ev rinbyhisao with charaexit
    
    show rin basic_absent_close at center
    show bg school_classroomart at right
    with dissolvecharamove


    hi "I'm not really happy with it. I wish I could draw better."

    show rin basic_deadpandelight_close with charachange
    
    rin "You just need some practice. Could you take my drawing to the teacher too? Thanks, that's awfully nice of you"
    
    "Ignoring her answering instead of me, I stand up anyway and step to Rin's easel. From the way Rin was drawing, it looked like she was really into it. I peek at the picture."
    
    window hide dissolve
    
    show ev hisaobyrin at center with charamoveinbottom

    $ renpy.pause(1.0)
    
    window show dissolve
    
    "It looks like me. No, it's more than that. The shades on my face, the serious eyes, and my messy hair in dire need of shearing."
    
    "It's perfect. She drew me."
    
    "And she did it with her foot."

    hi "Wow, that's amazing. I still can't believe how good you are at this."
    
    hide ev hisaobyrin 
    show rin basic_absent
    with charachange  
    
    rin "Thanks. I'm glad I could draw you. You are an interesting person."

    hi "You are an interesting person too, but that didn't help me at all."
    
    show rin basic_awayabsent with charachange

    "My self-deprecation has no limits today, but Rin ignores it all. I knew that I could never compare but even so, seeing the difference with my own eyes is quite humbling."

    rin "See, I tried to make you look like you think a lot, since you did a lot of thinking."

    show rin basic_deadpannormal with charachange
    
    rin "And yeah, I might have overdone the fed-up-with-life expression, but cynics just are like that, right?"

    show bg school_classroomart at left
    show rin basic_deadpannormal at right 
    with dissolvecharamove
    show nomiya smile at left with charaenter
    
    "Nomiya gives me no time to retort."

    no "Hurry up, you two!"

    "While we've been chatting the rest of the club has taken their leave."
    
    hide rin with charaexit
    
    "I quickly pick up our drawings and take them to the teacher's desk before hurrying after Rin who already left the classroom."
    
    scene bg school_hallway3
    with locationchange

    stop music fadeout 2.0
    "She is not in the hallway either. Oh well, I didn't have anything to say anyway, except maybe get back at her for calling me a cynic."

    hi "Yaaaaaaaawn."
    
    play music music_normal fadein 1.0

    "It's surprisingly late. I already got used to school ending at the same time every day, so I can feel the a few extra hours in my head. And my gut."

    "My growling stomach reminds me that I am absolutely ravenous. I'm so hungry that I'd dare anything the cafeteria staff has deemed edible."
    
    scene bg school_cafeteria
    with locationskip

    "My feet take me towards the Great Hall with irresistible force."
#<You sure that strength is the right word? I would have used determination, myself.>

    "Even when I see today's delicacy, fried mystery lumps, my steely resolve doesn't fade. I stuff the dinner down without tasting it at all, which is probably for the best."

    "I don't have much homework to do, but what little I have won't get done by itself so I stroll to the dormitories."
    
    scene bg school_dormhallway
    with locationskip

    "Preparing for the post-homework lull, I knock on Kenji's door."
    
    "He responds although I'm not sure in which way so I try the door."
    
    "It's locked."

    $ renpy.pause(1.0)
    play sound sfx_dooropen   
       
    "After several seconds the lock clicks open and he opens the door, "
    
    show kenji neutral at Slide(0.2,0.5,0.3,0.5,1.0) 
    with charaenter
    
    hi "Hey, could I borrow some books? I didn't take any with me when I moved here and the library closed already."

    show kenji tsun at Position(xanchor=0.5, yanchor=0.5, xpos=0.3, ypos=0.5625) with charachange

    stop music fadeout 1.0
    
    "He is squinting even more than usual and his eyebrows are twitching."

    play music music_kenji fadein 2.0

    "I surprised myself too. I'm usually more polite, I wonder if this is the consequence of dealing with Rin, to forget about all social norms?"
    
    ke "Er, sure. Go ahead, but return them and don't spoil any of my books."

    show kenji invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.1, ypos=0.5625) with dissolvecharamove
  
    $ renpy.pause(1.0)

    show kenji neutral at Slide(0.2,0.5,0.3,0.5,1.0) with charaenter
    
    $ renpy.pause(0.7)
    
    hi "Thanks."

    hi "Er, your books? These are from the library."
    
    show kenji neutral at Position(xanchor=0.5, yanchor=0.5, xpos=0.3, ypos=0.5625) with charachange
    
    ke "They are now mine."
    
    hi "Wait, are you the one who steals books from library?"
    
    show kenji rage at Position(xanchor=0.5, yanchor=0.5, xpos=0.3, ypos=0.5625) with charachange
    
    ke "What are you talking about man? If someone steals books don't come accusing me."
    
    ke "I've been liberating these from the oppressing feminist move."
    
    hi "You talking about that librarian girl, Yuuko?"

    show kenji invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.1, ypos=0.5625) with dissolvecharamove
    
    stop music fadeout 2.0
       
    "He turns away mumbles something I can't make out. I close the door behind me and walk to my own room at the other end of the hallway."

    show bg school_dormhisao_ss with locationskip

    "After finishing the homework and reading a few hundred pages, I'm ready to call it a day."
    
    window hide dissolve
    scene black with Dissolve(1.5)
    return

label en_R4:
    scene black
    with dissolve
    scene bg school_dormhisao
    with openeye   
    play music music_pearly fadein 1.5
    window show dissolve   
    
    "I wake up sweaty and panting as if I ran a marathon in my sleep."

    "I feel sick."

    "I don't think it was a nightmare."

    "Although, if it wasn't a nightmare, why did I wake up in such a condition?"

    "Pushing that thought aside, I set out to find my uniform."

    "{a=ismuth_R4_love}I'm out of clean shirts so I use the one from yesterday. I quickly button it up and pull on my pants before going outside.{/a}" #trousers -> pants - USA English
#<As opposed to leaving with the shirt unbuttoned and trouserless? I'm sure the ladies would l o v e that.>

    "The bitter taste in my mouth makes me lose interest in eating breakfast."
#<While this edit works, I think it might also work well to switch around the order of this sentence.>

    

    scene bg school_dormext_full
    with locationchange

    "Fighting back the sickening feeling, I join the rest of the students making their way to the main building."
    
    scene bg school_courtyard
    with locationchange

    play sound sfx_normalbell

    "I barely notice the morning sun shining brightly under the canopies of the cherry trees or the carillon sounding the beginning of class."
    
    scene bg school_hallway3
    with locationchange

    "My head feels worse with every step I climb on the staircase leading to the third floor."
    
    "I push myself past the boys gathered in the doorway and flop into my seat like a sack of flour."
#<Classmate boys sounds like a fancy title for someone in the worlds oldest profession.>
          
    scene bg school_scienceroom with locationchange

    stop music fadeout 6.0
    
    "From the corner of my eye I can see Shizune and Misha pause their animated conversation and turn almost simultaneously to my direction."

    "Goawaygoawaygoaway."

    show shizu behind_smile at tworight 
    show misha perky_smile at twoleft 
    with charaenter

    play music music_normal fadein 2.0


    mi "Good morning Hi!"

    "Her greeting is made of one hundred percent cheer and bursting energy."

    hi "Mornin'"

    "I fail to put either of those into my response."

    show misha perky_confused at twoleft
    with charachange

    mi "You don't look very energetic."

    hi "No wonder. I don't feel very energetic either."

    show misha hips_grin_close at twoleft
    with vpunch

    "She slaps me in the back and grins."

    show misha hips_smile_close at twoleft
    with charachange

    mi "Cheer up a bit! It's a great day!"

    show shizu basic_normal2 at tworight
    with charachange   

    "Misha's encouragement only makes me feel more miserable."

    "I catch Shizune's eyes. She has a strange expression on her face, but she blushes a little at the eye contact and looks away."
#<I couldn't think of a good way to keep some form of 'fluster' in there. If you are terminally ill, and the omission of that 'flusters' will kill you, then by all means rewrite.>

    show shizu adjust_happy at tworight
    with charachange

    "Could she be concerned for me?"

    show shizu basic_happy at tworight
    with charachange

    "Nah, get a grip, no way that princess ever could feel such a thing."

    "My saliva tastes metallic."

    "I press my hand against my mouth, trying desperately to swallow the rusty taste."

    "I wish I had something to drink."

    hide shizu 
    hide misha 
    with charaexit

    "Kayoko finally enters the classroom, sending everyone rummaging their bags for books and pens."

    "As I dig my pen case for a pencil, my hand brushes against something."

    "It's the piece of graphite I used to draw Rin's portrait yesterday. I put it in my pen case instead of returning it after yesterday's club meeting."

    "I pick up the graphite rod and weigh it against the palm of my hand."

    "There is nothing special in it, no hidden tricks, no magic. It's just a stick made of carbon."

    "{a=Note}However, if you know how to use it…{/a}"
#<This is one helluva cheesy line.>

    "I wish I could draw like Rin."

    "{a=Note}More practice?{/a}"

    "{a=Note}Is that all you need to be a good artist?{/a}"

    "Ignoring the teacher's sleep-inducing voice, I open my notebook from an empty page and press the tip of the graphite on it."

    play sound sfx_rustling
    with Pause(1.5)
    
    show ev bird0 with charaenter

    "What to draw?"

    "As I hesitate and raise my hand, the meek black mark it left on the previously blank paper seems aggravating."

    "What are you afraid of? Being laughed at?"
#<NIKE>
    
    "Picking the first image that pops in my head, I deliberately draw a thick line across the paper to get started."

    show ev bird2 with dissolve

    "I slowly sketch the picture on the notebook page, the image in my brain becoming clearer as the drawing gains shape."
     
    show ev bird3 with Dissolve(1.0)
    show ev bird4 with Dissolve(1.0)
    show ev bird5 with Dissolve(1.0)

    "Concentrating on the drawing, the sickening feeling fades to the background along with the teacher's voice."
    
    show ev bird6 with Dissolve(1.0)
    show ev bird7 with Dissolve(1.0)
    show ev bird8 with Dissolve(1.0)
    show ev bird9 with Dissolve(1.0)
      
    stop music fadeout 2.5
    
    "Suddenly a strange presence breaks my focus."
            
    show misha perky_smile behind ev at twoleft
    show shizu behind_blank behind ev at tworight
    
    hide ev bird9 with charamoveoutbottom
        
    "I look up to see two girls staring back at me."

    "Misha and Shizune have carried their chairs to my desk and are now standing on my either side, looking at my drawing."

    "I quickly dive on the desk, covering the doodle under my chest."

    hi "How long have you two been there?"

    show misha hips_smile at twoleft with charachange
    
    $ renpy.music.set_volume(1.0, 0.0, channel='music')
    play music music_comedy fadein 1.0
    
    mi "I think you need more practice."
    
    show shizu basic_normal_close at tworight
    with charachange

    "Shizune draws a few sharp signs in the air between herself and Misha."

    show misha sign_smile_close at twoleft
    with charachange
    
    mi "Shizune agrees."

    "Rin said the exact same thing yesterday, but why did it sound less condescending?"

    hi "You shouldn't judge before I'm finished."

    hi "Besides, don't you know it's bad luck to see an unfinished painting?"

    show misha cross_laugh_close at twoleft
    with charachange
    
    "Misha cracks in exuberant laughter."

    show misha hips_grin_close at twoleft
    with charachange

    mi "What, don't be silly! There's no way that could be true."

    hi "Whatever."

    show shizu adjust_frown_close at tworight
    with charachange

    "Shizune's eyebrows are furrowing dangerously and the movements of her hands are abrupt like knife slashes."

    show shizu behind_frown_close at tworight
    with charachange

    show misha hips_frown_close at twoleft
    with charachange
    
    mi "Shizune says that you should learn to take constructive criticism better."

    hi "I would if you'd actually offer some."

    "My ill temper is rising again. I know she is just teasing me but this day has been so awful so far that I just can't take it."

    hi "What are you doing there anyway?"
        
    show shizu basic_frown_close at tworight
    with charachange

    "Misha wags her finger admonishingly at my nose."

    show misha sign_smile_close at twoleft
    with charachange
    
    mi "Tsk, tsk Hicchan. Were you not listening to the teacher at all?"

    show shizu behind_blank_close at tworight
    with charachange

    show misha hips_smile_close at twoleft
    with charachange

    mi "We have a group assignment now."

    "I nod bleakly."

    show misha hips_grin_close at twoleft
    with charachange

    mi "So, what do you think of the topic of today's lesson?"

    hi "Not much anything… I didn't listen to a word of it."

    show misha hips_frown_close at twoleft
    with charachange

    "Misha slaps her forehead and shakes her head theatrically."

    mi "What are we going to do with you, Hicchan?"

    "How should I know?"

    "Luckily, Shizune and Misha together are more effective than three or four normal people so I can mostly slack on the assignment."

    "I try my best to offer at least some assistance, but I end up being mostly useless."

    show bg school_scienceroom 
    show misha perky_smile_close behind ev at twoleft
    show shizu behind_blank_close behind ev at tworight
    with shorttimeskipsilent
    
    play sound sfx_normalbell 

    "Kayoko keeps us in class five minutes past the lunch bells, but eventually she lets us off the hook."

    hide misha 
    hide shizu
    with charaexit
    
    "I quickly stuff my books into my bag while Shizune and Misha carry their chairs back to their own seats."

    "I crumple the failure of a drawing and stuff it in my pocket and start walking downstairs."
    
    stop music fadeout 2.0
    
    $ renpy.music.set_volume(0.5, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors
    scene bg school_hallway3
    show crowd
    show rin basic_deadpanupset at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.55) behind crowd 
    with locationchange

    "Bread from the cafeteria will have to suffice for my lunch. The only problem is the usual crowd swarming at the cafeteria."

    #"I have no choice but to brave the mob of students, unless I want to be left without lunch on top of missing breakfast."

    #"Anxiety grips my chest again as I wade through the sea of schoolmates. The noise is pure torture to my eardrums and the pressure is enough to give me claustrophobic vibes."

    #"I have to get out of here."

    #"Clutching my bread, I escape through the gardens, ending up at the perimeter wall."
   
    return

label en_R5:
    
    #scene bg school_scienceroom

    #show rin basic_deadpanupset
    #with charaenter
    $ renpy.music.set_volume(0.5, 0.0, channel='ambient')
    $ renpy.music.play(sfx_crowd_indoors, channel="ambient", if_changed=True)
    scene bg school_hallway3
    show crowd
    show rin basic_deadpanupset at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.55) behind crowd 
    with locationchange    
    
    play music music_normal fadein 1.0
        
    "It's not surprising Rin is lagging behind. I just don't see her being the kind of person who would rush for lunch, just like me."

    
    hide rin basic_deadpanupset with Dissolve(1.0)
    show rin basic_deadpanupset with Dissolve(1.0)
    
    rin "Hello."

    hi "Hi. Whatcha doing?"

    rin "Standing here. What are you?"

    hi "Err… I was going to the cafeteria for lunch."

    show rin basic_deadpannormal
    with charachange

    rin "Cafeteria… I haven't eaten there for a long time. I don't really like it. The food is not extraordinarily good."
    
    stop ambient fadeout 1.5
    hide crowd with Dissolve(1.5)

    "She falls silent and looks down at her shoes thoughtfully. Before I can ask if something is wrong, she snaps her head back upright."

    show rin basic_absent
    with charachange

    rin "Maybe it's time to see if the quality has improved."

    "I take that as a decision to join me for lunch."

    hide rin with charaexit

    "We descend the stairwell to the ground floor cafeteria."

    scene bg school_staircase2
    show rin basic_deadpan
    with locationchange

    play ambient sfx_crowd_indoors fadein 1.5

    "The line is quite long, reaching the bottom of the stairs, but we join it anyway."

    hi "To be honest, I'm not impressed by the taste of the cafeteria food either."
    
    show rin basic_deadpancontemplation with charachange
    
    rin "It is not extraordinarily good."   

    scene bg school_cafeteria
    with locationchange

    "We finally reach the counter, greeted by the impassive stare of the cook on the other side."

    "She looks so tired of her life I would not be surprised in the least if, one day, we found her drowned in her own ramen broth."

    show rin basic_deadpan
    with charaenter

    rin "I'll take curry."

    hide rin
    with charaexit

    "After I receive my soy sauce ramen, I pick up both trays and we set out to search for a table."

    "The cafeteria is crowded. Despite the atrocious food, it seems to be really popular since the atmosphere is really great and almost nobody bothers preparing lunch boxes here."
    
    "Emi seems to be the rare exception and even she opted to get that bread a few days ago."
    
    "I suppose most people couldn't do it anyway, and judging from the amount of different menu items, many people need special diets for… whatever."

    "Although almost all tables are full, the table closest to the entrance is for some reason occupied by only one student."

    "It's Hanako, already set her tray aside and reading a paperback book."

    hi "Are these seats free?"

    show hanako defarms_shock at centersit
    with charaenter

    "I clearly startle her badly, as she looks up from her book with an expression of mixed surprise and terror."

    show hanako emb_timid at centersit with charachange    
    
    ha "Aah… I guess… they are."

    show hanako emb_blushing at tworightsit
    with dissolvecharamove

    show rin basic_absent at twoleft
    with charaenter

    rin "Oh, it's the toilet gi—{w=0.2}{nw}" #reminder for the potential {nw} break

    show rin basic_surprised at twoleft
    show hanako emb_timid at tworightsit    
    with charaenter

    "I make a nice display of dexterity, dropping my own tray on the table and pressing a hand against Rin's mouth, trying my best to force a natural smile on my lips to calm down Hanako."
    
    show rin basic_awayabsent at twoleft with charachange
    
    "Even still, she looks positively alarmed."

    hi "You don't mind if we sit here?"

    show hanako emb_blushing at tworightsit
    with charachange

    "She looks at Rin who is looking at the ceiling absentmindedly and fidgets nervously with her hair, looking even more frightened."

    ha "No, it's not like that… please, go ahead."

    show hanako emb_blushtimid at tworightsit with charachange

    "She's not all that convincing but as the cafeteria is so crowded, we have little choice but to intrude upon her."

    show rin basic_absent at twoleftsit with dissolvecharamove
    
    "I sit down on the same side as Hanako while Rin seats herself opposite of me."

    "As I set Rin's tray in front of her, she pushes her chair away from the table and puts her feet on top of it."

    "Of course, why didn't I see this before? This is why she prefers not to have lunch at the cafeteria, eating here is problematic for her."

    show hanako emb_downtimid at tworightsit with charachange

    "Hanako immerses herself in the book again while we dig in the food. As expected, it's not much to speak of, but it's hot and fills the stomach."

    show rin relaxed_doubt at twoleftsit with charachange
    
    "I glance around the cafe while we eat, looking at my new schoolmates."

    "Hanako moves her lips while she reads, turning the pages at a slow pace. To her left, Rin looks disgusted at her lunch."
    
    show hanako emb_downsmile at tworightsit with charachange
    
    ha "Why are we here?"

    "She speaks so quietly that at first I'm not sure she spoke at all, but Rin, raising her eyes to look at Hanako seems to confirm it."

    show rin relaxed_surprised at twoleftsit with charachange
    
    rin "Because we are hungry."

    show hanako def_shock at tworightsit with charachange
    
    "Hanako starts."

    ha "A… aha.. no, I was just talking to myself. Please don't mind it."

    hi "Because we have to."

    show hanako cover_distant at tworightsit with charachange
    
    "Rin picks up another spoonful of the thick curry and chews it before answering."

    show rin negative_spaciness at twoleftsit with charachange
    
    rin "You've not been in a place like this before, right? So this is a new place to you. Do you think it is a good place?"

    "She is very direct. Despite the weird way that Rin asks her question, the green eyes focused directly on me catch me off guard, making me answer straight."

    "I think for a fraction of a second about my first week here."

    "It's been only a week but I already feel much less of an outsider here than at my previous high school, but I don't think that I “belong,” either."

    hi "I don't know. I don't really think of myself as a disabled person, in a loose meaning of the word. After all, my arrhythmia doesn't affect my everyday life that much."

    "Before coming here, I didn't even know anyone else who was disabled. It's not like I view disabled people any differently than others, I just didn't happen to know anyone."

    "The only thing I have trouble with is discussing the disabilities, and in this school you can't really avoid it."

    "I think I'm just too sensitive to that kind of stuff; almost everyone is pretty comfortable with the topic."

    "Then again, most of the people here have been living with their disabilities for most of their lives, unlike me."

    show rin basic_deadpancontemplation at twoleftsit with charachange

    rin "Same for me. I've been me for all my life and it's not much of a problem so far. Still, people think I am not me, they think I have no arms."

    hi "But you don't—{w=0.2}{nw}" #reminder for the potential {nw} break

    show rin negative_annoyed at twoleftsit
    with charachange

    rin "You too, toilet person."

    show hanako basic_worry at tworightsit with charachange

    "Hanako glances up from her book at Rin, who is pointing at her direction with her spoon."

    "She definitely looks like she doesn't want to be dragged into this conversation."

    show hanako emb_timid at tworightsit
    with charachange

    ha "Eh…?"

    show rin negative_spaciness at twoleftsit
    with charachange

    rin "Your problem is not that severe either, compared to some of the people here. For example, that one girl."

    ha "Who?"

    show rin basic_awayabsent at twoleftsit
    with charachange

    rin "You know, that girl. Nana."

    show rin basic_absent at twoleftsit
    with charachange

    rin "The second year with wavy hair and a really hard last name."

    show hanako emb_blushtimid at tworightsit
    with charachange

    "Hanako nods weakly."

    hi "No, I don't think I know who she is."

    show rin basic_deadpancontemplation at twoleftsit
    with charachange

    rin "She's a blind girl who also has parapl-something. But that's not important. Well, it is for her, but not for us."

    rin "What is important is that she has a lot of trouble doing easy things by herself, while we can do difficult things."

    show rin basic_deadpanupset at twoleftsit
    with charachange
    
    rin "Don't you think it's weird for us to be in a place like this?"
    
    show rin negative_spaciness at twoleftsit
    with charachange
    
    rin "Not this cafeteria, it's fine because at least I am hungry. Don't know about you."
    
    show rin negative_worried at twoleftsit
    with charachange
    
    rin "So do you? And I don't mean hungry."

    show hanako defarms_worry at tworightsit
    with charachange

    "Rin doesn't direct her words to Hanako, but since she is staring at her direction, Hanako starts to stutter alarmingly. I save her by cutting in before she bursts in tears."

    hi "I understand where you are coming from. But do you really see this school as some kind of asylum where people are sent away?"

    hi "If it was not for this place, I could never attend school and it's probable that you'd have some problems as well going to a normal school. Is it the same for you, Hanako?"

    "She stares at me with a bewildered expression, looking like she wants to run away."

    show hanako defarms_strain at tworightsit
    with charachange

    ha "I … I don't…it's not like that at all…"

    show hanako emb_timid at tworightsit
    with charachange

    "Hanako's voice fades away without her actually saying anything. I feel sorry for dragging her in right after I tried to keep Rin from interrogating her."

    show rin basic_awayabsent at twoleftsit
    with charachange

    "I lean my cheek against my hand and idly stir my cooling ramen with the chopsticks."
    
    "To my pleasant surprise, I find that I have learned to make sense of Rin's crazy nonsense a little better."

    "Discussion is a good diversion from the inedible food, but Rin's antagonism towards her school and fellow students is unexpected."

    hi "Well, people are prejudiced, that's true. I have noticed that people look at me funny when I go to the town in school uniform."

    hi "But, aren't you also being prejudiced in saying that people judge us based on outward appearances?"

    show rin basic_absent at twoleftsit
    with charachange
    
    hi "If you see a person in a wheelchair, isn't it only appropriate to assume he has trouble doing certain things?"

    "Not that I know anything of that since I look like a healthy person on the outside."

    show rin basic_deadpan at twoleftsit
    with charachange

    rin "Do you think I can paint or use chopsticks?"
    
    show rin basic_deadpancontemplation at twoleftsit
    with charachange
    
    rin "Not now, previously. When you had no idea who I am."
    
    show rin basic_deadpanupset at twoleftsit
    with charachange
    
    rin "No, I mean in between those. Somewhere there."

    "She is swinging her spoon above the tabletop defiantly."

    "I have no retort for that."

    hi "Point taken."
    
    show hanako emb_timid at tworight
    with dissolvecharamove
    
    "Hanako closes her book quickly and stands up, picking up her tray."
    
    ha "Excuse me… I promised Lilly… ah, Satou, I would see her before the afternoon classes."

    show rin basic_deadpannormal at twoleftsit
    with charachange

    rin "Don't mind us. It's not like you were much of a company and we disturbed you anyway."

    show hanako def_shock at tworight with charachange
    
    "Hanako is visibly taken aback by Rin's straightforwardness. Not knowing how to react, she just blinks a few times and leaves without saying anything."

    show hanako invis at right
    with dissolvecharamove

    show rin basic_awayabsent at twoleftsit
    with charachange

    "I'm not finished with my food but it's not like I feel like finishing it either."

    "I try to chew some soggy and stale noodles unenthusiastically, but the taste is enough for me to push the bowl aside."

    "Rin has eaten even less than me. Her plate of curry looks like it hasn't been touched at all."

    "Maybe such insignificant things as nutrition are low on her list of priorities."

    "Whatever they are."

    show rin basic_deadpan at twoleftsit
    with charachange

    rin "I'll go too."

    show rin basic_deadpannormal at twoleft 
    with dissolvecharamovefast

    "She abruptly stands up and turns away to leave. Maybe she's really had enough."

    hi "Hey, wait!"

    show rin basic_deadpansurprised at twoleft 
    with charachange
    
    rin "Why?"

    hi "I meant to ask you about the art club. It's today, right?"

    show rin basic_deadpancontemplation at twoleft 
    with charachange
    
    rin "Probably. Today is a Thursday."

    show rin basic_deadpandelight at twoleft
    with charachange

    rin "Thanks for taking my tray away."

    show rin invis at left with dissolvecharamove

    stop music fadeout 4.0
    stop ambient fadeout 4.0
    
    "With that, she goes, leaving her tray for me to clean up. What a bothersome girl."

    window hide dissolve
   
    scene black
    with Dissolve(1.5)
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    return

label en_R7:

    scene black
    with Pause(1.5)
    play sound sfx_alarmclock
    with Pause(1.0)
    scene bg school_dormhisao
    with openeye
    window show dissolve

    #reminder for me to add Emi inviting Hisao to this event somewhere in R1-R5, since the date has been changed a couple of times

    
    "{a=ismuth_R6_AuratoAura}I wouldn't have minded sleeping a bit more.{/a}"
    
    play music music_another fadein 1.0

    "To my dismay, the alarm clock sounds at 10:00 sharp, although the only one I can blame for setting it to wake me up is myself."

    "However, a promise is a promise. I slip from the bed to the cold floor and draw the curtains open to be greeted by too bright sunlight."

    "The wonderful weather seems to have set permanently on this town, not that I would complain."
#<Unlike what he's doing, which only looks like complaining to the untrained eye.>

    "Clothes."

    scene bg school_dormbathroom with delayblindsfadesilent
    
    "Toothbrush."

    "Cold water." with delayblindsfadesilent

    scene bg school_dormhisao with delayblindsfadesilent
    "Breakfast."
#<wait what? I feel as if I, the reader, have just been tossed around.>

    play ambient sfx_crowd_outdoors
    scene bg school_courtyard
    show crowd 
    with locationskip
    
    "The other students don't spend their free days sleeping late either."
      
    "Girls and boys in their casual clothes lie around in the gardens or walk towards the main entrance of the campus in twos and threes to spend a day in town."

    "However, most of the students are moving towards the sports field. I follow a bunch of underclassmen walking past the Great Hall and dormitories."

    "A large crowd has gathered around the running track, some filling the bleachers, others bunched around the starting line in small groups."

    "There are students from two other schools in this town attending the meet, although both of them are just normal high schools."

    "People seem to be in high spirits today, and why wouldn't they?"
    
    show bg school_track
    with locationchange

    "The competitors are stretching their muscles to prepare for the contests, while others are mingling and chattering with each other."

    play sound sfx_pillow
    with vpunch
    
    "As I wonder where I could find Emi, someone slaps my back with considerably more force than needed to get my attention."

    "I turn around on my heels to find the very person I was seeking."

    show emi basic_happy_gym 
    with charaenter
    
    emi "Good morning!"

    "She looks strange. Her matte-black carbon fibre running blades make her look like… Well… " #extended here
    extend "Half a robot."

    "Emi is standing proudly with her hands on her slim hips holding her head high, although that is because she still has to look up to see my face even though she's a good two inches taller than usually."

    hi "Good morning. It seems I didn't make it to the start, but here I am anyway. Have you already run?"

    show emi excited_smile_gym with charachange
    
    emi "We were fourth in the 400m relay!"

    "It looks like I asked the right question. She obviously was bursting to say something but waited me to ask and now she breaks in even wider smile, announcing her success."

    show emi excited_joy_gym with charachange
    
    emi "And I was second in the 200 meter dash!"

    "Her voice becomes a notch louder so I have to bring her back to earth."

    hi "Really? Of how many runners?"

    show emi excited_hesitant_gym with charachange
    
    emi "Of eight, of course."

    hi "Oh, I thought there might have been fewer participant teams, for instance; two?"

    "Her face drops instantly to horrified anger when she realises I'm teasing her. I can almost see steam coming out of her bright red ears."

    show emi sad_pout_gym with charachange
    
    emi "Whaaat? Hisao, you should not underestimate my powers!"

    "She wags her index finger at me in a scolding manner. I hold my hands up to appease her."

    hi "Sorry, sorry. Just kidding. Are you going to participate in other contests or did I miss my chance to see you in action completely?"

    show emi basic_grin_gym with charachange
    
    emi "Nah, I'm going to run in the 100 meter dash later. Will you stay and watch?"

    hi "Sure. I'll be cheering for you."

    emi "Rin is somewhere there in the audience, you should try to find her so she won't be all alone."

    hi "Ok, I'll look and see if I can find her."
    
    hide emi with charaexit
    
    "Emi skips off towards the gym and I walk to the bleachers, searching for Rin with my eyes."
    
    show bg school_track at left 
    show crowd at left
    with dissolvecharamove

    "Finally I spot her in the top rows of a section where there are still a few free places."
#<This just read really funky with 'the section'>
    show rin basic_awayabsent behind crowd with charaenter
        
    "The crowd is thick and I have to work my way through the crowd to get to the stairs and then to Rin."
    
    hide crowd with charaexit
    
    hi "Good morning"

    show rin basic_absent with charachange
    
    rin "Oh, hello, Hisao. You are here. Or there, but I guess you are close enough to be called here."

    hi "You took the words out of my mouth. Is this seat free?"

    "I point at the seat next to her."

    show rin basic_surprised with charachange
    
    rin "I don't see anyone sitting there, do you?"

    hi "No."

    show rin basic_deadpanamused with charachange
    
    rin "Oh, that's good. You got me worried for a while. I don't see anyone either, so it must be free."
    
    stop music fadeout 2.5
    
    "Sometimes, I wish I could converse with Rin in a manner that would not make me feel incredibly stupid."

    hide rin with charaexit
    
    play music music_ease fadein 2.0
    
    "I sit on the obviously vacant seat and lean back, trying and failing to find a comfortable position on the hard wooden bench."

    "We watch the boys run 400 metres and then 200 metres without trading another word."

    "The audience are cheering on them, waving their hands, whistling and yelling to their heart's content."

    "The runners are chasing each other around the track, each striving to beat the others."

    "Rin and I sit and wait, watching all this, in silence."

    "Slowly, the palpable feeling of time slowing down envelops Rin, me, and the entire running track in its embrace."
#<It can't be without him noticing if he's noting it in his inner narrative.>

    stop ambient fadeout 4.5
    
    "{a=Rewrite}As we sit there, both lost in our thoughts, even the loud din of the crowd and the cheers spurring on their favourites seems to no longer reach my ears and the silence between me and Rin expands to cover the entire crowd.{/a}"
#<While I think that my edits are functional, I wouldn't mind seeing some rewriting of this whole blurb.>

    "More than hear, I can feel the heartbeats in my chest."

    "I've never been doing sports and PE is my least favourite subject so I've always been detached from this world. I don't even like watching sports from TV that much."

    "Now that I have this condition, any chance of doing sports is more or less gone. Not a big loss."

    "…"

    rin "To tell you the truth, this kind of thing is not really my scene."
#<Yo?>

    show rin basic_awayabsent with charaenter
    
    "Rin is echoing my sentiments from just a moment ago. I turn to her, but she seems to not have noticed this coincidence herself."

    "She is leaning casually against the legs of the person sitting behind her, her expression somewhere in the no-man's land between bored and nonchalant."

    hi "Figures, I didn't think you had much of a sports fan feel to you."

    show rin basic_absent with charachange
    
    rin "I didn't think so either."

    hi "So why did you come to watch the meet then?"

    "I ask it more out of courtesy than curiosity. It's not particularly hard to guess why Rin would be here."

    rin "I wanted to see Emi."

    hi "You want to cheer on her?"

    "She considers her answer for an annoyingly long moment."

    show rin basic_deadpanamused with charachange
    
    rin "She doesn't need cheering. I came to watch her."
    
    rin "I went to the forest this one time… and… oh, that doesn't mean I have been there only once, I go up there often."
            
    stop music fadeout 2.0
    
    rin "And then… where was I going?"

    hi "To the forest."
    
    play music music_rin

    rin "Oh yeah, I found a butterfly cocoon. It could have been some other thing too since I can't tell one kind of a cocoon from another but let's say it was a butterfly."
    
    show rin basic_absent with charachange
    
    rin "I thought I'd watch it hatch because it'd be nice to see. So I did. But you see what I'm getting at is that it didn't need me watching."

    rin "To hatch."

    show rin basic_deadpancontemplation with charachange
    
    rin "It would have done it anyway."

    "Rin's stories are always a bit far out, but if she wasn't into painting, she could try this as a career."

    rin "I know that, because in the end I got bored and left. The next day the cocoon had hatched, without me watching."

    hi "You probably should have left that bit out."

    show rin basic_absent with charachange
    
    rin "Probably?"

    hi "Definitely."

    show rin basic_lucid with charachange
    
    rin "You could be right. Anyway, that's the way it is. Us normal people are not like them."

    "“Us?”"

    hi "Who?"

    show rin basic_absent with charachange
    
    rin "Emis. Butterflies. Feelings are not easy."

    hi "I don't follow… do you mean she uses sports… err… to come out of a figurative cocoon?"

    "Like self-expression of sorts? Well, I guess it makes sense, that's what hobbies are for after all."
    
    "Then again, Emi doesn't seem to have trouble being herself, so to speak. She's always cheerful and outgoing."

    "I never got into anything special, although I have tried a number of hobbies when I was younger."

    "Nothing just caught my interest in the long term."

    show rin basic_deadpandelight with charachange
    
    rin "Emi doesn't have legs, but she is the best runner in the school."

    "I get the feeling that part of the conversation was left out in the middle, or happened only inside Rin's head, but at least we can continue from here easily."

    hi "Ok, I get what you are saying."

    "For a change."

    hi "{a=Rewrite}Still, even though she might have beaten her amputation, the reality is that she, like all the students here lead harder lives because of whatever their problem may be.{/a}"
#<You should rewrite this sentence to either focus on Emi, or 'all students here'. You changed your subject midsentence.> -- Kind of fixed and reconjugated, TcDohl

    show rin basic_awayabsent with charachange
    
    "Rin doesn't have anything to say to that."

    "She draws her knees to her chest and drops her chin on top of the knees, curling her thin body tightly into itself."

    "I can't help wondering what is she trying to protect herself from."
    
    rin "I wish I could do it like Emi. All she has to do is to run."

    hi "Now you lost me completely. Aren't you a painter? I always thought art is considered as a high form of self-expression."

    hi "Can't you like… I don't know… put your feelings onto the canvas? I mean… well, that was a bit awkward but you get what I mean."
    
    rin "Would anyone know if I did?"
    
    show rin basic_absent with charachange

    "Rin turns her head to look at me, resting her cheek on her kneecaps. Her eyes betray a hint of something unusual, but I couldn't say what."

    rin "When you saw something I had done, did you think of what feelings I had put into the painting, as you said? What did you think?"

    "That it was amazing how she painted all that with just her feet."

    "I hang down my head in shame."

    hi "I see what you are getting at."

    hi "But still, how can you be so sure that people will not view your art objectively? It sounds like you are a bit paranoid about it."

    show rin basic_awayabsent with charachange
    
    "I feel filthy for preaching to her like this, even though I am guilty of the same infringement."
    
    "I don't want to admit it to her, but yes, even now I usually marvel at her deftness at using her feet rather than her art in itself."

    "I don't even understand art really, so in the end it wouldn't be any use even if I tried to put some deeper interpretations to it, when I know I can't?"

    "Besides, Even though we are not strangers anymore, I can't really say that I know Rin at all."

    "She never speaks of herself in a meaningful way, most of what comes out of her mouth tends to be irrelevant nonsense."

    "Feelings might not be easy to convey in any way, especially something like art, but—{w=0.5}{nw}" #reminder for the potential {nw} break

    show rin relaxed_nonchalant with charachange

    rin "Me and Emi are not like you. They can't see the things that are wrong with you."

    "She lifts her empty sleeve limply."
       
    rin "It's not the same."

    "The comparison is like a slap across the face. I would never have thought Rin at all self-conscious about her disability, not with the ease she manages everyday life."

    "I thought Rin was as nonchalant with her disability as she is with everything. Pretty presumptuous of me, now that I think about it."

    hi "But you just said you envy Emi for overcoming her disability. Aren't you just the same, doing that instead of just admiring how good at she is at running?"

    show rin basic_absent with charachange
    
    rin "You don't understand."

    hi "No?"

    show rin basic_deadpan with charachange
    
    rin "Seriously. You must clear the wax from your brains."

    hi "My ears."

    rin "What?"

    hi "My ears. You clear wax out of your ears, not brain."

    show rin basic_deadpancontemplation with charachange
    
    rin "Maybe I do, but you have to clear it out of your brain."
#<[21:58:02] <GAR> lol pwnt <--- I agree. Awesome.>

    hi "That's not what I meant… wait, I didn't even agree with your insult in the first place."

    show rin basic_deadpannormal with charachange
    
    rin "Then you should have said so instead of starting to argue the semantics. Besides, it wasn't an insult, it was a statement."

    hi "So are you going to tell me what I misunderstood?"

    "She looks at her toes, perched on the edge of the seat, and wiggles them. She is not wearing socks or sandals."
    
    rin "I can't explain it, no that's not right, I can but I can't really explain it, so I won't."

    hi "But…"

    show rin basic_absent with charachange
    
    rin "What?"

    hi "Nothing."
    
    hide rin with charaexit
    
    stop music fadeout 2.0

    "After I give up the conversation as pointless, the boys run the 800m competition as the sun climbs higher and higher."

    "It's scorching hot and I feel sweat flow down my temples, but I bet the people at the track are even worse off."

    "The announcer calls for the competitors of girls… 100m dash. The start line is on the far side, looking from us, but it's not hard to spot Emi jumping up and down at her spot."

    "The last runner is jogging across the field towards the starting place so the competition can start."

    scene ev emitrack_blocks at Fullpan(12.0, dir="left") 
    with locationskip
    
    "I see the girls taking their places. Emi crouches at her starting blocks like a spring pressed together, carefully placing her blades against the blocks."

    #announcer could be centered as opposed to a character maybe

    window hide dissolve
    centered "On your marks."
    play sound sfx_flash
    scene ev emitrack_blocks_close 
    with flash
    window show dissolve
    
    "Tension is building up as the announcer points his gun towards the clouds drifting overhead. Even the previously nonchalant Rin tenses up and leans forward."
    window hide dissolve     
    #These could be separated for effect, with starting pistol sfx or whatever?
    
    play sound sfx_flash
    scene ev emitrack_blocks_close_grin
    with flash
    
    
    centered "Ready!"
     
    show startpistol at right 
    with easeinright
       
    
    centered "Set! "
        
    play sound sfx_startpistol
    
         
    centered "Go!"
    
    play ambient sfx_emisprinting
    play music music_emi fadein 0.5

    scene ev emitrack_running at Fullpan(3.0, dir="left") 
    with flash
    
    window show dissolve

    "As the starting pistol bangs, the tension built in the competitors is released in a single burst of eight girls simultaneously springing from the starting blocks."

    "Emi gets off to a slower start than some of the girls, she is third or fourth, I think. It's hard to say because they are very close to each other."

    "As the girls sprint towards the goal line, Emi increases her pace."

    "Every step becomes longer than the previous; every step brings her closer to the girls in lead."

    "She passes one, no, two runners, leaving only one girl ahead of her, leading Emi by a bit."

    "There is precious little distance to the goal line and Emi is catching on the leading girl but it looks like she won't make it."

    show ev emitrack_finish with flash  
     
    "Amazingly, Emi seems to still be able to notch the gear up."
         
    show ev emitrack_finishtop with flash
    play sound sfx_crowd_cheer
    stop music fadeout 12.0
    stop ambient
    "She practically flies the last twenty meters, leaping across the finish line as the clear winner."

    "As Emi slows down her steps seem somehow unsteady, limping as if she is hurt, but she doesn't falter."

    "She greets the crowd with a wave of hand and a wide smile, as if she was the world champion."
    
    stop sound fadeout 14.0    
    play ambient sfx_crowd_outdoors fadein 14.0
    play music music_normal fadein 2.0
    show bg school_track
    show rin basic_deadpanamused
    with locationchange
    
    rin "Did you notice it?"

    hi "What?"

    show rin basic_deadpan with charachange
    
    rin "Nevermind."

    rin "It's good that she is such a good runner, since she is at a disadvantage."

    hi "Yeah, I guess prosthetics are not as good as normal legs after all. It was a close race."

    show rin basic_surprised with charachange
    
    rin "What? No, she needs to get her chest across the finish line to win. Looking at the other girls, it seems that she could have trouble winning."

    hide rin with charaexit
    
    "I don't have time to get flustered, as Rin suddenly stands up and walks past me."

    hi "Where are you going?"

    show rin basic_absent with charaenter
    
    rin "Do you want to stay?"

    hi "Is there anything else to see?"

    show rin basic_awayabsent with charachange
    
    rin "Suit yourself."

    hide rin with charaexit
    
    "She turns again and descends the steps to the ground level, one at a time."

    "I watch her go, lingering between the decision to follow or to stay."

    "I try to suppress a yawn, but it comes out as a sigh anyway. I feel lazy, and the sun is shining so brightly too…"

    "Oh well."

    "I balance my way past the other spectators and walk to the same direction Rin left to."

    show crowd
    show emi basic_grin_gym behind crowd at tworight
    with Dissolve(2.0)
       
    "Emi is surrounded by her teammates and other students patting her back and congratulating her."
    
    "It's hard to see her since she is so short, but she undoubtedly is in the center of attention."

    "I don't feel like breaking into the circle of people, so I stand there, waiting."

    show rin basic_awayabsent at twoleft with charaenter
    
    rin "Are you waiting for sky to fall down?"

    "Rin walks up to me from behind, which is very strange, since I didn't notice passing her."
    
    hide rin with charaexit
    
    "Without even looking at me, she pushes her way past a few second year girls to Emi."

    show rin basic_absent behind crowd at twoleft with charachange
    
    "I take advantage of the opening she created to get through as well."
    
    hide crowd with Dissolve(2.0)   
    
    show emi basic_closedgrin_gym at tworight with charachange
    
    "Emi notices us and smiles to our direction. She says something to Rin but I can't hear what."

    show rin basic_amused behind crowd at twoleft with charachange
    
    "Rin keeps quiet, just glances upwards amusedly, as if giving a secret sign."
    
    show rin basic_deadpannormal at twoleft with charaenter
    
    "I'm not the only one to catch it, as Emi stops midway her sentence and turns again to finish her conversation with some other people."
        
    show emi sad_annoyed_gym behind crowd at tworight with charachange
    stop ambient fadeout 5.0    
    "The folks dissipate quickly since the meet is still going on, leaving us three standing by ourselves."

    "Emi seems a bit anxious about something. To the outside, she is smiling like the sun, but something is so obviously wrong that even I can notice."
    
    play sound sfx_pillow
    show bg school_track with vpunch
    show emi sad_angry_gym at tworight with Dissolve(0.2)
    hide emi with charamoveoutbottom 

    #Originally she *almost* fell down, but actually falling down looked better. - Kelper    
    "When she takes a tentative step towards Rin she winces and goes out of balance, falling down."
    
    show rin relaxed_doubt at twoleft with charachange
    
    rin "You should not push yourself. Getting hurt is not a good thing, Emi."

    show emi basic_closedsweat_gym at tworight with charamoveinbottom
    
    "Emi stands again and smiles sheepishly, shrugging it off."

    hi "Did you hurt yourself?"

    show emi sad_depressed_gym at tworight with charachange
    
    emi "It's okay, not a biggie. It is like this always when I run a lot. It's the prosthetics."
 
    show emi basic_grin_gym at tworight with charachange
    
    emi "Anyway, I really should have practiced more, at least this week. Did you see how close it was?"

    show rin basic_deadpan at twoleft with charachange
    
    rin "Does it matter?"

    show emi basic_happy_gym at tworight with charachange

    emi "Yeah… mean, I guess not."

    emi "Thanks for coming, Hisao. It gives a little extra speed to know someone is cheering on me."

    show rin basic_deadpanamused at twoleft with charachange 
    
    show emi excited_happy_gym at tworight with charachange
    
    emi "Listen, would you want to come to celebrate with me and Rin next weekend? We would go today but

    I have to go see the Nurse and then there is a huge pile of homework we have to do."

    show emi basic_annoyed_gym at tworight with charachange
    
    emi "The teachers have been really nasty all week, have you noticed? Giving homework at least twice the usual amount. It's really mean. I bet they are conspiring against us."

    "She clenches her fist in subdued rage, as if the homework was somehow the end of the world."

    show emi excited_proud_gym at tworight with charachange
    
    emi "Would it be okay if Hisao came along, Rin?"

    show rin basic_awayabsent at twoleft with charachange
    
    "Emi's babbling almost made me forget that Rin was actually present. She looks away, to the direction of the gardens."

    rin "I don't mind."

    "Emi breaks into a wide smile."

    show emi excited_laugh_gym at tworight with charachange

    emi "Then it's settled! I'll go take a shower and meet the Nurse now. Will you come with me?"

    show rin basic_deadpandelight at twoleft with charachange
    
    rin "Good."

    emi "See you later, Hisao!"

    hi "Yeah…bye…"
    
    hide rin
    hide emi
    with charaexit
    
    stop music fadeout 2.0

    "I don't think Emi asked anyone else other than Rin if I wanted to come along."
    
    
    window hide dissolve
    scene black with Dissolve(1.5)
           
    return


label en_R8:

    scene bg school_scienceroom
    with locationskip
    window show dissolve
    play music music_tranquil fadein 2.0

    "I make it to the class in time, although my head feels like it's seen the business end of a sledgehammer."

    "Spending the classes balancing between studying and grinding my teeth together to lessen the pain makes me wish that I had just stayed in my room for today."

    show bg school_scienceroom with shorttimeskip
    
    "To my relief, the headache slowly leaves as the day passes. By afternoon classes it is but a memory."

    "One second at a time, the hands of the clock move towards the inevitable liberation."

    play sound sfx_normalbell

    "Not a moment too soon, the bells at the clock tower call for the end of the school day."

    "Mutou raises his head from the notes he was reading and glances at the clock, as if the end of the class comes as a surprise to him."

    show muto normal with charaenter
    
    mu "That's all for today, everyone. I want you to read chapter 6 before the next lesson and that's it. Off you go."

    "I collect my stuff and throw it in my bag."

    "There is no need to hurry since the classroom used for art club meetings is just across the hall."
    
    scene bg school_classroomart
    with locationskip

    #scene change to art classroom

    "Nomiya's extravagant entrance is less intimidating today, now that I know to expect it."
    
    play sound sfx_dooropen 
    $ renpy.pause(1.0)
    play sound sfx_doorslam 
    with vpunch

    "The teacher practically bursts through the door, carrying a wooden box of supplies and a pile of fresh paper."
    
    "He seems to be exceedingly happy about something, a rare occurrence for a teacher."

    show nomiya veryhappy with charaenter

    no "Good afternoon! If I may have your attention now, everyone! It's such a beautiful day today so I thought we could explore the school grounds."

    play sound sfx_impact2
    with vpunch 
    
    "To emphasize his exclamation, Nomiya slams the box on the teacher's desk so vigorously that several pencils fly all over the place."

    show nomiya talk with charachange
    
    no "I'd like you to continue using only graphite for today's assignment as well to polish your technique."

    "The teacher is literally excreting enthusiasm, maybe in the hopes that some of it will stick on us."

    show nomiya smile with charachange
    
    no "I'm sure you all found something to improve on last week."

    no "So, everyone take some graphite and paper and move outside."

    no "The subject for today is realistic illustration of vegetation, so pick any place you wish and draw the trees and bushes you see with as much detail as possible."

    "Seems like it's going to be a pretty lax club meeting."

    "We can relax outside and practically do whatever we want."
    
    "This is my kind of a club."

    show nomiya talk with charachange
    
    stop music fadeout 6.0
    
    no "Let's go then, we have the usual two hours. I'll be walking around so you can ask for tips and advice. Remember to return here before five o'clock!"

    "We follow him outside and everyone splits up to go on their own ways."
    
    scene bg school_courtyard
    with shorttimeskipsilent
    
    play ambient sfx_park 
    play music music_soothing fadein 2.0
    
    "The teacher was right, it's a gorgeous day."

    "Even though it's already afternoon, sun seems to be high up in the sky, shining brightly upon the school."

    "The air is still, barely managing to move even the most slender sprigs in the cherry trees around the walkways."

    "I'm about to leave to the gardens, the most obvious place to go to, when I notice Rin standing in the middle of the quadrangle, looking terribly bothered."

    show rin relaxed_sleepy with charaenter
    
    "She is rooted in her place like some odd marble statue that has been left there by a forgetful sculptor."

    "Her shoulders are drooping pensively, as is her head."

    "Nomiya and everyone else have already disappeared from the scene, leaving only us two here."

    hi "Is something wrong?"

    "I realize I am talking to her only after the words escape from my lips."

    "Concern is such an automatic reaction to distress of others that my common sense dissolves completely, keeping me from leaving Rin alone."

    show rin relaxed_nonchalant with charachange
    
    "Rin wakes from her thoughts and looks up, but not at me."

    "She keeps staring at something in front of us that only she can see."

    show rin relaxed_surprised with charachange
    
    rin "No, nothing."

    hi "Then why…"

    show rin relaxed_doubt with charachange
    
    rin "That's a strange question, don't you think? Things can never be right or wrong. They just are what they are."

    "A strange thing to say."

    "Maybe that would be the perspective of a total outsider."

    "But for anyone who actually experiences these “things,” it's impossible to avoid having some kind of a stand on matters that concern you."

    "Her question bothers me, but I don't know what to say to her."
    
    "Maybe Rin thinks of herself as someone who only observes life, instead of participating in it?"

    "I remember that I used to think so, in a way. But I managed to change, even if it was just a little bit, and only because I got sick like this."
  
    "{a=Rewrite}I shake my head rigorously to snap out of my silly contemplations and focus on the matters at hand.{/a}"
#This is kinda awkward, and I don't wanna just simplify your language everywhere I go lol.
   
    stop music fadeout 5.0
    
    hi "So, what's your problem with the state of things? Can't decide where to go to draw?"

    "She looks at me, her dark eyes wide with surprise."

    show rin basic_surprised with charachange
    
    play music music_rin fadein 1.0
    
    rin "How did you know?"

    hi "What… I just thought you looked like it. A lucky guess."

    "A tiny smile appears in her eyes, but her lips remain strictly horizontal."

    show rin basic_amused with charachange
    
    rin "{a=ismuth_R8_Points}You really are good at guessing.{/a}"

    hi "I guess I am."

    show rin basic_absent with charachange
    
    "…Come on."

    "Trying to be funny is utterly lost on Rin."

    "She doesn't even crack a smile, to my great dismay but to nobody's surprise, realistically speaking."

    hi "Let's go find some place."

    show rin basic_deadpancontemplation with charachange
    
    rin "How does one find a place?"

    "Her questioning face matches my inner confusion, but I figure we are uncertain of directly opposite matters."

    hi "The same way you find anything else."

    show rin basic_awayabsent with charachange
    
    rin "From the last place you look? I don't think that would work in this situation since I am looking for a place."

    show rin basic_deadpan with charachange
    
    rin "Can places be inside other places?"
       
    rin "I knew that some places exist only between other places, like airports and corridors, but inside?"

    "Her trains of thought are often more like trainwrecks."

    hi "What I meant was that we should just get started with it. Standing around here will accomplish nothing."

    show rin basic_absent with charachange
    
    rin "Oh I see. You want to go together? With me?"

    hi "I figured it would be more fun to work together. That's what the club meetings are for, right?"
    
    "She nods slowly, displaying the kind of unnecessary tentativeness that could easily make one worried about her apparent lack of {a=Note}mental agility{/a}."
    #It's odd. Sometimes Rin has mad mental agility, and sometimes she's a damp match in a dark cave.

    hide rin with charaexit
    
    stop music fadeout 7.0
    
    "As if to contrast her hesitating agreement, Rin abruptly takes off, leaving me standing behind."

    "For the lack of any better idea, I hurry along. Besides, it was me who suggested this."

    "The grounds are vast, and we have a myriad options to choose from."
    
    scene bg school_gardens
    with locationchange

    play music music_ease fadein 2.0
    
    "Unfortunately, none of them seem to be adequate for my finicky companion."

    "She plods through the grounds like a sleepwalker, looking like she isn't even trying to look around for a nice place."
    
    scene bg school_gardens2
    with shorttimeskip

    "We wander from place to place, seemingly picking random directions every time Rin deems our location unworthy of settling down to."

    "After wasting ten, then fifteen minutes on this pointless shuttling around the grounds I really become concerned that there won't be an end to this."
    
    scene bg school_gardens3
    with shorttimeskip

    hi "Hey, what kind of a place are we really looking for?"

    show rin basic_absent with charaenter
    
    rin "A good one."

    "Rin's knack for stating the obvious, while entertaining, does not make for very engaging conversations."

    hi "No kidding? What kind of a place would that be then?"

    show rin basic_awayabsent with charachange
    
    rin "I am not really sure. It just has to give off a good feeling. Like it's a place we want to be at."

    hi "That's a problem then. Where could we go to so that your criteria are filled?"

    show rin relaxed_nonchalant with charachange
    
    "Rin shrugs noncommittally, her attention already having diverted to the small flock of birds flying over the trees sometime between the two last words of my question."

    rin "You decide. I can draw something else."

    hi "Is that really okay?"

    "She considers this for a moment and shrugs again."

    show rin basic_absent with charachange
    
    rin "Probably. I don't really want to do this assignment anyway."

    hi "But I thought you liked doing art."

    "The sound of birds twittering in the trees emphasizes the following silence rather uncomfortably."

    "Rin realises after a second that she needs to explain herself to me so that we can be on the same page here."

    show rin basic_deadpancontemplation with charachange
    
    rin "That's a different thing. This is not interesting."

    rin "I am not interested in things that are not interesting."

    hi "Fine, then let's stay here. I'm not as picky as you are."
    
    scene bg school_greathall
    with locationchange

    "And so, we end up sitting down on a patch of grass next to the Hall, maybe fifty feet away from where we began our little quest."

    "Rin settles herself leaning against one of the cherry tree and kicks off her shoes while I sit down on the grass."

    "She picks the graphite stick between her toes, while pulling the paper in front of her with her other foot and leans back, closing her eyes for a moment."

    "I try to get started with my drawing as well, picking a triplet of tall cherry trees lining the walking path as my subject matter."

    "I start of with sketching the black trunks with a few strong lines and then move on drawing the branches."

    "The wind picks up, rustling the trees pleasantly in a background noise that conveniently prevents my brain from escaping to its own paths."

    "I'm not used to drawing so I have to really concentrate on it."

    "As I draw more and more lines, the cherry trees begin to take shape on the paper, almost magically."

    "I really become absorbed in my drawing, trying my best to push my admittedly meager skill to its limit, something akin like I did last friday before Misha and Shizune ruined the mood."

    "The simple wonder of producing a black line on white paper, something that most people seem to forget after the age of eight."

    "I can't hear Rin moving, so she must still be refusing to complying with the teacher's assignment."

    stop music fadeout 6.5
    
    hi "I still don't get why you don't want to do this."

    "…"

    "She doesn't answer so I raise my head to see if she has fallen asleep or something."

    "Ignoring other people completely is unusual even for Rin, who generally seems to be about as attentive as a lobotomy patient."
    
    play music music_soothing fadein 4.0

    "I flinch at finding her staring straight at me with an empty, inward-looking expression that invokes a mental image of a marble statue, for the second time this afternoon."

    "What little light her dark eyes normally reflect now seems to disappear completely within, as if she doesn't seem to be looking at anything at all."

    hi "Hey?"

    "I wave my hand in front of her to attract her attention."

    hi "Rin?"

    "The lack of any reaction, combined with the hollow, unblinking stare of Rin's is so deeply unsettling that I feel compelled to prod her a little to confirm that she is, in fact, still alive."

    "Rin starts at he contact as if I electrocuted her, but at least she is clearly aware that something happened."

    show rin basic_surprised at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charaenter
    
    rin "Hello."

    "She looks at me like we met for the first time today just now, an expectant and curious stare that makes me feel like she is waiting for me to initiate something fascinating."

    hi "Ah, it's nothing. I just wanted to know why you don't like this assignment."

    show rin basic_deadpanamused at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "I heard you on the first time. I just didn't listen."

    hi "Then…"

    "She doesn't pay attention to my attempt at an interjection, but continues her answer."

    show rin basic_deadpannormal at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "There is art and there is not art. This is not art, it's just drawing. I don't like it that much."

    "Her distinction between the two doesn't make much sense to me. Then again, a lot of things she says don't."

    hi "{a=ismuth_R8_ART}What is art{/a} then?"
       
    rin "It's something that comes from inside of you, not from outside, like feelings."

    show rin basic_deadpancontemplation at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "Other people can't tell you how you feel. It's the same with this."

    hi "Okay, I got it. There is art and then there is everything that is not interesting."
       
    "Rin finishes with a nod as if to confirm my statement and glances at her blank sheet of paper."

    show rin negative_confused at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange

    rin "I had a good idea a few days ago so I'm trying to remember what it was so I could draw that one."

    "I can't help but smile at Rin, the way her passion shines through her nonchalant appearance when it comes to art and the way she is capable of talking for surprisingly long without breathing in."

    hide rin with charaexit
    
    show bg school_greathall at left with dissolvecharamove
    
    "Shaking my head, I set back to work the details of the lush canopies of my half-finished cherry trees."
    
    "I can hear another pencil join mine, and glance at Rin, who true enough has finally started on her drawing as well."

    "Her eyes are again lost in thought, seeing nothing but the piece of paper in front of her and the picture in her mind."

    "Rin seems to be slowly drifting away, back to the mysterious inner world of hers, leaving me all alone to this real one."
        
    "For a while, the sound of two pencils scratching against two sheets of paper is the only disturbance in the stillness of our surroundings."

    "Even the time seems to become lazy, passing at a quiet and slow pace very similar to my snail-like progress with the drawing."

    "A sudden guffaw of laughter somewhere not too far away disrupts my concentration, causing me to look up to locate the culprit."

    "On the other side of the quadrangle Nomiya is talking animatedly with two girls from the club."

    "I see him waving his hand at them, and watch him strolling across the quadrangle to our direction so slowly that it's almost hypnotizing."

    "He gives a wave to us as well as he approaches, but I am probably the only one who notices him."

    show nomiya smile at left with charaenter
    
    no "Well! Aren't you two getting along well?"

    show rin basic_deadpanupset at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charaenter
    
    "The sound of his voice draws Rin back to reality, and she looks up from her drawing, looking somewhat annoyed at the sudden interruption."

    show rin basic_deadpansurprised at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charachange
    
    rin "We are just drawing at the same place, not entirely coincidentally though."

    show nomiya talk at left with charachange
    
    no "Is that so? How are the drawings coming along then?"

    "He looks down to see our drawings and raises her eyebrows in surprise as he sees Rin's drawing which doesn't look like vegetation at all."

    show nomiya talk at left with charachange
    
    no "That doesn't look like vegetation at all."

    show rin basic_deadpannormal at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charachange
    
    rin "Pretty observant, sensei."

    rin "It is a cliff jumping off a person except that that cliffs can't jump, so they are just floating apart like two soap bubbles when someone blows between them just a little bit so that they won't pop."

    "Nomiya stays admirably unfazed in the face of the surprise flood of art babble Rin bursts into."

    show nomiya smile at left with charachange
    
    no "Oh, was the assignment too boring?"

    rin "I'm sorry."

    "The flat tone Rin speaks with is directly at odds with the apologetic answer she gives to the teacher, who doesn't seem to mind in the least."

    show nomiya talk at left with charachange
    
    no "Don't be, I'm happy if you have done at least something."

    "He takes another curious glance towards Rin's drawing, but her feet are in his way."

    no "Can I see it?"

    "Without saying anything Rin pushes her paper across the few feet separating her and Nomiya, who crouches to pick it up."

    "He lifts his tinted glasses on top of his head and scans over the drawing, keeping it at an arm's length and even stretching his neck backwards to add to the distance. It looks strange."

    "Apparently happy with what he is seeing, he glances over the drawing at Rin, smiling genially and raising his eyebrows."

    show nomiya smile at left with charachange
    
    no "A sketch for a painting?"

    show rin basic_deadpandelight at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charachange
    
    "Rin gives the slightest of nods, obviously knowing that the question was merely rhetorical, only reassuring herself even when it's not necessary."
    
    no "I think it looks good, you should go for it if you feel like painting it."

    show rin basic_absent at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charachange
    
    rin "I think I could do it one of these days. Maybe if it's properly cloudy some day."

    show nomiya talk at left with charachange
    
    no "How about you then, Nakai?"

    "He turns to my direction like a vulture preying on a dehydrating victim."

    "I show him my rough drawing, and he looks over it enthusiastically."

    show nomiya smile at left with charachange
    
    no "Hmm hmm. You could try to take a look at the perspective. The proportions seem to be slightly off here and here."

    "He points at several spots on the drawing, but unfortunately I can't see which places he is pointing at because he is holding it away from me."

    show rin basic_awayabsent at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charachange
    
    no "Also try to pay a bit more attention to the shading, it's a very important aspect of graphite drawing, after all. It seems a bit sloppy, perhaps?"

    hi "I'll do my best."
       
    "He returns my paper to me and turns back to Rin, who already has lapsed back into fixatedly observing the way the grass blades sway gently in the light breeze sweeping over the quadrangle."

    "She even sways back and forth in the same rhythm herself."

    show nomiya talk at left with charachange
    
    no "Listen Rin, have you given any thought to that matter we talked about last week?"

    show rin basic_absent at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charachange
    
    rin "A little."

    "Despite her nonchalant tone, Nomiya's lips curve into a smile."

    show nomiya smile at left with charachange
    
    no "And what do you think?"

    show rin negative_worried at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charachange
    
    rin "I don't know. I don't like it."

    "Rin being bothered clearly bothers Nomiya. He furrows his brow and smacks his lips unappreciatively."
    
    show nomiya serious at left with charachange
    
    no "Please reconsider it, I think it's a unique and wonderful chance for you and you really should take up on it."

    "Rin wiggles her head to and fro in a way that could be interpreted either as a denial or agreement, or both."

    "I don't have time to pipe up and inquire what the two are talking about, as Nomiya checks his watch and draws in a sharp breath."

    show nomiya smile at left with charachange
    
    no "Heavens, look at the time. Come on you two, we must hurry back to the classroom."
    
    scene bg school_classroomart
    with locationskip

    stop ambient
    
    "Most of the club has already gathered at the third floor classroom, sitting idly on the desks and talking about whatever."

    show nomiya smile with charaenter
    
    "Nomiya rubs his hands together gleefully, obviously satisfied at the sight of his disciples piling the products of today's meeting on the teacher's desk."

    no "Well done everyone, we'll see again on Thursday."

    "With one last smile, he sends us off."
    
    stop music fadeout 2.0
    
    window hide dissolve
    scene black
    with Dissolve(1.5)

#label en_R9:



 #   return

label en_R10:
    
    scene black with locationchange
    scene bg school_scienceroom
    with locationchange
    
    window show dissolve
    play music music_pearly
    
    #"I try to push away the heavy thoughts clouding my mind while climbing the stairs to the third floor."

    "The cloudless sky portends a hot day, making the classes restless." 
    
    "Even the teachers start stealing yearning gazes through the windows at the same rate the temperature rises."

    scene bg school_scienceroom with shorttimeskip
    
    "At lunch hour it's already clear that today is the hottest day for a while, so I stay in the classroom because it's probably the coolest place to be."

    #I took this next sentence off because of continuity. - Kelper
    
    #"Somewhere in the back of my head, the nightmare is still living a life of its own."

    "The day is scorching, the sun shines relentlessly from the cloudless sky. Soon my white shirt is damp with sweat, and clings uncomfortably against my skin, causing my concentration to falter in the afternoon classes."
        
    scene bg school_gate with shorttimeskip
    
    "A humid and hot wind blows against my face on the steps of the main entrance."

    "The heat is almost unbearable, but that's summer for you."

    "It's hard to even think straight, but I know one thing for sure; I need something cold to cool myself down with."

    "The convenience store is not too far off, just down inside the local town. I might just be able to make it there and back again."

    #scene change
    $ renpy.music.set_volume(0.4, 0.0, channel='ambient')
    scene bg school_road
    with locationchange
    
    play ambient sfx_traffic fadein 1.5

    "The road in front of the school is dotted with the occasional tree, their shadows bringing temporary relief when I walk under them."

    "There is always plenty of traffic since the road is a thoroughfare from the district surrounding the school to the west."

    scene bg suburb_roadcenter
    with locationchange
    
    "As always, the sound of an oncoming car is an uncommon one. The school is far from large, with the same being said for the town below it."

    "I stand at the streat, waiting for a slow trickle of cars to pass while trying to fan some air to cool my face."

    "Further down the road the heat rising from the hot asphalt distorts the world into a feverish mirage."

    "Everything is rippling and wavering as if the entire world was just a reflection from the surface of a stone-broken pond."

    "A small group of elderly town residents are gathered at the sidewalk, waiting to get across like I am."

    "The sunlight makes me squint my eyes, which in turn makes my temples ache. I close my eyes for a while to give the muscles some rest."

    scene black with shuteye
    
    "My brain feels dull."

    "Someone strokes my shirt as he walks past me, the shy air current feels refreshing on my cheek."

    "It must be safe to cross the street now."

    scene bg suburb_roadcenter with openeye
    
    "I open my eyes, feeling the light striking my retinas like heated needles."
    
    stop music fadeout 4.0

    "The group has not moved, except for one red-haired girl who is a few yards in front of me."

    "A fancy sports car, one of those Italian import cars you only see in magazines, is speeding towards the crosswalk way over speed limits."

    "It is very red and just washed and polished, the kind of car that looks like you could get a ticket for speeding just for sitting in the driver's seat at a parking place. An odd sight for such a town."

    "Rin is walking slowly, so slowly she is almost unwalking across the road."
    
    play music music_tension fadein 0.5

    "Why is she there, and why doesn't she notice the car?"

    "Why is nobody doing anything, the dull thought passes through the back of my brain."

    "The adrenaline rush, or maybe the intense heat makes the following second go in slow motion."

    "I leap forward, closing the short distance between myself and Rin and grab her collar to yank her back with all my strength."

    "The sudden reverse in momentum makes me lose my balance, topple backwards and draw Rin down with me."

    play sound sfx_impact
    with vpunch
    scene black with shuteyemed
    
    play sound sfx_skid
    
    "Tires screech against the tarmac." 
    
    stop music fadeout 0.5

    "I feel Rin's head hitting against my chin as we plummet to the sidewalk in one bunch of me and her."
    
    show bg suburb_roadcenter with openeye_shock
    
    "I open my eyes to find both her and myself unharmed, just a few feet out of harm's way."

    "The driver honks his horn a few angry times and speeds off again."

    "I breathe out for the first time in at least ten seconds. It is a long one, almost a sigh."

    "Someone asks me if I'm all right in a raspy, strained voice, but I can only nod in answer with the adrenaline still surging through my veins making me unable to speak."

    "The handful of cars having passed, the gathered people cross the street. We are left alone, sitting on the sidewalk."

    show rin basic_absent with charamoveinbottom
    
    $ renpy.music.set_volume(0.1, 1.0, channel='ambient')
    
    play music music_rin
    
    rin "Hello."
    
    hi "Hello? Is that all you can say?"

    rin "No, but it was the first thing that came to my mind."

    rin "It's a nice word, round like a soap bubble and very big, even though it's not big like that. I like saying it so—{w=0.2}{nw}" #reminder for the potential {nw} break

    #This needs some emphasis, like so:
    
    $ renpy.transition(charachange, layer='master')
    show rin basic_surprised
    hi "{size=36}{b}WHAT THE HELL ARE YOU DOING?{/b}{/size}" with vpunch
    
    "I realize I have been shouting at the top of my lungs only after the people crossing the street turn back to stare at us."
    
    "It even startles me, causing me to slap my hand over my mouth as if to retroactively prevent the words from coming out."

    show rin basic_absent with charachange
    
    "Rin, however, seems to be the only person not taken aback at all, even though she shuts up."

    "She is staring at me with those green eyes of hers, without even a hint of emotion in them."

    "Or maybe something. If I had to describe it, which I don't but I do anyway, I'd call it confusion, or maybe concern."

    rin "Are you upset about something?"

    "I stare at her, feeling a headache building inside my head. I press my eyes shut with my fingers, squeezing the bridge of my nose hard."
    
    scene black with shuteye
    $ renpy.pause(2.0)
    scene bg suburb_roadcenter
    show rin basic_absent 
    with openeye
    "When I open my eyes, she is still there, staring at me the same way as before, sitting on the edge of the sidewalk the same way as before."

    hi "You could have died. What would you have done then?"

    rin "I don't know. But I didn't die, did I?"

    hi "Because I tackled you."

    rin "I might not have died anyway. You can't count out for example divine intervention, {a=ismuth_R9_whut}or disk brakes{/a}. Both are very efficient."

    "I plant my hand heavily on Rin's shoulder and squeeze, to make sure that she is paying attention." 
    
    "The unexpected contact makes her neck muscles stiffen and relax again, and to turn to look at my slightly trembling hand because suddenly it's very hard to look at Rin."

    show rin basic_awayabsent with charachange
    
    hi "Just don't do that again, ok? "

    show rin basic_absent with charachange
    
    rin "Why?"

    hi "Because I am in a bad mood and you treating your life with reckless abandon is making me even more upset. So, just don't." #on->in 

    rin "Why are you in a bad mood?"
        
    rin "No, don't say it. Let me guess. I am good at it after all, although it seems that you might surpass even me."

    show rin basic_lucid with charachange
    
    "She draws in deep breath."

    show rin basic_deadpanamused with charachange
    
    nvl show dissolve
    rinbabble "You probably woke up with the wrong hand so you got very depressed and then noticed that your Wednesday socks are in the laundry so you had to either use Tuesday socks for two days in a row or use Thursday socks 
               on Wednesday which not only is huge bad luck but also leads to a vicious cycle of using wrong socks on a wrong day so it's even more bad luck unless you can get another pair from somewhere. 
               Or no, the day is not wrong really, only the socks are. Two misfortunes like that in one morning is the kind of thing that could get anyone down. Trust me, I know."
    
    nvl hide dissolve
    nvl clear

    "I don't even bother to answer. Instead, I stand up and start making my way across the road."

    show rin basic_awayabsent with charachange
    
    "Rin follows me silently, walking half a step behind me."

    "…"

    "As we pass the third house down the street I can't stand the silent treatment anymore, even though it's me who is doing it."

    hi "I'm going crazy."

    show rin basic_absent with charachange
    
    rin "So I was right?"

    "…"

    hi "No."
    
    hi "I have been seeing these… nightmares I guess, for a few nights now. I'm thinking about going to see the nurse about them. For some reason they disturb me very much."

    show rin negative_spaciness with charachange
    
    "Rin doesn't seem to be too concerned, instead she raises her eyebrows and changes her angle so that she is walking almost sideways."

    rin "Oh, that's interesting. What are they like? I have never seen a nightmare."

    "Even though nowadays I try to brace myself against the unexpected when hanging out with Rin, she still manages to catch me off guard."

    hi "What? I thought everyone has nightmares."

    "She has no explanation to offer, just a noncommittal shrug of shoulders."

    show rin basic_awayabsent with charachange
    
    rin "I guess I'm not everyone."

    hi "Maybe you just don't remember?"

    "She shakes her head surprisingly assertively, making her auburn hair reflect the sunlight in tones of orange and gold."

    show rin basic_absent with charachange
    
    rin "I remember all my dreams, so I know."

    hi "How can you know that? If there was a dream you didn't remember, you wouldn't remember not remembering it either."

    show rin basic_lucid with charachange
    
    "She takes her time to sort through all the remembering in my rebuttal."
       
    show rin basic_absent with charachange
    
    rin "Maybe you are right. Three points."

    rin "But I'm pretty sure I would remember."

    show rin basic_delight with charachange
    
    rin "So anyway, tell me of yours."

    "Her simple request is not an order, but I feel compelled to explain myself regardless. I just don't what to say to Rin."

    hi "There's nothing to tell. There's no monsters or falling off a cliff or anything. I just dream of… I guess of dying and then wake up hurting like hell in here."

    "I press my finger on the precise spot it hurts, just a little to the left of my solar plexus."
    
    "She looks curiously at my finger and the spot it is pressing, furrowing her brow."

    show rin basic_deadpancontemplation with charachange    
    
    nvl show dissolve
    rinbabble "That's weird. Almost as weird as that one time when Emi found two butterflies in her lunch box and it turned out that those kinds of butterflies don't live in Japan at all. 
               The best theory to this date is that there was some kind of a teleportation going on, because not only her lunch had extra butterflies, she was missing a slice of tomato from her sandwich, 
               so maybe that was switched with the butterflies although the motivation for that is what boggles me. The tomato couldn't have been magically turned into the butterflies, since they were not red at all. 
               They were yellow with blue spots in all four wings and some white I think."

    nvl hide dissolve
    nvl clear
    
    show rin basic_absent with charachange
    
    rin "Well, anyway. Weird."

    hi "You can say that again. Well, you did already, I guess."

    #hi "I went to the nurse, but he wasn't helpful."

    #rin "A common occurrence. By the way, where are we going?"

    rin "By the way, where are we going?"
    
    "She suddenly seems to realize that we are not at the crossroads anymore."

    hi "Eh, I was going to the convenience store. Weren't you?"

    show rin basic_awayabsent with charachange
    
    rin "Oh no, I was following a cloud but when you knocked me down I lost track of it."

    rin "Then we started talking and it would have been difficult to keep doing that if you were going this way and I was going some other way."

    rin "But now that I am here, I guess I could go to the convenience store as well."
    
    stop music fadeout 2.0
    stop ambient fadeout 2.0

    #scene change

    scene bg suburb_konbiniext
    with locationchange
    
    $ renpy.pause(1.0)
    
    play sound sfx_storebell
    scene bg suburb_konbiniint
    with locationchange

    play music music_daily fadein 1.5
    
    "The store is cool inside. I wonder if they would let me just stay there for the rest of the day, or the month? Like reverse hibernation, wouldn't be too bad."
    
    "I make a beeline to the ice cream section. When it's hot and sunny, there is nothing like a chilly popsicle to freeze my brains with."

    "Rin joins me while I am contemplating between strawberry and {a=aura_raspberry_flavor}raspberry{/a} flavors. She is looking yearningly at the frozen products, just like me."

    #If one of the editors makes a fact check and comes telling me they don't sell raspberry flavoured popsicles in Japan, I swear I am going to come to your houses at night and stab you

    hi "Do you want something?"

    show rin basic_absent with charachange
    
    rin "{a=ismuth_R9_whut}Frozen corn please.{/a}"

    hi "What?"

    show rin basic_surprised with charachange
    
    rin "What what? Frozen corn is delicious."

    hi "Oh come on, don't be ridiculous. Take ice cream, or popsicle, or whatever. It's summer!"

    show rin basic_deadpancontemplation with charachange
    
    rin "No, I can't eat those and walk at the same time so it will melt. With corn, it doesn't matter."

    "…"

    hi "If it's only that, it's no problem."

    #scene change back to the street
    
    scene bg suburb_konbiniext
    with locationchange
    $ renpy.pause(1.0)
    $ renpy.music.set_volume(0.2, 0.0, channel='ambient')
    play ambient sfx_traffic fadein 1.5
    scene bg suburb_roadcenter
    with locationchange
    
    show rin basic_awayabsent with charaenter
    
    "We walk along the sidewalk back towards the school side by side, as slowly as possible to find a common rhythm."

    "Sun shines off the white-painted walls and clean windows of the houses on both sides of the street."

    "A few other people are around, dressed in their summer clothes, most walking towards the store."
    
    "The excessive warmth makes the afternoon feel lazy, as if the town itself is just basking in the sun."

    show rin basic_absent with charachange
    
    "I hold both popsicles, a raspberry flavoured in my left and and a strawberry flavoured in my right hand, trying to keep the one in my left high so Rin can suck on it easily."

    "Despite my efforts, she has to turn and bend down whenever she wants some, causing her steps to go out of rhythm, which in turn makes me go out of rhythm so we are walking with a constantly fluctuating pace."
    #2 mny wrds in sentenc

    show rin basic_awayabsent with charachange
    
    "Moving my hand to try to help Rin eat seems to only make it more difficult for her, so I contend myself to just hold the popsicle and let her figure out how to deal with it."
     
    "Some melted popsicle has stuck to the sides of her mouth, coloring them rosy red. When she licks her lips clean I notice the tone is almost the same as her tongue has."

    show bg school_road_ss with locationchange
    
    show rin basic_amused_ss with charachange
    
    "Rin is eating with her eyes closed, really getting into eating a simple popsicle with enthusiasm I wouldn't have suspected from her. She looks like she is truly enjoying it."

    "It makes me worried about her balance, but surprisingly enough she doesn't fall over herself or me."

    "…"

    stop ambient
    scene bg school_gate_ss with shorttimeskipsilent
    
    show rin basic_awayabsent_ss with charaenter
    
    "Somehow both of us manage to finish our icy cold treats before we are back at school."

    "I am still a bit bothered about the incident on the way to the store."

    hi "Listen, I'm sorry I yelled at you."

    "Why did I get so agitated? I consider myself a pretty calm and collected person, but nowadays I find myself losing my temper on a daily basis."

    "To be honest, I feel really bad about getting so angry even though Rin's nonchalant disposition is quite infuriating."

    "Even now, her probing, measuring eyes that seem to elude all attempts at locking gazes are looking at something that probably is not me."

    show rin basic_absent_ss with charachange
    
    rin "Don't worry."

    rin "It's all right if you have a hard time. Everyone has, sometimes."

    "The sun keeps on shining from the high sky as we enter the grounds from the main gate."
    
    stop music fadeout 2.0

    window hide dissolve
    show black with Dissolve(1.5)
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    return

label en_R11:
    
    show black 
    window show dissolve
    mu "So if you consider the momentum of…"
    scene bg school_scienceroom
    with openeye
    
    
    "In the middle of Mutou's explanation about something I wasn't listening to I awaken to realize I've actually been looking forward to today's art club meeting since the morning." #realise -> realize (USA English)
  
    "It's fun to mess around with the paints and pens, and Rin is fun to talk with in a way, if not for anything else, then for the entertainment her silly antics provide."

    "She makes the rational part of my head furious at times, but I can't help being secretly amused."

    "I take a sideways glance at the clock above the classroom door. Half an hour to go."

    "I feel anxious for other reasons too. Something about yesterday keeps on bothering me."

    "Rin wasn't too concerned about it, but…"

    #background change to black, or something ambiguous, text possibly NVL?
    
    window hide dissolve
    scene black
    with fade
    
   
    play music music_sadness fadein 1.0
    
    nvl clear
    nvl show dissolve
    
    n "Rin's close shave with that car made me realize, once again, how life is not to be taken as a matter of course."

    n "Didn't have the same effect on her, though. I remember being pretty freaked out after the heart attack in January, and not only because the arrhythmia was diagnosed."

    n "Rin just… shrugged it off."

    n "Usually people tend to put a great value on living itself, maybe exactly because it's so fragile."

    n "Everyone talks about death being a natural part of the cycle of life, but when it hits close, the ivory tower crumbles like a house of cards. At least that's how I felt."

    n "What if I died tomorrow?"

    n "That's possible, for all I know, no matter what medications I take."
    
    nvl clear

    n "Would I have regrets? Certainly, I haven't done a lot in my life, being so young and all. Missing out on the aspects of life I haven't yet seen seems like a waste."

    n "Maybe that is the real tragedy of kids dying. Such a waste."

    n "Yeah, I wouldn't be so bothered if I was 80 years old or something."

    n "Despite that, speaking about lost potential and stuff like that is crap, losing one's life is about something completely else than losing your potential worth to humankind."

    n "It shakes the very foundations of being."
    
    stop music fadeout 5.0
    nvl hide dissolve
    nvl clear
    
    scene bg school_classroomart
    with fade

    window show dissolve
    
    hi "{a=Note}I wonder what would shake Rin{/a}?"
#This makes it sound like Hisao is thinking aloud, sort of, as opposed to the pure inner monolouge it was beforehand. Also make's Rin's entering line a bit more… justified, for lack of a better word.
  
      
    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)  with charaenter
    
    rin "Did you say something?"

    #enter Rin sprite and art classroom in some order about hereish, or after the next line, or both

    hi "No… nothing."

    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)  with charachange
    hide rin with charaexit
    
    "She shrugs and turns back to her painting."
    
    play music music_tranquil fadein 2.0

    "Today we are allowed to do whatever we want."

    "Nomiya left us with no instructions whatsoever, told us to get materials by ourselves and then left to an important meeting with some artist acquaintance of his."

    "I picked up watercolors while Rin is sitting on the floor, a huge canvas in front of her slowly filling with oil paints."

    "It's supposed to be some larger project of hers, evident from the fact that the canvas was readily available and already partially painted."

    "As usual, Rin wouldn't say what exactly it is that she is going to paint, and from the abstract shapes and colors I can't say what it might be, either."

    "Besides, I have my own problems as well."
    
    "I decided to paint the same cherry trees I drew with graphite last week using my sketch as a model, but without a real life tree to look at I have a hard time visualizing what I want to paint, not to mention the problems I have with the medium itself."

    "Watercolors are notoriously easy to mess up irreparably, and I am quickly sliding to that direction."

    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charaenter
    
    rin "Do you ever feel like you are the world's oyster?"

    "The question makes me look up from my despair to see Rin intently staring at her half-way painted canvas. It is not immediately obvious which one of us she directed the question to."

    "I dip the brush into the water cup and sigh, half to Rin, half to the sad result of my attempts to create some trees on the paper."

    hi "That's not right."

    hi "You said it backwards. The world is my oyster. Or yours."

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "Do you ever feel like you are the world's oyster?"

    "She sounds like a broken gramophone, repeating the same track even though I tried to correct her."

    hi "I don't even understand what that means, if you actually wanted to ask that."

    hi "Am I a figurative mollusk, disgusting but delicious if you eat me with lemon? Am I open to the world to see what a wonderful person I am? What on earth are you trying to say?"

    "The silent, expectant stare of hers is frustrating, as if she is waiting for me to figure out what she is talking about by myself, instead of elaborating, or talking sensibly in the first place."

    "I chuckle to myself, feeling a bit silly. Why do I get so agitated by Rin, even now?"

    "I should know better."

    "As I calm down, one more explanation comes to my mind, but I don't want to say it aloud."

    "Am I waiting for someone to open my shell to find something?"

    "Is that how I look to Rin? I don't feel like I have a pearl inside of me."

    "Or did she even talk about me in the first place?"

    hi "I don't know. I'll let you know if I ever feel like that in the future."

    rin "Future?"

    hi "Yeah, like tomorrow and the day after that, and the next year and all the years after that."

    show rin negative_spaciness_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    "Rin tilts her head, looking uncertain. Surely she can grasp the concept of future?"

    rin "Is that the future?"

    hi "Yes, that's all there is to the future, right?"

    show rin negative_confused_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    "Rin's eyes shift around, darting from side to side as if she is avoiding looking at anything."
      
    rin "Yeah."

    "Her suddenly strange tone makes me realize that she is lying, or at least not saying what she thinks. Setting aside the fact that she is a terrible liar, it is odd that she would do it in the first place."

    hi "You knew the answer to your own question already, then."

    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    "Rin starts blinking her eyes as her gaze lowers back to the painting."

    show rin negative_spaciness_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "What do you do with the future?"

    hi "Me?"

    rin "You or someone else. Anybody. Everybody."
     
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "You, probably."

    show rin negative_spaciness_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "They asked that from us today in homeroom. There was some paper about my future career. Did you get one of those?"

    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "I just drew some butterflies on it."

    "I retract my hand that was already halfway to the brush. It's better to not try to do two things at the same time."

    "Rin has laid her wet brush down as well. A small puddle of crimson oil paint is forming on the floor, as if the brush was bleeding."

    hi "I don't know, haven't got any specific plans. I guess I will go to university to get an education first, after that… I don't know."

    "Rin tilts her head at my indecisiveness, as if she doesn't understand what I'm trying not to say."

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "Oh, what will you be studying?"

    hi "Ehh…haven't decided."

    show rin negative_spaciness_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "So you don't know anything about your future."

    "Even though she is right, the blunt tone of hers makes my blood boil."

    hi "How can anyone know about their future? "
    
    hi "That's stupid, sure you can have whatever grandiose plans for it, but in the end you might get screwed over by something completely unexpected."

    hi "I for one certainly didn't plan to have a heart attack at the ripe age of 17…"

    hi "…nor did I plan to be forced to come to this school hundreds of miles away from my home after spending the better part of half a year in hospital…"
    
    hi "…nor did I plan to come to this club and attempt and fail painting this stupid painting."

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "Did I make you angry?"

    hi "No. I just… never mind. What I tried to say is that, you can hope things from future but you can't know a thing."

    rin "And now you said it."

    hi "Yeah. Besides, you too—{w=0.3}{nw}" #reminder for the potential {nw} break

    show rin basic_deadpandelight_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "A butterfly."

    "Rin interrupts me, although it looks like it is not intentional as she has already moved her restless attention to the sky shining through the windows of the classroom."

    hi "A what?"

    rin "It would be nice to be a butterfly. In the future."

    "Her voice is dreamy, making me uncertain if she is conscious of the fact that she is talking with me."

    rin "There is a thing I want to do, but…"

    "Her voice trails off to a whisper, causing the last few words become too quiet to hear. I get the feeling that she didn't want me to hear them, but I can't help asking."

    hi "But what?"

    "Rin turns to look at me, her mouth drawn in a perfectly horizontal line."

    show rin basic_deadpanupset_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "I can't. So I thought I'd learn how to."

    hi "So, what, you are not a butterfly just yet?"

    rin "I am me."

    "The simple statement seems to carry much more weight than what it's worth with the way Rin says it, a firm utterance without an ounce of hesitation."

    "Rin too seems to be impressed by it. She pauses, then whispers the sentence a few times to herself as if she, by saying it aloud, discovered that she in fact is herself."

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "Nomiya has been trying to help me, sorta like a teacher or something."

    "So the thing she wants to do was painting after all? It would make sense, as it is the only thing I've seen Rin pay more than passing attention."

    hi "He is a teacher."

    rin "Yeah, but not a teacher like that. A nice kind of teacher."

    hi "So he like, what, helps you with your art?"

    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "He points out things he thinks I should not do and he points out things he thinks I should do better. He also points out things he thinks I am doing well."

    hi "I guess that's helping."

    "Speaking of the devil, Nomiya enters the classroom with barely fifteen minutes left until the end of the club."

    show bg school_classroomart at left
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) 
    with dissolvecharamove
    
    show nomiya smile at left with charaenter
    
    no "Hello, everyone! How have you been doing?"

    "His entry makes other people notice that the meeting is at the end too. Everyone starts putting down their materials and get ready to leave."

    "The club members are pretty disciplined, as most of them at least try to keep some order instead of just throwing everything onto Nomiya's desk."

    "Still, since we didn't have any control with the materials we used, the amount of stuff piling on the two wooden trays on the desk is pretty huge."

    "The teacher doesn't look too happy about it either."

    show nomiya talk at left with charachange
    
    no "Nakai, would you stay to help me cleaning?"

    hide rin with charaexit
    
    show nomiya smile at left with charachange
    
    "Me? I reflexively turn my head when I hear my name being called. The other members are quickly clearing out of the classroom, obviously knowing that staying behind means extra work."

    "I don't have the option to decline, it seems."

    "Of the few people still left, nobody volunteers to help with the cleaning and even Rin exits, leaving us two between ourselves to clean up."

    "As I gather the materials back to their respective boxes to be taken to the storage, I notice Nomiya studying me intently."

    no "I've noticed you get along well with Tezuka."

    hi "I guess you could say that."

    no "I'm surprised, really, and happy. She's always been a bit antisocial so it's a good thing if she found a friend."

    show nomiya talk at left with charachange
    
    no "You know Nakai, it makes me wonder if you could help me…"

    no "You see, I happen to be in very good standing within the art community in this town. Some of them are very famous people, you know, like the person I was meeting today."

    show nomiya smile at left with charachange
    
    no "At any rate, I am certain that Tezuka has the potential to become something."

    "I fetch the last brushes that someone had forgot to the desks at the back, and then we are ready to take all of them to the arts storage."

    show nomiya dreamy at left with charachange
    
    no "I can see it in her art, she definitely has the talent."

    no "So I have been talking about her to a gallerist friend of mine, so that she would have some of Tezuka's works on display."

    scene bg school_hallway3 with locationchange
    
    show nomiya serious with charaenter
    
    no "Unfortunately, Tezuka herself has been pretty hardheaded about it, saying that she doesn't want to put her works on show."

    no "I've tried to reason with her, but as you probably know, it's quite hard."

    "The hallway is empty save for us. The wooden tray is too big to be carried comfortably now that it's loaded with all sorts of brushes and other utensils, but I carry my burden without complaining."

    "Nomiya, with the smaller of the two trays on his arms, keeps on babbling about Rin."

    show nomiya talk with charachange
    
    no "So, I wonder if you could talk with Tezuka about it, and try to make her change her mind."

    no "It would be most unfortunate if she misses this chance."
      
    no "Don't you agree?"

    show nomiya smile with charachange
    
    "It takes me a second to realize that he had stopped talking."

    hi "Ah, Yes."

    "It is strange…"

    no "Right, I'll trust you to try your best. Thank you very much for helping me with these. Off you go, then."
    
    "I leave Nomiya to sort the various materials to their proper places and make my way downstairs."

    scene bg school_staircase2 with locationchange
    
    "So Rin would, at least in theory, have a chance to get some of her paintings to a gallery? But she didn't sound too exhilarated about it."

    "Why would she be hesitant to take up on such an awesome offer, especially if she wants to become a professional artist?"

    "And why does Nomiya think I can help him and Rin?"

    stop music fadeout 3.0
    
    "I have to admit, my interest is piqued, as this is gives me a chance to actually learn something about the enigma that Rin seems to be."
    window hide dissolve
    
    scene black with Dissolve(1.5)
    $ renpy.pause(2.0)

    return

label en_R12:
   

#Thinking of putting in a BG + sprite slideshow, but for now, simplicity
    
    play music music_timeskip

    show kslogo heart at Position(xalign=0.5, yalign=0.5)
    with clockwipe

    scene black
    show kslogo words at Position(xalign=0.5, yalign=0.5)
    with clockwipe

    $ renpy.pause(2.0)

    scene black
    with clockwipe

    $ renpy.pause(2.0)
    
    scene black
    scene bg school_dormhisao with openeye
    $ renpy.pause(1.8)
    scene bg school_courtyard with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_scienceroom 
    show muto smile 
    with shorttimeskip
    $ renpy.pause(1.8, hard=True)
    scene bg school_classroomart 
    show nomiya talk at left
    show rin basic_upset_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8)
    with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_courtyard_ss with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_dormhallway 
    show kenji rage at Position(xanchor=0.5, yanchor=0.5, xpos=0.3, ypos=0.5625) 
    with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_dormhisao_ni with shorttimeskip
    $ renpy.pause(1.8)
    scene black with shuteye
    $ renpy.pause(1.0)
    scene bg school_dormhisao with openeye
    $ renpy.pause(1.8)
    scene bg school_scienceroom 
    show misha sign_smile at twoleft 
    show shizu cross_rage at tworight
    with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_roof
    show rin basic_absent at tworight
    show emi excited_joy at twoleft
    with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_dormhisao_ni with shorttimeskip
    $ renpy.pause(1.8)
    scene black with shuteye
    $ renpy.pause(1.0)
    scene bg school_dormhisao with openeye
    $ renpy.pause(1.8)
    scene bg school_dormbathroom 
    show steam 
    with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_nurseoffice
    show nurse concern
    with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_hallway3
    show lilly basic_ara 
    with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_library 
    show yuuko neurotic
    show hanako emb_downtimid at right
    with shorttimeskip
    $ renpy.pause(1.8)
    scene bg school_gardens2
    show emi basic_happy at twoleft
    show rin basic_surprised at tworight
    with shorttimeskip
    stop music fadeout 6.5
    $ renpy.pause(1.8)
    scene bg school_dormhisao_ni 
    with shorttimeskip
    $ renpy.pause(1.8)
    scene black with shuteye
    $ renpy.pause(1.8)
    scene bg misc_sky_rn
    with Dissolve(2.5)
    
    
    play music music_another fadein 1.0

    #A textless slideshow of some backgrounds, maybe a clouded sky could open this day to drive in the point that the day changed (or actually we skipped three days). If that doesn't work, ask me to write more.

    window show dissolve
    
    hi "Are you sure you want to go?"

    
    emi "Of course! I've been waiting for this the whole week!"

    scene bg school_gate_rn with locationchange
    show emi sad_grin_rn at twoleft
    show rin basic_absent_rn at tworight
    with charaenter
    
    "Rin's silence is apparently a sign of her consent."
    
    scene bg school_road_rn with locationchange
    show emi basic_closedgrin_rn at tworight
    show rin basic_awayabsent_rn at twoleft
    with dissolve
      
    "The leaden clouds drooping over the town look worrisome, so I have my umbrella and I even asked if the girls really want to brave the potentially rainy weather, but…"

    "It looks like nothing will stop Emi now."

    "She is positively exhilarated, brimming with energy as always, but something seems special today."

    "It looks like she can hardly stop herself from jumping up and down on the spot."

    show emi excited_joy_rn at tworight with charachange
    
    emi "Come on!"

    "I grasp the wooden handle of the umbrella and set to follow the two girls who seem to have no inhibitions leaving me behind if I kept daydreaming here."

    "My umbrella is really nice, the old-fashioned kind with curved handle and a metal spike at the end. It used to belong to my grandfather."

    "It's really big too. I remember how me, my grandfather and my grandmother all fit neatly under it when a rainstorm caught us on an afternoon walk years ago, when I was maybe nine or ten."

    "My grandparents are both gone now, but I still have the umbrella to keep me dry when it rains."

    show emi basic_happy_rn at tworight with charachange
    
    emi "Horseshoe."

    "Emi's exclamation comes out of nowhere, or maybe I didn't hear the prefacing discussion."

    show rin basic_absent_rn at twoleft with charachange
    
    rin "Umm…a big tree with no leaves."

    "She doesn't miss a beat."
    
    show emi excited_proud_rn at tworight with charachange
    
    emi "No, a rabbit's foot."

    show rin basic_deadpandelight_rn at twoleft with charachange
    
    rin "A bird."

    show emi basic_concentrate_rn at tworight with charachange
    
    "Ok, something's that I am not aware of is going on."

    hi "What are you doing?"

    "I cut in at a bad time probably, as Emi looks like she is thinking so hard her head will split."

    "She doesn't look too bothered about the interruption though as she turns too look at me with a sheepish smile on her face."

    show emi basic_grin_rn at tworight with charachange 
    
    emi "It's a game. One says a word and the other tries to guess what she is thinking."

    show rin basic_absent_rn at twoleft with charachange
    
    emi "It's just something to do when you have nothing to do. Rin invented it."

    "I look at Rin, but she doesn't seem to have any further explanation to offer."

    "Eventually she catches my questioning gaze and shrugs her shoulders."
       
    rin "It's about… umm, what's that word for things that mean something else than the word does?"

    hi "I don't know… symbols, maybe?"

    show rin basic_delight_rn at twoleft with charachange
    
    rin "Yeah, that's it."

    show emi basic_confused_rn at tworight with charachange
    
    emi "How did you guess that?"

    "Emi's voice is as incredulous as is the stunned expression on her face, but what can I say?"

    hi "A lucky, no, let's say educated guess."
    
    show rin basic_deadpandelight_rn at twoleft with charachange
     
    rin "See now, Emi?"

    show emi basic_closedgrin_rn at tworight with charachange
    
    "Emi smiles widely and turns around all the way, walking backwards so she can face me when talking."

    emi "Do you want to try? We can play it with you too! Looks like you could even get one of Rin's right."

    show emi excited_proud_rn at tworight with charachange 
    
    emi "Ho ho, but I am a formidable opponent in the field of logic, you better prepare yourself Hisao!"

    "Suddenly this silly game feels like a very serious business. Emi's competitiveness bursts aflame and she looks like she is about to launch into a sprint"

    "I don't really know what this game has to do with logic though… it feels more like intuition or mindreading."

    show emi excited_joy_rn at tworight with charachange 
    
    emi "Ok, let's start over. You can go first, Hisao."

    "I think for a moment for a thing that could symbolize another thing. It's not too easy to think of a good one, but for once I feel like it's better to not overanalyze."

    hi "A star."

    show emi basic_concentrate_rn at tworight with charachange 
    
    emi "A wish."

    "Emi answers very quickly, while Rin thinks for a bit longer."

    show rin relaxed_nonchalant_rn at twoleft with charachange
    
    rin "A fish."

    show emi basic_annoyed_rn at tworight with charachange 
    
    emi "I said that already. You can't say the same thing."

    show rin basic_absent_rn at twoleft with charachange
    
    rin "No, a fish."

    show emi basic_grin_rn at tworight with charachange 
    
    emi "Oh, ok then."

    hi "Sorry girls, I was thinking of fame. You know, like movie stars… was it too hard?"

    show emi excited_happy_rn at tworight with charachange 
    
    emi "No no, it was really good one. Let's continue, me next!"

    show emi basic_concentrate_rn at tworight with charachange 
    
    "She looks like she tries to think of her question very hard, even a bit too hard. I almost made the same mistake."

    emi "A round stone."
     
    hi "Sea."

    show emi basic_hes_rn at tworight with charachange
    
    show rin basic_deadpancontemplation_rn at twoleft with charachange
    
    rin "A fish."

    "Again with the fish? Emi doesn't look very pleased at herself."
      
    emi "Sorry, Rin. Hisao guessed it right. Damn you! Ok, Rin's turn next"

    "I wasn't aware that this game had winners or losers, but maybe guessing right means that you have a certain kind of a mental grip over the opponent."

    show rin basic_absent_rn at twoleft with charachange
    
    rin "Two hearts."

    show emi excited_joy_rn at tworight with charachange
    
    $ doublespeak(hi, emi, "Love!")

    show emi excited_laugh_rn at tworight with charachange
    
    "We turn to look each other and burst into laughter, while Rin frowns, looking deeply disappointed."

    show rin relaxed_doubt_rn at twoleft with charachange
    
    rin "I tried to make this really easy one. I was thinking of a fish."

    show emi excited_hesitant_rn at tworight with charachange
    
    hi "Wait, what? Fish again? You can't seriously have associated a fish with all three of those. Now you really got to explain yourself."

    show rin relaxed_surprised_rn at twoleft with charachange
    
    rin "What? If you draw two hearts like this, one after the other, they look like a fish. And if you draw a star like this, it looks like a fish. And the third one should be self-explanatory."

    "She quickly brushes some dust into a shape of very elongated star and two very disfigured hearts with her toes, admittedly they are slightly resembling fishes."

    "Yeah, this game doesn't have anything to do with logic."

    show emi basic_closedhappy_rn at tworight with charachange
    
    "Emi laughs, looking like she is of the same opinion than me about Rin's trains of thought. I really can't fathom how she can think like she does."

    "How do you associate a round stone with a fish?"
    
    scene bg suburb_roadcenter_rn
    with locationchange

    show rin basic_awayabsent_rn at twoleft 
    show emi basic_grin_rn at tworight
    with charachange
    
    "We walk along the street leading to the convenience store with the clouds casting their dark shadow down on us."
    
    "The girls didn't disclose their plans, if there even are any, but I am fine with anything."

    "Then again, I hope we could be indoors. The weather seems to be going to a worse direction and I am pretty sure I just felt a raindrop on my head."

    hi "Didn't you guys think of taking umbrellas? It really looks like it'll rain."

    show rin basic_deadpannormal_rn at twoleft with charachange
    
    "Rin looks at her limply hanging sleeves and shrugs her head."

    "Gah, I didn't really mean her even though I used plural, but it still feels like I made a faux pas."

    show emi excited_proud_rn at tworight with charachange
    
    emi "I don't have one. Besides, a little rain won't kill us."

    "She pushes her chest out, looking very confident about that."

    show emi excited_joy_rn at tworight with charachange
    
    emi "We aren't made of sugar!"

    "Funny, I thought that's exactly what girls are made of."

    "The walk from the school to the local shopping district is not a long one, but it's not a short one either."

    "It's right there, in the gray area where you don't expect the trip to be quickly over with, but neither are you preparing for a long walk."

    show emi basic_grin_rn at tworight with charachange
    
    "And so, the trip is slightly too long to comfortably stay entirely quiet, even though Rin seems to try, and I almost manage it too."

    show rin relaxed_nonchalant_rn at twoleft with charachange
    
    "Emi, on the other hand, is way too happy about just walking."

    "She seems to literally jump a little on every step, or skip over cracks or balance on the edge of the sidewalk, every now and then commenting on something, to which Rin replies in a nonsensical way that makes Emi giggle like a schoolgirl."

    show rin relaxed_surprised_rn at twoleft with charachange
    
    "As we pass the convenience store, Rin's attention catches on the display windows of the neighbouring art shop."

    show emi sad_grin_rn at tworight with charachange
    
    "She halts on her tracks, causing me and Emi to walk a few steps before noticing that she is not with us anymore."

    "As we backtrack, I take a look at what Rin is watching so intently."

    "I see nothing special though, just some brand of oil paints on display and an example painting of an arrangement of red and yellow flowers, set attractively on a mini-sized easel."

    emi "We could go in. Would you like to, Rin?"

    stop music fadeout 5.5
    
    show rin basic_absent_rn at twoleft with charachange
    
    rin "I can wait for you out here too."

    show emi basic_annoyed_rn at tworight with charachange
    
    "Emi sighs and grabs Rin by the sleeve, dragging her in. I guess the stop at the art shop was not planned, but why not? We have the whole day free after all."
    
    # art shop?
  
    play sound sfx_storebell 
    play music music_soothing fadein 2.0    
    scene bg suburb_artshop with locationchange
    show emi basic_grin at tworight
    show rin basic_delight at twoleft 
    with charaenter
    
    "I have noticed the shop before, but it's the first time I step in. The interior is barely lit, the lack of light only enhanced by the cloudy weather outside."

    "The scent of paper and paint hangs heavily around here, just like in the art storage of the third floor."
     
    
    $ renpy.music.set_volume(0.0, 0.0, channel='ambient')
    play ambient sfx_rain 
    $ renpy.music.set_volume(0.2, 7.5, channel='ambient')

    
    "The shopkeeper pays us no attention as he lazily does some paperwork on the dark wooden counter in the back."

    hide rin with charaexit
    show emi invis at right with dissolvecharamove
    
    "I idly browse the selection of watercolor supplies as I wait for Rin to watch around until she is satisfied."
    
    show emi invis at left with None

    "Buying my own art supplies seems unnecessary even though I joined the club. It's just that I probably wouldn't do much of it on my free time."

    "Still, the fine brushes and fresh blocks of color look very fancy even to my eye."

    "Rin wanders through the aisles like a sleepwalker, periodically stopping to inspect some item, but not showing any interest in actually buying anything."

    "As my limited interest is about to end, I start wondering how long Rin will take."

    "Emi is leaning against the wall near the entrance with her hands crossed and a defeated smile on her lips, as if she knows that it's futile to even think of going with any other pace than Rin's."

    "As I walk to her, I think I can hear raindrops falling outside. Hope it's just a quick shower."
    
    show emi basic_grin at twoleft with charaenter
    with Pause(0.5)
    show rin invis at Position(xanchor=0.5, xpos=0.80) with None
    show rin basic_absent at tworight with dissolvecharamove   
    
    "Eventually, even Rin has seen enough, and joins us at the entrance."
    
    "As we step through the door, a nasty surprise is waiting for us."
        
    play sound sfx_storebell
    scene bg suburb_roadcenter_rn
    $ renpy.music.set_volume(1.0, 0.5, channel='ambient') 
    show rain
    with locationchange
    $ renpy.pause(0.7)
    show emi basic_annoyed_rn at twoleft 
    show rin basic_deadpannormal_rn at tworight
    with charaenter       
    
          
    "The rain is pouring heavily on the streets, drumming on the hoods of the cars parked on the sides of the street and already flowing in little creeks along the sidewalks."
    play sound sfx_thunder
    show bg suburb_roadcenter_rn with flash
    
    show emi basic_shock_rn at twoleft 
    
    emi "Oh, shoot."
     
    show rin basic_surprised_rn at tworight
        
    "We quickly retreat back to the art shop, with Emi pulling Rin from her sleeve lest she just keep standing there in the rain."
    
    stop ambient fadeout 0.5
    play sound sfx_storebell 
    $ renpy.music.set_volume(0.2, 0.5, channel='auxambient')
    play auxambient sfx_rain 
    scene bg suburb_artshop with locationchange
    show emi basic_annoyed at tworight
    show rin basic_absent at twoleft
    with charaenter
    
    "The shopkeeper shoots a weird stare at us because we suddenly barge back in, but he doesn't bother to comment on how we are blocking the entrance, even though we are."

    hi "What now?"

    "Emi considers our problematic situation for a moment. Obviously we don't want to stay here, as me and Emi would be instantly bored and I guess even Rin wouldn't want to be here forever."

    "The thick sound of rain is penetrating the walls of the shop, making me feel a bit queasy for some reason."
    
    show emi basic_happy at tworight with charachange
    
    emi "Have you been to Shanghai yet?"

    hi "I guess you mean the café that's somewhere around here, not the city? Yeah, I've been there once."

    show emi basic_grin at tworight with charachange
    
    emi "It's nice, isn't it? Everyone from the school likes to go there, it's really popular."

    emi "Let's go there to wait for the rain to end. It's really close, too."

    "Neither me nor Rin have a better idea, so we step back outside where I open my umbrella and lift it up."
    
    play sound sfx_storebell 
    $ renpy.music.set_volume(1.0, 0.5, channel='auxambient')
    scene bg suburb_roadcenter_rn 
    show rain
    with locationchange
    
    show rin basic_absent_rn at twoleftoff
    show emi basic_grin_rn at tworightoff
    with charaenter
      
    "It barely covers all three of us if the girls stay close to me, and while I'm not complaining, one of them really could have taken an umbrella as well."

    "The café is only a few blocks away, but we can't avoid getting slightly damp despite the umbrella."

    scene bg suburb_shanghaiext_rn
    show rain
    with locationchange
    stop music fadeout 4.0
    
    
    "The yellow light shining through the rainwater that streams down the windows looks very warm and inviting."
    
    
    stop auxambient fadeout 1.5
    play music music_jazz fadein 2.0    
    $ renpy.music.set_volume(0.4, 1.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 2.0    
    play sound sfx_storebell
    scene bg suburb_shanghaiint at left with locationchange
    scene bg suburb_shanghaiint at Fullpan(5.0)
    show emi invis at rightsit
    show rin invis at leftsit
    with None
        
    "I shake the excess water off the umbrella and follow Emi to a vacant table in the furthest corner of the small café."

    "The place is almost full; apparently other people had the same idea as Emi had and now we all are stranded here in this cozy little tea house."

    "The short, brownhaired waitress I met the last time is on shift today again, or maybe she is the only waitress here."

    "I watch her deliver a tray of tea cups and treats to another table taken by Yamaku students, then take an order from a middle-aged couple sitting across from us."

    "As the waitress comes to a stop at our table, Emi turns to her, eyes glittering like a child at the candy store."

    show rin basic_absent at twoleftsit 
    show emi basic_grin at tworightsit
    with dissolvecharamove
    
    emi "Hey, Yuuko!"

    "The girl is clearly startled that Emi knows her name. She bats her eyes a few times looking confused, then remembers that she was about to say something."

    show rin basic_absent at leftsit
    show emi basic_grin at rightsit
    with dissolvecharamove
    show yuukoshang neurotic_up at Slide(0.6,0.5,0.5,0.5,0.5) with charaenter
    
    yu "Umm… ahh, welcome to Shanghai. What can I get you today?"
    
    show emi basic_happy at rightsit with charachange
    
    emi "Tea! And cake!"

    "The waitress tries to stay as formal and professional looking as possible while she tries to figure out who Emi is and why is she talking so casually to her."
    
    show yuukoshang neutral_down with charachange
    
    show rin basic_awayabsent at leftsit with charachange
    
    "Well, I guess you can't remember every customer in a busy place such as this."
    
    yu "Ahh… yes, today we have strawberry tart or cheese cake with lemon and cream."

    show emi excited_happy at rightsit with charachange
    
    emi "Strawberry!"

    "She looks at me challengingly."

    hi "Err… I'll take the cheese cake, please."

    show rin basic_deadpan at leftsit with charachange 
    
    rin "Nothing."

    show emi basic_annoyed at rightsit with charachange
    
    "Emi makes a face like she had eaten a lemon at Rin. She is clearly not happy that Rin doesn't join us splurging with the sweets."

    emi "Oh come on, Rin. That's not polite at all."

    show rin relaxed_boredom at leftsit with charachange
    
    rin "Nothing, thank you."

    show emi basic_confused at rightsit with charachange
    
    emi "Noo, I meant that you should order something too ."

    show rin negative_spaciness at leftsit with charachange

    rin "I'll take a straw."

    show yuukoshang panic_up with charachange
    
    yu "Sorry?"
     
    show rin basic_awayabsent at leftsit with charachange
    
    rin "The drinking kind of straw. One, please."

    "The waitress, obviously uncertain of what to think about this just fiddles with her pen and stationery for a moment looking like she is going to cry, before deciding that we have finished ordering."

    yu "Thank you for patronizing our establishment!"
    $ renpy.pause (0.4)
    show yuukoshang happy_down at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.7) with dissolvecharamovereallyfast
    $ renpy.pause (0.4)
    show yuukoshang happy_down at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.5) with dissolvecharamove
    $ renpy.pause (0.3)
    show yuukoshang invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.5) with dissolvecharamove
    "She bows down very deep and scampers to safety behind the counter."
    show rin basic_absent at twoleftsit
    show emi basic_grin at tworightsit
    with dissolvecharamove  
    
    "After the ordeal is over with I have a chance to relax a bit and look at the surroundings more."

    "Almost every table is taken, with people happy to be safe from the rain thankfully sipping their teas and trying to get themselves dry."

    "Fragments of discussions berating the lousy weather or the latest batch of homework carry from the other tables to my ears, the voices drowning under each other and the sound of rainfall."
   
    show rin basic_absent at leftsit
    show emi basic_grin at rightsit
    with dissolvecharamove 
    show yuukoshang neutral_up at Slide(0.6,0.5,0.5,0.5,0.5) with charaenter
            
    "After a while the waitress returns to our table, carrying a tray with a teapot, some cups and two slices of cake."
    
    show yuukoshang neutral_up at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.7) with dissolvecharamove
    play sound sfx_tray_rattling
    $ renpy.pause (0.6)
    show yuukoshang neutral_down at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.5) with dissolvecharamove
    $ renpy.pause (0.3)    
    show emi basic_happy at rightsit with charachange   
    show yuukoshang happy_down at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.7) with dissolvecharamovereallyfast
    $ renpy.pause (0.4)
    show yuukoshang happy_down at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.5) with dissolvecharamove
    $ renpy.pause (0.3)
    show yuukoshang invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.5) with dissolvecharamove
        
    show emi basic_happy at tworightsit 
    show rin basic_absent at twoleftsit 
    with dissolvecharamove
    
    
    "She deftly lowers all items down on our tiny table before bowing again and leaving to serve the other customers."

    "Emi has been eyeing her strawberry tart very hungrily all this time, but somehow she managed to contain herself until the waitress was out of sight."

    show emi basic_closedgrin at tworightsit with charachange
    
    "She jumps in with breakneck gusto, while I content myself to pouring tea for everyone and placing the straw in Rin' s cup."

    show rin basic_deadpan at twoleftsit with charachange
    
    "Rin looks at the way the tea swirls round and round in her white china cup, her eyes half closed, almost like she is being hypnotized."

    "I pick up my fork too and taste a bit of my own cake. It's not bad at all, even though it's a bit too sweet."

    show emi basic_happy at tworightsit with charachange
    
    emi "Itsh very good."

    "She is smacking her lips, already halfway through her slice even though it's not exactly small."

    emi "I want to taste some of that too."

    play sound sfx_slide2

    show emi excited_happy_close at tworightsit
    show rin basic_absent at twoleftsit
    with characlose

    show emi basic_closedgrin at tworightsit
    show rin basic_awayabsent at twoleftsit
    with charachange
        
    "Before I get to respond, she has struck with her fork straight at my delicious cheese cake and escaped with a piece."

    show emi basic_closedhappy at tworightsit
    with charachange
    
    emi "This is delicious too."

    "The insolence is outrageous, but the gentleman in me allows for no retaliation."

    "I frown at her angrily, and she sticks out her tongue impishly."

    "Today Emi is even more hyper than usually. Maybe it's because of the long wait at the art shop?"

    "The tea is hot and good even though I don't usually care that much for tea, and the atmosphere in the café is very relaxing."

    "I don't mind spending the rest of the afternoon here, not even after Emi orders her third piece of strawberry tart and Rin spends most of the time staring fixatedly at the rain streaming down from the heavens."

    stop music fadeout 5.0
    stop ambient fadeout 5.0
    
    "Even the waitress rolls her eyes at the third piece of tart disappearing to Emi's bottomless tummy just as quickly as the preceding two."
    
    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')
    play ambient sfx_rain fadein 1.0
    scene bg suburb_shanghaiext_rn
    show rain
    with shorttimeskip

    "Despite the passing of time, when we step out of the doors of Shanghai it's still raining outside, and just as heavily as it did several hours ago."

    "With no other options available to us, we try to fit ourselves under my umbrella and start the long walk back."

    scene bg school_road_rn
    show rain
    with locationchange
    
    play music music_dreamy fadein 2.0
    
    "The raindrops hitting on the cloth hanging above us seem to drum in rhythm, although I know it's just a game of my imagination."

    "The two girls on my either side feel warm against the cool air, and I have to try my best to act naturally."

    scene bg school_gate_rn
    show rain
    with locationchange
    

    "We make it back to the school, but not exactly dry. I am mostly not soaked as I had to stay in the middle and hold the umbrella, but both of the girls are quite wet."
         
    scene bg school_courtyard_rn
    show rain
    with locationchange
    
    "Emi seems a bit anxious as her body feels very tense against my side. Maybe we were walking too slowly back?"

    hi "Too bad it had to rain on your parade."

    "She doesn't look too sorry herself."

    show emi basic_grin_rn at twoleft
    show rin basic_absent_rn at tworight
    with charaenter
    
    emi "Never mind! But now I really have to go and work out a bit, or I can't forgive myself for eating all that cake."

    hide emi with charaexit
    show rin basic_absent_rn with dissolvecharamove
    
    "She skips away from under the protection of my umbrella and quickly runs towards the dormitories."

    "Suddenly, Emi seems to remember something as she stops and spins around."

    show rin basic_awayabsent_rn at tworight with dissolvecharamove
    show emi basic_happy_rn at twoleft with charaenter
    
    emi "See you tomorrow!"

    emi "Come eat lunch with us on the roof! I'll get enough for three, or four."

    hide emi with charaexit
    show rin basic_absent_rn with dissolvecharamove    
    
    "Me and Rin are left looking at her wave her hand and speed of again. I can't conceive why she is constantly in such a hurry."

    "If Emi had waited for a little while longer, she wouldn't have gotten drenched in the rain as I could have walked her back to the dorm."

    show rin basic_deadpan_rn with charachange
    
    rin "I must go to dry myself."

    #Actually the hand sleeve originally wet was her right. But the left looked better. - Kelper
    
    "She looks disapprovingly at the wet side of her shirt. Rainwater is dripping from her left hand sleeve and the strands of her short hair, making Rin look a bit sorry."

    hi "Err, would you like me to walk you there so at least one of you won't get any more wet?"

    show rin basic_deadpannormal_rn with charachange
    
    rin "If you are happy with it."

    "I decide that I am, walking alongside Rin past my own dorm to the senior girls' dormitory."

    "I had a good time today, I think."
    
    scene bg school_dormext_full_rn
    show rain
    with locationchange
    
    show rin basic_deadpannormal_rn with charaenter

    hi "Was this really it? I mean, in the end we didn't do anything special for Emi's celebration."

    show rin basic_deadpancontemplation_rn with charachange
    
    rin "Normal things are sometimes special enough."

    "The expression gives me a pause."

    hi "Yeah, I guess Emi is the type who can appreciate any kind of thing."

    rin "I guess so too."

    "Rin walks up the steps to the door, looking over her shoulder one more time."

    show rin basic_deadpanamused_rn with charachange
    
    rin "See you tomorrow."
    hide rin with charaexit
    
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    #$ renpy.pause(2.0)
    window hide dissolve    
    scene black with Dissolve(1.5)
    return

label en_R13:
   
    scene black
    $renpy.pause(1.0)    
    scene bg misc_heartattack_ni 
    with Dissolve (1.5)
    $ renpy.pause(1.5)    
    $ renpy.music.set_volume(0.1, 0.0, channel='music')  
    play music music_rain
    $ renpy.music.set_volume(0.0, 0.0, channel='ambient')    
    play ambient sfx_heartfast
    $ renpy.music.set_volume(1.0, 15.0, channel='ambient')
    
    #DREAM

    #blah, centered/nvl, black/dream backgrounds etc
    
    centered "Am I awake or am I dreaming?{fast}" with Dissolve(2.5)
    
    centered "I am not asleep, but not exactly awake either.{fast}" with Dissolve(2.5)
    
    centered "For one reason or another, my brain is capable of only this much rational observation.{fast}" with Dissolve(2.5)
  
    centered "I can't wake up even if I wanted, but this feeling is nauseating, like a bad dream except I am not dreaming.{fast}" with Dissolve(2.5)
   
    centered "I must relax, shed it off my mind.{fast}  " with Dissolve(2.5)
    
    scene black with Dissolve(2.0)
    
    stop music fadeout (6.5)
    #a pause here
    centered "Sleep overtakes me again…{fast}" with Dissolve(2.5)
    scene black
    with Pause(6.0)
    stop ambient fadeout 5.0
    with Pause(5.0)
    
    $ renpy.music.set_volume(1.0, 0.0, channel='music')

    #skip ahead. This next bit is fast forward, if it is too contracted, I could expand it.
    
    scene bg school_dormhisao
    with openeyeslow
    window show dissolve
    "The dreary weather seems to have been only temporary, as the clear blue sky of this Monday morning proves."

    "However, I don't feel as dazzling as the weather."

    "The lack of sleep, combined with the recurring nightmares is an eyesore, as it cuts into the rest I get pretty badly."

    "I wonder if I could get some medication for that… if there even is a drug that could make me sleep better."

    "That reminds me…"
    
    "\“Take the morning pills.\”"

    "…"

    "They taste as bad as every morning."
    
    scene bg school_scienceroom
    with fade
    
    play music music_normal fadein 1.0

    "Today the morning classes are of my least favourite subject: English. I count the steps to the main building like a prisoner counts the tiles in the ceiling."

    "Unsurprisingly, the classes are just as awful as every morning."

    "Luckily, just as all good things have to come to an end, so have the bad things."

    play sound sfx_normalbell

    "Lunch bells ring, not a second too soon, and I exit from the classroom towards the stairwell at the end of the hallway."
    
    scene bg school_hallway3
    with locationchange

    "Climbing the steep, dark stairs to the roof feels like a ritual of… not exactly absolution but something akin to that. It is strangely liberating."
    
    scene bg school_staircase1
    with locationchange

    "I trudge to the top, leaving all worldly worries to the ground, or something."
    
    play sound sfx_dooropen
    $ renpy.pause (1.0)
    play sound sfx_door_creak
    play ambient sfx_rooftop fadein 1.0
    scene bg school_roof with locationchange
    #should meters be feet, or yards? I am constantly using both the metric system and the imperial system in parallel and the mishmash bothers me
    
    #Don't worry about it, unless some alpha tester complains. But, if you must, it'd be yards -Irina

    "The precious few meters that separate the rooftop from the third floor below must be instrumental to the effect." 
    
    "The chain link fence allows for a grand view over the treetops, all the way to the grey silhouettes of the downtown further away."

    scene bg misc_sky at Fullpan(20.0) with locationchange
    
    "The silvery blue sky seems to be a mere arm's reach away."

    "The rooftop might not be the top of the world, but for a small scale thing like my lunch break it's more than enough."

    "Only the sounds of the lunch break echoing from the cafeteria remind me of being in the school."

    "Maybe I really am six meters closer to heaven here."

    scene ev rin_roof_boredom with Dissolve(2.0)
  
    "Rin, too, is enjoying the closeness of the sky, lying on the rooftop not far from the bell tower."

    "She is watching the sky, or the clouds lazily drifting above, or both. Or sleeping."

    "I walk to take a look at her."

    show hisao_shadow with charaenter
    with Pause(1.0)
    
    "Two large, dark green eyes flicker about from below her short bangs. She must be awake. They move slowly to glare at me, proof of Rin acknowledging me."

    show ev rin_roof_doubt with charaenter
    with Pause(1.0)
    
    hi "Hi."

    "I know better than to wait for a response, and Rin doesn't seem to be in the mood to offer one either."
    
    show ev rin_roof_boredom with charaenter
    with Pause(1.0)
       
    hi "Where's Emi?"

    "The question is warranted, as the person who promised me delicious lunch is mysteriously missing."

    rin "In her room."

    hi "Did she have something else to do?"

    rin "She is sick. I think it's more or less a fever."

    rin "At least she said she wants to die and will not go to class and that I must get her cold medication and tea."

    show ev rin_roof_nonchalant with charaenter
    with Pause(1.0)
    
    "Rin's eyes harden for a moment, and her lips move quickly, whispering a repeat of her last line as if to confirm to herself that she really did say that."
    
    show ev rin_roof_doubt with charaenter
    with Pause(1.0)
    
    rin "Hmm, I seem to have forgot the medication. And the tea. I hope she is not very angry."

    hi "Oh, that's pretty unlucky. It's usually so rare to get the flu in the summer."

    rin "It's probably her body telling her to slow down."

    hi "I thought you said she just had the common cold."

    "She pauses for a while, maybe trying to rethink her nonsensical speculation."

    show ev rin_roof_surprise with charaenter
    with Pause(1.0)
    
    rin "It could be."

    rin "Things just are not always what they look like. Sometimes they are something completely else. I've seen it happen a few times."

    show ev rin_roof_boredom with charaenter
    with Pause(1.0)
    
    rin "This could be one of those cases again."

    hi "Why do you say that?"

    scene bg school_roof at left with locationchange
    show rin basic_absent at centersitlow with charamoveinbottom
    
    "Rin sits upright, crossing her legs and stretching her neck before answering."

    rin "Emi tries very hard."
    
    show rin negative_spaciness at centersitlow with charachange

    rin "Sometimes she tries too hard and overdoes things. I don't think it can be a good thing."

    "Rin's tone is abnormally clear and void of her usual slight drawl. Explaining things is not her forte, so I guess she compensates by concentrating harder."

    show rin basic_absent at centersitlow with charachange
    
    rin "After we came back yesterday, she went running to the track."

    hi "In the rain?"

    show rin basic_deadpancontemplation at centersitlow with charachange
    
    rin "In the rain."

    "That sounds a like going a bit too far with keeping up with training regime to me. Emi is a hardheaded one though, so I can see her running in the downpour just because she “had to.”"

    hi "Well, that's obviously overdoing it. And also the probable reason for her cold."

    hi "But isn't it a good thing that she has something she loves to do?"

    hi "Generally speaking, of course."

    "Rin shrugs, obviously not convinced."

    show rin relaxed_nonchalant at centersitlow with charachange
    
    rin "But what about everything else?"

    hi "What else?"

    rin "Everything that is not running."

    show rin relaxed_doubt at centersitlow with charachange
    
    rin "What if she never reads the book she would love the most? What if she never comes up with another hobby she would like? What if she never finds romance?"

    "Her concern is understandable, looking at how Emi got herself ill after getting drenched in the rain just because she wanted to go running, but still…"

    hi "I don't understand why you are so worried about a thing like that. Aren't you too painting all the time?"

    show rin basic_absent at centersitlow with charachange
    
    rin "It's all right. If I don't find romance I can always make a living out of my loneliness with paintings."

    show rin basic_deadpanamused at centersitlow with charachange
    
    rin "People who write books do it all the time."

    "Her answer surprises me. She sounds like… I don't know… Kenji, or even worse…"

    hi "That sounds a bit cynical. Are you sure you are not learning from me?"

    show rin relaxed_disgust at centersitlow with charachange
    
    rin "I hope not."

    "Her sincere answer makes me laugh."

    hi "So, I take it we don't have lunch now?"

    show rin relaxed_nonchalant at centersitlow with charachange
    
    "Rin shakes her head to confirm my suspicion."

    show rin basic_absent at centersitlow with charachange
    
    rin "Are you hungry?"

    hi "Not really."

    rin "We don't have lunch unless we go to the cafeteria."

    stop music fadeout 4.5
    
    "I am hungry, but not enough to make the trip downstairs and having to suffer the terrible cafeteria food."

    hi "It's fine with me. I'll fast."
    
    scene bg misc_sky at Fullpan(40.0)
    with dissolve
    play music music_twinkle fadein 2.0
    with Pause(4.0)     
    #A pause or something here, fade screen to sky, I dunno. Several seconds.

    "What does one do on a lunch break if not eat?"

    "It turns out, between the two of us, that we don't know."

    "Neither seems to want to lay down and look at the clouds like we have done before, not even Rin, even though she seems to enjoy the superficially meaningless way to pass time."

    "It turns out that we are not needed. Time passes still, even though there is no conversation to fill the silence between ticks of the clock, no stupid activities like cloud-gazing to spend the minutes between now and next."

    "I wonder why, more often than not, we don't speak much at all."

    "Maybe it's because it's always so difficult to come up with something to talk with Rin. She and I are on such different wavelengths that nothing seems to be on a common ground."

    "Maybe it's because—{w=0.2}{nw}" #reminder for the potential {nw} break

    play sound sfx_scratch
    stop music
    
    rin "You came here anyway."

    play music music_ease fadein 2.0
    
    scene bg school_roof with locationchange
    
    show rin basic_awayabsent at centersitlow with charachange
    
    "The interjection at my though process comes at a bad time, I was so engrossed with my contemplations about us not talking, that Rin suddenly talking catches me totally off guard."
          
    hi "Excuse me?"

    show rin basic_absent with dissolvecharamove
    
    rin "You came here anyway, even though you are not hungry."

    "Her point, if there is one, eludes me. Why would I have stood up her, hypothetical Emi and — sadly — even more hypothetical lunch even if I wasn't starving?"

    hi "Well, you came here as well. And you knew that there wouldn't be food."

    show rin basic_deadpancontemplation with charachange
    
    rin "Lunch break is not only for food."

    hi "Now you answered your own question."

    show rin basic_surprised with charachange
    
    "My clever reversal obviously impresses her, as a hint of a smile appears in the corners of her mouth."

    show rin basic_deadpanamused with charachange
    
    rin "I really did."
       
    play sound sfx_warningbell

    "There is no more time to contemplate what lunch break actually is for, as the bells burst out into the melody signaling the end of lunch."

    "They're too noisy for comfort here on the roof, but certainly loud enough to be heard even at the dorms."

    show rin basic_absent with charachange
    
    hi "Damn, already? Better to go."

    "I stand up reluctantly, but knowing that tardiness leads to scolding if I am late for the social studies class."

    hi "See you in the club after classes."

    "I dust off my pants, wondering why is it necessary to sit on the rooftop when there is an array of admittedly uncomfortable benches available."
    
    scene bg school_staircase1
    with locationchange

    "Something I almost forgot already comes to my mind, giving me a pause halfway to the stairs."

    "Despite the urging hurry to go to class before the teacher arrives, I feel compelled to turn back again and throw a question to Rin, who hasn't made a move to stand up and possibly go to her own classes."

    scene bg school_roof with locationchange
    show rin relaxed_nonchalant with charaenter
    
    hi "Hey, do you think we are closer to the heaven up here?"

    "Rin turns to estimate the heavens, maybe on reflex, maybe to make the figure of speech into something more tangible to her."

    show rin basic_absent with charachange
    
    rin "I know a better place."

    scene bg misc_sky at Fullpan(40.0) with locationchange
    
    "Maybe an esoteric thing like this can be tangible to someone like Rin."

    hi "You do? Well, show it to me sometime."

    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene bg school_staircase1 with locationskip
    
    "I leave Rin sitting behind on the rooftop and hurry downstairs."

    window hide dissolve
    
    scene black with dissolve
    
    return

label en_R14:
    
    scene black with dissolve
    $ renpy.pause(1.0)
    
    scene bg school_scienceroom with Dissolve(2.0)
    
    play music music_daily fadein 2.0
    with Pause(1.5)
    window show dissolve   
    "..."
    scene bg school_hallway3
    with shorttimeskip

    #Again, open this scene with something that makes it clear that time passes in class, like a slideshow.
    
    "The hallway slowly empties of people after the last classes of the day are over, but don't feel like going into the arts classroom just yet."

    "I am left alone."

    "I am a bit too tall for the old desks at the classrooms so my legs tend to get sore after sitting all day. Better to flex my muscles before I have to sit down again."

    "Besides, I don't even have anything to do in the classroom since I don't know the other people."

    "It's funny, despite Rin saying that I would probably like the other club members, I ended up sticking with her through almost all the club meetings."

    "At first it was maybe because she, like me, was always alone while everyone else was not, but it soon became apparent that she doesn't mind being alone."

    "I lean against the wall, scratching my tickling ear. As much as I'd like to think that it's only my inner masochist raising its ugly head, the truth is that Rin has grown on me, even if it's just a little."

    "It's not that her strangeness is any less strange, I just am more accustomed to it."

    "Despite her uncanny ability at frustrating me, I like being with Rin."

    "Nomiya appears from the stairwell, walking this way very briskly. It must be time for the club meeting."

    show nomiya smile at Slide(0.3,0.5,0.5,0.5,1.0) with charaenter
    
    no "Good afternoon, Nakai."

    hi "Good afternoon, sensei."

    "I note that he has learned my name only now, although I think he has used it before too."

    "Well, that makes more sense as Nomiya seems to have way less students to take care of than most other teachers."

    "Instead of going straight in, he stops at the door and turns to talk with me."

    no "How are you today?"

    hi "I'm fine thanks."

    "He smiles, seeming happy at my well-being, despite my answer being just the automated one, an empty thing you say when someone asks you how you are doing." #wellbeing -> well-being

    no "Good, good. So, did you talk with Tezuka about the thing I mentioned last time?"

    "Oh. I had forgotten it totally since I didn't see Rin until yesterday, and then, well, I had forgotten it."

    hi "Sorry, sensei, I haven't. I forgot it completely."

    show nomiya serious with charachange
    
    "Nomiya doesn't look too pleased at my confession. His frown makes me uncomfortably conscious of the fact that I let him down."

    show nomiya frown with charachange
    
    no "That's not good. Maybe I didn't stress enough how important this is potentially to Tezuka. Surely you'd like to support her as well. You are friends, right?"

    "Friends? I don't know… at least I haven't thought of it like that."

    "It's more like me and Rin just tend to hang around each other irregularly, talking, or not, about something that more often resembles some crazy twisted mutation of philosophy rather than normal, everyday things that friends talk about."

    "I don't know how to respond, but to my relief I don't have to as Nomiya pushes his frustration away and attempts to smile reassuringly."

    show nomiya smile with charachange
    
    no "Oh well, no matter. But please, do try to persuade her if you can, as I am at my wit's end I'm afraid."

    "I manage to nod at him, making a mental note that I really bring it up with Rin."

    no "Enough of that, we are almost late."

    "Nomiya conjures a brilliant smile on his lips just before he enters the classroom while I sneak to my usual seat with considerably less ado."

    scene bg school_classroomart at left
    with locationchange
    show nomiya smile with charaenter
    
    no "Good afternoon everyone! I hope everyone is well?"

    "The club members mumble their hellos and sit down, waiting for the teacher to continue."

    show nomiya talk with charachange
    
    no "So, as I unfortunately had to leave you last Thursday, I'd like to have a look at what you did and then we could continue to improve on those works, if possible."

    hide nomiya with charaexit
    scene bg school_classroomart with dissolvecharamove
    
    "Everyone shuffles to get their materials and works from the last time, creating a hustle."

    "I have to fetch Rin's oil painting in addition to my own stuff. It's heavy and cumbersome, but I get it to our seats unscathed."

    "I am not really in the mood to continue the watercolor painting from last time, but I can't think of any other thing to do right now so I sit down on my seat to work on it."

    "I get the feeling that I am missing something about how this is supposed to be done, as nothing I do seems to make it look like what I intended."

    "The difficulties I have with the painting make it hard to concentrate, and I soon find my thoughts wander off…"
    
    scene bg school_classroomart with shorttimeskip

    show nomiya frown with charaenter
    
    no "So Nakai, let me see that…"

    "Nomiya has sneaked behind me, and now is leaning down to look at my water colors."

    "He hmms and umms a few times before speaking again."

    show nomiya smile with charaenter
    
    no "I think that you should…"
    
    "I let his critique pass from one ear to another, nodding absentmindedly at the correct places."
   
    "He has good advice about something I should try to make the colours more vibrant, but I don't want to ask him to repeat what he just said as it would be the same as admitting I didn't listen to a word of it."

    hide nomiya with charaexit
    
    "As I watch him pass Rin with only an approving nod before walking to the next victim, Nomiya's request pops to my mind, making me forget about daydreaming."

    show bg school_classroomart at right 
    with dissolvecharamove
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) 
    show prop rin_basearbuds at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    with charaenter
    
    $ renpy.music.set_volume(0.0, 0.0, channel='ambient')
    play ambient music_crappy 
    
    "I glance at the red-haired girl sitting on the floor not three feet away from me."

    "Rin has silver-coloured earphones on, isolating her into a private world of music and painting."

    "She paints in big sweeps over the canvas, her toes almost, but not quite brushing against the wet paint."

    "How am I supposed to talk with her about anything like this?"

    #reminder for possible choice to not take her earphones off.

    "There is only one course of action."

    "I grab the earphones and yank them out of her ears."
    
    
    play sound sfx_blop
    hide prop with Dissolve(0.2)
    $ renpy.pause (0.2)
    stop music
    $ renpy.music.set_volume(0.1, 0.0, channel='ambient')    
        
    show rin negative_annoyed_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
 
    "This gets instant attention from Rin, as she turns around to look at me, her eyes wide with surprise."

    rin "Give those back."

    hi "Hey, I have a question."

    show rin negative_angry_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "I don't want to answer it. Give those back."

    "Her first sentence gives me a pause, and a question that has been bothering me ever since the first club meeting I attended escapes my lips instead of the one I planned to ask."

    hi "You know, I've been wondering why do you never socialize with the other people here."
    
    hi "I don't think I've seen you speak as much as a single sentence to anyone except me or the teacher."

    "Rin stares at the earphones dangling a feet above her head. I realize I'm being pretty rude, but tough cases call for tough measures."

    show rin negative_spaciness_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "They do not interest me. Give those back, I have to paint now."

    "She is still looking at the earphones, even though taking them off was meant to make her pay attention to me. Well, at least she is talking."

    hi "You don't like them?"

    show rin negative_confused_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "It's not that."

    "The look on Rin's eyes tells that she knows that is not a sufficient answer. She looks like she is actually in pain as she tries to think how to explain what she means."

    show rin negative_worried_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "We wouldn't have anything to talk about. Please give those back before I lose this thing inside me that is really good."
    
    rin "It could be good enough to last me to the end of this painting."

    "Does she need the earphones to prevent thoughts from escaping her brain through the ears?"

    "At least Rin is looking at them very yearningly, obviously wanting them back so she can return to her seclusion on the floor."

    "I won't let her."

    show rin negative_angry_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "Give those back or I won't forgive you. Don't you understand? I have to paint."

    "Something about the subtle shift of her usually so monotone voice makes me realize she really means it."

    "Besides, I feel pretty bad about forcing her to talk like this. I guess it's no use, Rin talks only if she will."

    hi "Okay, okay. I understand."

    hi "Sorry."

    "I crouch down and set the earphones on her ears, sweeping the auburn hair covering her ears away so it won't be in the way."
    
    stop ambient
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    
    play music music_daily fadein 2.0

    show rin relaxed_nonchalant_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) 
    show prop rin_relearbuds at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    with Dissolve(1.2)
    
    "I can feel the tension draining from Rin, almost like every muscle in her body relaxed at the same time"

    show rin basic_lucid_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    show prop rin_basearbuds at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    with charachange
    
    "Rin closes her eyes, letting the music flow in her ears. A deep breath out, and then she opens them again but doesn't look at me anymore."

    rin "Just wait a little."

    "For what? Rin just picks up her brush and returns to work."

    scene ev rin_painting_concerned at Zoom((800, 600), (0, 0, 800, 600), (0, 0, 720, 540), 10.0, bilinear=True) with locationchange
    
    "Another black line is drawn over the canvas."

    "I wait a little while, watching over Rin's shoulder at her work. The little while stretches first to a long while, then to a really long while."
    
    "She paints, her entire being fully concentrated on the brush between her slender toes and the painting coming to life one sweep of a brush at a time."

    scene ev rin_painting_faceconcerned with Dissolve(2.0)
    
    "I don't really understand how Rin takes some idea she has and then is capable of translating it to an abstract painting like that."
    
    "At first glance it looks like a mess of colours and shapes, impossible to interpret as anything, but the longer I stare at it, the better it looks to me."

    "It's still not making sense, but somehow, it's not a mess either."

    scene ev rin_painting_foot at Pan((0, 0), (0, 100), 8.0) with locationchange
    
    "Is this the difference between “art” and “not art?”"
    
    "I glance at my painting, but it doesn't really beckon me to work further. Failure is a failure and there is nothing I can do anymore to salvage it."

    "So, I content myself with watching Rin's feet move."    
    
    rin "I don't like talking."

    scene ev rin_painting_concerned with locationchange
    
    "The single-sentence contradiction strikes as strange to the pedantic part of my brain, but the breaking of silence interests me much more than pointing out the fact."

    "Besides, as Rin is still listening to the music from her earphones, she probably wouldn't hear me either."

    rin "Words are not the thing you want to say. It's something else you want to say, but you have to say words."

    rin "I… know that some people think my words don't really make sense."
    
    scene ev rin_painting_reply with None
    
    extend "{w=0.5}{nw}"
    
    extend " I am not stupid, you know."

    "She turns to me, confirming that she actually addressed her words to me instead of the just talking to the air."

    scene ev rin_painting_base with dissolve
    
    rin "So I try to not to."

    hi "But you talk to me, don't you?"

    "Rin looks at me, frowning like one frowns to a child who asks stupid questions. Her eyes look very sad."

    scene ev rin_painting_concerned with locationchange
    
    rin "I thought you'd have a chance to understand."

    rin "I think I would prefer if…" 
    
    stop music fadeout 2.5

    "She draws in deep breath, interrupting the sentence in the middle of the word."

    rin "A."

    "A?"

    rin "Aaa…{w=1.2}{nw}"

    play music music_rin
    
    scene bg school_classroomart at right 
    show rin relaxed_disgust_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    show prop rin_relearbuds at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    with vpunch
    
    rin "Atchoo!"

    "The sneeze is so loud that everyone else in the room turns to look at Rin, probably trying to determine if that was a hand grenade explosion or what. Luckily Rin had enough sense to not aim at me or the painting."

    show rin relaxed_sleepy_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    hi "Bless you. Are you sick now as well?"

    hi "Anyway, you were saying…"
    
    show nomiya talk at left behind rin with charaenter
    
    no "All right everyone, time to start cleaning up!"

    "Nomiya chooses this very moment to interrupt, stealing Rin's attention over continuing the discussion."
    
    hide nomiya with charaexit

    "Everyone stops whatever they are doing and diligently begin to clean up the classroom."
    
    hide rin 
    hide prop
    with charaexit

    "Sighing, I too start to collect my stuff and turn in my painting. Nomiya tries very hard to conceal his disdain, but there is nothing he could say that I already don't know."

    stop music fadeout 3.0
    
    "When I lift my bag off the floor, Rin has already disappeared with only the large painting propped up against the wall reminding that she was here."
    
    window hide dissolve
    scene black with Dissolve(1.5)

    return

label en_R15:
    
    scene black
    $ renpy.pause (1.0)    
    scene bg school_dormhisao
    with openeye

    window show
    
    play music music_pearly
    
    "Despite my best efforts, the Wednesday morning isn't any better than Tuesday morning, or Monday."

    "I wake earlier than the alarm. Despite the tiredness I can't sleep so I spend what little time I can trying to get fall asleep."
    
    "Just as I almost manage to do it, the alarm clock rings, forcing me to rise and shine."

    "Rising is fine, as my morning routine is mostly on autopilot, but I don't feel particularly shiny today."

    "I wish I could sleep more than five hours a night."
    
    window hide dissolve
    scene black
    with Dissolve (1.0)
    
    $ renpy.pause (0.5)
    
    scene bg school_scienceroom
    with shorttimeskip

    #skipping ahead…

    window show
    
    "The recess between the two morning classes is too short for any meaningful activity, but too long to just sit in the classroom and let my brain rot."
    
    play ambient sfx_crowd_indoors fadein 0.5
    scene bg school_hallway3
    show crowd
    with locationchange

    "The hallway is not much more inspirational, but flexing my stiffened muscles is leagues better than getting them even stiffer by staying seated."

    "Our neighbouring classroom's door opens and the students of 3-4 emerge to fill the semi-crowded hallway even more. It seems their teacher kept them in for a few extra minutes."

    "Emi is amongst them, and she notices me noticing her, which almost makes me look away on reflex."

    "I don't, however, and Emi smiles at me as she happily skips past the other students towards me."

    stop music fadeout 4.0   
    
    "It seems that she has recovered from the cold."
        
    "Emi looks pretty energetic with no sign whatsoever of illness, but it could just be because of the recess."

    $ renpy.music.set_volume(0.5, 0.5, channel='ambient')
    play music music_emi fadein 0.5

    show emi basic_closedgrin at center 
    with charaenter
    
    emi "Hey! Good morning!"

    show emi sad_shy with charachange
    
    emi "Sorry I broke the promise about the lunch on Monday. I got a little sick."

    hi "Nice to see you back on your feet. Feel better now?"

    "She looks fine to me, but I still feel compelled to ask."

    show emi excited_laugh with charachange

    emi "Thanks, yea I do, it was just a cold. Nothing serious."

    "Emi laughs brashly to put some weight on her exclamation."

    "I wonder what would count as serious in Emi's book. She shrugged off the fact that she hurt herself at the track meet just as lightly as this."

    "She seems to be eager to put the topic aside."

    hi "Where are you going?"

    show emi basic_closedgrin with charachange

    emi "I'm going to Rin's room to see if she's awake."

    hi "Oh? She skipped the morning class?"

    "A sheepish smile emerges on Emi's face and she flusters slightly."

    show emi sad_grin with charachange

    emi "Err…not exactly. It seems that she caught that cold I had."

    hi "Oh dear. Well, she was out in the rain as well on Sunday, wasn't she?"

    show emi basic_grin with charachange
    
    emi "Yeah. Anyway, I'm was going to get her some cold medication for her from the Nurse."

    "Medication… damn, did I remember to take my pills in the morning?"

    "I don't have a clear picture of myself reaching for the metal foil sheets on my night table nor popping the pills out of them."

    show emi basic_annoyed with charachange
    
    emi "Oh, that's right."

    "Emi's tone is very serious and she suddenly looks very sullen."

    emi "I heard you almost ruined her painting."

    hi "I… what?"

    show emi sad_annoyed with charachange
    
    emi "You took off her earphones."

    "At first I don't understand what she is talking about, but then I remember."

    hi "Yeah… at the club meeting the day before yesterday, but I gave them back."

    hi "But how does that translate to ruining a painting?"

    "Emi sighs at me, letting her shoulders droop as she apparently is disappointed having to explain what she is talking about."

    show emi sad_pout with charachange
    
    emi "You don't get it do you?"

    "I shake my head… what am I supposed to get?"

    "She pauses, frowning a little."

    show emi sad_shy with charachange
    
    emi "Well, I don't either… but!"

    "Emi contorts her entire face, leaving her mouth half-open in the anticipation of the exclamation she is about to say, as soon as she figures out how to say it."

    "It's funny how her entire thought process can be read from her face."

    show emi basic_grin with charachange
    
    emi "It's like, Rin needs to get a right “feeling” for when she paints."

    "She raises her hands to wiggle the quotation marks around the word “feeling” as she says it, raising her eyebrows in sync."

    emi "It's almost like she can't do anything at all if she doesn't feel like she wants to."

    show emi sad_grin with charachange
    
    emi "Sometimes it has to be the right weather, sometimes it's about food, sometimes it's just about the things she is thinking about."

    emi "This time it probably was about the music, and when you took them off, she almost lost the inspiration or whatever you call it."

    "She ends her explanation with a dismissive wave of her hand."

    hi "Oh… I didn't have any idea."

    hi "That's a strange way to process inspiration."

    "Emi smiles happily at my understanding, then she seems to remember something else as she giggles brightly."

    show emi basic_happy with charachange
    
    emi "Tell me about it, one time she thought the feeling she needed to paint was the smell that you get when you have a headache."

    hi "There is a smell when you have a headache? I have never noticed anything like that."

    show emi basic_confused with charachange
    
    emi "Me neither. Anyway, I had to barge in Rin's room and tackle her down on the floor so she wouldn't bang a hole in the wall with her forehead."

    "Damn, it wasn't even two days ago that Rin was complaining how Emi always overdoes things. Pot, kettle and so on, I guess."

    show emi basic_annoyed with charachange
    
    emi "Anyway, you shouldn't have taken them off. That's not what friends do to friends."

    "I don't fail to notice that Emi herself also ruined Rin's inspiration that time, but maybe it doesn't count if the option is to let her physically harm herself?"

    hi "Is Rin angry with me then?"

    "My question gives Emi a pause. She was so focused on herself being unhappy with me that apparently she hadn't considered Rin's feelings."

    show emi sad_annoyed with charachange
    
    emi "I don't know. I am not sure if Rin even knows how to be angry."

    "A strange thing to say… but true enough. Rin is a pretty mellow personality."

    hi "Yeah, she didn't seem to care about the whole matter at all after I gave the earphones back."

    hi "She just dropped the subject before I even said sorry or anything. Maybe it's fine like that."

    show emi basic_annoyed with charachange
    
    emi "Oh jeez, Hisao you are such a dork!"

    "Emi wags her index finger at me, looking very disappointed."

    hi "What… I thought there was no problem?"
    
    emi "Rin never says what she thinks."

    "Are we talking about the same Rin here? I've always thought of her as pretty vocal of her opinions, when she has them."

    emi "She just doesn't let you know how she really feels, you know. Even if she doesn't know how to be angry at you, she still might be."

    "She keeps on poking me in the chest with her finger, looking very annoyed."

    emi "She told me about you almost ruining the painting, which means that it bothers her. You should apologize properly."

    "The connection is not immediately obvious at me, but who am I to argue with Emi? She knows Rin the best, after all."

    "Suddenly Emi seems to realize that something is amiss. She takes a quick look over my shoulder to the clock hanging on the hallway wall and yelps."

    show emi basic_confused with charachange
    
    emi "Oh geez, now I really gotta go! I'm already going to be late from the next class!"

    show emi basic_happy with charachange
    
    emi "Bye!"
    hide emi with charaexit
    with Pause(1.0)
    
    stop music fadeout 2.0
    stop ambient
    scene bg school_dormhallground
    with shorttimeskip
    #with Fade (1.0, 0.5, 1.0)
    
    play music music_night fadein 0.5

    #fadetoblack
    #[reminder for me, possible choice here to either go to see Rin today/don't go]
    #I dislike this latter part of this scene and I might want to scrap it altogether. It has all the flaws: oneshot pointless side character, boring storytelling and the entire segment itself does almost nothing.

        
    "I skulk the corridor of the senior girls' dorm like a burglar, or perhaps an even more suspicious character."

    "I am a bit nervous for some reason."

    "There is nothing wrong in going to see someone who is ill, there is nothing wrong in going to the dorm building of the opposite sex, but I still feel like out of place here."

    "I am not alone, and while I am not getting too much strange looks from the girls returning to their rooms after the school day, I can imagine their stares in my neck."

    "A problem that earlier didn't come to my mind emerges. There must be about 40 rooms in this dorm building, and I have no idea which one of them is Rin's."

    "All I know is that it's on the same corridor as Emi's room, but that doesn't help at all as I have no clue of her room's whereabouts either."

    "Only one way to solve it."

    #This is bothersome. If the scene looks sucky ingame without the side character sprite, I'll just change it to Misha, Shizune or some other main character

    "I clear my throat pretty unnaturally behind a girl who is standing at the intersection of the first corridor, maybe waiting for a friend or something."

    "She doesn't reckon me though I thought I'd have made my presence clear."

    hi "Excuse me."

    "As she still won't pay attention to me, I walk around to her front, which finally rouses the girl."

    "She looks up to me and raises her eyebrows silently."

    hi "'Scuse me, but would you happen to know where Rin Tezuka's room is?"

    "The girl quickly shakes her head and makes two fast gestures with her hands."

    "Oh dear."

    "She is deaf."

    "I try to sign an apology without knowing what the correct sign even is, repeating “Sorry” and hoping she can read lips. I feel the blood surging to my cheeks."

    "She smiles amusedly at my despair and fishes a small notebook, not entirely unlike the one Shizune uses to communicate with us linguistically challenged, and offers it to me."

    "I accept it thankfully and quickly scribble my question on the paper. She answers just as quickly."

    play sound sfx_paper
    $ written_note("I think I know who you are talking about, but I am not exactly sure. Tezuka is that redheaded amputee from 3-4, or am I thinking of someone else?")

    "I nod at her in relief and she quickly adds one more sentence."

    play sound sfx_paper
    $ written_note("I think I know who you are talking about, but I am not exactly sure. Tezuka is that redheaded amputee from 3-4, or am I thinking of someone else?\n\nIt should be the third corridor down the hallway.")

    "I quickly bow thanks and scurry away before embarrassing myself any more. At least this person was nicer and more understanding than Shizune."

    scene bg school_girlsdormhall
    with shorttimeskipsilent
    
    "There are five doors in the third corridor, all of them looking exactly like each other."

    "If the layout is the same as in my dorm, the first door is the bathroom and the others are normal rooms."

    "One of the doors has a nameplate with “Ibarazaki” and two others belong to people I don't know, Kashiwagami and Yoshida."

    "The unmarked door is hopefully what I am looking for."

    "What am I doing?"

    "Rin's door looks the same as mine, just a simple wooden door."

    "Maybe a tad more intimidating."

    "I ball my hand into a fist and hesitantly raise it to knock on the white-painted door."
    
    play sound sfx_hammer 
    
    "My knuckles rap against the door three times in quick succession. The sudden sound against the silence of the corridor makes me flinch."

    "I wait a bit, glancing down the hallway to see if anyone heard the ungodly loud noise I made."

    "A moment passes, then another, but the door doesn't open."

    hi "Rin?"

    "No answer from the other side."
    
    hi "It's me, Hisao. Are you there?"

    play sound sfx_doorknock
    
    $ renpy.pause(2.0)
    
    "Still no answer."

    "Maybe she is asleep, or not there."

    "Hard to say where she could have gone, though, if she is supposed to be sick."

    "I wait for a little longer, feeling increasingly stupid trying to stare the door open, but to no avail."

    "Maybe I'll come back tomorrow."
    
    stop music fadeout 1.0
    window hide dissolve
    
    scene black with Dissolve(1.5)
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')

    return

label en_R16:
    
    scene bg school_scienceroom
    with fade
    
    play music music_happiness fadein 1.0

    window show
    
    "The afternoon classes are always longer than the morning classes. This is true, regardless on if I count in minutes or in times I doodle some lame scribbles on my notebooks."

    "I can't concentrate on either, so I can't justify not paying attention to Mutou's lecture by claiming that I am practicing my drawing skills."

    "The science class is interesting and all, the problem is with me. I am restless and tired."

    "As Mutou is giving our homework, I realize that if Rin is still sick, I'm going to have to suffer the art club meeting by myself."

    show muto smile with charaenter
    
    mu "Nakai, would you stay for a moment?"

    hide muto with charaexit
    
    "His remark draws raised eyebrows from Misha, who is stuffing her things in her bag right behind me."

    show misha cross_grin with charaenter
    
    mi "What's this? Have you been a naughty boy?"

    "I try to appear as innocent as possible to shake her off."

    hi "I haven't done anything."

    show misha cross_frown with charachange
    
    mi "Speaking of that… why don't you hang out with me and Shizu anymore?"

    show misha sign_smile with charachange
    
    mi "Imagine, two little girls all alone in the student council office…"

    show bg school_scienceroom at right
    show misha invis at left 
    with dissolvecharamove

    "I turn my back to her. I have no illusions about what really would happen if they managed to trick me to helping them again." #at -> to

    "Misha gets the message, it seems, as she doesn't continue pestering me."

    "While the rest of the class leave to their club meetings and activities, I stay behind as Mutou asked."

    "As soon as the door shuts behind the last student, he raises his eyes from the notes he was writing."

    show muto smile with charaenter
    
    mu "Oh, don't look so worried. Relax."

    "Mutou sits completely upright and leans back on his chair, then he decides it's better to stand up after all."

    show muto normal with charachange
    
    mu "I thought I'd check up on you since you are a new student and we haven't really talked much."

    mu "How have you been doing?"

    "His directness doesn't come off as unfriendly at all, not entirely unlike Rin's bluntness."

    "Although Mutou's way of talking to his students is more likely intentionally learned style of speech than natural inconsiderateness."

    #next line refers to an event that has not been written yet.

    hi "I am fine, I guess." # I had some trouble with my medication but it's fixed now."

    mu "And school? You were away from school for a while if I remember correctly?"

    hi "Ah… school is school I guess. I'm doing all right I think."

    show muto smile with charachange
    
    "My modesty makes Mutou smile."

    mu "Oh, yes. That reminds me, would you like to join the science club? You are absolutely brilliant at it."

    hi "Well… I already joined the art club."

    show muto irritated with charachange
    
    "Mutou's eyes sharpen suddenly like a hawk's. He starts to mutter to himself, clenching his fist."

    mu "That bastard Nomiya… I'll make him pay for this…"

    "He collects himself and clears his throat after noticing my bewildered face. Are they mortal enemies?"

    show muto normal with charachange
    
    mu "Well, it can't be helped. Besides, it's not like there are any other members. It'd have been just you and me. Too bad though."

    "That's one more reason to decline."

    show muto smile with charachange
    
    mu "Oh, that's right! My class had most of the career planning talks and such a few weeks before you transferred in so you missed all of that."

    mu "What are your plans after graduating? We teachers are supposed to support the students on stuff like this…"

    hi "Uhh… I haven't decided exactly. My parents are saying that I should get a good education and I don't really disagree."

    hi "I sorta thought I'd go to a university, but I haven't decided on the subject yet."

    show muto normal with charachange
    
    mu "Have you considered something like physics? I'm sure you'd do fine."

    hi "No… I'm not really interested about that."

    show muto smile with charachange
    
    mu "Well, you should think about it. Come chat with me anytime."

    "I take his remark as a permission to leave and quickly step outside."
    
    scene bg school_hallway3
    with locationchange

    "I wouldn't have suspected that Mutou actually is concerned about his students."

    "At most stuff like career counseling would have been unavoidable evil for him."

    "Standing at the corridor, I am faced with the choice to either go late to the art club meeting and endure that alone, or go downstairs and do something else for the rest of the afternoon."
    
    scene bg school_girlsdormhall
    with shorttimeskip

    #reminder for a path split here (or at R15 yesterday), goto club/go see Rin

    "My steps through the corridors of the girls' dorm feel more natural today."

    "I peeked in the art club's classroom, but she was not there."

    "Thus, no real reason for me to go either."

    "The third side corridor down the hall is as desolate as yesterday."

    "Today the door, too, is slightly less intimidating."
    
    play sound sfx_hammer 
    
    "I place a knock on Rin's unmarked door and wait."

    play sound sfx_rustling
    
    "After a few seconds of silence I hear something rustling inside the room."

    play sound sfx_dooropen
    
    "The door squeaks open and I find myself staring at Rin, who is staring at me."
    
    stop music fadeout 2.0

    "She looks like she has just woken up, with her hair all messed up and…"
    
    # If there ever is a separate Rin's room BG, it'd be here. 
    
    show rin basic_deadpanamused_pan at Slide(1.05,1.0,1.0,1.0,0.5) with charaenter
    
    "…and no clothes on."

    #Rin needs a sprite set with only her uniform shirt on (no pants, but panties are on in case they would show in the sprite) for this scene. The sprites might be reused later on. If you want to bother, draw the shirt partially unbuttoned too. Also this scene uses one special expression that (hopefully) won't be used anywhere else.

    "…"

    "…"

    "…"

    show rin basic_amused_pan at right with charachange
    
    rin "Hellooooo."
    
    play music music_rin fadein 0.5
    
    "There is a strange, stupid looking smile on Rin's face, the reason of which I'm not exactly sure."

    "Rin smiles so rarely that every one of them seems to be out of place, especially now, considering her partially undressed state that makes me feel extremely conflicted about if this was a good idea."

    "Her cheeks are red, probably from the fever."

    hi "Um, hi."

    show rin basic_absent_pan at right with charachange
    
    "Now what? I didn't plan anything further than this point and Rin is staring at me with those expectant eyes of hers again, although something about this situation give me very strange vibes."

    "Her eyes are even more vacant than usual and she seems to have a hard time focusing them on anything."

    "Rin's lack of clothes disturbs me but as she herself doesn't act embarrassed, why should I?"

    hi "Err, I thought I'd pay you a visit since you missed the art club."

    "Rin doesn't show any sign of recognizing what I just said, making me uncertain if she didn't understand me or did she just not hear me."

    show rin basic_deadpan_pan at right with charachange
    
    rin "Was there something interesting there?"

    "The blurry words flow out of her lips slowly and uncontrollably."

    hi "Ah… I didn't go either. The club meeting time is actually right now but I thought I'd rather skip it."

    show rin basic_deadpansurprised_pan at right with charachange
    
    rin "Why?"

    "Why, you ask… I content myself to shrugging my shoulders."

    show rin basic_deadpan_pan at right with charachange
    
    rin "Whatever."

    show rin invis at rightedge with dissolvecharamove
    
    "She turns on her heels and withdraws from the door, walking back inside the small room."

    "From the doorway I can see her walk to her bed and half fall down, half sit down on the messy pile of bedsheets."

    "Maybe she was sleeping."

    "The open doorway seems to be more of an obstacle than the closed door was, but as Rin doesn't say anything else, I step through it into her room."

    scene bg school_dormrin with locationchange
    
    "Rin is leaning against the wall on her bed, leaving the only chair in the room for me."

    "She keeps her quiet even after I sit down so maybe she meant to invite me in but just forgot to actually say it aloud?"

    "The room is very normal, which strikes me as strange."

    "I expected something more… different."

    "There are some paintings, undoubtedly Rin's, hanging on the walls but that's about the only real difference between her room and mine."

    show rin basic_deadpanamused_pan at twoleft with charaenter
    
    rin "Nobody has visited me before."

    "The breaking silence draws my attention from the room to its inhabitant, who currently seems to be in the middle of a very profound thought process."

    show rin basic_awayabsent_pan at twoleft with charachange
    
    rin "Actually that was not true, but Emi doesn't count."

    show rin basic_deadpan_pan at twoleft with charachange

    rin "Can't put my bra or pants on otherwise."

    "She looks groggily down at her legs which are only halfway covered by the bedsheets."

    show rin basic_absent_pan at twoleft with charachange

    rin "Which is probably why I have neither on, now that I think about it."

    "I haven't failed to notice that Rin doesn't have her shirt buttoned up either, and trying to remind myself where her eyes are is becoming increasingly hard."

    show rin relaxed_sleepy_pan at twoleft with charachange

    rin "She came to wake me up at half past seven!"

    show rin relaxed_doubt_pan at twoleft with charachange

    rin "Can you imagine that?"

    "She pauses for a while and glances up at my dumbfounded face."

    show rin basic_lucid_pan at twoleft with charachange

    rin "On second thought, you probably can."

    hi "Well yes, that's the usual time to wake up if you want to go to the morning classes."

    "I'm trying to sound as reasonable as possible to counteract Rin's unreasonable annoyance."

    show rin basic_deadpanupset_pan at twoleft with charachange

    rin "Told her to sod off."

    show rin relaxed_nonchalant_pan at twoleft with charachange

    rin "She gave me some medicine and told me to take them."

    show pills alpha at centersitlow 
    
    "I follow her eyes to her night table upon which a suspiciously empty metal foil sheet of medication lies."

    show pills with dissolvecharamove
    
    "I pick it up and turn it around see what kind of medication Emi brought."

    "Active ingredient… Codeine?"

    show pills alpha at centersitlow with dissolvecharamove
    hide pills with None

    hi "You took all of these?" #ate -> took 

    show rin relaxed_surprised_pan at twoleft with charachange

    rin "She told me to take them. I was hurting really bad in the morning, but now I think I don't hurt anymore."

    show rin relaxed_sleepy_pan at twoleft with charachange
    
    rin "Actually… I think I'm feeling juuuust fine."

    "Her head lolls around a round, looking like she is trying to stretch her neck muscles or pass out."

    "A full sheet of this stuff? Can that be safe anymore? At least it's bound to have some side effects… which I'm afraid I am witnessing right now."

    show rin basic_deadpanupset_pan at twoleft with charachange

    rin "I am feeling just fine… I am fine…fine… just someone take this buzzing away from my head."

    "The annoyed expression returns to Rin's face."

    show rin basic_upset_pan at twoleft with charachange

    rin "It's like many of those insect things… or one really big insect thing."

    show rin basic_awayabsent_pan at twoleft with charachange

    rin "With lots of wings. Very much colour and everything."

    show rin basic_absent_pan at twoleft with charachange

    rin "And shapes. I like shapes."

    show rin basic_deadpanamused_pan at twoleft with charachange

    "She smiles slightly at the last observation. The small pause in her monologue is not enough for me to dare saying something that potentially but not likely could salvage this discussion."

    show rin basic_amused_pan at twoleft with charachange
    
    rin "I saw some nice shapes yesterday."

    show rin basic_awayabsent_pan at twoleft with charachange

    rin "What did you see yesterday?"
     
    show rin basic_deadpansurprised_pan at twoleft with charachange

    rin "Hisao."

    "She utters my name as an afterthought, possibly to make clear that she is now addressing me instead of just talking her mind to whoever might be listening."

    hi "I actually came by yesterday as well. I knocked on the door, but you were not here or something."

    "Rin raises her eyebrows, making them almost disappear under her short bangs."

    show rin basic_awayabsent_pan at twoleft with charachange
    
    rin "Just come in."

    hi "What?"

    show rin basic_absent_pan at twoleft with charachange
    
    rin "There is no lock on the door."

    hi "What?"

    show rin basic_deadpan_pan at twoleft with charachange
    
    rin "There is a lock on the door."

    "I resist the urge to say “What?” for the third time."

    show rin relaxed_nonchalant_pan at twoleft with charachange
    
    rin "It is not locked, but it exists."

    rin "On the door."

    show rin basic_absent_pan at twoleft with charachange

    rin "I have only one key, but two people must come in."

    show rin basic_deadpan_pan at twoleft with charachange
    
    rin "Emi comes in sometimes."

    rin "As I already said."

    show rin basic_deadpancontemplation_pan at twoleft with charachange
    
    rin "You must pay more attention to what I say."

    rin "Otherwise I repeat myself."

    "The sentences come out of her mouth, and probably her brain, one at a time with a small pause between each, making her gibberish hard to understand."

    "I nod in understanding thought, despite not being entirely sure where she got the impression that I didn't know that Emi visits Rin occasionally."

    show rin basic_deadpanupset_pan at twoleft with charachange
    
    rin "And that is no good because then I can't think of any new thoughts."

    "Rin finishes with one more line, getting to say the last word over herself, an impressive display of what I can only describe as mental shadowboxing."

    "The odd situation has left me speechless since about the time Rin opened her mouth for the first time, and now that she herself doesn't seem to have anything more to add, silence takes over the small room."

    "It makes me glance around Rin's room in an attempt to find something to talk about."

    "The room is about as small as mine is. The big window, which takes the wall furthest from the door, gives to east just like mine."

    "About a dozen paintings, most in Rin's signature abstract style are taking up the rest of the wall space."

    "A faint smell of art… of paint and paper is floating in the air despite Rin saying that she doesn't like painting in her room."

    "Maybe she does anyway, sometimes."

    "Rin is not very concerned about tidiness it seems, as everything she owns seems to be arranged in various piles around her room."

    hi "Your room looks nice."

    "It's an empty sentence one uses to fill empty spaces in conversations, but my wits are failing me pretty hard right now."

    show rin relaxed_nonchalant_pan at twoleft with charachange
    
    rin "Yeah. Would you like me to show you the places?"

    "She looks down at her half-open shirt quizzically, making me inadvertently follow her gaze to her chest."

    show rin relaxed_sleepy_pan at twoleft with charachange

    rin "Oh… I guess I already did."

    "I can't deny that, no matter how hard I tried to act properly."

    "I want to watch, but I don't want to."

    "I am not supposed to."

    "These are the conflicts in a man's life. How wretched."

    "It is best to not take advantage of Rin's careless state though."

    "I will not watch. At least not too much."

    show rin basic_absent_pan at twoleft with charachange
    
    rin "It is very nice that you came to see me."

    show rin basic_deadpancontemplation_pan at twoleft with charachange
    
    rin "It makes me feel very… what's that word… you know, the one about things and stuff."

    show rin basic_lucid_pan at twoleft with charachange
    
    rin "Anyway, you came."

    "Rin's blabbering makes me remember that I actually came here for a reason, although it was half prompted by Emi."

    hi "Hey, about the club meeting on Monday."

    show rin relaxed_surprised_pan at twoleft with charachange
       
    rin "Hmmm?"

    "Rin doesn't seem to be exactly attentive right now, but it's not like she ever is."

    "I continue to just get it off my chest."

    hi "Sorry about almost ruining your painting."

    show rin basic_deadpan_pan at twoleft with charachange

    "Rin tilts her head and furrows her brows, looking like she doesn't get what I'm talking about."

    rin "I don't get what you are talking about."

    hi "The earphones."

    "Understanding lights in her eyes and she waves her head around in the way that could be interpreted as anything."

    show rin relaxed_sleepy_pan at twoleft with charachange
    
    rin "It's ok."

    show rin basic_lucid_pan at twoleft with charachange
    
    rin "I am feeling all right about it."

    rin "It's just sometimes a bit hard to keep my thoughts the way I like them."

    show rin relaxed_nonchalant_pan at twoleft with charachange
    
    rin "They are not very straight, at least most of the time."

    rin "Not that I want to have them straight… I just wish they were at least in some shape."

    rin "Round is fine too."

    show rin relaxed_boredom_pan at twoleft with charachange
    
    rin "My thoughts are very messy."

    show rin relaxed_sleepy_pan at twoleft with charachange

    rin "Messy."

    show rin invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.3, ypos=0.63) with dissolvecharamove

    play sound sfx_pillow

    scene ev rin_high_frown with locationchange
    
    "She repeats the word melancholically, then flops lying down on her bed and nuzzles her head against her pillow, shutting her eyes."

    rin "Enough. Tired."

    scene ev rin_high_oneeye with locationchange
    
    "She opens one of her eyes to look at me."

    rin "Was it you who likes to look at sleeping girls? Or someone else?"

    rin "Maybe there were many of those."

    scene ev rin_high_frown with locationchange
    
    rin "I can't remember."

    rin "You can stay if you want."

    hi "Nono, I'll leave. I have to… do homework anyway."

    stop music fadeout 2.0

    scene bg school_dormrin with locationchange

    "I stand up from the chair and take a step towards the door."

    rin "Wait."

    "Her request stops me on my tracks, not that I intended to scoot off right away."

    scene ev rin_high_grin with locationchange

    "I look over my shoulder at the girl lying on her bed, again with the strangest kind of smile on her features."

    "She should smile more often."

    rin "I can walk you to the door."

    scene ev rin_high_grinwide with locationchange
    
    rin "It's the least a gentleman can do."

    "Her remark makes me smile as well. The distance to the door is maybe three feet and I already am at an arm's length from the handle."

    scene ev rin_high_smile with locationchange
    
    "Rin herself giggles, making me certain beyond absoluteness that her cold medication dosage was way too heavy today."

    rin "I have always wanted to say that."

    scene bg school_dormrin with locationchange

    show rin invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.3, ypos=0.63) with None
    
    show rin basic_deadpandelight_pan at twoleft with dissolvecharamove
    
    "Difficultly and slowly, Rin rises first to sit again, then she stands up even more difficultly and slowly."

    "Indecency draws my eyes instantly to the curve of her thighs and the striped panties, from where my manners force me to lift my gaze back to Rin's eye level."

    "Rin is standing, although barely. It looks like she has trouble keeping her balance for some reason, probably the side effect of the medicine."

    show rin basic_deadpandelight_pan_close with dissolvecharamove

    "She takes an unsteady step towards me, then another smaller one as she notices that it's not a good idea to try to take big steps."

    "I feel my muscles tense as I prepare to catch Rin if she falls down."

    play music music_twinkle fadein 3.0

    play sound sfx_flash
    scene ev rin_kiss at Zoom((800, 600), (200, 0, 400, 300), (20, 0, 760, 570), 0.4) with shortflash
    scene ev rin_kiss at Zoom((800, 600), (20, 0, 760, 570), (0, 0, 800, 600), 5.0)
    
    "She manages to take two more steps before she falls against me and to my surprise, not her downwards momentum nor our slight height difference are able to stop Rin from pressing her heart-shaped lips squarely against mine."

    "My brain locks out everything that happens right now."

    "As our lips part after a confusing moment of nothing but the taste of…Rin, I look down at her, trying to find some explanation to my bewilderment."

    $ renpy.music.set_volume(0.69999999999999996, 2.0, channel='music')

    scene bg school_dormrin 
    show rin basic_deadpandelight_pan_close
    with locationchange

    "The euphoric smile of a madman broadens on Rin's lips again but her eyes are dangerously vacant."

    show rin relaxed_sleepy_pan_close with charachange

    rin "See? You are wrong."

    rin "Maybe it's not impossible for artists to find romance."

    "I am absolutely stumped on what to respond."
     
    show rin relaxed_sleepy_pan at twoleft with dissolvecharamove

    "Rin takes a step backwards, separating her body from mine and making me realize that they were connected in the first place."

    show rin invis at Position(xanchor=0.5,yanchor=0.5,xpos=0.3, ypos=0.63) with dissolvecharamove
    play sound sfx_pillow

    "The second step is actually a fall backwards, luckily straight on her bed."

    "The soft thud Rin's thin body makes against the mattress breaks the silence."

    scene ev rin_high_open at Zoom((800, 600), (0, 0, 800, 600), (0, 0, 800, 600), 0.001, bilinear=True) with locationchange

    "I step to her quickly to see if she hurt herself, only to meet the peaceful face of dreaming."

    "Rin sleeps."

    "She is lying diagonally across the bed, somehow managing to simultaneously fall asleep while standing up and fall down so that she won't hurt herself."

    "Fool's luck."

    scene ev rin_high_sleep at Zoom((800, 600), (0, 0, 800, 600), (0, 0, 800, 600), 0.001, bilinear=True) with locationchange

    "What is there for me to do?"

    "…"

    "I tuck Rin in, covering her with the sheets as well as I can."

    "She feels very light, even though I am not that strong."

    show ev rin_high_sleep at Zoom((800, 600), (0, 0, 800, 600), (80, 0, 720, 540), 10.0, bilinear=True)

    "I stand up to look at her, the oval-shaped face, the dark eyelashes shut against the feverish cheeks, the slender body covered with the pale sheets."

    "Rin sleeps."

    "A conflict, no, more than one are churning inside me."

    "The most immediate one is the most important one."

    "Should I call a nurse? Or stay back and watch at her?"

    "I take one more look at her peaceful face."

    "Rin will be fine." 

    stop music fadeout 5.0

    scene bg school_girlsdormhall with locationchange

    "I close the door behind me."

    "It is indeed unlocked."
    window hide dissolve
    
    $ renpy.music.set_volume(1.0, 0.0, channel='music')
    scene black with Dissolve(1.5)

    return

label en_R17:    
    
    scene black with None
    $ renpy.pause(1.0)
    scene bg school_scienceroom
    with fade
    play music music_pearly
    window show dissolve
    
    "Somehow, it's hard to focus."

    "Yesterday's strange events keep running through my mind."

    "Or really, only the last one, right before I left."

    "It was nothing."

    "Rin was out of her mind because of the medicine overdose, and she was tired."

    "Nothing."
    
    scene bg school_scienceroom with shorttimeskip

    "The day passes in fast forward as my mind keeps running its own course instead of focusing on matters at hand."

    play sound sfx_normalbell
    
    "The ringing of bells makes me flinch and realize that I haven't been paying attention to the latter half of the afternoon class, not to mention taking notes."

    "Maybe I should pack my stuff too."

    "The act is mostly automatic, even though I know it'd be more useful to stop this futile pondering."

    "Mulling over this won't do any good."
    
    "Meanings, actions, connections… I can't make any sense of them."
    
    play ambient sfx_crowd_indoors

    scene bg school_hallway3 with locationchange
    
    "The corridor gets easily crowded because it's not that wide and people with wheelchairs need space to move."

    "It's half-empty now, though, which suits me fine…"
    
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    
    "Ah."

    "My feet stop moving on their own accord, and I am left standing right there."

    "She has stopped in her tracks in the middle of the hallway, just like me."
    
    show rin basic_absent with Dissolve(1.5)

    "Her pose is so relaxed, but I feel like I have eaten a crowbar."

    "Other people walk past us from both sides, but they don't matter."
   
    image bg blurring = anim.TransitionAnimation("bgs/school_hallway3.jpg", 0.0, Dissolve(10.0),
                                                 "bgs/school_hallway3_blurred.jpg")
    scene bg blurring 
    show rin basic_absent
    with None

    play music music_tragic
   
    "To them, we are just two schoolmates more standing in the hallway."

    "There is no connection."

    "Except that stare of hers, which I'm having a hard time to match."

    "The look on Rin's eyes keeps reminding me of how she looked after she did…kissed me."

    "She doesn't seem to have any trouble looking at me, but her dark eyes are making me feel flustered for no reason."

    "It's hard to look straight at her."

    "I don't know what one should say in these kinds of situations."

    "Then again, I rarely know what to say to Rin in any given situation."

    hi "So… are you feeling better today?"

    show rin basic_awayabsent with charachange
    
    "Rin looks away and starts walking again without saying anything, maybe because of my indecisiveness, maybe because of a whim, who knows."

    "She walks past me as if I was mere air."

    hide rin with Dissolve(1.5)
    
    "There is a pang in my heart."

    "How can she just ignore me like that?"
    
    "Usually it'd be just a matter of course, but…"

    show bg school_hallway3 at left with dissolvecharamoveslow
    
    "I turn around and close the distance between us and reach my hand to stop her, but something keeps my hand from gripping her shoulder."

    "I hesitate, lower my hand and keep walking half a step behind her down the staircase to the ground floor."
    
    stop ambient fadeout 1.0
    scene bg school_courtyard
    with locationchange

    "The summery afternoon hits us at full force, a change of atmosphere I barely notice."

    "Still, after the long day in class and despite the bothersome situation, I can't help appreciating the beautiful weather."

    show rin basic_awayabsent with charaenter
    
    "We walk unnoticed amongst the rest of the students going towards the dormitory buildings."

    "The cherry trees offer shadow, with the sunlight blinking through the holes in the canopies to create a chaotic pattern of darkness spotted with bright places where the beams are hitting the pavement."

    show rin relaxed_nonchalant with charachange
    
    "Rin's eyes are wandering, to everywhere but my direction."

    "I get the feeling that it's intentional."

    "It's not that she is in her own world, or looking at something interesting, for what interesting there could be here?"

    "Rin is actively trying to not look at me."

    "Could she be as confused about yesterday as I am?"
    
    scene bg school_dormext_full
    with locationchange
    
    $ renpy.pause(1)
    
    scene bg school_girlsdormhall
    with locationchange

    show rin basic_awayabsent with charaenter
    
    "Her steps lead us to the girls' dormitory and up the steps to the door."

    "I contemplate for only a split second if I dare to follow Rin."

    "It's not like I haven't been here yesterday and the day before."

    "As I already suspected, Rin walks to her own room."

    show rin basic_absent at tworight with dissolvecharamove
    
    play sound sfx_impact2

    "She kicks the door open without unlocking the door that is not locked, but instead of going in, Rin finally turns to face me."

    "This is probably as far as I can go."

    "She reckons me for a moment in mutual silence."

    "I have wanted to say something to her all this time, but now that I have the last chance, I find that I don't know what I'd want to say."

    show rin relaxed_doubt at tworight with charachange
    
    rin "Are you sad?"

    "Her voice is quieter than usual, but the tone is the same."

    hi "What?"

    rin "Are you angry?"

    hi "I…no…"

    show rin negative_spaciness at tworight with charachange
    
    rin "Are you upset?"

    hi "I am not… any of those."

    hi "I am confused, maybe."

    hi "You…I…"

    "Damn, the words are not coming, not to mention that I still don't know what I want to say to Rin."

    "It's pretty hard to put into words."

    "She looks hesitating as well, as if there is something she wants to say but she doesn't know how."

    stop music fadeout 4.2
    
    "I know how she feels."
    
    show rin basic_upset at tworight with charachange
    
    "Rin seems to get over her confusion first because she perks up and opens her mouth."

    play music music_rin 

    rinbabble " It looks like you are troubled and I don't really remember much about yesterday except that you came here and that's why it might be because of me so if it's because of me I think that I know why, it's because 
               people don't really like talking to me and you might be the same and that would be sad I know that people and I'm talking about others than Emi too always say that I'm strange and that I talk strange things so I 
               thought I'd try not to say strange things but that just makes me think more and new and strange and colourful that was not a good word but maybe you understand anyway and odd things so if I want to say something 
               I don't really know how and then the words are not the same as the thoughts because something goes wrong on the way out but it's not like the thoughts are really the thing I should be saying it's more like the 
               idea of the thought or the feeling of the idea or the idea of the feeling but it's not really any of those either because there is no word for it unless I invent a new one which is not really useful so 
               I've been thinking if doing things is better than saying so maybe because yesterday I took those pills and I was feeling a little strange I might have done something that I shouldn't besides 
               I don't even know if it would be any better if I just could say the thought there is no telepathy that's real telepathy isn't there I think it'd be terrible and useful at the same time but right now 
               I wouldn't mind because misunderstanding is so easy but understanding is not and I thought you'd understand even though it is hard but then I realized that I don't understand either which just made me more 
               confused and I wasn't sure—{nw}" with dissolve #reminder for the potential {nw} break
    
    stop music fadeout 3.5
    scene bg school_girlsdormhall 
    show rin basic_surprised at tworight 
    with vpunch
    
    "I grasp her shoulder and squeeze hard to make her stop. I don't have the capacity to take all that in at once."
    
    "It's like the great flood of '69 except there was no such thing."
    
    "Rin shuts up instantly."

    hi "Take a breath."

    hi "No need to get it all said at once. I'll listen, even if you talk slower."

    show rin relaxed_sleepy at tworight with Dissolve(1.5)
    
    "Rin is heaving , as if she didn't realize that she talked for quite long without sufficient air intake."

    "She blinks her eyes a few times and opens her mouth to say something more, but then shuts it before she begins again."

    "…"
    $ renpy.music.set_volume(0.2, 0.0, channel='music') 
    play music music_comfort
    $ renpy.music.set_volume(1.0, 8.0, channel='music')
    rin "It just came out."

    show rin basic_blush at tworight with charachange
    
    "She looks at me embarrasedly, with almost pleading look in her eyes."

    rin "It's weird, no?"

    "What can I say?"

    hi "Yeah. It's weird."

    hi "I too think that you are a weird person."

    hi "But what's wrong with that?"

    show rin negative_confused at tworight with charachange
    
    "Rin slumps her shoulders, looking defeated for some reason."

    rin "Sorry. I wasn't normal yesterday."

    hi "You never are."
    
    "My joke doesn't lighten the mood at all."

    rin "I guess I was confused yesterday and then I was confused today too, like a flu or being tired or other things that won't go away if you sleep."

    rin "I just thought it would be a bad thing if you got angry and stopped being my friend."

    show rin negative_worried at tworight with charachange
    
    "Rin raises her chin to look up at me again."

    rin "You are… my friend, right?"

    "Rin… thinks of me as a friend?"

    "I don't understand. She is always so nonchalant about almost everything."

    "I wouldn't have thought that she would think of me like that."

    "And what of me?"

    "What do I think about her?"

    "…"

    hi "Yeah. Of course I am."

    "I probably would have made a better impression without that thinking pause right now, but I don't think it matters in the end."

    "At least Rin doesn't seem to have noticed."

    show rin basic_deadpandelight at tworight with charachange
    
    rin "I think it's a good thing."

    rin "If you'd be my friend."

    "Again with that word."
    
    show rin basic_lucid_superclose with Dissolve(1.0)
    
    "I don't have a time to start pondering the meanings of words again, because Rin suddenly takes a short step closer."

    "…and just like that, she kisses me for the second time in as many days."

    "This time, the overrational part of my brain has time to note that this is not a thing that friends should do."

    "But I don't push her away, even though I forget that there is something I could be doing too."

    show rin basic_absent_close with dissolvecharamoveslow
    
    "Rin separates herself from me after what probably was not even a second and looks at me, oddly with that perfect poker face of hers, as if to observe my reaction which I'm afraid is more like lack of one, so stunned I am about this."
    
    rin "Are you doing something on the day after tomorrow?"

    "Still feeling like a concussion victim, I can only manage a shrug and an unintelligible grunt, which Rin luckily interprets correctly."

    rin "I can show it to you."

    show rin basic_deadpandelight_close with charachange
    
    rin "My secret place."

    hide rin with charaexit
    with Pause(1.0)
    play sound sfx_doorslam
       
    stop music fadeout 5.0
    
    "She quickly darts inside her room and slams the door shut."
    
    
    window hide dissolve
    scene black with Dissolve(1.5)

    return

label en_R18:

    scene black with None
    $ renpy.pause(1.0)
    
    scene bg school_dormhisao
    with openeye
    
    play music music_soothing fadein 1.0

    window show dissolve
    
    "The word “secret” is exciting."

    "It smells of mystery and intrigue and sounds like whispers in the dark."

    "It seems that just one word has seized me so badly that today's…date, if one can call it such, has been on my mind more than necessary."

    "It's not the only thing that has made me feel confused about Rin, but for now I will try to figure out what she really thinks of me… and what I of her."

    "What is Rin's secret place?"

    "I am not even quite sure of the time we were supposed to go, or how far it could be."

    "I thought that after doing morning chores and eating some breakfast, I'd just…go and pick up Rin from her dorm."
    
    scene bg school_dormext_full
    with fade

    "As I step outside the dormitory doors, the most immediate observation is that my plans are foiled."

    show rin basic_awayabsent with charaenter
    
    "She is standing there, at the small paved area that was occupied by the art club gallery at the festival, looking at the nearby cherry trees."

    "Rin looks like she is just casually hanging out, with her shoulders limping relaxedly and her eyes wandering around the surroundings, almost as if she just coincidentally happened to be around here, at this time."

    "Unless her presence really is a coincidence, a possibility that I'm not fully discounting yet."

    "But if Rin indeed has been waiting for me, how long has she stood there?"

    hi "Rin?"

    "She doesn't even notice me until I step right behind her and call her name, which is pretty strange from someone who is waiting for a friend."

    "Rin doesn't turn around to greet me back."
    #
    show rin basic_absent with charachange
    
    "Instead she just glances over her shoulder even though that just accentuates the fact that she is being impolite which in turn accentuates the contradiction of her waiting for me out here and then not showing any reaction after I show up."

    "How can so many conflicts fit into a single person?"

    rin "Come."

    "Rin sure doesn't waste words."
    
    scene bg school_backexit
    with locationchange

    "She leads me around the dormitory buildings and besides the garden to the northern wall, where she marches straight to the black-painted gate that leads to the wooded hills behind the school."
    
    scene bg school_forest1
    with locationchange

    play ambient sfx_park fadein 1.5
    
    "Path leads deeper into the forest."

    "The lush greenery surrounding us from every side is strangely calming."

    "As the twigs crackle beneath our feet, I realize that we have been silent for the whole time. Again."

    "This is bad, I'm beginning to get used to these awkward silences."

    hi "So you have a secret place, huh."

    show rin basic_absent with charaenter
    
    rin "Doesn't everyone have one?"

    hi "No, that doesn't sound like common knowledge to me."
    
    show rin basic_surprised with charachange

    rin "Oh, I thought that everyone has those, a bit like imaginary friends and code languages."

    "Her unjoke makes me chuckle."

    show rin basic_awayabsent with charachange
    
    "Seriously though, at least I can't think of any place I'd consider my own secret, and I can't recall ever having an imaginary friend nor a language only I can understand."

    "Maybe I had a boring childhood."
    
    "Rin turns away from the main path and walks between two large trees, disappearing behind them."
    
    scene bg school_forest2
    with locationchange

    "There is another path, although narrower, leading up the steep hill while the main path continues to another direction."

    "The path snakes around the trees and undergrowth, with Rin following it and me following her."

    "Walking uphill is becoming harder as the hill becomes steeper, and I begin to feel my legs hurting."

    "I have to stop a few times to catch my breath, then run after Rin who doesn't stop to wait for me."

    "Soon I am out of breath again."

    "She is in pretty good shape, better than me at least, but it's probably because she uses her legs so much every day."

    "Suddenly the trees end."
    
    stop music fadeout 6.0

    show bg school_hilltop_border with locationchange
    
    "The edge of the forest is sharp like a line was drawn in the ground to mark it."

    "The hill continues to climb up, but from here to the top it's meadow, tall grass and small bushes."

    "Rin continues to climb along the narrow path without caring about the change in surroundings."
    
    scene bg school_hilltop_spring at left
    with locationchange
    
    play music music_twinkle fadein 1.0

    "The grass sways in the breeze, creating an entirely different kind of atmosphere than the forest."
    
    rin "This."

    scene bg school_hilltop_spring at Fullpan(25.0)
    
    "I look around. We are at the highest point of the hill, with the forest behind us and the view to every direction opening in front of our eyes."

    "The city lies below us, lazily reveling in the quiet mood of the Sunday afternoon."

    "You can see pretty far from here, and the vista is beautiful, but there is nothing special that I can see."

    hi "You secret place is the hilltop?"

    show bg school_hilltop_spring at right 
    show rin basic_absent at center 
    with charaenter
    
    rin "My secret place is the hilltop."

    "I could hardly think any less secret places around here, save for maybe the downtown."

    "The high hilltops can easily be seen from everywhere in the area."

    "Maybe she's right in a way though, people probably don't come here often. It was quite a workout to climb all the way up."

    "If nobody else comes here, does that make the hilltop, in a way, a secret place?"

    "I guess I read too deep into the word choice, and got my expectations a bit too high."

    "At any rate, here we are. I can hear my thighs sigh in relief."

    "Rin doesn't seem to be too tired even though she too is breathing heavier than normal and her cheeks are healthily blushed."

    "I am out of breath and out of strength, and I have to bend over myself to ease the pain in my abdomen but she stands as tall as she can, peering to the distant horizon."

    "The sunlight forces Rin to squint as she doesn't have hands to cover her eyes with but she doesn't turn her gaze away."

    show rin basic_deadpandelight with charachange
    
    rin "It's like in the pictures."

    "The irony gives me a wheezing laughing fit that dies instantly as my diaphragm starts to cramp again."

    "We trudged to the top somehow, panting and sweating… to see the view just like it is in the pictures."

    "It's not just us; everyone who visits anything worth visiting has the same dilemma."
    #
    "They bother themselves a lot to see places they could see from pictures or even worse, they take photos so that they can see what they saw after they return home."

    "I feel my pulse go down and my breathing becomes more even, allowing me to breathe in deeply and stretch to my full height."

    "The wind picks up, swaying the canopies below us and ruffling my hair. It makes the grass sway in waves as the breeze sweeps across the hilltop."

    "Sun shines from the open skies on us, what just moments before was painful heat is now gentle warmth."

    "I'm pretty sure that all that bother was worth it."

    "Rin did not lie; this place must be as close to heaven as it's possible around here."

    "As I take another deep breath, a familiar scent that I can't name right now makes me look around in search of the source."

    "It's flowers."

    "The entire hilltop is covered with yellow flowers."

    show ev dandelion at Zoom((800, 600), (0, 75 , 800, 600), (45, 105, 720, 540), 25.0, bilinear=True) with locationchange
    
    "Dandelions."

    "It's like the places where there is no tall grass had been painted brilliant yellow."

    "Rin notices me marveling the yellow sea and sits down on the grass, making me follow the suit to rest my aching feet."

    rin "They grow here every year, and when the summer is over they fly away."

    hide ev
    show rin negative_spaciness
    with charachange
    
    "Her voice is melancholic and surprisingly emotional, a strange contrast to her usual monotony."

    hi "Does it make you feel sad for them?"

    "She looks around the flowers surrounding her as if to find out what she thinks about them."

    show rin negative_confused with charachange
    
    rin "No."
    
    rin "That is what they must do, otherwise they wouldn't be proper flowers."

    "Her words give me a pause, reminding me of her talk at the track meet."

    hi "Then, does it make you feel sad for yourself?"

    "She doesn't answer, but with Rin it's not possible to say if I hit a nerve or if she ignored the question out of a whim."

    "It makes me remember Nomiya's proposal."

    hi "Why don't you want to take up on the change to get your paintings to a gallery?"

    hi "The teacher told me that he tried to set up something with some friend of his, and that you didn't think it was a good idea."

    show rin negative_spaciness with charachange
    
    rin "I don't think it is a good idea."

    "Rin voice is bored and irritated at the same time. This really seems to be a bad topic."

    hi "But you want to be a proper artist, right?"

    show rin basic_absent with charachange
    
    rin "Maybe. Probably."
    
    hi "You can't really do that if nobody knows of you, or buys your works."
    
    "I look around me to come up with something else to say."

    hi "Wouldn't it be sad if these flowers would not fly away?"

    show rin basic_awayabsent with charachange
    
    "She just shrugs her shoulders dismissively."

    rin "I want people to see the paintings, but I want them to look only at the paintings."

    show rin negative_confused with charachange
    
    rin "If I could be invisible there would be no problem."

    show rin negative_spaciness with charachange
    
    rin "Do you know how to be invisible?"

    hi "Wait, what? Let's backtrack a bit. I didn't think you were a shy person."

    "Rin looks very sour at this discussion, but I promised the teacher that I'd try to talk to her."

    "I can't really back up."

    show rin negative_sad with charachange
    
    rin "I have told it to you before."

    rin "If someone looks at my paintings, he doesn't look at my paintings. He looks at me."

    show rin negative_spaciness with charachange
    
    rin "I think that is not good."

    show rin negative_worried with charachange
    
    rin "Don't you understand?"

    hi "I do understand, but… how bad can it really be? You can't seriously expect that people would be gawking at you like a talking dog or something."

    "Then again, it's not like I can expect people to ignore Rin's… special circumstances either."

    "It's not like I did, or do."

    hi "Yeah, I get that you place a lot more worth on the art itself than the fact that you painted it, but isn't it equally bad thing to not even try to see what happens?"

    hi "You know, when I told you that I decided to live my life a little better, you said that you thought it was a good thing."

    hi "I don't understand why you refuse so adamantly to seize chances in your own life."

    hi "It would be a waste, and it makes no sense."

    "Rin takes my speech without blinking an eye, her mouth tightly shut."

    "I wonder if I made her angry."

    "As she doesn't say anything even after I finish, I feel compelled to add a final note."
    
    hi "You should do it."

    show rin invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.58) with dissolvecharamove
    
    "Rin flops lying down on the grass and flowers, turning her eyes up to the distant blue above us."

    "I take it as a sign that the discussion is over now."

    "It bothers me."

    "She bothers me."

    "Whenever I think that I might have some idea what Rin is thinking, I find out that I have no idea at all about what she is thinking."

    "She is so odd. That's why we can never understand each other."

    "I'm feeling a little bad about making her upset so, and only because I was asked to."

    "But I spoke my own words, not Nomiya's so I can't really blame him either, and it was me who agreed to do it in the first place."

    "With nothing else to do, I lean back against the uncomfortable ground and try to relax as well."
    
    scene bg misc_sky at Fullpan(40.0)
    with fade

    "The clouds are not bad."

    "Neither are the lazy gusts of wind or the sunlight warming my cheeks."

    "Maybe this isn't such a bad way to spend a Sunday, despite the awful climb and the unpleasant discussion just now."

    "She probably forgets it sooner or later."

    #sky background slideshow or something like that here, or another way to pass a bit of time like "…"

    rin "I have made a decision."
    
    scene bg school_hilltop_spring 
    with Dissolve(1.5)

    "I raise my head to see Rin even though that's not necessary to hear her voice."
    
    "She's been mulling the discussion all this time? Or is this about something unrelated again?"

    show rin basic_absent at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.63) with charaenter
    
    rin "I will try it."

    hi "Getting your paintings to a gallery?"

    show rin basic_awayabsent with dissolvecharamove
    
    "Rin nods and stands up, turning her back to me to look at the mountains in the horizon."

    rin "I will try it."

    "I don't know what to say. I am surprised, astonished even."

    "Rin seems always so… unaffected by anything and everything that I never would have guessed that my words could make her think and decide something."

    "She is like her eyes are, absorbing everything without showing the change to the outside."

    stop music fadeout 5.0
    
    "Then again, she is whimsical too, like a reed in the wind."

    "Maybe all she needed was a catalyst?"

    "…"
    
    scene bg school_forest1
    with locationskip

    #some fade effect here
    
    play music music_dreamy fadein 1.0

    "We walk down the slope carefully and slowly to avoid falling down, Rin in lead and me a few steps behind."

    "For some reason I am happy that Rin decided to overcome her contempt."

    "She should show her paintings to people."

    "That's what she wants; to be a real, professional artist."

    "But I am not sure if she understands that wishes don't come true just like that, without even trying."

    "If a person has a goal in life, that goal can be one of two things."

    "It's either real or it's a dream."

    "Rin surely could realize her goal, if she tried hard."

    "As for me, I have to find my goal first."

    "…"

    "I keep watching the back of the red-headed girl descending down the path a few steps ahead of me."

    
    stop music fadeout 5.0
    "If it's only this much... this distance between us is definitely within my reach."
    
    stop ambient fadeout 2.0
    window hide dissolve
    scene black 
    with Dissolve(3.0)

    #The end of Rin Act II, "Dream".
    return
