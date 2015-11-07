label en_HT1:

    #Yes! You heard it here first! The beginning of the true Hanako path!
    #Less death! No depressing H-scenes! Only happysex and rainbows!
    #Also I need to get back into my groove, so feedback plox.
    #except for you, TC.
    #XP

    #of course, this feeds directly on from the library scene.
    
    scene bg school_library at bgleft
    show hanako def_shock_close at centersit2
    with locationchange
    #with locationskip
    
    #play music music_daily fadein 4.0
        
    "Flustered, Hanako closes her book and clumsily stuffs it into her bag, all the while staring at me with a shocked expression."

    show hanako emb_blushing_close at centersit2
    with charachange
    
    ha "S…sure."
    
    show hanako emb_blushing_close at center
    with charamove

    "Shouldering her bag, she pulls herself up, putting ever the slightest strain on my hand in the process."

    show hanako emb_blushtimid_close
    with charachange
    
    "I smile at her, gently, causing her blush to deepen, yet her eyes stay fixed on mine."

    "By this time, all activity around us has stopped, everyone taking in this absurd scene straight from every romance novel ever."

    "I have to give her hand a slight tug to start her walking."

    hi "Come on, let's go get that air."
    
    show hanako emb_blushtimid_close at twoleft
    show bg school_library at bgright
    with charamove_slow

    "Still dazed, Hanako follows me out of the library…"
    
    play sound sfx_alarm_loud
    
    #centered "*BEEP BEEP BEEP*"
    
    show hanako defarms_worry_close at twoleft
    with vpunch

    "Lights flash and sirens blare as we pass through the library's sensomatic doors."

    #not entirely sure what everyone else calls them, but you know those loss-prevention door things.
    
    show hanako def_shock_close at twoleft
    with charachange

    "Hanako's shocked expression turns into one of terror as she realises that it was her that caused this calamity."
    
    show hanako def_shock at center
    show bg school_library at center
    with dissolvecharamovefast
    #with ease
    
    show hanako defarms_shock
    with charachange

    "The librarian eyes her curiously as she runs to the loans desk and upends her bag."

    ha "ImsorryImsorrIforgotIhaditImsorry!"

    "The librarian smiles in a delicate manner, collects the book from the pile of Hanako's note books, and scans it into the system."

    "Librarian" "You take care now."
    
    show hanako cover_worry
    with charachange

    ha "IwillI'msorryI'msosorry…"

    "Hanako packs her bag hurriedly, simply scooping the pile of books and stationary into the maw of her open schoolbag."

    hi "Alright, I think we've caused as much calamity as possible."

    hi "Let's leave these poor people in peace."
    
    show hanako emb_downtimid
    with charachange

    "Dejected, Hanako fixes her gaze firmly on the ground, and follows me out of the library."
    
    hide hanako
    scene bg school_gardens2 at bgright
    with locationskip
    
    play ambient sfx_park fadein 2.0

    "We wander aimlessly, drifting from the main building towards the gardens behind the Great Hall."
    
    show hanako emb_downtimid
    with charaenter

    "Along the way, I gather two cans of iced tea, and hand one to the still-smarting Hanako."

    hi "Here, this'll take your mind off things."

    hi "Nothing like a bit of tea to calm down the mind."

    show hanako emb_timid
    with charachange
    ha "T…thanks."

    "It doesn't take a genius to tell that she's still distracted."
    
    show bg school_gardens2 at bgleft
    show hanako emb_timid at twoleft
    with charamove
    
    with Pause(0.3)
    
    show hanako emb_timid at center
    with charamove
    
    play sound sfx_can

    "I sit down on a nearby bench, and Hanako silently copies me, carefully balancing her schoolbag against the bench before opening her can."

    hi "Lilly's pretty strong, you know. She'll be up and about in no time."

    hi "It was only a minor operation, she'll be back before we know it."
    
    show hanako emb_downtimid
    with charachange

    "Hanako runs her finger around the can's rim slowly, gazing into it as if it held all of the answers to life's questions."

    ha "I…I know all that."

    ha "But I… don't know what to do. I don't know what I can do."

    hi "Eh? What do you mean?"

    "The finger stops in its travel, but remains pressed firmly against the can."
    
    show hanako basic_worry
    with charachange

    ha "If… if it were one of us in that bed, don't you think Lilly would be doing something?"

    hi "I can't say I'm following you here."
    
    show hanako emb_timid
    with charachange

    "Hanako sighs, and takes a sip of her tea."

    ha "I don't think I am either."

    ha "I just… want to do something for her, but I can't."
    
    show hanako emb_downtimid
    with charachange

    ha "I feel… powerless."

    "Her words flow forth on a river of melancholy, but there are undercurrents of something else…"

    "Determination?"

    "That has to be it. Beneath Hanako's obvious lamenting, there is a driving force carrying immense power."

    "In an instant, my vision of Hanako is shattered and rebuilt."

    "She truly cares for Lilly, and wants to help her out…"

    extend " no matter what."

    "The timid Hanako disappears completely from my mind like the thin veil that it is."
    
    show hanako basic_worry
    with charachange

    ha "W…what's the matter?"

    "Shaking myself back into reality, I realise that I've been staring at the flesh-and-blood Hanako whilst musing to myself."

    hi "Oh… er… it's nothing."

    hi "I was just thinking that you've changed since we've met…"

    "Damnit, I'm echoing Lilly's words."

    "But, now, I think I can see the truth behind them."
    
    show hanako basic_bashful
    with charachange

    #hanako blushing but happy

    ha "D…don't be silly."

    "The faint smile turning the corner of Hanako's lips upwards is immensely relieving."

    hi "Say, how about we go together to visit Lilly today?"

    "Hanako gingerly raises the can to her lips, and nods as she takes a drink."
    
    $ renpy.music.set_volume(0.4,1.0)
    play sound sfx_normalbell
    
    stop ambient fadeout 4.0

    "Our interlude is interrupted by the distant ringing of the bells, summoning us back to the classroom."

    stop music fadeout 4.0
    
    hi "We'd best be getting back. We'll leave straight after class, right?"

    ha "Okay."

    #*****************************************
    #inside classroom
    #a22, should you take offence, feel free to veto this next passage.
    #i just kinda got a bit excited of the new misha sprites and she popped up in my mind.
    #scene bg school_scienceroom at bgright
    show bg school_scienceroom at bgright
    with locationskip
    
    $ renpy.music.set_volume(1.0,1.0)

    play music music_normal fadein 0.3
    
    "The first thing I notice as I enter the classroom is a contemplative Shizune carefully cleaning her glasses."
    
    "And, for some reason, the only thing I can think of is the terrified look of the wheelchair-bound student from the start of lunch."

    "I take advantage of Shizune's temporary distraction to whisper in Misha's ear."

    show misha cross_smile
    with charaenter

    hi "Hey… did that guy survive? What did she do to him?"
    
    show misha cross_grin
    with charachange

    "Misha brightens at my attention, seeming all too eager to answer."

    mi "I don't know!"

    extend " But!"

    hi "Wait, don't…!"

    "Too late."
    
    show misha sign_smile
    with charachange
    
    show bg school_scienceroom at center
    show misha sign_smile at twoleft
    with charamove

    show shizu basic_normal at tworight
    with charaenter

    "Misha has already spun around, and is tapping Shizune on the shoulder."
    
    show misha sign_confused at twoleft
    with charachange

    "I reach out and grab Misha's hands before she can start incriminating me."

    "Her warm, soft hands…"

    "Wait! This is no time for fantasy, I need to stop her asking Shizune that question."

    mi "Eh? Hisao? Confessing? To me?"

    hi "No! That's not it at all."
    
    show shizu behind_blank at tworight
    with charachange

    shi "…"
    
    show misha hips_frown at twoleft
    with charachange

    "Misha pouts in an overly fake manner."

    mi "You're mean."

    hi "I just wanted to stop you before you asked Shizune about that."

    hi "I have a feeling she'd take it the wrong way…"

    show misha hips_laugh at twoleft
    with charachange

    mi "Wahahaha~! Hicchan! You make her sound like some kind of bad person!"

    mi "Just take a look at her, there's no way she could be a bad person!"

    hi "Just promise me you won't ask her that."

    mi "Oka~y!"
    
    show misha sign_smile at twoleft
    with charachange
    
    show shizu basic_normal at tworight
    with charachange

    "I release Misha's hands, which immediately go about the business of communicating with Shizune."
    
    show shizu behind_frustrated at tworight
    with charachange
    
    $ renpy.music.set_volume(0.4,1.0)

    "Damnit, I can tell Shizune knows that something is up, but I can't follow a single thing either of them are saying."
    
    "But, from the look on Shizune's face, I can guess."
    
    show shizu cross_angry at tworight
    with charachange

    "I think I may have awoken a demon…"

    show misha cross_smile at twoleft
    with charachange
    
    mi "Hiccha~n! Shizune wants to have a word with you!"

    mi "She wants to remind you that the student council is here for the students, not for their own amusement!"

    mi "Any disciplinary measures put into place are solely for the benefit of the student body, and not for the entertainment of the student council."

    hi "What exactly did you say to her?"

    show misha cross_grin at twoleft
    with charachange
    
    mi "Oh, I can't remember any more."
    
    show shizu behind_frown at tworight
    with charachange

    shi "…"

    mi "Ah, Shicchan has one more thing to say."

    #Misha stern/serious
    show misha cross_frown at twoleft
    with charachange

    mi "That boy will bother you no more."

    "My blood runs cold at the thought of what these two would do to a fellow student…"
    
    hide shizu
    hide misha
    with charaexit

    "Thankfully, I am freed from their stares by the arrival of the teacher and their lesson."
    
    #*****************************************
    #timeskip
    scene bg school_scienceroom
    with shorttimeskip

    "As per usual, the classroom empties in the blink of an eye."

    "It takes mere seconds before Hanako and I are left alone."
    
    stop music fadeout 3.0
    
    show hanako basic_smile
    with charaenter

    hi "So, shall we head straight out?"

    "Hanako simply nods, and we make our way to the bus stop."
    
    scene bg city_busint at bgright
    show crowd 
    with shorttimeskip
    
    $ renpy.music.set_volume(0.29999999999999999, 0.0, channel='ambient') 
    play ambient sfx_crowd_indoors fadein 0.5
    
    play music music_pearly fadein 1.0

    "The first bus into town is surprisingly crowded."

    "I guess a lot of students want to put as much distance between themselves and the school as quickly as possible."
    
    #Curb was misspelled as kerb here. -md01
#    "Hanako and I manage to secure a seat, but by the time the bus pulls away from the kerb, not a single free seat remains."

    "Hanako and I manage to secure a seat, but by the time the bus pulls away from the curb, not a single free seat remains."

    "Getting any conversation out of Hanako in this environment is less likely than blood from a stone, so I look through my bag for something to read."

    "As I pass my fingers over my textbooks, I feel the plush texture of 3-3's gift to Lilly."

    "I almost forgot I had it in here."

    "Extracting the bear, I examine it once again."
    
    show bg city_busint at bgleft
    show crowd at bgleft
    with charamove
        
    show hanako basic_normal at tworight
    with charaenter

    ha "I…is that for Lilly?"

    hi "Wha…? Oh, yeah."

    hi "Her classmates got it for her and asked me to deliver it."

    show hanako emb_downsad at tworight
    with charachange
    
    ha "Oh… I see."

    show hanako defarms_shock at tworight
    with vpunch
    #Hanako sad, followed by a happy-ish Hanako
    
    ha "Hisao!"

    "Hanako's outburst causes me to jump in my seat, and I almost throw the bear in fright."

    hi "What?"

    extend " I mean, what's the matter, Hanako?"
    
    show hanako defarms_worry at tworight
    with charachange
    
    ha "We should get her something too…"
    
    show hanako emb_emb at tworight
    with charachange

    ha "Something to make sure that bear isn't alone."

    "\"Alone.\""

    "There's that word again."

    "I'm sure that Hanako's words are simply a coincidence, but I have a niggling feeling in the back of my head that there's something more to it."

    "I wonder…"

    extend " was Lilly perhaps talking about herself and Hanako?"

    hi "That's a good idea. There's a gift shop at the hospital, maybe we could get something there."
    
    show hanako emb_downdetermined at tworight
    with charachange
    
    "Hanako shakes her head, her stare fixed upon the bear in my hands."

    ha "No… those gifts have no… no…"

    show hanako emb_determined at tworight
    with charachange
    
    ha "…soul…"

    "Again, Hanako's voice has the hard-edged determination that it had earlier in the day."

    "Her eyes are ablaze with some inner passion."

    "But this time, I think I can relate to how she feels."
    
    stop music fadeout 3.0

    hi "You're right."

    hi "Actually, I know just the thing for this occasion, though it will require a slight detour…"
    
    stop ambient fadeout 0.5
    
    #*****************************************
    scene bg city_othello at bgleft
    with shorttimeskip
    $ renpy.music.set_volume(1.0, 0.0, channel='sound')
    play sound sfx_storebell
    play music music_soothing fadein 0.5
    $ renpy.music.set_volume(1.0, 4.0, channel='ambient')
    #background Antique shop
    
    show hanako basic_distant
    with charaenter

    ha "Othello's… Antiques?"

    hi "Yeah, I found it when I was looking for Lilly's birthday present."

    ha "Oh…"
    
    scene bg city_othello at bgright 
    show hanako basic_distant at tworight
    with charamove

    "I make a beeline straight for the Steiff bear I noticed on my last visit."

    hi "It's a little expensive, but I think…"

    show hanako emb_smile at tworight
    #show hanako somethingdeterminedorother
    with charachange
    #Hanako srsbsns

    ha "It's perfect."

    "I had barely lifted the bear off the shelf before Hanako had responded."

    "Slowly, tenderly, she takes the bear from my hands, and holds it to her face."
    
    hide hanako
    with charaexit

    "As she stands there, eyes closed, hugging the bear, I feel somehow saddened that I'm buying this for Lilly and not her."
    
    "Wheels turn in my head, and I start to calculate."

    "If I can constrict myself to drinking only water and eating only what the school provides me, I should be able to pull this off."

    "Under my breath, I thank my parents for the slight swell in allowance for this month."
    
    show bg city_othello at bgleft
    with charamove
    
    "Before Hanako opens her eyes again, I swipe the bear's companion from the shelf, wave to the store owner, and stuff it into my bag."
      
    show shopkeep neutral
    with charaenter

    "I grab a collection of notes out of my wallet, and, whilst pointing at Hanako, I jam the money under another of the bears upon the shelf."

    show shopkeep surprised
    with charachange
    
    "He gives me a puzzled look, and I desperately try to explain to him using sign language."

    "I've watched Shizune and Misha do this a heap of times."

    "Why is he just looking at me like I'm having a fit?"

    "Just as I'm about to walk over and explain everything to him, Hanako releases the bear."

    show bg city_othello at center
    show shopkeep surprised at tworight
    with charamove
    
    show hanako basic_smile at twoleft
    with charaenter
        
    ha "Excuse me, but we'd like to buy this."
    
    show shopkeep happy at tworight
    with charachange

    "Storeowner" "Ah… sure thing, miss."

    "Storeowner" "Is this for you, Lilly?"
    
    show hanako defarms_shock at twoleft
    with charachange

    "Hanako gawks at the store owner, and I close my eyes, wishing that this whole situation had never occurred."

    ha "H…how did you know this was for Lilly?"
    
    show shopkeep thinking at tworight
    with charachange

    "Storeowner" "Well, I remember the young man here from his last visit."
    
    show shopkeep neutral at tworight
    with charachange

    "Storeowner" "He got me to engrave “Lilly” on a music box."

    "Storeowner" "So I thought that might be you… seeing as… oh!"
    
    show shopkeep surprised at tworight
    with charachange

    "It seems that the gears in his head have finally made the connection."
    
    show hanako defarms_worry at twoleft
    with charachange

    hi "Lilly is a mutual friend of ours that's in hospital."

    hi "But I'm surprised you remembered."
    
    show shopkeep happy at tworight
    with charachange

    "Storeowner" "Ah, well, I've got this thing for faces."

    hi "And names, apparently."

    "Storeowner" "Well, it was a unique order."
    
    show hanako cover_worry at twoleft
    with charachange

    ha "So… how much is this?"

    "The store owner looks at me, then at my bag, then at the shelf that conceals my payment for the bear hidden in my school bag."

    show shopkeep thinking at tworight
    with charachange
    
    "Storeowner" "I tell you what, I'll cut you a bargain, a “Get-well” special. Six thousand, even."

    "I grimace, knowing that I left almost twice that on the shelf behind us."
    
    show hanako basic_bashful at twoleft
    with charaenter
    #Hanako happy

    "Hanako, however, is delighted."

    ha "T…thank you!"
    
    show shopkeep happy at tworight
    with charachange

    "I smile as I fish out my wallet for a second time, and give the owner the remains of my cash."

    "Storeowner" "…and here's your receipt. I hope Lilly gets well soon!"

    hi "Cheers."

    ha "Thank you ever so much."
    
    show hanako basic_smile at twoleft
    with charachange
    
    show hanako basic_smile at Transform(xpos=0.1475, ypos=0.1) 
    with ease

    with Pause(0.2)

    show hanako basic_smile at twoleft
    with ease
    #insert command for bowing

    "Hanako bows ever so slightly. It's the first time I've ever seen her be so formal."

    "It's strangely charming."
    
    show shopkeep thinking at tworight
    with charachange

    "Storeowner" "Do you need a bag for that, or…"
    
    show hanako cover_bashful at twoleft
    with charachange

    "Hanako shakes her head."

    ha "No, I'll carry it, thank you."
    
    show hanako emb_downsmile at twoleft
    with charachange

    "True to her word, Hanako carries the bear against her chest, hugging it from behind."
    
    hide shopkeep
    with charaexit
    
    show bg city_othello at bgleft
    show hanako emb_downsmile at center
    with charamove
    
    play sound sfx_storebell
    
    hide hanako
    with charaexit

    "The little bell on the door rings as I put my wallet into my pants."
    
    stop music fadeout 3.0

    "I sigh a little as I feel how light it is compared to when I entered the store."

    "I am such an idiot sometimes."

    return

    #*****************************************
label en_HT2:
    
    scene bg hosp_ext_ss at bgleft
    with locationskip
    
    play music music_night fadein 6.0

    "Hanako and I arrive at the hospital a little later than I would have liked, but the detour was well worth it."
    
    show akira basic_smile_ss at twoleftsit
    show yuuko neutral_up_ss at tworightsit
    with charaenter

    "Sitting on the bench beside the main entrance is Yuuko, and next to her is a young man drinking a beer."

    hi "Hey Yuuko, who's your friend?"

    #sorry delta, I wrote this at work and I can't access the wiki for the character codes and
    #I'll probably forget to change them at home…
    
    show yuuko neurotic_up_ss at tworightsit
    with charachange
    
    show yuuko neurotic_up_ss at tworight
    with charamove

    yu "Hey Hisao, Hanako. This is… um… she's…"

    "She?"
    
    show akira basic_laugh_ss at twoleftsit
    with charachange
    
    show akira basic_laugh_ss at twoleft
    with charamove
    
    aki "Akira Satou. Pleased to meet cha."

    "The young man stands up, and, upon closer examination, it is apparent that she actually is a she."
    
    show yuuko worried_down_ss at tworight
    with charachange

    hi "Er… Hisao Nakai… how'd you do…"
    
    show akira basic_smile_ss at twoleft
    with charachange

    "Akira grabs my hand and shakes it with a bizarre energy."

    aki "Hey there Hanako. Long time no see."
    
    show bg hosp_ext_ss at center
    show akira basic_smile_ss at center
    show yuuko worried_down_ss at right
    with charamove
    
    show hanako emb_downtimid_ss at left
    with charaenter

    ha "H… hi there Akira."

    "The way Hanako and Yuuko are avoiding looking at Akira worries me slightly."

    "I guess that none of them get along."
    
    show akira basic_resigned_ss
    with charachange

    aki "Anyway, my work here is done, so I best be off."
    
    show akira basic_smile_ss
    with charachange

    aki "Good to meet you, Hisao. Thanks for keeping an eye on my sister…"

    "Ah. Satou. Lilly's sister. That should have clicked when I heard the name but I was still confused by the gender switching."
    
    hide akira
    with charaexit
    
    #show bg hosp_ext_ss at bgright
    show hanako emb_downtimid_ss at twoleft
    show yuuko worried_down_ss at tworight
    with charamove

    "But, before I can investigate further, Akira has already hailed a cab, totally ignoring us."
    
    show hanako emb_timid_ss at twoleft
    with charachange

    hi "So, Lilly's sister, eh?"
    
    show yuuko neutral_up_ss at tworight
    with charachange

    yu "She was sent here by Lilly's parents to check on her."

    hi "I thought that was your job?"
    
    show yuuko panic_down_ss at tworight
    with charachange

    yu "Well, it should be, but… I don't know."

    "Yuuko looks she's just been fired; a look of dejection and loss."

    hi "Maybe she was just concerned for her little sister…"
    
    show hanako basic_worry_ss at twoleft
    show yuuko worried_up_ss at tworight
    with charachange

    "Hanako and Yuuko both give me a strange look."

    ha "L…Lilly is the oldest sister in her family…"

    hi "Huh.. how about that… She just seems like she's older than Lilly."
    
    show yuuko worried_down_ss at tworight
    with charachange
    
    yu "There's only a year between them, and Akira has always been chasing Lilly in that regard."
    
    show hanako emb_timid_ss at twoleft
    with charachange

    yu "I guess I'm just used to her looking like that so I didn't really notice."

    hi "I guess that makes sense. So, did you get a day off work or something today?"
    
    show yuuko panic_down_ss at tworight
    with charachange

    "Yuuko's dejection evaporates in a cloud of confusion."

    yu "No, what makes you say that?"

    hi "Well, I thought that you might have had to start by now."
    
    show yuuko panic_up_ss at tworight
    with charachange

    "Panic rises."
    
    yu "I… I.. what time… oh no… I'vegottago!"
    
    show yuuko panic_up_ss at tworightoff
    with slice_in
    show yuuko panic_up_ss at closeright
    with ease
    show yuuko panic_up_ss at tworight
    with ease
    
    "Yuuko's neurotic side surfaces, and she skitters past Hanako and myself, her hands fumbling around in her pockets."
    
    show yuuko neurotic_up_ss at tworight
    with charachange

    yu "Keys… keys… where are my…"

    extend " Oh… Lilly gets out tomorrow… I'llseeyoulater!"
    
    stop music fadeout 3.0
    
    hide yuuko
    with charaexit

    "I meekly wave at the panicking Yuuko as she stumbles over her scooter."
    
    show bg hosp_ext_ss at bgright
    show hanako emb_timid_ss
    with charamove

    hi "Well then… shall we go and see her?"
    
    show hanako basic_bashful_ss
    with charachange

    ha "Yes… let's go."
   
   
    #*****************************************
    scene bg hosp_room2
    with locationskip
    #BG hospital Room
    
    play music music_lilly fadein 1.0
    
    show lilly basic_reminisce_pat at centersit
    with charaenter

    "Lilly sits up in her bed, gently running her finger over a hard-cover book."

    "It could be my imagination, but she almost looks rattled."

    hi "Afternoon, Lilly. Hanako and I came by to visit."
    
    show lilly basic_listen_pat at centersit
    with charaenter

    "In a practised move, Lilly inserts a bookmark into the book, places it on the bedside table, and runs her fingers around the tabletop; memorising its position."

    #"For some reason, I find the little tricks people use to get around their disabilities fascinating."
    #Commented 'cause I'm not sure if that's Hisao or me.
    # That's you.
    
    show lilly basic_smile_pat
    with charachange

    li "Good Afternoon, Hisao, Hanako. How does the day find you?"

    "Her voice is still little more than a whisper; however the croaking of the past few days is starting to subside."

    "At the very least, she seems to be in slightly higher spirits than before."
    
    scene bg hosp_room2 at bgleft
    show lilly basic_smile_pat at twoleftsit
    with charamove
    
    show hanako basic_bashful at tworight
    with charaenter

    ha "Hi Lilly. We… We brought presents."

    #Lilly Smile
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange
    
    li "I'll be discharged shortly. You needn't have gone to the bother."
    
    show lilly basic_smile_pat at twoleftsit
    with charachange

    hi "Well, your classmates got you something, and we felt bad about not getting you anything."

    "I walk to her bedside and fish out the bear from my bag, being careful not to show its contents to Hanako."

    hi "Here, all the students in your class pitched in for this."

    hi "Even Kenji."
    
    show lilly basic_giggle_pat at twoleftsit
    with charachange
    #lilly small laugh

    li "Well, isn't that a surprise."

    "I place the bear in her searching hand, and she immediately runs her fingers through its long fur."

    show lilly basic_smile_pat at twoleftsit
    with charachange
    
    li "My my, it's splendid. Could you please pass on my thanks?"
    
    show lilly basic_oops_pat at twoleftsit
    with charachange

    li "I probably won't be at school until next week."

    hi "Sure thing."
    
    show hanako emb_timid at tworight
    with charachange

    "Hanako nervously steps forward, and I quickly re-seal my bag."

    ha "T… this is from Hisao and I…"
    
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange
    
    show hanako emb_downtimid at tworight
    with charachange

    "Hanako releases the Steiff bear from her embrace, almost sad to see it go."

    "Lilly deftly places the first bear atop the book she was just reading, and takes the bear from Hanako."

    show lilly basic_emb_pat at twoleftsit
    with charachange

    "Upon touching the second bear, her face changes."

    li "Oh, Hanako… you shouldn't have…"
    
    show hanako basic_bashful at tworight
    with charachange

    "Running her delicate fingers around the bear's face brings on a surprised look from Lilly."

    "She pulls the bear to her face to nuzzle with it."
    
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange

    li "It… it smells like you, Hanako."
    
    show hanako emb_blushtimid at tworight
    with charachange
    #Hanako blush

    "I'm glad that Lilly can't see sometimes, as I think that I'm probably blushing harder than Hanako right now."

    show hanako cover_worry at tworight
    with charachange   
    
    ha "I… ah… we…"

    hi "Hanako hasn't let go of it since she saw it. From the instant she saw it we had to get it for you."

    #lilly Fufufu
    show hanako cover_smile at tworight
    with charachange  

    li "Thank you. You didn't need to."
    
    show lilly basic_pout_pat at twoleftsit
    with charachange

    li "And I'm sorry for making you worry."

    "Her face shows just how genuine her apology is."

    show hanako basic_normal at tworight
    with charachange
    #Hanako Relieved/neutral

    "Thankfully, Hanako seems to leave it at that."

    "I don't think I'd be able to explain my vivid daydream to her without causing some kind of incident."

    ha "That's okay, Lilly. We just wanted to do something for you."

    hi "Yeah, I felt kinda bad delivering someone else's gift when I haven't even given you yet."

    hi "And it's only natural that we'd be worried, you're our friend."
    
    show lilly basic_smile_pat at twoleftsit
    with charachange

    li "Well, thank you again. You seem to have incredible taste when it comes to gifts, Hisao."

    hi "Ah, well, Hanako picked it out…"
    
    show hanako def_worry at tworight
    with charachange

    ha "But you found the shop…"
    
    show lilly basic_giggle_pat at twoleftsit
    with charachange

    li "My my, the two of you, working together as a team."
    
    show hanako basic_bashful at tworight
    with charachange

    li "I feel a little left out."

    hi "Well, how about I take you there next time, Lilly?"
    
    show lilly basic_smile_pat at twoleftsit
    with charachange

    li "Hmm, that'd be nice."

    "As we continue our banter, I notice that Lilly never once lets go of her newest bear."

    "Thinking back to the last time I was in her room, she only has a handful of stuffed animals and dolls. No doubt presents from Hanako and her relatives."

    "While I have a suspicion she'd rather a book as a present, the fact that this is from Hanako and I seems to make that fact trivial in her mind."

    "Before long, a nurse wheeling a dinner cart knocks gently on the door and notifies us that hospital visiting hours are ending."

    hi "Catch you later, Lilly."
    
    show hanako basic_bashful at tworight
    with charachange

    ha "Good bye, Lilly."
    
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange
    
    #That grammar gave me cancer -md01
    #li "Good bye, you two. I'll be back at the dorm by tomorrow, if things to go plan, so I'll see you at school next time."
    
    li "Good bye, you two. I'll be back at the dorm by tomorrow, if things go as planed, so I'll see you at school next time."

    li "Thank you for the gift, too. I'll treasure it."
    
    stop music fadeout 2.0
    
    hide lilly
    hide hanako
    with charaexit

    "The nurse bows gently to Hanako and I as we pass, and then pushes the cart into Lilly's room."
    
    #*****************************************
    scene bg city_busint_ss at bgright
    with shorttimeskip
    
    $ renpy.music.set_volume(0.5, 0.0, channel='ambient') 
    play ambient sfx_businterior fadein 1.0
    #BG bus w/ fade through black

    "The silent bus trip lets me reflect on Lilly's situation."

    "Her sickness and the operation following it have brought the three of us closer together, but it feels as if nothing has changed at all."

    show bg city_busint_ss at bgleft
    with charamove
    
    show hanako def_smile_ss at tworight
    with charaenter
    
    "In fact, since we all met, only Hanako has changed."

    "She's become more confident. Even Lilly agrees to that."

    "She's talking to me, and no longer acting like a lost sheep when Lilly's not around."

    "Lilly is still just Lilly, and, apart from sleeping less, I'm still me."

    "She really does seem to care for everyone, no matter how small their problem."

    "And at that, Hanako worries about her as if Lilly were her own mother."

    "Despite that, though, both of them have asked me to look after the other over the course of the past month."

    "And I've promised them both that I would. I wonder, can I really do that?"
    
    stop ambient fadeout 0.5

    "The bus jerks to a halt, ending my reverie."
    
    scene bg school_gardens_ss
    with locationchange
    
    $ renpy.music.set_volume(0.7, 0.0)
    play music music_tranquil fadein 4.0

    "Hanako and I walk back to the dorms in the fading light, and I try to find an opportunity to give Hanako her present."

    "But the stifling silence between us presents no such chance, and we part ways with a courteous “Good Night.”"

    "Damn it. Why is it so much easier to give someone a gift when they're laying in a hospital bed?"

    scene bg school_dormhisao_ss
    with locationskip
    #BG room

    "I throw myself upon my bed, and look up at the ceiling."

    "I'm mentally exhausted, but I have a nagging feeling that I'm not going to sleep well tonight."

    "Just like any other night, actually."
    
    scene black
    with shuteyemed
    
    scene bg school_dormhisao_ss
    with openeyefast

    "I blink, and once again a flutter of blue streaks across my vision."

    "I sit upright and try to track its motion, but it is too fast, disappearing into the air from whence it came."

    "But something else now fills my vision; my bulging school bag."

    "I guess there's no point in holding onto that bear forever."
    
    stop music fadeout 4.0

    "And if I hold onto it for too long before giving it to her, she's going to think I'm weird."

    "Besides, I only bought it for her because we bought one for Lilly."
    
    "It's not like it's got any special meaning or anything."

    "I open my bag, retrieve Hanako's bear, and head outside."

    return

    #*****************************************
label en_HT3:
    scene bg school_gardens_ni
    with locationskip

    $ renpy.music.set_volume(0.1,0.0, "ambient")

    play ambient sfx_cicadas fadein 0.3
    #BG Outside night

    "The cicada's cries have started to die down as evening becomes night."

    "And, as if in defiance of the sweltering days, the night air is surprisingly chilly."

    "I guess that's why no-one's out at the moment."

    "Well, that and studying."

    "Part of my brain chastises me for not using my countless sleeping nights to catch up on that aspect of student life."

    "Ah well, I guess I'll just have to cram in some last-minute work before the exams."

    "It's worked for me before, I'm sure I'll be alright."
    
    stop ambient fadeout 2.0

    scene bg school_girlsdormhall at bgleft
    with locationchange
    #BG dorm hall

    "The dorm halls are similarly vacant. Even the common room is deserted."

    "Normally at least one of the girls would be catching up on their TV at this hour, but not tonight."

    "Honestly, I'm a little relieved."

    "In my rush to sneak Hanako's bear out of the store, I didn't even think about getting a bag for it."

    "Walking around the girls' dorm with a teddy bear would be kinda difficult to explain."

    "Hanako and Lilly's hall seems even quieter than the rest of the dorm."

    "I can almost hear the roar of my blood as it circulates around my ear."

    "You notice so much more in the absence of some things."

    "I wonder if Lilly would agree with me on that?"
    
    show expression Solid("#00000022") 
    show hanako_door_base at right 
    show hanako_door_door at left 
    with locationchange
    
    play sound sfx_doorknock2
    #BG Dorm door

    "I gently rap on Hanako's door, the knocking deafening in the silent hall."

    "No answer."

    "I doubt that Hanako would be asleep at this hour, she seems like more of a night owl than anyone else I've met."
    
    $ renpy.music.set_volume(0.2, 0.0, channel='sound')
    play sound sfx_hammer
    "I knock once more, this time a little harder, just to be sure."

    "No response."

    "Guess she must be asleep after all."

    "Ah well, I can always give it to her tomorrow. Something to commemorate Lilly's return, perhaps."

    "I twist on my heels, and head off down the hallway."

    show bg school_girlsdormhall at bgleft
    with locationchange
    #BG dorm hall
    
    show bg school_girlsdormhall at center
    with charamove

    hi "Looks like I've got to run the gauntlet with you again, little guy."

    hi "Try not to be seen."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='sound')
    play sound sfx_lock

    "The sound of a door unbolting stops me in my tracks."

    "Instinctively, I hide the bear behind my back."

    "But it sounded too close to be Hanako's door…"
    
    scene bg school_girlsdormhall at bgleft
    with charamove

    ha "H…Hisao?"

    ha "Is that you?"

    hi "Hanako? Sorry, did I wake you up?"
    
    play sound sfx_dooropen

    scene bg school_dormlilly 
    show hanagown worry_close at twocenteroff
    show expression Solid("#00000022") 
    show hanako_door_base at right 
    show hanako_door_door at left
    with locationchange
    
    show hanako_door_door at leftdoor
    with charamove

    $ renpy.music.set_volume(1.0, 0.0)
    play music music_moonlight fadein 4.0
    #BG Dorm Door

    "I turn to see Lilly's door slightly ajar, a slither of light bisecting the gloom of the hallway."
    
    show hanagown distant_blush_close at twocenteroff
    with charachange

    ha "N…not as such."

    hi "Do you mind if I come in? I have something for you…"
        
    play sound sfx_door_creak

    show hanako_door_door at leftdooropen
    show hanako_door_base at rightwallopen
    show bg school_dormlilly at roomopen
    show hanagown distant_blush_close at twocenteroff2
    with charamove

    scene white 
    with dissolve

    with Pause(0.1)
    
    scene bg school_dormlilly 
    show hanagown distant_blush_close
    with dissolve

    "The door to Lilly's room slowly swings inwards, revealing Hanako."

    #Show Hanako sad

    "She looks totally crestfallen, her eyes puffy and red, her head cowed."

    hi "Hanako? What's the matter? Isn't this Lilly's room?"
    
    show hanagown worry_blush
    with charachange

    "Hanako nods silently, and steps back from the door."

    "Behind her, I see Lilly's bedspread practically knotted on the bed."

    "A tattered plush rabbit sits amongst the wrecked linen; one that I've never seen before."

    #Fact check; I'm pretty sure Hisao hasn't seen Hanako's room before now. If he has, then use this line instead:

    #"Hanako's tattered plush rabbit sits atop the heap of linen."

    "It's obvious that Hanako was lying there only moments ago."
    
    show hanagown distant_blush
    with charachange

    ha "I… "
    
    extend "I'm sorry."

    hi "Sorry? For what?"

    ha "I shouldn't be in here."
    
    show hanagown distant_cry
    with charachange

    ha "But I just couldn't…"

    #hanako cry

    "A glossy coat of tears paints itself across Hanako's eyes."
    
    show hanagown worry_cry
    with charachange

    "She's deliberately avoiding looking at me; a side effect of her guilt."

    "When a girl starts crying before a guy, he becomes full of compassion, no matter who he is."

    hi "Hey now, there's nothing wrong with it, right?"
    
    show hanagown normal_cry
    with charachange

    hi "I'm sure Lilly wouldn't mind."

    "I realise that I'm still hiding the bear from Hanako, an instinctual reaction, albeit a stupid one."

    hi "Look, here, I brought you a present."
    
    show hanagown normal_cry2
    with charachange

    "I offer the bear to Hanako, who initially shies away from my outstretched arms."
    
    show hanagown worry_cry2
    with charachange
    #Hanako surprised
    
    "But, as her tear-stained eyes recognize the form before her, shock spreads across her face."

    "She stares at it in disbelief, and I feel as if the world has ground to a halt."

    "Eventually, she reaches out with shaking hands, and lifts the bear from my palms."

    "Her grip on the bear is like that of a new mother holding her child for the first time; tender yet protective."

    hi "So, what do you—{w=.3}{nw}"
    
    show hanagown irritated_close
    with None
    
    play sound sfx_impact
    with vpunch
    
    extend " oof!"

    "I barely start to speak before Hanako lurches forward into my chest, wedging the bear between us."
    
    show hanagown irritated_alt
    with charachange

    ha "How…? When…?"

    hi "Well, er, when I saw you in the shop I thought you looked good together."

    hi "So I secretly bought it for you while you were distracted."
    
    show hanagown smile_alt
    with charachange

    ha "It's… t—thank you."
    
    show hanagown smile_blush
    with charachange

    "Hanako stares at the bear, her guilt-ridden face now flooded with a strange wonder."

    #Hanako neutral

    hi "Well… I'd best be off…"
    
    show hanagown normal
    with charachange

    "Hanako's arm shoots out before I can even notice, grabbing my sleeve."
    
    stop music fadeout 14.0

    ha "D—don't go. Not yet…"

    "Amazingly, she never takes her gaze off the bear."

    hi "Sure, I guess I can stay for a bit."

    hi "Let me put the kettle on."
    
    show hanagown distant
    with charachange

    "Hanako nods, and slowly releases my sleeve."
    
    show hanagown distant at tworight
    show bg school_dormlilly at bgright
    with charamove

    "She stumbles backwards, and sits awkwardly on Lilly's bed."

    "As I fill the kettle and switch it on, she fumbles through Lilly's bed sheets until her hand rests on the tattered rabbit."

    "Without looking, she scoops up the rabbit and brings it into her field of vision, gently resting it against the bear on her lap."

    "What a strange sight we must make; Hanako staring intently at two toys whilst I watch her from across the room."

    "The kettle whistles, and I fill the waiting pot with the steaming water."
    
    show hanagown distant
    show bg school_dormlilly at bgleft
    with charamove

    "As if guided by some invisible hand, I place the teapot on Lilly's small table, and then sit down next to Hanako."

    "I've been in Lilly's room a number of times, but this is the first time I've ever touched her bed."
    
    "The springs respond a little as I sit, and I can faintly smell Lilly on the sheets."

    "But, right now, our blind friend is miles from my mind."

    "There's something to Hanako's reaction that makes me incapable of thought."

    "I didn't exactly expect her to be ecstatic, but I didn't expect her to just stop, either."

    "Still, she certainly looks a little cheerier than she did when she first opened the door."

    "… I think."

    hi "So, I guess your friend there isn't alone anymore, right?"
    
    show hanagown worry
    with charachange
    #Hanako Shocked

    ha "Eeh?"

    "Hanako starts a little at my question, as if she had forgotten that I was in the room entirely."

    "Were I quicker on my feet, I'd think of something to say."

    hi "Your friend, the rabbit. He's not alone anymore now, right?"

    hi "He looks pretty old now, too."
    
    show hanagown normal
    with charachange
    #Hanako neutral

    ha "I… I guess you're right."
      
    show hanagown distant
    with charachange
    
    play music music_hanako fadein 4.0

    ha "It's just that… no-one has bought me something like this…"
    
    extend " since then."

    "Something in the back of my brain tells me that I shouldn't be pushing the issue."

    hi "Then?"

    "It just seems that the back of my brain is about a second behind my vocal cords."
    
    show hanagown distant_alt
    with charachange
    with Pause(0.5)
    show hanagown normal
    with charachange

    "Hanako closes her eyes for a second, clutches both of the animals before her for a moment, then looks at me."

    #Hanako srs bsns

    ha "I grew up with foster parents."

    ha "They were kind to me, but I could never bring myself to ask anything of them."

    ha "I was already imposing on them enough just by living with them."
    
    show hanagown distant
    with charachange

    ha "But, before that… before that…"
    
    show hanagown worry
    with charachange
    #Hanako sad

    ha "Before that, my parents bought me Petra."

    "At the mention of her parents, she clutches the rabbit slightly tighter."

    ha "He and I were the only things to survive the fire."

    hi "Things?"

    ha "Everything burnt. My house, my toys, my parents… everything."

    ha "I don't remember much, but I know when the firemen woke me up in the snow, all that was left was Petra."

    show hanagown distant
    with charachange
    
    ha "Since then, all we've had was each other."

    #Hanako neutral

    hi "Have… you ever told anyone else this?"
    
    show hanagown normal
    with charachange

    "Hanako shakes her head."

    ha "Not even Lilly."

    hi "Really?"

    ha "Really."

    #Really? Really!

    #Also, so long 12.0 wpl

    "I lean back onto Lilly's bed."

    "So, Hanako hasn't told Lilly everything."

    "The mere thought of that spins my head around."

    "I remember Lilly mentioning that Hanako once told her everything. To think that she was keeping things from her…"

    "I wonder what else Lilly doesn't know?"

    #And thusly, the Onee-sama intelligence network was brought into disrepute."

    hi "So… why are you in here?"
    
    show hanagown normal_blush
    with charachange
    #Hanako Embarrassed
    
    stop music fadeout 6.0

    ha "Ummm… I… I t—thought I heard something in here… a—and I came to check it…"

    hi "You're a terrible liar."

    hi "I liked it better when you were being honest."

    show hanagown distant_blush
    with charachange
    #Hanako Looing down embarrassed.

    "There is a brief pause as Hanako avoids my gaze."

    ha "My…"

    extend " my light broke."

    hi "Your light?"

    "Still avoiding my gaze, she rubs Petra's elongated ears."

    ha "I…"
    
    show hanagown normal_blush
    with charachange
    play music music_heart fadein 4.0

    ha "Promise you won't laugh."

    "This is getting interesting…"

    hi "I promise."
    
    ha "I'm… afraid of the dark."

    hi "Huh? But during the festival you were messing around in the hall all the time."

    hi "That was pretty dark, wasn't it?"
    
    show hanagown distant_blush
    with charachange

    ha "That's… different."

    ha "I can't sleep without my light."
    
    show hanagown worry_blush
    with charachange

    ha "But now it's broken."

    ha "Normally I just sneak in with Lilly when this happens, but…"

    #Hanako sad

    "I need a distraction… now…"

    hi "Ah, the tea's getting cold, would you like a cup?"

    "I am the king of suave."
    
    show hanagown normal
    with charachange
    #Hanako neutral

    ha "Ah… please."

    "I deftly pour the two cups, and pass Hanako hers."

    "She shuffles a little to allow both of her “friends” to sit on her lap without her holding them."

    hi "So, your light is broken, and there's no Lilly here."

    hi "Whatever will you do?"
    
    show hanagown drunksmile
    with charachange

    ha "Well… ah… Lilly keeps a spare for me in here."

    "How very… Lilly."

    hi "I see. So you're going to hijack her room?"
    
    show hanagown worry_alt
    with charachange
    #Hanako happy embarrassed

    ha "N… it's not like that."

    hi "Sure it isn't."
    
    show hanagown drunkpout
    with charachange
    #Hanako pout

    ha "You said you wouldn't laugh…"

    hi "I'm not laughing, I'm making a joke."

    hi "There's a difference, you know."
    
    show hanagown normal_alt
    with charachange
    #Hanako embarrassed/happy
    
    ha "You're mean."

    hi "Well, in that case, I guess I won't have to buy you any more gifts…"

    show hanagown smile
    with charachange
    #Hanako happy/smile

    ha "Meanie."

    "This is the first time I think I've ever seen Hanako smile in the absence of Lilly."

    "It's sobering, yet relaxing."

    "I smile, and place my cup on Lilly's bedside table."
    
    play sound sfx_alarmclock

    "Clock" "The time is… Eleven… fourteen… PM."

    hi "Wha? How did it get this late?"

    show hanagown worry_alt
    with charachange
    #Hanako shocked/worried

    ha "I… I'm sorry. I talked too much…"
    
    show hanagown normal
    with charachange
    
    hi "No, it's not that."
    
    hi "I already tempted fate coming here."

    hi "If I leave now I know I'll be spotted."

    ha "Oh…"

    ha "Well…"
    
    show hanagown distant_blush
    with charachange

    ha "You could… stay here…"

    "Whatthehelldidshejustsay?"

    "Wait wait, calm down."

    "I don't think she meant…"

    hi "Sure."

    show hanagown smile
    with charachange
    
    "Damn it, again?"

    "I need to practice the whole “Think before you speak” thing a whole bunch more."

    hi "I'll sleep on the floor."
    
    show hanagown distant_blush
    with charachange

    ha "No… I couldn't…"

    hi "It's alright, I've slept on worse."

    hi "Besides, girls belong in beds, guys belong on the floor. It's the natural order."

    show hanagown drunknormal
    with charachange
    #Hanako blush/embarrassed

    ha "O…okay then."
    
    show hanagown drunknormal at tworight
    show bg school_dormlilly at bgright
    with charamove

    "I gather up the things from Lilly's table and arrange them on her desk."

    "Upending the table leaves me with a fair bit of space."

    "And it's not like it's sleeping on bare concrete."
    
    show hanagown smile at tworight
    with charachange

    ha "Ah… wait a second…"
    
    show hanagown smile at offscreenleft
    with charamove

    "Hanako places her two plush toys on Lilly's bed and runs out the door."
    
    show hanagown smile at center
    show bg school_dormlilly at center
    with charamove

    "Seconds later, she returns, her arms full of linen and a comforter."

    #Do you guys call them doonas or quilts? Or is it comforter?

    ha "You… you can sleep on these."

    show hanagown drunkdistant
    with charachange
    
    ha "They… they're mine."

    "Huh. So she just went and stripped her bed."

    "I thought she might have had a spare set or something."

    "…"

    "Wait a minute… That means when she said she sneaks into Lilly's room…"

    "…She means she sneaks into her bed…"

    #BG flashback?

    li "Oh… I know something that will help you sleep, Hanako…"

    #BG return

    "Be still my raging hormones…"
    
    show hanagown smile
    with charachange
    
    hi "T…thanks a bunch."
    
    hide hanagown
    with charaexit
    
    show bg school_dormlilly at bgright
    with charamove
    
    play sound sfx_rustling
    
    "I take the wad of fabric from Hanako, and start arranging them on the floor."

    "It's not that hot tonight, so I guess I'll sleep on the comforter."
    
    play sound sfx_switch
    
    scene bg school_dormlilly_ni at bgright
    with locationchange

    "Once I'm done arranging my makeshift bed, I turn off the lights."

    "A faint glow emanates from the corner of the room; Lilly must keep Hanako's backup night light constantly plugged in."

    "Its light is barely enough to see by, but it does keep the darkness at bay, and shouldn't really affect my sleep."

    "Hanako quickly adjusts Lilly's messy bed and climbs in, being sure to keep Petra and the Steiff bear within reach."

    scene black
    with shuteye
    
    "I settle myself down, and close my eyes."

    "Hanako's scent instantly fills my head, and I have to fight off a wave of dizziness."

    "As I suspected, I don't exactly drift off to sleep."

    "My body feels tired, but my mind just won't let up."
    
    stop music fadeout 6.0

    "The combination of the drugs in my system and the girl in the same room are keeping me wide…"

    ha "I used to have another friend."
    
    scene bg school_dormlilly_ni at bgleft
    show hanagown distant_ni at tworight
    with openeye

    hi "Hmm?"

    ha "He was a good friend."
    
    show hanagown distant_alt_ni at tworight
    with charachange

    ha "I think… I think he loved me."
    
    show hanagown normal_ni at tworight
    with charachange

    ha "But… when I asked him, he ran away."

    ha "If I never asked him, he would still be here."

    ha "Hisao…"
    
    show hanagown worry_ni at tworight
    with charachange

    ha "Please don't run away."

    hi "Why would I run away?"
    
    show hanagown normal_ni at tworight
    with charachange

    ha "Just… don't."

    hi "Okay."
    
    ha "Hisao?"

    hi "Mm?"
    
    show hanagown smile_ni at tworight
    with charachange
    
    ha "Thank you."

    extend " For everything."
    
    scene black 
    with shuteye
    
    window hide
    
    with Pause(1.5)

    #Far out, there must be like an average of 2 wpl in this scene.
    # Farking dailouge.
    #Now, the question that has been gnawing at me for ages…
    #Will Hanako sneak into Hisao's bed tonight?
    #PS that won't mean H though.
    #Also there will be an omake thing unlocked after this, kinda like "Future"
    #it will be the whole Hanako's friend getting pwned by a truck.
    #that is, of course, if I keep the current ending.

    return

    #*****************************************
label en_HT4:

    scene black 
    with dissolve
    #bg black
    play sound sfx_alarmclock

    "Clock" "The time is… seven… oh one… am."

    "Clock" "The time is… seven… oh one… am."

    scene bg school_dormlilly
    with openeye
    #bg dormlilly with eyes open

    "Urgh. I don't think I'll be counting last night on my top ten list of “good night's sleeps.”"

    scene bg school_dormlilly at bgright
    with charamove
    
    "Even as I roll over to try and sit up, I can hear my back protesting. I feel like an old man."

    "Clock" "The time is… seven… oh two… am"

    hi "Yes, I get that… how do I shut this thing off?"

    show hanagown smile at right
    with charaenter
    
    play music music_dreamy fadein 4.0
    #show Hanako neutral smile at right

    ha "Oh… you're awake…"
    
    scene bg school_dormlilly at bgleft
    show hanagown smile at center
    with charamove

    "I look up from my prone position on the floor, directly up at a smiling Hanako."

    "The morning light streams through the window, striking her face at a strange angle."

    "Combined with a male's typical morning…'situation'… this could become embarrassing."

    hi "Er, yeah… The, uh… clock… alarm…"

    "I struggle to bury myself deeper in the sheets whilst I calm myself."
    
    show hanagown normal_alt
    with charachange

    ha "Yes, Lilly does set it quite early, doesn't she?"
    
    show hanagown smile
    with charachange
    
    show hanagown smile at twoleft
    with charamove

    "Hanako crawls along the bed, still in the nightgown she was wearing last night."

    "She presses a couple of buttons on the clock, silencing the alarm."
    
    show hanagown normal at twoleft
    with charachange
    
    ha "At least this way we'll have a chance to clean up before classes."

    hi "Yeah, let's clean this place up. Lilly comes back today, remember."
    
    show hanagown smile at twoleft
    with charachange
    #hanako neutral bigsmile

    ha "How could I forget?"
    
    play sound sfx_rustling
    
    show hanagown smile at center
    show bg school_dormlilly at center
    with charamove
    
    "Having sufficiently calmed myself, I throw back Hanako's sheets and sit up; causing my back to crack in the progress."
       
    hi "Ouch…"
    
    show hanagown worry
    with charachange
    #Hanako embarrassed concerned

    ha "Are you alright?"

    hi "It's okay, my back's just a little stiff from sleeping on the floor…"

    show hanagown distant_blush
    with charachange
    #Hanako neutral looking down

    ha "S…sorry. I shouldn't have made you stay here…"
    
    show hanagown irritated_alt
    with charachange

    "I stand up, and pat Hanako on the head."

    hi "Don't be silly. I had to stay here, remember?"

    hi "A sore back is a lot easier to deal with than explaining why I was leaving the girl's dorm after curfew…"

    show hanagown normal
    with charachange
    
    ha "I… guess you're right."

    hi "Come on. Let's make this place ready for Lilly's triumphant return, eh?"

    show hanagown smile
    with charachange
    #hanako embarrassed smile

    ha "Okay…"
             
    show bg school_dormlilly
    with shorttimeskip
    
    "It doesn't take us much time at all to clean up the small dorm room to its usual glory."

    "Finally, Hanako bundles up the linen that she loaned me, and heads for the door."

    #Hanako embarrassed look down smile
    show hanagown smile_blush
    with charaenter

    ha "Well… I'll see you later."
    
    show hanagown smile
    with charachange

    ha "T…thanks for sticking around."

    hi "Not a problem at all."
    
    show bg school_dormlilly at bgright
    show hanagown smile at left
    with charamove
    
    play sound sfx_dooropen
    
    hide hanagown
    with charaexit
    
    play sound sfx_doorclose
    with Pause(1.5)

    "Without saying a further word, she skips out of Lilly's room and back into her own, shutting her door behind her."

    #hide hanako
    
    show bg school_dormlilly at bgleft
    with charamove
    
    stop music fadeout 3.0

    "I take a quick look to assess the state of Lilly's room."

    "Deciding that all is well, I head back to my room for a quick shower before breakfast."
    
    #*****************************************
    scene bg school_hallway3 
    with shorttimeskip
    #bg classroom with ? some kinda timeskip?

    "Even with the head start Lilly's alarm gave me, I still find myself rushing to class in order to beat the bells."

    "I guess I dawdled through my morning routine knowing that I had more time than usual."
    
    play sound sfx_dooropen
    
    scene bg school_scienceroom at bgright
    show hanako cover_distant at left
    with locationchange
        
    "Not surprisingly, Hanako is already in her seat at the back of the class, lazily gazing out the window."

    "I'd like to go an say hello, but an obstacle blocks my path."
    
    hide hanako cover_distant at left
    with charaexit
       
    mi "Hi—sa—o~!"
    
    show bg school_scienceroom at center
    with charamove
    
    play music music_happiness fadein 4.0
    
    show misha hips_grin at twoleft
    show shizu behind_blank at tworight
    with charaenter
    #show misha at twoleft and shizune at tworight

    "Make that two obstacles."

    hi "Yes ladies, how can I help you this morning?"
    
    show shizu basic_normal at tworight
    with charachange
    
    show misha sign_smile at twoleft
    with charachange

    "A flurry of hand signals pass between the pair before Misha poses Shizune's question."

    mi "We were wondering if you could help us find a boy."

    hi "Oh, really? I didn't think either of you would be the type for blind dates…"
    
    show misha perky_confused at twoleft
    with charachange

    "There is a brief lag as Misha relays my response to Shizune, but I receive the desired effect."

    show shizu cross_angry at tworight
    with charachange
    # shizune pouting/angry
    
    show misha hips_laugh at twoleft
    with charachange

    mi "Wahahaha~! Hisao, it's not like that! I should hit you for being so insolent though!"
    
    show shizu adjust_smug at tworight
    show misha hips_smile at twoleft
    with charachange

    mi "But we need your help, so I'll save that for later, when you're not looking!"

    "Part of me wants to laugh that off, but deep in my heart, I now fear turning my back to either of the girls before me…"

    hi "Okay then, I'll help. Who's this boy you're looking for?"
    
    show misha perky_smile at twoleft
    show shizu behind_blank at tworight
    with charachange

    mi "Well, this morning, no boys entered the girls' dorm, but one left."
    
    show misha sign_smile at twoleft
    show shizu basic_normal at tworight
    with charachange

    mi "Don't you think that's strange, Hisao?"

    hi "Not really… why would that be strange?"
    
    show misha cross_grin at twoleft
    with charachange

    mi "Hahaha~ Hisao! Do the math!"
    
    show misha sign_smile at twoleft
    with charachange

    mi "If no boys went into the dorm in the morning, but one left…"
    
    show misha perky_smile at twoleft
    show shizu behind_blank at tworight
    with charachange

    mi "That means that…?"

    hi "I've got no idea. You'll have to enlighten me…"

    show misha cross_laugh at twoleft
    play sound sfx_impact
    with vpunch
    #misha more lol

    "Misha slaps me hard on the back, causing me to lurch forward into my desk."

    mi "It means that you stayed the night in the girl's dorms, doesn't it?"

    "I should have known they had already figured out this much…"

    hi "Perhaps. But how does that concern either of you?"
    
    show misha sign_smile at twoleft
    with charachange
    show shizu basic_normal at tworight
    with charachange
    show misha perky_smile at twoleft
    with charachange
    #signing between the girls

    mi "We are the student council, remember?"
    
    show shizu behind_blank at tworight
    with charachange

    mi "Part of our duties involves knowing about the goings on of the student body."
    
    show shizu adjust_happy at tworight
    with charachange

    "As if by some cue form Misha, Shizune pushes her glasses up on her nose to accentuate the point."

    "I wonder if they've rehearsed this move before?"

    hi "I would think that would count at snooping, wouldn't you?"
    
    show misha hips_grin at twoleft
    play sound sfx_impact
    with vpunch

    "Once again Misha assaults my already strained back."
    
    mi "It's not snooping if it's your job, right, right?"
    
    stop music fadeout 3.0

    "Thankfully, Mutou chooses this moment to appear, putting an end to Misha's assault."
    
    hide misha
    hide shizu
    with charaexit
    
    show bg school_scienceroom at bgleft
    with charamove
    
    show muto normal
    with charaenter
    
    #hide shizune and misha
    #show muto from right

    mu "Ah… now everyone… exams."

    mu "Get ready for them."
    
    show muto smile
    with charachange

    mu "Now, onto today's lesson…"
    
    "And that is the extent of today's warnings about the upcoming exams."

    "Still, he's rambled on about them enough over the past few weeks, so I guess he's just about as over them as we are."

    "Then again, it's not like he has much to stress about at this time…"

    "And his rambling lectures seem to not have wavered at all in what is generally considered a time of crisis for students."
    
    hide muto
    with charaexit
    #hide muto with dissolve

    "But, as he drones on, I can't help but think back to last night."

    "Hanako seemed pretty weird last night."

    "Even though she was letting me in on her past, she somehow seemed happy."

    "As if it were somehow relieving to let go of the secrets she's been holding onto for so long."

    "Yet, there was that one last confession… her friend that “ran away.”"

    "I know I shouldn't press the issue, but I guess I'm too curious for my own good."

    "Maybe I'll ask Lilly if she knows anything."
    
    #*****************************************
    scene bg school_hallway3 
    show crowd
    with shorttimeskip
    play sound sfx_normalbell
    #sfx bells
       
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 0.5

    "Like a pack of wild animals, students rush off to devour their food in their respective areas."
                
    show hanako basic_bashful
    with charaenter

    "Through the confusion, I spy Hanako, who simply points upwards and lifts a small bag so that I can see it."

    "It doesn't take much thought to decipher what she means."
    
    stop ambient fadeout 0.5
    
    scene bg school_staircase1 
    with locationskip

    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')
    play ambient sfx_rooftop

    "I push through the crowds and head for the stairs to the roof."

    play sound sfx_door_creak
    $ renpy.music.set_volume(0.5, 0.5, channel='ambient')
    
    scene white 
    with dissolve

    with Pause(1.0)
    
    show bg school_roof at bgright
    with locationchange
    #bg roof1 with transition

    "I get up the stairs before Hanako, but I am not the first onto the roof."
    
    play music music_emi fadein 4.0

    show emi excited_laugh at twoleft
    show rin basic_awayabsent at tworight
    with charaenter
    #show emi and rin
    #going for the record of sprites in a scene!

    emi "…then like BLAM! it's all gone."
    
    show emi excited_happy at twoleft
    show rin relaxed_doubt at tworight
    with charachange

    rin "I never knew you could do that with peanut butter…"
    
    show emi basic_happy at twoleft
    with charachange

    emi "Oh, hey Hisao! You should hear this story! I was…"

    hi "Er, something tells me I'm better off not knowing."

    show emi sad_shy at twoleft
    with charachange
    #emi ???

    emi "Oh, really? I guess that's okay too."
    
    show rin basic_deadpansurprised at tworight
    with charachange

    rin "If you're not here for the story, then why are you here?"

    hi "I was just going to have some lunch with…"

    ha "H…Hisao? Are you here yet?"

    hi "…Hanako."
    
    show hanako defarms_worry at offscreenright
    with None
    
    show bg school_roof at center
    show emi sad_shy at left
    show rin basic_deadpansurprised at center
    show hanako defarms_worry at right
    with charamove
    #show Hanako, if she'll fit… surprised
    
    show emi basic_grin at left
    show rin basic_absent at center
    with charachange

    emi "Oh, hiya there Hanako!"

    ha "E…Emi… Rin… Hello…"

    "Hanako seems a bit surprised to see the crowd on the roof, but it takes her only a second to regain her composure."

    show hanako basic_normal at right
    with charachange
    #hanako neutral.

    ha "Hisao… If you'd like, I have some sandwiches."
    
    show hanako cover_distant at right
    with charachange

    ha "Normally I make them for Lilly, but I forgot she wasn't here, and…"

    hi "Sounds good. I can't turn down a free lunch, can I?"
    
    show emi basic_closedhappy at left
    with charachange
    #Emi delighted

    emi "Ohohoh! A shared, hand-made lunch!"

    emi "Isn't this exciting, Rin?"
    
    show rin relaxed_nonchalant
    with charachange

    "Rin gazes lazily through the fence and out over the town."
    
    rin "If you say it is then it must be."

    show hanako emb_downtimid at right
    with charachange
    #haanko embarrassed looking down

    ha "It… it's nothing like that…"

    ha "I just made too much for me and…"
    
    show hanako emb_timid at right
    with charachange

    ha "…would you like some too, Emi?"
    
    show emi excited_amused at left
    with charachange
    #Emi big smile

    "Emi smiles hugely, leaning forward to place her chin in her hands."
    
    emi "Oh, no, not at all. I just want to watch this blossoming romance from the front row…"

    show hanako defarms_shock at right
    with charachange
    
    $ doublespeak(hi, ha, "It's not like that!", "It's not like that…")
    
    show emi excited_laugh at left
    with charachange
    #emi laughs

    emi "You two are just classic…"
    
    show rin basic_absent
    show hanako def_worry at right
    with charachange

    rin "So when will Lilly be fixed?"
    
    show emi basic_grin at left
    with charachange

    hi "She gets out today, and should be back here some time around evening."
    
    show rin negative_spaciness
    with charachange

    rin "That's good. It's no good being stuck in a place at a time."

    hi "I… guess you're right there."

    "Rin seems to refuse making eye contact with anyone she's talking to."

    "Her gaze has shifted from the town to the school's grounds, endlessly searching for… who knows what."

    show emi sad_annoyed at left
    with charachange
    
    emi "Would you stop stalling?"
    
    show emi basic_happy at left
    with charachange

    emi "I want to see you eat her sandwiches!"
    
    show emi excited_joy at left
    with charachange

    emi "Make sure to tell her that they're delicious, even if they aren't!"
    
    show emi excited_proud at left
    with charachange

    emi "ESPECIALLY if they aren't!"

    "Emi seems to have whipped herself into a frenzy over this, and I'm starting to fear for all of our safety."

    "The “safety” fence up here doesn't look like it would stop an Emi at full steam."
    
    show hanako emb_downtimid at right
    with charachange

    ha "P…please. They're probably not that good…"
    
    show emi basic_happy at left
    with charachange

    emi "That's it! Perfect!"
    
    hi "Fine then. Hanako, I'd love one of your sandwiches."

    show hanako emb_smile at right
    with charachange
    #hanako embarrassed yet smiling, Emi expectant

    "Hanako unwraps the small bag, and produces a sandwich from it."

    ha "H…here you go…"
    
    show emi basic_concentrate at left
    with charachange

    "Emi looks on like a seagull watching a tourist eating chips."

    "Her eyes are locked on the sandwich as I take it from Hanako and slowly move it to my mouth."

    "I can almost feel her breathe in as I take a bite, and the tension in the air as I swallow."

    hi "Not bad. Not bad at all…"
    
    show emi excited_circle at left
    show rin basic_surprised
    show hanako defarms_shock at right
    with vpunch
    #emi angry? Or something like that

    emi "DO IT PROPERLY!"

    "Emi's outburst makes everyone jump, including the disinterested Rin."

    hi "Woah… okay…"

    hi "They're… delicious…"

    show emi basic_closedgrin at left
    show hanako def_worry at right
    with charachange
    #Emi :3

    emi "See? Doesn't that feel so much better?"
    
    emi "It's a proper love-love rooftop lunch now."

    hi "I think you need your head read…"
    
    show rin basic_deadpanamused
    with charachange

    rin "I've been telling her that for years."

    "Coming from Rin, that kind of comment has got to hurt."

    "But Emi doesn't even seem to notice, too wrapped up in her own fantasy world."

    hi "Can we eat our lunch in peace now?"

    show emi sad_grin at left
    with charachange
    #emi not :3

    emi "What? Oh, yes, go ahead."
    
    stop music fadeout 6.0

    "Emi, having seen what she wanted to, seems to be largely ignoring us now."
    
    hide emi
    hide rin
    with charaexit
    
    show bg school_roof at bgleft
    show hanako def_worry at center
    with charamove
    
    #hide emi and rin

    "Hanako sits against the outside wall of the stairwell, and I take up a position near her…"

    #Hanako neutral looking down

    "…though not near enough to attract Emi's attentions again."
    
    play music music_another fadein 6.0

    hi "Thanks for these. I totally forgot about lunch this morning."
    
    show hanako emb_emb
    with charachange

    #hanako embarrassed, looking down smiling

    ha "You're welcome. I just made too much though…"

    hi "I guessed as much. It was a pretty crazy morning."
    
    show hanako emb_downsmile
    with charachange

    ha "Yeah."

    hi "Say, should we throw a little “Welcome home” party for Lilly tonight?"

    hi "I'll go to the shops and get a cake and stuff, if you want to set up her room?"
    
    show hanako basic_smile
    with charachange

    #hanako neutral smile

    ha "That sounds nice."

    hi "Then it's settled."
    
    #stop music fadeout 6.0

    hi "I'll meet you at Lilly's room at about six, 'kay?"
    
    show hanako cover_bashful
    with charachange

    ha "Okay, I'll be there then."
    
    show emi sad_grin at leftdoor
    with vpunch
    #emi, at right, smile
    
    #play music music_emi fadein 0.000001

    emi "Be where when?"
    
    show hanako cover_distant
    with charachange

    "Damnit, I forgot that she was up here."
    
    show bg school_roof at center
    show emi sad_grin at twoleft
    show hanako cover_distant at tworight
    with charamove

    hi "Oh, it's nothing. We were just planning our evening."

    emi "Oooh a date already?! But she only just started making you lunches!"
    
    show emi basic_happy at twoleft
    with charachange

    emi "You sure move fast, Hisao!"

    hi "No, you klutz. It's for Lilly."

    show emi excited_proud at twoleft
    with charachange
    #emi poke tounge

    emi "I know that. But you're both too easy to tease."
    
    show emi basic_closedgrin at twoleft
    with charachange

    emi "Say hi to Lilly for me."
    
    show emi basic_closedgrin at offscreenleft
    with charamove
    
    #stop music fadeout 6.0

    "With that, Emi walks past Hanako and I, towing Rin by her empty sleeve."
    
    show bg school_roof at bgleft
    show hanako cover_distant at center
    with charamove

    "I look across to Hanako, half expecting her to be buried inside herself again."
    
    show hanako basic_smile
    with charachange
    #Hanako neutral, slight smile

    "However, she seems perfectly fine with the situation."

    hi "You alright, Hanako?"
    
    show hanako basic_normal
    with charachange

    ha "Hmm? Oh… yes."
    
    show hanako basic_bashful
    with charachange

    ha "I was just thinking that she's… a nice person."

    hi "Who?"

    ha "Emi. She's… nice."

    hi "But she was just teasing us…"
    
    show hanako emb_emb
    with charachange

    "Hanako shakes her head."

    ha "That's just her way of playing."

    ha "And she's a good friend to Rin, too."

    ha "That means she's nice, right?"

    hi "I guess you're right."

    hi "Anyway, we should be headed back down now, right?"

    hi "The bells are going to go off any second now, and they're really loud here…"
    
    show hanako basic_smile
    with charachange

    ha "Oh…okay."
    
    stop music fadeout 8.0

    hi "I'll duck off straight after class to go get a cake for Lilly, so I'll see you at her room at six, okay?"

    ha "S…sure."
    
    show hanako basic_bashful
    with charachange

    ha "I'll see you then."
    
    hide hanako
    with charaexit
    
    play sound sfx_doorclose
    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')
    
    scene black
    with dissolve

    with Pause(1.0)
    
    scene bg school_staircase1
    with locationchange
    
    play sound sfx_normalbell

    #sfx bells
    #bg fade out
    
    stop ambient fadeout 2.0

    "The bells of the carillon clatter into life just as we close the door behind us, their deafening peal recalling the students back to the boredom of the afternoon classes."

    return

    #*****************************************
label en_HT5:
    
    scene bg school_staircase1
    with locationchange

    #aslo, this scene tok forever. If it fails, please let me know.
    #Yes, Hanako at the end is a little OOC. I'm not sure if it's overly so, nor do I intend to use "crazy" as an excuse.
    #Please let me know if it's too far over the top, or if it needs explaination or something.

    scene bg school_dormlilly 
    with shorttimeskip
    #bg dormlilly with timeskip
    show hanagown normal at tworightsit
    show lilly basic_smile_paj at twoleftsit
    with charaenter
    #show lilly and Hanko in pyjamas
    
    $ renpy.music.set_volume(0.80000000000000004, 1.0, channel='music')
    play music music_one fadein 4.0
    
    li "My my, you really shouldn't have…"

    "Lilly, still a little hoarse from her operation, seems a little overwhelmed by our little reception."

    hi "Nonsense. It's only proper to have a welcoming home party for those that have risked their lives."

    show lilly basic_giggle_paj at twoleftsit
    with charachange
    #lilly giggle

    li "Oh, I hardly risked my life. It's a fairly common procedure…"

    show hanagown smile at tworightsit
    show lilly basic_smile_paj at twoleftsit
    with charachange
    #lilly restore

    ha "I… we're just glad that you're back."

    hi "Anyway, enough with the formalities, I've got this cake here that isn't being eaten…"
    
    show lilly basic_satisfied_paj at twoleftsit
    with charachange

    li "Oh, splendid! I've had nothing but hospital food for the past week, some cake would go down a treat!"

    show lilly basic_smile_paj at twoleftsit
    show hanagown normal at tworightsit
    with charachange
    
    "The cake is gone almost as quickly as I can cut it."

    "I guess girls really can't help themselves when it comes to sweets…"

    "…"

    "Then again, I ate my fair share too. I can't complain too much."
    
    show hanagown smile at tworightsit
    with charachange

    ha "That… was really good."
    
    show lilly basic_cheerful_paj at twoleftsit
    with charachange

    li "Indeed it was. Where did you say you bought it, Hisao?"

    hi "Eh? Just down at Auramart. They have this display up the back…"

    show hanagown distant at tworightsit
    show lilly basic_pout_paj at twoleftsit
    with charachange
    #both girls, looking displeased.

    li "Come now, Hisao. You could at least lie to us about this kind of thing."

    ha "Who buys cakes from convenience stores?"

    hi "Eh? What's wrong with that?"
    
    show lilly basic_listen_paj at twoleftsit
    with charachange

    li "It would seem that you don't quite understand the finer points of life, Hisao."

    hi "I have no idea what you're talking about."
    
    show hanagown irritated_alt at tworightsit
    with charachange

    ha "Cakes should come from a bakery."
    
    show lilly basic_cheerfulblush_paj at twoleftsit
    with charachange

    li "Not a convenience store."
    
    show hanagown normal_alt at tworightsit
    with charachange

    ha "It's the rules."

    hi "O…kay. I'll try to remember that next time."

    hi "But it wasn't bad, was it?"
    
    show lilly basic_pout_paj at twoleftsit
    with charachange

    li "Well, now that you mention it, it was a little dry…"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "And I think it could have been sweeter…"

    hi "Alright, alright, I get it! I won't do it again, I'm sorry!"
    
    show hanagown smile at tworightsit
    show lilly basic_planned_paj at twoleftsit
    with charachange
    #both girls, happy

    li "Well, I'm glad that you have learnt your lesson."

    li "One mustn't underestimate the importance of such matters."

    hi "I understand."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Well then, would one of you care to fill me in on the events of the past week?"
    
    show lilly basic_oops_paj at twoleftsit
    with charachange

    li "I feel like everyone has left me behind and gone ahead without me."
    
    show hanagown normal at tworightsit
    with charachange

    hi "Nothing's really happened."

    ha "Everyone's been worried about you though."

    hi "Oh, and exams. They're pretty much next week."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Well, I suppose that not much happens over the course of a week."
    
    "The conversation comes to an unexpected dead end."
    
    show hanagown distant at tworightsit
    with charachange

    "Lilly continues to drink just as daintily as she always has; a picture of the upper class."

    "Hanako, however, holds her cup in two hands, tilting it gently to her lips."

    "She reminds me of a hamster nibbling on a corn kernel."
    
    play sound sfx_teacup

    "Out of habit, I start cleaning up the leftovers of the cake."
    
    hi "So, Lilly, did you and your sister talk about much?"
    
    show lilly basic_surprised_paj at twoleftsit
    show hanagown normal at tworightsit
    with charachange

    li "Oh, so you met Akira?"

    hi "Yeah, the other day. I guess you don't catch up with her that often."
    
    show lilly basic_sad_paj at twoleftsit
    with charachange
    #lilly sad

    li "That is true. It is a shame, living so far from home."
    
    show lilly basic_reminisce_paj at twoleftsit
    with charachange

    li "But I suppose that we are all in a similar situation."
    
    show hanagown distant at tworightsit
    with charachange
    #Hanako …. quizzical? Whatever is closer.

    ha "…in one way or another…"

    show lilly basic_smile_paj at twoleftsit
    with charachange
    #lilly neutral

    li "However, it was good to say hello and catch up on family affairs."

    hi "So, are you going to visit them over the break?"
    
    show lilly basic_listen_paj at twoleftsit
    with charachange

    li "I shouldn't think so. It is a fairly long way to go."

    hi "Really? How far?"

    li "South Africa."

    "I stop in shock, nearly dropping the crumb-covered plate in my hands."

    hi "South Africa? You mean, like, the one in Africa?"
    
    show lilly basic_ara_paj at twoleftsit
    with charachange

    li "That is around where South Africa is located, yes."
    
    show hanagown irritated_alt at tworightsit
    with charachange

    ha "Didn't you know?"
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Sorry for not telling you earlier, Hisao."

    hi "That's… fine I guess."

    hi "In that case though, what are you going to do over the break?"

    #lilly/Hanako pondering
    show hanagown normal at tworightsit
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "I think that I shall take some time off to my family's summer house in Hokkaido."

    li "It's rather well equipped, yet remote enough to be quite tranquil."

    hi "Sounds nice. What about you, Hanako?"

    show hanagown worry at tworightsit
    with charachange
    #hanako thinking

    ha "I'm not too sure. Maybe I'll go with Lilly."
    
    show lilly basic_cheerful_paj at twoleftsit
    with charachange

    li "That sounds like a wonderful idea. You're also welcome to come along, Hisao."
    
    show hanagown smile at tworightsit
    with charachange

    li "The more the merrier."

    "To be invited to a remote summer home by two girls…"

    "What kind of madman would refuse an offer like that?"

    hi "Sure. I'll speak to my parents and let them know."

    ha "It would be good if you could try."

    hi "I definitely will."

    "A brief flash of reality reminds me of more pressing issues."
    
    show hanagown normal at tworightsit
    with charachange

    hi "But… shouldn't we be thinking about exams before we make too many plans?"
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Due to my operation, I have received a bit of relief from the exams."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "However I don't think that I shall need to make use of that…"

    "Lilly's right. One look around her room is all it takes to notice that she's quite well read."

    hi "Huh. Lucky you. How about you Hanako? How do you think you'll do?"
    
    show hanagown distant at tworightsit
    with charachange

    "There is a strange noise from Hanako as she coughs into her teacup."

    "I guess my question caused her to inhale a little of the hot liquid…"
    
    show hanagown worry_blush at tworightsit
    with charachange
    #hanako embarrasseed
    
    $ renpy.music.set_volume(0.00000000000000004, 4.0, channel='music')

    ha "I… I haven't really thought about it."
    
    show hanagown distant_blush at tworightsit
    with charachange
    
    $ renpy.music.set_volume(0.00000000000000004, 1.0, channel='music')

    ha "But I think I may need to study some…{w=.3}{nw}"
    
    show hanagown worry_alt at tworightsit
    show lilly basic_concerned_paj at twoleftsit
    with vpunch
    play sound sfx_impact

    li "Egerhk!"

    #lilly shocked

    "Hanako is cut off by Lilly's strange utterance."

    "By the time I look at her, she has put down her teacup and is grasping at her throat."

    hi "Lilly? What's the matter?!"
    
    show lilly basic_displeased_paj at twoleftsit
    with charachange

    "Lilly takes a moment to compose herself, slowly removing her hand from her throat."

    show lilly basic_surprised_paj at twoleftsit
    show hanagown distant at tworightsit
    with charachange
    #lilly calm again
    
    li "Oh, I'm sorry Hisao. It would appear that my throat is still a little raw."

    li "I swallowed a little too much tea, and that seems to have aggravated it."

    hi "Do you want me to call the nurse or something?"
    
    show lilly basic_sad_paj at twoleftsit
    with charachange
    
    $ renpy.music.set_volume(0.80000000000000004, 6.0, channel='music')

    li "No, I'm fine now. I just think I should take it easy."
    
    show hanagown normal at tworightsit
    with charachange

    ha "Are you sure?"

    li "I'm positive."

    #only fools are positive.

    #are you sure?

    #I'm positive.

    hi "Still, you should get some rest. How about we call it a night?"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "It's probably a good idea, Lilly."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange
    #lilly Happy

    li "You're right. Staying up late isn't exactly going to help me."
    
    show hanagown normal_blush at tworight
    with charamove

    "Hanako stands up, and we start clearing the small table."
    
    show lilly basic_weaksmile_paj at twoleft
    with charamove
    
    show bg school_dormlilly at bgright
    show lilly basic_weaksmile_paj at left
    show hanagown normal_blush at right
    with charamove

    "Lilly rights herself, and starts running her fingers along her bookshelf, gently feeling the bumpy spines."

    "She stops on one, and removes it from the shelf."
    
    show hanagown normal_blush at tworight
    with charamove

    "Hanako stacks the crockery in its rightful position then heads for the door."

    ha "'Night Lilly."

    hi "Good night, Lilly. Get yourself some rest."

    show lilly basic_smile_paj at left
    with charachange
    #lilly big smile
    
    stop music fadeout 6.0

    li "I will. Thank you both again."
    
    hide hanagown
    with charaexit
    
    play sound sfx_dooropen

    "Hanako walks out into the hall, and I follow, closing the door behind me."
    
    scene bg school_girlsdormhall
    with locationchange
    
    show hanagown distant
    with charaenter
    #bg dormhall
    #hanako looking down.
    
    play sound sfx_doorclose

    "Lilly's door closes with a click, and I am left facing Hanako, who is avoiding my gaze."

    ha "Um… Hisao…?"

    hi "What's up?"

    "Hanako nervously toys with her hair, twirling a few strands around her fingers."
    
    show hanagown distant_blush
    with charachange
       
    ha "Um… I just wanna say t…thank you."

    ha "For not telling Lilly about last night."

    hi "That's okay. If anything, I'm just as guilty as you."
    
    show hanagown distant_alt
    with charachange
    
    with Pause(0.2)
    
    show hanagown distant_blush
    with charachange

    "Hanako shakes her head, still fiddling with her hair."

    ha "No… no, it was my fault."

    ha "So I… I wanna thank you properly."
    
    show hanagown normal_blush
    with charachange
    #Hanako Defiant

    "Hanako lets her hair go, and locks her gaze on mine."

    ha "C… close your eyes."

    hi "Huh?"

    ha "J…. just do it. Please."

    "Reluctantly, I close my eyes."
    
    scene black 
    with shuteye

    #BG blackout with eyes closed.

    "I hear Hanako take a deep breath, and take a step towards me."

    #it would be nice if there were an effect here, but I can live without it.
    
    $ renpy.music.set_volume(1.0, 0.0, channel='music')
    play music music_twinkle fadein 0.1

    "I feel something warm against my face as Hanako pecks me on the cheek."

    hi "Huh?"
    
    scene bg school_girlsdormhall
    show hanagown normal_blush
    with openeye

    #BG Dormhall with eyes open.
    #Hanako Embarrassed.

    ha "I… Li… I thought I should be more… more…"
    
    show hanagown smile
    with charachange

    ha "So I… thank you."

    "I'm glad that Hanako is filling in the silence, because I doubt I would be able to make any more sense."

    "Just where the hell did this come from?"
    
    show hanagown normal_blush
    with charachange

    ha "I thought… I should stop relying on you two."

    hi "Relying on us?"

    hi "Isn't that what friends do?"
    
    show hanagown distant_blush
    with charachange

    ha "Yes, but…"
        
    #"For some reason, I feel compelled to pat Hanako on the head."
    #I'm sorry, but I had to comment this out. Holy hell does crud like to make Hisao pat Hanako's head... -Alphabro

    hi "Don't sweat it."

    hi "Lilly's a bit under the weather now, but I'm sure everything will be back to normal soon enough."

    ha "Okay…"

    hi "You should probably get some rest too."
    
    show hanagown normal_blush
    with charachange

    ha "Okay…"
    
    show bg school_girlsdormhall at bgleft
    show hanagown normal_blush at tworight
    with charamove

    "Hanako turns and heads for her room."

    hi "Oh, and Hanako?"

    "Hanako freezes, her hand on her door's handle."

    hi "…thanks for that."
    
    show hanagown smile at tworight
    with charachange
    #Hanako embarrassed smile

    "Unexpectedly, Hanako tilts her head, and smiles at me."
    
    stop music fadeout 6.0

    ha "You're welcome!"
    
    play sound sfx_dooropen
    
    show hanagown smile at offscreenright
    with charamove
    
    "Before I can react, she rushes into her room and closes the door behind her."
    
    hide hanagown
    with None
    #hide Hanako with move right

    "I am alone in the hallway, my cheek still tingling from Hanako's kiss."

    "Anyone who can understand her would have to be some kind of genius."

    "Walking like a zombie, mulling over the enigma that is Hanako, I return to my room."
    
    scene bg school_dormhallway
    with shorttimeskip
    #bg dormdoor

    "I stop at Kenji's door, considering asking him what he'd think about the situation…"

    #it would be good to get the following in some kind of flash-back or something…

    ke "It's a conspiracy!"

    "Yeah. Perhaps he isn't the best person to speak to about this kind of thing."

    "I get the feeling he'll somehow sour my mood."

    "This is a rare opportunity to escape a tea party at a reasonable hour, and our talk of exams has got me jittering."

    "Time to hit the books, I think…"
    
    scene black
    with dissolve

    return

label en_HT6:

    #Yet another song name for the title.
    #Transition from the last scene with eyes closed/eyes open
    #perhaps we could have a shot of books on a desk for this commonly recurring theme?
    #also, damn, 11 days between scenes. Freaking work
       
    scene black 
    with dissolve
          
    scene bg school_dormhisao
    with openeye
    #bg dormroom with eyes open.
    
    $ renpy.music.set_volume(0.80000000000000004, 6.0, channel='music')
    
    play music music_daily fadein 10.0

    "Huh. Awake before my alarm."

    "How rare."

    "Still, five minutes is nothing to get excited about, and there's no point in going back to sleep."

    "A splash of water to the face and a quick change into my uniform and I'm ready to go…"

    "… a good half-hour before I usually am."

    "I think I shall use this rare opportunity to get a relaxed breakfast."
    
    scene bg school_cafeteria
    with shorttimeskip
    #bg cafeteria with dissolve

    "As expected, even the smallest time difference has a large effect on the population of the cafeteria."

    "The place is almost abandoned, meaning that I can secure myself a fairly large breakfast."

    "Well, almost abandoned."
    
    show bg school_cafeteria at bgright
    with charamove

    hi "Hey there, Lilly."

    show lilly basic_surprised
    with charaenter
    #show Lilly generic

    li "Is that Hisao?"

    hi "Yeah, it's me."
    
    show lilly basic_cheerful
    with charachange

    li "Good morning. Odd to see you so early."

    hi "Yeah I somehow managed to get up a bit earlier than usual. How's your throat?"

    show lilly basic_smile
    with charachange
    #show Lilly smiling

    li "It feels much better after a night of rest."

    hi "That's good to hear. I'd hate to see you out of action for much longer."

    hi "It'd get depressing…"

    show lilly basic_ara
    with charachange
    #show lilly laugh

    li "Now Hisao, you're making it sound like I had some terrible disease. Hanako doesn't seem immune from the habit, either."

    "The mention of Hanako reminds me of our strange encounter in the dorm last night."

    hi "Say, Lilly… Have you spoken to Hanako recently?"
    
    show lilly basic_weaksmile
    with charachange

    li "Indeed I have. Could you be a little more specific?"

    hi "Um, well, have you noticed anything odd about her? Like any changes?"

    show lilly basic_oops
    with charachange
    #show lilly concerned

    li "Nothing comes to mind. Tell me, did something happen?"

    hi "Well, yes… no…"
    
    show lilly basic_planned
    with charachange
    
    li "Maybe?"

    hi "Eh?"
    
    show lilly basic_weaksmile
    with charachange

    li "Sorry, I was just completing the pattern for you."

    hi "Oh, right."
    
    show lilly basic_smile
    with charachange

    "Damn it, now I've lost my train of thought. I guess I just better spit it out then."

    hi "Anyway, last night Hanako, she, er…"

    hi "She kissed me."
    
    show lilly basic_ara
    with charachange
    #show Lilly happy

    #"Kareha" "ままま!" <- This is the kind of face I was thinking of.

    li "My my, what a development!"

    li "Please, tell me all about it!"

    "Lilly seems far too happy about this. It's almost like she's watching a drama."

    "How very un-Lilly like."

    "Even so, I can't stop the blood rushing to my face. Thankfully no-one else is here yet to see this."

    hi "It was nothing, really."

    hi "Just a peck on the cheek."

    hi "But it was just so sudden… which is why I thought you might have said something to her… or something…"

    "Even if she can't see my face, my pathetic speech has probably given away my embarrassment anyway."
    
    show lilly basic_cheerful
    with charachange

    li "Well, that certainly is unexpected."
    
    show lilly basic_smile
    with charachange

    li "It seems that, perhaps, my stay in hospital lent Hanako a measure of initiative."

    "I guess… that's possible…"

    "Damn, I do not understand women at all."

    #Could not resist.

    hi "Well, moving on. Have you seen Hanako this morning?"
    
    show lilly basic_weaksmile
    with charachange

    li "No, I haven't. I left before she woke up, I believe."

    hi "Huh. I guess I'll see her around then."
    
    show lilly basic_smile
    with charachange

    li "I don't think she'll have any excuse to not be in class."

    hi "True. Anyway, this is getting cold. If you'll excuse me, I think I'll eat."
    
    li "Please, be my guest."
    
    $ renpy.music.set_volume(0.39999999999999999, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 2.0
    
    hide lilly
    with charaexit
    
    show bg school_cafeteria at center
    with charamove

    "Too late. My conversation with Lilly was just long enough for all the heat to escape from what looked to be a fantastic breakfast."
    
    "And, on top of that, the cafeteria has been slowly filling up, and by now all the good breakfast is probably gone."

    "Something about this feels like a bad omen."

    "I unenthusiastically shovel the cold food into my mouth whilst Lilly simply sits across the table, content to let me eat undisturbed."

    "In an effort to offset the discomfort of the cold food, I shovel it down in large gulps."

    "It doesn't help."

    extend " Quite the opposite, actually."
    
    show lilly basic_cheerful at centersit
    with charaenter

    li "You must have been famished, eating like that."

    hi "Nah, I just wanted it over and done with."

    hi "Are you headed to class now? Do you want a hand?"
    
    show lilly basic_ara at centersit
    with charachange

    li "My my, that's quite gentlemanly of you, Hisao. What kind of woman would I be to refuse?"

    hi "Er, I don't know?"
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "The answer is “an uncourteous one.”"

    hi "Right."
    
    hide lilly
    with charaexit
    
    show bg school_cafeteria at bgleft
    with charamove
    
    stop music fadeout 6.0

    "Ruminating on my lack of answer to such an obvious question, I collect Lilly's plates and return them to the scullery window."

    #Yeah, I get it, none of you will know what a scullery is, either. Gimme a replacement, please.
    
    show bg school_cafeteria at center
    with charamove
    
    show lilly cane_smile
    with charaenter
    
    "By the time I return to the table, she's collected her bag and cane and stands ready for the brief walk to the Main Building."

    #bg school hallway
    
    stop ambient fadeout 1.0
    
    scene bg school_hallway3
    show lilly cane_smile
    with locationskip

    li "Well then, here is where we part, Hisao."
    
    show lilly cane_weaksmile
    with charachange

    li "Don't concern yourself too much with Hanako. Thanks to you, she's become much stronger."

    "Thanking Lilly's inability to see my mild blushing, I quickly move to end the conversation."

    hi "Sure thing. I'll see you after class."
    
    play sound sfx_dooropen
    
    hide lilly
    with charaexit

    "Lilly disappears into her classroom, and I walk the short distance to my own class."

    scene bg school_scienceroom at bgleft
    with locationchange
    #bg classroom
    
    $ renpy.music.set_volume(1.0, 0.1, channel='music')
    
    play music music_normal fadein 8.0

    "Inside, only the studious students have arrived, making use of the peace of the room to bury their noses in their textbooks."

    "Not even Shizune or Misha have arrived yet. What a rare occurrence."

    "But there is one person here that surprises me."
    
    show bg school_scienceroom at center
    with charamove
    
    show hanako emb_downtimid at twoleft
    with charaenter
    #show Hanako distracted/neutral

    hi "Hey there, Hanako. How are you this morning?"
    
    show hanako defarms_shock at twoleft
    with vpunch
    #show Hanako embarrassed

    ha "Ah… Hisao… G—good morning."

    "Hanako practically jumps at the sound of my voice, slightly more embarrassed than usual."

    hi "Is everything alright?"
    
    show hanako emb_blushtimid at twoleft
    with charachange
    #Show Hanako panicked

    ha "Whe? Yeah… yeah I'm all good. How's… you… things with?"

    hi "I'm… fine. Are you sure you're good?"
    
    show hanako emb_downtimid at twoleft
    with charachange

    "Hanako is panicking like a rabbit caught in a cage; desperately looking around for something to distract me."

    show bg school_scienceroom at bgright
    show hanako emb_downtimid at center
    with charamove

    show hanako emb_downtimid_close
    with charachange
    
    "I lean down close to her, whispering into her ear conspiratorially."

    hi "Hey, look, if this is about last night, don't worry about it."

    hi "I… kinda enjoyed it."
    
    show hanako defarms_blush_close
    with charachange
    #hanako Mega panic.

    "Hanako's frenzied head movements stop, her face going a full shade redder."
    
    show misha perky_smile behind hanako
    with charaenter
    
    stop music fadeout 3.0

    "Only now do I notice that on the other side of Hanako, leaning in as close as I am, is another face."

    #show Misha neutral/serious

    mi "I guess she enjoyed it too, hey?"
    
    play sound sfx_impact
    
    show bg school_scienceroom at bgleft
    show misha cross_laugh at twoleft
    show hanako defarms_worry at tworight
    with vpunch
    
    play music music_running fadein 2.0

    "I jump back suddenly, nearly tripping over the desk behind me."

    hi "M—M—Misha! When did you get here?"
    
    show misha sign_smile at twoleft
    with charachange
    
    "Misha stands up, leaving Hanako frozen in a state of shock."

    mi "I was here to hear the good part, and that's all that matters, right?"

    show misha hips_grin at twoleft
    with charachange
    #misha lol

    mi "Oh, Hisao and Hanako~"

    mi "Doing naughty things at night~"

    mi "I can't wait to tell Shizune~"
    
    show hanako emb_blushtimid at tworight
    with charachange

    hi "No wait! You can't do…"

    "Too late."
    
    play sound sfx_impact2
    
    with Pause(0.5)
    
    play sound sfx_footsteps_hard

    "Behind me I can hear the sound of a bag being placed rather forcibly onto a desk, followed by angry footsteps."
    
    show misha hips_grin at left
    show hanako emb_blushtimid at right
    with charamove
    
    show shizu cross_angry
    with charaenter
    #show Shizune, angry.

    shi "…"
    
    show misha sign_smile at left
    with charachange
    
    show shizu basic_angry
    with charachange
    
    show misha perky_smile at left
    with charachange
    #shizune and Misha signing

    mi "Shizune wants you to know that… um… “fraternisation”… isn't allowed in the public areas of the school."

    mi "She also thinks that it's a bad idea for high school students to be wasting time on personal matters when exams are so close."

    show misha hips_smile at left
    with charachange
    
    mi "Also, she thinks that if you want to pass notes, you should use a more direct delivery system…"
    
    show hanako emb_downtimid at right
    with charachange

    hi "Wait, what the hell are you talking about?"

    hi "You've got it all wrong, nothing's going on between us…"

    hi "Wait, notes?"
    
    show misha sign_smile at left
    with charachange
    show shizu behind_frown
    with charachange
    show misha perky_smile at left
    with charachange

    "Misha quickly signs something to Shizune, who then produces a small note."

    "On the front, in writing so faint it's almost illegible, is written “To Hisao.”"

    mi "You left this lying on your desk where anyone can see it."
    
    show misha cross_frown at left
    show shizu adjust_frown
    with charachange

    mi "I don't care what you do in your own time, but keep it out of the classroom."

    mi "Understood?"

    "At times, I wonder if Shizune sees Misha as a friend, or if she simply possesses her just to use her mouth."
    
    show hanako emb_blushing at right
    with charachange

    "I snatch the note out of Shuzune's hand, noting that Hanako winces a little as I grab it."

    hi "Fine, understood."

    hi "Man, you two really know how to misinterpret the situation."

    hi "There's nothing “naughty” going on at all."
    
    show misha cross_grin at left
    with charachange
    #misha :p

    mi "Su~re there isn't."
    
    show misha perky_smile at left
    with charachange

    mi "Anyway, it looks like you have something to deal with, so we'll leave you alone for the moment."

    mi "Right, Shizune?"
    
    show shizu basic_angry
    with charachange

    shi "…"
    
    hide shizu
    hide misha
    with charaexit
    
    stop music fadeout 4.0
    
    $ renpy.music.set_volume(0.39999999999999999, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 2.0
    
    show bg school_scienceroom at center
    show hanako emb_blushing at center
    with charamove
    
    "I breathe a little relief as Misha drags Shizune back towards their desks, leaving me with a visibly shaken Hanako."

    "She looks a little too stressed to talk, so I guess I'll read the note first…"

    play sound sfx_impact

    show hanako defarms_shock
    with vpunch
    #Hanako Embarrased/defiant
        
    stop ambient fadeout 1.0

    ha "DONTREADTHAT!"
    
    "The background murmur of the class drops into silence as everyone tries to discreetly eavesdrop on this sudden outburst."

    hi "Er… okay."

    hi "Should I give it back?"

    ha "No!"

    hi "Er… right. So I shouldn't read it then?"
    
    show hanako emb_downtimid
    with charachange
    #Hanako looking down, embarrassed

    ha "N…no. Just… don't read it now."
    
    play sound sfx_normalbell
    
    #Wrong kind of peal. -md01
    #"The school bells peel throughout the classroom, and I am forced to return to my seat…"
    "The school bells peal throughout the classroom, and I am forced to return to my seat…"

    #"…but not before I pat Hanako on the head."
    #Holy hell, crud... It doesn't even make sense here- Alphabro
    
    hide hanako
    with charaexit
    #hide Hanako

    "It's not long before the class is underway, and whilst Shizune and Misha are distracted by taking notes, I unfold the tiny letter."

    $ written_note("Dear Hisao,\n I have something I want to tell you.\nPlease meet me behind the dorms after school.")
    #lawl, be there or i'll {s}kill you{/s} go home? d.

    "Huh, unsigned."

    "Then again, it's not like it's hard to work out where it came from."

    "Making sure the teacher is facing the board, I turn around to face Hanako."
    
    show bg school_scienceroom at bgright
    with charamove
    
    show hanako emb_blushing at twoleft
    with charaenter

    #show Hanako Embarrassed

    "It doesn't take long to get her attention. It's almost as if she's been watching my back all morning…"

    "I hold up the note, point to it, and give her a quick thumbs-up."
    
    show hanako emb_downsmile at twoleft
    with charachange

    #Show Hanako embarrassed looking down, smiling

    "She looks away, pretending not to notice me."
    
    show hanako emb_smile at twoleft
    with charachange
    
    with Pause(0.6)
    
    show hanako emb_downsmile at twoleft
    with charachange

    "But, a moment later, she quickly looks back at me for an instant, returning my thumbs-up, before once again pretending not to look at me."

    "Teacher" "Nakai! Eyes front!"
    
    hide hanako
    with charaexit
    
    show bg school_scienceroom at bgleft
    with charamove

    hi "Sorry…"

    "Teacher" "Sorry won't cut it. I want you to read from the textbook, starting at page 54…"

    "Huh, I guess this is what my cold breakfast was trying to warn me about…"

    return
    
label en_HT7:
    
    scene bg school_scienceroom at bgleft
    with locationchange
    
    scene bg school_scienceroom
    with shorttimeskip

    "My moment as the star of the class passes quickly, much to my relief."

    "Teacher" "That's enough. Now, let me continue…"

    "Word after word issues forth from the teacher's mouth, but I find it hard to follow along."

    "Half-way through the class, I look at my notes, only to find that they are covered with a mess of doodles."

    "Even here, where my mind is taking some kind of form, there is no order, just a random mess of squiggles."
    
    play sound sfx_normalbell

    "Thankfully, the lunch bells relieve me of this affliction."
    
    show bg school_scienceroom at bgleft
    with charamove
    
    show hanako emb_timid at right
    with charaenter
    
    with Pause(0.6)
    
    show hanako emb_timid at offscreenright
    with charamove

    "I turn, ready to talk to Hanako, only to see her disappear through the classroom's rear door."

    "Looks like she's not ready to talk to me yet."

    "On the other hand, this does give me a bit of time to clear my mind."

    "I need to talk to someone, and I can think of only one person up to the task."

    scene bg school_miyagi at bgright
    with locationskip
    #bg school roof- nah, I've been tainted by the Final route. Make this the tearoom
    
    play music music_friendship fadein 4.0
    
    show lilly basic_smile at tworightsit
    with charaenter
    #show Lilly neutral

    hi "Lilly, have you got a moment?"
    
    li "But of course. What's the matter, Hisao?"

    #"Thankfully, Lilly is the only person on the roof today. I don't know what I would do if Rin and Emi were here today."
    "Thankfully, Lilly is the only person in the tearoom today. I don't know what I would do if Hanako was here too."

    hi "Um, it's about Hanako."

    show lilly basic_oops at tworightsit
    with charachange
    #show lilly concerned.

    li "Oh, has something gone wrong?"

    hi "Er, not exactly."

    hi "She, er, she gave me what looks like… a letter."

    li "A letter? What type of letter?"

    "I fidget nervously."

    "It's fairly obvious what Hanako intends to talk to me about, but even so, the anticipation inside me is palpable."

    hi "It, well, she's asking me to meet her after school."

    li "In a letter? Why didn't she just ask you to your face?"

    hi "That's… what I was hoping to ask you."

    hi "You know how this morning I was asking you about Hanako?"
    
    show lilly basic_weaksmile at tworightsit
    with charachange

    li "Of course."

    hi "Well, I think that maybe… I dunno."
    
    li "That perhaps she likes you?"

    "Emotions run through me like a lightning bolt."

    "It's not like this is really news to me, but, still…"

    "Hearing someone say it out loud excites me a little."

    hi "Yeah, something like that."
    
    show bg school_miyagi at bgleft
    show lilly basic_weaksmile at centersit
    with charamove
    
    #show lilly basic_weaksmile
    #with charamove

    "Not knowing what to do, I sit down next to Lilly."
    
    show lilly basic_smile at centersit
    with charachange

    li "Well, is that a problem, really?"

    hi "I… don't know."

    hi "I haven't really thought about it."

    "Itching to be doing something, my hand reached into my pocket and retrieves Hanako's note."

    "After simply holding it for a second, I feel another, different set of emotions."

    hi "You know…"

    extend "This isn't the first time I've received a letter like this…"

    show lilly basic_planned at centersit
    with charachange
    # lilly curious, or something like that.

    li "Oh, really? You must be handsome then, Hisao…"

    hi "That's not exactly what I meant."
    
    $ renpy.music.set_volume(0.00000000000000001, 4.0, channel='music')
    
    "Panic grips tentatively at the edges of my mind, and before I know it…"

    hi "It was at my last school…"

    "…I'm telling Lilly about the last time I got such a letter."

    hi "I got a letter like this, with just a place and a time, and it turns out it was a girl that I liked."
    
    show lilly basic_listen at centersit
    with charachange

    hi "But that was when I had my heart attack."

    hi "The doctors heard about that and blamed it on the stress…"

    li "I see."

    li "It would be troublesome if such a thing happened again."

    li "However, this time you at least know who the letter is from, correct?"

    hi "Well, unless I'm grossly mistaken, then yes."
        
    show lilly basic_weaksmile at centersit
    with charachange

    li "So that should at least relieve you of some of the surprise, correct?"

    hi "I suppose."
    
    show lilly basic_smile at centersit
    with charachange
    
    $ renpy.music.set_volume(1.0, 4.0, channel='music')

    li "The other part, however, may require some extra work."

    hi "Other part?"
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "Well, do you actually like Hanako?"

    "Lilly poses this question just as easily as she would ask me the time."

    "I just wish I could answer as easily."

    hi "Um… well… I like her, but I like you too, I guess…"

    show lilly basic_displeased at centersit
    with charachange
    #lilly sad/frustrated/thinking/something like that.

    "Lilly sighs slightly."

    li "Let's try this a different way."
    
    show lilly basic_oops at centersit
    with charachange

    li "What do you plan to do when you leave school?"

    hi "Eh? Go to university, I guess?"

    hi "But what does that have to do with anything?"
    
    show lilly basic_listen at centersit
    with charachange

    "Lilly ignores my question and continues with her interrogation."

    li "What do you intend on studying?"

    hi "Science, I guess."

    hi "But…"

    li "And why is that?"

    "Lilly just ploughs along; I guess I'll just have to run with it for now."

    hi "Not really sure. It's just something that I enjoy, I guess."
        
    show lilly basic_smile at centersit
    with charachange

    li "Well, there you have it."

    hi "Eh? What?"
    
    show lilly basic_planned at centersit
    with charachange
    #lilly whimsical, or something.

    li "You are planning the rest of your life based on a whim."

    li "So what is the sense in putting so much thought into something as trivial as a high-school romance?"

    "I try to find a way to refute Lilly, but end up totally lost for words."

    "What she's saying makes perfect sense, even if it seems overly clinical."
    
    show lilly basic_weaksmile at centersit
    with charachange

    li "I take it that this seems a little, well, direct for you, yes?"

    hi "I… guess."

    li "Well, just answer me one question;"

    extend " Would you have any objections to Hanako?"

    hi "No… I really like her."

    hi "Why would I have any objections?"
    
    show lilly basic_smile at centersit
    with charachange

    li "Then I think you have just answered your own doubts."

    show lilly basic_ara at centersit
    with charachange
    #lilly coquettish or something like that

    li "Unless, of course, you have someone else in mind?"

    hi "Eh? No, not really."
    
    show lilly basic_smile at centersit
    with charachange

    li "Then I recommend that you accept Hanako's offer."

    li "I think that it would help both of you."

    li "It should help you get over the anguish of your heart attack, and it also shows that Hanako is almost out of her shell."

    hi "But… I'm still not sure…"

    show lilly basic_weaksmile at centersit
    with charachange
    #lilly small smile

    "Lilly turns to me, and, after a bit of fumbling, rests her hand on my shoulder."

    li "Do you need to be sure?"
    
    li "I would think that it would be slightly exhilarating; throwing yourself headlong into a relationship at this age."

    #lawl nympho Lilly appears

    li "And, if things don't work out, then you can always just go back to being friends."

    li "I'll always support both of you."

    hi "Thanks, Lilly."

    show lilly basic_smile at centersit
    with charachange
    #Lilly Smiles

    li "You're welcome, Hisao."

    li "However, if I am correct, we are almost out of time."

    #li "We should leave here before the bells start. It's awfully loud from here…"
    li "We should leave here before the bells start. It'd be best to avoid the crowd…"

    hi "Agreed. Here, I'll help you up…"
    
    #show lilly basic_smile at centersit
    #with charamove
    
    show bg school_miyagi at bgright
    show lilly basic_smile at tworightsit
    with charamove
    
    show lilly basic_smile at tworight
    with charamove

    "I quickly jump to my feet and gently grasp Lilly's hand, helping her to her feet."
    
    play sound sfx_doorclose
        
    scene bg school_hallway3
    show lilly basic_smile
    with locationchange
    
    stop music fadeout 4.0
   
    with Pause(0.4)
    
    play sound sfx_normalbell
    
    
    #"It seems that Lilly's sense of time is correct; as soon as I close the door to the stairwell, the bells clamour into life."
    "It seems that Lilly's sense of time is correct; as soon as I close the door to the tearoom, the bells clamour into life."

    #BG hallway

    "For the second time today, Lilly and I part ways in the hallway."
    
    show lilly back_giggle
    with charachange

    "Lilly gives me a short wave before leaving, and, without thinking, I wave back."
    
    hide lilly
    with charaexit
    

    "Chiding myself for doing something so stupid, I simply call out after her."

    hi "See you, Lilly. And thanks again."

    #bg classroom
    scene bg school_scienceroom
    with locationchange
    
    play ambient sfx_paperruffling

    "The classroom is in a typical state of disarray as I walk in; all of the students are trying to jam in as much as they can into the brief interval before class."

    "It's like they were slacking off during the break and are trying to make up for lost time before the teacher appears."

    stop ambient fadeout 0.5

    "I guess it doesn't matter if it's conversations or assignments; students are bound to leave everything until the last possible moment."
    
    #Eh, placeholder for some extra "deep" should I want to put it in later.
    #something about how this reflects on Hisao x Hanako and what Lilly said.

    "One character in this never-ending drama, however, is missing."
    
    "The rearmost window seat is currently lacking one Hanako."

    "I guess she's avoiding me out of embarrassment… or something."
    
    show bg school_scienceroom at bgleft
    with charamove

    "I keep my eyes on the doors, awaiting her return."
    
    play sound sfx_dooropen
    
    show hanako emb_timid at offscreenright
    with None
    
    show hanako emb_timid at right
    with charamove
    
    #with Pause(0.4)
    
    show hanako emb_timid at rightsit
    with charamove
    
    hide hanako
    with charaexit

    "Just as the teacher slides open the front door to the class, Hanako bolts to her chair from the rear door."

    "She was probably waiting in the hallway until the last possible moment."
    
    show bg school_scienceroom at center
    with charamove

    "Not wanting to suffer the same fate as I did this morning, I keep my eyes glued firmly to the front of the class, taking notes where appropriate."

    "Lilly's pep-talk has made me surprisingly focused, not only on my impending meeting with Hanako, but also with the class."
    
    
    show bg school_scienceroom_ss
    with shorttimeskip
    
    play sound sfx_normalbell

    "As a result, I am genuinely surprised when the bells sound for the end of the class."
    
    show bg school_scienceroom_ss at bgleft
    with charamove
       
    show hanako emb_timid_ss at right
    with charaenter
    
    #with Pause(0.4)
    
    show hanako emb_timid_ss at offscreenright
    with ease

    "With speed rivalling a gazelle, Hanako is out of the back door before I can even turn around."

    "Nervous energy, I suppose."

    "Well, here goes nothing, I guess."

    #BG Hanako's wall from Act 1. I know we're not using that scene anymore, but I like that shot.
    
    scene bg school_dormext_full_ss at bgleft
    with locationskip
    
    $ renpy.music.set_volume(0.1, 0.0, channel='ambient')
    play ambient sfx_crowd_outdoors

    "The area behind the dorms is shady and peaceful."

    "Behind me I can hear the muffled sounds of students going about their daily lives."

    "Cheers from various sporting clubs, the sounds of cooking and washing from the dorms…"
    
    stop ambient fadeout 3.0

    "But everything seems somewhat… distant."

    "It's like some kind of barrier is preventing the outside world seeping into this forgotten plot of land between the dorm buildings and the school's wall."

    "Of course, there is another person here, and it only takes a moment's walk before I reach the hunched figure leaning against the stone wall."
    
    show bg school_dormext_full_ss at bgright
    with charamove
    
    show hanako emb_blushing_ss
    with charaenter
    #Show Hanako embarrassed
    
    hi "So, I guess it really was your note?"

    ha "Um, er… yes. I guess you know that, right?"

    hi "I had a hunch…"
    
    "A bird's song drifts over the school's wall, giving Hanako a chance to pause before answering."
    
    show hanako emb_downtimid_ss
    with charachange

    ha "Um, H—Hisao…?"

    hi "Yes?"
    
    show hanako emb_blushtimid_ss
    with charachange
    #Hanako Embarrased, looking down. Or perhaps a super embarrassed.

    ha "W…what do you think about me?"

    "I guess it's not that easy to be direct, but even for Hanako, this seems a little round about."

    hi "Well, I like you. You're a good friend."
    
    show hanako emb_blushing_ss
    with charachange

    ha "Is… is that all?"

    "I have a feeling that this is not going all that well."

    hi "What do you think about me, Hanako?"
    
    show hanako basic_worry_ss
    with charachange
    #Hanako embarrassed, surprised

    ha "M—me?"

    ha "Do think about you…"
    
    show hanako emb_blushtimid_ss
    with charachange

    ha "Um, er…"

    hi "Take your time… we've got all day."
    
    show hanako emb_downtimid_ss
    with charachange

    "Hanako takes a deep breath."
    
    show hanako emb_blushtimid_ss
    with charachange

    ha "I like you too, Hisao."

    hi "That's good to know."

    hi "So, what did you want to talk to me about?"

    "Hanako looks around, presumably to make sure no-one is watching."
    
    show hanako basic_worry_ss
    with charachange

    ha "You… you know how I told you that I had a friend before?"

    "I strain my memory for a second, but then remember Hanako's words when we slept in Lilly's room."

    hi "Oh, your friend from before?"

    "Hanako simply nods in response."

    #It is quite possible that this bit will change a little, depending on if I keep the whole
    #"dead boyfriend" thing. I dunno.
    
    show hanako emb_blushtimid_ss
    with charachange
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    
    play music music_innocence fadein 3.0

    ha "He… he said I was a good friend too…"

    extend " when I asked him like this."
    
    show hanako emb_downtimid_ss
    with charachange

    ha "But then… I ran away."

    ha "I ran away and he chased me."

    #Hanako crying
    
    show hanako emb_downtimid_cry_ss
    with charachange

    ha "And… and then…"
    
    show bg school_dormext_full_ss at center
    show hanako emb_downtimid_cry_ss at twocenteroff3
    with charamove

    "Hanako, unable to continue, starts to stagger away from the wall."
    
    show bg school_dormext_full_ss at bgleft
    show hanako emb_downtimid_cry_ss at center
    with ease
    
    show hanako emb_downtimid_cry_close_ss
    with charachange
    
    "Instinctively I rush forward and catch her, holding her close to my chest."

    ha "Promise me… promise me you won't die too…"

    hi "I… promise you."
    
    show hanako emb_sad_cry_close_ss
    with charachange

    "Hanako takes great heaving sobs into my chest, before looking up at me with her reddened face."

    ha "Hisao…"
    
    show hanako emb_timid_cry_close_ss
    with charachange

    ha "I love you."

    "Lilly's advice rushes through my brain at a million miles an hour, as does all the time I've spent with Hanako up to this moment."
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    show ev hanako_kiss_scroll:
        xalign 0.5 yalign 0.5 ypos 0.0
        linear 6.0 ypos 0.65
    with dissolve

    "But, before I can make a rational decision, I find my head bending down, and my grip on Hanako's slight frame tightening."
    
#    play sound sfx_whiteout
#    
#    scene white 
#    with dissolve
#    
#    show ev hanako_kiss_easein
#    with dissolve

    "The salt from her tears mixes with the latent taste of lip-balm as we kiss."
    
    "I feel a pressure on my back, and realize that Hanako has wrapped her arms around me, pulling me into this ever-deepening embrace."
    
    with Pause (0.5)
    
    scene white 
    with dissolve
    
    scene bg school_dormext_full_ss at bgright
    show hanako basic_bashful_close_ss
    with dissolve
           
    "After what feels like an eternity, we separate our lips, looking directly into each other's eyes."

    hi "How's that for an answer?"

    show hanako emb_smile_close_ss
    with charachange
    #Hanako happy embarrassed

    ha "I… I think it's a pretty good one."
    
    hi "Say, what are you doing tomorrow after morning classes?"
    
    #show hanako emb_timid_close_ss
    #with charachange

    ha "N—not much."

    hi "Wanna go somewhere together?"
    
    show hanako basic_bashful_close_ss
    with charachange
    #Hanako smile

    ha "Yes… and I think I know a place that would be good."

    hi "Really? Where?"
    
    show hanako cover_bashful_close_ss
    with charachange

    ha "It's… a secret place of mine."
    
    ha "I can take you there."

    hi "Sounds good. Should I bring anything with me?"
    
    show hanako basic_normal_close_ss
    with charachange

    "Hanako looks up for a moment, as if accessing some seldom-used part of her brain."

    ha "Maybe, some food?"

    hi "Consider it done."

    hi "But… what should we do now?"

    show hanako emb_smile_close_ss
    with charachange
    #Hanako defiant smile

    ha "Um, I have an idea…"

    "Once again, Hanako's grip on me tightens, pulling me towards her beckoning lips."
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
#    show ev hanako_kiss2
#    with dissolve

    show ev hanako_kiss_outside
    with dissolve

    "Considering that a little over three hours ago I was having doubts about this very situation, I put up very little resistance to yet another kiss…"

    return

label en_HT8:
    
    scene bg school_dormext_full_ss
    show hanako emb_smile_close_ss
    with dissolve

    "Breathless, Hanako and I tear ourselves apart."

    hi "Um… wow."
    
    show hanako emb_downsmile_close_ss
    with charachange
    #Hanako Look down smile

    ha "Yeah… wow."

    hi "So, uh, I guess I'll see you tomorrow then."

    ha "Yeah… at.. class…"

    hi "Yeah, class, right."

    "For a moment, neither of us really knows what to say, and just stand there, avoiding each other gaze lest we become overcome again."
    
    show hanako emb_smile_close_ss
    with charachange

    ha "I'd… better get going."

    hi "Yeah, me too. If we're going out tomorrow then I guess I should study some more tonight."
    
    show hanako defarms_shock_close_ss
    with charachange
    #hanako shocked

    ha "Oh, right, study!"
    
    show hanako defarms_worry_close_ss
    with charachange

    ha "I should do that… too."
    
    show hanako def_smile_close_ss
    with charachange
    #hanako slight smile

    ha "G'night, Hisao."
    
    stop music fadeout 6.0

    hi "Night, Hanako."
    
    hide hanako
    with charaexit

    "Awkwardly, we part ways, disappearing to opposite sides of the dorm that just served to hide us from the world."

    #bg dormhall
    scene bg school_dormhallway
    with locationskip
    
    "As I pass Kenji's door, I am suddenly overwhelmed with the urge to talk to someone about my newfound relationship."

    "Even if that means risking a lecture on the fascist nature of the fairer sex."

    "For a moment, I consider knocking lightly."

    #bg dorm door
    show bg school_dormhallway at bgright
    with charamove
    
    play sound sfx_doorknock

    "But then I remember that this is Kenji we're talking about, and pound the hell out of his door."

    "No response."

    "Probably watching something unsavoury with his headphones again."
    
    play sound sfx_doorknock

    "I beat on the door again, and keep doing so until my hand starts to hurt."

    "Ah well, I guess I can keep this to myself for the moment."

    "Time to get to study then, I guess…"

    #BG dormroom
    scene bg school_dormhisao_ss
    with locationchange
    
    play music music_comfort fadein 3.0

    "Not surprisingly, I find my focus drifting a little."

    "I open my textbook, click a lead into my clutch pencil, and rest it against my lips whilst I read…"

    "My lips…"

    "Damn. I managed a whole fifteen seconds without reminding myself of what just happened."

    "But I need to focus. I'm going to waste all of tomorrow afternoon with Hanako, meaning that I'll only have the evening to study."

    "Exams are important… Aren't they?"

    "Once again my mind drifts back to my conversation with Lilly at lunch."

    "Just what is it that I plan to do with my life?"

    "What if all this time I've spent studying just turns out to be a waste of time?"

    "If I'm not chasing any particular goal, then what is the point in wearing myself out?"

    "…"

    "Well, that just passed a good ten minutes, back to the books."

    "I don't want to be fretting over a lack of study when I'm with Hanako tomorrow."

    "I just wish that I could prevent the opposite occurring…"

    "This isn't working. I need to calm myself down."
    
    stop music fadeout 4.0

    "Maybe I should just lie down for a second…"
    
    scene black
    with shuteye
    
    window hide
    
    with Pause(2.0)
    
    play sound sfx_alarmclock
    
    with Pause(0.6)
    
    window show
    
    scene bg school_dormhisao
    with openeye
    #bg bedroom with eyesopen

    "Well, that didn't work as planned."

    "Looks like the study will have to wait until tonight."

    "I silence my alarm and get ready for a quick shower."

    "I'll have just enough time to grab a quick breakfast before class if I can keep this shower under three minutes…"

    "Go!"

    scene bg school_dormbathroom
    show steam
    show steam2
    with shorttimeskip
    #bg bathroom

    "Looks like I'll be skipping breakfast, then."
    
    hide steam
    with charaexit
    
    "Shouldn't be a problem though. There's only the morning classes today, and with exams looming it might even be some kind of revision class."
    
    hide steam2
    with charaexit
    
    "At least I might be able to make up for the time I lost last night."

    scene bg school_scienceroom at bgleft
    with shorttimeskip

    play music music_normal fadein 0.3
    play ambient sfx_crowd_indoors fadein 0.3
    #bg classroom

    "Every time I enter the classroom of a Saturday morning, I am reminded of a cage at a zoo."

    "In reality, a zoo cage is a good place for an animal to be."

    "It gets food, is cared for, protected from predators, and is put into breeding programs."

    "All in all, major wins all-round."

    "Yet the wild animal side in them means that they will resist to the bitter end, jumping around, making a lot of noise, and attacking the zookeepers."

    "This classroom is the same."

    "In reality, being here is solely for our benefit, but not a single student wants to be here, especially on what the rest of the world considers a weekend."

    "The typical disarray of the morning class is amplified, the chatter reduced to white noise as various conversations fight for air time."

    "But, at the back corner of the class, looking lazily out of the window, sits a singular student."

    "I'd call out to her, but I don't feel like wasting my breath."
    
    show bg school_scienceroom at bgright
    with charamove
    
    stop ambient fadeout 10.0

    "It takes only a little time to force my way through the herd to Hanako's seat."
    
    show hanako basic_smile
    with charaenter

    #Hanako basic happy

    hi "Morning."

    ha "Morning."

    hi "Sleep well?"
    
    show hanako basic_normal
    with charachange

    ha "Not at all. You?"

    hi "Like a log, somehow."

    hi "I guess my meds are messing with my head again."
    
    show hanako emb_smile
    with charachange
    #Hanako laughs a little

    ha "You should watch out for that, sometimes medication does strange things to you."

    hi "I'll keep that in mind."
    
    show hanako emb_timid
    with charachange

    mi "Keep what in mind?"
    
    show bg school_scienceroom at bgleft
    show hanako emb_timid at left
    with charamove
    
    show misha hips_grin
    show shizu behind_blank at right
    with charaenter
    #Misha/Shiszune curious

    hi "Oh, nothing, just talking about meds."

    mi "Medication, eh?"
    
    show misha hips_smile
    with charachange

    mi "I guess that's an important enough topic."

    hi "Well, thank you for your approval."
    
    show misha perky_smile
    with charachange

    mi "Not at all."
    
    show misha cross_frown
    show shizu basic_normal2 at right
    with charachange

    mi "So, what's with you two being here and ignoring everyone else, huh?"
    
    #Misha pout

    mi "That's not very friendly."

    hi "I just thought I'd say hi to Hanako."
    
    show misha cross_smile
    with charachange

    mi "I see, I see…"
    
    show hanako basic_worry at left
    with charachange

    ha "I was going to go over the plans for our date this afternoon…"

    mi "I see, I…"

    show misha perky_confused
    with charachange
    #misha Surprised

    mi "Waitwhat?!"
    
    show shizu adjust_frown at right
    with charachange

    shi "…"
    
    show misha perky_sad
    with charachange

    mi "Oh, right, sorry…"
    
    show misha sign_confused
    with charachange

    "Misha, who's reflexive signing had stopped mid-sentence, hurries to bring Shizune up to speed."

    #shizune smile
    show shizu behind_smile at right
    show misha perky_smile
    with charachange

    #eh, just trying this out for shits and giggles

    $ doublespeak(shi,mi,"…","Um, I guess congratulations are in order then.")
    
    show shizu adjust_happy at right
    show misha hips_smile
    with charachange

    $ doublespeak(shi,mi,"…","I'm glad that you both are getting along so well.")

    hi "You're… not mad or anything?"
    
    show shizu basic_normal at right
    show misha cross_smile
    with charachange

    $ doublespeak(shi,mi,"…", "Why would I be?")

    hi "I… suppose you're right."
    
    show misha cross_grin
    with charachange

    mi "Yeah, good job, Hisao~!"

    mi "I mean, you've bailed out on helping us so much recently, but that's not a problem."
    
    show misha perky_smile_close
    with charachange

    "Misha leans towards me and whispers in my ear, as if trying to hide something from Shizune."

    mi "Between you and me I think that Shizune makes up a lot of the “work” she gave you anyway."

    show shizu behind_blank at right
    show misha hips_laugh
    with charachange
    #Shizune neutral and misha laughing

    mi "But now Hanako can become friends with everyone, right? Right?!"
    
    show hanako cover_worry at left
    with charachange

    ha "I… guess."
    
    show misha hips_grin
    with charachange

    mi "See! I think that this is the best thing for everyone."
    
    show misha sign_smile
    with charachange

    mi "You look after her, okay now Hisao?"

    hi "Right, right, I got you."

    hi "Now, are you going to pay attention to the man at the front of the class anytime soon?"
    
    show shizu basic_normal2 at right
    show misha perky_confused
    with charachange
    #misha/Shizune ? faces

    mi "Eh? What are you talking about, Hisao?"
    
    show muto irritated behind misha at tworight
    with charaenter

    mu "I believe, Miss Shiina, that he is referring to me."

    show shizu basic_normal at right
    show misha perky_sad
    with charachange
    #Misha/Shizune sad
    
    stop music fadeout 6.0

    "It would seem that while Misha and Shizune were so wrapped in Hanako's and my drama, Mutou had already settled the rest of the class."
    
    show misha sign_sad
    with charachange
    
    with Pause(0.2)
    
    hide misha
    with charaexit

    "Embarrassed, Misha turns slowly to the front of the class, gives Mutou a sheepish wave, and returns to her seat."
    
    show shizu behind_blank at right
    with charachange
    
    with Pause(0.2)
    
    hide shizu
    with charaexit

    "Shizune follows suit, replacing the wave with a curt bow."

    mu "Well then, now that we have been brought up to speed on the class's gossip, I shall now attempt to bring you all up to speed on relativity…"

    #LOL physics joke. I doubt even people who care will get this one.

    "I gently pat Hanako's hand before following Misha and Shizune back to my seat."
    
    hide hanako
    hide muto
    with charaexit
    
    show bg school_scienceroom at bgright
    with charamove

    #hide Hanako
    
    play music music_another fadein 6.0

    "I can't believe they're taking this so well."

    "Though the fact that Hanako was the one that told them may have had something to do with that."

    "It doesn't take Mutou too long to get lost in the joy of lecturing, and I use his distraction to whisper to Misha…"

    hi "Psst! Misha!"
    
    show misha perky_smile at twoleft
    with charaenter

    #Misha Smile

    mi "What's up?"

    hi "So, you and Shizune aren't angry?"
    
    show misha perky_confused at twoleft
    with charachange

    mi "At what?"

    hi "Hanako and I dating?"

    #misha small lol
    show misha cross_grin at twoleft
    with charachange

    mi "Wahahaha~! of course not!"

    mi "Shizune said it herself; why would we?"

    hi "I… dunno."
    
    show misha cross_smile at twoleft
    with charachange
    #Misha Srsbsns

    mi "Look, we might not be her friends, but then again, no-one is."

    mi "Still, we all want what's best for her, right?"

    mi "If you can get her to talk to others, then that's a good thing."

    hi "I guess that makes sense…"
    
    show misha hips_laugh at twoleft
    with charachange
    #misha big lulz

    mi "Of course it does, I said it!"

    mi "Wahahaha—{w=.3}{nw}"
    
    show muto irritated behind misha at rightwallopen
    with charaenter

    mu "Shiina…!"
    
    show misha perky_sad at twoleft
    with charachange
    #Misha "uh-oh"

    mi "…ha. Sorry."

    "Misha leans back into her “good student” position, and Mutou resumes his ramblings."
    
    hide misha
    hide muto
    with charaexit
    
    show bg school_scienceroom at bgleft
    with shorttimeskip

    "Surprisingly, it doesn't take long at all for the class to come to an end."
    
    show muto normal
    with charaenter

    mu "…and that's that. I should remind you all that this is practically your last class before the exams next week."

    mu "Monday and Tuesday will be revision days, so if you have any questions, please use them to ask me then."

    mu "The exam timetable will be posted on the noticeboard by tonight, please study it carefully."

    mu "And…"
    
    play sound sfx_normalbell
    #sfx bells
    
    show muto smile
    with charaenter

    mu "…have a good weekend."

    "The class is practically empty by the time Mutou finishes his sentence."

    "Before he leaves, though, he gives me a cryptic salute."
    
    hide muto
    with charaexit

    "I guess too much science really does make you crazy."
    
    show bg school_scienceroom at bgright
    with charamove
    
    show hanako basic_normal
    with charaenter

    #Hanako, basic

    hi "So then, where should we meet up?"
    
    show hanako cover_distant
    with charaenter

    ha "Um… if it's okay with you, then can you meet me at the Green Door in about an hour?"

    "I strain my memory to work out where Hanako is talking about."

    hi "Green Door… oh, you mean the door to the woods out the back of the school?"
    
    show hanako basic_smile
    with charachange
    #hanako slight smile

    ha "That's right. Is that okay?"
    
    stop music fadeout 6.0

    hi "It's perfect; I think I'll go get changed now."
    
    ha "Me too."

    hi "See you there then."
    
    show hanako basic_bashful
    with charachange
    #hanako big smile

    ha "Okay!"
    
    scene black
    with dissolve

    #Chapter end. Close on a timeskip or something.

    return

label en_HT9:

    #Splitting this scene to help the H-tagging

    #HT9 – Lullaby for Strain

    #Well, here it is, the fated H-scene scene. It'll take a bit of getting to, but it's there.
    #And I may also have a second one planned.
    #So ner.

    #BG Greendoor with timeskip
    scene bg school_greendoor at bgleft
    with locationchange
    
    play music music_happiness fadein 2.0

    "For once, I am thankful that girls seem to take an eternity to get ready."

    "My early night last night meant that I hadn't prepared any food for today, breaking the one promise that I made to Hanako about today."

    "Luckily, I still had some left over food from my last shopping trip, so I was able to hurriedly throw together a semblance of a picnic basket in a short amount of time."

    "Even so, I find myself waiting for a good fifteen minutes by the small, green door before Hanako finally arrives."

    #Show Hanako casual basic
    show hanako emb_smile_sun
    with charaenter

    ha "H..hello. Have you been waiting long?"

    hi "Not at all, I only just got here myself."

    hi "I brought along a bit of food, but I didn't know where we were going so I kinda guessed…"

    "Nice save; now it doesn't matter that all you've packed is left overs."

    ha "I think anything will do, really."
    
    show hanako emb_blushtimid_sun
    with charachange

    ha "But will you be okay to carry that?"

    hi "I can't see why not. We're not going rock climbing or anything, are we?"

    show hanako emb_downtimid_sun
    with charachange
    #hanako look down

    "Hanako looks away, as if she doesn't want to answer."

    hi "…Are we?"
    
    show hanako emb_blushtimid_sun
    with charachange

    ha "Well, not exactly. But… it is a bit of a walk…"

    "I take stock of Hanako in her yellow dress."
    
    # Inserted dialogue to force the dress to make sense. Sue me. -Alphabro
    "I'm a bit surprised at her choice of attire; it's the most that I've ever seen her show of her scars before."
    
    "She lets her hair drape over her right side and keeps her body turned just slightly away from me. I suppose she still isn't exactly comfortable with showing her skin."
    
    "Then again, she still chose to wear the dress for our date. That's got to mean something, right?"

    "At the very least, she certainly doesn't look like she's about to go climb a mountain."

    "Maybe she's just being overly cautious with me?"

    hi "Well then, if that's the case, we'd best be off, right?"

    hi "The day is simply wasting away…"
    
    show hanako emb_emb_sun
    with charachange
    #Hanako casual surprised

    ha "Oh! So it is! We should go…"
    
    play sound sfx_door_creak
    
    hide hanako
    with charaexit

    "Hanako pushes through the door in the wall, and the cool air of the woods beyond it hits my nostrils."
    
    scene bg school_forest1
    with locationchange
    
    play ambient sfx_park fadein 2.0
    #bg woods1

    "We have barely taken a step into the greenery, yet I still feel relaxed."

    hi "So… where are we headed?"
    
    show hanako emb_emb_sun at tworight
    with charaenter

    ha "There's a place I want to show you."

    ha "It's a bit of a walk, but it's worth it."

    hi "Alright then, you're the boss…"
    
    show hanako emb_smile_sun at right
    with dissolvecharamovefast
    
    hide hanako
    with charaexit

    "Hanako simply smiles at me, then strides off at an amazing pace."
    
    scene bg school_forest2
    with locationchange

    "I almost have to jog to keep up, constantly watching the ground for errant roots waiting to trip me up."

    "But every now and again, on a clear stretch of path, I manage to lift my eyes long enough to take a look at Hanako."
    
    show hanako emb_emb_sun
    with charachange

    "Unlike myself, she seems to be able to walk along with her head up, but that's not what catches my eye."

    "Her figure easily glides over the roots that have been hindering my progress, and each movement sends ripples through her dress and hair."

    "This is the first time I've ever looked at her seriously, but my trained eye can tell that underneath her loose clothing lies a pretty nice figure."

    "If only…{w=.3}{nw}"
    
    play sound sfx_impact
    show bg school_forest2 at bgright
    show hanako emb_blushtimid_sun at tworight
    with vpunch
    
    with Pause(0.2)
    
    "While I'm distracted, my foot catches a root from underneath and nearly throws me flat on my face."

    ha "Are you alright?"

    hi "Yeah, I wasn't looking where I was going, and I guess I tripped over something…"

    "Hanako squats down next to me, offering her hand to help me up."

    "I should really keep my eyes on the ground as opposed to perving."

    "It could be bad for my health…"

    ha "I didn't realise; am I going too fast?"
    
    show hanako emb_downtimid_sun at tworight
    with charachange

    ha "I just thought we might run out of time…"

    hi "No, it's okay, I'll be more careful. Thanks…"
    
    show hanako emb_blushtimid_sun at tworight
    with charachange

    "Hanako pulls me to my feet, and I collect the basket from where it has fallen."

    hi "Right then, let's go, shall we?"
    
    show hanako emb_emb_sun at tworight
    with charachange

    ha "Right."
    
    hide hanako
    with charaexit

    "Hanako twists on her heels, the resultant fluttering of cloth and hair mesmerising me for a moment."

    "Shaking my head to regain control, I set off after her."
    
    scene bg school_forestclearing
    with locationchange
    #BG woods 2

    "We continue to push through the woods for ages."

    "The dirt path that we were following peters out, fading from an obvious thoroughfare to practically nothing."
    
    show hanako emb_emb_sun
    with charaenter

    "Yet Hanako never breaks stride."

    "She deftly pushes branches out of her way, whilst I seem to be struggling with every step."

    "I guess this is what happens when you grow up in the city."

    "In a short clearing, I manage to avoid the trees for long enough to check my watch."

    "We've been hiking for nearly an hour."

    hi "So…"

    extend " just how much further is it?"
    
    show hanako emb_smile_sun
    with charachange

    ha "Not far, just this last thatch and we should be able to see it…"
    
    play sound sfx_rustling
    
    hide hanako
    with charaexit

    "Hanako disappears into a dense patch of vegetation, and I quickly follow through the rapidly closing gap."

    "If I lose track of her now I've got no idea how to get back to the school."

    "But, despite my best efforts, the figure in the yellow dress is gone; swallowed by the trees."

    hi "Hanako?"

    ha "I'm here Hisao… just a little further…"
    
    show bg school_forestclearing at bgleft
    with charamove

    "I follow the sound of her voice, the dense greenery surrounding me."
    
    stop music fadeout 4.0

    hi "Where? I can't see you…"
    
    stop music fadeout 1.5

    "I hear Hanako gasp a little…"

    hi "Hanako? Is something wrong?"
    
    play sound sfx_rustling

    "I charge through the branches, not caring what happens to me…"
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    #bg white

    "Bright light shines in my eyes, blinding me after the darkness of the woods."

    ha "We're here."
    
    scene bg school_picnic
    with whiteout

    #bg valley with fade
    
    play music music_twinkle

    "Slowly, my vision returns to me, revealing a vast valley stretching for as far as the eye can see."

    "Green treetops fill my vision, uninterrupted by human development."

    hi "Where… are we?"
    
    show hanako emb_emb_sun at tworight
    with charachange

    ha "The other side of the mountain."

    hi "This is a great spot. How did you find it?"
    
    show hanako emb_downsmile_sun at tworight
    with charachange

    ha "Well, I used to skip class a lot, and I found it then…"
    
    show bg school_picnic at bgright
    show hanako emb_downsmile_sun at right
    with charamove_slow

    "I take my gaze off Hanako to take in the view of the valley once again."

    "It's miles from anywhere, on the back side of the hill that the school rests on, totally opposite the town."
    
    show hanako emb_smile_sun at right
    with charachange
    
    show bg school_picnic at center
    show hanako emb_smile_sun at tworight
    with charamove

    ha "You can almost imagine that there's no-one else on the planet, can't you?"

    hi "Yeah… wow…"

    "We both look out over the valley, side by side, in silence."

    "I feel my hand reaching out from my side, and the slight warmth as it wraps itself around Hanako's."

    "I'm not sure if I wanted to share a bond with her, or if I was simply reaffirming that I was not alone here, but it felt like the right thing to do."

    "I go to take a step out into the clearing, but Hanako gives my hand a slight tug."
    
    show hanako emb_blushtimid_sun at tworight
    with charachange

    ha "I… wouldn't get too close to the edge."

    ha "It's a long fall."
    
    scene bg school_picniccliff at bgleft
    with locationchange

    "Moving my eyes downwards, I see what she means."

    "Whilst we are standing on a bit of a clearing, it is only a few meters from a cliff edge that dives directly to the valley floor."

    "The rolling green of the valley gives a false perspective of how far away the edge actually is."
    
    scene bg school_picnic
    show hanako emb_emb_sun at tworight
    with locationchange

    hi "Right. Got ya."

    hi "In that case, should we have some lunch?"

    "Truth be told, I'm starving. Skipping breakfast was a dumb idea."
    
    show hanako emb_smile_sun at tworight
    with charachange

    ha "Sure."
    
    show bg school_picnic at bgleft
    show hanako emb_smile_sun at center
    with charamove
    
    show hanako emb_smile_sun at centersit
    with charamove

    "Hanako spreads out her dress and sits on the grass, and I start unpacking the basket."

    hi "It's not much, but I hope this will do."
    
    show hanako emb_blushtimid_sun at centersit
    with charachange

    ha "I… I don't mind."
    
    show hanako emb_smile_sun at centersit
    with charachange

    ha "So long as it's here…"

    "I watch Hanako as she eats her food, and not once does she take her eyes off the expanse before us."

    "And I don't really blame her. It's hard to believe that this is Japan."

    "It does not take us long to consume my meagre offerings. I guess these things are best left to girls, after all."

    "I close up the basket and sit back down next to Hanako."
    
    show hanako emb_downsmile_sun at centersit
    with charachange

    "To my surprise, she leans her head against my shoulder."
    
    show bg school_picnic at center
    show hanako emb_downsmile_sun at tworightsit
    with charamove

    "Gingerly, I put my arm around her shoulder, and together we just stare out over the valley."

    hi "Say, Hanako…?"
    
    show hanako emb_smile_sun at tworightsit
    with charachange

    ha "Yes?"

    hi "What do you think you'll do after you graduate?"
    
    show hanako emb_blushing_sun at tworightsit
    with charachange

    "Hanako doesn't move, but I can almost feel her thinking on my shoulder."
    
    show hanako emb_blushtimid_sun at tworightsit
    with charachange

    ha "I haven't really thought about it."

    ha "Maybe something in medicine."

    hi "Medicine? Have you got the grades for that?"
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "Don't know. Why, do you need good grades?"

    hi "I think so."
    
    show hanako emb_blushing_sun at tworightsit
    with charachange

    ha "Well, I don't think I have bad grades."

    ha "Maybe I should look into it."
    
    "And with that, the topic seems to close."

    "I guess Hanako and Lilly have a lot in common, once you get past the obvious differences."

    "I suppose they're both right, as well."

    "Since the beginning of the year, my entire life has changed."

    "There's still a fair amount of time between now and graduation."

    "And years before finishing university."

    hi "Life can wait. I think I want to deal with now, first."
    
    show hanako emb_emb_sun at tworightsit
    with charachange

    ha "Hmm. That's pretty deep, Hisao."

    "Damn, I didn't even realise I was thinking out loud."

    hi "Thanks. I was just thinking about what Lilly told me yesterday."
    
    show hanako emb_blushtimid_sun at tworightsit
    with charachange

    ha "Oh? Lilly talked to you too?"

    hi "Yeah, she was just talking about how putting too much thought into things doesn't always help."
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    #hanako ?

    ha "Strange… she said something similar to me the other day."

    hi "Well then, what a coincidence, eh?"

    ha "True… oh…"
    
    show hanako emb_smile_sun at tworightsit
    with charachange
    #Hanako Happy
    ha "It's about to start!"
    #Had to change the above to a normal line because an extend was not working properly. -md01
    
    
    hi "Eh? What?"

    "Hanako doesn't say anything, but simply points out into the valley."
    
    stop ambient fadeout 4.0

    hi "What, I don't see anything…"

    ha "Shhh…"

    "For a moment, it seems like nothing has changed."
    
    $ renpy.music.set_volume(0.15, 0.0, channel='ambient')
    
    play ambient sfx_cicadas fadein 3.0

    "But, slowly, I notice the rising of the cicada's cries."

    "Flocks of birds start to swarm towards the valley, circling around patches of trees."
    
    scene bg school_picnic_ss at center
    show hanako emb_smile_sun_ss at tworightsit
    with dissolvecharamoveslow

    "Then, without warning, a shadow starts to creep across the valley."

    hi "Sunset…"

    ha "Right. You can watch the change from day to night from here."

    "The shadow edges across the valley floor; a clear line between the light and the dark."

    "On one side, we can see the woods going to sleep, on the other, everything is still wide awake."

    hi "Cool…"

    ha "Isn't it?"

    hi "Still, shouldn't we be getting back?"

    hi "I really don't want to be hiking in the dark…"
    
    show hanako emb_downtimid_sun_ss at tworightsit
    with charachange

    #Hanako pouts

    ha "Okay…"
    
    show hanako emb_blushtimid_sun_ss at tworightsit
    with charachange

    ha "I just wanted to show you that."

    ha "I've never shown anyone that."

    hi "Thanks, Hanako. I don't think anyone's ever done something like that to me before."
    
    show hanako emb_smile_sun_ss at tworightsit
    with charachange
    #hanako smiles

    ha "You're welcome."

    hi "Shall we?"

    ha "Let's."
    
    show bg school_picnic_ss at bgleft
    show hanako emb_smile_sun_ss at centersit
    with charamove
    
    show hanako emb_smile_sun_ss
    with charamove

    "I gather up the picnic basket in one hand, and grasp Hanako's in the other."

    "She doesn't seem to mind, although her quick pace through the woods means that she spends most of the trip back pulling me along."

    return

label en_HT10:
    
    scene bg school_greendoor_ni at bgleft
    show hanako emb_smile_sun_ni
    with locationskip
    #bg green door.
    
    stop music fadeout 3.0

    "By the time we return to the Green Door, it is pitch black."

    "Our progress back through the woods was a lot slower than the trip out, mostly due to the dying light."

    hi "Say, it's pretty late, I think the Hall will be closed."
    
    show hanako emb_downtimid_sun_ni
    with charachange

    ha "I… I've got some food in my room."
    
    show hanako emb_blushtimid_sun_ni
    with charachange
    #Hanako embarrassed

    ha "D—d—do you want some?"

    hi "I think that would be good. I used up all my food on that crappy picnic we had for lunch."
    
    show hanako emb_smile_sun_ni
    with charachange
    #Hanako Releived
    
    stop ambient fadeout 2.0

    ha "O…okay. Come on, I'm pretty hungry."
    
    scene bg school_dormhanako
    with shorttimeskip
    
    #"NOTICE" "This is the point at which the art/scene direction for Release #1 ends. You can either wait for the next Release, hopefully within 1/2 weeks, or you can read on (keeping in mind that there will be no art or sound beyond this point)."
    #bg dormhanako
    
    play music music_heart fadein 4.0

    "Hanako's room is still as sparse as ever."

    "On her bed lie her rabbit and the Steiff bear I bought for her."
    
    "She busies herself by preparing a few sandwiches for us on her desk."
    
    show hanako emb_timid_sun at tworight
    with charaenter

    ha "I'm sorry, I don't have much, and if we use the kitchen people might see us…"

    hi "It's alright, I've managed on less before…"
    
    show hanako emb_downtimid_sun at tworight
    with charachange

    ha "Even so, it's rude of me to invite you here if I have nothing for you…"

    hi "Don't be silly, we're going out, right?"

    hi "It's natural for us to hang out, isn't it?"
    
    show hanako emb_smile_sun at tworight
    with charachange
    #Hanako embarrassed

    ha "I… I guess."

    "It doesn't take long for us to finish the sandwiches, and after a little cleaning up, Hanako's room is back to its usual, featureless state."

    "A quick check of the watch reveals that it is nearing nine."

    "I guess I need to study some time this weekend."

    "But first, I think I have to try something."

    hi "Say, I think I should go now, but first…"

    show hanako emb_blushing_sun at tworight
    with charachange
    #hanako mega embarrassed

    ha "Y… yes?"

    hi "I thought maybe we could try… you know… what we did yesterday."
    
    show hanako emb_blushtimid_sun at tworight
    with charachange

    ha "Eh?"

    "Now it's my turn to be embarrassed."

    "I've never really gone out with a girl before, so I don't know how to handle this kind of thing."

    hi "I was thinking, if you wanted to, maybe I could kiss you goodnight…"

    "Man, this is such a low point in my life."

    ha "S…sure."
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    scene ev hanako_kiss
    with dissolve

    "Hanako closes her eyes and puckers her lips, clasping her hands tight to her chest."

    "Nervously, I lean forward, and kiss her gently."

    "It lasts a little longer than expected, and before I know it, Hanako's arms are wrapped around me."
    
    scene bg school_dormhanako
    show hanako emb_blushing_sun
    with dissolve

    "Breathless again, we separate."

    "Hanako, however, looks intensely nervous."

    hi "Is something the matter? Was that too much?"
    
    show hanako emb_downtimid_sun
    with charachange

    ha "N… no that's not it."
    
    show hanako emb_blushtimid_sun
    with charachange

    ha "Um, Hisao?"

    hi "Yeah?"
    
    stop music fadeout 6.0

    ha "I… want to show you something, so don't go just yet, okay?"

    hi "O…kay."
    
    show hanako emb_blushing_sun
    with charachange

    ha "Just, um, just sit there for a second."
    
    play sound sfx_impact
    
    show hanako emb_blushing_sun at twocenteroff3
    show bg school_dormhanako at bgright
    with vpunch

    "Hanako pushes me onto her bed with more than a little force, and I almost fall over backwards."
    
    show hanako invis at twoleft
    with dissolvecharamove
    
    play sound sfx_lock
    
    with Pause(0.5)
    
    play sound sfx_switch
    scene bg school_dormhanako_ni at bgright
    hide hanako
    with locationchange    

    "Before I can complain, she has walked over to the door, locked it, and turned off the light."

    hi "Um, Hanako? What's the matter?"

    ha "Shhh…"

    "I can hear Hanako's voice waver as she returns to the center of the room, facing away from me."

    "With the light off, the room is lit only by the faint glow of the night sky as it radiates from the window."

    "It casts strange shadows around the room, and I can barely see what Hanako is…"
    
    "She…"

    return

label en_HT10h:
    
    play music music_hanakohscene fadein 4.0
    
    play sound sfx_whiteout
    scene ev hanako_scars_dark
    with whiteout

    "Hanako's dress falls off her shoulders and piles up on the floor, the fabric making a pleasant sound as it comes to a stop."

    hi "H…Hanako?"

    ha "S…shhh."

    ha "I… I w-wanted you to see this."
    
    show ev hanako_scars
    with dissolvecharamoveslow

    "My eyes begin to adjust to the gloom, and Hanako's figure starts to solidify against the shadows of the room."

    "As I watch, she gently lifts her hair from her back, throwing it over her shoulder."

    ha "This… this is me. All of me…"
    
    show ev hanako_scars_large_move
    with locationchange

    "I blink, and suddenly things begin to become clear."

    "The skin on Hanako's back lacks the smooth texture of most people."

    "Grafted skin, taught like a drum, stretches from her neck, right across her back, and down her right leg."

    ha "I… in the fire… I curled up."

    ha "I curled up in a ball, so my back is the worst."

    ha "So… w—what do you think?"

    "Words fail me, so I simply stand up and place my hands on Hanako's back."

    "Even though it looks like leather, it is still smooth to the touch."
    
    stop music fadeout 4.0

    "I find myself gently caressing the grafted skin whilst Hanako shakes before me."

    "Pressing my head against her neck, her scent suddenly fills my nostrils, sending shudders down my spine."

    #"Almost unconsciously, I unclasp her bra and let it fall to the floor, where it lands atop the yellow dress."
    
    play music music_romance fadein 4.0

    hi "Hanako…"

    extend " You look fantastic."

    "I'd be lying if I said anything else."

    "As I suspected, Hanako in the flesh is almost perfectly proportioned."
    
    scene bg school_dormhanako_ni 
    show hanagown stockworry_blush_close_ni
    with locationchange

    "My hands reach the border of the grafted skin, and I finger the divide up her neck, and she turns instinctively to face me."

    "Her eyes are red, but she doesn't cry."
    
    "I feel my shirt being undone; Hanako's hands deftly casting it onto the rapidly growing pile of clothes."
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    scene ev hanako_kiss_night
    with dissolve
    
    "We kiss again, and my free hand is struggling with my pants."
    
    scene bg school_dormhanako_ni 
    show hanagown nudeworry_blush_close_ni
    with locationchange

    "Within moments, Hanako and I are face-to-face, naked save our underwear."
    
    show hanagown nudenormal_blush_close_ni
    with charachange

    "I continue to trace the line of her grafts down her front."
    
    show hanagown nudeworry_blush_close_ni
    with charachange

    "She gasps a little as I touch her breast, so I take a slight detour."
    
    #Got rid of this line because lol non-canon -md01
    #"Guided by instinct, we fall backwards onto the bed. I begin to massage her nipple, which hardens almost instantly under my touch."
    
    "Guided by instinct, I massage her nipple, which hardens almost instantly under my touch."
    
    show hanagown nude_moan_close_ni
    with charachange

    "Hanako's gasp turns into a gentle moan, which I seal away with a kiss."
    
    show hanagown nude_moan2_close_ni
    with charachange

    "My fingers leave her nipple and trace the graft line downwards, and goose bumps begin to appear all over her skin."

    "I fear that I am in a similar state; my hands can't stop shaking, and my mind is awash with a million thoughts."

    "All that guides me now is raw emotion and instinct; nothing else matters but the flesh before me."
    
    show hanagown nudesmile_close_ni
    with charachange

    "As my hand reaches her panties, she leans backwards, but pulls me with her."
    
    #lol non-canon -md01
    #"She sits on the bed, and tugs at my underwear with nervous hands."
    
    "She sits on the desk, and tugs at my underwear with nervous hands."
    
    scene white
    with dissolve
    
    show ev hanako_kiss_night
    with dissolve

    "Once again we kiss, an uncoordinated, groping kiss, and I help her shuck my briefs."
    
#    scene evh hanako_missionary_underwear 
#    with whiteout

    play sound sfx_whiteout    
    
    scene white
    with dissolve

    show evh hanako_miss1
    with dissolve

    "There we are; her sitting on her desk, and me naked, leaning over her."

    "Both of our bodies have prepared ourselves for this; a fact obvious to an outside observer."

    ha "You… you look ready…"

    hi "Are we really going to do this?"

    "My heart pounds in my chest, nothing like what I have felt before, even during my heart attack."

    "Hanako's breathing comes in short, sharp gasps."

    "She wraps one hand around my neck, and gently strokes my sex with the other."

    "My hormones rage, and it takes mammoth self control to contain myself at this instant."

    "Words choke up in my mouth, and I have to swallow hard before I can even speak."

    hi "Ready?"
    
#    scene evh hanako_missionary_glance 
#    with charachange

    show evh hanako_miss2
    with dissolve

    "Hanako simply nods, and bites her bottom lip."
    
#    scene evh hanako_missionary_closed 
#    with charachange

    "I lean into her, twisting her soaked panties aside with one hand."

    "She uses the hand wrapped around my manhood to guide me, but even still, I slip a little before reaching my mark."
    
#    scene evh hanako_missionary_clench 
#    with charachange

    ha "Go… do it…"

    "I drive my hips forward slowly, and I feel Hanako's fingernail's dig into my back."

    "There is some resistance as I push forward, but the heat and friction instinctively drive me onwards."
    
    show evh hanako_miss3
    with dissolve

    "She inhales sharply as our hips meet."

    hi "Are you okay?"
    
#    scene evh hanako_missionary_glance 
#    with charachange

    ha "Y…yes… just be slow…"
    
    "Nervous tension fills me as I begin to grind myself into Hanako."
    
#    scene evh hanako_missionary_clench 
#    with charachange

    show evh hanako_miss4
    with dissolve

    "She wraps both arms around my back, pulling me into her."

    "Her warmth surrounds me, both inside and out."

    "She rocks her hips forward to match my thrusting, and we start to pick up the pace."
    
#    scene evh hanako_missionary_open
#    with charachange

    show evh hanako_miss5
    with dissolve

    ha "F…faster… please… faster…"

    "Sweat beads on both of our bodies, and I feel my grip on Hanako's back start to slip."
    
#    scene evh hanako_missionary_closed 
#    with charachange

    show evh hanako_miss6
    with dissolve

    "She notices this too, and wraps her legs around me; her ankles digging into the small of my back, pushing me further into her."
    
    show evh hanako_miss7
    with dissolve

    "Sharp pain shoots across my back as the fingernails dig in for extra grip, but this serves only to heighten the experience."

    "I press myself against Hanako's, her breasts sliding against my sweat-covered chest."
    
    show evh hanako_miss8
    with dissolve

    "I go to kiss her but her head is cocked back in ecstasy, so I kiss her scarred nape, once again tasting salt."
    
#    scene evh hanako_missionary_clenchs 
#    with charachange

    ha "Keep… keep going…"

    hi "I can't… I'm almost…"

    "I feel a familiar surging in my groin, and I try to remove myself from Hanako before it's too late."

    hi "Hanako… I have to…"
    
#    scene evh hanako_missionary_closed 
#    with charachange

    ha "I don't care, keep going!"
    
    show evh hanako_miss9
    with dissolve

    "Hanako's hips drive themselves into mine, and she clenches me to her body with her ankles."

    hi "I really…"
    
#    scene evh hanako_missionary_open
#    with charachange

    ha "Do it!"

    "I grit my teeth to the end, but the mixture of pleasure and pain is too much."

    "I am blinded by the rush as I thrust with my all into Hanako, and she matches my movements."

    "Her arms tighten, and I feel my skin break under her nails."
    
#    scene evh hanako_missionary_closed 
#    with charachange

    "Her legs tighten, and drive us closer together."

    "Her back arches, her hair falling away in a waterfall of purple."
    
#    scene evh hanako_missionary_ending
#    with charachange

    "I can take no more, and surge deep inside Hanako, my body wracking with each pulse as we orgasm."
    
    #window hide

#    scene bg school_dormhanako_ni 
#    show white 
#    with Dissolve(3.0)

    #window show
    
    stop music fadeout 10.0

    "Panting, sweaty, and completely locked in each other's grasp, Hanako and I stay still whilst the fog of sex slowly lifts."
    
    show evh hanako_miss10
    with dissolve

    "Slowly, Hanako brings her eyes back to mine."

    "This is one of the few times I have seen both of her eyes, and they both seem to say the same thing."
    
    show evh hanako_miss11
    with dissolve

    ha "I love you, Hisao."

    hi "I love you too, but…"

    "Before I can finish, Hanako kisses me, a slow, measured kiss, not like the frenzied ones of before."

    "I manage to pull away from her long enough to get a word in."

    hi "Hanako… I… in you…"

    return

label en_HT10x:
    
    scene ev hanako_after_smile 
    with locationchange

    play music music_twinkle fadein 1.0

    "We slowly untangle ourselves from each other."

    "The bed is covered in sweat and skin oil; proof of our deed."

    "Hanako reaches down into her soiled, twisted panties."
    
    scene ev hanako_after_worry 
    with locationchange

    ha "I know. I wouldn't have done it if I didn't know."

    hi "Know what?"

    ha "The consequences."
    
    scene ev hanako_after_smile 
    with locationchange

    ha "But, I think we will be fine."

    "I'm not sure on what she is basing her assumption, but I am too tired to care."
    
    stop music fadeout 8.0

    hi "Say, can I…"
    
    window hide

    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.1)

    hide heartattack alpha 
    with Dissolve (0.8)

    window show

    "My vision goes grey, and I start to feel dizzy."
    
    scene ev hanako_after_worry 
    with locationchange
    
    hi "Whoa…"

    "I sit down on Hanako's bed, and put out an arm to steady myself."

    ha "Hisao? What's wrong?"

    hi "I… dunno. Just a little woozy."
    
    hi "Too much exercise, eh?"
    
    scene ev hanako_after_smile 
    with locationchange
    
    with Pause(1.0)
    
    show black
    with shuteye

    "I manage a little smile, which Hanako returns, before I pass out onto her bed."

    return
    
label en_HT11:

    #HT11, wherein I please my back-washing desires.
    #I could not recommend getting yourself washed in this manner enough.
    #The title is from the Poltergeist CD (Ghost Hound OP)
    #Anyway, it'll probably be done with 2-3 CGs
    #Or we can cut it.
    scene black
    with dissolve
    
    show bg school_dormhanako_ss
    #show hanagown
    with openeye
    #Bg dormhana with eyes open and timeskip. Or skip to black then open later
    
    play music music_serene fadein 2.0

    "I awake to a warm touch on my stomach."

    hi "W… what happened?"
    
    show hanagown worry_blush_close_ss
    with charaenter
    #show Hanako pyjamas neutral
    
    "Hanako quickly retrieves her hand, not expecting me to be awake."

    ha "Oh… I was just checking…"

    ha "The nurse told me to keep an eye on you…"

    hi "The nurse?"

    "Swirling memories of the night before bubble and surface in my mind."

    "I can't think of anything that I'd really feel comfortable telling the nurse."
    
    show hanagown normal_close_ss
    with charachange

    ha "Well, after you, um, passed out, I called Lilly."

    "Lilly too? I get the feeling that I'm going to have some explaining to do…"

    hi "Lilly… right… so what then?"

    ha "Lilly came to check on you, and she called the nurse."
    
    show hanagown distant_close_ss
    with charachange

    ha "He wanted to know what we did during the day, and he got her to take your pulse."
    
    show hanagown normal_close_ss
    with charachange

    ha "He said that you were probably just a little dehydrated, but he asked us to keep an eye on you."

    "The fog of sleep starts to lift, and I start to notice a few things."

    "Firstly, the dim light of pre-dawn is visible around the outline of the curtains."

    "A quick scan of the room reveals that our clothes are exactly as we left them; scattered across the floor…"

    "Hang on…"

    "I pull back the sheets, revealing my naked form to the world."

    hi "H..Hanako… you said Lilly came in here?"
    
    #Hanako puzzled

    ha "Yes."

    hi "While I was… naked?"
    
    show hanagown drunkworry_close_ss
    with charachange
    #hanako embarrassed

    ha "I… I didn't think she'd notice…"

    hi "Huh, I guess you've got a point there. But you could have at least put my pants on…"
    
    show hanagown distant_close_ss
    with charachange

    ha "Sorry. I just panicked a little."
    
    show hanagown normal_close_ss
    with charachange

    "I place a hand on Hanako's shoulder."

    hi "That's alright. Thanks for looking out for me."
    
    show hanagown smile_close_ss
    with charachange
    #Hanako smile

    ha "It's okay. Oh, the nurse wanted to see first thing; he said he'd be in his office at seven."

    "Hanako's bedside clock reveals that this is just a little over ninety minutes in the future."

    hi "Good idea; I think I would have gone and seen him anyway."
    
    show hanagown drunkpout_close_ss
    with charachange

    "Hanako yawns, a deep, long yawn."

    hi "Huh, tired are we?"
    
    show hanagown drunknormal_close_ss
    with charachange

    "She nods, sleepily."

    ha "I stayed up all night watching you, just like the nurse asked…"

    "I know that Hanako meant no harm by that, but I can't help but feel a little unnerved knowing that someone was watching me sleep…"

    hi "Thanks, Hanako. You're pretty amazing, you know?"
    
    show hanagown smile_close_ss
    with charachange
    #Hanako embarrassed

    ha "It…it's nothing."
    
    show hanagown smile_ss
    with charachange
    
    "I get out of bed, and start putting on my clothes."

    hi "I'm going to head back to my room, and get ready to see the nurse."

    hi "You should really get some sleep."
    
    show hanagown normal_ss
    with charachange

    ha "Okay. Can I see you after?"

    hi "Sure thing. I'll come by and grab you when I'm done, 'kay?"
    
    show hanagown smile_ss
    with charachange

    ha "'kay."
    
    hide hanagown
    with charaexit
    
    "Hanako crawls onto the bed, and pulls the sheets over her."
    
    hi "G'night."
    
    #show bg school_dormhanako at bgleft
    #show hanagown smile_close
    #with dissolvecharamove
    
    #show bg school_dormhanako
    #show hanagown smile at tworightsit
    #with dissolvecharamove

    "I lean over and we kiss."

    ha "Night."

    "I grab the picnic basket and head out into the corridor, closing the door behind me as quietly as I can."
    
    scene bg school_dormhisao
    with shorttimeskip
    
    stop music fadeout 3.0

    #BG bathroom

    "Being so early, I decide to clean myself up before meeting with the nurse."
    
    scene bg school_dormbathroom
    with locationchange

    "After discarding my clothes into the laundry basket, I enter the small bathroom and start running the hot water."

    "Not wanting to disturb Kenji, I opt for the washbasin-and-hose option rather than the upright shower."

    "It's been a while since I've washed myself like this, anyway."

    "I fish out the little bath stool from the cupboard, and get myself ready."
    
    play ambient sfx_shower fadein 1.0
    
    show steam 
    show steam2
    with dissolve

    "There's something relaxing about washing like this, and it gives you a sense of purpose."

    "As I am scrubbing away at my legs, I hear the catch on the door click open."

    hi "Ah, Kenji, I'm in here. I'll be done in a bit…"

    ha "I… I'm not Kenji…"
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    play music music_heart fadein 3.0

    "Hanako stands in the doorway, naked and holding a towel."

    hi "Hanako? What are you doing here?"

    #Hanako embarrassed/CG

    ha "I… couldn't sleep."

    ha "So I was going to go to the nurse with you, but you were in here."

    ha "C…can we do it together?"

    hi "Um… s—sure. I suppose."

    "Hanako smiles, hangs up her towel, and kneels down behind me."

    #CG switch, Hanako kneeling behind Hisao. Perhaps a chain for different expressions?
    #Also lol where the hell is weee?

    ha "I guess I'll go first then…"

    "Hanako leans forwards, pressing herself into my back."

    "She reaches past me and grabs my washcloth, wetting it in the washbasin, and starts to scrub my back."

    ha "H—how is it?"

    "Remember, remain calm. That is important in situations like this…"

    hi "Gr…ood."

    ha "Grood?"

    hi "I mean great…"

    "Embarrassment aside, it does feel pretty good."

    "Like when someone offers to scratch your back for you, only when you're naked."

    "Actually, that may not be the best comparison."

    "Hanako leans forward again to rinse the cloth, but this time stays pressed against my back."

    "She wraps her arms around me and starts to wash my chest, then my stomach… and then…"

    #Chain CG (maybe) Of Hanako now pressed into Hisao

    hi "H…Hanako!"

    ha "Huh? Shouldn't I wash there?"

    hi "T—that's not it. It's just I…"

    "Hanako continues to rub the washcloth into my groin, which is already responding to her touch."

    hi "Ijustdontwannapassoutagain."

    "Hanako stops, and retracts the washcloth."

    ha "Y—you're right. You should see the nurse before we… do this kind of thing."

    "I grab the wash basin and empty its contents over the two of us."

    # Chain CG, Hanako wet

    ha "H—hey!"

    hi "Heh, we can still play around though. Here, it's your turn now…"

    "I spin on the bath stool, snatch the washcloth form Hanako, and start to massage it into her shoulders."

    hi "Here, you sit up here…"

    "We switch places, with Hanako sitting on the stool whilst I wash her back."

    # Chain CG (if you want) Hanako on the bath stool

    "I continue to wash her back, but every so often I feel my hands reaching around her sides to feel her chest."

    ha "I.. I thought you said we couldn't…"

    hi "I said I couldn't…"

    "Copying Hanako's earlier moves, I slide my hand between Hanako's thighs."

    ha "H—Hisao…"

    "She squeezes her legs together, causing my suds-covered hand to slip around her legs."

    "Hanako squeals a mixture of surprise and pleasure, and instantly I am reminded of where we are."

    "If Kenji were to find out about this, I would never hear the end of it."

    hi "I guess you're right. And I should go see the nurse as soon as possible."

    ha "O…okay."

    "I lean over Hanako, turn on the shower head on the flexible hose, and start to rinse us down."
    
    stop ambient fadeout 2.0

    "Our playtime at an end, we quickly dry ourselves and dress."
    
    scene bg school_dormhisao
    show hanako emb_timid_cas
    with locationskip
    #BG dormhisao
    #show Hanako casual embarrassed

    #"Hanako wears a new outfit that I haven't seen before. With hat and all, it's definitely a more concealing get-up than yesterday's attire."
    
    "Hanako wears the same outfit that I saw her in a few days ago, hat and all."

    ha "I was in a hurry, and it was already out, so…"

    hi "Don't stress; I like it."

    hi "It suits you…"
    
    show hanako basic_smile_cas
    with charachange
    #Hanako casual smile
    
    stop music fadeout 4.0

    ha "T…thanks."

    "I wrap my arm around Hanako, and together we walk to the nurse's office."
    
    scene bg school_nurseoffice
    show nurse neutral
    with shorttimeskip
    #BG nurse office w/fade
    
    play music music_nurse fadein 2.0

    "The nurse removes the stethoscope from my chest, and I re-button my shirt."

    nk "So, explain to me what happened yesterday."

    hi "Well, we went out for a bit of a walk in the woods, and then when I came back, I just felt really tired, and that's all I remember."
    
    show nurse concern
    with charachange

    "The nurse eyes me suspiciously."

    nk "So, on this… walk, was there any strenuous activity?"

    hi "Um, not really."

    nk "Did you eat much yesterday?"

    hi "I had a little bit of lunch and dinner, but I skipped breakfast."

    nk "What about water?"

    hi "I can't remember drinking much, to be honest."

    "The nurse taps his pen against his clipboard a couple of times, never once taking his eyes away from mine."

    "After a brief pause, he hands me a small container."

    nk "Behind that door you'll find a toilet. I'd like you to fill this up."

    hi "Sure thing…"
    
    show nurse neutral
    with charachange

    nk "Mid-stream, please."
    
    show bg school_nurseoffice
    show nurse neutral
    with shorttimeskip

    "There's something unnatural about urine samples."

    "Giving someone a warm cup of something you normally flush away is just… wrong."

    "But the nurse takes it as if I were offering him a normal glass of water, and inserts a couple of paper strips."

    "He swirls them around the yellow liquid, taps off the excess, and examines them."
    
    show nurse concern
    with charachange

    nk "Hmm, it's just as I thought."
    
    show nurse neutral
    with charachange

    nk "Your blood sugar is pretty low, and it looks like you were pretty dehydrated."
    
    show nurse grin
    with charachange

    nk "You've got to look after your body, especially if you are planning to take up “walking in the woods” as a hobby."
    
    show nurse fabulous
    with charachange
    #nurse smile

    nk "Do you get my drift?"

    "I guess it's impossible to hide anything from him."

    hi "Sure thing."
    
    show nurse neutral
    with charachange

    nk "You should go and get a good breakfast, and also drink a few litres of water today."

    nk "Not all at once, mind. Try a few bottles spread out across the day."

    hi "Got you."
    
    show nurse concern
    with charachange

    nk "Oh, and one last thing."

    hi "Hmm?"
    
    show nurse neutral
    with charachange

    nk "I know you already know this, but don't do anything now that you may regret later."

    nk "You know, on your “walks.”"

    hi "Um, right. I'll be careful."
    
    stop music fadeout 3.0

    nk "Please do. See you later."
    
    scene bg school_nursehall
    show hanako basic_worry_cas
    with locationchange
    #BG corridor.
    #show Hanako casual concerned/neutral

    "Outside the nurse's office, Hanako waits patiently."

    ha "So? What's the matter?"

    hi "Oh, nothing, it's nothing to do with my heart, thankfully."
    
    show hanako basic_bashful_cas
    with charachange
    #Hanako Smiles

    ha "That's good news!"

    ha "So, what should we do now?"

    hi "Well, I was just ordered to have a good breakfast, would you care to join me?"
    
    show hanako basic_normal_cas
    with charachange

    ha "That sounds like fun, but I don't think the Hall is open just yet…"

    hi "I was actually thinking we could head for the Shanghai, what do you think?"

    ha "O…okay. Let's go."

    return

label en_HT12:

    #This is the first of the scenes written since the changes to the Hanako paths.
    #I'll finish the HT path as per the new plan, then rewrite.
    #I just hate leaving things unfinished.
    #also, not entirely sure on Hanakos reaction at the end.
    
    scene bg suburb_shanghaiint 
    show hanako emb_emb_cas
    with locationskip

    play music music_dreamy fadein 2.0
    #bg shanghai with dissolve

    "As expected, the Shanghai is deserted."
    
    "Yuuko sits at the back of the café, her eyes red and droopy."
    
    show bg suburb_shanghaiint at bgright
    show hanako emb_emb_cas at tworight
    with charamove
    
    hi "Must have had a rough on last night then, eh?"
    
    show yuukoshang panic_up at twoleft
    with charaenter
    
    yu "Huh? Oh, no, I was just up late last night."
    
    show yuukoshang worried_down at twoleft
    with charachange

    yu "I was hanging out with… um… with a friend."

    "Yuuko's mid-sentence pause says more than her words, but in the interest of keeping her stable enough to serve us, I don't push the issue."

    hi "Right. I hope you had fun."
    
    show yuukoshang happy_up at twoleft
    with charachange

    yu "Oh, we did, I can assure… you…"
    
    show yuukoshang panic_down at twoleft
    with charachange

    "Yuuko suddenly blushes, as if realising what she has just said."

    "Must change the topic, quick…"

    hi "So, is breakfast being served yet?"
    
    show yuukoshang worried_up at twoleft
    with charachange

    yu "Sure thing, we have both traditional and western breakfasts available."

    hi "Well, I'll take a full western breakfast."
    
    show hanako basic_smile_cas at tworight
    with charachange

    ha "I'll take the same, please."
    
    show yuukoshang neutral_up at twoleft
    with charachange

    yu "Two breakfasts coming up."
    
    hide yuukoshang
    with charaexit
    
    show bg suburb_shanghaiint at bgleft
    show hanako basic_smile_cas at center
    with charamove
    
    show hanako basic_smile_cas at centersit
    with charamove

    "Yuuko disappears into the back of the cafe, and Hanako and I take our seats."

    hi "So, how are you feeling now? Still tired?"
    
    show hanako emb_timid_cas at centersit
    with charachange

    ha "A little."
    
    show hanako emb_smile_cas at centersit
    with charachange
    #Hanako smile

    ha "B—but better now that you're okay."

    hi "Yeah, same here. I was a bit worried that the nurse was going to ban me from… well, you know…"
    
    show hanako emb_downtimid_cas at centersit
    with charachange
    #Hanako Embarrassed looking down

    ha "Y—yeah."

    "Hanako looks away; apparently it's still a little early to bring up this subject in public."
    
    show yuukoshang invis at left
    with None

    "Then again, I can feel a blush spread across my face at the simple thought of last night."
    
    show bg suburb_shanghaiint at center
    show yuukoshang worried_up at Motion(trembleleft,8.0,repeat=True)
    show hanako emb_timid_cas at tworightsit
    with dissolvecharamove

    "Our uncomfortable silence is short lived, as moments later Yuuko returns, carrying two heaped plates of food."

    "I grit my teeth and prepare to dodge as the plates waver in Yuuko's grip as if she were daring gravity to run its course."

    hi "Do you want a hand there?"

    yu "N—no, I'm fine, I just—{w=.3}{nw}"
    
    play sound sfx_impact2
    
    show yuukoshang worried_down at twoleftsit
    show hanako defarms_shock_cas at tworightsit
    with vpunch
    
    with Pause(0.2)
    
    show yuukoshang neurotic_up at twoleft
    with dissolvecharamove

    "She slams the plates onto the table, and for a second I fear that they will smash, along with the table."
    
    show hanako def_worry_cas at tworightsit
    with charachange

    "Surprisingly, everything holds, albeit a little mixed up."
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "There we are, just as ordered."

    hi "Thanks."
    
    show yuukoshang worried_up at twoleft
    with charachange

    yu "Say, Lilly's not with you guys today?"

    hi "We decided to give her a day off. She always seems to be fretting over us, so it seemed only fair to give her a day to herself."
    
    show hanako emb_timid_cas at tworightsit
    with charachange

    ha "People… need time alone, I think."
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "Hmm, that sounds right enough."

    yu "But this isn't an excuse for the two of you to be alone, is it?"
    
    show hanako cover_worry_cas at tworightsit
    with charachange
    #Hanako embarrassed

    $doublespeak (ha,hi,"W-well, maybe…","Yeah, pretty much…")
    
    show yuukoshang happy_down at twoleft
    with charachange
    #Yuuko Happy

    yu "Oh ho, does that mean you two are, you know?"

    hi "I guess that's one way of putting it."
    
    show yuukoshang closedhappy_up at twoleft
    with charachange

    yu "Ha! I knew it!"
    
    show yuukoshang happy_up at twoleft
    with charachange

    yu "Don't worry though, I can keep a secret!"
    
    show hanako emb_timid_cas at tworightsit
    with charachange

    "My memory drifts back to the last time Yuuko promised that she would keep a secret for us."

    "My memory reminds me that this is a very bad idea."

    hi "There's really no need, it's not that much of a secret."
    
    show yuukoshang worried_down at twoleft
    with charachange
    #Yuuko saddened

    yu "Oh, alright. Still, I'm not one for gossip."

    "Something about that seems at odds with reality, but I think I'll let it slide."

    hi "So what else is happening with you, Yuuko?"
    
    show yuukoshang happy_up at twoleft
    with charachange
    #Yuuko happy

    yu "Well, I found my boyfriend again!"

    hi "Found? Again?"
    
    show yuukoshang neutral_up at twoleft
    with charachange

    yu "Yes! I found him again."

    yu "I thought he had moved or something, but it turns out he had just become a recluse."

    hi "Is that much better?"
    
    show yuukoshang closedhappy_up at twoleft
    with charachange

    yu "He's not dead!"

    hi "An added bonus, I must admit."
    
    show hanako basic_normal_cas at tworightsit
    with charachange

    ha "Where did you find him?"
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "I was going to visit Lilly after school the other day, and I ran into him there."
    
    hi "What was he doing at the school?"
    
    show yuukoshang happy_up at twoleft
    with charachange

    yu "Oh, he's a student!"
    
    show hanako def_worry_cas at tworightsit
    with charachange

    ha "I don't remember you visiting Lilly…"
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "I got a bit distracted, Kenji's got a lot of interesting things in…"

    hi "Kenji?"

    hi "As in militant anti-feminist hermit-dwelling blind-as-a-bat Kenji?"
    
    show yuukoshang happy_down at twoleft
    with charachange

    yu "Oh, so you know him then!"

    "I pinch the bridge of my nose, hoping that the pain will help me cope with the reality of the situation."
    
    show yuukoshang neutral_down at twoleft
    with charachange

    hi "So you're telling me that your boyfriend is my roommate, the guy with glasses so thick that they must weigh a tonne?"
    
    show hanako emb_timid_cas at tworightsit
    with charachange

    ha "And he's a little weird…"

    hi "And you've even been to my room, which involves walking past his room, and didn't even notice?"
    
    show yuukoshang worried_down at twoleft
    with charachange

    yu "Well, I wasn't looking for him then."

    hi "This makes no sense."
    
    show yuukoshang panic_up at twoleft
    with charachange
    #Yuuko confused

    yu "Why not?"

    hi "Because it doesn't, that's why."

    hi "I mean the guy rarely leaves his room, even to go to classes… wait…"

    hi "The other day, when I was pounding on his door…"
    
    show yuukoshang worried_up at twoleft
    with charachange

    yu "Oh, so that was you? He said it was an annoying jerk that would go away if I kept quiet…"

    hi "Absurd."

    "My brain has shut down."

    "I know that both Yuuko and Kenji have mentioned that they had lost their respective partners, but this seems to make no sense at all."

    "Then again, that alone makes it make perfect sense."

    "My fragile mind can't take any more abuse, so I start shovelling the hot breakfast into my mouth as quickly as I can."
    
    show hanako basic_normal_cas at tworightsit
    with charachange

    ha "So, how did you two meet?"
    
    show yuukoshang neutral_down at twoleft
    with charachange

    yu "Well, he used to come here every so often, always by himself, so I started talking to him."

    yu "Then, you know, we were out drinking one night, and one thing led to another…"
    
    show yuukoshang smile_up at twoleft
    with charachange

    yu "He was just so passionate about whatever he was raving about that I couldn't leave him alone…"

    yu "It's nice to have someone dedicated, you know."

    hi "Dedicated enough to just disappear for however long without telling you he was just up the road the whole time?"
    
    show yuukoshang worried_down at twoleft
    with charachange

    yu "What can I say? Sometimes people just need some space…"

    "Something tells me that, against all odds, Yuuko and Kenji are just… made for each other."

    "However, they were not made for me."

    "The sheer enormity of this revelation makes my head hurt, and with our breakfasts finished, there's no reason for us to hang around."

    hi "Well, I'd love to stay and chat, but we have a date."
    
    show hanako emb_timid_cas at tworightsit
    with charachange
    #Hanako confused

    ha "We do?"
    
    show yuukoshang smile_down at twoleft
    with charachange

    yu "Aw, isn't that sweet. Don't worry, I won't keep you."

    hi "Thanks. Here, keep the change."
    
    show bg suburb_shanghaiint at bgleft
    show yuukoshang invis at left
    show hanako emb_timid_cas at center
    with dissolvecharamove

    "I grab Hanako's hand, and we are out the door before Yuuko even gets the chance to clumsily bid us farewell."
    
    play sound sfx_storebell
    
    scene bg suburb_shanghaiext
    show hanako basic_normal_cas
    with locationchange
    #bg street

    hi "So, where to now?"
    
    show hanako cover_worry_cas
    with charachange

    ha "I don't know, I'm a little tired, actually."

    "Hanako has a point; the heavy breakfast in my stomach and the excitement of the last day has left me feeling a little sleepy, too."

    "I can only imagine what it would be like after having stayed up all night."
    
    stop music fadeout 5.0

    hi "How about we sit down for a bit? There's a small park just near here."
    
    show hanako basic_bashful_cas
    with charachange

    ha "Sounds good."

    scene bg suburb_park
    #show hanako basic_normal_cas
    with locationskip
    #bg picnic park
    
    play ambient sfx_park fadein 3.0
    
    "The little park is only a few minute's walk from the Shanghai."

    "Still being fairly early in the morning, the only other people in the park are the occasional joggers."

    "I half expect Emi to bound past on her black-ribbon prosthetics at any time; she seems like the type to trade a morning's sleep for a run, any day."

    scene bg suburb_park at bgleft
    with charamove
    
    show hanako emb_emb_cas at tworightsit
    with charaenter
    
    "We find a small bench under a tree, and take a seat."

    "The cool of the shade is refreshing; there's no doubt that summer is just around the corner."
    
    show hanako emb_downsmile_cas_close at tworightsit
    with charachange

    "Hanako rests her head against my shoulder, and I put my arm around her."
    
    show hanako emb_timid_cas_close at tworightsit
    with charachange

    ha "I'm glad you're not dead."

    hi "Not half as glad as I am, I can assure you."
    
    show hanako emb_emb_cas_close at tworightsit
    with charachange

    "Hanako laughs a little, a nervous titter on the edge of hearing."
    
    show hanako emb_blushtimid_cas_close at tworightsit
    with charachange

    ha "T—that's not what I meant."
    
    show hanako emb_downsad_cas_close at tworightsit
    with charachange

    ha "Last night, I kept thinking it was my fault."

    ha "Like, that you passed out because of what I did…"

    hi "I think you mean what we did; it was kind of a team effort…"
    
    show hanako emb_smile_cas_close at tworightsit
    with charachange
    #Hanako embarrassed.

    ha "I—it was good though."

    hi "I… didn't hurt you, did I?"
    
    show hanako emb_timid_cas_close at tworightsit
    with charachange

    ha "A little, but only at the start."

    hi "Sorry."
    
    show hanako emb_smile_cas_close at tworightsit
    with charachange

    ha "It's okay. I don't think it'll be like that all the time."

    hi "I guess you're right."
    
    show hanako emb_sleep_cas_close at tworightsit
    with charachange
    
    "…"

    hi "Er, Hanako?"

    "I get no response from Hanako, who has fallen fast asleep on my shoulder."

    "She deserves the rest, so I'm content to act as a pillow for the moment."

    "Besides, there are worse ways to spend a Sunday than to have a girl sleeping against you."
    
    scene bg suburb_park
    show hanako emb_sleep_cas_close at rightsit
    with shorttimeskip
    #timeskip?
    
    play music music_daily fadein 5.0
    
    show hanako emb_downtimid_cas_close at rightsit
    with charachange

    "Morning slowly gives way to the midday sun before Hanako stirs, gently moaning and wiping her eyes."
    
    show bg suburb_park at bgleft
    show hanako emb_downtimid_cas_close at tworightsit
    with charamove

    hi "Morning, sleepy."
    
    show hanako emb_timid_cas_close at tworightsit
    with charachange

    ha "Huh? Where am I…?"

    hi "The park. You fell asleep after breakfast."
    
    show hanako cover_worry_cas_close at tworightsit
    with charachange
    #hanako embarrassed

    ha "Oh… sorry…"

    hi "Don't be; you looked after me last night, you deserve a rest."

    ha "But it's still rude."

    hi "Don't sweat it. What's say we head home via Aura mart and pick up some snacks?"
    
    show hanako basic_bashful_cas_close at tworightsit
    with charachange
    
    stop ambient fadeout 1.0

    ha "S—sure."
    
    scene bg suburb_konbiniint
    show hanako emb_emb_cas
    with locationskip
    #bg Auramart
    
    $ renpy.music.set_volume(0.33, 0.0, channel='ambient')
    
    play ambient sfx_crowd_indoors fadein 0.5

    "The small convenience store is unusually busy for a weekend, but even still you couldn't call it crowded."

    "Hanako and I walk down the narrow aisles together, randomly grabbing snacks as we pass them."
    
    show bg suburb_konbiniint at bgright
    show hanako emb_emb_cas at tworight
    with charamove

    "As we pass by the toiletry section, something catches the corner of my eye, causing my heart to race a little."

    hi "Um, Hanako?"
    
    show hanako basic_normal_cas at tworight
    with charachange

    ha "Mmm?"

    hi "Say, I forgot to pick up, er, some chocolate milk. Could you go get it for me?"
    
    show hanako def_worry_cas at tworight
    with charachange
    #hanako puzzled

    ha "S-sure."
    
    show hanako invis at right
    with dissolvecharamove

    "Hanako turns around, wearing a quizzical look."

    "With her gone, I turn my attention back to the toiletries, specifically one section of the shelf."

    "I was hoping for a quick and discreet decision, but instead I am bombarded with dozens of choices."

    "Thin, thick, flavoured, glow-in-the-dark, ribbed, textured, vibrating, assorted…"

    "Tiny, brightly colored packages fill the shelf space between the toothpaste and the deodorant."

    "I am lost in a world totally unknown to me, when suddenly…"
    
    show hanako emb_timid_cas at tworight
    with dissolvecharamove
    #Hanako appears
    
    stop music fadeout 4.0

    ha "Here you are Hisao, I got…"
    
    extend " what are you looking at?"
    
    show bg suburb_konbiniint
    show hanako emb_timid_cas
    with ease

    hi "Eh!? Um, er… nothing…"
    
    show hanako defarms_shock_cas
    with charachange

    ha "Condoms?"
    
    stop ambient fadeout 0.5

    "Suddenly, every pair of eyes in the store is trained on us."

    "I can feel the sweat beading on my brow."

    hi "Well, I thought, that if…"
    
    show hanako emb_timid_cas
    with charachange

    ha "I-I… suppose it's a good idea."
    
    show bg suburb_konbiniint at bgright
    show hanako emb_timid_cas at twoleft
    with charamove

    "Hanako reaches out and grabs a packet marked “assorted,” adding it to our shopping basket."

    "Surprisingly, she seems to be less embarrassed about this than I am."

    hi "Aren't you worried? All these people are looking at us!"
    
    show hanako def_worry_cas at twoleft
    with charachange

    ha "Eh? Who is?"

    "Hanako looks up from the groceries, finally noticing the stares of the other people in the shop."
    
    show hanako defarms_shock_cas at twoleft
    with charachange
    #hanako deep embarrassed

    ha "I… w-well… I… we'vegottago."
    
    show bg suburb_konbiniint
    show hanako defarms_shock_cas
    with ease

    "Hanako turns bright red, grabs me by the sleeve, and rushes for the counter."

    "The attendant quickly scans the items and puts them into the bag, snickering a little when he finally pulls the small box from the basket."

    "Neither Hanako nor I can bear to make eye contact with him, and as soon as I have my change, we make a rush for the exit."
    
    scene bg suburb_konbiniext
    show hanako emb_downtimid_cas
    with locationchange
    #bg street

    #hanako embarrassed looking down
    
    play music music_another fadein 3.0

    "Outside the store, I could almost swear that I can hear laughing from inside."

    ha "Why didn't you tell me they were looking?"

    hi "Well, they weren't until you said… that."
    
    show hanako emb_blushtimid_cas
    with charachange

    ha "Condoms?"

    hi "Yeah."
    
    show hanako emb_blushing_cas
    with charachange
    
    ha "Well, they're perfectly normal, right?"

    hi "I… guess. But that doesn't mean you should yell it out…"
    
    show hanako emb_downtimid_cas
    with charachange
    #hanako deep embarrassed

    ha "S—sorry."

    "I pat Hanako on the head."

    hi "Don't worry, it's over now. And we've got them now…"
    
    show hanako emb_blushtimid_cas
    with charachange

    ha "R—right. Better to be safe."

    hi "Right."

    "…"

    hi "Should we head…"
    
    show hanako emb_blushing_cas
    with charachange
    
    stop music fadeout 3.0

    ha "Y-yeah, let's head back."
    
    hide hanako
    with charaexit

    "Hanako and I set off back towards the school at a nervously fast pace."

    "Not once do either of us look back towards the little convenience shop."

    return

label en_HT13:
    
    scene bg suburb_konbiniext
    with locationchange

    scene bg school_dormhanako
    with shorttimeskip
    #bg hanadorm
    
    play music music_one fadein 2.0

    "As if we were both on autopilot, we head directly for Hanako's room."
    
    play sound sfx_lock
    
    show hanako basic_bashful_cas
    with charaenter
    #Hanako bashful ?

    "Hanako locks the door behind her, not once taking her eyes from mine."

    ha "I… I guess you'll want to clean up after such a stressful day?"

    hi "Eh? But I hardly… oh."

    hi "Right. Clean up."
    
    show hanako basic_bashful_cas:
        xalign 0.5 alpha 1.0
        linear 1.0 xpos 0.0 alpha 0.0

    "I drop the bag of groceries and unbutton my shirt whilst Hanako fumbles with her jacket."
    
    play sound sfx_switch
    
    scene bg school_dormhanako_nl     
    
    "She clicks off the light as her clothes fall to the floor for the second time in as many days."
    
    show hanagown nudenormal_blush_close_nl
    with charaenter

    "I step over the rapidly growing pile of clothes to take Hanako in my arms, her skin warm and tender against mine."

    ha "Shouldn't we wait until we get into the bathro…"
    
    scene ev hanako_kiss_day
    with dissolve

    "I stop Hanako's words with a long, deep kiss."

    "She resists for a moment, but soon she is kissing me back with equal ferocity."
    
    scene bg school_dormhanako_nl
    show hanagown nudesmile_close_nl
    with locationchange

    "As we part, she gently bites my lower lip, stretching it a little before releasing it."

    "I use the brief reprise to free myself from my strained pants."

    "A moment later and either my pants or my raging member would suffer irreparable damage."
    
    show hanagown nudeworry_blush_close_nl
    with charachange

    "Hanako fumbles around in the dim afternoon light, desperately trying to find the small box that caused such embarrassment such a short time ago."

    "Packets of snacks fly across the room as she retrieves the colored box."
    
    show hanagown nudenormal_blush_close_nl
    with charachange

    ha "So, uh… how do we…?"

    hi "I don't think there's much to it, you just… put it on."

    hi "I think."
    
    show hanagown nudeworry_blush_close_nl
    with charachange

    "Hanako tears open the box in a nervous panic, sending little foiled packets across the room."

    ha "Oops…"

    hi "R…relax."

    "My quivering voice probably doesn't have the calming effect that I had hoped."

    return

label en_HT13h:

    hide hanagown
    with charaexit

    "I am temped to help Hanako search, but watching her kneeling, naked body squirming on the floor is far more appealing."

    #Perhaps a cg?

    "The light is better now than it was yesterday, and I can clearly see the differences in the grafted and original skin."

    "Just as she said last night, the majority of the scarring is on her back, with only the upper outside of her right thigh showing any damage."

    "Her entire left leg is like china; incredibly pale and smooth."

    "Wearing concealing clothing for most of her life must have protected her skin from the ravages of the sun."

    #Damn, even I do not know what the fuck I am talking about anymore.

    scene white
    with dissolve
    
    show evh hanako_finger_close #:
        #xalign 0.5 yalign 0.5 zoom 0.4 # my my, instead of resizing cg you used ingame zooming?.. [str]
    with dissolve

    "I can watch no longer, so I kneel down, flipping Hanako onto her back as I do."

    "She gasps a little, but I set upon her like an animal in heat."

    "I kiss her neck whilst one hand seeks out the thighs that were enchanting me seconds ago."
    
    show evh hanako_finger_1:
        xalign 0.5 yalign 0.5 zoom 1.0
    with dissolve
    
    "She reflexively clenches her legs together around my hand, but relaxes a little as I slide my probing fingers ever deeper into the tuft of her pubic hair."
    
    show evh hanako_finger_2
    with dissolve

    "My fingers feel a warm wetness, and I push forward."

    "Again, she gasps slightly as my fingers massage her insides."
    
    show evh hanako_finger_3
    with dissolve

    ha "H—H—Hiiiisao…"
    
    show evh hanako_finger_close_scroll:
        xalign 0.5 yalign 0.0
        linear 8.0 yalign 1.0
    with dissolve

    "I kiss down her neck to her chest, feeling the texture change as I move from the grafted skin to the natural skin of her breast."
    
    show evh hanako_finger_3
    with dissolve

    "I rub her privates a little harder and softly bite her nipple, resulting in a delighted squeal from the girl pinned beneath me."
    
    scene bg misc_ceiling
    with locationchange
    
    play sound sfx_impact
    with vpunch

    "Suddenly, my world flips over, and I find myself looking at the ceiling."

    "Somehow, Hanako has managed to flip me over, and is now straddling my stomach."

    #too much?

    "Her pubic hair tickles my skin and she bends over me, sucking on my neck, and then biting my earlobe."

    "Payback for the nipple, I guess."
    
    scene white
    with dissolve
    
    show evh hanako_cowgirl_1
    with dissolve

    "After a breathless second, she rears back up, flicking her hair away from her face with the same motion."

    "Both of her dark eyes are fixed on mine, and for a moment all we can do is stare at each other."
    
    show evh hanako_cowgirl_2
    with dissolve

    ha "I… I guess it's time…"
    
    show evh hanako_cowgirl_3
    with dissolve

    "Shuffling on her knees, Hanako slides herself over my erection, picks up a foil packet from the floor, and tears it open."

    hi "I don't think…"

    "Too late."

    "The rubber circle slips straight out of the packet and lands amongst the scattered clothes and snacks."
    
    show evh hanako_cowgirl_4
    with dissolve

    "Hanako panics and tries to pick up the condom, but that only causes it to slip out of he grasp once again."

    "I scoff a little at the hilarity of the image."

    "A second ago, Hanako was lost in the flurry of sex, but now she's back to her usual, embarrassed self."
    
    show evh hanako_cowgirl_5
    with dissolve

    ha "D—don't laugh. It's slippery…"
    
    show evh hanako_cowgirl_6
    with dissolve

    hi "I think that's the point, here…"
    
    show evh hanako_cowgirl_7
    with dissolve

    "I retrieve a fresh packet from the floor, and take out the rubber, placing it on the head of my cock."
    
    show evh hanako_cowgirl_8
    with dissolve

    ha "C… can I?"

    hi "Eh? I guess…"

    "Hanako reaches down, her fingers wrapping around my dick and unrolling the latex over its shaft."

    "I gulp a little as it unrolls, as it applies a little pressure along my entire length."
    
    show evh hanako_cowgirl_7
    with dissolve

    "The experience is over in a second, and Hanako wastes no time in positioning herself over me, my shaft still in her hand as she rears herself over me."

    #damn it why am I always ripping off the Lilly path?

    ha "I… I'm doing it…"

    "She lowers herself, guiding me into her with her hand."

    hi "H—how is it?"
    
    show evh hanako_cowgirl_9
    with dissolve

    ha "It feels different… but good…"

    "She falls onto my chest, wrapping her arms around my neck and burying my face in her breasts."

    "In response, I rock my hips forward and upwards."

    "Inside the latex, I feel slightly different, but Hanako's warmth still envelops me."

    "With each thrust, Hanako rolls her own hips onto mine, driving us ever closer together."

    "I reach around her body and grab her butt, pulling her in further still."
    
    show evh hanako_cowgirl_10
    with dissolve

    "Her arms tighten, driving my face deeper into her chest."

    "Breathing becomes gasping, which becomes sub-vocal screaming."
    
    show evh hanako_cowgirl_11
    with dissolve

    ha "H… Hi… Hisssssssaa ooooooh…."

    ha "Hiiiii Hi Hi Hi Hiiiiissssssa…"
    
    show evh hanako_cowgirl_12
    with dissolve

    "Sweat beads on my brow only to be wiped away by breasts, and I find myself digging my fingers into the soft skin of Hanako's behind."

    "With the extra grip, I thrust upwards with all the force I can muster, and Hanako loses all ability to make words."

    ha "Hiiiahahahaaaaaa"
    
    show evh hanako_cowgirl_13
    with dissolve
    
    $ renpy.music.set_volume(0.0, 1.0, channel='music')
    
    play sound sfx_doorknock2

    "…"

    li "Hanako? Hanako?! Are you alright?"

    li "I thought I heard something… I'm coming in…"
    
    show evh hanako_cowgirl_14
    with dissolve

    "Hanako and I freeze, and we hear Lilly frantically turn the locked door handle."

    "The door rattles for a second, and then stops."
    
    "…"

    "Lilly's voice is gone, and we breathe a sigh of relief."
    
    $ renpy.music.set_volume(1.0, 5.0, channel='music')

    hi "Um, should we keep going?"
    
    show evh hanako_cowgirl_15
    with dissolve

    "Hanako, breathless beyond speech, simply rocks herself forward onto me."

    "We're both so close, and the close call with Lilly has both of our hearts racing."

    "Nervous energy fills us and we both speed up our thrusting."

    "I can hear Hanako trying her hardest not to make a sound, but the wet thwacking of our deed is hard to mask."
    
    show evh hanako_cowgirl_16
    with dissolve

    ha "Hisao… I… I'm…"

    hi "Me too… just a little…"

    "My muscles tense, my hands grab just ever so tighter, and we both move just a little faster…"

    ha "Hisao… I'm…. I'M…"

    hi "Just… j—just…"
    
    show evh hanako_cowgirl_17
    with dissolve

    "Hanako's arms grip me like a bear, and she squeezes me between her legs."

    ha "…Coming!"
    
    show evh hanako_cowgirl_18
    with dissolve

    "Fingernails dig into Hanako's butt, and my back arches into her body as I lose control."

    "I feel the hot mass of semen fill up around me in the condom, a slightly unnerving feeling to say the least."

    "I pull out of Hanako quickly and remove the used rubber, which is now covered in all manner of bodily fluids."

    hi "Ew…"

    return

label en_HT13x:

    scene bg misc_ceiling
    with locationchange

    "Hanako rolls off me, and lies down beside me."

    ha "That was… wow."
    
    stop music fadeout 3.0

    hi "Yeah but… I think I need to wash up."
    
    scene bg school_dormbathroom at bgleft
    with locationchange

    "I carry the used condom between two fingers, and open the door to the bathroom."
    
    show lilly basic_listen_close
    with charaenter
    
    play sound sfx_impact
    
    show bg school_dormbathroom
    show lilly basic_pout at centersit
    with vpunch
    
    play music music_running fadein 1.0

    "I step through the door without looking, and almost trip over Lilly."

    hi "LILLY?!"
    
    show lilly basic_surprised at centersit
    with charachange

    li "H—Hisao? W—what are you doing here?"
    
    show lilly basic_surprised
    with ease

    "Lilly tries to stand up rapidly, and almost falls over in the process."

    #Lilly Surprised

    "Instinctively I reach out to help her, but pull back at the last second."

    "It's hard enough to explain this as is; let alone if I were to cover her in Hanako's and my juices."
    
    show lilly basic_emb
    with charachange

    "She quickly rights herself, but she can't hide the embarrassment that is written across her face."

    hi "Are you alright?"
    
    show lilly basic_concerned
    with charachange

    li "I… heard some strange noises, and I thought that Hanako might be in trouble."
    
    show lilly basic_listen
    with charachange

    li "She had a difficult night last night and so I felt obliged to check on her."

    li "And I hadn't seen her all so perhaps something was amiss."
    
    show lilly basic_emb
    with charachange
    
    li "The front door was locked so I tried to make an entry through the bathroom… "
        
    extend "butnowIrealisethereisnoproblemgoodnight."
    
    stop music fadeout 4.0
    
    hide lilly
    with charaexit

    "Lilly, too embarrassed to stay in our company, bows quickly and then retreats back to her room through the bathroom."
    
    play ambient sfx_shower fadein 1.0
    
    show steam 
    show steam2
    with dissolve

    "In order to prevent further mishaps, I flush the condom and start the shower."

    "I rinse myself of the sweat, and then change places with Hanako, who does the same."
    
    stop ambient fadeout 1.0

    "We dry ourselves in silence."
    
    scene bg school_dormhanako
    with locationchange

    "Hanako changes into her pyjamas, and I redress."
    
    show hanagown normal
    with charaenter
    #Hanako pjs embarrassed looking down.

    "For what feels like an hour, we just look at each other sheepishly."
    
    show hanagown distant_blush
    with charachange

    "A number of times, one of us goes to speak, but no words come out."

    "Both of us are too embarrassed to move, so we just sit uncomfortably."
    
    play sound sfx_doorknock2
    
    show bg school_dormhanako at bgright
    show hanagown normal_blush at tworight
    with dissolvecharamove

    "Eventually, there is a small knock on the door, followed by a whisper."

    li "Um, Hisao, Hanako? I have made some tea, would you like to join me?"

    "As if commanded by Lilly's words, Hanako and I sheepishly get up and open the door."
    
    play sound sfx_dooropen
    
    scene bg school_girlsdormhall
    show lilly basic_concerned at twoleft
    show hanagown worry at tworight
    with locationskip
    #bg dormhall
    
    play music music_comfort fadein 1.0

    hi "Lilly… I'm sorry…"

    ha "It won't happen again."
    
    show lilly basic_smile at twoleft
    with charachange
    #Lilly Smile

    li "I should be the one to apologise, I was the one invading your privacy…"

    hi "But we…"
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "You were doing what lovers do."
    
    show lilly basic_oops at twoleft
    with charachange

    li "Though, after a close call like last night, is this really wise?"
    
    show hanagown normal at tworight
    with charachange

    ha "But the nurse said…"
    
    show lilly basic_pout at twoleft
    with charachange
    #Lilly surprised

    li "You asked the nurse if it was okay?"

    hi "Well, not really, but I think he knew…"
    
    show lilly basic_emb at twoleft
    with charachange
    #Lilly blush

    li "So last night too?"
    
    show hanagown distant_blush at tworight
    with charachange

    ha "I'm sorry I didn't tell you…"

    li "I suspected that fainting was too much of a reaction to a long walk…"
    
    show lilly basic_weaksmile at twoleft
    with charachange
    #lilly smile

    "Lilly shakes her head, as if trying to get herself back on track."

    li "Come now, the tea is getting cold."
    
    scene bg school_dormlilly
    show lilly basic_smile at twoleftsit
    show hanagown distant at tworightsit
    with locationskip
    #bg dormlilly

    "The three of us sit around Lilly's small table, sipping our tea in an uncomfortable silence."

    "Hanako and I are still wearing embarrassed faces, but Lilly seems almost pleased at the situation."
    
    show lilly basic_planned at twoleftsit
    with charachange

    li "I guess I was wrong about you two, though."
    
    show hanagown normal at tworightsit
    with charachange

    hi "Eh? What do you mean?"
    
    show lilly basic_smileclosed at twoleftsit
    with charachange
    #Lol convenient plot-tie up phase GET. And you thought this was just porn.

    "Lilly's smile widens a little, like someone remembering their childhood."

    li "When you and Hanako first met, I thought that it was a good chance to help her make something more than a friend."
    
    show lilly basic_listen at twoleftsit
    with charachange

    li "But after the festival and that picnic, I thought that she wasn't interested in you in that kind of way."
    
    show lilly basic_smile at twoleftsit
    with charachange

    li "So I just let things be. Forcing these issues never really works."

    hi "I don't get what you mean…"
    
    show hanagown worry at tworightsit
    with charachange

    ha "You… wanted to set us up?"
    
    show lilly basic_weaksmile at twoleftsit
    with charachange

    li "Well, nothing so blatant. I merely wanted to push you two together."

    li "It seems that I didn't have to do anything."

    hi "But, I think you did, in a way."

    hi "If you didn't get sick, I don't think Hanako and I would have ended up together."
    
    show hanagown smile at tworightsit
    with charachange

    ha "I don't think so either."

    hi "And you're still our friend… so long as you're okay with that."
    
    show lilly basic_ara at twoleftsit
    with charachange
    #Lilly insulted? Or happy

    li "My my, of course I am. I'm overjoyed to see Hanako happy."
    
    show lilly basic_weaksmile at twoleftsit
    with charachange
    
    li "She's had a rough time. When she first arrived, I thought she would never open up to anyone."

    li "It took her about two months before she would even talk to me."

    hi "Really? But you're like best friends…"
    
    show hanagown normal at tworightsit
    with charachange

    ha "Lilly was always nice to me. I was just a little afraid at the beginning."

    hi "I guess it is hard to move into a new school, especially one like this."

    hi "I still can't believe that I met everyone here so quickly."
    
    show lilly basic_smile at twoleftsit
    with charachange

    li "New places are always a good basis for new friendships."

    li "And it's normal to make a lot of friends in a place like this, where everyone is the same because they are different."

    #too much?

    "I open my mouth to reply, but my words are blocked by a long-reaching yawn."

    hi "Oh… sorry."
    
    show lilly basic_planned at twoleftsit
    show hanagown smile at tworightsit
    with charachange
    #Lilly and Hanko smile

    li "It's quite alright."

    li "I can imagine that you would be exhausted."
    
    show hanagown normal_blush at tworightsit
    with charachange
    #Hanako embarrassed

    hi "Yeah, and I didn't get a bit of study done…"
    
    show lilly basic_oops at twoleftsit
    show hanagown worry_alt at tworightsit
    with charachange
    #Hanako shokku!

    ha "The exams! I forgot!"
    
    show hanagown worry_blush at tworightsit
    with charachange
    #dicking-induced amnesia. Happens all the time.

    "I pat Hanako on the head."

    hi "Tell you what, tomorrow night, we'll study together. Sound good?"
    
    show hanagown smile_blush at tworightsit
    with charachange
    #Hanako embarrassed happy

    ha "O—okay."
    
    show lilly basic_giggle at twoleftsit
    with charachange

    li "My my, this sounds interesting."

    hi "It's not like that, we need to study."

    hi "We're in the same classes, so it makes sense, right?"
    
    show hanagown worry_blush at tworightsit
    with charachange

    ha "Right?"
    
    show lilly basic_oops at twoleftsit
    with charachange

    li "…"

    hi "Honestly! It's not like that…"
    
    show lilly basic_weaksmile at twoleftsit
    with charachange
    #Lilly smile/ fufufu

    li "Very well, I will take your word for it."
    
    show hanagown normal_blush at tworightsit
    with charachange

    li "Now, however, I think you should return to your room before you cause us any more distress."
    
    show lilly basic_smile at twoleftsit
    with charachange

    li "Good night, Hisao."
    
    show hanagown normal_blush at tworight
    with ease
    
    show bg school_dormlilly at bgleft
    show hanagown normal_blush at center
    show lilly basic_smile at leftsit
    with charamove

    "I stand up, and Hanako springs to her feet."
    
    show hanagown smile_blush
    with charachange

    ha "G…goodnight Hisao…"
    
    show hanagown smile_close
    with charachange

    "She leans forward, almost tripping over Lilly's table in the process."

    "She kisses me gently on the cheek, a grin spreading from ear to ear."

    ha "I… I'll see you in class tomorrow."

    hi "'night, Hanako."

    ha "Hisao?"
    
    stop music fadeout 4.0

    hi "Mmm?"

    ha "I love you."

    hi "Love you too, night."
    
    scene black
    with dissolve

    #Fade to black.

    return
