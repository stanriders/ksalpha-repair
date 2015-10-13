
label en_L20:
    
    scene bg school_scienceroom
    with locationchange
    
    play music music_another fadein 1.0

    "As another of Mutou's droning lectures comes to a close, the class sighs in relief."

    "Lunchtime."

    "A symbol of freedom and liberty for every highschool student across the nation."

    "I grab my bag from the side of the desk and swing it up to shove the lesson's sheets inside."

    "As I look at the top sheet before putting it in, the forboding text at the top beckons."

    $ written_note("EXAM REVISION SHEET 3:\nTHE LAWS OF THERMODYNAMICS")

    "In contrast to Mutou's scruffy and barely-legible handwriting, it's clearly printed from a word processor."

    "That alone's enough to see it's mandatory revision work, as opposed to his usual teaching material."

    "The sheet's text also lacks his penchant for extremely spartan sentence structures."

    "He's a scientist, alright."

    "But then again, I have to wonder why the hell he's a teacher and not a researcher."

    "It's pretty obvious he's not exactly the best for the job."

    "Well, such are the mysteries of life I suppose."

    "As I slot in one sheet after another, I pause as I suddenly hear my name from the other side of the room."
    
    show bg school_scienceroom at bgleft
    with charamove

    "Looking over to the door, I see two girls talking, with one pointing directly at me."

    "The one pointing's a girl from our class—a tomboyish and athletic black-haired girl called Miki who accidentally lost her hand thanks to her father's powertools."

    "I shudder slightly."

    "That's one conversation I wish I hadn't overheard."

    "The other, though, I've never seen before."

    "She looks small with dark brown twin braided hair, and seems quite pretty."

    "From the fact that she doesn't look to have anything wrong with her, and was talking to Miki, she must either be an interpreter or blind."

    "I leave my bag on the desk and walk over to the two at the door."
    
    show miki basic_smile at twoleft
    show aoi oops at tworight
    with charaenter

    mk "Ah, here he is."

    hi "You want me?"

    "Girl" "Are you… uh…"
    
    show miki basic_grin at twoleft
    with charachange

    mk "Hisao. The guy you want's called Hisao."

    hi "Yeah, that's me."
    
    show aoi smile at tworight
    with charachange

    "Girl" "Um, would you be able to give this to Li— I mean, Satou, for class 3-3?"

    "She holds up a small stuffed teddy bear."

    "Judging by the fact that her face hardly moves at all as I take it, I guess she must be blind."

    "I hold it in my hands and quickly examine it."

    "Soft and fluffy, the stiff joints make it seem closer to a collector's item than a plaything."

    "Though, considering what Lilly's personality is like, it seems like the perfect present."
    
    show miki basic_serious at twoleft
    with charachange

    mk "Dammit, looks like I owe you five then."

    "I look up from the bear to her."
    
    show aoi oops at tworight
    with charachange

    "Girl" "You never saw it?"

    "Yep, she's blind. Even as she talks to Miki, her head doesn't move."

    "Seeing her act like this reminds me of just how much practice Lilly must put into making her mannerisms appear normal."
    
    show miki cross_oops at twoleft
    with charachange

    mk "Hey, don't blame me for not being a social butterfly. The track club's not a social party, you know."

    hi "Um, what's going on?"
    
    show miki cross_concerned at twoleft
    show aoi neutral at tworight
    with charachange

    mk "Huh?"

    "She suddenly looks over, seemingly forgetting the fact that I could hear her."

    mk "Oh yeah, me and Aoi had a little bet."
    
    show miki basic_serious at twoleft
    with charachange

    "She looks sharply at the other girl, putting her only hand on her hip."

    mk "Which I lost."
    
    show aoi oops at tworight
    with charachange

    "Aoi's face becomes pained."

    "Aoi" "I never said you had to pay up right now."

    hi "I'm still lost here."
    
    show aoi smile at tworight
    with charachange

    "Aoi" "Ah ha… We kind of made a bet about whether you and Lilly were dating."

    hi "You've got to be kidding me."
    
    show miki basic_wink at twoleft
    with charachange

    mk "Quite the Casanova, aren't ya?"

    hi "Hey, don't get the wrong idea here. I'm not going out with her."
    
    show miki basic_surprised at twoleft
    show aoi surprised at tworight
    with charachange

    "Aoi" "Whaaaat?"
    
    show miki basic_whistle at twoleft
    with charachange

    mk "Ha ha! Looks like I'm rich!"
    
    show aoi oops at tworight
    with charachange

    "She proudly puffs out her chest as the other pouts. It doesn't take a genius to see who bet either way."

    hi "Fine, I'll take the card to her."
    
    show aoi neutral at tworight
    with charachange

    "Aoi" "Um, thanks… Hisao."
    
    hide miki
    hide aoi
    with charaexit
    
    stop music fadeout 3.0

    "With that, the two leave the room. Even from inside I can hear the laughter and protesting between them."

    "As I grab my bag and carefully slip the card inside, an unwelcome voice rings out from behind me."
    
    play music music_comedy fadein 0.1

    mi "Hicchan~"

    hi "Uh-oh. Uh, I mean, hey Misha, Shizune."
        
    show bg school_scienceroom at bgright
    with charamove
    
    show shizu adjust_happy at tworight
    show misha hips_smile at twoleft
    with charaenter

    "As I turn around to meet them, I give a small wave to Shizune with my free hand."

    mi "We heard what happened, Hicchan."

    hi "I'd be surprised if the student council hadn't, practically the entire school has by now."
    
    show misha sign_smile at twoleft
    with charachange

    "She looks up in thought, bringing her finger to her chin to exaggerate the point."

    mi "You do have a point…"
    
    show shizu behind_blank at tworight
    with charachange

    "Shizune reaches forward and taps her on the shoulder twice to grab her attention."
    
    show misha perky_confused at twoleft
    with charachange

    mi "What is it, Shicchan?"
    
    show shizu basic_normal at tworight
    with charachange
    
    show misha sign_smile at twoleft
    with charachange

    "Shizune starts to sign, but once she's finished Misha starts to sign back. Interpretation isn't meant to work this way, I'm sure of it."
    
    show shizu behind_blank at tworight
    with charachange

    "The two seem to have a comfortable chat as I stand patiently waiting. Though, that's only a guess at what they're saying."

    "For all I know, they could be planning the radical feminist movement's next—" #reminder for the potential {nw} break

    "NO! NO! NOT THAT! DAMMIT, KENJI! GET OUT OF MY MIND!"
    
    show misha sign_confused at twoleft
    with charachange

    "As I rough my hair in frustration, Misha pauses and looks over."

    "I guess she misinterpreted it as frustration at her."
    
    show misha perky_confused at twoleft
    with charachange

    mi "Shicchan says,"
    
    "She brings her hand to her mouth and clears her throat in the most formal manner she can summon."
    
    show misha hips_smile at twoleft
    with charachange

    mi "The student council wishes to extend their best wishes for Lilly Satou's quick recovery, and are prepared to help you as far as our duties allow."

    show misha perky_smile at twoleft
    with charachange
    
    "Once she's finished, she looks sideways to Shizune."
    
    show shizu adjust_happy at tworight
    with charachange

    "An affirmative nod. I guess their talk was a negotiation about the wording of their, for lack of a better term, press release."

    hi "Thanks you two. It's good to know I can depend on you."
    
    show misha cross_grin at twoleft
    show shizu behind_smile at tworight
    with charachange

    mi "How could we call ourselves the student council if we couldn't support the students, Hicchan?"

    hi "Yeah, you've got a point. Still, thanks. Both of you."
    
    show misha cross_smile at twoleft
    with charachange

    mi "No problem. Shicchan and I had better be off, though."

    mi "See you later, Hicchan!"

    hi "Seeya."
    
    stop music fadeout 5.0
    
    hide shizu
    hide misha
    with charaexit

    "With that, they move to Shizune's desk to fish out some books."

    "What to do, what to do…"

    "I'm not exactly overly hungry, and a quick glance at Hanako's desk is all that's needed to see that she's left."

    "Well, the library's as good as anywhere, I suppose."

    "I exit the classroom along with the last of the students and enter the hall."

    scene bg school_hallway3
    with locationchange

    "Walking along, I glance out the window."
    
    play sound sfx_whiteout
    
    scene bg misc_sky at Fullpan(25.0)
    with locationchange

    "A blue sky, punctuated by the occasional cloud. The temperature's quite nice, too."
    
    "…"
    
    play music music_running fadein 0.1

    "Boy" "OUT OF THE WAY! OUT OF THE WAY!"

    hi "Huh?"
    
    scene bg school_hallway3
    with locationchange

    "As I look back, the scene plays out as if it were a sequence of still frames."

    "A boy in a wheelchair is moving, nay, careering, along the hall."

    "I see that, unfortunately, I seem to be the only one who hasn't moved out of his way."

    "His face changes from one of determination to one of panic."

    "He opens his mouth to yell, but it's too late."
    
    play sound sfx_impact2
    with vpunch

    scene black
    with Dissolve(0.2)

    "He slams into me at full speed, sending me flying sideways and his wheelchair swinging around to a sliding halt."

    hi "Shit. Shit. Shit."
    
    scene bg school_hallway3
    with openeye

    "I open my eyes as I prop myself up with my arms."

    "Boy" "I'm sorry, I'm sorry!"

    "Girl" "Are you alright?"
    
    "I look up and back to the classroom I'd exited not long ago."
    
    show misha invis at offscreenleft
    with None
    
    show bg school_hallway3 at bgright
    show misha perky_confused at left
    with dissolvecharamove

    "Misha stands there, a worried look on her face."

    "I move my hand up and wave away her concern with a grin."

    hi "I'm fine, no harm done."
    
    show shizu invis at offscreenleft
    with None

    "As I say it, I notice a movement out of the corner of my eye."
    
    show bg school_hallway3 at center
    show misha perky_confused behind shizu at leftoff
    show shizu basic_angry at twoleft
    with dissolvecharamove

    "Following it, I see Shizune striding up to the wheeled bandit."

    "All I can do is grimace in anticipation of what's to come."

    "He looks from me to her, and instantly looks stricken with fear."

    "Looks like she has a reputation."
    
    show shizu cross_angry at center
    with dissolvecharamove

    "She steps up to him confidently and crosses her arms."

    "Seconds pass."

    "Boy" "Uh… Um… I—I… didn't mean to…"
    
    show shizu behind_frown at centeroff
    with dissolvecharamovefast

    "Without warning, she steps behind his wheelchair and latches onto the handles with an iron grip."
    
    hide shizu
    with charaexit

    "And just like that, she starts to wheel him away."

    "Boy" "H—Hey! What're you doing!? Hey, hold on!"

    "All I can do is look on with a bemused expression."
    
    show bg school_hallway3 at bgright
    show misha perky_confused at twoleft
    with charamove

    hi "He's screwed, isn't he?"
    
    show misha hips_grin at twoleft
    with charachange

    "Misha grins wildly. Don't tell me she secretly enjoys Shizune doing this…"

    hi "Go easy on him, will ya?"
    
    show misha cross_smile at twoleft
    with charachange

    mi "Hmm, I'm not sure I can do that, Hicchan. Once Shicchan sets her mind on something, she's very stubborn."

    "While I don't doubt her claim one bit, I can't help but notice a distinct lack of regret about it."

    mi "Need a hand?"

    "I suddenly realise I'm still on the floor, propping myself up with an arm."

    hi "Yeah, thanks."
    
    show bg school_hallway3 at center
    show misha perky_smile_close at left
    with dissolvecharamove

    "She reaches out a hand, which I clasp in mine and lever myself up with."

    "She has a surprisingly strong grip, given her looks."

    hi "Thanks."

    mi "No problem~"
    
    stop music fadeout 3.0
    
    hide misha
    with charaexit

    "And with that, she merrily walks off down the hall after Shizune."

    "Still more than a bit dazed, I begin my journey to the library anew."

    scene bg school_library at bgright
    with locationchange
    
    play music music_daily fadein 4.0

    "Inside the library, it's the regular hub of busy activity."

    "Students are furiously sleeping on desks, the wind ripping through unattended books. The noisy hum of students snoring is near constant."

    "A regular academic success story."
    
    "Glancing through the shelves though, I see Hanako at one of the small, square tables."

    "Considering it's placement at the very back corner of the library, I'm surprised I even managed to catch sight of her."
    
    show bg school_library at bgleft
    with charamove

    "As I casually stroll up, I see her reading a book placed flat on the surface, her left hand both hiding her face and holding her hair back."
    
    show hanako emb_downtimid at centersit
    with charaenter

    hi "Hey."
    
    show hanako defarms_shock at centersit
    with vpunch
    
    with Pause(0.2)
    
    show hanako def_worry at centersit
    with charachange

    "She looks up with a look of fright on her face, the tension evaporating as she catches sight of me."

    ha "Ah, Hisao."

    hi "Hey, don't sound too enthusiastic now."
    
    show hanako emb_timid at centersit
    with charachange

    ha "Ah, sorry. I was just… reading, and I…"
    
    show hanako emb_downtimid at centersit
    with charachange

    "As she looks away in shame, I fall into a seat opposite her."

    hi "Don't worry about it. What's the book?"
    
    show hanako emb_timid at centersit
    with charachange

    ha "Hmm? Oh, It's… uh… Dune."

    hi "Dune, huh?"

    "Of all the genres I'd think her to read, sci-fi's pretty low down the list."
    
    "I rock on the back legs of the chair as I stare at the ceiling."
    
    scene bg misc_ceiling
    with locationchange

    "The shadows on the stucco ceiling are surprisingly interesting to examine."

    "Time passes as I look closely at the roof above out of sheer boredom."

    "As I do, though, I find myself listening for the sound of Hanako's book."

    "Or rather, the lack thereof."

    "Not a single page has been turned since I started listening."

    "I stop swinging for a second and look downwards."
    
    scene bg school_library at bgleft
    show hanako emb_downtimid at centersit
    with locationchange

    hi "Hanako."
    
    show hanako emb_timid at centersit
    with charachange

    ha "Mm?"

    "She keeps her face pinned to the page, only shifting her eyes upwards. It doesn't take much effort to see what she's feeling."

    "She's been attached to me like a third arm these past few days."

    #"And now, the first time she's decided to be alone, I barge in."

    return

label en_L20a:

    # Choice [1]

    hi "I don't want to have to deal with you too."

    ha "…?"

    hi "Don't try to hide it, you're worried about Lilly."

    ha "Ah, er… uh…"

    "Her voice comes out as fractured squeaks."

    hi "You'd have seen it too. How she was different."

    "She closes the book and meekly nods."

    "I let the chair fall forward with a thud and sit myself upright."

    hi "I'm worried about her too, Hanako."

    ha "Hi… sao?"

    hi "I'm really, really worried for her."

    hi "But… I also trust her."

    hi "She worries about others so much, she need to think about herself more often."

    hi "When we visited her on Saturday, I talked to her after you went to get the drinks. Even then, she was worrying about you."

    hi "If we keep worrying about her, she'll never stop fussing."

    hi "I want to help her. I'm sure I want to help her. But to help her, I need to trust in her as well."

    hi "So let's trust her together, okay?"

    "I put my hand on her head, causing it to bob down slightly."

    ha "…Mmm."

    scene black
    with dissolve

    return

label en_L20b:

    # Choice [1]
    # Hanako True End assured

    hi "Hey, Hanako?"
    
    show hanako basic_worry at centersit
    with charachange

    "She looks up, a pensive look on her face."

    "“I'll take good care of her.”"

    "I look into those shy eyes of hers."

    "…"

    "I know what I have to do."

    hi "Want to go outside for a bit?"
    
    show hanako cover_worry at centersit
    with charachange

    ha "Outside?"

    hi "Yeah. Some fresh air wouldn't hurt, would it?"
    
    show hanako def_worry at centersit
    with charachange

    "I give a mischievous grin and stand from the chair."
    
    show hanako defarms_shock_close at centersit2
    with charachange

    "Before she can say a word, I take her hand, her face suddenly becoming a mixture of surprise and embarrassment."

    ha "H… Hisao?"
    
    "I give a deep bow as I look to her, drawing the gazes of a few passing students."

    hi "Shall we take our leave?"

    # The rest of this could well be summarised in the beginning of HT1 as part of a flashback
    # Enjoy your Hanako path

    return

label en_L21:

    # Act 4 title card: "Past and Present"

    scene black

    # BG change to black
    # Maybe SFX

    centered "*THUMP*"

    scene bg school_scienceroom
    with openeye
    with vpunch

    "I open my eyes with a start."

    "First observation: My face is sideways on a classroom table."

    "Second observation: There is a balled fist centimeters from my face."

    "I right my head and follow the arm upwards."
    
    $ renpy.music.set_volume(0.20000000001, 1.0, channel='ambient')

    play music music_tranquil fadein 2.0
    
    show muto normal at center
    with charaenter
    
    "Sure enough, the tall, lanky figure of Mutou is the owner of it."

    mu "Have a good sleep, Nakai?"

    hi "Not really."
    
    show muto smile at center
    with charachange

    "He gives a chuckle as awkward as his smile."

    "This guy really has no idea how to properly act around others. Every facial movement seems like an act of careful but misdirected choreography."

    "As I quickly glance around him, I see the room's entirely empty."

    hi "What time is it?"

    show muto irritated at center
    with charachange
    
    "He glances to his watch."

    mu "About ten minutes since the afterschool bell rang."

    hi "You've got to be joking."
    
    show muto normal at center
    with charachange

    mu "You looked like you were sleeping so peacefully, I didn't want to wake you."

    hi "I can't even remember when I went to sleep."

    mu "It was around…"

    mu "When was it…"
    
    show muto irritated at center
    with charachange

    mu "Ah, that's right. It was when I was telling the class about the demonstration I'd be doing tomorrow."

    hi "Demonstration?"

    mu "Blowing up a balloon filled with hydrogen."

    show muto smile at center
    with charachange
    
    "He grins madly. Don't tell me he's a pyromaniac."

    "Well, I suppose I'd better go along with it."

    hi "Sounds good."

    mu "Can't beat an experiment that involves a good explosion."

    show muto normal at center
    with charachange
    
    mu "Ah, those were the days."

    show muto smile at center
    with charachange
    
    mu "You know, I made myself a damned good crater in my backyard once."

    mu "Just bought a few firecrackers, made myself a dash of gunpowder to add to the mix."

    "His wistful smile suddenly jerks back into the world of reality."

    show muto irritated at center
    with charachange
    
    mu "But don't do that, okay?"

    "He brings his hand to his mouth and forces himself to cough."

    mu "I could've blown my hand off doing that, so don't do it. Ever. Understand?"

    hi "Don't worry, I'm not suicidal."
    
    show muto normal at center
    with charachange
    
    mu "Good to hear."

    "Seemingly not noticing the not-so-subtle implication, he begins to walk back to his desk."

    hide muto
    
    "I wonder…"

    hi "Hey, Mutou?"

    show muto smile at center
    with charaenter
    
    mu "Yes?"

    hi "Don't suppose you know anything about… er…"

    "And now I start to have second thoughts."

    "Think this stuff through before saying half the sentence, genius."

    hi "Existentialism?"

    "He cocks an eyebrow and leans on a table next to him."
    
    show muto normal at center
    with charachange

    mu "Good ol' existentialism, eh?"

    mu "I guess it's not rare for guys your age to think about that kind of stuff."

    mu "Well, actually…"

    mu "I guess it kind of is."

    show muto smile at center
    with charachange
    
    mu "But don't worry, you're in good company."

    "On the plus side, he doesn't think of me as a pretentious idiot for it."

    "But on the other, he thinks me weird."

    "And to hear this from, of all people, Mutou."

    hi "Thanks."

    "Really."

    "He looks up for a brief moment, lost in thought."

    show muto normal at center
    with charachange
    
    mu "I think I still have a few books about that stuff kicking around somewhere…"

    hi "You're into philosophy?"

    mu "The philosophy of what makes a beautiful explosion, yes. Otherwise, no."

    hi "Yet you have books on it?"

    mu "I went through a phase. I think everyone does."

    mu "Why we're here, what we're going to do, how we should live."

    mu "Everyone handles it differently."

    show muto smile at center
    with charachange
    
    mu "For me, and evidently you, we looked into ourselves."

    hi "I… see."

    "He picks the weirdest times to make perfect sense."

    hi "Did you find what you were looking for in those books?"

    mu "God no."

    show muto normal at center
    with charachange
    
    mu "Some old pretentious Greeks babbling on about God knows what."

    show muto normal at center
    with charachange
    
    mu "And don't get me started on those German guys."

    hi "You didn't like them?"

    mu "I was young and dumb. Once I put down the books and thought a bit, I found the answer myself."

    hi "Explosions, right?"

    mu "Full marks."

    hi "Um, thanks."

    mu "Not a problem."

    show muto irritated at center
    with charachange
    
    mu "Sorry to bring school back into this, but finals are coming up."

    hi "Yeah, I've been studying."

    mu "Know where you'd like to go with yourself?"

    hi "Not really. I guess I'd like to go to uni, but that's about it."

    show muto normal at center
    with charachange
    
    mu "Make sure to think about it. This is a pretty important time in your life."

    mu "If you put your head to it, you could do just about anything you want, especially in science."

    hide muto
    
    "With that, he walks back to his desk to collect the books and folders piled on top."

    "All but exhausted of conversation, I grab my bag and head out of the classroom."

    scene bg school_hallway3
    with locationchange

    "As I head out into the hall, I grab the mobile phone from my pocket and turn it on."

    "I scroll through my pitifully small contacts list, slowly taking note of each name."

    "Lilly, Kenji, Misha, Shizune…"

    "Here we go, Yuuko."

    # Timeskip

    scene bg hosp_hallway
    with shorttimeskip

    "It doesn't take long before we reach the hospital, thanks to the scooter."

    "It may not be the healthiest or speediest thing around, but it goes from point A to point B well enough."

    "…When it decides to start in the first place, that is."

    "As we enter the final hallway to Lilly's room, Yuuko behind me as we walk, she claps her hands together."

    "I guess that mannerism's inherited."
    
    show yuuko neutral
    with charaenter

    yu "Good news, Hisao!"

    hi "Yeah?"

    yu "Looks like Lilly's going to be discharged tomorrow! Her throat's been healing up really well."

    hi "Damn, that's the best news I've heard all day."

    yu "It seems she took well to the news as well."

    "As I turn to look back down the hallway, I raise an eyebrow."
    
    show akira basic_boo at left
    with charaenter
    
    show yuuko neurotic
    with charachange
    
    "A darkly-clad figure steps out from the door ahead, striding out and walking down the hallway towards us."

    "Pausing a moment to try and work out why he's been in Lilly's room, I take measure of him."

    "Dressed in an obviously very expensive designer suit, it fits his tall and very slender figure perfectly."

    # Show sprite
    # For now, I'll use the character code "aki", easily changed if need be
    # New character GET

    show akira basic_smile at center
    with charamove

    "He suddenly stops directly in front of us, seemingly ignoring Yuuko entirely as he looks at me."
    
    show akira basic_kill at center
    with charachange

    "He stares intensely into my eyes, his hand to his chin as if he were examining piece of fine art."

    "…"

    "He stands there immobile for seconds on end, his eyes staring into mine."

    hi "Uh…"

    aki_ "Interesting. Just the type I thought she'd go for."

    show akira basic_smile at center
    with charachange
    
    hi "Wh… what?"

    "His utterly fake Kansai accent takes me off guard almost as much as what he says."

    hide akira
    with charaexit

    "Before I can dwell any further, though, he turns sharply and takes the stairs downwards without so much as a look back."

    "I stand and watch the mysterious suited figure helplessly as he rounds the staircase and promptly disappears from sight."

    hi "What in the hell?"

    show yuuko worried
    with charachange
    
    yu "Hisao, go see Lilly. I'll deal with this."

    hi "Huh?"

    yu "Go on, she'll be waiting for you."

    hi "Fine, but tell me what the hell's going on when I get back, okay?"
    
    hide yuuko
    with charaexit
    
    "I stride up to the door briskly, trying to walk off the annoyance."

    "He really seemed to have a confident air about him."

    "Actually, confident is the wrong word. “Obnoxiously smug” would be a better description."

    scene bg hosp_room
    with locationskip
    $ renpy.music.set_volume(0.10000000001, 1.0, channel='music')
    
    play music music_credits fadein 2.0
    
    "As I open the door to Lilly's room, I see the same sight as before; the room all but devoid of life except for her."
    
    show lilly basic_listen_pat at center
    with charaenter

    "She turns her head to the side to try and hear as best she can."

    hi "Yo, Lilly."

    show lilly basic_smile_pat at center
    with charaenter
    
    li "Ah, Hisao. Good…"

    show lilly basic_weaksmile_pat at center
    with charachange
    
    "She trails off, seemingly unable to work out what time of the day it is."

    hi "Afternoon."

    show lilly basic_smile_pat at center
    with charachange
    
    li "Thanks. It's somewhat difficult to work out what the exact time is here."

    "I take a seat next to her bed, taking note that the cushion on it feels distinctly warm."

    hi "At least you won't be in here too much longer."
    
    show lilly basic_cheerful_pat at center
    with charachange 

    li "Ah, Yuuko told you about when I'd be discharged?"

    hi "Yeah, tomorrow. Looking forward to it?"

    show lilly basic_smile_pat at center
    with charachange
    
    li "I shan't feel any regret to be leaving such a place behind, to be honest."

    hi "Hanako's been doing well."

    show lilly basic_giggle_pat at center
    with charachange
    
    li "And you?"

    hi "Yeah, pretty well. Is there treatment you'll have to keep doing after getting out?"

    show lilly basic_smile_pat at center
    with charachange
    
    li "The doctor's said that as long as I don't stress my voice too much, I should be fine."

    hi "That's one good thing at least. Not that you'd likely be doing anything overly vocal, anyway."

    show lilly basic_pout_pat at center
    with charachange
    
    li "Is that, perhaps, a statement about my speech?"

    hi "Certainly not."

    show lilly basic_giggle_pat at center
    with charachange
    
    "She gives a small giggle, though suddenly cuts herself short as she cringes."

    "I quickly get off the seat and stand tensed."

    stop music 
    
    hi "Ah, Lilly— {w=.5}{nw}"

    li "It's fine, I just…"
    
    show lilly basic_emb_pat at center
    with charachange

    "She takes a shallow breath and settles back down."

    show lilly basic_pout_pat at center
    with charachange
    
    li "It seems mu throat's not quite fully healed yet."

    hi "It hurts even when you laugh?"

    "As she silently nods, I fall back into the chair with a soft thud."

    hi "That's not stressing your voice, Lilly. You're underplaying this."

    show lilly basic_emb_pat at center
    with charachange
    
    li "It's okay, Hisao. The doctors said it should heal in due time."

    show lilly basic_weaksmile_pat at center
    with charachange
    
    li "Given the rate my throat's been healing, there's little reason to stay in hospital."

    hi "Still, you need to be more careful of yourelf."

    "I glance to the small clock hanging on the wall."

    hi "I'd better get going, Yuuko's waiting for me."

    li "Ah, I take it she drove you to the hospital?"

    hi "Yeah."

    "I rise from the chair with a slight heave."

    hi "Seeya, Lilly."

    li "Bye."
    
    play sound sfx_doorclose
    scene bg hosp_hallway
    with locationchange
    
    "I walk through the door and close it behind me, the sight of Lilly's gentle waving disappearing behind it."

    "The day after tomorrow, Lilly will be back in school."

    "But it won't be the same Lilly as before."

    "No, it's the same Lilly as she's always been."

    "What's changed is our relationship."

    "We're closer than we've ever been before."

    "But by the same token, there's something between us that wasn't there before."

    "Or rather, there's something between us that I'd never noticed."

    "I want to see her happy again."

    "But even as I think that, I don't know where to begin."

    "She's acting so oddly, I can't even begin to guess at what's wrong."

    "And on top of that, even Yuuko's doing strange things."

    "I rub my eyes in annoyance."

    "Grasping this situation seems like trying to catch running water with an open hand."

    scene bg hosp_ext
    with shorttimeskip

    "As I exit the doors of the hospital, I look down to the bench."

    show yuuko worried at leftsit
    with charaenter
    
    "As expected, Yuuko's there."
    
    #yuuko sprite must be sitting here
    
    show akira basic_boo at rightsit
    with charaenter

    "Looking past her though, the stranger from before sits alongside."

    "Elbows on his knees and a can of beer in his hand, he shifts only his eyes to see me."

    hi "Hey Yuuko."
    
    show yuuko panic_down at leftsit
    with charachange
    
    yu "Sorry about leaving you like that."

    hi "Nah, it's fine. Um…"

    yu "Ah, this is…"

    show akira basic_smile at right
    with charamove
    
    "The suited figure stands up, extending his hand casually."

    aki_ "Akira. Akira Satou."

    "I take his hand and give a slight nod."

    hi "Hey. I'm— {w=.5}{nw}"

    aki "Hisao Nakai, right? Yuuko filled me in."

    hi "I… see."

    "I swear he's taking every opportunity he can to tick me off."

    "As we let go of each other's hands, I realise a detail about his name."

    hi "Satou? You're a relative of Lilly's?"

    show akira basic_smile at right
    with charachange
    
    aki "Yeah, you could say that. Folks sent me down to check on 'er."
    
    show yuuko worried_down at leftsit
    with charachange
    
    "I note the almost imperceptible look of annoyance that flickers across Yuuko's face."

    "I guess she and Lilly's family don't get along."

    "He turns back to take the can left on the seat behind him, giving a curt nod to Yuuko."

    show akira basic_boo at right
    with charachange
    
    aki "I'd better be off."

    "The end of the cigarette glowing for a second, he reaches out and pats me twice on the shoulder."

    show akira basic_laugh at right
    with charachange
    
    aki "Take good care o' Lilly, eh? Seeya."

    hide akira #at rightedge
    with charaexit
    
    "And with that, he walks off, his free hand raised."

    hi "Is Akira always like this?"

    "She gives a nod of resignation as she sighs."

    "Those two really don't get along."

    hi "Shall we be off then?"

    scene black
    with dissolve

    window hide
    
    return

label en_L22:
    #scene black with fade
    scene bg school_scienceroom
    with dissolve

    $ renpy.music.set_volume(1.0000000001, 1.0, channel='music')
    
    play music music_daily fadein 10.0
    
    "As I sit watching another of Mutou's long-winded lectures, my mind wanders far from the scribbles on the dirty blackboard."

    "It's only been a week over a month since the festival, yet this school's become a second home."

    "The same school populated by burn victims, amputees, the blind, the deaf and all manner of disabilities inbetween."

    "If someone had described this school to be before I'd come, I'd have shrugged it off as an overactive imagination."

    "It's amazing how quickly one becomes used to the environment they're forced to live in, really."

    "Before my mind can wander any further though, I find a page of lined paper slipped under my bored face."

    # These lines alternate between Hisao and Misha's writing. Maybe Misha could write in pink or red ink?

    window hide
    $ fixedwritten_note(u"Don't look so bored Hicchan, school's nearly over!", text_args={"color":"#FF2AAA"})
    window show
    
    "I covertly uncap my pen and scrawl away at the page before passing it back to her, flicking my eyes to the front of the class every now and again."
    
    window hide
    $ fixedwritten_note(u"I'm guessing you have something planned?")
    window show
    
    "She takes the paper back and hunches over it comically, her tongue poking through the side of her mouth."
    
    window hide
    $ fixedwritten_note(u"Student council work with Shicchan, of course~", text_args={"color":"#FF2AAA"})

    $ fixedwritten_note(u"You're not still brooding over that, surely?")

    $ fixedwritten_note(u"But Hicchan could have helped us poor, lonely girls.", text_args={"color":"#FF2AAA"})

    $ fixedwritten_note(u"I'd lend you a hand for today if I weren't going to be busy.")

    $ fixedwritten_note(u"Ooh, naughty naughty Hicchan~", text_args={"color":"#FF2AAA"})

    $ fixedwritten_note(u"It's just shopping. I'm not going to be doing any funny things.")

    $ fixedwritten_note(u"Funny things? What would “funny things” be?", text_args={"color":"#FF2AAA"})

    $ fixedwritten_note(u"-_-")

    $ fixedwritten_note(u"Lighten up, Hicchan! Weekend~ Weekend~", text_args={"color":"#FF2AAA"})

    $ fixedwritten_note(u"A decent night's sleep would good enough for me.")

    $ fixedwritten_note(u"I hear Lilly's back?", text_args={"color":"#FF2AAA"})

    $ fixedwritten_note(u"Yeah, she was discharged yesterday, so she'd be back in school today.")
    window show
    
    "As she takes the note back and begins to write, I look up to see an unwelcome sight."
    
    stop music

    "As I frantically try to silently grab Misha's attention, Mutou confidently strides though the gaps between the desks from the front of the class, his intent gaze focused directly on her."

    show muto irritated at center
    with charaenter
    
    "She suddenly stops writing as his tall figure casts an impossibly long shadow over the page."

    mi "Ah…"

    "He silently takes the piece of paper from in front of her and begins to read."

    "Sweating bullets, I quickly glance around the class, noting their complete silence. Of course, it would just have to be the one thing that actually gets their attention during the lesson."

    "After a scant few seconds scanning the page, he rolls the paper up into a small tube and lightly bops Misha over the head with it."
    
    show muto normal at center
    with charachange
    
    mu "Half an hour until you can hop off to the student council. I think you can hold off until then."

    hide muto
    with charaexit
    
    "Misha's face cracks as the entire class erupts into laughter."

    "He might well be awkward, but he knows how to handle her excellently."

    "I'd probably feel sorry for her if I weren't as busy laughing as everybody else."

    scene bg school_road
    with shorttimeskip#locationskip

    "After the wryly amusing events of earlier, the rest of the class seems to pass much faster."

    "Walking through the courtyard, I round the corner of the gate to a familiar sight."

    "Lily walks down the path as expected, but beside her isn't the person I was expecting."

    hi "Hey Lilly, Akira."

    show akira basic_smile at twoleft
    show lilly cane_smileclosed at tworight
    with charaenter

    $ doublespeak(aki, li, "Huh?","Yes?")

    aki "Oh, hey Hisao!"

    li "Ah, Hisao. Good afternoon."

    "As Lilly gives a small bow and Akira curtly waves, the difference between the two's reactions is striking, even more obvious thanks to Lilly's even softer-spoken than normal demeanor."

    "I quickly jog up to them and take my place on the outside, Akira taking center and Lilly to the side with her cane skating along the corner of the sidewalk and wall."

    show lilly cane_smile at tworight
    with charachange

    li "I take it you've met Akira then?"

    hi "In… a way."

    hide akira
    with charaexit

    aki "Hey, hey, don't get all cold on me!"
    
    show akira basic_smile at right
    with charaenter

    "He wraps an arm around my neck in an altogether too friendly way, grinning like a madman."

    hi "Anyway, we met outside the hospital. You know, you never said you had a brother."

    show lilly cane_surprised at left
    with charamove
     
    show akira basic_lost at right
    with charachange
    
    li "…"

    aki "…"

    hi "What?"
    
    show lilly cane_reminisce at left
    with charachange

    li "She's… my sister…"

    hi "Oh."

    hi "Wait, WHAT!?"

    show akira basic_kill at right
    with charachange
    
    "Akira lowers her head and looks at me incredulously."

    aki "You… thought I was a guy?"

    hi "Ah… well…"
    
    show akira basic_laugh at right
    with charachange

    "Without warning, he, or should I say she, breaks out into uncontrollable laughter."

    aki "Oh my God, oh my god, this is great! Ha ha ha ha!"

    "She pauses and looks at me for a split second before cracking up once again after seeing my lost expression."

    aki "Bwuahahahaha!"

    show lilly cane_displeased at left
    with charachange
    
    li "Hisao! That's mean!"

    hi "Well… she doesn't seem to be taking it too badly."

    "She slowly begins to collect herself, taking a few deep breaths to reign in her outburst."

    show akira basic_lost at right
    with charachange
    
    aki "Well, haha, moving on."

    hi "Uh, yeah, moving on."
    
    show akira basic_smile at right
    with charachange

    aki "As I was saying to Lilly, looks like I'll be kicking around this place for a while."

    hi "I see."

    aki "Figured that I may as well make the most of it after coming down to check on Lilly."

    hi "You two seem pretty close."

    show akira basic_boo at right
    
    "An unusually quiet Akira flicks her eyes to Lilly before continuing."

    aki "Yeah, you could say that."

    show lilly cane_smile at left
    with charachange
    
    show akira basic_smile at right
    with charachange
    
    li "She is my favourite sister, after all."

    show akira basic_laugh at right
    with charachange
    
    show lilly cane_giggle at left
    with charachange
    
    aki "Why of course, who else would it be?"
    
    show akira basic_smile at twoleft
    with charamove

    "As she gives a grin and a quick hug to Lilly, I decide to take advantage of the direction the conversation's headed."

    hi "So how many sisters do you have, Lilly?"
    
    show lilly cane_listen at left
    with charachange
    
    li "Akira who's twenty-two, and Leanne and Adrianne who are both fourteen."

    hi "So you're the second oldest then?"

    li "Correct."

    show akira basic_boo at twoleft
    with charachange
    
    aki "Shit, that reminds me."

    li "Hmm?"

    show akira basic_smile at twoleft
    with charachange
    
    aki "Ah, I still need to get a souvenir for those two. They were bugging me about it even as I left the damn door."

    show lilly cane_smile at left
    with charachange
    
    li "So they're still like that?"
    
    show akira basic_laugh at twoleft
    with charachange
    
    aki "Yeah. Spoiled brats, both of 'em. At least Leanne's still the cutest little thing ever."

    show lilly cane_cheerful at left
    with charachange
    
    li "Is she still attached to Adrianne?"

    aki "Like a third arm."

    show lilly cane_giggle at left
    with charachange
    
    li "I doubt she'll ever grow out of it, at this rate."

    show akira basic_boo at twoleft
    with charachange
    
    aki "Yeah, you got that right."

    "As I look on, one feeling is stronger than that of being a forgotten third party in the conversation."

    "That is, the feeling that someone is following us."

    hi "Hold on, you two."
    
    show lilly basic_listen at left
    with charachange
    
    show akira basic_lost at twoleft 
    with charachange

    li "You heard it too?"

    aki "Heard what?"
    
    hide lilly
    hide akira
    with charaexit

    "I turn around to see who's following us."

    # Show Emi and Rin sprites, with completely black sunglasses
    show emi basic_annoyed_glass at tworight
    show rin basic_awayabsent_glass at twoleft
    with charaenter
    
    $ doublespeak(rin,emi,u"…")

    hi "What the hell?"

    emi "<My my, would you look at that! These children seem to be looking straight at us!>"

    "She talks in such unbelievably bad English that it takes a couple of seconds to decipher what she's actually saying."

    hi "Emi, Rin, what the hell are you two doing?"

    emi "Why, I am just a random stranger who's name is Sarah MacKenzie, and this is my companion…"

    rin "Heinrich von Eingelbottomstaffenshire."

    rin "The fourth."

    # Sprite change, Emi flat
    show emi basic_confused_glass at tworight
    with charachange
    
    emi "…"

    # Sprite change, Emi annoyed

    show emi sad_angry_glass at tworight
    with charachange
    
    emi "Hey, that's not the name I said you had!"

    rin "Your name was boring. I made a better one."

    emi "We could've fooled him!"

    "I reach forward and pluck the oversized sunglasses from Emi and Rin's faces."

    # regular sprites from now on [str]
    show emi sad_angry at tworight
    show rin basic_awayabsent at twoleft
    with charachange
    
    hi "It takes more than a pair of cheap sunglasses to fool me."
    
    show rin basic_awayabsent at left
    with charamove
    
    show akira basic_evil at center
    with charaenter
    
    "Suddenly, Akira walks past me and observes Emi altogether too closely from the side."

    show emi sad_shy at right
    with charamove
    
    emi "Er… What are you…"

    aki "She's not too bad. Not too bad at all."
    
    aki "Hey Hisao, why didn't you go for her instead? Too young for your tastes?"

    # respawning emi for upcoming scene [str]
    hide emi
    show emi sad_shy at right
    
    hi "Good lord."

    emi "I'm eighteen!"

    aki "Huh, you look closer to twelve. Damn."
    
    show emi basic_shock at right
    with charachange
    
    emi "Why you…!"

    emi "HIYAA-aaagh!"
    
    show emi basic_shock at twocenteroff3
    show akira basic_evil at twocenteroff
    with charamove
    
    show akira basic_evil at center
    with charamove
    
    with Pause(0.5)
    
    show emi excited_circle at twocenteroff3
    with charachange
    
    "As Emi moves to deliver a lightening-fast karate-chop to her side, Akira expertly slides past her outstretched arm and grabs it, pulling it around and pinning it to Emi's back."

    emi "Hey, let go of me! Gyah!"

    aki "Oi Hisao, if you don't take 'er now I'll have 'er!"

    "She's a twenty-two year old female pedophile who knows martial arts."

    "Suddenly I wish I had never met this girl."

    extend " Or consider myself extremely lucky to be graced with her presence. I'm not sure which."

    li "Calm down, Akira!"

    aki "I'm just having a little fun, no 'arm done."

    hi "Just release her."

    aki "Fine, fine."
    
    show akira basic_evil at center
    with charamove
    
    show emi excited_circle at right
    with charamove
    
    "She reluctantly loosens her grip on Emi's arm, taking a step back to avoid any counterattacks."

    "All Emi can do as she rubs her arm is scowl menacingly."

    "Well, as menacingly as she can muster, anyway."

    rin "You're a judo master?"

    aki "Aikido, actually."

    rin "You look a judo master. From the Yakuza."

    "Rin jumps from logical leap to logical leap as if she were a chimpanzee, her rapidfire misinterpretations all but losing the suited figure next to her."

    aki "Uh… huh."

    hi "She's always like that."

    rin "Like what?"

    hi "Odd."

    rin "I would not describe myself as odd."

    aki "How would you describe yourself then?"

    rin "Normal."

    "As Akira looks at me, a pained expression on her face, all I can do is shrug."

    hi "That's how it is."

    emi "Come on Rin, it looks like we've been caught."

    li "You're not coming to the store?"

    rin "No, we were just spying on you."

    emi "Rin…"

    hide emi
    hide rin
    show lilly invis at left
    with charaexit
    
    "With that, they turn to walk off, the two busily dissecting where their plan went wrong as they disappear into the distance."

    aki "Cute pair. Strange, but cute."

    aki "Rin and Emi, right? Friends?"

    show lilly cane_weaksmile at twoleft
    show akira basic_smile at tworight
    with charamove
    
    li "Indeed."

    hi "Yeah. As weird as they are, they're not much stranger than the rest of the school."

    aki "You've got a quick mouth on you, boy. You attend that school too, you know."

    hi "Did I ever say I was normal?"

    aki "You seem normal enough."

    li "Just don't try any of your martial arts on him, please."

    aki "Huh? Why?"

    "I thrust at my chest a couple of times with an outstretched thumb. Her expression shows that she got the hint."

    aki "Ah, I wondered why you were here."

    "She gives a loud groan as she stretches her hands high above her head."
    
    scene bg suburb_konbiniext
    show lilly cane_weaksmile at twoleft
    show akira basic_smile at tworight
    with shorttimeskip
    
    hi "Well, here we are. Aura-Mart."

    aki "So this is where you guys shop, eh?"

    li "Right, though the cafeteria's open for all mealtimes if we want to use it."

    aki "Sounds like you guys could just about live in the school."

    hi "Well, there is the small fact that the cafeteria sucks."

    li "I wouldn't say that, but…"

    aki "Haha, I see what you mean. Well, are we gonna go in, or just talk outside all day?"

    scene bg suburb_konbiniext
    show lilly cane_weaksmile at twoleft
    show akira basic_smile at tworight
    with shorttimeskip

    "As we emerge from the store holding one bag each, Akira's the first to break the silence."

    aki "So, what've you two got planned for Marine Day?"

    hi "Marine day… Ah, that'd be coming up soon, wouldn't it?"

    li "Monday, to be precise. This'll be a long weekend."

    hi "Huh, that soon. Time flies."

    aki "Take it you've got nothing on then?"

    hi "Nah."

    li "Nothing that I know of."

    aki "Excellent."

    li "You have something in mind?"

    aki "Summer house. You know the one Lilly, up North?"

    li "Ah, there. It does bring back memories."

    hi "Haven't been there in a while?"

    li "Last time I was there was… three years ago?"

    aki "Yeah, that sounds about right."

    hi "Where is it?"

    li "Hokkaido. Fairly close to the Northern tip, if I remember correctly."

    hi "Hmm, it'd be nice around there this time of year."

    aki "So, you two going?"

    li "Well, we didn't have much else to do. It would be a nice trip."

    aki "Alright! You takin' Hanako?"

    hi "Oh, you know about Hanako?"

    aki "Yeah. Me and Lilly've been sending letters to each other for a while."

    aki "Heh, you should see what she's written about you…"

    hi "Lilly…"

    li "She's riling you up Hisao, don't listen to her!"

    aki "Woah, she's guilty about something!"

    li "Akira!"

    aki "Haha, fine. I'll ease off. Back to the trip, Hanako going?"

    li "I don't mind. Hisao?"

    hi "I'm easy, may as well bring her along if she wants. The change of scenery might do her good."

    li "Will you come, Akira?"

    aki "Nah, I think I'll hang around here. I've got stuff to attend to and sights to see."

    "Lilly sighs sadly."

    li "Well, your choice."

    aki "Hey, I'll be around when you get back, don't worry."

    scene bg school_dormext_ss
    with shorttimeskip

    "It doesn't take long for us to reach the dorms, and the split we have to take to reach each of our own."

    hi "Well, looks like we'll have to split here."

    "I take my other bag from Akira's hand."

    hi "Thanks for helping carry that up."

    aki "Nah, no problem. You look pretty weedy, so it's the least I could do."

    li "Akira!"

    aki "I just call it as I see it."

    hi "I don't mind. I'm not exactly going to be winning any weightlifting competitions anytime soon."

    aki "Well, if you two are splitting I might as well do the same."

    li "You're welcome to come to my room, Akira."

    aki "Thanks, but I'd better get back to the hotel. Seeyas."

    hide akira
    with charaexit
    
    "She turns and walks off, her hand held in upwards in farewell as she goes."

    "A jazz tune with no beat, singer or direction."

    hi "You keep interesting company."

    li "It's nice to see her again."

    "Her voice is warm as she smiles."

    hi "She does seem nice, if a bit carefree."

    "A small nod from Lilly."

    "Her persona seems to have changed entirely, with her thoughts in another world."

    hi "Well, I'd better be off too. Bye, Lilly."

    li "Good night, Hisao."

    scene bg school_dormhisao_ss
    with locationskip

    "After reaching my dorm room and dropping my bags on the floor, I practically fall onto the bed."

    "To have a family like that…"

    "Being an only child, I all but lost that kind of relationship."

    "Though, I guess not having one would be better than having it taken away."

    "I lackadaisically reach up to the light with an outstretched hand, blocking it from my vision."

    "A brother or sister, to be beside me until I'd leave home."

    "I guess I left that kind of normality behind when I had the heart attack."

    "Clenching my hand, I give up on trying to rewrite history."

    "Right now, what I need is sleep."

    scene black
    with dissolve

    return

label en_L23:
    scene black with fade # why fade? [str]
    scene bg city_trainstation
    with shorttimeskip

    play music music_daily fadein 7.0
    
    "As the morning chill wraps itself around my violently shivering body, I huff into my cupped hands to deperately try and stave off the cold."

    show lilly basic_sleepy_cas at twoleft
    show hanako basic_distant_cas at tworight
    with charaenter
    
    hi "Dammit, Lilly, why'd we have to get here so early?"
    
    show lilly basic_displeased_cas at twoleft
    with charachange

    li "Unfortunately, it looks like the train schedule's against us. The next train to Hokkaido is at two in the afternoon."

    hi "Great. Just great."

    "I pause a moment to wipe some sleep out of my eye, with Lilly taking advantage of the opening."

    show lilly basic_smile_cas at twoleft
    with charachange
    
    li "Cheer up, Hisao. Once we get there it'll be fun."

    hi "Why not just take the Shinkansen? A normal train's going to take hours to get us there, so we may as well take it up as far as we can and switch trains at the end."

    li "There's a certain charm in older trains, wouldn't you agree?"

    hi "I'd agree if I weren't freezing in the morning cold because we decided to take one."
    
    show hanako emb_downtimid_cas at tworight
    with charachange

    ha "I'm… sorry, Hisao."

    hi "Sorry? For what?"

    ha "I… was the one who suggested taking a normal train."

    "Way to make me feel guilty. All I can do is sigh and cover my face with my hand."

    hi "It's fine, I'm just grumbling."

    show lilly basic_ara_cas at twoleft
    with charachange
    
    li "My my, Hanako, you needn't shoulder all the blame yourself. If not for your suggestion, I'd stil have opted for the same thing."

    show hanako emb_smile_cas at tworight
    with charachange
    
    hide hanako
    hide lilly
    with charaexit
    
    "Thankful for the quick interception from Lilly, I take a quick gander around the station."

    "Aside from us, the train platform's all but deserted, the morning dew settling on the empty benches."

    "I guess no one else was masochistic enough to brave the conditions."

    "Though, if there was, they'd more than notice the huge bags both Lilly and Hanako brought with them."

    hi "Just what did you find to pack into those things, anyway?"

    show lilly basic_listen_cas at center
    with charachange
    li "The bags? Hmm…"

    "She pauses a moment and looks upwards in thought."
    
    show lilly basic_smileclosed_cas at center
    with charachange

    li "A change of shirt, change of skirt, raincoat, underwear, sleepwear, two books… I think that's most of it."

    hi "You make it sound as if I'm unprepared…"

    show lilly basic_surprised_cas
    with charachange
    
    li "You brang less?"

    hi "Underwear and a pack of cards. That's it."

    li "No pajamas?"

    hi "…Dammit. I knew I forgot something."

    "As I rough my hair in frustration, Lilly sighs."
    
    show lilly basic_weaksmile_cas
    with charachange

    li "There might be clothing still there, the summer house is for use by the entire Satou family, after all."

    show lilly basic_smile_cas
    with charachange
    
    li "I shan't see any problem in you borrowing a set of pajamas, if need be."

    hi "Thanks. Still, I don't mind just sleeping in my normal clothing."

    show lilly basic_surprised_cas
    with charachange
    
    li "After two days?"

    hi "Point."

    "Almost as soon as I say the word, a loud train whistle beckons from the rails ahead."
    
    hide lilly
    with charaexit

    "Looking past Lilly and Hanako, though, the train's still well out of sight."

    "A quick check of my watch is enough to see that it's our ride."

    hi "The six-thirty train was ours, right?"

    show lilly basic_smileclosed_cas at twoleft
    show hanako basic_distant_cas at tworight
    with charaenter
    
    li "Correct."

    hi "Either of you want me to take your bags? Mine's not exactly heavy."

    show lilly basic_ara_cas at twoleft
    with charachange
    
    li "My my, that's very gentlemanly of you, Hisao."

    hi "Don't accept too reluctantly, now."

    "As I bend down to pick up Lilly's large bag, I look up to see Hanako picking up hers."

    hi "You fine with that?"

    show hanako basic_normal_cas at tworight
    with charachange
    
    "A silent nod's the only answer."

    "I'm starting to get the feeling that I'll be able to count every sentence she says by trip's end on one hand."

    stop music fadeout 50
    
    play ambient sfx_trainint fadein 5.0
    
    scene black
    
    scene train_scenery
    show train_scenery_fg
    show evfg lilly_trainride
    with shorttimeskip

    hi "Do you have a… ten of clubs?"

    ha "Go fish."

    ha "Do you have a five of diamonds?"

    hi "Go fish."

    hi "Have an ace of diamonds?"

    ha "Mm, here."
    with shorttimeskip

    ha "I'll raise by five."

    hi "…I see that and raise you six."

    ha "Fold."
    with shorttimeskip

    ha "How come some of the cards have different patterns on the back?"

    hi "Some of the cards come from another pack after I lost some."

    ha "I see."

    # Timeskip

    hi "How's the book, Lilly?"

    li "Quite good, actually."

    hi "What title is it?"
    
    #show evfg lilly_trainride_smiles at train_shake
    show evfg lilly_trainride_smiles
    with charachange

    li "<To Kill a Mockingbird.>"

    hi "Foreign?"

    li "Correct. American, to be exact."

    hi "Translated?"

    li "No, it's in English."

    hi "I see."
    with shorttimeskip

    ha "King of clubs."

    hi "Go fish."

    ha "Why do some of these cards have folded corners?"

    hi "They've just been heavily used."

    ha "I see."

    hi "Ten of diamonds."

    ha "Here."
    with shorttimeskip

    hi "Who was the one that decided to take a normal train?"

    ha "Me."

    hi "Ah, that's right."

    ha "Six of hearts."

    hi "Go fish."
    with shorttimeskip

    ha "I'm out of cards."

    hi "Ha, I win!"

    li "Hisao?"

    hi "Yes?"

    li "You shouldn't cheat when playing dear Hanako."

    hi "Damn."

    ha "Uweeh!?"
    
    scene bg hok_houseext
    with shorttimeskip#locationskip
    
    play music music_tranquil fadein 3.0
    play ambient sfx_park fadein 4.0


    "After a seemingly endless trip, we finally reach the promised land of Lilly's summer house."

    "Even after the train trip, the walk up almost took half that time again."

    "Despite my grumblings though, I'd have never guessed the sight that would be in store for us as we walked along that long, deserted road."

    "It looks more like a farmhouse than a summer house, small in size and surrounded by trees."

    "Out the back though, the empty expanse of wheat fields and farming land seem to stretch on forever."

    "It's a majestic sight, and one rare to see just about anywhere."

    "The only thing that doesn't surprise me is it's Western styling."
    
    show bg hok_houseext at left
    with locationchange #None

    hi "This is amazing…"
    
    show lilly basic_smileclosed_cas at twoleft
    show hanako basic_bashful_cas at tworight
    with charaenter

    ha "Mm, it's wonderful."
    
    show lilly basic_smile_cas at twoleft
    with charachange

    li "It seems to have changed little since I last visited."

    hi "It looks like there isn't another soul for miles."
    
    show lilly basic_listen_cas at twoleft
    with charachange

    "She furrows her brow in thought, seemingly recounting almost forgotten knowledge."

    show lilly basic_weaksmile_cas at twoleft
    with charachange
    
    li "Hmm, from memory there's a small town not too far ahead. Other than that though, there's a large expanse of rural country."

    hi "To find a place like this in Japan nowadays… it's kind of anachronistic."
    
    show lilly basic_smileclosed_cas at twoleft
    with charachange

    li "Well, this town does have quite a bit of history."
    
    "I look down the street one last time before getting back to the task at hand."

    hi "Shall we go in, then? I'm parched."
    
    show hanako basic_normal_cas at tworight
    with charachange
    
    show lilly basic_smile_cas at twoleft
    with charachange
    
    hide hanako
    hide lilly
    with charaexit
    
    scene bg hok_lounge
    with locationchange

    "I look out the window to the orange setting sun."

    hi "Where should we put our bags?"
    
    show lilly basic_smileclosed_cas at twoleft
    show hanako basic_normal_cas at tworight
    with charaenter

    li "I'll show Hanako our bedroom. You can put yours here."

    hi "You mean I don't have the same bedroom as you two?"
    
    show lilly basic_ara_cas at twoleft
    with charachange
    
    show hanako emb_emb_cas at tworight
    with charachange

    li "Hmm, I shan't think Hanako to appreciate it I'm afraid."

    hi "It was worth a try."

    ha "L—Lilly!"
    
    show lilly basic_giggle_cas at twoleft
    with charachange
    
    show hanako emb_timid_cas at tworight
    with charachange

    li "My my, Hanako. I'm just joking, I assure you."

    "Even as she says that though, I can't help but regret it a little."

    hi "Hold on, if I'm to leave my bags here, where will I be sleeping?"

    li "Well, seeing as we lack a guest bedroom…"
    
    show lilly basic_concerned_cas at twoleft
    with charachange

    hi "The couch, huh?"

    li "Sorry, Hisao."

    hi "Well, it can't be helped."
    
    hide lilly
    hide hanako
    with charaexit

    "After she leaves to show Hanako to their bedroom, I take a quick account of my surroundings as I drop my bag on the floor."

    "To say the exquisite couch is large is an understatement, indeed, the entire room as extravagant as can be."

    "It looks more like a nobleman's bedroom during the renaissance than a summer house."

    "As I scan around the room, one thing looks distinctly out of place given the look of yesteryear."

    hi "Huh, a TV."

    "I crouch down to the table in the center of the room and pick up the controller, pointing it at the black box."

    "It immediately flickers to life, apparently set to a news channel."

    "Television" "—launch of the shuttle Discovery, carrying the Japanese astronaut Nobusa…"

    li "Ah, I see you've found the television."
    
    show lilly basic_smile_cas at twoleft
    show hanako basic_smile_cas at tworight
    with charaenter

    "I look behind me to see Lilly and Hanako, their bags absent."

    hi "Yeah. Seems kind of out of place for such a lavish room."

    li "Well, some allowances must be made for the times."

    "Hanako gives a deep yawn, only just remembering to cover her mouth at the last minute."

    show hanako emb_downsad_cas at tworight
    with charachange
    
    show lilly basic_smileclosed_cas at twoleft
    with charachange
    
    li "My my, are you tired, Hanako?"

    show hanako basic_smile_cas at tworight
    with charachange
    
    ha "Ah, mm. I didn't get much sleep last night."

    hi "I'm kind of pooped too, come to think of it. That was a bloody long walk up here."

    li "If that's the case, I suppose we should retire for the night. Good night, Hisao."

    ha "Good night."

    hi "'Night."
    
    hide lilly
    hide hanako 
    with charaexit
    
    stop music fadeout 5.0
    $ renpy.music.set_volume(1.0, 8.0, channel='music')


    "With that, they quietly turn and walk back to their bedroom."

    "Looking down at the couch, I give a sigh."

    "I suppose I'll watch some TV quietly before going to bed."

    scene black
    with dissolve

    return
    
label en_L24:

    scene black
    with None #dissolve
    
    $ renpy.music.set_volume(0.5, 0.0, channel='ambient')
    play ambient sfx_park fadein 6.0

    li "Hanako, is he still sleeping?"

    ha "I think so."

    "I'm not."

    li "Hmm, it is late in the morning by now."

    "I know that."

    ha "Maybe he stayed up watching TV too long?"

    li "He did seem to have it on at least as we went asleep."

    "Only because I couldn't do the same."

    ha "Should we wake him?"

    "Don't do that, Hanako."

    li "No, we should leave him. I doubt he'd want to be woken early if he didn't get much sleep during the night."

    "Thank you, Lilly."

    li "Besides, he sounds so peaceful…"

    "Straight face, Hisao. Keep a straight face."

    ha "Um, Lilly…"

    "Hmm?"

    "I suddenly feel Lilly's outstretched hand gently rest on my chest."

    "C—c—c—c—c—calm, Hisao! Calm!"

    "As I struggle to keep my composure, a choking silence passes."

    "Seconds, minutes, hours, how long a time passes is all but lost."

    "The only thought in my mind is of that gentle, outstretched hand laying upon my chest."

    li "Hanako?"

    ha "Ah, yes?"

    li "Could you go to the fridge and fish out what's needed to make lunch?"

    ha "Alright, just the vegetables and rice?"

    li "Mm, that should be enough."

    "Hanako's footsteps on the carpeted floor can be heard moving away from the living room, with Lilly's hand still on my chest."

    "Another silence, though this time Lilly breaks it sooner, withdrawing her hand as she does."

    li "Good morning, Hisao."

    $ renpy.music.set_volume(1.0, 3.0, channel='ambient')
    play music music_dreamy fadein 8.0

    scene bg hok_lounge 
    show lilly basic_smileclosed_cas at center 
    with openeye

    "Conceeding defeat easily, I prop myself up and rub my eyes."

    hi "How'd you know?"
    
    show lilly basic_weaksmile_cas
    with charachange

    li "Your breathing was irregular."

    hi "Ah."

    show lilly basic_displeased_cas
    with charachange
    
    li "If you want to sleep more, you should really go to bed earlier. Hanako and I heard the television going long into the night."

    hi "Uh, sorry about that. My meds've been screwing with my sleep constantly. Even if I'm tired I have trouble actually sleeping."

    show lilly basic_oops_cas
    with charachange
    li "Ah…"

    li "I'm… sorry, Hisao."

    hi "Come on, you worry about it more than I do at times."

    show lilly basic_reminisce_cas
    with charachange
    
    li "But still…"

    hi "I. Am. Fine. Stop worrying."

    "She gives a sigh of abject consternation, giving up the point."
    
    show lilly basic_weaksmile_cas
    with charachange

    li "If you say so. Do please take things easily, Hisao."

    hi "Like you did with your tonsillitis?"
    
    show lilly basic_pout_cas
    with charachange

    li "That was different!"

    hi "Was not."

    li "Was so."

    hi "Was not."

    li "Was so."

    hi "Was so."

    li "Was not."
    
    show lilly basic_emb_blush_cas at center
    with charachange
    with Pause(1.0)
    
    show lilly basic_pout_cas at center
    with charachange

    li "Erk."

    hi "Go on, Hanako could use some help."
    
    show lilly basic_smile_cas at center
    with charachange

    li "I'll never understand you, Hisao."

    "I snort and give a playful grin."

    hi "Hey, that's my line."
    
    hide lilly

    "And with that, she disappears to the kitchen, her hand running along the smooth white walls as she slowly and elegantly walks."

    "I suppose I'll follow her. It's not like I have anything better to do, after all."

    "With a quick press on the remote control for some background noise to kill the deafening silence, I head out."

    scene bg hok_kitchen
    with locationchange

    "As I round the corner, I see Hanako and Lilly, backs turned, quietly cutting food on the granite-coloured counter."

    "I can just see Lilly guiding the knife down slowly with a finger on the carrot she's cutting."

    hi "You two want any help?"
    
    show lilly back_smile_cas at twoleft
    show hanako basic_normal_cas at tworight
    with charaenter

    li "Hmm, can you cook?"

    "That's not the question I was expecting."

    hi "Those bags of food don't cook themselves, you know."

    li "A point. Thanks, Hisao."

    "Hanako simply smiles and nods as I begin to grab food from the fridge."

    hide hanako
    hide lilly
    with charaexit
    with shorttimeskip
    
    scene bg hok_lounge
    with shorttimeskip
    
    play music music_another fadein 8.0

    "As I lay out the plates of food, steam slowly rising from the well-cooked rice and curry dishes, Hanako lays out the utensils."

    "Knife one side, fork on the other. Western."

    "How perfectly fitting, I think to myself."

    "As we take our seats, taking careful heed of the dark red tablecloth hanging below our knees, Lilly emerges from the kitchen."

    "In her hands are three glasses, and… a bottle of white wine."

    "As I recall our previous runins with that devilish elixir, I hide my face in my palm."

    hi "Alcohol?"

    show lilly basic_cheerful_cas at center
    with charaenter
    
    "She pauses as she reaches the table, a playful grin perched on her smiling face."

    show lilly basic_giggle_cas
    with charachange
    
    li "Did you expect any differently?"

    hi "I guess I shouldn't have."
    
    show lilly basic_smileclosed_cas at center
    with charachange

    li "A glass of wine shan't cause trouble, I assure you. Moderation is what's important."

    show lilly basic_smile_cas
    with charachange
    
    hi "You passed out on my bed the last time you got into that stuff."

    show lilly basic_pout_cas
    with charachange
    li "That was different."

    hi "Was… "

    extend "…I give up. Pour me a glass."

    show lilly basic_smileclosed_cas
    with charachange
    
    "As she dips her finger inside to feel the liquid level, I look through my obscuring fingers."

    "The white of her finger almost seems to glow as the sunlight hits it, the delicate outline blurred and refracted by the glass."

    "Her finger's definitely longer than mine, though roughly the same thickness."

    "Her fingernail, though, seems to be cut quite short for a girl's."

    "I guess they'd only get in the way when the only way she can percieve the world is through touch."
    

    "…I need to stop thinking about her finger. Of all the things to think about."

    "Quickly shaking the thoughts out of my mind, I see that both Hanako and Lilly's glasses have already been poured."

    hide lilly 
    with charaexit
    
    "As we quickly dig in to our meal, the clatter of forks and knives against plates rings out."

    "None of us are particularly eager to speak whilst eating, Lilly altogether too reserved for such a thing, Hanako probably too shy to start conversation, and I too busy savouring the food."

    "Such a pedestrian activity, eating together at a table."

    "It seems so utterly normal."

    "…I guess that's why I'm enjoying it so much."

    "A little oasis of normality in my strange, strange life."
    
    with shorttimeskip

    "It takes all too little time for everyone to finish eating, the wine thankfully having little effect at these amounts."

    "I slump back into the seat, patting my stomach contently."

    hi "I'm stuffed."
    
    show lilly basic_smileclosed_cas at twoleft
    show hanako basic_smile_cas at tworight
    with charaenter

    "Lilly pats her mouth twice with a knapkin."

    "Twice, only twice, and with evenly timed intervals inbetween."

    "It's hard to tell sometimes whether how she acts is a well-trained routine or a well-rehearsed act."
    
    show lilly basic_satisfied_cas at twoleft
    with charachange

    li "Indeed. Hanako?"
    
    show hanako cover_bashful_cas at tworight
    with charachange

    ha "It was nice."

    li "Now that we're well fed, shall we be off?"

    hi "Off? Where?"
    
    show lilly basic_weaksmile_cas at twoleft
    with charachange

    li "Ah, you weren't privvy to the discussion between Hanako and I."
    
    show hanako basic_bashful_cas at tworight
    with charachange

    ha "We'll be going into the town nearby."

    hi "Ah, I see. How long's the walk in?"
    
    show lilly basic_smile_cas at twoleft
    with charachange

    li "Hmm, it'd be around a mile to my mind."

    stop music fadeout 4.0
    hi "Nearby, huh? Great."

    "Just great."

    scene bg hok_road at bgright
    with locationskip
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    play ambient sfx_park fadein 6.0
    play music music_soothing fadein 0.5

    "As we walk up the side of the road, I watch Lilly and Hanako walking ahead."

    "The slight breeze all but whisks away the sound of Lilly's cane gently tapping on the ground."

    "A deep, lung-filling breath of the fresh country air makes me wish all the harder that the air around home had been quite so clean."

    "It can't have even been half a mile, but I'm already working up a sweat."

    "Though, it isn't the coolest day on record either."

    hi "Hey Lilly, how do you know this town, anyway?"
    
    show lilly back_smileclosed_cas at center
    show prop lilly_back_cane
    with charaenter

    li "I went to it the year before I entered Yamaku, while I was staying at the summer house."

    "I quickly take a moment to pump my hands a couple of times, staving off the oddly cold feeling in them."

    hi "Like it up here?"
    
    show lilly cane_weaksmile_cas
    hide prop
    with charachange

    li "Mm, it's nice and quiet."

    hi "Well, quiet it certainly is."

    "Though, lonely is how I'd put it."

    "Other than the prophesised small town, supposedly not worthy of being called much more than a village, there isn't another soul for miles around."

    "Coming from a home nestled deep within the big city, it's an almost eerie atmosphere."
    
    show lilly cane_smile_cas
    with charachange

    li "Ah, Hisao?"

    "Lilly's voice cracks through my thoughts with the force of a lightning strike."

    hi "Yeah?"

    li "Have you been to Hokkaido before?"

    hi "Nah. I used to live down south, and there weren't any field trips up this far."
    
    show lilly cane_cheerful_cas
    with charachange

    li "Well, it's a new experience then."

    hi "Sure is."

    hi "You ever been up here, Hanako?"
    
    show lilly cane_cheerful_cas at twoleft
    show bg hok_road at center
    with charamove
    
    show hanako emb_smile_cas at tworight
    with charaenter

    "She shakes her head from side to side."
    
    show hanako basic_bashful_cas at tworight
    with charachange

    ha "It's my first time too."

    "As we continue walking, I begin to feel pins and needles in my legs."
    
    stop ambient fadeout 9.0
    
    stop music fadeout 4.0

    hi "Ah, could you two hold on a moment?"
    
    show lilly cane_surprised_cas at twoleft
    with charachange

    li "Hmm?"

    hi "Ah, I've just got pins and needles in…"
    
    window hide
    
    play sound sfx_heartslow

    show heartattack alpha 
    with Dissolve (0.1)

    hide heartattack alpha 
    with Dissolve (0.2)

    with Pause(0.7)

    play sound sfx_heartfast
    show heartattack alpha 
    with Dissolve (0.1)

    hide heartattack alpha 
    with Dissolve (0.8)

    with Pause(0.05)

    play sound sfx_heartstop
    show heartattack alpha 
    with Dissolve (0.1)

    show heartattack residual 
    with Dissolve (0.8)

    play music music_tragic fadein 0.5

    window show
    
    "My vocal cords suddenly become taught as my chest tightens instantaneously."

    "I quickly pull my upper arm over it, trying to quell the shot of pain spreading throughout my entire body."
    
    show lilly cane_reminisce_cas at twoleft
    show hanako defarms_strain_cas
    with charachange

    ha "Hisao?"

    play sound sfx_heartslow

    show heartattack alpha 
    with Dissolve (0.1)

    show heartattack residual 
    with Dissolve (0.8)

    hi "I'm fine, I'm fine. Just tired."

    "As I remove my arm from my chest and beging walking again."

    "It only takes a couple of steps before my legs turn to jelly, all tension in my knees seeming to evaporate."

    "Before I can react, they uselessly give way under my weight and leave me only just enough time to brace and fall onto all fours."

    scene bg hok_road at left
    with charamove
    show lilly cane_reminisce_cas at twoleft
    with charachange
    
    scene bg hok_road at right
    with charamove
    
    show hanako defarms_strain_cas at tworight
    with charachange
    
    show heartattack residual 
   
    play sound sfx_pillow
    with vpunch

    hi "Ah, damn…"
    
    scene bg hok_road at center
    with charamove
    
    show hanako defarms_shock_cas at tworight
    with charachange

    ha "Hisa… KYAAAH!"

    "As I look up to her, I realise my face is still taught with pain."
    
    show lilly cane_oops_cas at twoleft
    with charachange

    li "Hisao!? Hanako, tell me what's going on!"

    li "Hanako, tell me!"
    
    show hanako def_strain_cas_close
    with characlose

    "As Hanako stands there, petrified, I lower my face and take a deep breath."
    
    scene black 
    show heartattack alpha 
    with shuteyefast

    "The medications."

    "I didn't take them this morning."

    "My daily bribe to Death, missed in a flurry of excitement."
    
    stop music fadeout 9.0

    hide heartattack 
    with Dissolve(3.0)

    "As I take another breath, the pain begins to die down as suddenly as it had come on."

    "Thank God. Thank God. Thank God, thank God, thank God."
    
    play ambient sfx_park fadein 6.0

    scene bg hok_road 
    show lilly cane_oops_cas at twoleft 
    show hanako def_strain_cas_close at tworight 
    with openeye

    "As it does, I become acutely aware of the sweat by now pouring off my face."

    show lilly cane_reminisce_cas at twoleft
    with charachange

    li "Hisao! Say something, please!"

    hi "I'm fine, Lilly. I'm fine."

    "I furrow my brow and lever myself up, stumbling a bit before regaining my balance."

    "As I look to both Lilly and Hanako, worry's written on both their faces."

    "I feel awful."

    "Really, really awful."

    show lilly cane_sad_cas at twoleft
    with charachange

    li "I think we should go back."

    hi "I…"

    "As I begin to object, I look away in frustration."

    hi "Fine."
    
    stop ambient fadeout 2.0

    scene black
    with dissolve
    
    return
    
label en_L25:

    scene bg hok_lounge
    with openeye    
    
    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')
    play ambient sfx_cicadas fadein 2.0

    "I open my eyes groggily."

    "Completely bereft of energy, I simply lie in place and stare at the ceiling."

    "We went to walk to town. My heart nearly gave way. We came back. I slept."

    "I can only remember each period of time as a snapshot, but the timeline is clear enough."

    "If I look at the ceiling hard enough, I can imagine the tile edges and small dimples of the ceiling in the hospital."

    "That alone is enough to make me pull myself up."

    "I scratch the back of my dishevelled hair, glancing around the room."

    "Lilly and Hanako are nowhere to be seen, and the television's off."

    "The time on the clock above it says it's six in the evening. Despite that though, the sky outside the windows is still a bright blue."

    "I turn and pick myself off the couch, swaying slightly as I put my arms out for balance."

    "I suppose I'd better go look for them."

    "As I lazily look out the window, I see something in the distance."

    "Straining my eyes to make it out, the shape of a person's figure, a long skirt blown to the side by the wind, comes into view."

    "…Lilly?"

    "Without a second thought, I walk from one room to another until I find the door outside."

    scene white
    with dissolve
    
    stop ambient fadeout 2.0
    play music music_innocence fadein 14.0

    scene bg hok_wheat
    with locationchange

    "The brightness of the sun assaults my freshly woken eyes, forcing me to avert them until they adjust."

    "As I look back up though, that solitary figure is still there."

    "The long, yellow strands of wheat brush against my legs as I wade through them, the densely-grown field making it almost impossible to advance."

    "Regardless, my eyes stay ahead, true to that solitary figure."

    "Within minutes I reach her, meters behind her turned back."

    hi "Lilly?"
    
    show bg hok_wheat at right
    show lilly back_pout_cas at center
    with charaenter

    "She simply nods."

    hi "Where's Hanako?"
    
    show lilly back_listen_cas 
    with charachange

    li "She's in bed. She went to sleep after I calmed her down."

    "She says it of-a-matter-of-factly, as if it were as true as night becoming day."

    "There's something different about her."

    "Her normally confident figure seems oddly fragile, her body offering little resistance to the breeze blowing at her skirt."

    "The strands of wheat sway from side to side as a deafening silence passes, the only sound being their rustling."

    "Those events in the hospital."

    "As we stand in the field alone, I know what I have to ask."

    hi "Lilly, you're hiding something from me. What is it?"
    
    show lilly back_sad_cas
    with charachange

    li "Remember when I talked of my stay in the boarding school, Hisao?"

    hi "The boarding school…"

    "I look downwards in through, sifting through my scattered memories."

    "The event seems to leap at my hand as I search for it, rising to the surface as soon as it was recalled."

    hi "In the music room, before the festival."
    
    show lilly back_sad_cas 
    with charachange

    "She gives a simple nod."

    li "I was sent there when I was six."

    li "“The Japanese Institute of Learning for the Blind and Vision-Impaired”"

    li "At the time, my family lived in South Africa, though they still do."

    li "My only contact with them was through Akira."

    li "She was the only one to remain in contact with me."

    "She gives a deep, slightly uneven, breath."
    
    show lilly back_pout_cas
    with charachange

    li "But she stopped. Not by her own volition, but by my father."

    li "That was the one time when, more than anything, I hated myself."

    li "The fact that I couldn't see was the only reason I was forced to enter that school."
    
    stop music fadeout 4.0

    "She says it with more than a hint of scorn."
    
    show lilly back_sad_cas 
    with charachange

    li "So I learned to hide it."

    hi "Hide what?"

    li "Everything—Sadness. Anger. Emotions."
    
    show lilly back_smileclosed_cas 
    with charachange

    li "After all, as long as I smiled, everyone was happy."

    li "As long as I smiled, everything would be okay."

    li "But… I can't do that any more. As much as I wish I could, I can't."
    
    show lilly back_sad_cas 
    with charachange

    li "I lost Akira then. I can't… lose you as well."

    "As her voice begins to break, her hands tighten."

    hi "Why?"
    
    show lilly basic_concerned_cas at center
    with charachange

    "She turns around."

    "Tears roll down her porclain cheeks, her mouth and hands clenched tight."
    
    show lilly basic_concerned_cas_close at center
    with charachange

    li "Because I love you, Hisao."

    play music music_romance fadein 2.0
    
    li "Isn't it silly?"

    li "I love you… but I can't smile."
    
    show lilly basic_sleepy_cas_close at center
    with charachange

    "So… that was it."

    "She created a shield around herself. A barrier. A facade."

    "One which held up for years, for the sake of others."

    "For Hanako. For Akira. For everyone."

    "And now… I'm the one who breaks it."

    hi "You idiot."

    show lilly basic_surprised_cas_close at center with charachange

    li "Hi… sao?"
    
    "I slowly walk towards her, the wheat giving way with each step."

    "My heart isn't racing, nor pounding."

    "In fact, this feels like the most natural thing I've ever done in my life."

    "As I stop in front of the fragile, quivering figure, I smile deeply and gently put my hands on her shoulders."

    "She pauses, her expression becoming lost for a fleeting moment."

    hi "Everyone wouldn't be happy, you said that yourself."

    hi "Lilly, I want to see every single emotion you have."
    
    show lilly basic_oops_cas_close at center
    with charachange

    hi "Sadness, anger, whatever you feel."

    hi "But most of all, I want to see your smile."

    hi "Your true smile."

    "I single gust of wind rustles the wheat, a second's silence passing."

    hi "Smile when you want to smile. Cry when you want to cry."

    hi "I love you, Lilly. So you don't have to hold back any more."

    "With that, she falls into my arms, her face beside mine."
    
    window hide
    
    show ev lilly_wheat_large at center
    show ovl lilly_wheat_foreground
    with whiteout
    
    window show

    # Event CG

    "As her tears fall down my back, she faulters and breaks down, bursting into tears."

    li "Hisao! Hisao!"
    
    show ev lilly_wheat_small
    with whiteout

    "I close my eyes and bring my head down to her shoulder, holding her shaking frame tightly."

    hi "It's okay, Lilly. I'll never go away."

    hi "I promise."
    
    stop music fadeout 6.0

    scene black
    with dissolve
    
    return

label en_L26:

    scene bg hok_lounge_ss
    with locationchange

    "After a slow walk back to the house as we held each other tightly, we gently take a seat on the couch inside."

    "Lilly leans her head onto my shoulder, my arm still around her waist."

    "Neither of us has any want to break the silence."

    "With her eyes shut, it's hard to work out whether she's fallen sleep."

    "Not that I mind."

    "The warmth of her body leaning against me, the softness of her hand delicately held in mine."

    "It's a feeling I'll relish for a long time, if not for as long as I'll live."

    "For minutes on end, we sit against each other, not a single sound to be heard."

    "Eventually, Lilly's voice softly and quietly ends the silence."
    
    show lilly basic_smileclosed_cas_close at center
    with charaenter
    
    play music music_twinkle fadein 6.0

    li "Thank you, Hisao."

    hi "Thank you?"
    
    show lilly basic_smile_cas_close at center
    with charachange

    li "For returning my feelings."

    hi "Did you think I wouldn't?"
    
    show lilly basic_weaksmile_cas_close at center
    with charachange

    li "There was the possibility."

    "I take a deep breath in thought. That much was only my fault."

    hi "I'm sorry. I… wasn't sure myself for a long time."
    
    show lilly basic_oops_cas_close at center
    with charachange

    hi "The world moved around me. Everyone moved around me. I looked to my sides, but never ahead."

    hi "I just went with whatever happened, letting the flow take me."

    hi "I never considered what you were feeling. What anyone was feeling."

    hi "I'm sorry, Lilly."
    
    show lilly basic_weaksmile_cas_close at center
    with charachange

    "She gives a weak smile as she shakes her head, her light hair rubbing against my shoulder."
    
    show lilly basic_smile_cas_close at center
    with charachange

    li "You are thoughtful, Hisao. That's why I like you."

    li "To be honest, I'm pleased my plan didn't work."
    
    show lilly basic_satisfied_cas_close at center
    with charachange

    hi "Plan?"
    
    show lilly basic_reminisce_cas_close at center
    with charachange

    "She opens her eyes, her delicate smile slipping."

    li "I thought that, perhaps, Hanako needed a different type of relationship to move forward."

    li "So… I tried to bring you and Hanako together."

    "A pause, seemingly reviewing her memories."
    
    show lilly basic_emb_cas_close at center
    with charachange

    li "I misjudged her, though. She didn't need courtship. All she wanted was friendship."

    li "I didn't see that, and also ended up falling for you."
    
    show lilly basic_reminisce_cas_close

    "She trails off, sadness filling her face and a newfound silence hanging in the air."

    "The tea party. The picnic. The journeys into town."

    "She did seem to become trusting very quickly, but I'd never questioned why."

    "I gently bend my head down, giving her a kiss on her light, whispy hair."

    hi "We're a couple of right old fools, aren't we?"
    
    show lilly basic_smileclosed_cas_close at center

    li "…Mmm."

    "After a moment's silence, she speaks again."

    li "Hisao?"

    hi "Hmm?"

    li "I…"
    
    stop music fadeout 4.0
    
    show lilly basic_weaksmile_cas_close at center
    with charachange

    li "I wouldn't mind if you… took me."

    "I feel her hand tensing under mine, trembling slightly."

    "My mouth opens, not quite sure of what to say."

    hi "Lilly…"

    "Before I can say another word, she slips her hand from under mine, gently taking the side of my face in it."
    
    show lilly basic_pout_cas_close at center
    with charachange

    "Taking her head from my shoulder, her unseeing eyes meet mine, a mixture of trepidation and love within them."

    li "Please."

    "I give a deep smile, taking her hand in mine as I give a single nod."

    hi "Okay."
    
    play music music_heart fadein 0.5
    
    show lilly basic_smileclosed_cas_close 
    with charachange

    "As I look into her eyes, she leans towards me, her hand firmly on my cheek."

    "Her delicate lips touch mine, almost blanking my mind."

    "She breaks off nary a second later, faintly smiling."
    
    show lilly basic_smile_cas_close
    with charachange

    li "I love you, Hisao."
    
    show lilly basic_smileclosed_cas_close
    with charachange

    hi "I love you too."

    "We kiss again, this time with both of us meeting the other."

    "While the previous kiss was one of love, this is one of unbridled lust, our tongues entangled and our breathing heavy."

    "After precious seconds we part, both our faces well and truly flushed."
    
    show lilly basic_pout_cas_close at center
    with charachange

    li "Ah…"

    hi "What is it?"
    
    show lilly basic_weaksmile_cas_close at center
    with charachange

    li "Should we… go on the floor?"

    hi "Hmm? Ah, y—yeah…"

    "Now that she mentions it, the couch would be somewhat awkward to do much on."

    "At least one of us is thinking straight."
    
    show lilly invis
    with dissolvecharamove
    
    hide lilly
    with vpunch

    "I take her hands and guide her sideways as I move, both of us tentatively sitting on the carpet."

    "As I reach forward to undo the top button on her shirt, she stops as she moves her hands towards the top of mine."

    li "You're shaking."

    "I pause for a moment and look at my hands."

    "Sure enough, they're quivering slightly. Whether it's from nervousness or excitement, I'm not sure."
    
    show lilly basic_weaksmile_cas_close
    with charachange

    hi "Uh… I guess they are."

    "She gives a weak smile."

    li "So you're as nervous as I am, then?"

    show lilly basic_cheerfulblush_cas_close
    with charachange
    
    "I withdraw my hands and give a sigh, steadying myself."

    hi "Well, I guess it's the first time for both of us, after all."
    
    show lilly basic_smile_cas_close    
    with charachange

    li "Mm."

    li "I'm… glad to have it with you, Hisao."

    "I match her smile twofold, leaning forward and taking her body in my arms as she reaches to hug me back."

    hi "I love you, Lilly."
    
    show lilly basic_smileclosed_cas_close
    with charachange

    li "You already said that."

    "I can't help but grin. Even in such a situation, she still has her wits."

    hi "That's because I mean it twice as much."
    
    hide lilly
    with charaexit

    "We break apart, her hand sliding around my body and finding the top button."

    "With a slightly stiff hand, I manage to undo the buttons on her shirt as she does mine."

    return

label en_L26h:

    show lilly behind_smileclosed_nak
    with charaenter
    
    "As we take off the last of our clothes, all of them now haphazardly piled behind us, my breath is taken."

    "Her long, shapely legs, those full hips and pale, plump breasts…"

    "Her tall, porclain-white body, all but bare, is staggeringly beautiful."

    "Her hands, tightly clasped on her legs, only serve to further accuentuate her chest."

    "Her slightly blushing face, delicate and reserved in its lust, is framed by the bangs of her yellow, whispy hair."

    "I lean forward, gently taking her soft, bare shoulders in my hands."

    "As I do, she brings one hand from her lap to the side of my face, taking my cheek in her palm."

    "With a slightly uneven breath, we lean in, our tongues entering each other's mouths as our lips lock."

    "As I feel Lilly's hand gently slide up to my shoulder, her head suddenly moves forwards with a surprising amount of force."

    hi "Woah!"

    show lilly behind_smile_nak
    with charachange
    
    "Our mouths separate as I fall onto my back, Lilly's body following mine."

    "My breath catches as her face hangs above me, her deep blue eyes almost swallowing me in."

    hi "Lilly…"

    "As my arms stay awkwardly pointed upwards, she moves her body backwards, her head lowering to my chest."

    "My entire body tenses as her hands slide onto it, her lips kissing its center."

    "My mind races as my breath accelerates."

    "She's amazingly forward, more bold than I'd have ever guessed her to be."

    hi "Ah, L—Lilly…"

    li "…?"

    show lilly behind_pout_nak # fixme! [str]
    with charachange
    
    "She pauses and lifts her head slightly"

    "As she does, I completely forget why I was going to object."

    hi "I—It's okay. It's just… you're going faster than I expected."

    show lilly behind_smileclosed_nak
    with charachange
    
    "She gives a small smile as she lowers her head, pecking my lower chest."

    "Lifting her face once again, she slowly moves her hands downwards, her breath catching as she brushes the side of my lower hair"

    "She gently moves her hand sideways, delicately touching the most honest part of my body."

    li "Th… this is…"

    hi "Y—yeah."

    "She gently pats up and down it, as lightly as if it would break if breathed upon."

    "The mere fact that it's being touched by her is surprisingly erotic."

    "My body relaxes as hers seems to tense."

    show lilly behind_weaksmile_nak
    with charachange
    
    li "Do you mind… if I…"

    "I wait for a second the last of the sentence, but none is forthcoming."

    "She may be trying to take the lead, but she's still incredibly nervous."

    "I can't help but smile as I reach forward and put my hand on her hair, reassuring her."

    hi "It's okay."

    "She pauses a moment before giving a small nod, shifting her legs over mine and righting her body."

    # Event CG
    show evh lilly_cowgirl_smile
    with whiteout

    "She gently brings both hands under my shaft, cupping it before lowering her body from the knees."

    "I can only look on frozen as she slowly and delicately rests her reddened lips over it."

    "As she does, I reach up to her plump, snow-white breasts."

    "Gently giving way under my hand, I delicately knead them, her dark pink nipples noticably hardened."

    "She slowly begins to move her hips back and forth, the softness of her lips enveloping my conciousness."

    "Compared to my ragged breaths of excitement, Lilly's are slow and deep, seemingly savouring the feeling."

    "The entire experience is incredible."

    hi "Lilly… that feels… good."

    "She silently nods. Judging by her intense face, she's just as taken as I by the experience."

    "It doesn't take long for said experience to start coming to a head, though, for both of us."

    "Both our juices are now flowing, the insides of her thighs noticably wettened."

    hi "I can't… hold it… much more…"

    "As she stops moving her hips, I move my hands down to the top of her thights."

    "She takes a deep breath to collect herself, opening her deep blue eyes, her face pointed downward."

    li "I'm going… to put it in now."

    hi "Ah, o—okay."

    "It's the only answer I can muster, my breathing ragged as I remain close to climax."

    "She moves her hands to the base of the hardened shaft, lifting her body and ever-so-slowly lowering herself upon it."

    "After a brief pause as the head touches the wettened entrance, she slowly lowers herself."

    # Event CG
    show evh lilly_cowgirl_cry
    with charachange

    "Her entire body tenses as it enters, her face obviously one of stifled pain."

    "Even as I see it though, I can't help but savour the soft, warm feeling enveloping my shaft."

    "As the last vestiges of it all but disappear inside her, she tenses incredibly, her nails slightly scraping into my chest."

    li "Ah… Ahhhh… Haaaahhh…"

    "She moans in pain, its level it too much for her to stifle completely."

    "As I open my mouth to reassure her, I see the dark red blood trickling from between her legs."

    hi "Lilly, if it's too much, you don't have to…"

    "She clenches her mouth tightly, shaking her head side to side."

    "After a couple of seconds, she relaxes her body slightly, still obviously in pain."

    li "I… It's okay… I'm okay."

    "She swallows deeply, trying to collect herself."

    li "I'm… going to move now."

    hi "Ah, mm."

    "She lifts herself slowly, the mixture of our juices and the warm, red blood becoming visible."

    "As she brings herself back down, she relaxes slightly more, the feelings of pleasure slowly overtaking those of pain."

    "Her breathing starts to match the ragged patterns as mine, her body slowly but surely moving up and down."

    "I move my hands up to her arms, sliding them down and taking her hands in mine."

    # Event CG
    show evh lilly_cowgirl_strain
    with charachange
    
    hi "Lilly… it's… good… Haaaa."

    "She gulps before replying, squeezing her hands around mine."

    li "Hisao…"

    "She gives a soft moan of pleasure, her pace picking up."

    li "Hisao… Hisao!"

    "I start to squeeze her hands back, slowly losing the ability to tether my excitement."

    hi "I'm… I'm going… to come…"

    "She keeps on moving, her face becoming more intense."

    hi "Lilly… I'm…. I'm…"

    "I grit my teeth, moaning in ecstacy as I try to hold back."

    hi "Lilly… Ah—AAAAH!"

    li "Ah… Aaaah… AAAAAAAAAH!!"

    # Event CG
    show evh lilly_cowgirl_weaksmile
    with charachange

    "My mouth and eyes fly open as my entire body tenses, my hips hitting hers as I orgasm."

    "Her back arches back instantaneously, her breasts following her chest upwards."

    "We stay locked in all-encompassing ecstasy for a brief moment, both of us enraptured."

    scene bg hok_lounge_ni
    with whiteout
    
    "As it ends all too soon, our bodies collapse in exhaustion, with Lilly all but falling on top of me."

    "I wrap my arms around her loose, sweating body, the tiny droplets like dew on her soft, white skin."

    "For minutes we lay there, silently savouring each other's contact as we recover from the experience."

    "I look sideways to her tired face, the effort almost forcing her to the verge of collapse."

    hi "I love you, Lilly."

    "She nods weakly, rubbing my hair with her right hand."

    "A soft kiss on my forehead is the only answer."
    stop music fadeout 3.0 # [str]
    scene black
    with dissolve

    return

label en_L27:

    scene bg hok_lounge_rn 
    with locationchange

    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')
    play ambient sfx_rain fadein 1.0

    "Once again, I wake up in that familiar couch and remain all but immobile once doing so."

    "I feel awful."

    "As I let my arm hand down the side of the couch, I lackadaisically stare up at the ceiling."

    "Just what the hell did I do last…"

    "…"

    "…Ah."

    "As the images of last night fill my mind, I try to sort through them."

    "Rather unsuccessfully, I might add."

    "My mind seems to fold in on itself as I try to comprehend everything that's happened, the events of yesterday reduced to a blur of emotions."

    "Giving up on the futility of the task, I sit myself up and stare at the curtains blocking the window."

    "The morning light shining through them is broken by the streams of water trickling down from the rain."

    "A pity. This'll be the last day of our trip before we have to return to school."

    "I guess everyone around here waiting to go to the beach for Marine Day's going to be disappointed, too."

    "Running a hand through my hair, I walk over to my travel bag pushed up against the end of the couch and rummage through one of the pockets."

    "Within the minute, there's a small pile of packets and bottles on the floor next to it, all manner of exotic and nonsensical names on their outsides."

    $ renpy.music.set_volume(0.10000000000000001, 1.0, channel='ambient')

    window hide
    nvl show dissolve

    nvl clear

    n "I slap them one-by-one into my mouth, not bothering to get a drink to wash them down."

    n "After over a month of having to take them, I eventually ended up just downing them as quickly as possible."

    n "It's not hard to get used to dry-swallowing pills after a while."

    n "Just like getting used to living in a school full of disabled students, I suppose."
    
    $ renpy.music.set_volume(0.20000000000000001, 1.0, channel='ambient')

    nvl clear
    nvl hide dissolve

    window show

    ha "Good morning, Hisao."
    
    show hanagown smile_rn at center
    with charaenter

    hi "Ah, Go—Gack!"
    
    $ renpy.music.set_volume(0.0, 0.20000000000000001, channel='ambient')

    with vpunch

    "As I reply to her, I completely forget I'm in the middle of swallowing a particularly large pill, violently gagging on it."

    show hanagown worry_rn at center
    with charachange
    
    ha "Ah, Hisao!"

    "After spluttering loudly and tapping my chest a couple of times to force it down, I manage to right myself."

    hi "I'm fine. Sorry, forgot I was swallowing."
    
    play music music_happiness fadein 5.0

    show hanagown distant_rn 
    with charachange

    ha "Sorry, Hisao. I—" #reminder for the potential {nw} break

    "I hold my hand up, gesturing for her to stop."

    hi "I gagged. It's my fault. 'morning, Hanako."

    "She pauses a moment before bowing in reply."
    
    show hanagown distant_rn at tworight 
    show bg hok_lounge_rn at bgright 
    with charamove
    
    show lilly basic_sleepy_paj_rn at twoleft 
    with charaenter

    "Walking, no, staggering in behind Hanako is the familiar figure of Lilly, still dressed in her pajamas."

    "With her hair poorly tied back and her face reeking of tiredness, she looks about as awful as I do."

    li "Hello, Hisao."
    
    show lilly basic_weaksmile_paj_rn at twoleft 
    with charaenter

    "Her voice matches her looks perfectly, not a hint of energy or thought behind them."

    hi "You look awful."

    show lilly basic_pout_paj_rn at twoleft
    with charachange
    
    li "Hisao~"

    hi "Don't worry, I do too."

    hi "You look bright and chipper at least, Hanako."
    
    show hanagown emb_rn at tworight
    with charachange

    ha "Ah… mm."

    "She's being evasive. More evasive than usual, at least."

    "As I rub my tired eyes, I can't help but remember back to yesterday."

    hi "Hanako… um…"

    "I shake my head, trying to organise my thoughts."

    "I may feel like a hammer's been taken to my stamina, but I want to get this out of the way."

    "The last thing I need is Hanako misunderstanding something, and she deserves to know in any case."

    hi "Lilly… and I…"
    
    stop ambient fadeout 25.0

    "As I trail off, Lilly guides herself along the wall beside Hanako and I, delicately taking a pinch of the cuff of my pajamas in her hand."
    
    show lilly basic_listen_paj_rn at tworight
    with charachange

    "This is a lot more awkward than I thought it would be."
    
    show hanagown distant_blush_rn at twoleft           
    with charachange

    "Before I can say another word though, she smiles and shakes her head."
    
    show hanagown smile_rn at twoleft
    with charachange

    ha "I know."

    hi "You… know?"

    li "Hanako?"

    ha "About you and Lilly."
    
    play music music_serene fadein 6.0

    "She closes her eyes, giving the widest smile I've ever seen on her face."

    "It suits her."

    ha "I'm happy."

    ha "I'm really, really happy."

    "I feel as if the weight of the world's been lifted off my shoulders. Lilly and I move forward to her in unison, wrapping our arms around her in one big hug."

    show lilly basic_smile_paj_rn at tworight
    li "Thank you, Hanako."

    hi "Yeah, thanks."

    "The chaotic events of the morning are all but forgotten, this precious moment etching itelf on my memory. On all our memories"

    "We slowly part after minutes of tightly holding each other."

    "As her emotion starts to die down, she lowers her face, a small smile still firmly held on it."

    ha "I love you, Lilly, Hisao."

    "We both nod in reply, a small silence taking over."

    li "When did you know, Hanako?"
    
    show hanagown distant_blush_rn at twoleft
    with charachange

    ha "I saw that you two… fit together."

    ha "I might look like this, but I realised it."

    hi "It?"

    ha "What Lilly was trying to do."
    
    show hanagown worry_blush at twoleft
    with charachange

    "As Lilly lowers her head, Hanako quickly moves to allay her shame."

    ha "No, no, I didn't mind it!"
    
    show hanagown smile_rn at twoleft
    with charachange

    ha "But… it made me happy. That you were doing that for me."

    ha "Which is why I'm even happier now."

    "I take the back of my hair in my hand, scratching it in slight embarassment."

    hi "Was it… that obvious?"
    
    show hanagown distant_blush_rn at twoleft
    with charachange

    "She averts her face, blushing slightly."

    ha "Well… there was… that… too."

    "As I cock my head sideways, she glances to me and flicks her face back in embarassment."
    
    show hanagown worry at twoleft

    ha "You were… loud. Last night."

    hi "Lou…"

    "My breath catches as my mind recreates the Hindenburg disaster in graphic detail."

    hi "Y—y—y—you…?"

    "She gives an almost imperceptible nod."

    "As I struggle to do so much as force a single word out, I suddenly hear Lilly burst out beside me."
    
    show lilly basic_giggle_paj at tworight
    with charachange
    

    li "Pfft…"

    li "Hahahahahaha!"
    
    show hanagown smile at twoleft
    with charachange

    "She's… laughing."

    "Not giggling in that trademark constrained and refined way, but laughing. Honest to God, laughing."

    "It's the first time I've ever seen her so carefree, and as the situation replays itself in my head, I can't help but join her."

    hi "Bwuahahahaha!"

    li "Hahaha! Hahaha!"

    "I can hardly control myself at all, covering my face with my hand and doubling over in laughter."

    hi "Hahahaha! Oh god, hahahaha!"

    li "Hahaha, hahahaha!"

    "As Hanako looks on, completely lost as to what to do, even she can't help but giggle as we laugh like unrestrained madmen."

    "We eventually manage to calm ourselves, the occasional giggle slipping through as we breath out the last of our gaiety."

    hi "I'm just going to… go wash my face."

    "I wave my hand in the direction I intend to go as I struggle to get the words out, my ribs in significant pain from the laughter."

    scene bg hok_bath
    with locationchange

    "As I splash water from the running tap onto my face, I pause, looking at my reflection."

    "Lilly confessed to me, and I confessed back."

    "I lost my virginity… though it might be more correct to say that I had it taken from me."

    "Hanako accepted that Lilly and I love each other."

    hi "Lilly and I love each other."

    "A smile spreads over my lips as I say that beautiful sentence."

    "It's so simple, yet so grand."

    "And now I'm grinning like an idiot."

    "I guess, in a way, it doesn't change that much."

    "I'm still attending Yamaku, and everyone is still the same person."

    "Hanako, Emi, Rin, Yuuko, Shizune, Misha, Akira, and… Lilly."

    "Even the name itself takes on a new significance."

    "I jump back and throw a few playful punches forwards through the air."

    "No. Things won't be the same."

    "Even if they don't change now, I'll change them."

    "Because this is the first day of my future."

    "My future with Lilly."

    scene black
    with dissolve

    return

label en_L28:

    # BG, summer house bathroom
    scene black with fade
    scene bg hok_bath
    with shorttimeskip

    "As I relax in the deep, hot bath, my mind drifts like the mist hanging in the room."

    "Thanks to the rain, the afternoon was an unendingly boring affair."

    "While slumped lazily in the couch watching television, Lilly sat beside me reading as Hanako idly poked a teru teru bozu doll she made after lunch."

    # http://en.wikipedia.org/wiki/Teru_teru_bozu

    "It may not have been the most exciting finale to the trip, but the quiet peacefulness is something to savour."

    "Even after we return to the school tomorrow, I think I'll remember this little house in Hokkaido for a long time."

    "I lean back in the bath, the hot water flowing up to my chin."

    "It's been so long since I've had a good, deep bath. I wish I could stay in here forever."

    "It's a pity we only have a couple more hours to spend here before getting the train back."

    "All I can do is yawn as I absentmindedly watch the steam slowly rising."

    centered "*tap* *tap* *tap*"

    "As I hear the series of raps on the door, I pick myself up and sit upright."

    hi "I'm in here, I'll be out in a sec."

    li "May I come in?"

    "The unmistakable voice coming from the other side of the door freezes me."

    "After a second's thought, I rest on the side of the bath and let my arms dangle over the side."

    hi "Sure, come in."

    "With that, she opens the door, slowly walking into the room and closing it behind her."

    "She looks oddly calm, countering my racing heart."

    hi "Ah… h—hey, Lilly."

    li "Do you mind if I take a bath with you?"

    hi "Ah, sure. Go ahead."

    "With a small nod she begins to unfasten her shirt, button by button."

    hi "I could do that for you, if you'd like."

    li "Refused."

    "She says the word surprisingly forcefully."

    hi "Why?"

    li "If you do it, one thing will lead to another."

    hi "…I guess you have a point."

    "She continues undressing, her shirt and skirt falling to the floor leaving her in her bra and panties."

    "Compared to last time, it's a lot easier to survey her entire figure."

    "Those long, shapely legs, her well-defined hips, that large bust."

    li "Hisao?"

    hi "Hmm?"

    li "You're thinking perverted thoughts, aren't you?"

    hi "You're undressing in front of me, give me a break."

    "She furrows her brow in absentminded thought."

    li "I guess this would be somewhat more erotic for you than me."

    hi "Why?"

    hi "…Ah."

    "That took disturbingly long to click. Regardless, she gives a small, lighthearted chuckle."

    li "If this is too much for you, Hisao, I can come back later."

    hi "No, no, this is fine. A guy can't pass up seeing a bared lady, after all."

    hi "And besides, you're stunningly beautiful."

    "The earnest comment draws a vivid red blush from Lilly as she brings her hand to her cheek."

    li "Hisao…"

    "I give a small grin."

    hi "You're cute when you're taken off guard."

    "With a small huff, she unhooks her bra and slides down the last of her underwear."

    return


label en_L28h:
    
    "The small tuft of blonde hair and her uncovered breasts draw an honest reaction from my body."

    "Damn tostesterone."

    "With a final small tug, she looses her ribbon, her hair falling down past her shoulders."

    "As her hair falls, by breath catches."

    "With her wavy, blonde hair hanging freely unlike I've ever seen it before, it's amazingly beautiful."

    li "May I come in?"

    hi "Ah, sure."

    "I lean forwards and take her hand in mine, drawing her over the the side of the bath."

    "As she feels out the side of it, she gently lowers herself in, my breath catching as she sits and leans her back onto my front, her legs inside mine."

    # Event CG

    "Letting out a long breath to calm myself, I rest my arms on the sides of the bath."

    "Despite far from missing the sight of her gratuitous assets, the feeling of her body against mine is surprisingly relaxing."

    "Even the sweet smell of her hair is intoxicating."

    li "So nice~"

    hi "You like hot baths?"

    li "Mm, I usually run them quite hot."

    "I sit idly watching the wall ahead of me and the steam rising, every now and again stealing a glimpse at her wiping her legs."

    "The white of her skin glistens as she runs her hand over them, their length and tone all the more obvious."

    hi "You know, compared to Akira, you look a lot more foreign."

    li "I took after my mother's side, genetically. Akira took after my father's."

    hi "So that would make your mother South African and your father…"

    li "Japanese. He met my mother on a business trip."

    hi "Ah, I see. Surprising neither of you have accents."

    hi "Well, aside from Akira's dialect."

    "She gives a small giggle before continuing, apparently amused by her sister's odd habit."

    li "We were born in Japan. It was only when I was seven that they moved to South Africa."

    hi "And you were left here?"

    li "In the boarding school, to be precise."

    "I guess that's why she became the was she is."

    "Motherly and confident, all because she had no family there to support her. She took on the role that had been denied to her."

    "Giving in to temptation, I take my arms from the sides of the bath and bring them around her stomach, tightly hugging her."

    "As soon as I do so, her body reflexively tenses."

    # Event CG

    li "Ah, H—Hisao!"

    hi "I can't help it, you're just so cu~te."

    "She relaxes back into me once more, resting the side of her head against mine."

    "We sit for minutes on end, resting against each other."

    "The feeling of our bodies against each other, sharing our warmth, is wonderful."

    hi "Hey, Lilly?"

    li "Mm?"

    hi "How was it? Last night, that is."

    "She pauses in thought."

    li "Hmm, I'd be lying if I said it didn't hurt."

    li "But… it was nice."

    li "Was it good for you too, Hisao?"

    hi "Mm. It was good."

    "I peck her affectionately on the shoulder, her head nestling beside mine."

    "Even as I do though, I can't help but let my gaze linger between her legs."

    li "Hisao, your heart's beating."

    "I give a small, devilish grin, slowly moving my right hand downwards from her stomach."

    li "Hi… Hisao?"

    "As my fingers start to brush through her light, whispy hair, her body tenses in realisation."

    li "Hisao!"

    hi "Shhh, Hanako might hear."

    li "But, Hisao!"

    hi "You took the lead last time, it's my turn now."

    "I gently lower my hand between her legs, my middle finger slipping between the soft folds."

    # Event CG

    "With a fractured breath, I move my legs over and between hers, locking them to the edges of the bathtub."

    "With a kiss to her bare shoulder, I start to move my finger up and down, savouring the softness as the skin under it gives way."

    li "Hisao, please…"

    "Even as she says it, her breathing becomes noticably deeper."

    "Eventually her hands come over mine, guiding it up and down as I move to massage her right breast."

    "All signs of reluctance give way as I continue gently rubbing."

    "I wonder if…"

    "With a kiss to her neck, I move my mouth to her ear, ever-so-slowly bring my teeth to her earlobe."

    li "Kyaaah!"

    "Her body tenses momentarily in surprise, her breath accelerating. So, she's sensitive here."

    "I open another front in my assult on her senses, carefully rubbing my teeth back and forth on her ear."

    "The feeling of her earlobe's quite nice, all soft and squishy."

    "It only takes a few minutes before her body starts to squirm ever so slightly, unable to stifle her quiet moaning any more."

    "It looks like she's getting close…"

    "Heeding her calls, I relax my hands and return them to their place around her stomach."

    li "Shall we do it, again?"

    "Her voice is punctuated by shallow, lustful breaths."

    hi "Mmm."

    "Still tense from the excitement, she maneuvers herself out of the bath as I do, retaining her hold on the side."

    "I take my place behind her, knees on the ground."

    # Event CG

    "The nape of her neck and exposed shoulderblades are so tempting that I can't help but run my hand over her back, her body flinching slightly."

    li "Hisao…"

    hi "I'm… putting it in now."

    "She gives a weak nod, gulping down her lust."

    "Even now she must still be on the verge of her climax."

    "Looking down, I take a moment to position myself before leaning my hips forward, slowly and gently entering her."

    "While her grip on the side of the bath tightens, it seems to be hurting much less than last time."

    # Event CG

    "As I slowly start to rock back and forth, I realise just how much pleasuring her's excited me."

    hi "Lilly, I can't… go much longer…"

    "She gives no answer. With her face lowered, her entire mind is taken by the pleasure sweeping over her."

    "It doesn't take long before she's moving just as much as I am, her shoulderblades petruding as her back arches in pleasure."

    "As my breaths become more and more ragged, I rapidly feel my limit approaching."

    hi "Lilly, ah… ah…"

    li "Ah…. aaah…"

    li "Ha, ha, ha, HAAAAAAH!"

    "A series of exhasperated breaths is the only warning before her final moan of ectasy, her entire body tensing incredibly."

    "As the insides of her feel as if they're sucking me in, I can't hold back any longer."

    hi "Lilly… LILLY!"

    # Event CG

    "My hips hit hers, both of us frozen against each other in simultaneous orgasm."

    "In precious seconds, it's all but over, Lilly slumping downward as I collapse on top of her."

    "Taking a moment to catch our breaths, I hold her left hand tightly."

    hi "That was… good."

    "She takes a gulp of air before replying, steadying herself as she nods."

    li "Mmm."

    "She turns her head and gives a small kiss on my cheek, nestled beside hers."

    scene black
    with dissolve

    return

label en_L28x:

    # Timeskip from previous sentence
    # Open to modified CG from L23
    # Hanako sleeping on Lilly's lap, night-time scenery outside window, Hisao resting his head in his hand
    # Same SFX, if one is used, as L23 as well

    # Event CG

    scene lilly_trainride_ni

    "Train 43. The last passenger train running today."

    "After a chaotic dash to the station, we promptly crashed once finding out seats in the otherwise deserted carriage."

    "With Hanako fast asleep on Lilly's lap, I can barely muster the energy to stay awake."

    "I'd probably be pretty depressed about going back to school if my brain were actually working."

    "As it is, though, the sight of the night-time scenery scrolling by is surprisingly beautiful, and something I hadn't noticed on the way in."

    "A loud yawn is the only sound heard other than the rattling of the traintracks."

    hi "So tired…"

    li "And who's fault is that, Hisao?"

    "I grimace."

    "From the tone of her voice, she's pissed."

    "As I move my eyes sideways to look at her though, she wears a mischeivous grin."

    "She really does toe the line between insulting and amusing."

    "I give a snort and look back out the window, my reflection just visible on the clear pane."

    "Truth be told, she's perfectly correct."

    "If it weren't for the little interlude of a couple of hours ago, we'd have a lot more energy."

    hi "Yeah, yeah, it was mine. Still, getting into a bath with a guy is a dangerous thing to do."

    li "Evidently."

    hi "Sorry, I guess I kind of took advantage of the situation back there."

    li "Well…"

    "As she trails off, I look back to her."

    "My eyes narrow as I see her slightly reddened cheeks and furrowed brow."

    hi "Say it."

    li "I… knew the possibility of it happening… was there."

    hi "I knew it. You're just as perverted as I am."

    "She quickly coughs into her hand, making her disapproval crystal clear."

    li "That's a rather crude way of putting it."

    hi "Oh? And you would suggest?"

    li "I merely have a functioning adolescent sex drive."

    hi "So in other words, perverted."

    "Almost seeming to sense the moment, Hanako mumbles quietly as she furrows her head in Lilly's lap."

    "Her look of disapproval all but melts as she gently smiles and strokes her hand on Hanako's long, dark hair."

    "All I can do is watch."

    "Watch, that is, and smile."

    "If someone were to ask me when I fell in love with her, I wouldn't be able to answer."

    "The best I'd be able to come up with is “it just happened at some point, but I didn't realise it.”"

    "If someone were to ask me why I love her, though, then I could answer easily."

    hi "You really love Hanako, don't you?"

    "She gives a deep nod, smiling warmly."

    li "It's a pity we have to return to school."

    hi "Well, There's only three weeks left of it. We could come back here during the summer holidays."

    li "Mm, that'd be good."

    "I nod approvingly."

    "Summer, together with Lilly."

    "Yeah, that sounds good."

    scene black
    with dissolve

    return

label en_L29:

    scene bg school_hallway3
    with shorttimeskip
    
    "Today has been a day of highly unusual happenings."

    "Unusually, I got up slightly before the alarm blared at me."

    "Unusually, I didn't have a nightmare, nor have trouble sleeping."

    "Unusually, I felt awake and alert as soon as I got out of bed."

    "And to top it off, I managed to make it into class early despite only reaching the dorms late into the night."

    show bg school_scienceroom at bgleft
    with locationchange
    
    $ renpy.music.set_volume(0.5, 1.0, channel='music')
    play music music_normal fadein 1.0

    "As I stride into the classroom feeling on top of top of the world, Shizune and Misha stand discussing near the front of the room."

    show misha sign_smile at left
    with charaenter
    
    show shizu basic_normal at twoleft
    with charaenter
    
    "As soon as Misha sees me, though, she breaks off from signing to-and-fro and beckons me over."

    mi "Hicchan~!"
    
    show misha hips_grin at twoleft
    show shizu basic_normal2 at tworight
    show bg school_scienceroom at center
    with charamove

    "A quickly jog over, pleased to note the lack of cold analysis behind Shizune's eyes or mischievous grin on Misha's face."

    "It looks like, for once, that I'm not going to be interrogated or asked to do another menial task."

    hi "Hey Misha, Shizune."
    
    show misha hips_smile at twoleft
    with charachange
    
    show shizu behind_blank at tworight
    with charachange

    "I give a curt nod to Shizune, to which she nods back."

    mi "You look happy today, Hicchan."

    hi "Really?"

    mi "Usually you look like this in the morning:"
    
    show misha perky_sad at twoleft
    with charachange
    
    show shizu behind_smile at tworight
    with charachange

    "She brings her hands to her face and drags her cheeks downwards, tilting her head slightly."
    
    show misha perky_confused at twoleft
    with charachange

    mi "“I am Hisao. I am not in the mood for your jokes. I am feeling very, very booooring.”"

    hi "You flatter me."
    
    show misha sign_smile at twoleft
    with charachange
    
    show shizu adjust_happy at tworight
    with charachange

    "She withdraws her hands and pats me on the shoulder, grinning."

    mi "This look suits you, Hicchan!"

    "As I look sideways, I see even Shizune smiling, seemingly echoing her comrade's sentiments."

    "Slightly embarassed, I quickly move to change the subject."

    hi "So, what'd you two get up to on the long weekend?"
    
    show misha hips_grin at twoleft
    with charachange
    
    show shizu basic_happy at tworight
    with charachange

    mi "Shopping, shopping, we went shopping~"

    hi "Shopping, huh? Have fun?"
    
    show misha sign_smile at twoleft
    with charachange
    
    show shizu behind_blank at tworight
    with charachange

    mi "Of course!"

    "Approaching this with a male's mind, I can't really see the enjoyment in spending a holiday doing, of all things, shopping."

    "I guess it's just a girl thing."

    "I make a mental note to follow this mystery of life up sometime with Lilly, as I have a feeling raising the subject with Misha would only bring teasing."

    show misha cross_smile at twoleft
    with charachange
    
    mi "So, Hisao?"

    hi "So… what?"
    
    show misha cross_grin at twoleft
    with charachange
    
    show shizu adjust_happy at tworight
    with charachange 

    mi "What did you do for the holiday, silly!"

    hi "Oh. I went to Lilly's summer house with her and Hanako."
    
    show misha perky_smile_close at twoleft
    show shizu behind_blank_close at tworight
    with charachange

    mi "Two girls and one little boy out in the country, how scandalous~"

    hi "Now don't get the wrong ide— {w=.25}{nw}"

    "Wait, she's actually perfectly right."

    "And it was not only once, but twice."

    show misha cross_smile_close at twoleft
    with charachange

    "Why is she…?"

    "Oh no."

    "Why did I pause?"

    "Why did I have to pause?"

    "And on top of that, I can feel my cheeks blushing like mad."

    "You idiot, Hisao. You idiot, you idiot, you idiot."

    "I hide my face in my hand, stealing a glance at Shizune."

    "She's staring daggers at me. If not for her slight blushing I'd be running scared from the room."

    hi "Please forget what I said. I beg of you."

    "Misha raps me on the shoulder, harder than before."
    
    show misha cross_frown_close at twoleft #hips_frown_close
    with charachange
    
    show shizu behind_blank_close at tworight
    with charachange

    mi "It's only natural for a boy your age! So? So?"

    hi "So…?"

    mi "Who was it? Who was it?"

    "I look at her flatly."

    "She's practically bouncing up and down like a dog eagerly awaiting it's meal."

    "Every fiber of my being is screaming at me not to tell her. That said, though, she'll find out eventually."

    "Gossip spreads fast, and the student council would have their ears to the ground."

    "Bah."

    "I grin madly and point my finger in the air teasingly."

    hi "Not telling."
    
    show misha hips_frown_close at twoleft
    with charachange
    
    show shizu behind_frown_close at tworight
    with charachange

    mi "Whaaaaat?"

    hi "You'll find out eventually."

    show misha perky_sad at twoleft
    with charachange
    
    show shizu behind_blank at tworight
    with charachange
    
    mi "But you could tell me now!"

    hi "But this is so much more fun."

    mi "You're mean, Hicchan."

    show misha cross_smile at twoleft
    with charachange
    
    show shizu behind_smile at tworight
    with charachange
    
    hi "Maybe I am."

    ha "Ah, Hisao."

    "Hearing a familiar voice ringing out behind me, I turn to see Hanako."
    
    show hanako invis at Position(xpos=1.1)
    
    #scene bg school_scienceroom at left
    
    show misha cross_smile at left
    show shizu behind_smile at twocenteroff
    show bg school_scienceroom at bgleft
    show hanako basic_smile at tworight#rightedge    
    with dissolvecharamove

    "Surprisingly, she looks just as chipper as I do."

    hi "Hey Hanako. You remember to pack lunch today?"

    ha "Mm. Cheese sandwhiches."

    "How… plain. Regardless, she seems to be quite happy about them."

    hi "Want to eat on the roof?"
    
    show hanako basic_normal at tworight 
    with charachange

    ha "Lilly was going to ask you to."

    hi "Well, I guess that's settled then."
    
    hide hanako
    with charaexit
    
    "With a quick nod to Misha and Shizune, she walks to her desk and hooks her bag on the side."

    "As I turn back to Misha, she stares at me while rubbing her chin."
    
    show misha hips_grin at twoleft
    show shizu behind_blank at tworight
    show bg school_scienceroom at center
    with dissolvecharamove

    mi "She's in a very good mood, wouldn't you say, Hicchan?"

    hi "No comment."

    show misha sign_smile at twoleft
    with charachange
    
    mi "Tsch."

    "She snaps her fingers in frustration at her failed attempt to prize any small morsel more information from me."

    "As she does, I can't help but notice Shizune's distinct silence during the proceedings."

    "Well, silence would be expected, but nary a thing can be read from her face."

    hi "What's Shizune's take on this?"
    
    show misha sign_sad at twoleft
    with charachange
    
    show shizu behind_frown at tworight
    with charachange

    mi "Ah…"

    "She reluctantly begins to sign to her bespectacled company."

    "From the way she's acting, it seems as if she didn't want to ask rather than forgetting to."

    "After a quick sign to and fro, Shizune gives a curt nod and walks off to her desk."
    
    hide shizu
    with charaexit
    
    #show misha sign_sad at twoleft
    #with charamove

    hi "Did I… say something wrong?"

    mi "No, no, you didn't do anything wrong."

    mi "Shizune says:"

    "She clears her throat and proceeds in a deeper, faux-businesslike tone."

    mi "It is none of my business who you date or go out with. Nevertheless, I am pleased you have found someone you like."

    "I raise an eyebrow, as much at Misha's antics as Shizune's apparent coldness."

    hi "How… professional."
    
    show misha perky_smile at twoleft
    with charachange
    
    "She gives a weak smile, as if apologising for her friend."

    mi "Shizune and those two… don't get along well."

    hi "Why?"

    mi "Well, Shizune's set in her ways. If she decides she doesn't like someone, she takes a long time change her opinion of them."

    hi "I can't say I'm surprised. That doesn't answer my question, though."

    mi "That's really something you should ask her or Lilly."

    hi "Yeah, you have a point. Thanks, Misha."
    
    hide misha
    with charaexit
    
    "As Mutou strides into the classroom behind me, the class takes their seats and an obedient silence falls over the room."

    "While he's far from the strictest teacher in the school, he's certainly a lot more jovial when obeyed."

    "As he begins to scrawl equations for exam revision on the board, I idly chew on a fingernail."

    "Every time I feel like I'm getting used to the school and the people in it, I'm thrown a curveball."

    "So, Shizune dislikes Lilly and Hanako."

    "I guess her stubborn personality could lead to friction like that, and Hanako's shyness can be frustrating at times. From the way Misha phrased it though, it seems as if it goes both ways."

    "I guess it's only human not to get along with everybody."

    scene bg school_roof
    with shorttimeskip

    "As I open the door to the rooftop, Hanako by my side, I quickly blink to overcome the dazzling brightness of the sun."

    show lilly basic_smileclosed at leftsit
    show rin basic_awayabsent at rightsit
    show emi basic_grin at centersit
    with charaenter
    
    "Ahead of us sit Lilly, Emi and Rin, jovially chatting amongst themselves."

    "As Rin casually scoops up her food with a fork held in her toes as Emi chews into an apple."

    "I guess their questioning will have to be fronted as well."

    hi "Hey guys."

    show lilly basic_surprised at leftsit
    show rin relaxed_surprised at rightsit
    show emi basic_confused at centersit
    with charachange
    
    "The three all stop eating in unison, looking curiously towards us."
    
    show emi excited_laugh at centersit
    with charachange
    
    emi "Ah, Hiffao!"

    hi "Swallow, then speak."
    
    show emi excited_happy at centersit
    with charachange
    
    "She tilts up her head and swallows the piece of apple in her mouth without bothering to chew the rest."
    
    show emi excited_joy at centersit
    with charachange
    
    emi "Hey, Hisao, hey Hanako."
    
    # complications...meh. [str]
    
    show lilly invis at Position(xpos=0.05) #leftoff
    show rin invis at Position(xpos=0.05)
    show emi invis at Position(xpos=0.05)
    with dissolvecharamove
    
    show rin invis at Position(xpos=1.00) #rightendge
    show emi invis at Position(xpos=1.00)
    show hanako invis at Position(xpos=0.05, ypos=1.15) 
    with None
    
    # too bad _close sprites cant fit on screen [str]
    show lilly basic_smile at leftsit
    show hanako basic_smile at twoleftsit
    show emi basic_grin at tworightsit
    show rin basic_deadpannormal at rightsit
    with dissolvecharamove
    
    "With a polite wave from Hanako we walk over to the trio and drop our bags on the ground, fishing out our lunches."

    "As soon as I move my sandwhich to my mouth, Emi moves in for the kill."
    
    show emi basic_grin at tworightsit
    with charachange
    
    emi "So, Hisao, I hear you three had a trip the the country."

    hi "Yeah, it was great. What'd you two do?"
    
    show emi basic_grin at tworightsit
    with charachange
    
    emi "Don't dodge the question, Heart Sniper!"

    "I look at her incredulously."

    hi "Heart… Sniper?"

    "She takes a breath and begins to tell the tale as if it were a modern Illiad."
    
    show emi basic_grin at tworightsit
    with charachange
    
    emi "Oh, graced was he. Oh yes, graced."

    emi "Unknown to tales of woe, our intrepid man set out on a journey, the journey of his life."

    emi "But hark! Girls twice beckon!"

    emi "Torn between two fates, two destinies, two wills, two lives, he is thrown into despair!"

    emi "Oh fair hero, torn so cruelly in tween! Of which fair maiden do you profess your love?"

    hi "Translated?"

    "Her face falls flat."

    emi "Who'd you choose?"

    hi "Who said I chose anyone?"

    emi "Three days alone with two girls? I'm not that stupid."

    hi "Well…"

    play sound sfx_impact
    with vpunch
    #centered "*thud*"

    "Before I can react, Emi's outstretched arm slams down onto my head."

    hi "Ow, ow, ow."

    li "Ah, Hisao!"

    hi "I'm fine… mostly."

    emi "Hmph. Serves you right."

    "As I cradle my aching head in my hands, I look over to Rin."

    "With a look of distinct disinterest, she continues munching her food."

    hi "Hey, can't you call off your attack dog?"

    emi "What was that!?"

    rin "She is my attack cat, not my attack dog."

    emi "Huh?"

    hi "Cat?"

    rin "She is more catlike than doglike. Therefore, she is an attack cat."

    "Giving up on the prospect of aid from her ally, I turn to one of mine, reaching out to Lilly with wavering arms."

    hi "Help me Lilly, she's being mean to me~"

    li "There, there."

    "She reaches out with an outstretched hand, rubbing my head lightly after I move it slightly sideways to meet her palm."

    "Emi watches on, giving a frustrated sigh."

    emi "So, who was it?"

    hi "Why, that would be… Mmm!"

    "Before I can say another word, Lilly hand slides from my hair to my cheek as she forcefully takes my lips in a kiss."

    "My mouth uselessly hangs open as our lips stay connected for precious seconds, my mind blanked and heart racing."

    "As she breaks off, all I can do is sit in place, stunned, dazed and blushing furiously."

    emi "Woah! So bold!"

    rin "Uooh."

    "As I slowly collect myself, I notice Hanako staring and Rin, amazingly, having stopped eating."

    hi "W—well, uh… th—that's…."

    "Stammering in the throes of surprise, I jerk my head around to Lilly."

    "Her warm smile all but melts my embarassment, making me feel slightly silly for being so awkward."

    hi "Yeah. That's how it is."

    "I bring my arm around her shoulder, hugging her tightly."

    "The act draws an enthusiastic thumbs-up from Emi."

    emi "Good job!"

    li "Thank you, Emi."

    hi "Thanks."

    emi "This calls for a celebration!"

    "Lilly claps her hands together in delight at the suggestion."

    li "Excellent! Where shall we go?"

    emi "Er… hmm."

    "Her excitedness gives way to concentrated thought."

    "Minutes pass as we mentally raise suggestions and discard each in short measure."

    ha "Kara… oke?"

    "Hanako's tentative proposal breaks the silence."

    emi "Karaoke… not bad."

    "She looks over to Rin, who gives a lackadaisical nod."

    li "Karaoke would be nice. Hisao?"

    hi "Yeah, sounds like a plan. When'll we go?"

    li "Sometime on the weekend would probably be best…"

    emi "I have practice on Sunday, but I could do Saturday."

    rin "I'm fine with whenever."

    hi "Hanako?"

    ha "Saturday is okay."

    emi "Alright, Saturday it is!"

    "After a second's thought and a click of her fingers to clear her thoughts, she continues."

    emi "We'll meet downtown at five. Last one there has to buy a round of drinks for everyone!"

    hi "Good thinking, Hanako."

    li "This has turned out quite well."

    emi "Why yes it has, especially for Heart Sniper here."

    hi "You're still on that? Wait, why especially?"

    emi "Oh ho, slow today, aren't we Hisao? Think about who's coming."

    hi "Me, you, Lilly, Hanako and Rin, I suppose."

    emi "Exactly. How many guys get to go out with four girls at the same time?"

    hi "I only need one."

    "I place a gentle hand on Lilly's shoulder, smiling."

    li "Ah, th—thank you, Hisao."

    "She blushes wildly."

    "She really is cute when she's taken off guard."

    emi "Juliet, oh Juliet, come into my arms my one true love!"

    "With that, Rin falls into Emi's outstretched arms as she plays along with her theatrics."

    rin "Romeo, you have apple juice on your shirt."

    emi "Erk."

    "She levers off Rin and quickly moves to wipe her shirt with the cuff of her sleeve."

    hi "Oi, oi."

    "With a round of laughter, the rest of lunch carries on in the same lighthearted manner."

    "When I first came to Yamaku, I preferred solitude. I always had, really. Even as a child."

    "I guess it comes naturally when both parents are often working and you're an only child."

    "Now, though, I can't help but smile when surrounded by company."

    "Life is good."

    "I never thought I'd say it, especially after the heart attack, but it's true."

    "I smile and nod approvingly."

    "Yeah. Life is good."

    scene black
    with dissolve
    
    return

label en_L30:

    scene bg school_scienceroom
    with shorttimeskip
    
    "Yet another day amongst many."

    "Well, that's what I'd like to say it is."

    "To tell the truth, the atmosphere of the entire class, nay, school has changed."

    "While an undercurrent of subdued trepidation had pervaded the class, now that the exams are within eyeshot, it's boiled over into frantic studying of the like rarely seen otherwise."

    "Stuffing ourselves with food during lunch hasn't afforded anyone a measure of energy, it seems."

    "Even the bubbly, ever-energetic Misha seems oddly deflated, idly chewing a pen as Mutou orates from the front of the class."

    "…"

    "I do believe she's eating it, upon closer inspection."

    "Tearing my eyes from the maudlin spectacle, I quickly glance around the class."

    "Hanako sits frantically scribbling in her notebook with her face mere inches away from the page, seemingly trying to record every word that leaves Mutou's mouth."

    "Shizune's… well… Shizune."

    "Cool as a cucumber, she sits diligently takes notes with her attention focused wholly on the blackboard."

    "Truth be told, it's what I should be doing as well, if not for the fact that I've studied ahead to allow myself this moment of slackery."

    "My eyes lazily scroll back to Hanako, sitting in the last row on the window side of the classroom."

    "I can't help but simmer with envy."

    "Ah, what wouldn't I give for a view like—{w=.25}{nw}" #reminder for the potential {nw} break

    show muto irritated
    with charaenter
    
    mu "Nakai!"

    "Mutou's voice suddenly brings me out of my idle survey of the classroom."

    hi "Yes?"
    
    show muto smile #probably overusing sprites and should just use _smile all the time
    with charachange
    
    mu "The answer to question number fourty-two, which we just went over?"

    hi "The suffix for it would be -ane."
    
    show muto normal
    with charachange
    
    "His sly grin faulters, evidently having been hoping to catch me out."

    mu "Correct. Moving on, the suffix for…"

    hide muto
    with charaexit
    
    "As my attention towards Mutou falls away once again, I spot Misha giving me an enthusiastic thumbs-up."

    "I grin and nod gracefully, my role on the stage having come to an end."

    "Even Mutou's out of sorts. The exams really do have an insidious grip of the school."

    scene bg school_scienceroom
    with shorttimeskip

    "After the end-of-school bell rings and the class begins to file out, Mutou calls from the front of the class."
    
    show muto irritated
    with charaenter
    
    mu "Nakai, could I see you for a moment?"

    "I can only grimace, feeling the eyes of the rest of the class on me."

    "With a slight sigh, I gather myself and accepting my fate, striding up to the front."

    hi "Yes?"

    mu "I don't doubt your ability in this class, but do try to at least pretend to pay attention."

    "He has a point."

    hi "Ah, sorry."

    "As long as I nod and agree with him, it'll be fine."
    
    show muto normal
    with charachange
    
    mu "Well, no point lecturing you. All students do is nod and agree until the lecturing ends anyway."

    "Erk."

    "He's more insightful than most teachers, it seems."

    mu "That wasn't why I called you up though."

    hi "It isn't?"

    mu "Unless you wanted it to be, that is?"

    hi "No, that's fine."

    mu "Thought so."

    mu "Well, anyway, I was wondering what you intended to do once you leave here."

    "What I intend to do?"

    "I guess I never gave it any real thought."

    hi "I don't really know, to be honest. I guess something science-related would be good."

    "He gives a short chuckle, a suspiciously forced attempt to lighten the mood."

    mu "Well, I guess you're in the same boat as most. Take something you're good at and run with it, eh?"

    hi "Yeah, pretty much."

    mu "Thought about about going to university?"

    hi "If I want to get into science, I suppose I'll have to."

    mu "Right, right."

    "He pauses, thinking to himself."

    "Evidently coming to a satisfactory conclusion, his face lights up once more."
    
    show muto smile
    with charachange
    
    mu "I have it!"

    "It takes some measure of resistance to avoid saying “Have what?” as he dives into the briefcase propped up beside his desk."

    "As he rights himself after a quick rummage through the oversized briefcase, a thick, dark blue book is visible in his hand."

    hi "A Brief History of Time?"

    mu "Correct. I got that book when I was in university."

    mu "To be precise, after I'd blown out a couple of windows and was trying to work out what to do after I'd been kicked out of chemistry."

    "He gives a nervous laugh, realising that he'd perhaps said more than he meant to."

    "I can't say I'm overly surprised, though."
    
    show muto normal
    with charachange
    
    mu "Well, leaving that aside, it's good."

    mu "If you read it, we could discuss anything about it you want to."

    "He says “if,” but obviously means “when.”"

    "Though, I doubt he intended to make the distinction."

    "As I examine the cover, I absentmindedly read the text aloud."

    hi "From the big bang to black holes… Stephen Hawking."

    mu "That's what it's about. The guy's a role model, at least for me."

    mu "You know he was diagnosed with Motor Neurone Disease when he was in university?"

    "I nod silently, more as a token gesture of listening than agreement."

    mu "Yet he still went on to discover all these things, and teach people about them."

    mu "I think that's a great thing."

    mu "To not only discover something, but to help other people understand it."

    "I raise an eyebrow, something I'd been idly wondering having suddenly become surprisingly clear."

    hi "Is that why you're a teacher?"

    mu "Hmm?"

    hi "To not just discover things, but to teach others about them?"

    "He gives a genuine smile, nodding deeply."

    mu "Bingo."

    "He leans back on the shelf jutting out from the blackboard, in a manner quite unbecoming of a teacher."

    mu "Explosions, black holes, mysteries of the universe…"

    mu "I love learning about them, and trying to work stuff like that out."

    mu "But when it comes to telling other people about it, it's a different matter entirely."

    "As his voice starts to drift away, he leans forward and clips up his briefcase, taking it in his hand."

    mu "I just hope I can give you guys a bit of what I feel, I guess."

    mu "That wonderment about the universe."

    mu "Bah."

    mu "I guess I'm rambling. I have to be off, anyway."

    hi "Where?"

    "As soon as I say it, I suddenly wonder why I did."

    "Taken slightly off balance, he quickly collects himself and gives his trademark awkward grin."

    mu "The wife's relatives are coming over."

    hi "Ah. Good luck."

    mu "Thanks, I'll need it."

    mu "Oh, and read that book, Nakai. It's good."

    "And with that, he walks off."

    "I'd never understood Mutou, but now, I think I do."

    "I can't say I don't respect him a touch more."

    "With a stretch, as much from stiffness as an attempt to try and gather myself, I slide the book into my bag and leave the classroom."

    scene bg school_hallway3
    with locationchange

    "I'm not quite sure exactly where I go, once I enter the halls."

    "As I try to work out what to do, I casually walk around, every now and again sliding past groups of talking students in the corridors."

    "My legs are as active as my mind, I guess."

    "As I slide past two particular students, busily chatting between them, I pause."

    show miki basic_smile at twoleft
    show aoi neutral at tworight
    with charaenter
    
    hi "Hey Miki, Aoi."

    "They both give a polite nod."

    "I can't help but take a moment to savour the smell of perfume coming from Aoi before continuing."

    hi "How're you going for the exams?"
    
    show miki basic_serious at twoleft
    with charachange
    
    mk "Don't. Say. That. Word."

    hi "That bad, huh?"
    
    show aoi surprised at tworight
    with charachange
    
    "Aoi" "Ah!"
    
    show miki basic_surprised at twoleft
    with charachange
    
    "Both of us turn to meet her, an expression of sudden enlightenment on her face."

    "Aoi" "Hisao, do you mind if I ask you a question?"

    hi "Shoot."
    
    show aoi oops at tworight
    with charachange
    
    "Aoi" "I overheard something."

    hi "Could you be a little more specific?"

    "Aoi" "Lilly said she took a trip with you."

    hi "Well, yes. That's true…"
    
    show miki basic_grin at twoleft
    with charachange
    
    "I suddenly notice Miki grimacing."

    "Aoi" "Are you dating?"

    "I pause for a moment, considering the options."

    "Each and every one is quickly discarded but for the truth."

    hi "Yeah."
    
    show miki basic_upset at twoleft
    with charachange
    
    mk "No! This is awful! How could you do this, Hisao!?"

    hi "What's so awful?"
    
    show aoi smile at tworight
    with charachange
    
    "Aoi gives a weak smile, trying to cover for her despairing friend."

    "Aoi" "We kind of… made another bet."

    hi "I can guess who bet each way."

    "Aoi" "I'm happy for you, though."

    "Miki gives a sigh, looking back to me."

    mk "Yeah, I am too. Good job."

    hi "Uh, thanks."

    "They make it sound more like I'd felled a legendary beast than begun dating someone."

    "Seemingly noting my expression, Aoi quickly continues."

    "Aoi" "It might be wise to try and keep this quiet, Hisao."

    hi "Huh? Why?"

    "Aoi" "Class representative of 3-2, well-liked by many in the class, foreign…"

    hi "Ah."
    
    show miki basic_grin at twoleft
    with charachange
    
    "Now that she mentions it, I guess Lilly would be the kind to be popular."

    "But, why is Miki grinning like a… Oh no!"

    "Before either Aoi or I can stop her, her quickly takes a deep breath, filling her lungs for a verbal onslaught."
    
    show miki basic_excited at twoleft
    show aoi oops at tworight
    with charachange
    
    mk "Hisao's conquered Lilly! Step right up folks, we have a winner! Roll up, roll up, see the magnificent boyfriend of 3-2's Wolf in White!"
    
    "I bury my blushing face deep into my palm, Aoi trying in vain to calm her loudly dancing friend."

    hi "I'm… uh… going. Seeyas."

    "Aoi" "Sorry, Hisao."

    hi "It's fine."

    hide miki
    hide aoi
    with charaexit
    
    "I walk down the hallway slumped and grimacing, feeling all too close to an oddity paraded around in a circus act."

    "It was inevitable it'd leak out, but that's…"

    "Ah, stop it, Hisao. What's done is done."

    "I pick myself up slightly and begin to walk down the stairs, deciding on a quick trip to the dorms to salvage what's left of my pride."

    scene bg school_lobby
    with locationchange

    # Making an assumption about the layout of the classes here, need to sort this out

    "As I round the bottom of the stairs and begin to make my way to the exit, I pick up the faintest of sounds."

    "A familiar tambre, floating through the air like roses on a breeze."

    "Like a mouse following the sweet scent of cheese, I half-conciously drift towards the source of the melody."

    "Deep, but playful."

    "Measured, but whimsical."

    "Standing before a classroom door I've encountered several times before, I slowly cast aside the barrier between us."

    scene bg school_musicroom
    show lilly silhouette
    with locationchange

    "The sight is exactly as I'd expected as I close the door beind me."

    "Lilly sits near the window, gracefully playing her cello with her eyes closed."

    "Rather than switch on the lights, I quietly pull up and chair and sit in it backwards, resting my arms on the back and my chin within them."

    "Her small grin is the only indication she knows I'm there, with her playing thankfully going uninterrupted."

    "It's a different tune than the Saraband, and entirely unfamiliar."

    "Compared to the Saraband, it seems uplifting and playful, more akin to a ditty than an orchestral performance."

    "Each note is whimsically touched and then discarded in short order, far from lingering in the air."

    "I've never heard the cello played in such a way, though before meeting Lilly I'd heard very little of the cello to begin with."

    "It's nice."

    "Closing my eyes, I relax and let the music take me."

    scene black
    with shuteye
    
    #scene bg school_musicroom
    scene black
    with shorttimeskip

    "I'm not quite sure how much time passes, whether it be a scant few minutes or an hour, or even if I actually slept or just rested."
    
    scene bg school_musicroom
    with openeye
    
    "In either case I eventually come to my senses, groggily opening my eyes as she still plays."

    "Giving a stifled yawn, I lean back in the chair as I stretch."

    "…Oh dear."

    "I hate this feeling."

    "The feeling of my center of gravity going beyond the point of no return."

    with vpunch
    
    "Almost as if everything were moving in slow motion, I fall backwards and land on the floor with a loud thud."

    hi "Ah, damn…"

    show lilly basic_surprised_close_ni
    with charaenter
    
    "As I quickly move to right myself, picking the chair off my front as I do, I see Lilly in front of me with her cello performance having come to an abrupt end."

    li "Hisao, are you—!"

    hi "Calm down, I'm fine."
    
    show lilly basic_weaksmile_ni
    with charachange
    
    "We both give a sigh, Lilly in relief and I in exhaustion."

    li "Hisao, do be careful."

    hi "I know, I know. I'm not that fragile."

    "Well, to tell the truth, I am."

    "That fall, any fall, could have killed me."

    "The delicate tripwire over my heart need only a breath to trigger. Indeed, it could trigger all by itself."

    "But that's not important."

    "If I die, I die, and that's it. The last thing I want to do is worry others, much less Lilly."

    "This is my burden, and mine alone."

    "With the fracas of before abating, we return to out seats. Both of them the correct way around, I might hasten to add."

    hi "What was that piece called?"
    
    show lilly basic_smile_ni
    with charachange
    
    li "<Yeah this needs a new cello piece that's kind of lighthearted. Title will go here.>"

    hi "<Title>, huh? It's nice."

    "She gives a nod of appreciation, packing her cello into its case."

    "As I idly watch her, I can't help but recall Mutou's words."

    centered "“Future”"

    "It's a foreboding word, telling of either happiness or sadness."

    "As someone who'd just taken each day as it came, I'd hardly ever paid it any heed."

    "As Lilly rights herself, cello safely packed, my wonderment takes on verbal form."

    hi "Hey Lilly?"

    li "Mm?"

    hi "Do you know what you want to do after school? As a career?"

    li "Hmm, I'd like to be an English teacher, I suppose."

    hi "Woah, fast!"
    
    show lilly basic_giggle_ni
    with charachange
    
    "She gives a small giggle."

    li "I've held the idea for quite a time now."

    hi "Well, I can understand English. Why'd you decide on teaching though?"

    "She furrows her brow in thought momentarily, organising her scattered thoughts rather than deciding upon new ones."

    li "If I were to put it one way, it's that I like being around people."

    "I lean back, taking her words to account."

    "For her to like being around others is expected, I guess. Not to mention being the class repsesentative and taking to the position with gusto."

    hi "To have such a clear idea of what you want to do… I'm kind of envious."

    li "You're not sure what you want to do?"

    hi "Not at all, though it's more because I didn't think about it rather than really not knowing."
    
    show lilly basic_smile_ni
    with charachange
    
    li "I'm surprised. I thought you were quite driven."

    hi "Really?"

    li "You seem to excel in science."

    hi "Well, I kind of have a knack for it. I tend to think logically, I suppose. I'm guessing you think creatively?"

    li "Hmm, you could say that."

    "With a slight grunt, she stands up and picks up her cello."

    "Taking my cue, I pick myself off my chair as well."

    li "Shall we be off then?"

    hi "Indeed we shall, madame."
    
    show lilly basic_smile_close_ni
    with charachange
    
    "As I hold out my elbow, she hooks her left arm through it, her face lingering close to mine."

    "With a light, affectionate kiss, I open the door, light flooding into the darkened room."

    scene bg school_hallway3
    with locationchange

    "Walking through the hallways, arm in arm, more than a few of the students we pass steal sidelong glances at us."

    "All I can do is smile and hold my head high, just as Lilly does."

    scene black
    with dissolve

    return

label en_L31:

    scene black
    with None

    #centered "*thump* *thump* *thump*"
    play sound sfx_doorknock
    with Pause(0.5)

    "Eugh."

    "The sound of knocking on my door is very far down the list of things I'd like to be woken up by."

    "A gentle kiss on the cheek would be nice, or a sweet blonde face near mine…"

    li "Wake up, Hisao. It's morning."

    hi "Just a little longer~"

    li "You sleep too much, you know that?"

    hi "I sure do."

    scene bg school_dormhisao
    with openeyefast
    
    "No! Stop! Don't do this, Hisao!"

    "I quickly shake my head to get the atrociously cliche scene out of my mind."

    "Kenji's manga is rotting my brain, I'm sure of it."

    "Alert and alarmed, I pick myself up out of bed and quickly swing open the door."
    
    play sound sfx_dooropen
    
    scene bg school_dormhallway
    show kenji tsun
    with locationchange
    
    # Open to Kenji sprite

    hi "Speak of the devil."
    
    show kenji rage
    with charachange
    
    ke "What?"

    hi "Nothing."

    "Huh."

    "It's not unusual for my admittedly dry humour to fail on him, but he seems to be positively simmering with rage."

    hi "Uh, dude?"

    ke "I can't believe this, man."

    hi "Believe what?"

    ke "You betrayed me. I can't believe this."

    hi "Betrayed you? How?"

    ke "You're a traitor to the cause, an agent, a spy planted by the enemy forces."

    hi "Damn man, slow down. What'd I do?"

    ke "You know damn well what you did."

    ke "Sickening."

    "It takes a monumental effort not to snap at him for pulling this on me just after I wake up."

    hi "Kenji, I will close this door if you do not tell me what I've done."

    ke "Fine, fine. I—{w=0.15}{nw}" #reminder for the potential {nw} break

    scene bg school_dormhisao
    with locationchange
    
    play sound sfx_doorclose
        
    "I close the door."

    "After a couple of seconds of sweet, sweet silence I reluctantly open it once more."
    
    play sound sfx_dooropen
    
    scene bg school_dormhallway
    show kenji rage
    with locationchange
    
    ke "What's up with that? I was about to tell you."

    hi "You were too slow."

    "…"

    hi "Fine, just spit it out."
    
    show kenji tsun
    with charachange
    
    ke "It's Lilly, man."

    "I should've guessed."

    hi "I'll save you the questioning. We love each other, and we're dating. Anything else to add?"

    "Momentarily taken on the back foot, the statement, surprisingly, seems to calm him down."

    ke "Good."

    hi "Good…?"

    ke "You understand what this means, then."

    hi "Understand what?"

    ke "I had high hopes for you, I really did."

    ke "But, damn. Of all the people…"

    ke "It was nice knowing you, but we've come to the end of the line."

    ke "You know Sex and the City? This is like when… yeah, that's right."

    ke "You're Mr. Big, I'm your wife, and Lilly's, like, Carrie."

    ke "You had an affair with her, and you broke our thing."

    ke "You get that, man? You broke it. Completely. It's all over the goddamn floor. Superglue ain't gonna fix that now."

    "He's delusional."

    "Completely. God-forsaken. Delusional."

    "I can only stand and watch his tirade helplessly, thinking him more fit for an asylum than Yamaku."

    ke "This is it, man. We gotta part ways, here and now."

    ke "You're one of them now. Them. You hear me?"

    "I wish I didn't."

    ke "I… I gotta go. Seeya, man."

    hi "Uh… seeya."

    hide kenji
    with charaexit
    
    "And with that, he simply and silently walks off."

    hi "What in the world…"
    
    scene bg school_dormhisao
    with locationchange
    
    play sound sfx_doorclose
    
    "My entire day's energy seemingly sapped within the space of a few minutes, I lazily let my hand flop onto the door, barely shutting it."
    
    "So I'm on the side of the feminists now, I'm called Mr Big and I come from some American TV show."

    "I was wrong."

    "He isn't that hard to understand."

    "He's just completely goddamn insane."

    "Trying to push the memory to the back of my brain as much as humanly possible, I quickly busy myself with getting ready for the coming school day."

    "Thank God it's a Friday."

    scene bg school_gate_ss
    with shorttimeskip

    "Class for the day ends not a moment too soon, the sunset's orange glow faintly bathing the concrete as I walk through the courtyard with the other students."

    "The mood in the school seems to have risen a miniscule amount, now that everyone's getting into the rhythm of exams."

    "That's not to say it's back to normal though."

    "Well, there's the summer vacation to look forward to at least."

    "As I round the large school gate, I see the welcome sight of Lilly patiently waiting beside it."

    hi "Hey, Lilly."

    li "Ah, Hisao. Good afternoon."

    "She gives a deep bow after saying it, her bangs falling beside her face."

    hi "Where's Hanako?"

    li "It seems classes held her up."

    "An obvious lie."

    "We both give a weak smile to each other in mutual acknowledgement."

    hi "She's a terrible liar, isn't she?"

    li "It seems so."

    hi "Still, her heart's in the right place at least."

    "With a nod of agreement, she loops her arm through mine as we begin down the street to the store."

    scene bg school_road_ss
    with locationchange

    "As we silently walk, arm in arm, I gaze up at the sky."

    "A cloudless expanse, tinted orange by the beautiful sunset. Even the slight breeze felt as I woulked through the courtyard seems to have settled."

    "All that's left is a feeling of upmost serenity and silence, the occasional passing car the only sound bar our footsteps on the pavement."

    "I'm turning into a hopeless romantic, I'm sure of it."

    "As I look over to Lilly, calmly and gracefully walking beside me, I can't help but wonder how the scene seems to her."

    "Minutes pass as we walk, a knowing silence passing between us."

    "I never thought I'd find the same calm when next to another that I felt in solitude, but I have."

    "My little reverie is abruptly ended, though, as two people come walking up the path towards us."

    "To the left, Akira, and to the right… someone I don't know."

    "Short in stature and very slender, she seems to be a young girl."

    "Thinking back to Akira's run-in with Emi, I can't help but let my mind wander in unwelcome directions."

    aki "Yo, Hisao, Lilly."

    li "Ah, Akira. Good afternoon."

    hi "Hey Akira, uh…"

    hh "Hideaki. Pleased to meet you."

    "Hideaki, huh? That means “she” is actually a “he,” I guess."

    "Looks like I dodged a potentially quite embarassing bullet."

    hi "Hi, I'm—" #reminder for the potential {nw} break

    hh "Hisao, I heard from Akira. The girl beside you is Lilly, I assume?"

    "She gives an affirmative nod."

    aki "Well, that's the introductions out of the way."

    hi "You know each other?"

    li "Ah, this must be the boyfriend you mentioned to me before."

    "Lilly leans towards him and beams a smile, to which he smiles back."

    aki "That's how it is."

    hi "I see."

    "Several things become immediately obvious."

    "One, there is an obvious difference in height between the two."

    "Two, he does not look legal by any stretch of the imagination."

    "Three, I have a worrying suspicion that Akira doesn't care about such trivialties."

    hh "I see that Lilly is blind."

    "The blunt statement draws a raised eyebrow from Lilly and I."

    hi "How'd you know?"

    hh "She's not looking directly at me."

    hi "Oh."

    "A second's silence."

    hh "You're not the sharpest knife in the drawer."

    hi "What?"

    hh "Unlike her, I'm not blind. I can see the retracted cane held in the same hand as her bag."

    "As I quickly glance down, noting that she does, indeed, have a cane in her hand, I feel a fair measure more stupid than before."

    li "Many in this school don't take as well to their disabilities as I, Hideaki."

    hh "That does not concern me. I am not interested in knowing anyone who is so easily offended by pointing out the obvious."

    "A momentary silence falls, the words of Hideaki being analysed by all."

    "He's sharp, yes, but more than a little unsympathetic. Logical, but lacking in tact."

    "His attitude reminds me of Shizune, in a way, as do his looks."

    aki "Well, that's the shortie for ya."

    "I raise an eyebrow at the nickname, but he doesn't seem to mind it."

    "I guess, for him, it falls neatly into the category of “the obvious.”"

    hh "As for you…"

    "He narrows his eyes, examining me closely."

    "Ah, I see."

    "For him, this is nothing more than a game. A test of his observational skills."

    "He really does have the mentality of a child."

    hh "Heart."

    aki "Woah, you're good!"

    hi "How did you…?"

    hh "You're in a Yamaku uniform, so there's obviously something wrong with you."

    hh "Looking at you, though, you have no missing limbs or deformities, so external disabilities are out."

    hh "Considering the lack of any strange mannerisms, it's unlikely you'd have a mental disability in any case."

    hi "Yamaku doesn't take mentally disabled students."

    hh "I know."

    hh "Leaving that aside, the only possibility left is that of internal disabilites, of which the most common is a heart condition."

    "More than a little bemused, I look to Akira."

    hi "He's sharp, I'll give him that."

    aki "The shortie's got a head on him, pity about the mouth though."

    "She latches down onto the top of his head with her hand, pulling it around a bit."

    "The spectacle is made all the more amusing by the dreary look on his face."

    "As she withdraws her hand, Lilly gently reaches forward, lightly feeling out the top of his hair before pulling back and lowering her eyebrows in concern."

    li "Akira…"

    aki "Yeah?"

    li "How old is he?"

    hh "You needn't direct the question elsewhere. I'm sixteen."

    "He doesn't strike me as the kind of person to lie, but I'll be damned if he looks that old."

    "His statement doesn't seen to alleviate Lilly's concern, and only partially abates mine."

    "The cocky smile on Akira's face doesn't exactly help things, either."

    hi "Let's not… go down this path."

    li "Indeed."

    "Akira breaks out into laughter as Hideaki simply shrugs, neither seeming overly concerned by the age nor height difference between them."

    "What a strange duo."

    aki "Well?"

    hi "Well… what?"

    aki "Ya goin' down to the shop, or just standing here?"

    hi "Ah, yeah."

    scene bg suburb_roadcenter_ni
    with shorttimeskip

    "As we emerge from the store, the darkness of the night's fallen on the path ahead, the streetlights ahead giving the only illumination to be seen."

    "The strange sight of a blonde foreigner, a girl in a luxurious suit and a young boy who looks closer to a cute girl draws more than a few stares from the people within."

    "Not that any of us care. In fact, I suspect a certain suited woman relishes the confusion of those around us."

    "A small yawn comes from Hideaki, earning him a pat on the head from Akira."

    aki "Tired?"

    hh "Mmm."

    aki "I'll take ya back to the hotel once we see off these two, then."

    "I can't help but narrow my eyes at her, a gesture which goes far from unnoticed."

    aki "Get ya mind out of the gutter, boy. You seen where he lives? It's stifling as hell."

    "Looking to Hideaki for his thoughts on the matter, all I see is the boy tiredly wiping his eyes while paying the conversation little heed."

    "The infectious yawn seems to leap to Lilly, barely giving her time to politely hide her open mouth with her hand."

    aki "Long day for everyone, huh?"

    "I can't help but think back to the morning's dealings with Kenji."

    hi "Yeah, you could say that."

    li "You had a long day too?"

    hi "Kenji. You?"

    li "The entire class of 3-2."

    "I give her a couple of pats on the shoulder, from one battle-weary comrade to another."

    hi "Sounds like you had it rougher."

    li "My dealings with Kenji in the past… lead me to think otherwise."

    hi "Ah, that's right. He's in your class."

    hi "Hmm, what was he today?"

    li "Today? Hmm…"

    "She brings her finger to her chin briefly to mull the question over."

    li "He was somewhat withdrawn… though that seems to be the status quo for him. Why? Did something happen?"

    hi "Nah, it's nothing. He just seemed kinda odd this morning is all."

    "The fewer that know about his paranoid ranting the better."

    scene bg school_dormext_ni
    with locationskip

    "Before long, we stand at the entrance to the student dorms."

    aki "Well, we'd better be off."

    hi "We do as well. See you, Akira, Hideaki."

    li "Bye."

    "As Lilly waves and akira and Hideaki start to leave, Akira's voice rings out as she holds her hand in the air with Hideaki walking next to her."

    aki "Seeyas. Good to see you're finally together."

    "And with that, they leave."

    hi "Another day down, I suppose."

    li "As odd as they are together, I'm happy for them."

    hi "Yeah. They seem to get on well."

    li "To be honest, I was somewhat worried when I heard she'd found a boyfriend."

    hi "With a personality like hers, I can't imagine why."

    "As sarcasm positively drips from my voice, I suddenly realise something."

    hi "Hey Lilly, did you tell her we'd started going out?"

    "She silently shakes her head, before her expression matches mine."

    li "“Finally together?”"

    hi "That woman…"

    "As we say our goodbyes, we start to head off to our respective dormitories."

    "That is, before we both stop and face each other."

    hi "Shall we, madame?"

    li "My my, that would be very gentlemanly of you, Hisao."

    "With a nod of appreciation, she hooks her arm in mine as we leave for my dormitory together."

    scene black
    with dissolve

    return

label en_L32:

    scene bg school_dormhisao
    with openeye

    "Mmh, so bright…"

    "Propping myself up with an arm as I rub my tired eyes, I quickly try to take measure."

    "Let's see, it's daytime. That's good, I suppose, as it means I actually had a solid sleep through the night."

    "Lilly lies beside me, naked under the sheets, due to…"

    "I grin slightly as the events of last night daintily dance across my mind."

    "Looking back down to Lilly, I gently brush back a bang of her blonde hair."

    "She really looks peaceful when sleeping, her slow, calm breathing being the only movement she makes."

    "As much as I'd like to linger though, the fact that we're meeting the others in town today doesn't escape my memory."

    "As careful as I am not to disturb her as I maneuver out of the bed, she stirs as I lever myself off."

    li "Himamo?"

    "It seems her mouth hasn't quite woken up with the rest of her body."

    "With severely dishevelled hair, she sits herself upright and wipes the sleep from her eyes."

    hi "You look awful."

    "She stares at me with half-closed eyes, entirely unwilling to play along."

    hi "Don't worry, I don't look the best either. You can have a shower after I'm done."

    li "Hisao, Hisao."

    "She waves her arms in front of her, half-heartedly calling for me."

    "Smiling, I gladly meet them and give her a warm hug, both of us savouring each other's contact."

    "After precious seconds I break off, giving her a light kiss as I lean back and rub her hair."

    "Beaming at me with closed eyes, she looks like a satiated puppy."

    hi "There, there. We'd better get going, it's almost time to meet them."

    "She gives a smiling nod, pulling the blankets up around her for warmth."

    "With a quick yawn and a stretch, I open the door to the shower."

    scene bg school_dormbathroom
    with locationchange

    "As the warm water flows over my body, I suddenly realise just tired last night's events made me."

    "I guess, having only gone to sleep well after midnight, it'd make sense to have slept in."

    "Waking up just after noon is somewhat ridiculous, though."

    "An impromptue cough brings me out of my thinking, allowing me to savour the hot shower."

    "I can feel seemingly every muscle in my body relaxing as my mind clears."

    hi "Ah, so good…"

    li "Mm, it feels very good, doesn't it Hisao?"

    "I all but freeze as I hear Lilly's silky-soft voice from behind me."

    "That pales in comparison, though, to my reaction as I suddenly feel Lilly's wet body pressing against my back, her left leg coming around mine."

    hi "L—L—L—L—" #reminder for the potential {nw} break

    li "You needn't stutter, Hi… sa… o."

    "My breath catches as her right hand reaches around my left cheek, her other hand turning off the tap before venturing onto my bare chest."

    return

label en_L32h:

    # Event CG

    scene black

    "Hisao, think, stop panicing, just collect yourself for a second!"

    "…"

    "It's useless."

    "My mind races seems to race in every direction as her breasts press into my back, her entire body being pulled against mine."

    "My body only tenses more as her hand starts to move down my chest, slowly zigzagging downwards."

    "To say the experience is incredibly erotic is understating things."

    hi "L—Lilly, this is kind of…"

    li "Wonderful…"

    "The single word is far from a response to my words, her voice giving form to the feeling beneath her moving hand."

    "Whether it's out of arousal or shock, I can't move a muscle in my body, even as her fingers gently move through my lower hair."

    li "My my, Hisao…"

    # Event CG

    "I give a gulp to gather myself as her hand her hand moves around my sack, gently but firmly cupping and feeling it."

    hi "Ah…"

    li "Does it feel nice?"

    hi "Ah, mm."

    "Hardly able to form so much as a coherent sentence, I can barely mumble a response."

    "Taking precious moments to feel it, moving her hand and fingers around it's expanse, her beath continues to deepen."

    "As her hand moves upwards, my breathing becomes more and more ragged."

    # Event CG

    "Just as her hand comes around my shaft, slowly moving up and down in rhythmic motions, she turns my face to meet hers, locking our lips together as her tongue ventures into my mouth."

    "I have no idea how much time passes, all control of my body ceded to her as our longues lap over themselves."

    "It doesn't take long, though, before I rescue my mouth from hers, taking a much-needed breath of air to fill my lungs."

    hi "Lilly, I can't… hold on…"

    li "Just a little longer, Hi—sa—o."

    "My hips start to move back and forth slightly, every ounce of my will focused on stemming the urge to come."

    hi "L—Lilly…"

    "I can barely force the words through clenched teeth, well on the verge of my control."

    hi "I… I c—can't… Aaah!"

    # Event CG

    "My mouth and eye open as my hips thrust forwards, my mind blanked as the force of my orgasm all but destroys my thoughts."

    "Surge after surge flows before I fall back into Lilly's arms, all but exhausted."

    "My ragged panting belies the fact that it's the most powerful orgasm I can ever remember having."

    "I stay in Lilly's arms for minutes, regaining myself from the experience."

    hi "Lilly… that was… amazing…"

    "She brushes a hand over my forehead, moving my fringe sidewards as I feel her nod."

    "As I look sideways to steal a glance at her face, she smiles as we peck each other's lips."

    "As my thoughts regather themselves, I turn to face her, gently moving her back to the wall of the shower with a soft wet thud."

    li "Hisao?"

    hi "It would only be proper to repay you in kind, no?"

    "Before she can object, I bring my lips to hers, stealing her words with my tongue."

    # Event CG

    "As we break off, I move down to her pale, wet breast, taking a nipple in my mouth as I gently knead both."

    "Her hand gently strokes the back of my hair, a quick glance being all that's needed to see her biting a finger of her other."

    "Throwing herself on me must've given her a measure of excitement as well, I guess."

    "I can't help but marvel at the feel of her breasts, the wetness and softness apparent underneath my hands."

    "Lightly playing with her nipple inside my mouth, it seems to be surprisingly stiff already."

    "As her breath suddenly seems to catch, I begin to move downwards, lightly kissing her wet body as I go."

    "A single kiss to the blonde tuft of hair below her stomach is the last I give before a pause, ever-so-gently pilling her lips aside with my thumbs."

    "At the center is my prize. That small, pink nub."

    # Event CG

    "Leaning forwards, I gently lap at it with my tongue, for moments strumming it before sucking and back once again."

    "As her breathing becomes more fractured and her hips start to squirm, it becomes obvious she's nearing her limit."

    "Unlike Lilly's gentle teasing, though, I all but vibrate my tongue against her as I slip two fingers into the gap between her legs."

    # Event CG

    "Her groans become audioble as she bites down harder, my fingers twisting and separating inside her."

    "After precious moments of feeling her soft insides, almost by complete accident, my fingers happen upon a section softer than the surrounds."

    li "Ah… Aaah…!"

    "She can barely contain her excitement, her moaning picking up in speed and intensity."

    "This must be her g-spot, from the reaction she gave."

    "Grinning slightly as my opportune find, I gleefully tap it with my paired fingers, continuing to lap the delicate nub between her lips."

    li "H—H—Hi… Ah… Hi… AAAAAAH!"

    # Event CG

    "Her entire body tenses tightly, her toes and fingers curling around as she orgasms."

    "As her insides seem to suck my fingers inward, even I notice the difference from last time as a small spurt of clear liquid shoots from behind my fingers, her body remaining sensed and her mouth clenched open but silent."

    "Even the duration seems to last longer, but it eventually begins to fade, a deep uneven breath leaving her as she falls back against the wall, letting it hold her weight."

label en_L32x:

    scene bg school_dormbathroom
    with locationchange

    "Momentarily savouring the sight, I stand and take her body in mine as she weakly puts her arms around my back, our wet and exhausted bodies pressed against each other."

    li "I guess…"

    hi "Hmm?"

    "She takes a couple of long breaths before continuing."

    li "This makes us… even."

    "I can barely manage a small chuckle in response."

    hi "Mm."

    scene black
    with dissolve

    return


label en_L33:

    scene bg city_street1
    with shorttimeskip

    "Lilly and I slowly walk through the brightly sunlit town, with her holding my right hand."

    "Actually, it would probably be more correct to say that she's taking it hostage. Not that I mind."

    "After a quiet trip down, Lilly leaning against my shoulder as we went, there's a certain pang of regret in the fact that we can't spend the day alone together."

    "Well, there's always tomorrow, I guess."

    "As we continue walking, the familiar sight of Emi, Rin and Hanako comes into view."

    "Not to mention Akira and Hideaki."

    "As Rin looks upwards, wholly absorbed in watching a cloud lazily floating across the sky, Akira and Emi sway from side to side, sizing each other up as they prepare to lunge."

    "Hideaki looks on as if he were a better watching a horse race as Hanako silently motions for them to stop, a look of worry on her face."

    hi "Hey guys."

    "The statement draws Emi's face to us, a look of annoyance written on it."

    "That is, until she realises her fatal mistake."

    "Seizing on the opportunity, Akira dashes forwards and in a single fluid motion brings Emi's arm behind her back once again."

    emi "H—Hey! Let go of me! That's not fair!"

    aki "I didn't get the memo that said war was meant to be fair."

    "Lilly gives a sigh of consternation, having all but figured out what's happening."

    hi "Good grief."

    "Akira pokes her head over Emi's shoulder, letting her catch a glimpse of her smug grin."

    "As she does, I suddenly notice her grave mistake."

    "As I silently move my eyes from Emi's face to her shoulder a couple of times, she takes and hint and give an almost impercepible nod."

    aki "Eh?"

    "Akira clicks that I'm signalling something, but it's all too late."

    "With a sharp upwards movement of Emi's shoulder, Akira's face flicks up as it hits her chin sharply."

    "Momentarily dazed, she wildly stumbles back before gathering herself and rubbing her chin sorely."

    aki "Son of a bitch, two on one!"

    "Emi grins madly and gives a thumbs-up for my part in the impromptue alliance."

    hi "Hey, I thought you said war wasn't meant to be fair?"

    "Scowling at me as she withdraws her hand, she silently admits defeat, Hanako looking significantly more relaxed now that the fighting's ended."

    emi "You may have helped me, Hisao, but that doesn't excuse you for being late."

    hi "Whaaaat?"

    emi "Fifteen minutes! That means you have to buy a round of drinks for everyone!"

    hi "Fine, fine."

    "Wait, let's see here…"

    "Me, Lilly, Emi, Rin and Hanako make five people all up."

    "Assuming drinks at the karaoke place are overpriced, as they always are, and everyone gets a reasonably expensive drink, that'll be three hundred yen a piece."

    "Five times three hundred would make it one thousand, five hundred yen for everyone."

    "But now there's Akira and Hideaki, which means another six hundred yen on top of that if they decide to come."

    "That brings it to two thousand, one hundred yen in total for everyone, and that's just for drinks."

    hi "Ah, dammit."

    li "We can share the cost, Hisao. I was the one who made us late, after all."

    hi "No, no, I can't do that. I'll pay it."

    emi "Good! Looks like we're set for drinks!"

    "As she pumps her fist into the air, a cheer resounds from everyone present."

    "As I slump my head and sigh, Lilly gives a comforting pat on the back."

    hi "Well, we'd better be… getting… off… then…"

    "Before I finish the sentence, Rin slowly turns and walkes away, the heals of her feet off the ground as her face remains pinned upwards."

    "As I look upwards, I see what she's gazing so intently at—a small cloud lazily floating away from us."

    hi "Uh…"

    aki "What the hell?"

    emi "I knew this was a bad idea…"

    hi "What was?"

    emi "She didn't really want to come, so I kinda promised her we could go cloudwatching while we were out."

    hi "Cloudwatching?"

    "Rin doesn't exactly strike me as the socialising type, but it seems she's quite content to remain in her own little world."

    hh "She's about to walk onto the…"

    "As he says it, Rin turns from her course, one which was bringing her right to the edge of a busy road."

    hh "…Nevermind."

    emi "I'll grab her."

    hi "Please do. She'll do herself in one of these days."

    "As Emi skips off to lasso her wayward companion, Lilly and Hanako exchange greetings."

    hi "So, what brings you guys here?"

    aki "Shoppin' for a souvenir for Adrianne and Leanne."

    "Adrianne and Leanne… Ah, Lilly's younger sisters."

    "I click my fingers as I recall a useful memory."

    hi "Hey, Akira, what kind of souvenir were they wanting?"

    aki "Stuffed animals. Leanne's got a damn collection of the things, and despite what she'd have you believe, Adrianne's the same."

    hi "I'll be back in a jiffy!"

    scene bg city_othello
    with locationskip

    "A small bell's metallic ringing resounds through the anachronistic store, that familiar dusty smell hanging in the air."

    "Storekeeper" "Oh, I see you've come again. Welcome to Othello's Antiques."

    hi "You remembered me?"

    "Storekeeper" "I remember every last person that goes through that door. Doesn't hurt that there aren't many who do so, though."

    "He gives a quiet, husky chuckle."

    "Not many people would come to some an old-fashioned store, I suppose."

    "With a quick nod I set off into thhe isles, my objective clear in my mind."

    "One shelf, two shelf, three shelf, four."

    "Bingo, that's it."

    "Reaching forward and plucking two oversized, fluffy teddy bears from the shelf in front of me, I quickly walk back to the counter."

    "As he picks the up and examines them under the bottom of his glasses, he flicks his eyes back to me."

    "Storekeeper" "That'll be ten thousand yen, lad."

    "Shoving my depression at the figure to the back of my mind as fast as possible, I fish out my wallet and finger through the notes inside."

    "Ten, twenty, thirty, fourty… ten thousand."

    "I hand the small wad over to him, giving him pause."

    "Storekeeper" "Cash?"

    hi "Ah, is that a problem?"

    "Storekeeper" "No, no, not at all. Not many seem to deal in cash nowadays is all."

    "Storekeeper" "Can't say I like the trend myself. I like to see my money."

    "With the cash handed over in exchange for the bagged teddy bears, I leave the store with a small ding and a significantly lighter wallet."

    scene bg city_street1
    with locationskip

    hi "Back!"

    "As I jog up to the mishappen group, I see Emi and Rin having returned."

    aki "Ah, you're back. Whatcha' get?"

    "I hand the large back over to Akira, who pulls the handles aside with both hands and dips her head deep inside."

    aki "Woah! That's perfect!"

    li "What did you get, Hisao?"

    hi "Couple of big teddy bears. They looked cute the first time I went into the store, so I thought they might be okay as souvenirs."

    "Looking back to Akira, she's taken one of the bears out and started playing with it."

    hi "Hey, you're gonna have to pay for those, you know."

    aki "Tsch. Cheapskate."

    "A small giggle from Lilly, amused at the besting of her sister."

    emi "Well, we gonna go or just stand here?"

    ha "It'll be dark soon."

    li "Hmm, she's right."

    hi "Alright, let's go then. I assume one of you knows the way there?"

    ha "Um, I do."

    aki "Alright, let's go!"

    hi "You two're coming as well?"

    aki "Of course! How could I miss a trip out with my sister?"

    "Two thousand, one hundred yen."

    "Damn."

    scene bg city_karaokeint
    with locationskip

    "Thanks to getting in before the night-time rush, we manage to grab the largest room available for non-booked patrons."

    "With the women seemingly gravitating to one side of the room, Hideaki and I are left to occupy the left seats."

    "On the table in the center are three bowls of snacks, Akira shouting the entire group's food."

    "Unfortunately, that's where the good news ends."

    "Two of the three bowls are already empty due to Rin and Hideaki eagerly scoffing away at them."

    "Not to mention, at the mention of buying drinks, Akira casually picking a flask of whiskey out of her suit pocket."

    "Feeling more than a little tired, I lean over to whisper to the busily chewing Hideaki."

    hi "You looked stuffed."

    hh "I could say the same for you."

    hi "You mind if I ask something kinda personal?"

    hh "I can choose whether to answer, but not whether to listen."

    "I suppose that's as close to “yes” as I'll get from him."

    hi "Is Akira kind of… how should I put it…"

    hi "Eager, if you know what I mean?"

    "He pauses his busy chewing, shifting his eyes to me."

    hh "Lilly is too?"

    "I let my head fall downwards."

    hi "I knew it. It's hereditary."

    "As soon as I say the word, I feel a hand grip down onto the top of my head with a surprising amount of force, dragging it around in circles."

    aki "What's hereditary?"

    hi "No comment."

    aki "Yo, shortie, what's hereditary?"

    "He closes his eyes and sticks his nose up pointedly."

    hh "Men's business."

    aki "Tsch."

    "She lets go of my head, giving me a much needed moment to massage my temples."

    emi "So, are we just gonna talk all day?"

    "Lilly claps her hands together as the prospect of moving past idle chatter is raised."

    li "Excellent! How shall we arrange ourselves?"

    emi "Hmm…"

    "She glances to Rin before quickly looking back."

    emi "I'll go solo."

    "A polite giggle from Lilly and Hanako."

    li "Shall we do a song together, Hanako?"

    ha "Mm, okay."

    "Behind her smile is badly hidden thankfulness for not making her go out on the stage alone."

    aki "Shortie, you up for a song?"

    "He looks up from the last remaining food bowl, silently shaking his head before getting back to the Very Important Business of selecting which sweet to have next."

    aki "Heh, looks like I'm a solo act. You, Hisao?"

    hi "I'll go alone. That is, if Hideaki doesn't want to be my wingman."

    "As he looks up once again, slightly confused, I give him a sly wink."

    "Taking the cue, he nods in agreement."

    aki "Oi, oi. You two seem to be getting on well."

    li "Emi, shall you go first?"

    emi "Say no more!"

    "True to her words, she quickly moves to the stage and picks a microphone off the table."

    emi "Hey, Hanako, pick a song!"

    ha "Ah, right!"

    "She moves as fast as she can to fulfill the request, flicking through songs on the console as fast as she can read."

    "Whatever criteria she's using seem to be met as she stops and selects a song from the rediculous number available, both Japanese and foreign."

    "As Emi sees the song title flick up on screen, she gives a quick thumbs-up to Hanako as she takes a breath."

    "A loud chomp from Rin as she bites down on a biscuit held between her toes heralds the beginning of her singing."

    "Pop."

    "Cheesy, sugary-sweet pop."

    "Her singing's surprisingly good, and very much suited for the song…"

    "It's just a pity I can hardly stand the music."

    "Regardless, as the last of the song passes, the room gives her a gracious applause for the performance."

    li "Hanako, ready?"

    ha "Mm."

    "With a quick nod, the two make their way onto the stage, Akira taking a quick swig from her flask before screwing the cap on."

    "A quick scroll through the list is all that's needed for Hanako to find a song, though, as she says the title to Lilly, I don't think I've heard it before."

    "Three neatly-timed beats prelude the music, and as the song begins in earnest so do Hanako and Lilly."

    "A quick but somewhat more dainty tune, quite well-suited to Hanako's voice. A voice which, surprisingly, seems to easily match Lilly's in volume."

    "While her movements are somewhat stiff to begin with, her body frees up in short time as she finds her rhythm, the two actively dancing together on stage."

    "In all too little time the song's over, the two having spent quite a bit of energy on stage."

    "Their performance earns them a crass whistle from Akira as every gives their share of applause."

    hi "You're up, then."

    aki "Ya got that right."

    "She puts her flask down on the table, a cold chill running down my spine as she shoots a cold glare up at me."

    "From that point on, I regard that small, metal flask as if it were highly radioactive."

    "Akira's wrath is something I have little want to incur."

    "With a quick skip up onto the stage, she skims through the songs and selects one in mere seconds."

    "Starting not with a beat but a low wind instrument's smooth, deep sound, it sounds far different from any pop song I've heard."

    "As her mouth opens and she begins to sing, the entire room freezes, even Rin all but forgetting the food still in her mouth."

    "Freed of it's awkward dialect and sung, her deep voice takes on a graceful, refined edge."

    "Closer to a folk song than any form of pop, she'd look much more the part in a kimono rather than a business suit."

    "For minutes the room sits, wrapt in her amazing performance."

    "Slowly trailing off, the room erupts into furious applause as soon as the music ends."

    hi "My god…"

    "Flicking my eyes to Hideaki, it seems even he was unaware of her talent."

    aki "So, Hisao, that's whatcha' gotta live up to now."

    "Damn, she knows she's talented alright."

    "Giving her a deep nod of praise as I walk up to the stage, Hideaki comes along beside me as I lean to the side, whispering."

    hi "You'll know the song. I'll take lead singer, you take backup, 'k?"

    "He gives a small, silent nod."

    "Taking our place as everyone has the girls had before, I quckly strum through the song titles."

    "Some I know, most I don't, every single one neatly categorised with cover art beside the title."

    "Sure enough, the song I'd hoped would be there is indeed present."

    "As I step back from the console, the music starts, a quiet series of foot taps coming seconds before the first words appear on screen."

    "A small grin flickers on Hideaki's face, my spontaneous plan becoming crystal clear."

    "As we sing in admittedly rough unison, his high, childlike voice perfectly compliments mine."

    "A playful twitter of the flute, a tist of saxaphone and the occasional blowing of trumpets pass through the carefree jazz tune."

    "It was a gamble on whether he'd know it, but it seems it paid off well."

    "As the minutes pass, the last chorus comes around, my heart accelerating slightly in preparation."

    "Not now…"

    "Close…"

    "Now!"

    hi "Ooh, in other words…"

    "I take a step off the stage, microphone in hand."

    hi "In other words…"

    "Hideaki's voice trails off expertly, my nerves thankfully managing not to effect my voice."

    hi "I…"

    "Another step, placing me in the center of the room."

    hi "love…"

    "I crouch down in front of Lilly, taking her pale hand in mine as my other grasps the mic."

    "With a succession of piano taps sounding out, I place the lightest kiss on the back of her hand before looking up to her face, a wild grin on mine."

    hi "You."

    "…"

    "Silence."

    "As Lilly sits frozen, her cheeks all but filled with a scarlet red, the entire room seems to erupt at once."

    aki "Woo! Way to go Hisao!"

    emi "Go Hisao!"

    "Even as laughter and clapping resounds around me, my eyes remained pinned to Lilly."

    "Taken entirely on the back foot, she can hardly say a single word."

    "Eventually, somewhat collecting herself as she smiles, she leans downwards, brushing her hair back with one hand as she lightly kisses my hair."

    scene bg city_karaokeext
    with locationskip

    "As we emerge from the karaoke parlour, night's all but fallen."

    "More than a little sapped of energy, our ragtag septet slowly makes it's way through the town."

    "Though, said slow speed isn't helped by Akira leaning heavily on Lilly for support."

    "Drunk as a skunk, it seems she doesn't possess Lilly's levels of alcohol tolerance."

    "Not that she says it's anything other than friendliness, mind."

    "At least she's quiet. That, and the fact that she's saved us the experience of her vomiting everywhere."

    "As Hideaki walks beside me, he gives a yawn and a stretch."

    hh "Nice work."

    hi "I thought you might not know the song, to be honest."

    hh "My father makes me listen to all sorts of crappy stuff."

    hi "I see."

    hi "…Hey!"

    "He smirks smugly."

    hi "Well, I guess it's good enough for you to sing it."

    hh "You two're pretty close, aren't you?"

    hi "Yeah, I guess so."

    "Now that I think of it, we really haven't spent that much time together since the trip to Hokkaido."

    "Five days. Not even a week."

    "Though, we'd come pretty close in the month before that I suppose."

    hi "How long have you and Akira been together, anyway?"

    hh "One year, one month, two weeks, four days."

    hi "You, uh, keep track of it well."

    "Eidetic memory?"

    "No, nothing quite so ridiculous. I guess he just likes her enough to remember it that accurately."

    "Though, that does lead me to another question."

    hi "How'd you two meet anyway? Isn't her family living in South Africa?"

    hh "Business trip."

    hi "Ah."

    "I guess his family must be pretty rich to do that kind of overseas travel."

    hh "I'd be lying if I said it was just us that wanted to be together, though."

    hi "Oh?"

    hh "Both our families saw how convenient such a union would be."

    hh "From there, everything was pretty much out of our hands."

    hh "And so, here we are."

    "A moment's silence."

    "What I'd thought to be a chance meeting that blossomed into unlikely love suddenly turns into a somewhat maudlin forced relationship."

    "Two powerful families using their children as pawns… it's positively medieval."

    hi "Isn't that kind of… sad?"

    "I'm not quite sure whether I should say it, or whether the word is right."

    "Nevertheless, I can't help but feel for he and Akira, especially with him being at such an age."

    "He doesn't seem to be phased by my questioning at all though, taking it in his stride."

    hh "Nah. Don't get the wrong idea, we still like each other."

    "He looks back at Akira, his gaze lingering for a second before returning to face me."

    hh "I don't know about love, but we like being together."

    hh "That's good enough for me, and if that means it makes our families happy, all the better."

    "I really can't understand Hideaki."

    "One moment, he's eating sweets with childlike fervour, and on the other he stoically defends he and Akira's forced relationship."

    "I grin and reach down, scruffing his hair to his protest."

    hi "Whatever works, eh?"

    hh "Yeah. That's how it is."

    "As I turn to the motley crew behind us, Emi excitedly walks beside Akira."

    "It seems her performance lent her a measure of respect in Emi's eyes."

    "I look back up to the night-time sky."

    "Relationships rise and fall around us, sometimes doing pirouettes and twists along the way."

    "I guess that's how life works."

    "Regardless of how one lives, the world keeps moving around them."

    "That's why I have to keep moving, without a single glance back."

    "I won't be left behind."

    "Not now that I've found someone to share my life with."

    scene black
    with dissolve

    return



label en_L34:

    scene bg school_dormhisao
    with locationchange

    "The lesson for this afternoon, learned after long hours of studying: "

    extend "Stoichiometry is boring. Easy, but boring."

    "Closing the book in front of me and rubbing my eyes, I lean back in my chair before spinning it around like a playful child."

    "Spin, spin, spin, spin."

    "Spin, spin, spin, spin."

    "Spin, spin, feeling sick, feeling sick…"

    "I stop the chair with an outstretched leg, suddenly feeling very green."

    "As I spend a few moments trying to regain my sense of balance, I find myself staring at the suit left on my bed that Lilly dropped off this morning."

    "A delivered rental, paid for in preparation for the date we were to take tonight."

    "Wait, tonight…"

    "A quick check of my clock confirms that it is, indeed, night."

    "About half an hour before Lilly said she's come, though. Thankfully."

    "Suddenly imbued with a sense of purpose, I lever myself off the chair."

    "The jelly-like feeling of my knees reminds me that I've spent entirely far too long stuck in the thing, having been sitting pretty much since lunch."

    "Not that it really accomplished much, unfortunately."

    scene bg school_dormhisao at right
    with charamove
    
    "With a slight uneasiness to my movements, I reach my bed and promptly begin undressing."

    "…"

    "With the final buttons of the suit done up, my daily pills stuffed in a trouser pocket just in case, and my tie expertly adjusted (a talent of mine, it seems), I take a moment to move around a little in it."

    "Never having worn a suit before, at least not in memory, the crisp and neat feeling is somewhat constricting."

    "I have to say I much prefer the light breeziness of my yukata to such a thing."

    "Nonetheless, it does look quite smart."

    "Very smart, actually. I quite like this."

    "The plain black of the suit jacket contrasts well with the clean white of the shirt and dark grey of the tie."
    
    play sound sfx_doorknock

    centered "*Knock* *knock* *knock*"

    "Ah, that'd be Lilly."

    "While I'd arranged to go meet her, I suspect she's come down early to, knowing her, get up to some foolish business before we leave."

    "With a small, slightly pleased sigh, I open the door…"

    play sound sfx_dooropen
    
    show misha hips_grin at twoleft
    show shizu basic_normal at tworight
    with charaenter

    "As Shizune gives an amused smile, Misha's cellphone suddenly appears with supernatural speed."

    mi "Pa-ching!"

    "With the press of a button and a snap, the phone suddenly disppears one more into her pocket."

    "Oh dear lord."

    hi "Misha…"

    mi "You look great, Hicchan! I couldn't resist!"
    
    show shizu basic_happy at tworight
    with charachange
    
    show misha hips_laugh at twoleft
    with charachange

    hi "Uh… thanks."

    hi "So uh, I guess you want an explanation, huh?"

    show misha sign_confused at twoleft
    with charachange
    
    show shizu behind_blank at tworight
    with charachange
    
    "The two look at me quizzically."
    
    show misha sign_smile at twoleft
    with charachange
    
    mi "You're going on a date with Lilly, aren't you?"

    hi "yeah, I… how'd you know?"

    show misha hips_grin at twoleft
    with charachange
    
    show shizu basic_happy at tworight
    with charachange
    
    "Misha's smile returns, redoubled."

    show misha hips_smile at twoleft
    with charachange
    
    show shizu adjust_happy at tworight
    with charachange
    
    mi "First weekend after you got back, fancily dressed just before nightfall."

    "I can feel myself deflate in front of them."

    hi "Oh. I guess it was kinda obvious."
    
    show misha hips_grin at twoleft
    with charachange
    
    show shizu basic_normal2 at tworight
    with charachange

    "She pats me on the shoulder a couple of times. Hard."    
    
    mi "Good luck, Hicchan!"

    "I look sidelong to Shizune, who gives a very businesslike nod."

    show shizu behind_blank at tworight
    with charachange
    
    "The animosity between she and Lilly really is something to behold."

    hi "Thanks. So, what brings you over to little ol' me?"

    "She seems to be taken off guard for a second, Shizune sighing at her forgetting of their original objective."

    "An envelope, notably from Shizune's hand, is given to me."

    "After a quick check as to whether it's addressed to me (yes, it is), and who it's from on the back (blank, how odd), I give a nod of appreciation."

    mi "You should check your mail more often, Hicchan!"

    hi "I wouldn't be getting much, would I?"

    mi "Ah, the carelessness of youth."

    "She says it with a whistful, though obviously fake, tone."

    mi "There's a whole heap of school stuff in your letter hole, Hicchan."

    hi "Oh."

    hi "Sorry. I'll make sure to collect it tomorrow."

    "The two of them nod before leaving, satisfied with my apology."

    "Though not before Misha calls back as they walk down the hall."

    mi "Good luck on your date, Hicchan~"

    "If anyone in the hall didn't know about where I was off to, they do now."

    "Shrugging, I swiftly launch the letter onto my desk before eading out the door to collect Lilly."


    scene bg school_girlsdormhall
    with shorttimeskip
        
    play sound sfx_doorknock
    
    centered "*Thud* *thud* *thud*"

    "Standing outside of Lilly's door, I patiently wait."

    "One second. Two seconds. Three seconds… Huh, no reply."

    #play sound sfx_doorknock
    
    "As I lift my hands to rap my knuckles on the wooden door once again, it opens."

    "Before me is a sight that I've seen only once before."

    show lilly basic_smileclosed_che_close at twoleft
    with charaenter
    
    #screw you, ksdevs. I'm not going to ask people to draw new lillydress sprites if we already have them but looking slightly different [str]
    #"Lilly, stunningly dressed in a dark blue full-length dress, and with her wavy, blonde hair freed from it's usual ponytail."
    "Lilly, stunningly dressed in a red full-length dress."
    
    li "Is that Hisao?"

    hi "At your service, madame."

    "I hold out my hand, which in an almost unseen movement is felt out and taken in her own."

    hi "Transport arranged?"
    
    show lilly basic_smile_che_close at twoleft
    with charaenter
    
    "She gives an affirmative nod."

    li "To the restaurant we go."

    # Timeskip
    show ev lilly_restaurant_listen
    with shorttimeskip
    
    "As we step up the the front counter, I glance over to Lilly."

    "Surprisingly, her face holds the same edge of pensiveness that mine does."

    "With a quick word to confirm our booking, the smartly-dressed man leads the two of us to a table by the wall."

    "I can hardly keep my eyes ahead as we walk."

    "No man nor woman is dressed in anything but their finest, with deep bergundy wallpaper adorning the richly-decorated walls."

    "With the ambient hum of quiet speech and the high-pitched clattering of cutlery and wineglasses, it really feels like another world."

    "To say I've never been anywhere like this is obvious. A fancy Japanese teahouse for an occasion or two, but never anything this lavish nor European."

    "Actually, on that note, there are a notable amount more foreigners than usual here. High-flying businessmen, it seems."

    "At least we look the part. I shudder to think how much the clothes we're wearing alone would cost, let alone the dinner itself."

    "With a quick bow, the waiter leaves to attend to others as we take our seats opposite each other."

    "Far from depending on my help, Lilly expertly brushes her hands on the sides of the table to get her orientation and sit herself dead center in the chair."

    "As my eyes flicker around, I can tell from Lilly's face that she's listening just as hard as I'm looking."

    hi "I guess this is a new experience for both of us, then?"
    
    show ev lilly_restaurant_sheepish
    with charachange
    
    "She turns somewhat sheepish."

    li "I've never come to anywhere such as this before, no."

    hi "One hell of a first date, huh?"

    "A small giggle. Even now, our nervousness is dissipating."

    "Her hands skates along the center of the table until it gently touches the menu, which the takes in both hands and brings to her face."

    li "Um, Hisao?"

    "As the lowers the beige, laminated sheet just below her eyes, I can see another sheepish look."

    "I have doubts asking the waiter for a menu in braille would be productive."

    hi "No problem."

    "As I take mine and give a quick read of it, my small grin faulters."

    hi "Er, perhaps it is."

    li "What's wrong?"

    hi "I've never heard of any of this stuff before."

    "One bizarre cuisine after another is listed, a dizzying amount of languages having been used for each one."

    "Even the simply named ones are remarkably odd."

    hi "…You can cook that?"

    "A small giggle of amusement comes from the other side of the paper sheet."

    hi "Well, I could read them all out, but it'd take a few hours."

    li "Is there anything with some kind of fish in it?"

    hi "Let's see…"

    "No. No. No. No. Aren't those poisonous? No. No. No. They eat that stuff? No. No. No. No… Ah, here we go."

    hi "There's something here with the word “tuna” in it."

    li "I suppose I'll just go with that, then."

    hi "I might do the same. I'm pretty sure a couple of these dishes are from poisonous animals. I've had anough deathly run-ins for now."

    "Lilly maintains a smile, but there's a distinct lack of laughter. Black humour mustn't be her cup of tea."

    "Before another word can be said, a portly waiter in a distressingly tight vest appears at our table to take our orders."

    hi "Provencal Tuna Salade Nicoise, please. Two."

    "I hope I didn't mess up the pronunciation of that too badly."

    li "A glass of chardonnay, please. Hisao?"

    hi "Oh, uh, the same."

    "As the waiter nods and leaves, I suddenly realise what was said."

    "I almost instantaneously bury my face in my palm."

    hi "Alcohol…"

    li "Only a bit."

    hi "Surprising they didn't ask for identification."

    li "Well, we both look old for our age. This isn't exactly the kind of place to ask such things at, either."

    hi "Point."

    "We both give a slight sigh, relaxing slightly into our seats."

    "Almost as soon as we do, the same waiter reappears at our table with two empty glasses and a bottle, the contents of which is quickly and professionally poured into the former."

    "We both nod politely as he leaves, Lilly taking her glass and gently moving it from side to side, the wine inside glistening as it works it's way halfway up the tall, clear glass each time."

    "Mine remains untouched."

    hi "I guess I'm not that surprised you know about a place like this. Those who have the money would, I suppose."

    "She pauses a moment, a whistful look on her face, before gently smiling."

    li "Why do you think I'm doing this, Hisao?"

    "Taken slightly off guard, it takes a second to reply."

    hi "Bored?"

    "She gives a small chuckle, shaking her head."

    li "No. A habit picked up while being taught at the academy."

    li "Learning how to fit into society was as much a subject as math or history."

    hi "So learning dexterity by feeling the weight in the glass, and subtly adapting?"

    li "It was one of the exercises. Not with wine though, obviously."

    li "Even though I've left that world behind, vestiges of it still remain."

    "Her speech, her graceful movement, her exceptional manners… I couldn't tell."

    hi "What was it like?"

    li "It was a prestigeous school. Many powerful families sent their children there."

    li "That fact permeated everything. Even at such a young age, relationships were usually formed with one aspect in mind—connections."

    li "Everything was superficial. A show put on to give a display of power and wealth."

    # Lilly haet gokigenyou

    "She gives a small, self-deprecating chuckle."

    li "I shouldn't complain about it though. Not many even have the chance to go to such a school."

    hi "Do you… resent your parents for sending you there, then leaving?"

    "She gently shakes her head."

    li "My family is highly patriarchal. My father, business in mind, was entirely lost as to what to do with me."

    li "In the end, he made the decision that my learning was a higher priority than staying with the family."

    li "He simply did what he thought was best."

    "To say such things so easily. What an unbelievable girl."

    hi "You're too kind-hearted, you know that?"

    li "Hmm?"

    hi "Most would hate their parents for something like that."

    "She takes a sip from her glass, the wine slipping down effortlessly."

    li "What of yourself? What's your family like?"

    hi "Mother. Father. Only child. Middle-class."

    hi "My parents live a fair way down south of here, so I had to live in the dorms."

    li "Was it ever lonely, being an only child?"

    hi "Well, I had friends and stuff. I guess it's not really any substitute, though."

    "I guess my experience is the same as hers. For all intents and purposes, bereft of communication with her sisters, she was an only child as well."

    "After a second's silence, we both note the waiter delivering our meals."

    "Lilly does an expert job of appearing entirely normal, if not for the fact that her nod to him is slightly misaligned due to his silence."

    "The dish served lives up to the salad name, though the portion's rather small."

    "At least it looks edible, I guess."

    "Lilly takes her knife in one hand and fork in the other, quickly getting to work on the dish as I do."

    "My haphazard, noisy shuffling of leaves and vaguely-meatlike squares onto my fork is matched by Lilly's silent and measured prodding and chewing."

    "The only giveaway as to her sight is the occasional tapping of the sides of a piece of meat to work out it's edges."

    "Another vestige of her academy days."

    "I find myself having finished my meagre meal in little time, Lilly taking the last few bites as I sit observing her."

    "Her aura of confidence is something I've never really felt from any other."

    "She gives off an air of womanly grace. The word “girl” doesn't seem to fit her in any case."

    "In caring for Hanako, and indeed herself, she must have needed such a personality."

    "In order for everyone else to smile, she hid her sadness."

    "As she dabs her mouth with a knapkin, I find myself shaking my head."

    "She doesn't need pity. Neither would she ever ask for it."

    li "Finished, Hisao?"

    hi "Yeah. Small, but it was pretty nice."

    "In a leafy, tasteless kind of way."

    "At least I know I'll never become a vegetarian."

    "Content with my appraisal, she gives a small nod."

    hi "You know, you're stunningly beautiful. I'm surprised no-one's ever confessed to you before."

    li "You assume they haven't."

    "The simple statement takes me off guard. Not that I should be surprised, I guess."

    hi "Really? Who was it?"

    "She gives a small, whimsical smile."

    li "He was from my class last year."

    li "A sweet boy, but a womaniser. It hardly took him a week to find another sweetheart."

    hi "Somehow, you making sure that he found someone else is hardly surprising."

    "She quickly moves to change the subject, a touch of embarassment written on her face."

    li "And what of you, Hisao? I'm sure someone like you must have had at least one admirer."

    "As I open my mouth to speak, my throat seems to become slightly tight."

    hi "I… had… one. Her name was Iwanako."

    "I swallow down the ball in my throat, Lilly's face collapsing slightly as she hears the uneasiness in my voice."

    hi "It was when she confessed to me that I had my heart attack. There in the woods, during winter."

    li "I… see."

    "In the face of my unexpected wound, she find herself lost for words."

    hi "She visited me when I was in hospital. For months she came in and talked, but eventually… she just stopped coming."

    hi "She was there every day. Then every second. Then once a week."

    hi "And finally, one day, she just stopped entirely."

    li "Did you ever see her again?"

    "I shake my head before realising the futility of the task, wrapped in my own little world."

    hi "No. That was the last I saw of her."

    "Seconds pass in silence, before I speak again."

    hi "Come to think of it, I never did reply to her confession."

    hi "She just came of her own accord, and left just as she'd come."

    li "Did you love her?"

    "Did I love her… "

    extend "It's such a simple, obvious question, but I'd never asked it to myself."

    "Though I have a feeling that, no matter how much I pondered it, I'd never come to a conclusion."

    hi "I don't think so."

    hi "At the time I was just happy to have a girlfriend. I never felt any real attraction to her."

    li "But if you hadn't have had that happen to you…"

    hi "Well, in the end it did. There's no changing that. Besides, if I hadn't had my heart attack, I wouldn't be here."

    hi "Nearly dying gave me a second, totally different life. Ironic, isn't it?"

    "Instead of replying, she reaches forwards, taking my cheek in her palm as she smiles warmly."

    li "You're kind, Hisao. I really do love you."

    "Seeing her face like this, with her palm gently caressing my face…"

    "I guess this is love."

    extend "What a fickle emotion."

    hi "We've both had pretty weird pasts, eh?"

    li "I think by most standards, our present is rather odd as well."

    "I smile and hang my head."

    hi "Touche."

    "I look back around the room, the quiet hum of patrons continuing."

    hi "This place probably fits into the “odd” category."

    li "It is a tad… overbearing."

    hi "That's one word for it, yes."

    "I catch the eyes of a scurrying waiter, a short, scrawny boy no older than twenty."

    "He kind of reminds me of Kenji, though obviously less comically overdressed."

    "After a curt bow and an offer to remove our plates, Lilly asks for the bill politely and softly."

    "With expert coordination, he maneuvers around the tables, our plates in hand, to retrieve our bill from the kitchen behind the double doors."

    "…"

    "In no time he reappears through the doors, smartly handing our bill to Lilly."

    "…Who promptly hands it to me, causing him to raise an eyebrow."

    "As I read the small computer-printed leaflet, the number of zeroes in the total cost is mind-boggling."

    li "Hisao?"

    hi "Uh… oh… uh…"

    "I quickly stammer out the amount, to which Lilly merely nods and reaches for her purse."

    "Giving her card to the waiter, he disappears to go into the kitchen once again."

    hi "That was a lot of money, to state the obvious."

    "The statement seems to make Lilly slightly uncomfortable."

    li "This is… another vestige from that world."

    li "Along with my education, my parents are quite forthcoming with finances."

    hi "They're fine with you spending that much?"

    li "Usually I'm not quite so luxurious with my spending, though they can well afford it in any case."

    li "I dislike throwing money about, but this one time I think I can make an exception."

    hi "You know, this is a travesty of my gentlemanly mindset."

    li "Hmm?"

    hi "Not only did you choose our first date, but you paid for both of us as well."

    hi "And for the rental of this suit, mind."

    "I take the bridge of my nose in my fingers and I grin in amusement."

    hi "You've set one hell of a bar to reach, Lilly."

    "She gives a small giggle."

    li "I'll look forward to it, Hisao."

    hi "Wait… you're not gonna hold me to that, are you?"

    "She warm smile makes me grimace."

    hi "Oh god."

    "The waiter reappears beside us, as if by magic, and hands Lilly's card back to her."

    "Leaving, he exercises a measure of diplomacy as he avoids questioning me on my maudlin expression."

    "Clapping my hands together to banish the thought, I take a deep, refreshing breath."

    hi "Shall we be off, m'lady?"

    "We both stand and step from our chairs, Lilly offering her hand and I taking it."

    li "Lead on, sir."

    # Timeskip

    # Completely gratuitous use of the performance dress, GO

    "As we step into Lilly's room, Lilly practically falls onto her bed as I remove my tie and begin unbuttoning the suit jacket for some much-needed air."

    li "We're… back!"

    "Lilly brings her arms out wide before flopping messily onto the bed."

    li "That was tiring…"

    hi "Doubly so for me."

    "She tilts her head, facing vaguely in my direction."

    hi "You didn't have to contend with having been nearly assaulted in the shower."

    li "…Ah."

    "She takes a moment to remember the event before giving another of her small, devilish grins."

    li "You enjoyed it though, didn't you?"

    "I open my mouth to reply, but suddenly realise that she's perfectly right."

    "On the one hand, it was entirely unsolicited."

    "But on the other… it was pretty darn good."

    hi "Got me there. I'll just have to make sure I take you the next chance I get."

    "Lilly takes a second to snuggle her head into her pillow before facing me."

    li "You missed your chance, Hisao. I've taken the lead once again."

    "A pause."

    "As a devilish grin spreads over Lilly's face, even my admittedly naieve mind clicks."

    "No man nor god could stop me as I walked towards the woman on that bed, quickly casting my clothes to the floor."

    "I lower my lips to hers, her hands coming around my head and feeling the back of my hair."

    "As our tongues begin to lap, my hands begins to wander down her side and between her legs."

    "The smoothest touch is enough for her to breathe deeply."

    "As I draw my face back, her her hands remain on my now flushed, sweaty cheeks."

    "Her black pupils, set within those deep sapphire eyes, are visibly dilated from lust."

    "She slowly pushes herself up, moving backwards until her back is against the wall."

    li "Hisao…"
    
    return

label en_L34h:

    "As her hand ventures downwards, I can easily see her hand moving inside white panties as she begins to rub herself."

    "All I can do is gulp and stare as she lets herself give in to the pleasure enveloping her."

    hi "Lilly, I…"

    "A shuddering breath emanates from her, the white of her panties visibly wettening."

    li "Hisao… mmm…"

    "My hips begin to squirm slightly from the excitement, but by the barest of margins I avoid joining her in the activity."

    "To say I'm on a wire trigger due to the arousement is understating things."

    "Her eyes opening and facing directly at me, she removes her panties to reveal her wet self."

    "It takes every ounce of restraint to avoid pouncing on her there and then."

    "Beginning her rubbing anew, her other hands tightly grips the sheets of the bed as her excitement grows with each motion."

    li "Hisao… Hisao…"

    "As her moaning slowly grows, I can't hold myself back from her erotic display any longer."

    "A quick crawl across the bed is all that's needed before I lock my lips with hers, our tongues lapping."

    "With my hands slipping behind her back, I gently move her woards me as I sit, her head level with mine as my eyes stare into hers."

    hi "Lilly…"

    li "I want you, Hisao."

    "With a long breath, she lowers herself onto me, her hands reaching across my back."

    "Slowly but surely, I feel her soft, warm body envelop me."

    "For a moment her body tenses, but it soon softens once again."

    hi "Lilly, I love you."

    "She smiles back warmly as she nods."

    "Slowly but surely, she begins to move herself up and down, her hips seemingly drawing me in further with each thrust."

    "With her mouth just inches from mine, I can hear each lustful breath that comes with each motion."

    "The feeling inside of her, her smell, those small beads of sweat… I want all of them."

    "My mouth quickly finds hers, our tongues locking and twisting as our bodies remain locked in their erotic embrace."

    "This girl… this woman… I love and feel her as much as I can."

    "As our mouths break, a slight tremble in my thighs begins as I try and hold myself back."

    hi "Lilly… I…"

    "Her soft moaning draws me even closer to bursting point."

    hi "Lilly…"

    li "Please, Hisao… Mmm…"

    "I can't… hold on… any longer…!"

    hi "Lilly… Ahn… Ahhhh!"

    li "Hisa… Ah—Ahhhhh!"

    "For a second, both of us remain locked in orgasm clutching each other tightly."

    "In all too short a time, though, our bodies relax as we hold ourselves to each other tightly."

    return

label en_L34x:

    "With the fatigue of the day's events on top of the sex, both of us take more than a few moments to regain lucidity."

    li "Hisao…"

    "As her smiling, tired face stares at mine with unseeing eyes, I gently close mine and give a small kiss."

    return

label en_L35:

    scene bg school_dormlilly_ni
    with openeye
    
    play sound sfx_alarmclock

    centered "*beep* *beep* *beep* *beep* *beep*"

    "Ugh, where the hell do I turn this thing off?"

    "I flail my arm out to the side as I lay on the bed, half-asleep as I try to restrain the blaring alarm."
    
    play sound sfx_alarmclock
    
    "Clock" "It is… six… thirty-one… in the… morning."

    "The damned thing must say the time so blind people can use it. Great."

    "Another round of banging on the top of the clock commenses in the search for the right button."

    "Eventually I chance upon the right one, the annoying sound vanishing as soon as it started."

    "Thank god for that."

    "Without another word, I return to sleeping while savouring the slight scent of Lilly beside me."
    with shorttimeskip
    
    scene bg school_dormlilly
    with openeye

    "Abuh…?"

    "I slowly lever myself off the bed, shielding my eyes from the sunlight that pierces through the altogether too thin curtains."

    "For once I feel quite refreshed. All the more so for waking up next to Lilly's sleeping (and very much bare) figure."

    "It's times like these that her lack of sight is slightly advantageous."

    "Compared to her snow-white, smooth skin, I look pretty darn plain."

    "Well, not really. Tall (which, considering Lilly's height, is a bonus) and weedy, I was teased at times in elementary school for looking girly."

    "Eugh. Damned memory."

    "I quickly shake my head to force the images out."

    "I do wish memory weren't quite so strange in how it works. The fact that it seems only bad memories seem to surface quite so randomly is all the worse."

    "Another bad memory, though one much more urgent, comes to the fore as my morning grizzling slowly wears off."

    "My pills, where the hell did I put my pills!?"

    "I quickly duck off the bed and slip on my underwear from the pile of clothes haphazardly strewn in the middle of the floor."

    "Now… I put them in my suit…"

    "I quickly rifle through the jacket pockets, quickly moving to the slacks after turning up with only a few strains of dust."

    "Eventually, a small while bottle is to be found in the right pocket."

    "Phew."

    "As per normal, I tip the several daily pills I have to take in my hand and dry-swallow them."

    "As soon as I do, I hear a stirring coming from the bed."

    li "Hmm…?"

    play sound sfx_impact
    
    centered "*THUD*"

    "Followed by a loud thump."

    "As I quickly turn around, I see Lilly slowly getting back up as she uses the bedstand as an aid."

    show lilly behind_sleepy_nak
    with charaenter
    
    hi "You okay, Lilly?"

    "She looks at me with a dazed face, very slightly swaying as she stands."
    
    show lilly behind_reminisce_nak
    with charachange
    
    li "I'm okay…"

    hi "Are you… even awake?"

    show lilly behind_sleepy_nak
    with charachange
    
    li "I think so. Maybe. Am I?"

    hi "I have my doubts."

    "She shakes her head in an attempt to wake herself up, an act which seems to work."

    extend "Somewhat."

    "I'd probably be able to better guage the fact if I weren't ever-so-slightly distracted by the effect that shaking herself had on her chest."

    hi "You're really not a morning person, are you?"
    
    show lilly behind_pout_nak
    with charachange

    "She barely summons the energy to shake her head sullenly."

    show lilly basic_reminisce_nak
    with charachange
    
    li "Could you give me the pills in the top… right, I think… drawer?"

    hi "Wait, you take pills as well?"

    "She looks slightly confused at my own confusion."
    
    show lilly behind_pout_nak
    with charachange
    
    li "Birth control pills."

    hi "Oh."

    "A small lightbulb goes off in my head."

    hi "…Oooooooh."
    
    show lilly behind_emb_nak
    with charachange

    "She pauses for a second, trying to take measure of my response."

    show lilly behind_pout_nak
    with charachange
    
    li "Did you think we were…"

    hi "Well… I… uh…"

    "I feel pretty stupid right now."

    "Sighing at my complete lack of foresight, I look back to her."

    hi "At least one of us was on the ball."
    
    hide lilly

    "Grimacing past her look of disapproval, I turn and open the top right drawer, as per her instructions."

    "Sure enough, there's a small packet of pills in there."

    hi "How many?"

    li "Two."
    
    play music music_another fadein 10.0

    show lilly behind_sleepy_nak
    with charachange
    
    "As she slowly walks over, still slightly dazed from the tremendous effort of waking up, I take her hand and guide her over."

    "After placing the pills in her hand, she fills a glass with water and takes them with a mouthful of the clear liquid."

    hi "You can't dry-swallow?"
    
    show lilly behind_smileclosed_nak
    with charachange
    
    li "It's not safe to do that. You'll end up choking if you get one stuck in your throat."

    hi "Yes, mother."
    
    show lilly behind_weaksmile_nak
    with charachange

    li "Good, good."

    "Far from being insulted, she simply smiles and pats my head playfully."

    hi "You know…"
    
    show lilly behind_smile_nak
    with charachange

    li "Hmm?"

    hi "As much as I like seeing you naked, aren't you kind of cold like that?"
    
    show lilly behind_pout_nak
    with charachange

    "She takes a moment to ascertain whether she is, in fact, cold."
    
    hide lilly

    "Evidently coming to a conclusion, she gives a nod and quickly skips over to where her school clothes are hanging."

    stop music
    
    "Wait a moment…"

    "Where her school clothes are hanging… "

    extend "School clothes… "

    extend "School!"

    hi "Wait, what time is it?"

    li "Oh, um…"

    show lilly behind_emb_nak 
    with charaenter
    
    "She reaches across and taps the top of her clock."

    "Clock" "It is… one… o'clock… in the… afternoon."

    "Both of us freeze."

    hi "Well, uh… I wasn't really in the mood to go to school today anyway. You?"
    
    show lilly behind_smileclosed_nak
    with charachange

    li "Arriving this late would cause more fuss than simply skipping the day."

    hi "Well then, that's easily settled."
    
    hide lilly

    "As I take a moment to watch Lilly as she begins dressing, it comes to my attention that I'm barely more dressed than she was."

    hi "Hang on, I need to go get my clothes too. I'll skip over to my dorm room in the suit and grab my school stuff."

    li "Okay. I'll prepare some tea in the meantime."

    "I quickly whip on the slacks and a shirt, giving Lilly a quick kiss on the way out."

    scene bg school_dormlilly
    with shorttimeskip
    
    play music music_friendship fadein 10.0 
    
    hi "I'm home, honey."
    
    show lilly basic_smile 
    with charaenter

    li "Welcome back, Hisao."
    
    show lilly basic_smileclosed at centersit
    with charamove
    with Pause(1.0)
    
    show lilly basic_smileclosed at center
    with charamove
    
    "She gives a perfect sitting bow, the table next to her having two steaming teacups placed on it."

    "From the color alone I can tell that mine's coffee, as opposed to her rich, black tea."

    "Having changed into my school clothes in my dorm, I neatly fold the suit and place it over the desk before sitting down opposite her."

    "As expected, the coffee's just to my liking as I gently take a sip."

    hi "Thanks, Lilly."

    show lilly basic_smile at center
    with charachange
    
    li "It's no trouble. Tea and coffee are quick to make."

    hi "Not just for the tea and coffee. For actually covering for our… bedroom shenanigans."

    show lilly basic_giggle at center
    with charachange
    
    "She gived a short giggle, amused by my choice of words."

    li "While I'd like to eventually have children, it'll be a while before the time is right."

    hi "Somehow, I'm not surprised."

    "That goes for both her wanting children, and her frankness on the subject."

    "Thankfully, I've become used to it by now."

    show lilly basic_satisfied at center
    with charachange
    
    li "Have you ever entertained the idea of having a family?"

    hi "Hmm…"

    "I lean back, taking a moment to get my thoughts in order."

    hi "I don't know about a family, but I guess I like children."

    show lilly basic_smile at center
    with charachange
    
    li "I could see you getting alone well with children."

    "We both give a small lighthearted snort to brush away the seriousness of the discussion."

    "After a few small sips of out respective teacups, I decide to follow on the general subject."

    hi "What were you wanting to do as a job, anyway?"

    show lilly basic_smileclosed at center
    with charachange
    
    li "I've quite liked the idea of becoming an English teacher, one day."

    "Likes children, check. Great English skills, check. Good leader, check."

    hi "Something tells me you'd make a great English teacher."
    
    show lilly basic_smile at center
    with charachange

    li "What of yourself?"

    "I guess this is where the line of discussion would inevitably lead."

    "For once, though, I know what to say."

    hi "I don't think about the future much."

    show lilly basic_surprised at center
    with charachange
    
    li "Really?"

    "I lean back once again, gently placing my teacup on the saucer."

    hi "I used to know a friend. Before my heart attack, I got to know him pretty well."

    hi "He was into planes. Loved them, even. Pretty much any kind of plane you can imagine entralled him."

    hi "Every time he heard a plane passing, he'd go over to a window to try and catch a glimpse of it."

    hi "Two guesses as to what he wanted to be when he graduated."

    li "A pilot?"

    hi "Yeah. In the JSDF."

    hi "His dream was to soar through the air in a fighter jet."

    li "How is he going with getting to his goal?"

    hi "Well…"

    hi "Let's just say Yamaku isn't the only school with students that are wheelchair-bound."
    
    show lilly basic_sad at center
    with charachange

    "Lilly's smile of wrapt curiosity fades instantly."

    li "Oh. I… see."

    show lilly basic_oops at center
    with charachange
    
    li "How did he…?"

    hi "A disease. One which will eventually kill him, whether it be months or years ahead."

    hi "He stopped thinking about the future, after that. Instead, he concentrated on the time where he was."

    hi "From then until now, he studied hard, and got great grades. He discovered other talents, but didn't really think about how to apply them."

    hi "Because he feared that once he set his sights on something, it would just be snatched away once again."

    "Silence falls."

    show lilly basic_listen at center
    with charachange
    
    "As Lilly takes her turn to collect her thoughts, she picks her words with particular caution."

    show lilly basic_oops at center
    with charachange
    
    li "To live life without looking forwards… isn't that kind of sad?"

    hi "How so?"
    
    show lilly basic_smile at center
    with charachange

    li "Well, to continue using an odd metaphor for me, looking out the side windows of a car is nice to see the scenery."

    li "But the reason you're in the car is to get somewhere, and only by looking forwards can you see where you're going."

    li "While the scenery may be pretty, your destination is where you'll find those that''ll be with you after the journey's end."

    li "At least, that's my take on it."

    "Another silence."

    hi "You know, that's a pretty weird analogy for you of all people to use."
    
    show lilly basic_smileclosed at center
    with charachange

    li "Well, it's the one I had given to me."

    li "Come to think of it, I'm surprised it had any effect at all."
    
    show lilly basic_giggle at center
    with charachange

    "We both share a round of laughter."

    "I suspect, though, that mine is a measure less genuine than hers."
    with shorttimeskip

    "Before long, our teacups lay empty."

    hi "I'd better be getting back before the other students start getting back to the dorms."
    
    show lilly basic_smileclosed at center
    with charachange

    li "I suppose it's best not to provoke any more fuss than we already have."

    hi "I can't imagine our teachers appreciating us skipping class if rumours start flying, either."

    "I pick myself up with a slight grunt, giving Lilly an affectionate kiss on the forehead before stepping to the door and opening it."

    show lilly basic_satisfied at center
    with charachange
    
    li "See you tomorrow, Hisao."

    hi "Seeya."
    
    hide lilly

    scene bg school_girlsdormhall
    with locationchange
    
    "As I step out into the hallway, Lilly's voice bring my head inside once more."

    show lilly basic_listen at center
    with charachange
    
    li "Oh, Hisao?"

    hi "Yeah?"

    li "What was your friend's name?"

    hi "…"

    hi "Shin. Shin Kuzuhara."

    show lilly basic_smileclosed at center
    with charachange
    
    li "I see. I'd like to meet him some day."

    li "Goodbye, Hisao."

    hi "'Bye."

    "With that, I close her sturdy, wooden door."

    "I'm sorry, Lilly."

    "I'm really, really sorry."

    scene black
    with dissolve
    
    return

label en_L36:

    scene bg school_library
    with openeye
    
    play music music_daily fadein 10.0

    "As I wake up from a midafternoon nap, seized during a quiet moment in the library, I silently curse to myself."

    "Truth be told, the library is one of my favourite places in the entire school."

    "Quiet, with plenty of reading material and usually almost completely devoid of other people. Practically a paradise."

    "Exams have a habit of changing student's behaviours, though."

    "Right now, students are busy studying and quietly discussing amongst themselves, lending the area an ambient rabble of chatter."

    "Well, I guess I shouldn't complain."

    extend " This could be considered my penance for skipping school yesterday."
    
    show lilly back_smileclosed at right
    with charaenter

    "That aside, Lilly's introduced me to the braille section of the school library, and is currently sitting beside me with her long, pale finger slowly scanning the small bumps on a pure white page."

    "I'm surprised just how many times I'd walked past it without taking any notice whatsoever."

    "I guess, since there weren't any titles visible on the books, I just cruised on by without them grabbing my attention."

    "I have a suspicion whatever book she's reading is far more interesting than mine."

    hi "What're you reading?"

    show lilly back_smile at right
    with charachange
    with Pause(0.5)
    
    show lilly basic_smileclosed at right
    with charachange
    
    "She opens her eyes and turns to me, very nearly making eye contact."

    "It took a while, but I'm starting to pick up on her (admittedly very minor) slipups in covering over her blindness."

    li "A maths textbook."

    hi "…Ah. You doing any better than before in it?"

    show lilly basic_pout at right
    with charachange
    
    "She visibly deflates, communicating the message well enough."

    "Not wanting to press the topic, I decide to change the subject to one that I'm slightly curious about."

    hi "How do you read maths anyway? I know about braille, but isn't that just for letters and numbers, and not fractions or anything?"

    show lilly basic_ara at right
    with charachange
    
    li "Well, braille's quite malleable."

    show lilly basic_smile at right
    with charachange
    
    li "I guess the best analogy would be letters. “X” can mean a letter, or a variable. Likewise, “A” in braille can be used to represent different things."

    hi "There's still a lot of symbols to account for, though."

    show lilly basic_smileclosed at right
    with charachange
    
    li "Well, yes. In the end, mathematics wasn't developed for the blind. The best we can do is mould both braille and audio to suit the task."

    hi "I guess that wouldn't help learning it, either."

    show lilly basic_smileclosed at right
    with charachange
    
    li "Yamaku teachers have experience in teaching the blind, so the barrier isn't as high as usual."

    li "I just have trouble grasping the more advanced concepts we cover, then get even more lost as the class moves ahead using those techniques."

    hi "Well, I guess we can't be good at everything."

    show lilly basic_listen at right
    with charachange
    
    "As she moves to open her mouth, she freezes for a second, listening."

    show lilly basic_concerned at rightsit
    with charachange
    
    "It's not long before she sits back in her chair and grimaces."

    hi "What's wrong, are you feeling sick?"

    stop music fadeout 1.0
    
    li "No, but I think I will be in a few moments."

    "Raising an eyebrow, I look to the door."

    "Bright, curly hair pokes through the doorframe before the person's face or body, but it's all too obvious who it is."

    play music music_shizune
    
    show misha hips_grin at left
    with charaenter
    
    show shizu adjust_happy at twoleft
    with charachange
    
    "Sure enough, Misha and the everpresent Shizune appear through the entrance. I really do wonder if those two ever part."
    with Pause(1.0)
    
    hide misha
    
    hide shizu
    
    "It honestly wouldn't surprise me if they stayed together even after class."

    "From class, to the dorms, even into the…"

    li "Oh dear."
    
    show lilly behind_displeased at right
    with charachange

    "Lilly's voice stops my overactive imagination in it's tracks."

    hi "What's up?"

    li "Misha's eating something, isn't she?"

    show lilly basic_surprised at right
    with charachange
    
    "Looking back to the counter at the entrance, the two've been stopped by a very irate librarian who's altogether too far away for me to hear."

    "She never fails to remind anyone, through obnoxious posters or scoldings, that the library is her turf. She displays a remarkable lack of enthusiasm when asked anything, too."

    "I think most, even amongst the staff, silently wish that she'd just take her retirement money and go."

    "Looking back to Misha, a small white stick is visible poking out of her mouth."

    hi "Yeah, a lollipop."

    "We both continue to observe the situation playing out in each of our ways."

    "The librarian scolds her, Misha makes a pouting face and Shizune sighs. The same routine plays out repeatedly for minutes on end."

    "It eventually comes to a startling conclusion as Misha gulps the entire lollipop, stick and all, into her mouth."

    "The librarian and Shizune look as shocked as we do."
    
    show lilly basic_pout at right
    with charachange

    li "Did she just suck the whole thing in?"

    hi "Yup. The whole thing."

    show lilly basic_oops at right
    with charachange
    
    li "All of it?"

    hi "All of it."

    "After a couple of seconds, her cheeks move before spitting out the bare stick."

    "Shizune hides her face in her hands as the librarian gives up and frantically tries to wave them on."

    "Surprisingly, the two make a beeline for the two of us as soon as they pass the librarian checkpoint."

    show lilly basic_listen at rightsit
    with charamove
    "Lilly slinks down in the chair as she hears the two's footsteps approaching."

    show misha hips_grin at left
    with charaenter
    
    show shizu basic_normal at twoleft
    with charaenter
    
    mi "Hey Hicchan~"

    hi "Misha?"
    
    show misha hips_smile at left
    with charachange

    show shizu behind_blank at twoleft
    with charachange
    
    mi "What is it?"

    hi "Don't ever do that again."

    show misha hips_frown at left
    with charachange
    
    mi "But why, Hicchan~?"

    "She puts her hands on the desk, leaning over."

    "The battle between my testosterone and my brain over the control of my eyes is pitched."

    show misha perky_smile at left
    with charachange
    
    show shizu behind_fron at twoleft
    with charachange
    
    hi "That is a dirty, dirty tactic. I swear there's something in the Geneva Conventions about that."

    show misha sign_confused at left
    with charachange
    
    mi "Gehova what?"

    hi "…Nevermind."

    show shizu basic_frown at twoleft
    with charachange
    
    "Shizune taps her foot extra hard, to make sure the thick carpet doesn't drown out the noise."

    show misha sign_smile at left
    with charachange
    
    show shizu basic_normal at twoleft
    with charachange
    mi "Oh, yes, uh, Lilly?"

    "Seeing Misha taken off balance like this is both amusing and curious. Even the paper-thin grin the adopts is a pretty obvious facade for her discomfort."

    show lilly basic basic_displeased at right
    with charachange
    
    li "The class attendance?"

    "Misha nods, taking a second to realise that such an affirmation is lost on Lilly."

    show misha hips_grin at left
    with charachange
    
    show shizu behind_blank at twoleft
    with charachange
    
    mi "Yup! That's what we need."

    li "Aoi Yamada will have it. I was away yesterday, so she'd have the attendance sheet in my place."

    show shizu behind_frustrated at twoleft
    with charachange
    
    show misha sign_smile at left
    with charachange
    
    "Shizune's forboding look of disapproval becomes all the more pronounced as Misha grins."

    mi "Really? Hicchan was away yesterday too! What a coincidence~"
    
    show shizu basic_happy at twoleft
    with charachange
    
    show lilly basic_emb at right
    with charachange
    
    show misha sign_smile at left
    with charachange

    "I silently shake my head, trying to veto this line of discussion without Lilly's notice."

    "…"

    "No dice. Misha's playful teasing knows no bounds, and Shizune isn't exactly prone to allowing excesses like this."

    "As I think of how to defuse the situation, something I heard once comes to mind."

    "'If a situation becomes uncomfortable, making it absurd will at least allow you to laugh about it.'"

    "Steeling myself for whatever may happen next, I calmly stand and push my seat back."

    "As simple as can be, I walk up to Shizune, carefully pick the glasses off her head, and place them onto Lilly."

    "Content with my work, I simply take a step back and let the situation play itself out."

    # Sprite changes

    "…"

    "…"

    "…"

    mi "Bwuhahahahaha!"

    "She only indication of Shizune's cool exterior having been dented is the very much audible tapping of her fingers on the desk."

    "Even Lilly, usually calm and composed, sits looking entirely lost at what this strange, foreign object is doing on her face."

    "Taking a deep sigh to calm herself, Shizune reaches out and retrieves her glasses from Lilly's face."

    "As Misha collects herself, she and her other half quickly sigh to and fro."

    "As soon as the two are done signing, Shizune strides out of the library."

    "What was said is easily communicated by Misha, as she parrots Shziune's disapproval with a comically puffed-up and scowling face."

    hi "I thought it might have that effect."

    mi "Situation avoided! Good work, Hicchan."

    hi "I try my best. Have fun."

    mi "Bye Hicchan, bye Lilly."

    li "Goodbye, Misha."

    "With that, Misha bounces out with her trademark bubbling energy."

    "We both give a sigh of exhaustion as I take my seat once again."

    li "I assume you put Shizune's glasses on me?"

    hi "Yeah. The situation wasn't exactly comfortable."

    li "It could have become quite embarassing, yes."

    hi "No, not that. You and Shizune. You really have it in for one another, don't you?"

    "She rubs her temple, the mere recollection of Shizune irritating her."

    li "She can be insufferably harsh sometimes, to say nothing of her family."

    hi "You know her family?"

    li "It's… complicated."

    li "I wouldn't say I hate her, but… she makes things more difficult than they must be."

    "Thinking about the two as class representatives, the difference in their leadership styles really is striking."

    "While Shizune is the hard taskmaster who practically whips the class into submission, Lilly gains favour through charisma and soft-spoken diplomacy."

    "Yamaku, a perfect model of our oh-so-wonderful democracy. Who'd have thought?"

    li "Hisao?"

    hi "Yeah?"

    li "Did the glasses suit me?"

    hi "Not at all. I think they're best left on Shizune."

    li "I suspect that might prove safer in the long run, as well."

    "Picking ourselves out of our seats to go to our respective exams, we share a lighthearted laugh."

    scene black
    with dissolve
    
    return

label en_L37:

    scene bg school_dormlilly
    with openeye
    
    show lilly basic_smile_paj at right
    with charaenter
    
    show hanagown normal_blush at left
    with charaenter

    li "It's been too long since we had a tea party like this."

    hi "Mm, it is."

    "As we all take a sip from our respective teacups, I silently reaffirm her words."

    "The two really do look lovely, to say the least."
    
    show hanagown normal at left
    with charachange

    ha "I've never seen you in your pajamas before, Hisao."

    show lilly basic_smileclosed_paj at right
    with charachange
    
    hi "When in Rome, do as the Romans, they say."

    show hanagown smile at left
    with charachange
    
    ha "They look nice."

    hi "Ah, thanks."

    "I could say the same for both of them, really."
    
    show lilly basic_weaksmile_paj at right
    with charachange

    li "Sorry, you'll have to excuse me for a bit."

    hide lilly 
    with charaexit
    
    "With a small nod, she stand and walks to the bathroom."

    "I can't help but stare as she navigates the room entirely unaided, as naturally as if she could see."
    
    show hanagown worry at left
    with charachange

    "As I turn back, I see Hanako staring at me as if I were a bug under close examination."

    hi "Y… Yes?"

    show hanagown smile at left
    with charachange
    
    "Her side smile takes me entirely off guard."

    ha "Thank you, Hisao."

    hi "Thanking me without telling me what for… you're starting to sound like Lilly."

    "She gives a small giggle before continuing."

    show hanagown smile_blush at left
    with charachange
    
    ha "It's just that… Lilly seems happier now. And I'm happier, too."

    "I feel my cheeks becoming flushed as she looks at me."

    show hanagown distant at left
    with charachange
    
    ha "I wasn't sure if I wanted you and Lilly to be together, to be honest."

    hi "Really?"
    
    show hanagown normal at left
    with charachange

    ha "Mm. Lilly had cared for me for so long, I'd grown dependant on her."

    show hanagown_distant at left
    with charachange
    
    ha "But she had to lead her own life, and I had to lead my own."

    show hanagown smile_alt at left
    with charachange
    
    ha "That's why I have to thank you, Hisao."

    "She gives a small nod to herself, seemingly happy with her choice of words."

    "I take a sip of tea as I mull over what she said."

    "In my time with Lilly, we'd maintained contact with Hanako, but little more."

    "Nonetheless, she didn't seem to have a problem with it. I guess this just confirms what I'd suspected."

    "She's grown."

    hi "How's the teaching going for the sound system?"

    show hanagown normal at left
    with charachange
    
    "After a second's thought on what I'm referring to, she clicks."

    show hanagown smile at left
    with charachange
    
    ha "It's going really well. Aoi's nice, and she really wants to learn."

    hi "Good to hear."

    play sound sfx_dooropen
    
    show lilly basic_smile_paj at right
    with charaenter
    
    "The door to the bathroom opens behind us, Lilly coming through and taking her seat once again."

    show hanagown normal at left
    with charachange
    
    ha "Well, I'd better be going."

    show lilly basic_oops_paj at right
    with charachange
    
    li "So soon?"

    ha "Curfew would be coming up soon."

    show lilly basic_weaksmile_paj at right
    with charachange
    
    li "Very well. Good night, Hanako."

    show hanagown smile at left
    with charachange
    
    hi "'Night."

    "She stands and gives a nod in farewell before leaving."

    hide hanagown
    
    "And then, it's just us."

    show lilly basic_smile_paj_close at center
    with charamove
    
    li "It seems she's coping well. I'd been worried, but she's becoming more outgoing."

    hi "Yeah. She's doi— {w=.5}{nw}"

    "As I suddenly wonder how in the world she'd know, I sigh and hang my head in realisation."
    
    hi "I can never get used to the freakish sense of hearing you have."

    show lilly basic_giggle_paj_close
    with charachange
    
    "She giggles, taking pleasure in taking me quite so off-guard."

    show lilly basic_cheerful_paj_close
    with charachange
    
    li "It does prove useful, on occasion."

    show lilly basic_smile_paj_close
    with charachange
    
    li "Though, to more immediate matters…"

    "Her voice becomes overly accusative."

    show lilly basic_satisfied_paj_close
    with charachange
    
    li "I assume there is a reason for you staying past curfew?"

    li "And, at that, another reason for you to arrive in your pajamas?"

    hi "Get your mind out of the gutter, girl."

    show lilly basic_giggle_paj_close
    with charachange
    
    "My attempt at channeling Akira comes off surprisingly well."

    show lilly basic_smile_paj_close
    
    li "I assure you, I'm only joking."

    hi "Well, I wouldn't mind sleeping in your room tonight. That is, of course, if you have no objections?"
    
    show lilly basic_ara_paj_close
    with charachange

    li "My my, Hisao, my room is open to you whenever you wish."

    hi "Thanks."

    "I pick up the teacup to take another sip, though look down to find it empty."

    "Giving up on the prospect of, heaven forbid, any more tea than I've already had, I lean back on my arms."

    hi "You know,"

    show lilly basic_surprised_paj_close
    with charachange
    
    li "Hmm?"

    hi "I really don't know if I've got enough energy to keep up with you."

    show lilly basic_ara_paj_close
    with charachange
    
    li "Shall I make an effort to temper myself?"

    hi "Please do. Not that I exactly mind it, though."

    "I give a deep yawn, the time having been marching along."

    hi "Well, at least I can handle this kind of exercise."

    show lilly basic_smile_paj_close
    with charachange
    
    li "Hmm?"

    hi "I can't really go doing any real running or lifting. My meds can keep up with this kind of thing, though."

    show lilly basic_reminisce_paj_close
    with charachange
    
    li "Ah…"

    "She looks away, suddenly downcast."

    show lilly basic_sad_paj_close
    with charachange
    
    li "I'm sorry, Hisao. I…"

    hi "No, don't. Not for this. I won't let you apologise."

    show lilly basic_oops_paj_close
    with charachange
    
    li "But…"

    "I reach forward and take one of her hands in mine, gripping it tightly."

    hi "I won't let you apologise any more for my problem. Not once, not ever."

    "My grip tightens."

    hi "I won't let this get between us. Ever. Don't treat me differently because of it."

    hi "I…"

    "I suddenly realise my grip on her hand's visibly whitening it."

    "Releasing it as if it had scalded my skin, I look at her pensively."

    hi "Ah… sorry."

    show lilly basic_emb_paj_close
    with charachange
    
    li "N—No. It's… okay."

    "We both take a moment to calm ourselves."

    "Just where the hell did that come from?"

    "As Lilly takes a sip of tea, her face suddenly scrunches up."

    show lilly basic_pout_paj_close
    with charachange
    
    li "I believe the tea has gotten cold."

    "I bury my face in my hand and laugh, though as I look back up, her smile is weaker than before."

    show lilly basic_weaksmile_paj_close
    
    li "Hisao?"

    hi "Yeah?"
    
    show lilly basic_concerned_paj_close
    with charachange
    
    li "How do you… deal… with it?"

    "She clenches her teeth, unsure of whether she should have said what she did."

    "I'm not even sure of how to answer her."

    "I guess…"

    hi "I just never gave it too much thought, really."

    hi "I mean, I thought about it while I was in hospital after the heart attack, but I never really came to a conclusion."

    hi "It's not like there's really that much to say about it. No matter what I think to myself, I'm still going to be like this."

    hi "I just accept my lot and get on with it, I suppose."

    show lilly basic_displeased_paj_close
    with charachange
    
    "She nods, though her sullen expression doesn't waver."

    "Silence."

    "I sit and watch her intently, oberving her reaction."
    
    show lilly basic_pout_paj_close
    with charachange
    with Pause(1.0)
    
    show lilly basic_displeased_paj_close
    with charachange

    "As she opens her mouth to answer, she seems to think better of it and closes it again."

    hi "Lilly, what…"
    
    show lilly basic_smileclosed_paj_close
    with charachange

    "She closes her eyes and leans forwards, putting her hand to the side of my face and pressing her lips to mine."

    "As she pulls back, she gives a warm smile and lightly rubs her fingers on my cheek."

    show lilly basic_smile_paj_close
    with charachange
    
    li "I love you, Hisao."

    hi "I love you too, Lilly."

    "For a few moments, I take her hand in mine before she withdraws it."

    li "Would you give me a hand cleaning up?"

    hi "Of course, madame."

    scene black
    with dissolve

    return

label en_L38:

    scene bg school_scienceroom
    with shorttimeskip
    
    play music music_daily fadein 10.0

    "The end of an era is upon us."

    extend " That is, the era of exams."

    "The mood of the class has been changed from stressed depression to longing for the summer holidays. At just over a week away, they're well within eyeshot."

    "To speak of the class from such a third-person perspective is slightly misleading, though."

    "Exams are far down the list of things I like about school, and the prospect of spending the summer with Lilly is a wonderful one."

    "That, and finally meeting my parents again after so long being out of touch with them."

    "A phone call here and there is no subsitute for real contact. At least, that's the way I've come to think after arriving here."

    "Mutou's voice brings me out of my little reverie."

    mu "Nakai, could you solve the question on the board?"

    "I promptly stand and take a glance at it."

    "As expected, it's reasonably easy, only requiring a series of wrote steps to be solved."

    "As I open my mouth though, my throat squeezes shut."

    hi "Ah, i—it—{nw}" #reminder for the potential {nw} break

    "Pain."

    extend " Pain."

    extend " Pain. Pain. Pain. Pain. Pain."

    "My legs give way underneath me, leaving me only enough time to quickly brace myself on my desk."

    with vpunch

    mu "Nakai!?"

    "As the pain subsides, I lever myself back and and open my eyes."

    "As I feel the eyes of everyone in the class drilling into me, I silently rue the timing my body just had to choose."

    hi "I'm okay."

    "Mutou takes the bidge of his nose in his fingers for a second, assessing the situation."

    mu "Nakai, I think it'd be better for you to skip this lesson. It's nearly the end of the day anyway."

    mu "Hakamichi, please help him to the nurse's office."

    "As she gives a silent nod to him, we leave the class together and enter the halls."

    scene bg school_hallway3
    with locationchange

    "The silence is unbearable."

    "Expected, but unbearable."

    "Eventually my patience wanes, and I give Shizune a gentle tap on the shoulder."

    "Holding my hand flat and gesturing as if I were writing on it, she easily takes the cue and hands me a notebook and pen."

    "I quickly scrawl as we walk, the motion making my already scruffy handwriting somewhat scruffier."

    # Note

    $ written_note(u"Thanks, Shizune. This doesn't happen often, I assure you.")

    "She takes the note and looks at it, writing her reply in another notebook that she produces from her pocket."

    # Note

    $ written_note(u"Your handwriting has become slightly better.")

    "As I look up to her, raising an eyebrow, a small grin is written on her face."

    "She's not going to dwell on it. Thank God."

    # Note

    $ written_note(u"It's still far from as good as yours.")

    # Note

    $ written_note(u"Flirting will not get you anywhere.")

    # Note

    $ written_note(u"Just an earnest compliment. I'm surprised you took it otherwise.")

    "I can't help but grin at her pouting."

    "With a annoyed huff, she signals the end of our exchange as she slides her notebook back into her pocket."

    "I stretch to check for any pain left in my chest, though disguise it as being out of tiredness."

    "Thankfully, it seems to have been nothing more than a fleeting heart flutter."

    "Just another kick in the teeth at the worst possible time, I suppose."

    scene bg school_hallway3
    with locationskip

    "In short measure, we're standing in front of the nurse's office on the first floor."

    shi "…"

    "She lingers before leaving, giving a questioning smile."

    hi "I'll be alright, don't worry."

    "I smile widely, making sure that, even if my words don't reach her, my feelings will."

    "She nods and smiles, happy with the gesture."

    "With a quick wave, we see each other off as I enter through the open door."

    scene bg school_nurseoffice
    with locationchange

    "Hearing my footsteps, the nurse spins around in his chair as soon as I enter the room."

    nk "Ah, Hisao. Good to see you."

    nk "Or bad, I guess, considering that I'm a doctor."

    "He gives a small laugh, amused at his little joke."

    "A joke I suspect has been said more than a few times before."

    "He claps his hands together, evidently ready to Get Down to Business."

    nk "Alrighty, what brings you here?"

    hi "Uh, heart flutter. It happened during class."

    nk "Hmm, not good, not good at all."

    "He gestures for me to take a seat, which I gladly do."

    nk "This is the first since that incident a couple of weeks back, right?"

    "I give a nod."

    nk "What were you doing when that incident happened?"

    hi "I was walking, though it was pretty hot at the time."

    nk "And this time it just happened during class…"

    "He leans back in his chair, mulling over the mysterious case of the heart flutters."

    nk "Well, they may well be linked. If that's the case this definitely needs sorting out, and quickly."

    nk "The fact that this happened while you weren't doing anything overly physical is interesting, though."

    "Moving his lips from side to side to show he's thinking, he comes to a conclusion."

    nk "I'll have a talk with your doctor, but right now I suspect that they're due to different things."

    hi "Is there any immediate problem?"

    nk "Well, the fact that this happened without any warning or cause makes me think that your medication's side-effects might be the culprit."

    nk "Nonetheless, I want to keep a close eye on you for a while. Just to make sure things aren't going downhill."

    hi "Should I come in more often?"

    "He checks the calendar next to his computer, spinning back towards me after doing so."

    nk "The summer holidays are a bit of a pain considering the timing…"

    nk "Check with me next week and I'll run a few tests to make sure everything's sticking to the status quo. Otherwise, just take it easy."

    hi "What should I do for today?"

    nk "It's nearly time for school to be over, so you may as well just leave early."

    "He gives me a sly wink, making sure that I understand he's doing me a favour."

    hi "Well, doctor's orders. Thanks."

    nk "It's what I'm here for, after all. Don't do anything too strenuous for a while and you should be fine. Bye."

    "As I leave, he spins around and gets back to typing on the computer in front of him."

    "I suppose I'll just wait for Lilly by the gate."

    scene bg school_gate
    with locationskip

    "I don't have to wait long after the bell sounds out for Lilly to come into view."

    hi "Yo, Lilly."

    li "Ah, Hisao. Good afternoon."

    "We lean in and give each other a quick kiss before setting off down the road arm in arm."

    scene bg school_road
    with locationskip

    "The fact that we're pretty much exactly the same height is somewhat amusing."

    "While the old stereotype may be of the girl having to stand on her toes to kiss, it's all but unnecessary with Lilly's height."

    "Silence, blissful silence, is all that greets us as we slowly walk in the orange evening light."

    hi "Hey, Lilly?"

    li "Mm?"

    hi "Would you like to go on a date tomorrow? Just the two of us?"

    "Countering my rapidly beating heart, she simply smiles and nods."

    li "That would be lovely."

    hi "Where'd you like to go?"

    "She face suddenly changes to mock disapproval."

    li "You can't do that, Hisao. That's cheating."

    hi "Do what?"

    li "A gentleman should never ask a lady where to have a date."

    hi "Ah… oh."

    "Her smile quickly comes back, reassuring me that she's far from serious."

    hi "Hmm, suburbs then? We could grab a drink at the Shanghai."

    "An affirmative nod signals her approval of the plan."

    hi "Rightio then. If we leave in the afternoon we could catch Yuuko just before she finishes work, too."

    "As I say it, I remember the events of yesterday and the day before."

    hi "You think she knows about us?"

    "Her face falls into one of resignation"

    li "Knowing Akira, I have little doubt she will."

    hi "Well, at least she's not the type to tease us about it."

    li "To the contrary, I imagine she'll be quite pleased."

    "With an affirmative nod, I can't help but let my gaze linger on her."

    "The light of the waning summer's day illuminates her features, her blonde hair shining in the dying sun."

    li "It's unusual for you to be at the gate before I am. Our teacher dismisses us quite early on Fridays."

    hi "Mutou just ended the lesson earlier than usual. The end of the exams seem to have made him a bit less stressed."

    "As for the real reason that I'm here before she is… "

    extend "I think that question can go unanswered."

    li "Mmm."

    "She gives a simple nod and continues on."

    hi "I take it your exams are over as well?"

    li "Yes, they are."

    hi "Thank goodness. Exams are a pain."

    li "That they are."

    "We reach the store after only a short while, the rest of the walk passing in silence."

    scene bg school_road
    with shorttimeskip

    "Each carrying a bag, we emerge from the store and begin walking back."

    "Step, step, step."

    "Step, step, step."

    "Something's out of the usual."

    "Oddly tensed, Lilly's silence takes on a sharp edge."

    "Step, step, step."

    "Step, step, step."

    "For her to not say what's on her mind isn't like her."

    hi "Lilly, is something bugging you?"

    "She remains quiet for a couple of seconds before no longer being able to hold back."

    li "Liar."

    hi "Wh… what?"

    li "Hanako told me."

    hi "Told you what?"

    li "What happened in class today."

    "My mouth hangs slightly open as I try to form a response."

    "She saves me the bother of responding, though."

    li "Hisao, why didn't you tell me?"

    hi "I…"

    "As I start to try and fend her off, I realise she isn't angry with me, but sad."

    "To tell the truth, it hurts infinitely more."

    hi "I'm sorry, I…"

    li "Didn't want to worry me?"

    "She's got me."

    "I hang my head uselessly, genuinely regretful."

    hi "Right. That's right."

    "She clenches her teeth for a second, regaining herself."

    li "Hisao, you think of others too much."

    hi "Wait, what's that supposed to mean?"

    li "It means what I said."

    li "Please, Hisao… don't do that again."

    hi "…I won't. Sorry, Lilly."

    "She steps up to me, bringing her hand to my cheek."

    li "You know I love you, Hisao."

    hi "Yeah."

    "I give a smile as weak as hers as I take her hand in mine."

    scene bg school_dormhisao
    with locationskip

    "Ignoring the glaring Kenji as I passed through the dorm hall, I collapse on my bed as soon as I drop the groceries."

    "“You think of others too much.”"

    "What in the hell does she mean by that?"

    scene black
    with shuteye

    return

label en_L39:
    scene bg school_dormhallway
    with shorttimeskip

    "It's somewhat odd, really."

    "As I stand before Lilly's dormitory door, I can't help but reflect on how cold it is."

    "All morning I've been unable to get that single phrase out of my head."

    "“You think of others too much.”"

    "That touch of sadness, perhaps pity, that it was said with."

    "I'm about to see her for the first time since that awful moment, but right now all I can think about is this damned chill."

    "It irritates me. Immensely."

    "After realising I've been standing in front of her door for minutes on end, I finally rap my knuckles on it."

    centered "*thud* *thud* *thud*"

    li "Come in, the door's unlocked!"

    scene bg school_dormlilly
    with locationchange

    "As I gingerely open the door, the reason for her muffled voice becomes clear as the sound of her running shower echoes through the room."

    hi "Hey Lilly, it's just me."

    li "I guessed as such, I'll be out in a little while. If you'd like, you could make a coffee for youself."

    hi "Ah, sure. Want some tea before we leave?"

    li "Yes, please."

    "As I glance around, I notice the collected teaware and packets on the counter and get to work."

    "With a practiced hand, the two cups are made in no time, both steaming invitingly."

    "As I bring them both to the edge of the counter, I suddenly note the conspicuously absent noise of the shower."

    "I guess she must be getting getting dressed."

    "Leaning back and taking a sip of coffee from the badly-suited teacup, I look around the room."

    "As expected, it's the same beige as always."

    "Taking somewhat more careful note of my surroundings than last time, I note something partially surprising."

    "Whilst far from being able to be described as bare, she seems to keep her room immaculately clean."

    "The familiar music box I'd given her is given pride of place in the center of a shelf, flanked by numerous small dolls and teddy bears."

    "Gifts from Hanako and Akira, I'm guessing."

    "On the other side of the room, opposite her bed, is a bookcase all but full of reading material."

    "Two small piles of books, obviously bought after the shelves were filled, lie in front of it."

    "I guess there's a reason she scores so highly in school, but it makes even my reading habits seem tame."

    "As I take the last swig of my coffee, the shower door opens."

    "Lilly emerges in her usual shirt and skirt, her hair still slightly wet."

    "As soon as I open my mouth, the awkwardness of the situation hits home."

    hi "Uh… hey."

    "She gives a nod in my general direction, having worked out roughly where I am."

    "Leading her over by her hand, I guide her to the counter and the poured cup of tea."

    hi "Hey, Lilly?"

    "She lowers her teacup slightly."

    hi "About what you said yesterday…"

    "Placing the teacup back on the counter, she leans back against it."

    li "Everyone has their own pace. Don't worry about it."

    hi "Their own… pace? You've gone and lost me again, Lilly."

    "She gives a lighthearted giggle."

    li "I've always been amused at that part of your personality, Hisao."

    li "You're kind and intelligent, but… perhaps the best analogy would be an absentminded professor."

    "Her genuine smile's enough to see it's far from an insult. To be honest, it's pretty much exactly on the mark."

    "I am somewhat unobservant at times, I guess."

    "This isn't one of those times, though."

    "Silently, I reach over and take her teacup and sip the last remaining tea."

    "As she reaches for it, she finds herself grasping thin air."

    "Her utterly lost expression causes me to launch into laughter."

    hi "Hahahaha!"

    li "Hisao~"

    "Her pouting expression makes it all the harder to reign myself in."

    hi "Sorry. Ready to go?"

    "She gives a sigh, finding herself out of any avenue of retribution."

    li "Very well."

    "Taking each other's hands after a light kiss, we step through the door and into the cold afternoon air."

    scene bg school_road
    with locationskip

    "Walking down the street, much as we do every Friday, I can't help but feel the unusual chill of the breeze."

    "No doubt it'd be worse for Lilly, with her being in a skirt."

    hi "Damn."

    li "Hmm?"

    hi "I was kinda hoping it'd be warmer, considering it's our first real date."

    li "Well, we can't choose the weather."

    "Both of us sigh in unison, lamenting the cruel trick that summer played on us."

    li "I am pleased to see Hanako's confidence is gaining, though."

    "I guess she must be referring to yesterday's outing."

    "At the time she was pretty much letting herself go when on stage, even with people she'd hardly met watching her."

    "The idea of her doing such a thing when I'd first met her is outright impossible."

    hi "Yeah, she does seem to be getting better than she used to be."

    "She gives a deep nod."

    li "It seems what she needed was less, not more, care."

    li "After all this time of doting on her, it was only when she saw you with me that she changed."

    "A wave of regret seems to wash over her, almost seeming to try and hide her face."

    "I give her a sharp pat on the shoulder to pull her out of it."

    hi "Hanako was a wreck she came to Yamaku, you said that yourself."

    hi "Without you, god knows how she'd have been."

    "She nods, some measure of confidence returning."

    li "Thank you, Hisao. It's thanks to you that she's grown so much, though."

    hi "It's good to see she's becoming confident in herself, however long it may have taken."

    li "Indeed."

    scene bg suburb_roadcenter
    with locationchange

    "The welcome sight of the Shanghai looms in the distance as our discussion comes to an end."

    hi "The Shanghai's just up ahead. Want to grab a drink?"

    li "Mm, that'd be nice. Yuuko should be getting off work soon, too."

    hi "Perfect."

    "As we come to the front of the store, I open the door for Lilly and guide her in before I follow."

    scene bg suburb_shanghaiint
    with locationchange

    "As usual, it's empty. Bar, that is, for one person."

    yu "Welcome to our esta—" #reminder for the potential {nw} break

    yu "Ah, Lilly! Hisao!"

    "Her unusually wide smile puts me on edge."

    li "Good afternoon, Yuuko. I haven't seen you in a while."

    yu "That's okay! That's okay!"

    "Her overenthusiasm gives Lilly the same lost expression as mine."

    yu "Right this way, sir and madame~"

    "Okay, now this is getting creepy."

    "She bubbily leads us to the by now familiar table number twelve and promptly disappears behind the counter."

    "Leaning forward to Lilly, I keep my voice low."

    hi "What the hell's gotten into her?"

    li "Akira's told her. I'm sure of it."

    hi "…Ah."

    "As we sigh in resignation, Yuuko bounces around the corner of where she's gone to."

    "In her hands is a large cake, which she slides onto the table between us."

    "I can't help but notice the large “13” printed onto the middle of the cake with icing."

    hi "A cake?"

    "Lilly's face lights up with delight as she claps her hands together."

    li "Thank you Yuuko, this is lovely."

    "She gives a sharp, quick bow."

    yu "I heard you two were dating from Akira,"

    "Looks like Lilly was right."

    yu "So I brought a cake for you!"

    li "Thanks, Yuuko. It looks great."

    hi "Hey, Yuuko?"

    yu "Hmm?"

    hi "You do know this is a birthday cake, right?"

    yu "Is that bad?"

    hi "Well, no, it's not really—" #reminder for the potential {nw} break

    yu "I'msorryitwasthelastcaketheyhadinthestoreandIgottherelateandthey'dsoldoutofall—" #reminder for the potential {nw} break

    "She, amazingly, manages to say the entire thing in one breath, taking a quick gasp of air to continue."

    yu "theothersandmyscooterbrokedownonthewayandI'msorryIcouldn't—" #reminder for the potential {nw} break

    hi "Yuuko, stop."

    "Taking my heed, she quickly silences herself."

    hi "Thanks for the cake, Yuuko. I mean it."

    li "Mm, it's lovely."

    "She relaxes and smiles warmly."

    yu "You're welcome. It's enough to see you two smiling."

    "As she walks off behind the counter to attend to cleaning, Lilly and I take two spoons and begin to eat away at the cake."

    "Soft and spongy with a layer of cream in the middle, it reminds me of the cakes I used to have on my birthdays."

    "Not that I'd ever really had many friends, but my parents being there was enough for me."

    "Just the three of us, eating cake together."

    li "Hisao?"

    hi "Ah, yeah?"

    li "You stopped eating."

    "She looks at me inquisitively as I note that I had, in fact, stopped eating."

    hi "Nah, it's nothing."

    "That isn't my world any more."

    hi "This cake's really nice isn't it?"

    "This is my world."

    li "Mm, it's wonderful!"

    "This is the world I need to stay focused on, with all my being."

    # Timeskip

    "After a quick dab of our mouths with knapkins, all that's left of the cake is the scattered crumbs on the plate."

    "As we both lean back contently, Yuuko finally comes from behind the counter, now dressed in her casual clothes."

    hi "Work over?"

    yu "Mm, you can stay here as long as you want, though, as long as I stay."

    li "You needn't bother yourself for us, Yuuko."

    yu "No, no, it's okay. I wanted to talk to you anyway. I haven't seen you in a while."

    hi "Hmm, it'd be about a fortnight since we last saw each other, wouldn't it?"

    yu "Well, Akira's told me about what's been happening either way."

    "She says the sentence in a less than enthusiastic tone."

    "Akira's wayward personality would be enough to drive anyone as fastidious as Yuuko spare, I suppose."

    "As Lilly and Yuuko begin to talk between themselves, I put my arms up on the seat and lazily think to myself."

    "I guess I'm going to have to patch things up with Kenji eventually."

    "As much of a lunatic as he may be, the idea of him becoming a hermit isn't a welcome one."

    "How that guy managed to make me care in the least for him, I'll never know."

    "Stupid conscience."

    "I take the opportunity to grab Lilly's attention as the two finish discussing."

    hi "Hey, Lilly, what do you know about Kenji?"

    li "Kenji… other than being introverted and shy, not much."

    hi "Damn. I was hoping you knew something I could use to help me stop this latest stupid idea he's latched onto."

    li "What does this idea curtail?"

    hi "Something about me being Mr. Big, him being… no, that's not it."

    hi "He was Mr. Big and I was Carrie and… damn, I can't remember. Some characters from an American show."

    yu "Sex and the… City?"

    "What the hell?"

    "From seemingly nowhere, Yuuko pins exactly what I was thinking of."

    hi "Uh… yeah."

    "She suddenly adopts a look of concentration, her brow furrowing."

    "She idly repeats the title, as if reassuring herself that it was the correct thing to say."

    li "Yuuko?"

    yu "Kenji, was it?"

    hi "Yeah, Kenji Setou."

    "Wait. There's no goddamn way this could be related to…"

    hi "Yuuko, you don't mean to say…"

    yu "How tall is he?"

    hi "Short. Thin, too. Kinda runtish, to put it another way."

    "She looks up at me mouth slightly open in realisation."

    "Even Lilly's twigged at what's happening in Yuuko's mind."

    li "Kenji Setou is…"

    yu "He's…"

    yu "My boyfriend."

    "She throws herself out of her seat and comes around beside me, wrapping me in an incredibly tight hug."

    yu "Hisao! He's the one! He's the one!"

    yu "Kenji was the one I loved!"

    "As I'm buffeted left and right by Yuuko's excited bouncing, my brain re-enacts the Hindenburg disaster."

    "Judging by her face, it seems as if Lilly's almost as surprised, or should I say shocked, as I am."

    "As I slowly come to my sense, I realise what has to be done."

    hi "Lilly, we're leaving! Yuuko, you too!"

    li "Ah, right!"

    yu "Okay!"

    "With that we dash out of the Shanghai, making a lightning-fast dash back to my dormitory."

    scene bg school_dormhallway
    with locationskip

    centered "*thud* *thud* *thud*"

    "Dammit Kenji, open this door."

    centered "*thud* *thud* *thud*"

    "Come on, come on."

    centered "*thud* *thud* *thud*"

    "As Lilly remains in my bedroom with Yuuko, both sitting on my bed when I left them, I rap on Kenji's door repeatedly."

    "Eventually all my knocking comes to fruition, the door opening to reveal an annoyed-looking Kenji."

    ke "Oh. It's you."

    "As he begins to close the door, I quickly jam my foot into the closing gap."

    "Momentarily taken on the back foot, he stares at it for a couple of seconds before looking up curiously."

    ke "What?"

    hi "Shut up, you're coming with me."

    ke "Huh?"

    "Before he can protest, I grab his wrist and pull him into the hallway and towards my room."

    "He's surprisingly easy to drag around, actually, even despite his best efforts to pull away."

    ke "Hey, let go of me!"

    hi "You have some stuff to sort out, dude."

    ke "Stuff? What stuff?"

    hi "You'll see. And you're sorting it out right this instant, like it or not."

    "I can't say I have a lot of sympathy for him."

    "While the whole story isn't privvy to me, I can't let go of the fact that he left her thinking he was still there for her."

    "Two years."

    "For two years that girl waited for him. Her knight in size-small clothing."

    "As I reach my door, I open it and quickly drag him in behind me."

    scene bg school_dormhisao
    with locationchange

    "And there we stand."

    "On the bed, Yuuko and Lilly. In the center of the room, Kenji and I."

    "As soon as the two catch sight of each other, they freeze."

    "I can't read a single expression on their frozen faces."

    hi "Lilly."

    "Taking my heed, she holds out her hand. Gently taking it in mine, I lead her out of my room and shut the door."

    scene bg school_dormhallway
    with locationchange

    "Thoroughly exhausted, we both lean back against the wall."

    hi "Kenji…"

    li "And Yuuko…"

    hi "I can't imagine what the hell brought those two together."

    li "Do you want to know?"

    hi "With them both knowing about Sex and the City? Hardly."

    "We both share a small laugh, and return to waiting as we lean on the wall."

    scene bg school_dormhallway
    with shorttimeskip

    "After, with a check of my watch to confirm, half an hour, the two emerge from the door to my room."

    "The fact that their faces are both stoic, and their hands not holding, doesn't give me high hopes."

    "They silently walk past us down the hall, nary a single sound made between them."

    "Just before they disappear down the stairs though, Yuuko turns back."

    "A deep smile and a nod."

    "I give a long, deep breath as the two leave."

    hi "They're together."

    "Lilly positively beams at those two, simple words."

    "Both grinning madly, we quickly hug each other in excitement."

    "Today's a good day."

    "Today is a fantastically good day."

    scene black
    with dissolve

    return

label en_L40:

    scene bg school_dormhallway
    with shorttimeskip

    "Once again, I find myself outside Lilly's dorm room."

    "Having been invited to yet another tea party, I try to make myself as inconspicuous as possible as I loiter around."

    "In the female dorms. In my pajamas. In the evening."

    "My efforts are about as successful as they could possibly be, really."

    "As I raise my hand to rap my knuckles on the door once more, it slowly opens."

    li "Might that be Hisao?"

    hi "Of course, madame."

    "I accentuate the point with an unseen bow."

    "Despite her blindness becoming second-nature by now, I still continue to make such pointless gestures. Old habits are hard to break, I guess."

    scene bg school_dormlilly
    with locationchange

    show hanagown distant_tail_close
    with charaenter
    
    "As she waves me in, I follow her lead and take a seat opposite Hanako."

    ha "Hi, Hisao."

    hi "Hey."

    #This assumes ponytail Hanako is getting sprites. Easily tweaked if that's not the case.

    "It's at this point that I suddenly realise that Hanako's hair is in a ponytail."

    hi "That looks nice."

    show hanagown normal_tail_close
    with charachange
    
    ha "Hmm?"

    hi "Your hair. It's nice to be able to see your face."

    ha "Ah…"

    show hanagown normal_blush_tail_close
    with charachange
    
    "Her face reddens, though holds back from shying away."

    ha "Th…Thank you."

    show bg school_dormlilly at bgright 
    show hanagown smile_tail_close at tworight 
    with charamove
    
    show lilly basic_cheerful_paj_close at twoleft
    with charaenter
    
    "Lilly sits down to my left, smiling indulgently as she places a filled teacup in front of me and a plate of biscuits on the low table."

    "From the smell coming from the cup, it seems to be…"

    hi "Coffee?"

    li "You always ordered coffee at the Shanghai, so I guessed that you preferred it to tea."

    hi "Well, you guessed right. Thanks."

    "As I take a sip, I realise she's guessed more then just that."

    "One teaspoon of sugar, with milk. Just the way I usually have it."

    "There's much more milk than I'd usually have, mind. The color of the coffee looks closer to white than brown. Oh well."

    "As I obediently drink my milk with added coffee, Lilly gives a loud yawn."

    ha "Tired?"

    li "Mmm, I spent most of last night studying."

    hi "Exams are over though, aren't they?"

    li "We still have a couple of tests to go for our class."

    hi "Ah, I see. Mutou wanted to get all of our tests out of the way fast, so we'd have the last week as a clear run."

    "She sighs enviously."

    li "Our teacher is a harsh taskmaster."

    hi "At times I'd prefer a harsh taskmaster over… whatever Mutou is."

    show hanagown distant_tail_close
    with charachange
    
    ha "He has a point…"
    
    "Hanako's pained expression matches mine perfectly."

    hi "You sure read a lot, half the room's taken up by books."

    li "Well, aside from played the cello it's my only hobby. I've started reading a fair bit more, recently."

    "No doubt due to taking care of Hanako freeing up much of her time."

    "From the sound of it, she only had the smallest time outside of cello practice to herself beforehand."

    hi "I guess that's one hobby we both share."

    li "You read too?"

    hi "Yeah. It's probably the only thing I really do in my spare time."

    "We all take a sip from our slightly neglected cups."

    centered "*thud* *thud* *thud*"

    "Well before I manage to empty mine, a series of knocks resounds from the door."

    li "You can come in!"

    "With a clank of the doorknob, the door opens."

    aki "Yo."

    "It looks like our quiet tea party's going to become much less quiet."

    "As Hideaki and Akira walk over, Hanako stares intensely at the table in front of her."

    "I guess she must be debating whether to let her hair back down or not."

    "Eventually coming to a decision, she slowly and hesitantly looks back up whilst leaving her hair as-is."

    hi "Hey Akira, Hideaki."

    li "Good evening."

    "Akira sits herself beside Hanako and I, forming a circle around the table."

    "Her look changes to one of surprise, though, as Hideaki proceeds to sit in her lap."

    aki "Hmm?"

    li "What is it?"

    aki "Ah, nothin'."

    "A smile spreads over her face as she brings her arm over him."

    "The sight's as amusing as it is heartwarming."

    aki "You're a lucky bastard, Hisao."

    hi "Huh?"

    "I can't help but grimace at her sly smile."

    aki "Seeing my sister in her pajamas, there's a lotta men out there who'd like to be where you are."

    "I've seen a lot more than that."

    li "Akira!"

    aki "Hey, I'm just teasing."

    "She leans over to me as much as she can, whispering."

    aki "And Hanako, too. You pervert."

    hi "Hey, it was her idea."

    ha "Um, I… uh…"

    "We both look over to her, her entire body fidgeting."

    ha "If… if it's Hisao… I don't mind…"

    "Dammit."

    "I know Hanako's altogether too innocent to bother reading too much into such a thing, but Akira's positively stunned."

    "As she flicks her head around to me I just about leap backwards in fright."

    "K—K—K—K—Killing intent!"

    li "Um… Akira…"

    "It seems Lilly can sense it just as well as I."

    "As she looks away from me, I breath a sigh of relief, thankful for my life having been spared."

    "Looking to Hideaki for his thoughts on the matter, I see him busily eating a biscuit with crumbs stuck on the side of his mouth."

    "No use looking for help there, it seems."

    aki "So, you still on that idea o' yours?"

    li "Teaching?"

    aki "Yeah. It's not like you aren't good enough at English to pull it off."

    li "Mm, I'd still like to do it. Do mother and father know?"

    "Mother and father…"

    "I can't help but notice how distantly she refers to them. It's as if they were mere strangers to her."

    "I guess it's to be expected, considering that they all but disappeared from her life when she was such a young age."

    aki "I told 'em. They're happy you've got a direction to go in."

    "She nods silently, evidently content for this line of discussion to be finished."

    aki "So, what're you gunning for?"

    hi "Me? Well…"

    "I may not give much thought to the future, but recent events have given me some pause."

    "“Absentminded professor,” huh?"

    hi "Science, probably teaching it."

    aki "Uooh, high flyer, eh?"

    "Lilly gives a small giggle, noting how close to the mark her offhand quip was."

    li "He certainly has the right personality for it."

    hi "What about you, Hanako?"

    ha "Hmm? Oh, ah…"

    "Content with her position as an observer to the conversation, my question throws her off her guard."

    ha "Something to do with music, I suppose."

    aki "Oh? You play an instrument too?"

    ha "No, I'm just kind of good with sound systems."

    "As I watch their conversation I move my teacup to my mouth."

    "…and promptly choke on the cold coffee."

    li "Hisao?"

    hi "Ah, it's just the coffee's gotten cold."

    "Lilly face suddenly turns to one of realisation."

    li "Yes, drinks, I completely forgot. Akira, Hideaki?"

    aki "Wouldn't mind a coffee, if you could."

    hh "Tea."

    li "Coming right up."

    "She stands and moves to the counter after retrieving my cup, getting to work."

    hi "So, what brings you two here?"

    aki "Just checkin' on my sister. Hideaki thought he may as well come too."

    "He gives a nod to confirm her account of events."

    "The two are strange combination, but they seem to be getting along better than ever."

    aki "I'm sure he doesn't mind the sight either way, eh?"

    "He simply closes his eyes and dons his most civil face as she smiles down at him."

    "Hanako and I give a small laugh at his expense."

    "As shy as she is, she's handling herself quite well. She'd only met Akira once before at karaoke, too."

    li "Here you go."

    "She sets the cups on the table, everyone taking them in hand and eagerly drinking away as she retakes her seat on the floor."

    aki "Ah that's right, I was talking to Yuuko yesterday."

    "She takes a gulp from her cup before continuing."

    "Yuuko? Why bring Yuuko up?"

    "…Oh."

    "Before she's removed the cup from her lips I can already guess what she's going to say."

    aki "She seems happier than usual. What's up with that?"

    "Lilly gives a silent giggle and I give a badly-hidden snort of laughter."

    "As her and Hanako's eyes flick between us, anticipating an answer, she gives up."

    aki "Fine, have it your way."

    "She gives a resigned sigh."

    aki "You two're a real pair, you know that?"

    aki "Well, we'd better get going, anyway."

    li "So soon?"

    "Akira pushes herself up, Hideaki doing the same in quick succession."

    aki "Yeah, your curfew's at ten, right? It's already ten to."

    li "Well, if you must."

    aki "Hey, don't look so down. Ah, that's right!"

    li "Hmm?"

    aki "How 'bout we go down to the Shanghai on Saturday? Your vacation starts then, doesn't it?"

    li "That'd be wonderful! Hisao, Hanako?"

    ha "Mm, I'd like to go."

    hi "Same here."

    aki "Alright, we have a plan! You can invite anyone else over you can think of, like that shortie without legs… uh…"

    "She scrunches her face as she tries to recall her name."

    "There can only be one person she's referring to."

    hi "Emi."

    aki "Yeah, that's right. Emi."

    "To specifically mention her, I suspect that she has ulterior motives."

    "After the recent karaoke trip, it looks like Emi's the first member of her little fanclub."

    hh "We'd better be going."

    aki "Hmm? Ah, yeah, right. Seeya guys."

    li "Goodbye, Akira."

    "As we say our farewells, she shoots quick glance in my direction."

    "Looks like she still hasn't let Hanako's comment slip by her."

    ha "I should go as well. Bye, Lilly. Bye, Hisao."

    "With another round of farewells, she exits the door almost as soon as Hideaki closes it."

    "I fall back onto the floor with a long breath."

    hi "Akira's exhausting."

    li "She can be, yes."

    li "Though now, it's my turn to be exhausting…"

    "She leans to the side and slowly crawls around the table to me on all fours, stopping with her head just above mine."

    li "Come here, Hisao~"

    "As I look into her sapphire eyes, I can't help but grin."

    hi "We're not going to be getting much sleep tonight, are we?"

    li "Not if I can help it…"

    "As she leans downward, I steal her lips before she can do the same to me."

    "Tonight will be a long night."

    scene black
    with shuteye

    return

label en_L41:

    "It's odd, really."

    "I've walked down this same orange-tinted path to go to the corner store many times, but this once, it feels completely different."

    "While I've always liked the quiet of this route, having Lilly quietly walking beside me was taken for granted after a while."

    "I guess I was wrong in my initial reflections. What I'd liked wasn't the solitude, but the quiet."

    "…Though it doesn't look like I'll be alone for much longer, as a familiar suited figure walks up the street towards me."

    aki "Yo."

    # Timeskip

    aki "Ah, so Lilly's got class rep work, eh?"

    hi "Yeah. She really keeps herself busy."

    aki "Same old Lilly as ever, then. Never one to take things easy for herself."

    "It seems the two know each other pretty well."

    hi "She was like that before coming to Yamaku?"

    aki "Yep. She pretty much fought her way onto the student council at her previous school. Not easy when your competition's a horde of spoilt little princesses."

    aki "I want to tell 'er off for never keeping any time to herself, but I'm as guilty as she is."

    aki "I guess you saved me having to, though."

    "I give a nod as we continue down the street."

    "Glancing over to her, she lacks the acceptance of silence that Lilly has, distracted wholly by the lack of conversation."

    "Well, not that I don't have something to fill the void. After a few moment's thought, I decide to raise the subject."

    hi "Hey Akira, do you mind if I ask something kind of personal?"

    aki "My three sizes are con—fi—den—tial."

    hi "Not that, more about something I heard from Hideaki."

    aki "You dirty little—" #reminder for the potential {nw} break

    hi "Nothing like that either!"

    "Come on Hisao, you can't get caught in her pace."

    hi "He told me you were engaged. Congratulations."

    aki "Ah…"

    "Akira seems, amazingly, to be caught on the back foot."

    aki "Well, yeah, I guess we are."

    hi "You don't sound very sure of yourself."

    "She gives a sigh, returning to her headstrong self."

    aki "Well, it's not me. I'm fine with it."

    hi "He seemed pretty much the same way when I talked to him…"

    aki "Well, that's kinda what I'm thinking about. Hey, how many fingers you have?"

    hi "Fingers? Ten…"

    aki "Good, good. Can never tell with students from Yamaku."

    aki "Anyway, I've been through as many guys as you have fingers. Hideaki's the first to really take my interest."

    "She gives a short chuckle to herself."

    aki "Heh, should've seen how worried the folks were about the prospect of having an unmarried daughter."

    aki "I do worry about the shortie though. You've seen it right? How childlike he is?"

    hi "He is sixteen, it's not like he's a kid."

    aki "Yeah, I guess so…"

    hi "Please don't sound so unsure of that."

    aki "Don't worry about it, don't worry about it. I'm not like that."

    "Yeah, right. I wonder if the term “cradle robber” extends to women."

    aki "I dunno. I just wonder if he really knows what he's getting in to."

    "Perhaps it's an exaggeration, but it almost seems akin to a prodigy and a sociopath joining out of mutual curiosity about each other."

    "The fact that Hideaki can inspire such feelings in the typically reckless Akira is enough to see the fault of her thinking."

    hi "He may seem ike that at times, but he's pretty wise."

    hi "The fact that you're like this is enough to see you like each other, and you both sound like you want to go ahead with it."

    aki "Yeah. Maybe I'm just worrying too much."

    hi "That just goes to show how much you like him."

    "She gives a small grin as she reaches over and grabs my head, roughly moving it around in a circle."

    aki "A regular romanticist, aren't ya?"

    aki "Well, I guess that's just the kinda person Lilly'd like."

    "She gives a short, somewhat uncultured, snort of laughter."

    aki "You two really are like one another, you know that?"

    hi "Really?"

    aki "Yeah. Good thing, too. If you were the wrong type…"

    "She balls her fist and hits her other hand, the loud clap sending a shiver down my spine."

    "She really is an expert in making me as unsettled as humanly possible."

    aki "Ah…"

    "She got distracted, thank God. Following her gaze, I see that we've already arrived at the store."

    # Timeskip

    aki "Pig."

    "She lacks the subtle touch that Lilly has in such matters."

    hi "You're just used to someone who's half my size."

    hi "Come to think of it, where is Hideaki anyway?"

    aki "Sleeping. The exams are doing a right old job on him. Doesn't help that he's being pushed so hard on 'em by his dad."

    "Ah yes, the infamous father that makes him listen to “crappy music.”"

    hi "It seems you both dislike him."

    "Akira's temper flares fiercely, her face looking like a bomb about to explode."

    "She really does change moods quickly and unpredictably."

    aki "Man, if I could just get my hands on that guy I'd do a right job on 'is smug old face."

    aki "Goddamnit that guy pisses me off, and now I'm thinking about him, so now I'm pissed off!"

    aki "Hisao! You are personally responsible for making me pissed off!"

    hi "If my hands weren't full with bags I'd help organise a lynch mob."

    "She looks at me for a second before chuckling off her annoyance."

    aki "Nah, it's not your fault. I just wish the guy'd lighten up once in a while."

    aki "That reminds me. You two going to tanabata on Sunday?"

    "A fail to see the connection between the two, but having seen Akira's temper, I'm all too happy to go with the new line of dicussion."

    hi "Tanabata's this Sunday? Already? Wow, time goes fast."

    hi "I'll check with her, but I'd be surprised if she didn't want to."

    aki "Good, good. It'll be the first she's gone to."

    hi "Really?"

    aki "Can you imagine her going with Hanako?"

    "I involunatarily grimace, remembering the Hanako of months ago."

    "Deathly quiet and scared to death of social interaction, she was a complete mess held together only by Lilly."

    "In an environment like tanabata, she'd have a fierce panic attack."

    hi "…Point."

    aki "Show 'er a good time, eh?"

    "She playfully jabs an elbow into my ribs, prompting another from me."

    "As we walk back, chatting some more before separating, I smile while pondering the prospect of going to tanabata with Lilly."

    return

label en_L42:

    scene bg school_girlsdormhall
    with locationskip
    
    "I can't remember the last time I wore a yukata."

    "I suppose the last time would've been at a Tanabata before my unfortunate event."

    "Following that train of thought, I guess that's where the red stain on the right sleeve came from."

    "I guess I should've checked the thing before the day I had to wear it, really."

    "Oh well. There are worse things that could happen."

    extend " I suspect Lilly will be less than concerned by it, at any rate."

    "Right. Lilly. That's why I'm here."

    "As my brain finally kicks into gear, I rap my knuckles on Lilly's door."
    
    scene bg school_dormlilly
    show lilly basic_smile_yuk_close at twocenteroff
    #show expression Solid("#00000022")
    show hanako_door_base at right  # yep, hanakodoor. 
    show hanako_door_door at left
    with locationchange
    
    li "Coming!"

    "As soon as I hear her voice, the quiet sound of wooden clogs dances on the edge of my hearing."

    "Within seconds she opens the door…"

    play sound sfx_dooropen
    
    # here we move everything. Kinda problematic to get right coordinates for every thing in this scene.
    show bg school_dormlilly at roomopen
    show lilly basic_smile_yuk_close at Position(xanchor=0.5, xpos=0.48, yanchor=0.5, ypos=0.5)
    show hanako_door_base at rightwallopen
    show hanako_door_door at leftdooropen
    with charamove
    
    "…leaving me completely stunned."

    "As she stands there, gently smiling in the most lavish garb, I'm completely spellbound."

    "Second pass before I finally manage to find my voice."

    hi "Y—You look… amazing."

    "Not quite the most suave, nor thought-out, response. Darned if it isn't thruthful, though."

    "From the dark red… stick… thing in her hair to the black and dark red kimono, she looks amazingly graceful and refined."

    "She silently takes a step forward and runs her hand from my left shoulder to the end of my sleeve, feeling out the yukata's contours."

    "Compared to her geisha-like demeanor and clothing, I must look close to a pauper in my light brown, loose-fitting yukata (with a red stain)."

    li "It seems you're just a dressed up as I."

    hi "Ah, y—yeah."

    "What she doesn't know won't hurt her."

    "Her face seems to slip slightly as seconds pass."

    li "You seem quiet today, Hisao."

    hi "Only because your looks have all but stolen my words, my love."

    show lilly basic_cheerful_yuk_close
    with charachange
    
    "…Where in the world did that come from?"

    "Regardless, she seems to quite like the cliche-ridden compliment."

    scene bg school_girlsdormhall
    scene bg school_girlsdormhall
    show lilly basic_cheerful_yuk_close
    with locationskip
    
    li "Shall we be off, then?"
    
    hi "Indeed we… "

    extend "oh."
    
    show lilly basic_surprised_yuk_close
    with charachange
    
    li "Is something wrong?"

    hi "I seem to have overlooked something. Something that was painfully obvious."

    "She halts for a second before giving a resigned smile."

    li "Transport?"

    hi "Yep. Hang on, I'll just call a cab."

    "I slip my hand undearneath the yukata's front and feel around."

    "Wallet… dormitory key…"

    "Dormitory key… dormitory key…"

    hi "Ah, that's right. I didn't bring my cellphone. Mind if I use yours?"

    li "Go right ahead. It should be on the counter."

    scene bg school_gate_ss
    show lilly basic_weaksmile_yuk_close_ss
    with shorttimeskip

    "After sliding past and calling the taxi service, it's not long before we're on the street outside the gate and waiting."

    "If my guess is right, it'd be about six in the evening."

    "The night's chill hasn't quite set in yet, though the street's already bathed in an orange glow."

    "An uncharacteristic yawn manages to slip by Lilly's defenses, in a rare moment of carelessness."

    li "Ah, sorry."

    hi "Up late last night?"

    show lilly basic_sleepy_yuk_close_ss
    with charachange
    
    li "I lost track of the time as I was reading. I think by the time I got to bed it was past midnight."

    "I narrow my eyes at her."

    hi "Is that all you were doing?"
    
    show lilly basic_surprised_yuk_close_ss
    with charachange
    
    li "…"

    with Pause(1.0)
    
    # sprite change
    show lilly basic_pout_yuk_close_ss
    with charachange

    li "…"

    "I allow myself a small smirk at her expense, before giving her a gentle hug."

    "That is, until I bring my mouth next to her ear and give a lowly whisper."

    hi "Tanabata won't be the end of our night."
    
    show lilly basic_cheerful_yuk_close_ss
    with charachange
    
    "A small grin spreads on her face as I pull back, a small nod being the only reply."

    "Right on cue, the sound of the taxi pulling up on the side of the street can be heard."

    "I can't help but note the lingering eyes of the driver as I guide her into the car."

    "That said, I can't quite place whether it's due to her looks, or the fact that her eyes are closed—telltale of the blind."

    "With a quick skip around the back, I slide into the other side of the cab before shutting the door."

    # Timeskip
    
    scene bg tanabata_bamboo#suburb_tanabata_ni # TODO: replace with something new. [str]
    show crowd
    show lilly basic_pout_yuk_close_ni
    with shorttimeskip
    
    "With a nod and a polite tip for the exquisite drift around the last corner, of which Lilly strangely didn't seem to appreciate, the taxi disappears off down the road."

    "Though slightly flustered, Lilly regains herself in no time."

    hi "Well, this is it. Tanabata."

    li "Have we arrived in time for the fireworks?"

    hi "Yeah, I made sure we had some time to burn before they started. We have a couple of hours to spend."

    "Looking up to the sky, the orange tint of before is replaces by a moonlit deep blue."

    "Unfortunately, that also means that the night's chill has set in."

    "Given how heavy and thick her kimono seems, though, I doubt Lilly will mind."

    "The larger problem right now are the throngs of people moving around the brightly-coloured stalls and attractions."

    li "Hmm, it sounds busy."

    "A fact which doesn't escape Lilly's keen hearing."

    hi "Yeah, this could be a problem."

    li "I'll make sure to hang on tight."

    hi "Good, wouldn't want you getting lost."

    hi "With that out of the way, what should we do first?"

    li "Given our circumstances, I think you're the most qualified to answer."

    hi "What? Oh. Ah, right."

    "My mental stumbling earns me a small giggle."

    li "Shall we get something to eat while you think?"

    hi "Sounds like a—" #reminder for the potential {nw} break

    # Sprite change

    extend "Subtle. Very subtle."

    "Hand in hand, we begin our journey through the crowds."

    "As we move through them, the sound of the wooden clogs beside me is just audible through the sounds of everyone around us."

    "It's a little saddening to see so few in traditional clothing. Jackets and jeans abound, both for men and women."

    "Just one more reason for the badly-disguised glances at us from passers by."

    "I feel like a show pony."

    "Despite it being well-hidden, Lilly nature is ever-so-slightly tensed, too."

    "I guess she must be overhearing snippets of conversations, as as I'm seeing their glances."

    "Thanksfully, a food stall comes within sight to distract us."

    "Storekeeper" "Hey, waddaya want?"

    "Don't sound too enthusiastic there, bud."

    "Come to think of it, he looks like he'd rather be a million other places than here. In the cold. Behind a counter. Serving smiling people."

    "Poor sod."

    li "May I have a candy apple, please?"

    "Storekeeper" "Anything for you?"

    hi "Ah, no thanks."

    "Storekeeper" "Right. One candy apple, coming right up."

    "As he turns back into the stall to make it, I glance over to Lilly."

    "Patting her waist's sides a couple of times, she looks to me with a painful look on her face."

    hi "No money, huh?"

    li "I didn't have any place to put my purse in my kimono, and I forgot to pick it up when we left."

    hi "No problem, I have enough to cover us."

    "…Just."

    li "Sorry, Hisao. I'll make sure to pay you back."

    hi "Don't worry about it. Besides, you paid a lot more than this for our other date."

    # Reference to a to-be-rewritten scene, not a continuity error

    "Notes in hand, I pay the storekeeper his due as he hand Lilly the bright red candy apple."

    "My mouth wells with saliva just contemplating how sweet it looks."

    hi "You like sweets, then?"

    li "Mmm!"

    "She beams a childish smile, clutching her precious sweet in one hand and my hand in the other."

    "I can't help but smile back."

    hi "Maybe we should go sit somewhere while you eat that."

    "She gives an affirmative nod as she gently licks her treat, her eyes closed shut."

    "Our trip through the crowds is much more pleasant this time around."

    "With Lilly's attention focused on enjoying her candy apple and mine on her, we're all but oblivious to everything around us."

    "Eventually we find a bench and take a seat, with her continueing to enjoy herself and I leaning back to relax."

    "Walking through such a huge site is tiring."

    "Not that I mind. There are far worse ways to spend a sunday."

    "After a few minutes of savouring the cool breeze, a glance over to Lilly confirms that her candy apple is a thing of the past."

    hi "Done?"

    li "Done."

    "As soon as the word is out of her mouth, I notice the left over candy apple stains around her mouth, looking like badly-applied lip-stick."

    "As she begins to stand up, I quickly call her back down."

    hi "Ah, hold on."

    li "What's wrong?"

    hi "Hold still for a second."

    "Lacking a handkerchief, I pull my hand back in my sleeve and put the already stained section of the right sleeve to Lilly's mouth, gently rubbing it."

    "She brings her face forward a little, realising what I'm doing."

    #"For a moment I pause, looking at her soft, red lips."

    return

label en_choiceL42:
    menu:
    #Choice time
    # Choice [1] - "Kiss her."
    # Choice [2] - "Check inventory."

        "For a moment I pause, looking at her soft, red lips."
        
        "Kiss her.":
            return m1
        
        "Check inventory.":
            return m2

label en_L42a:

    # Choice [1]

    "Closing my eyes, I gently wet my lips and give her a lingering kiss."

    "With my finger on her chin, I can feel her delicate mouth twisting into just as delicate a smile."

    "As I lean back, both of us are slightly blushing."

    hi "All finished."

    li "Thank you, Hisao."

    "As she smiles at me warmly, a feeling of utter contentment fills my being."

    "Clapping my hands together, I lever myself off the seat and give Lilly a hand up."

    hi "To the sideshows!"

    li "Forward!"

    return

    # Choice [2]

label en_choiceL42a:
    menu:
    # Choice time, again
    # Choice [2A] - "Wallet."
    # Choice [2B] - "Dormitory key."

        "Wallet.":
            return m1
        
        "Dormitory key.":
            return m2

label en_L42b:

    # Choice [2A]

    "Let's see, wallet… wallet… wallet… Here it is. Now…"

    "I take the small, black leather wallet and gently press the back of it to her lips."

    "Her cheeks blush slightly as she pushes her lips forwards."

    "It's not long, though, before her expression faulters."

    "She jerks her head back, bringing a hand to the wallet and feeling its outline."

    li "Hisao~"

    "Confronted with her adorably pouting face, I can't decide whether to laugh or hug her."

    "I decide to do both, chuckling as I bring my arms around her."

    "As she brings her arms around me and snugles her head in, my laughter trails off into a silent smile."

    li "We must look like fools, mustn't we?"

    hi "I wouldn't want to look like a fool with anyone else, though."

    "We gently let go of each other, Lilly taking a second to regain her graceful composure."

    li "Where shall we be off to next?"

    hi "Sideshows, I guess."

    "She gives a nod of approval as I lever myself up, the two of us making our way into the busy throng."

    return

label en_L42c:

    # Choice [2B]

    "Now where's that darn… there it is."

    "Taking my dormitory key in hand, I slowly but gently move it upwards towards its target."

    "Just… a little… bit… more…"

    li "Ah!"

    "As the cold metal of the key touches the inside of her nose, she jerks back in shock."

    "I can hardly supress my laughter."

    li "Hisao!"

    hi "Sorry, you looked so vulnerable that I couldn't resist."

    "She feels the bottom of her nose, trying to work out what I'd put up it."

    hi "It was my dorm key. Uh, sorry."

    "She regains her composure in short measure, gathering herself expertly."

    li "My nose feels kind of funny."

    "As if to emphasise the point, she wiggles her nose to try and dispell the cold feeling."

    "Stifling the last remnants of my laughter, I gather myself once again and lever myself off the bench."

    hi "Shall we be off to the sideshows, then?"

    "She gives a short sigh before taking my hand and smiling."

    li "Lead on."

    return

label en_L42x:

    # End choices

    "As we walk hand in hand, my eyes move from one brightly-coloured stall to another."

    hi "Anything you want to try?"

    li "Well, I don't think I'd be much good at most of them."

    "A point, I guess."

    "There's only one thing to say to that."

    hi "Right. In that case, I'll win you something."

    "She claps her hands together in delight at the idea."

    li "What will you play?"

    hi "Hmm…"

    "I scan my eyes from side to side, catching glimpses of the stalls to our sides as people pass."

    "Eventually, I find one that I've been looking forward to trying since we came."

    hi "Toy shooting. I've been wanting to try it, too."

    "With a gleeful nod, we both walk over to the stall."

    "The old man slumped in a chair beside it looks just as excitable as the food stall owner."

    "Stall owner" "Pay the money, get three shots. Anything to make fall over you get to keep."

    "He says the line in a monotone voice, as if he were reading from a practiced script."

    "Politely nodding, I hand over a few notes as Lilly stands to the side."

    "Rolling my shoulders back, and trying my best to look like I know what I'm doing, I up the toy rifle and take a quick gander at it."

    "Wooden, pretty heavy, seemingly a replica of some old rifle used by the military."

    "…How this is allowed to be used as a sideshow attraction's got me beat. The scope even seems to work pretty well."

    "My confidence having been boosted, I crouch down and take aim, looking down the sight on the tip."

    "Stuffed doll, "

    extend "china doll, "

    extend "matryoshka doll, "

    extend "bear."

    "Right, I'll go for this."

    "I bury the gun in my shoulder and hold my breath as I line up the shot."

    centered "*Thud*"

    "Some marksman I am. The shot cork harmlessly thuds into the wall beside its head."

    li "No good?"

    hi "No good. I'll have another try."

    "As I turn to look back down the barrel, my eyes stop at the old man sitting beside the stall."

    "One eye's closed, but the other's open just a crack."

    "If his eye were at any other angle I'd say he's taking her looks into careful account."

    "Nonetheless, with his gaze pinned on her closed eyes, it's obvious that he's trying to work out what to make of her blindness."

    "The temptation to shoot one of these corks into his eye to show him first hand is high."

    "Resisting, though only barely, I loudly and pointedly cough into the back of my hand as I glare at him."

    "He quickly rubs the back of his neck awkwardly as he hurries to look away."

    "His action does give me an idea, though."

    hi "Hey Lilly, how about you take the shot?"

    "She gives me a bizarre look. A well-deserved one, probably."

    "Taking her hand, I guide her over and walk behind her."

    hi "Okay, put one hand heer and the other… there."

    "I take each of her hands in mine, placing one on the trigger and the other on the underside of the barrel."

    "A small grin spreads on Lilly's face as she slowly learns how to handle it."

    li "So if I pull there, that'll fire?"

    hi "Yeah. Now, if you just move it over this way…"

    "By now we're both fully aware of just how ridiculous we must look."

    "The shooter, a blind blonde in a kimono, and the guy reaching around her to help."

    "Working together, we manage to get the barrel… kind of around where the target is."

    "Taking off my hands and stepping aside, she crouches down to make the shot."

    centered "*Thump*"

    "The soaring cork strikes dead into the bear's nose, toppling it from the shelf."

    "…a blind person is better at shooting than I am."

    "Somewhat depressing, really. Good thing I'm not in the army."

    li "Did I hit it?"

    hi "Yup. You shot better than I did."

    li "Well, it was only luck."

    "Well, yes, but that's not the point."

    "With a groan, the tired old man gets off his chair and retrieved the fallen teddy bear, placing it on the counter."

    "Lilly reaches forward and gently takes it in her arms, holding it tight to her chest."

    li "Thank you, Hisao."

    hi "You took the shot, not me."

    "Nodding farewell to the stall owner, not that he bothers nodding back, Lilly and I move off."

    "Clutching the bear in one hand and mine in the other, she looks perfectly content."

    hi "So, where'll we go now? Somewhere a bit more secluded?"

    li "Mm, that sounds like an idea."

    "Walking through the still thick crowds, they eventually start to thin out as the stalls start to disappear behind us."

    "As I open my mouth to comment on the fact, I notice Lilly wholly distracted."

    hi "Lilly?"

    li "Shh."

    "I look at her intently, before following the direction of her face as I realise she's listening for something."

    li "This way… I think it's over here."

    "She begins to lead me, instead of the other way around."

    "She seems to utterly wrapt in her task that she's forgotten to fill me in on what this task actually is."

    "Silently following her, I pick up on what she's sensed."

    "…Sobbing?"

    "As we walk to the edge of the forest on the outskirts of the festival, now in full-swing, the source of the sound becomes clear."

    "There, at the foot of a tree, sits a boy no older than five, quickly sobbing."

    "With short-cut black hair, striped shirt and shorts, he tightly grips his knees as he buries his head into them."

    "Lilly quickly crouches down in front of him as I do the same."

    li "Um, hello…"

    "The boy looks up, his cheeks slightly reddened from crying."

    "For a second he looks bewildered by the figures in front of him."

    "Boy" "Um… hello."

    "His voice wavers from shyness."

    li "Is something wrong?"

    "Boy" "I… I shouldn't…"

    hi "Talk to strangers, eh?"

    "He nods quickly."

    "Lilly's maternal instincts seem to be on full display, instantly wrapt in the child's evident problem."

    "I rub my chin in an effort to work out an answer to the quandry."

    "…Well, it's cliche. I guess children don't mind cliches much, though."

    hi "Right. That's easily fixed."

    "He attention moves to me, a questioning expression on his face."

    hi "I'm Hisao. Hisao Nakai. And this is…"

    li "Lilly Satou. Pleased to meet you."

    "As she smiles warmly at him, he seems to relax somewhat."

    "Boy" "I'm… Reo. Reo Sonomiya."

    hi "Well, now we know each other, we can talk. What's up?"

    "Reo" "I was with my mom, and we…"

    # 'mom'
    # I am raging at you, Americans. Raging oh so hard.

    "His voice starts to crack as he trails off, though it's obvious what happened."

    "Lilly reaches forward, and with a couple of taps to find it, rubs his hair gently."

    "The gesture doesn't go unnoticed, his attention being distracted from his sadness for a scant few moments."

    "As she closes her eyes and smiles, he seems to lose interest in working out the riddle of the inaccurate hair-rub."

    hi "Well, there's just one thing to be done, then."

    "Lilly stands up as I do, evidently knowing full well what I intend."

    "Standing up proudly, we both thust an upturned thumb to the boy."

    $ doublespeak(hi, li, "Reo, we'll help you find your mother!","Reo, we'll help you find your mother!")

    # Timeskip

    with shorttimeskip
    
    "This kid is heavier than I thought."

    "With Reo perched on my shoulders and Lilly holding my hand, our haphazard mother-hunting trio makes its way through the buzzing croud."

    "To say we stick out like a sore thumb is understating things."

    "The red stain on my yukata is all the more brighter after cleaning Lilly's mouth with it, as well."

    "Nevertheless, with Lilly's hearing and both of our heights, I doubt there's anyone more qualified for the job for miles around."

    "Reo" "Ah, there!"

    "He excitedly thrusts his finger forwards, pulling me along with it."

    "Reo" "Wait, no, that's not her."

    "Lilly takes a moment to smile at him before getting back to acting as the group's land-borne sonar."

    "Despite this having been a minute-by-minute routine for quite a while, I'm far from hating it."

    "Dammit, my paternal instincts have gotten the better of me."

    "Before long, I feel a small tug on my hand."

    hi "Heard something?"

    li "I think so, it came from this direction."

    "She points directly ahead of her, just forwards from dead right."

    hi "Alright, we have a lead!"

    "Reo" "Forwards!"

    hi "Fowards!"

    "With a small giggle from Lilly, we make our way in the direction she pointed out."

    "Reo" "Ah!"

    hi "Did you see something, Reo?"

    "Reo" "She's over there!"

    "He enthusiastically points ahead of him, Lilly and I picking up our pace."

    "A pace that's not exactly going to set records, given her wooden clogs."

    "Eventually we manage to leave the stream of people moving to and fro, coming face to face with a woman."

    "Reo's mother, going by both her long, black hair and her amazed face."

    "Woman" "Reo!"

    "Reo" "Mom!"

    "I quickly crouch down, the boy practically leaping from my shoulders."

    "Lilly and I are both left smiling as the two hug each other tightly."

    "Eventually she looks up, a look of great relief and gratitude on her face."

    "Woman" "Thank you for finding him, both of you. We got separated in the crowd, and…"

    "I hold up a hand, halting her breathless gratitude."

    hi "It's fine. He was fun to be with."

    "Lilly bends down and looks towards the cheekily grinning boy."

    li "Mm! Isn't that right, Reo?"

    "He leans outward on one leg as he beams a full-strength smile at Lilly."

    "Woman" "Now, Reo, you should thank them for helping you."

    "Instead of the expected quick “thank you,” he steps forward and gives Lilly a quick hug."

    "For a second, she's taken aback before her smile returns."

    li "Thank you, Reo."

    "Both I and his mother are more than amused at the proceedings."

    "Woman" "If there's anything I can do for you?"

    "Lilly gracefully rights herself before replying."

    "His mother pauses and examines Lilly for a moment through curious eyes."

    "For a second, I wonder why until I see that Lilly's eyes are closed."

    "It's become so second-nature to me, I sometimes forget it's not normal to converse with the other's eyes closed."

    "Seemingly working out why she has the mannerism, her face returns to normal."

    li "It's okay. Being with him was more than enough reward."

    "Woman" "Thank you. From the sounds of it, he's earned himself take-aways for tea."

    "Reo" "Yay!"

    "With a polite bow from every party, we part our ways, Reo energetically waving goodbye."

    "As soon as he's out of eyeshot I slump and sigh in exhaustion."

    hi "I'm not cut out for this mother-finding business."

    "Lilly giggles lightheartedly."

    li "You seemed to be having fun."

    hi "Yeah, it was fun…"

    hi "Unfortunately, my shoulders don't seem to agree with that, though."

    li "Shall we sit somewhere to recuperate, then?"

    hi "Yeah, sounds good. The fireworks should be starting soon, too."

    hi "Not to mention I'm out of money."

    "She smartly puts her hand in mine, grinning past the unneeded note."

    li "Please lead on, dear sir."

    hi "Indeed I shall, madame."

    # Timeskip
    # Half me being lazy, noted for possible small expansion
    
    scene bg misc_sky_ni
    with shorttimeskip
    
    "It doesn't take long before I find a nice, secluded area."

    "With the forest behind us, the distant hum of the crowds has all but died out."

    "True, there's no benches, but sitting on the grass isn't too bad."

    "As I prop myself up on my arms, Lilly rests herself on my shoulder."

    "I'm not sure how long we've been sitting here, but no doubt it's been a fairly long time."

    li "You found a nice place, Hisao."

    hi "Thanks. If we hadn't found Reo, I wouldn't have thought to come here."
    
    play ambient sfx_fireworks
    show fireworks
    
    "As if right on cue, a single yellow line shoots up into the sky, bursting into a vivid yellow flower in the night sky."

    "While she may not see them, she can definitely hear them flying up and bursting in the air."

    "One, two, three, four. One bright colour follows another, together forming a momentary garden floating in the air."

    "As we sit, silently watching the grand spectacle, I can't bring myself to smile."

    "Something is wrong."

    "My fingers, my hands, my feet, they all feel cold."

    "Much, much colder than the night air."

    "As I look upwards, I try to stifle my own thoughts."

    "If only I'd been normal."

    "Then I wouldn't be feeling like this after carrying a boy around for just a small while."

    "This feeling… I've felt it only once before."

    "Back then, I'd been unaware of what this feeling meant."

    "Now, though, I know all too well."

    li "They're wonderful…"

    "I look down to Lilly, her face all but focused on listening to the airborne spectacle."

    "The twilight of my life… has been a happy one."

    # Insert heart attack graphics where applicable

    #centered "*THUD*"
    play sound sfx_heartfast
    show heartattack alpha 
    with Dissolve (0.1)

    hide heartattack alpha 
    with Dissolve (0.8) 

    with Pause(0.15) 

    play sound sfx_heartslow 
    show heartattack alpha 
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.8)

    play sound sfx_heartfast
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.8)

    "Just as last time, the pain is sudden and ferocious."

    "My entire body tenses as I narrowly avoid yelping out in pain."

    "Lilly stirs slightly, feeling the change in my muscles."

    "Dammit, why now? Just when everything started going right."

   # centered "*THUD* *THUD*"
    play sound sfx_heartfast
    show heartattack alpha  
    with Dissolve (0.1) 

    hide heartattack alpha
    with Dissolve (0.8)

    with Pause(0.15) 

    play sound sfx_heartslow 
    show heartattack alpha 
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.8)

    play sound sfx_heartfast
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.8)
   
    "The second wave of pain all but destroys any remaining resistance I can muster."

    with vpunch
    
    "With my mind wracked in pain, I fall back onto the ground with a soft thud."

    "The sky."

    "That beautiful, endless sky."

    li "Hisao? Hisao!"

    "Lilly's face comes into view, her panicked expression hovering over my gaping mouth."

    li "Hisao! Please!"

    hi "L—Lilly… I…"

    "Force it out, force it damn well out!"

    hi "I'm…"

    "I just need to say that one, final word."

    hi "Lilly…"

    stop ambient fadeout 4.0

    #centered "*THUD* *THUD*"
    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.1) 

    hide heartattack alpha 
    with Dissolve (0.2) 

    with Pause(0.7) 

    play sound sfx_heartfast 
    show heartattack alpha  
    with Dissolve (0.1)

    hide heartattack alpha 
    with Dissolve (0.2)
    
    "Pit-pat. Pit-pat."

    "The tears from Lilly's eyes tap freely onto my cheek."

    "As much as I want to wipe them off, every sense and muscle in my body seems to be shutting down."

    li "Hisao! Anyone, help! Please!"

    #centered "*THUD* *THU—*"
    play sound sfx_heartfast 
    show heartattack alpha 
    with Dissolve (0.1) 

    hide heartattack alpha 
    with Dissolve (0.8) 

    show passoutOP1 
    with None 

    "I'm sorry, Lilly. I couldn't say it."

    "I couldn't say goodbye."

    with Pause(1.0)
    window hide 

    play sound sfx_heartstop 

    scene black 
    with None 

    with Pause(2.7) 
    
    # End of Lilly act 4
    
    return
