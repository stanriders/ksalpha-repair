label en_HLT3:
    # > Random crazy idea: Any chance some of these "My my" could become "Oh my"? Some variety couldn't hurt. --Kagami
    
    #Due to rearranging callout scenes from the imachine file, this act is now playable if you select Emi's act two and skip the first scene.
    
    stop music fadeout 1.0
    
    show white
    with locationchange
    

    #show movie

    #play movie "video/note.mpg"
    
    
    centered "A note from the editor" with dissolve
    
    nvl show dissolve
    
    n "Welcome to the Hanalilly-trunk route!"
    
    n "This route was meant to serve as a special Act 2 that shortcuts the player to either Lilly's or Hanako's routes, depending on certain choices made throughout the Act."
    
    n "Originally unlocking this route meant reaching a certain choice in Act 1 that either locked the player into this route, or Kenji's bad end."
    
    n "Ultimately, however, the entire idea was scrapped, and the route was locked out of the game."
    
    n "Until now, that is."
    
    nvl hide dissolve

    nvl clear

    window show
    
    play music music_daily 
   
    scene bg school_gardens2
    with locationchange
        
    "Confused, I make my way through the door that leads to the gardens."

    "The noise of the festival wafts through the trees, louder than before."

    "I guess that most of the crowds come here in the afternoon."
    
    "For a moment, I stand still; the only thing I planned to do today was watch Lilly play."

    "With that goal now complete, I am at a loss as to what to do."

    "Thankfully, my body is more decisive than I am, as my stomach growls in anticipation of lunch."

    scene bg school_courtyard
    with locationchange
    
    show crowd
    play sound "sfx/crowd_outdoors.ogg"
    
    "Following the paved footpath around the Great Hall, I make my way to the festival grounds."

    "It takes me less than five minutes to find myself a noodle stall, owned and operated by the hard-working souls of some second-year class."

    "Within a moment, I am the proud owner of a plate of undercooked noodles."

    "While stuffing my face, I see Shizune wavering within the crowd."

    show shizu cross_angry at twoleft
    show misha hips_grin at tworight
    with charaenter

    "Misha is a step behind Shizune, grinning madly and waving a stick of pink candy floss around in the air like a drunken fool."

    "I try to call out, but my mouth is still full of food."

    hi "Fizube! Mmifa!"

    "Of course, Shizune's pace doesn't falter, but Misha looks up."

    "I guess her interpretation skills also include “full mouth.”"

    "She pauses for a moment, before pulling the cheek below her left eye down and sticking her tongue out."

    "In an instant, she rejoins her partner and they're lost in the crowd once again."
    
    play sound "sfx/crowd_outdoors.ogg"

    hide misha
    hide shizu
    with charaexit

    "She can be such a child sometimes."

    "Ah well. I wouldn't have her any other way; last week showed me just how much work that council can be. For her to be in such high spirits is comforting."

    "I have better things to do with my time."

    "…"

    "I'm a terrible liar."
    
    play sound "sfx/crowd_outdoors.ogg"
    
    "I wander listlessly around the stalls, but I can't seem to get into the festival feel."
    
    "The stalls littered around the school are plain boring."
    
    "I dispose of my now-empty plate and head back to my dorm."
    
    "Maybe I can kill my mind with a light novel or somethng."
    
    "Something festive, to get me in the mood."
    
    stop sound
    
    #I'm still not sure about BG cues and such, so I'll just put mine in comments
    
    #scene bg dormroom
    #with fade
    
    hide crowd
    
    scene bg school_dormhisao_ss
    with shorttimeskip
    
    stop music fadeout 0.5
    
    "Before I even realize it, the sun is scraping the tops of the trees outside my window."
    
    "Seven-thirty. It gets dark late up here."
    
    "I need to learn how to keep track of time."
    
    "Well, at least I can be early for the girls."
    
    "I replace my book on the bookshelf and head out for the girls' dorm."

    scene bg school_girlsdormhall
    with locationskip
    
    play sound "sfx/doorknock2.ogg"
    
    "I rap gently on the Lilly's door and, honestly, my heart is racing."
    
    "An invitation like this is something to treasure."

    li "Just a moment…"

    "Lilly's voice lilts through the door; gentle and silky, but with a touch of playfulness. I hear an almost inaudible voice come soon after."

    ha "Is that… Hisao?"

    li "Indeed, Hanako. It appears as if our guest has arrived."

    "The door makes a clicking sound and opens a fraction."
    
    play sound "sfx/dooropen.ogg"
    
    show lilly basic_smile_paj
    with charaenter

    "As the door opens, she gives a graceful curtsy."

    li "Please come in, Hisao."

    #it would be now that you see the sprites.
    
    play music "bgm/To_Become_One.ogg"
    
    scene bg school_dormlilly
    with locationchange

    #it would be now that you see the sprites.
    
    #Or, you know, CG. Whatever.

    "Lilly swings the door open, revealing a lavishly decorated room."

    "Pale beige seems to be the order of the day."

    "Everything, from the gossamer-thin curtains to the silk bedspread, are in various colors, ranging from dark brown to burgundy to white."
    # > I swear there should be some commas in here.  --Kagami

    "Everything, that is, except the two figures before me."
    
    scene ev lilly_bedroom
    with whiteout

    "Immediately in front of me is Lilly, wearing a dark blue, almost black, silken top and pants with white trim."

    "Behind her, adorned in light purple flannel and kneeling beside the low table, is Hanako."

    "Her hands are firmly fixed between her legs, her shoulders forward, and her head down, as if trying to hide herself in her pajamas."

    "Not that that would be too hard; they look to be a good two sizes too large for her."

    "Folds of flannel flow from her frame, making her look like a child playing dress-up in her parents' clothes."

    "She looks up to confirm my identity, and a thin smile creeps across her face."

    "I steal a glance to the side to take note of Lilly."

    "Her pajamas are dark and breezy, and obviously of quality make. Silk, at a guess."

    "Underneath her short-sleeved top is a pair of silken shorts…"

    "…Which reveal her long, pale, shapely legs…"

    "…her thin, yet graceful thighs…"

    "…The gentle taper to her unblemished knees…"

    "…those smooth thighs, extending down to her beautiful ankles and shapely bare feet…"
    
    li "Ah, Hisao?"

    "Her voice brings me out of my fascinated examination of her legs."

    "I'm blushing. I've obviously let her know something's out of place. Even Hanako's noticed my staring…"

    "…But I can't say I regret it. Not in the least."

    hi "Ah, n—nothing. You're both a welcome sight, believe me."

    "I am the luckiest man alive."

    li "Well now, there's no point in you standing in the doorway. Please, take a seat."
    
    scene bg school_dormlilly
    with locationchange
    
    show hanagown normal at tworightsit
    with charaenter

    "I take a step into the room, and Lilly closes the door behind me."

    "As she turns back toward the room, she bumps into me and grasps my arm."
    
    show lilly basic_ara_paj at twoleft
    with charaenter

    li "My my, I'm afraid that this is a small room with the three of us."

    "She says that as if it's a bad thing."

    li "Would you mind helping me take a seat?"

    "Slightly dumbfounded, I guide Lilly to the table, where I see a small tea set resting."
    
    show lilly basic_smile_paj at twoleftsit
    with charamove

    li "Well now, how about some tea? Hanako, could I impose upon you as to pour?"

    ha "S…sure. His…sao… Would…"
    
    show hanagown distant at tworightsit
    with charachange

    ha "…would you…"
    
    show hanagown distant_blush at tworightsit
    with charachange

    ha "…would you like…"

    hi "I'd love some tea. Do you need a hand?"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "N… no I'm fine…"
    
    show hanagown smile at tworightsit
    with charachange

    ha "Thank you…"
    
    show lilly basic_giggle_paj at twoleftsit
    with charachange

    li "Hanako, you are alright?"
    
    show hanagown distant at tworightsit
    with charachange

    ha "N… no. It's just… just…"

    hi "It's just been a tiring day?"
    
    show hanagown smile at tworightsit
    with charachange

    ha "Y… yeah."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    "Despite my current understanding of Hanako, she continues to don her thin smile as she pours the tea."

    "I take up my position at the table, with my back to the door."

    "To my left is the darkly-clad Lilly and to my right sits the violet Hanako."

    "The tea set on the table looks exquisite; as if pure beauty had been frozen in bone-white china."

    "A highly appropriate set for someone as refined as Lilly."

    "There is a slight “tink” as Hanako accidentally clips the teapot on a cup as she is pouring focuses my attention on her."
    
    show hanagown worry at tworightsit
    show lilly basic_displeased_paj at twoleftsit
    with charachange

    "She breathes in sharply; I guess the set is as delicate as it is beautiful."

    "A fitting metaphor for the pair of girls that grace my presence."
    
    show hanagown worry_blush at tworightsit
    with charachange

    "Hanako quivers at her mistake before Lilly gently rests a hand on her wrist."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Hanako, are you okay?"

    # Some lines snipped - Suriko

    "Hanako glances to Lilly's face, a look of slight worry upon it."

    "I guess Hanako isn't usually this skittish, though I can well understand why."
    
    "I'm nervous as all hell, and I'm not even the one trying to hide myself from someone."
    
    show hanagown normal at tworightsit
    with charachange

    "However, Hanako seems to find some confidence in Lilly's words and deftly pours the next two cups."
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "Here you go, Hisao… Lilly."

    "Hanako gently places a cup and saucer in front of me, and then another in front of Lilly. I could get used to service like this."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Thank you, Hanako."

    hi "Yeah, uh, thanks Hanako."

    ha "You're both welcome."

    "Lilly searches gently for her cup, and upon finding it, sips gently."
    
    show lilly basic_ara_paj at twoleftsit
    show hanagown normal_blush at tworightsit
    with charachange

    li "My my, delicious as expected, Hanako."
    
    ha "Thanks."
    
    stop music fadeout 1.0
    
    #SFX Single firework
    
    play sound "sfx/fireworks.ogg"
    
    "As I sip from my cup, a loud thump shakes the room, and I nearly spill my drink."
    
    stop sound 
    
    hi "What the—?!"
    
    show lilly basic_smile_paj at twoleftsit
    with charachange
    
    li "Oh, that's probably the fireworks show."
    
    li "It's one of the largest in this town."
    
    hi "Strange, I never even heard about it."
    
    #sfx fireworks
    
    play sound "sfx/fireworks.ogg"
    
    play music music_dreamy 
    
    "The booming sounds of fireworks continue to grow as bursts of color flash outside the window."
    
    "Judging by the steady stream of bangs and whistles, this is no ordinary school fireworks show."
    
    "Then again, I don't think my present company could or would appreciate fireworks."

    #"That would explain why both of them are here."
    
    #Is that too vauge? Lilly being blind and Hanako being burnt? Do I need to spell it out?
    # > It *would* sound good, but the fire fear isn't exactly obvious to Hisao/the player yet. Plus, the fireworks-->fire connection is reaching a bit.
    # > Nevertheless, went with an edited version of it. Commented out the last line, though; it drives home an already obvious point. --Kagami

    "Lilly raises her voice ever so slightly to be heard above the din."
    
    play sound "sfx/fireworks.ogg"
    
    show lilly basic_satisfied_paj at twoleftsit
    show hanagown normal at tworightsit
    with charachange

    li "So, Hisao, what did you think of the festival?"

    hi "Well… It was a lot busier than I expected. I'm used to school festivals where nobody but the students and their parents show up."

    ha "That's because it's one of the big festivals in town."
    
    show hanagown distant at tworightsit
    with charachange

    ha "Mostly because of the fireworks."
    
    play sound "sfx/fireworks.ogg"

    hi "Well, I think it's good to see everyone working so hard to put on a good show."

    hi "Back at my old school, we all just put on crappy cafes."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "What a shame. There's a certain joy in putting a lot of effort into your work."

    hi "Is that why you play the cello, then?"
    
    show lilly basic_sad_paj at twoleftsit
    with charachange
    show lilly basic_smile_paj at twoleftsit
    with charachange

    "A glimmer of sadness briefly flashes across Lilly's face, but it's gone in an instant."

    #Fireworks SFX out
    
    li "Somewhat, although a measure is out of not wanting to see practice go to waste."

    "Something tells me there's more to this that she's leaving out. I should probably change the topic."

    hi "So… how did you spend your afternoon?"

    ha "We went to the roof."

    hi "The roof?"

    #ha "The roof is on fire."

    # > I'm sorry, I had to do that. --Kagami

    # Ufufu sprite
    
    show lilly basic_giggle_paj at twoleftsit
    with charachange

    li "My my, Hanako means the roof of the main building."

    li "She likes to go up there, to watch the crowds."
    
    show hanagown irritated at tworightsit
    with charachange

    ha "Lilly!"
    
    show lilly basic_ara_paj at twoleftsit
    with charachange

    li "My my, I didn't mean to tease you, Hanako. Perhaps you would be best suited to explain."

    #Hanako Embarrassed
    
    show hanagown normal_blush
    with charachange

    ha "It's just a hobby."
    
    #hi "Oh, you mean the place where I met you, with the crappy fence?"
    
    ha "It has a nice view."
    
    #SFX Pipirupirupiru pi piru pi! (Aka Lilly's phone ring)
    
    show lilly basic_surprised_paj at twoleftsit
    with charachange
    
    play sound "sfx/cellphone.ogg"

    "Hanako is unexpectedtly cut off by the ringing of Lilly's phone."
    
    li "Oh my, excuse me."
    
    li "Would the two of you wait here while I get this…?"
    
    # > I'm suddenly wondering if the way I reworded this takes away from Lilly's intent to hook them up.  --Kagami
    
    "Lilly quietly answers her phone, and, feeling her way around me, makes her way into the hall."
    
    hide lilly 
    with charaexit
    
    "Hanako and I sit in the newly formed silence, nursing our teacups."
    
    hi "So, do you really watch the crowds?"
    
    show hanagown worry at tworightsit
    with vpunch
    
    "Hanako almost chokes on her tea, but saves herself."
    
    #Hanako Panicked
    
    ha "Wha? I… no, it's just… um…"
    
    show hanagown distant_alt at tworightsit
    with charachange
    
    "Just as I think Hanako is about to implode, she closes her eyes, and takes a deep breath."
    
    show hanagown normal at tworightsit
    with charachange
    
    ha "It's nice up there. You can be alone."
    
    hi "Huh, a good hiding place, eh?"
    
    ha "S—something like that."
    
    hi "I wish I knew that earlier."
    
    hi "I could have used it to hide from Shizune…"
    
    show hanagown smile at tworightsit
    with charachange
    
    #Hanako laugh
    
    "Hanako giggles a little, hiding her face as she does so."
    
    "It's a quiet but unassuming laugh, shy and just a little cute."
    
    "I can't help but smile along with her."
    
    ha "They did seem to make you work hard last week…"
    
    hi "You got that right. I've never worked so hard for school before in my life."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charaenter
    
    show hanagown normal at tworightsit
    with charachange
    
    "Lilly returns from the hall, and I help to guide her back to her seat."
    
    li "My apologies, duty called."
    
    hi "Oh, was that something related to the school?"
    
    show lilly basic_listen_paj at twoleftsit
    with charachange
    
    li "No, I fear it was my cello tutor."
    
    li "She had to cancel my next lesson."
    
    "Part of me is surprised that Lilly takes lessons."
    
    "But then again, even pro athletes have a coach. I guess there's always something you can learn."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange
    
    li "However, I do now have next weekend free."
    
    li "Hisao, would you perhaps like to accompany Hanako and I?"
    
    li "It could be a good chance to become familiar with the town."
    
    hi "Sounds good to me, did you have any ideas?"
    
    show hanagown smile_blush at tworightsit
    with charachange
    
    "Hanako's eyes light up under her fringe."
    
    ha "We… we could go on a picnic…"
    
    show lilly basic_satisfied_paj at twoleftsit
    with charachange
    
    li "What a wonderful idea. What do you think, Hisao?"
    
    hi "I couldn't think of anything I'd like more."
    
    show lilly basic_ara_paj at twoleftsit
    show hanagown smile at tworightsit
    with charachange
    
    li "Well then, it's settled."
    
    li "Hanako and I will prepare some snacks, so you shouldn't need to worry about food."
    
    hi "Awesome. I'm liking the sound of this more and more…"
    
    stop music fadeout 5.0
    
    "I finish my sentence with a drawn-out yawn."
    
    hi "Oh, excuse me…"
    
    show lilly basic_weaksmile_paj at twoleftsit
    show hanagown normal at tworightsit
    with charachange
    
    li "It's quite alright, though I believe we should start making plans for bed."

    hi "Sorry. I guess I'm just a little tired from this week."

    ha "I think we're all a little tired…"

    hi "Yeah… I should go."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Thank you for coming here tonight, Hisao."
    
    #"Thank you for your presence"? Was that intentional wording on her part, or...? 

    hi "Thank you for inviting me… For tonight and next weekend, too, that is."
    
    hi "But for now, I think I'll get out of your hair."
    
    show hanagown normal_blush at tworight
    with charamove
    
    "I stand up and make for the door, Hanako gingerly standing up behind me as I do so."

    "A tad puzzled, I stop and face her."

    hi "Are you coming with me?"
    
    play music "bgm/Generic_Happy.ogg"
    
    show hanagown worry_blush at tworight
    with charamove

    "Hanako instantly blossoms into a vivid, scarlet blush."

    ha "No! I… not… this room… isn't…"

    # Ufufu sprite
    
    show lilly basic_giggle_paj at twoleftsit
    with charachange

    li "My my, you're so bold, Hisao."

    hi "It's okay, I was only joking."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    "That said, all I seem to have done is embarrassed her."

    "I feel kinda terrible, but the face she's making right now is adorable."
    
    "She's hiding the burnt side of her face, and peering at me over her cupped hands."
    
    show hanagown distant at tworight
    with charachange
    
    "But as soon as she catches me looking at her, she glances away."
    
    "She's such a kid…"

    ha "Oh… okay… g'night…"

    li "Goodnight Hanako, Hisao."

    hi "Night all."

    "And with that, our tea party ends."

    scene bg school_girlsdormhall
    with locationchange

    "As soon as Hanako and I are out of Lilly's door, she makes a bolt for the next room."
    
    play sound "sfx/doorclose.ogg"

    "She shuts the door behind her, and I see her name on the nameplate."

    "I guess that explains a lot."

    "I start to walk back to my dorm, but the simple act of walking seems to drain me of my energy."
    
    stop music fadeout 1.0
    
    scene bg school_dormhisao_ni
    with shorttimeskip

    "A wave of exhaustion hits me as I enter my room, the day's events taking their toll."

    "I kick off my shoes and all but fall onto the bed, falling asleep by the time my head hits the pillow."

    scene black
    with dissolve

    return

label en_HLT4:

    #Yeah, since this is a pretty big change I'm just going to repost it.
    #I think I've got all the calls/tags right, but it's probably worth checking them

    #Also, there is a 6-day gap between the last scene and this one. I've done this for 2
    #reasons.
    #First, it allows us to put in an interstitial if we need it, or we can put one of the
    #"common" scenes here.
    
    # > What's that second reason? --Kagami

    #Scene starts as a fade from dark
    #We have BGs to match this now, so this is no longer a need
    
    scene bg school_dormext_full
    with None
    
    play music music_soothing 

    "As I stand outside the Girl's dorm, I realize that this is the first actual weekend I've had since coming to Yamaku."

    "And, compared to the hectic festival week, the school is comparatively tranquil."

    "I've been so bored after classes each day that I regularly find myself just flicking through the small collection of books I brought with me."

    "But now, salvation is at hand."

    "Although I'd never admit it to anyone, I've been looking forward to this outing all week."

    "I mean, what type of guy gets excited over a picnic?"

    "The door before me creaks open, and Hanako and Lilly emerge from the dorm."

    #Maintaining the outfits from the SVN scene, but they can change.
    
    show lilly cane_smileclosed_cas at twoleft
    show hanako emb_timid_sun at tworight
    with charaenter

    "Lilly wears a skirt that reaches well past her knees in addition to a light shirt, obviously of quality make."

    "Even though it is technically less revealing than the school's uniform, the cut of the shirt and the length of the dress are nothing short of alluring."

    "Hanako, however, is garbed in a long, pale yellow dress."

    "As with her uniform, the dress looks to be a few sizes too large for her, covering her entirely."

    "She holds a small picnic basket in front of her with both hands, forming a barrier between herself and the outside world."

    hi "Good morning, Lilly, Hanako."
    
    show lilly cane_smile_cas at twoleft
    with charachange

    li "Oh, you're here already Hisao? How are you?"

    hi "Couldn't be better. What about you guys?"

    li "I am refreshed, and looking forward to today."

    hi "Good to hear. How about you, Hanako?"
    
    show hanako emb_shock_sun at tworight
    with charachange

    "Hanako jumps a little as I turn towards her, hoisting the basket ever so slightly towards her chest."

    #Hanako looking down/away
    
    show hanako emb_downtimid_sun at tworight
    with charachange

    ha "Um... good, thanks."

    hi "Well then, should we make a move?"

    li "Ah yes, let's."

    hi "Well, I only really have one question; where are we headed?"
    
    show lilly cane_planned_cas at twoleft
    with charachange

    li "There is a little park not far from here. It's a bit out of the way, but that also means that it is usually unoccupied."

    hi "Great. How do we get there?"

    li "It's only a short walk."

    #Bg change to empty street w/ fade
    
    scene bg school_road
    with shorttimeskip
    
    show lilly cane_listen_cas at twoleft
    show hanako emb_emb_sun at tworight
    with charaenter

    "Lilly's short walk could be better described as a trek."

    "Sweat beads on my brow as we walk down street after street."

    hi "How much further is this park?"
    
    show lilly cane_surprised_cas at twoleft
    with charachange

    li "Ah, I'm not entirely sure. Which street are we on?"

    "I glance around, trying to find a street sign."
    
    show hanako emb_timid_sun at tworight
    with charachange

    ha "Hiroba Street."
    
    show lilly cane_smile_cas at twoleft
    with charachange

    li "Ah, then it isn't much further. Just another block or two."

    "We continue down the footpath, three abreast, with Lilly leading against all odds."
    
    stop music fadeout 1.0
    
    show hanako emb_downsad_sun at tworight
    with charachange

    "Without warning, Hanako slows down, holding her picnic basket to her chest and bowing her head."

    hi "Hanako? What's the matter?"

    #hanako cowed
    
    play music music_hanako

    ha "T-they're looking at me..."
    
    show lilly cane_displeased_cas at twoleft
    with charachange

    hi "Whomst'd've?"

    "Hanako doesn't answer, but simply nods her head forwards."

    "On the footpath ahead, I see a man and woman walking towards us, talking to each other."

    "As I watch them, they notice the three of us."

    "They look for a couple of seconds, but as soon as they see Lilly waving her cane, they seem to divert their eyes from us."

    hi "Hanako, they're not looking at you."

    hi "See?"
    
    show hanako emb_sad_sun at tworight
    with charachange

    "Hanako's head raises slightly, her fringe swaying gently."

    "Beneath it, I see her eyes dart to confirm my statement."

    #once again, if I lose the "disability" debate, we can throw in a line here about "OMG
    #BURNS"
    
    show hanako emb_downsad_sun at tworight
    with charachange

    "She sees the couple and lowers her head again."

    ha "They're looking. I can tell."

    hi "No they're not, look…"

    "I look up at the couple again. It's like it pains them to avoid looking at us."
    
    hi "Oh..."
    
    show lilly cane_sad_cas at twoleft
    with charachange

    "Suddenly, I realize Hanako's point."

    "Even without our uniforms, it's pretty obvious that we're from Yamaku."

    "Apart from the school, there are very few houses in this end of the town, and Lilly's cane is a dead giveaway."

    "By deliberately avoiding eye contact, the couple are paying just as much attention to us as if they were staring directly at us."

    "I guess that Hanako has experienced this a lot."

    "Even with the most careful grooming and the loosest-fitting clothes, you can still see some of the grafts on her hands and face."

    "It must be pretty hard to put in all that effort and still have people staring at you."

    "I move alongside Hanako, putting myself between her and them as they pass."
    
    stop music fadeout 5.0

    hi "They're gone now."
    
    show lilly cane_weaksmile_cas at twoleft
    show hanako emb_downtimid_sun at tworight
    with charachange

    ha "T…thanks."

    "Hanako keeps her head down and trails behind Lilly, still afraid to look up."

    "For the time being, I leave her and walk alongside Lilly."
    
    show lilly cane_smile_cas at twoleft
    with charachange

    li "Ah, there you are."

    li "I was about to suggest that perhaps I am not the most qualified to lead this party."

    hi "Why?"

    hi "Oh! Sorry."

    "I was so busy focusing on Hanako that I forgot that Lilly still needed someone to read out the street signs for her."

    li "If I recall correctly, the next road on the right should be Kasaneru Avenue, correct?"

    hi "Um… yeah, that looks like it."
    
    show lilly cane_smileclosed_cas at twoleft
    with charachange

    li "Good. That's our destination."

    #scene change to datin' park.
    
    scene bg suburb_park
    with locationchange
    
    play music "bgm/Daylight.ogg"

    "The park is as abandoned as Lilly made out."

    "It's a patch of grass nestled between an intersection."

    "A small grove of trees sits at one end, but apart from that, there's nothing but grass."
    
    show lilly cane_smile_cas at twoleft
    show hanako emb_downtimid_sun at tworight
    with charaenter

    "We move towards the shade from the trees, and I take the picnic basket from Hanako."

    hi "Here, let me set this up for you."
    
    show hanako emb_timid_sun at tworight 
    with charachange

    "She is initially reluctant to give me the basket, but releases it nonetheless."
    
    show hanako emb_timid_sun at left
    with charamove
    
    show lilly cane_weaksmile_cas at twoleft
    with charachange

    "Immediately she runs to Lilly's side. She's probably still rattled by the incident before."

    "I open the basket to find a striped blanket, which I spread out in the shade."

    hi "Would you two like to sit whilst I get this ready?"

    li "Please. The walk was a little longer than I remembered."

    "Hanako nods, and guides Lilly to the blanket."
    
    show lilly basic_smileclosed_cas at twoleftsit
    with charamove
    
    show hanako emb_timid_sun at tworight
    with charachange
    
    show hanako emb_timid_sun at tworightsit
    with charamove

    "After making sure that Lilly is alright, Hanako sits between the two of us."

    ha "H…here. Let me help…"

    "Hanako dives into the basket and starts pulling out tiny wrapped packages, which she then arranges in front of us."

    "I peer into the basket, and notice a thermos sitting in the bottom."

    hi "Oh, is that something to drink? I'm parched…"
    
    show lilly basic_smile_cas at twoleftsit
    with charachange

    li "Ah, of course. Hanako, could you please get that?"

    ha "S—sure."
    
    show hanako emb_downsmile_sun
    with charachange

    "Hanako removes the metal cylinder from the basket and hands it to me, then sets three cups from the basket."

    hi "I guess one each then, eh?"

    li "If you could, please."

    "I pour out the three cups of the dark, cool liquid."

    "We all take our glasses and start to drink."

    #I've softened the original "drinking" session, however since it's a recurring theme
    #I think that it should be kept in. Unless, of course, we drop all drinking.
    #But that's a little unrealistic.
    
    #Well, due to popular demand, drinking is now kaput.
    # > The Itis does not work here at all. Maybe play up the sunny weather angle? --Kagami

    "The iced tea goes down like a treat." 

    "For a time, none of us speak; I guess the walk took a lot out of us all."

    li "So, Hisao, how do you like it?"
    
    hi "It's good. What's it called? I'd like to pick some up on the way home."
    
    #Lilly ufufuf maybe?
    
    show lilly basic_planned_cas at twoleftsit
    with charachange
    
    li "That would be difficult, as I made it myself."
    
    hi "Really? I didn't expect that…"

    #Lilly concerned
    
    show lilly basic_concerned_cas at twoleftsit
    with charachange

    li "Ah, are you not enjoying yourself?"

    hi "No, it's not that. Just… there are a lot of unexpected things, really."
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "Um… it's ready now…"

    "Hanako interrupts our conversation and draws our attention to the food set out in front of us."

    hi "Wow, that's a lot… How did it all fit into the basket?"

    ha "P—practice… I guess…"

    hi "Well, it looks great, and I'm starving. Where did you buy this stuff?"

    #Hanako embarrassed
    
    show hanako emb_emb_sun at tworightsit
    with charachange

    ha "Well, um…"
    
    show lilly basic_satisfied_cas at twoleftsit
    with charachange

    li "Hanako prepared most of this last night, knowing that we would be going out."

    hi "You made all of this?"
    
    show hanako emb_smile_sun at tworightsit
    with charachange

    ha "S…sort of… I guess."

    #Fuck sake she's being Nerine. I HATE Nerine
    # > Who? --Kagami
    #Character from "Shuffle!". Basically a walking doormat, she's passive and modest and that basic nice girl shit

    hi "Well then, we'd better not let it go to waste."
    
    with shorttimeskip
    hide hanako
    
    stop music fadeout 2.0
    
    "We all start eating, and before long all that remains is the discarded cellophane."
    
    # > You must build additional food descriptions. --Kagami

    "I refill our cups from the thermos, and find that it is also nearly empty."

    "The combination of the food, the midday sun and the long walk has made me a little drowsy."
    
    show lilly basic_sleepy_cas at twoleftsit
    with charachange
    
    "…And it looks like I'm not the only one."

    "Hanako seems to have already nodded off onto Lilly's lap." #- too bad we don't have sleepy-like sprites for Hanako in her dress, ksdevs. she'll go spriteless
    
    show lilly basic_weaksmile_cas at twoleftsit
    with charachange

    "Lilly takes her cup as I pass it to her, and beckons me with her finger."
    
    show lilly basic_weaksmile_cas_close at twoleftsit
    with charachange

    "I lean closer, and she whispers to me."

    li "Is she asleep?"

    "I glance at Hanako, who does indeed seem to be peacefully dozing away."

    hi "I think so."

    li "Then could I ask you to do me a favor?"

    hi "Of course."

    li "Would you please help me set her down?"

    "It takes me a few seconds to work out what she means."

    "Hanako is leaning pretty heavily against Lilly's lap; and that can't be comfortable."

    hi "Sure."

    "Gently holding onto Hanako's shoulders, I lay her down on the blanket."
    
    show lilly basic_listen_cas at twoleftsit
    with charachange

    "Lilly stretches out her shoulder, rubbing it gently."

    li "Thank you. I didn't want to wake her up."

    hi "That's okay. Should we maybe leave her be for a bit?"

    hi "We wouldn't have to whisper, either."
    
    show lilly basic_smile_cas at twoleftsit
    with charachange

    li "That's a good idea. Could you please help me up?"

    "Lilly holds both of her arms out, the international signal for “Help me up.”"

    #cut the next two lines if you wish. Just moar Lilly fanservice
    
    show lilly basic_smile_cas at twoleft
    with charamove

    "I oblige, and only partly because the way she is holding her arms is creating a tempting gap in her collar."

    "Damn, an undershirt. Ah well, it was worth a try."
    
    show lilly basic_smile_cas at centersit
    with charamove

    "We move to a nearby tree and sit against the trunk."
    
    # > Tree scene could maybe use a bit more detail in its setup. Just another line or two, maybe three?  --Kagami

    "Here, we can keep an eye on the sleeping Hanako without disturbing her."

    #I'm cutting this here for two reasons. Firstly, H5r will have a lot of the stuff from H6,
    #and also Miku just arrived, and it would be rude of me not to play with her.

    #I'd like to say I'm looking for feedback, but I'm really not.
    # > YOU GONNA GET FEEDBACK'D
    
    # > ....well, actually, you already have been. --Kagami

    return

label en_HLT5:
    
    play music music_soothing 

    hi "So, are these trips away from school a typical thing for you two?"
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    li "Well, in a way. I try to take her to places where she doesn't have to worry about others."
    
    li "In that respect, I'm glad that you're here with us."

    hi "Me? Why?"

    li "If I were to put it one way, I'd say that she trusts you."

    hi "I find that a bit hard to swallow."
    
    show lilly basic_giggle_cas at centersit
    with charachange

    "She gives her trademark giggle, her curled finger to her mouth."

    li "Well, Hanako is Hanako. She can be a tad difficult to understand at times."

    "Now that's an understatement."
    
    show lilly basic_smileclosed_cas at centersit
    with charachange

    li "Nevertheless, she's more comfortable around you than most others. You've been wonderful for her."

    "She gives a deep smile, taking me well and truly on the back foot."

    li "Thank you, Hisao."

    hi "Ah, um, y—you're welcome. I think."
    
    show lilly basic_smile_cas at centersit
    with charachange

    "Her smile is so deep and genuine I can't get it out of my head."

    hi "So, er, Lilly… how come you and Hanako are such good friends?"
    
    show lilly basic_surprised_cas at centersit
    with charachange

    "Pausing for a second, Lilly leans back and thinks."
    
    show lilly basic_reminisce_cas at centersit
    with charachange

    li "Hanako first came to this school in a bit of a shell."

    li "She wouldn't talk to anyone, including myself, even though I lived next door to her."

    li "Each morning I would try to make conversation as she got up, but she always hurried past me."

    hi "So… what changed all that?"
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    "She lets out a deep breath, rubbing her chin in thought."

    li "Hmmm… I guess it was something that happened during the third week that she was here."

    li "One of the girls in a dormitory room near mine had just been dumped. It had been nothing but a fledgling's romance, yet she was in tears."
    # > "a fledgling's romance"     a what? --Kagami

    li "In the end, the girl came to my room. Being the class president and an acquaintance of hers, she decided that she could confide in me."

    li "I made her some tea, and after she told me her stories of woe, she felt a little better."

    li "As she left, I sensed someone standing at my door, silently."
    # > ...Wait, what?  She heard them standing?

    li "It turns out that Hanako had heard most of the affair through her walls, and she wanted to see if I could help her."

    li "It seems that it wasn't until then that she realized I was blind… that seemed to relax her a lot."

    li "Until then, she was frighteningly scared of anyone and everyone."

    li "My blindness though, allowed her to relax just enough for her to open up to me."

    li "Since then, we've developed a mutual friendship for one another."

    "She pauses a moment, looking to Hanako."
    
    show lilly basic_sad_cas at centersit
    with charachange

    "Her expression changes to one of slight regret."

    li "Unfortunately, I'm the only one she's ever developed a friendship with."

    li "I feel as if I've failed her."

    hi "Failed her?"

    li "I've tried to make her more comfortable around others. I never managed though, despite my best efforts."

    li "She's kind and definitely has it in her, but I feel as if she's deliberately bottling herself up."

    hi "I see."
    
    show lilly basic_listen_cas at centersit
    with charachange

    "Silence."

    "As it passes, I realize a notable absence:"

    "Specifically, her own part in their relationship."

    "She cares so deeply for Hanako, but what of herself?"
    
    show lilly basic_sleepy_cas at centersit
    with charachange

    "Before I can pursue this matter with Lilly, she lets out a yawn."
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    li "Oh my, excuse me."

    li "I'm just feeling sleepy all of a sudden."
    
    li "Days like this are quite nice, after all."

    #"I can see that Lilly is gently trying to change the topic, so I decide to leave my questioning at that."

    return

label en_choiceHLT5:

    #Choice:
    #1 – Stay with Lilly
    #2 – check on Hanako

    menu:
        with menueffect
        
        "I can see that Lilly is gently trying to change the topic, so I decide to leave my questioning at that."

        "Stay with Lilly.":
            return m1
        
        "Check on Hanako.":
            return m2

label en_HLT5a:

    #1 – Staying with Lilly
    #+1 lilly
    
    # > I thought we weren't using points anymore. Or is that just A1F?   --Kagami
    
    stop music fadeout 1.0
    
    "I can see that Lilly is gently trying to change the topic, so I decide to leave my questioning at that."

    hi "You're right, days like this are nice."

    hi "You can just do whatever you want, whenever you want."

    hi "It's refreshing, in a way."
    
    show lilly basic_giggle_cas at centersit
    with charachange

    #Lilly Ufufufu

    "Lilly giggles a little, tired."

    li "You know, Hanako said something very similar at roughly this time last year."

    hi "Oh, really? What did she say?"
    
    show lilly basic_smileclosed_cas at centersit
    with charachange

    li "Well, we were spending some time in my summer house, and she noted that she liked having the time to herself."

    hi "Summer house?"
    
    show lilly basic_smile_cas at centersit
    with charachange

    li "My family owns a summer house somewhat north of here. I've only been to it a few times, though."

    li "Hanako and I have gone there for the summer break these last two years."

    li "That being said, I would like to go there during winter, even just once. The snow is said to be wonderful near there."

    hi "You like snow?"
    
    show lilly basic_planned_cas at centersit
    with charachange

    li "Mm, it's wonderful."

    "I guess it has a… unique texture."

    "To be honest, it's kind of hard to see what would be so appealing about snow to someone that couldn't see it."

    hi "To be able to own a summer house… how do you have so much money? Housing's horribly expensive nowadays."
    
    show lilly basic_listen_cas at centersit
    with charachange

    li "Ah. …Are you perhaps aware of a company known as Tachibana Enterprises?"

    hi "Tachibana Enterprises… Yeah, I think I've heard of that, somewhere."

    hi "Oh, right! They found some big new diamond deposit in South Africa. It was all over the news for a few days."

    li "Yes, the very same."

    li "…My father is one of the executive board members."
    
    play music music_night

    "My jaw drops open."

    "A board member? Of a diamond mining company?"

    "Even if they're only breaking out into the field, it more than explains how she can afford such things."

    hi "That's… amazing."
    
    show lilly basic_concerned_cas at centersit
    with charachange

    "As I turn to her, I realize I might have touched on an awkward subject for her."

    li "It's… not really that big of a thing…"

    "Seemingly realizing the implications of what she just said, she quickly tries to reassure me."

    li "Ah, sorry. It's just a little… an odd situation. That is the reason for my affluence, in any case."

    hi "I… see."

    "The move doesn't really take away the guilt at my painfully spurious reaction."

    "In any case, it would seem expedient to change the topic."
    
    # > I'm trying to figure out what he's supposed to be feeling guilty about, and I just can't.

    hi "Sorry, I'm just feeling kind of tired."

    "With wonderful timing, I summon a deep yawn as if to accentuate the point."
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    li "I have to admit that I am, too. Shall we take a nap?"

    hi "You can, if you'd like."
    
    hide lilly
    with charaexit

    "Lilly slides down the trunk of the tree until she lays flat on the grass."

    #"As I follow her lead, laying in the shade of the tree as well, it doesn't take long for sleep to overcome me."

    #"Moments before I shut my heavy eyes, I can just remember one thought."

    #hi "It'd be nice to see the summerhouse."

    #li "…It would."

    #End Part 1

    return

label en_HLT5b:

    #2 – Check on Hanako
    #+ 1 Hanako

    hi "I'm going to go check on Hanako."

    li "Ah, good idea."

    #li "But in that case, would you be offended if I took a nap?"

    #hi "Not at all. Please do."

    #li "Thank you."

    #"Lilly slides down the trunk of the tree until she lays flat on the grass."

    "As I flick my eyes back to the sleeping figure of Hanako, I think on Lilly's words."

    "Until now, I'd only seen her scars as physical."

    "I guess they're psychological, as well."

    "And, after what I saw this morning, I can believe that."

    "To know that every single person you meet will be judging you based on your face alone must be pretty taxing."

    "I don't know if I would be able to handle that kind of pressure."

    "Feeling drawn towards the sleeping figure, I stand up and take a few tentative steps towards her."

    "Big mistake."

    "I've been sitting in the shade for far too long, especially after the long walk."

    "By standing up too quickly, I've given myself a headspin."

    "The dizziness forces me to sit back down."

    "I close my eyes for a second to regain my senses…"
    
    stop music fadeout 2.5
    
    scene black
    with shuteye

    #End splits

    return

label en_HLT5x:
    
    scene bg suburb_park
    with openeye

    "A faint breeze rouses me from my slumber."

    "I rub the sleep from my eyes and take a look around."
    
    play music music_tranquil

    "The sky has turned from the deep blue of the day to the yellow-blue of late afternoon."

    "I guess we've been out for a while."
    
    show hanako emb_downtimid_sun at tworightsit
    with charaenter

    "Lilly still sleeps against her tree, but Hanako appears to be wide awake, sitting about a foot from Lilly and I, hugging her knees."

    hi "Oh, hey Hanako. Have you been there long?"
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "N…not really."

    ha "I… I only just woke up."

    "She shuffles a little, and I see the picnic basket behind her, packed and ready for the trip home."

    "Who knows how long she's just been sitting there, waiting for us to wake up, but not wanting to disturb us."

    hi "Well then, should I wake Lilly?"
    
    show hanako emb_downsad_sun at tworightsit
    with charachange

    ha "Um… I don't… um…"

    hi "It's okay. Lilly would think it pretty rude to stay asleep whilst we waited for her, don't you think?"

    "Hanako seems to think about this for a moment."
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "O…okay."
    
    #I'm going to keep the "falling" bit 'cause I think that it's fun. And it might be moe. I don't know, obviously.
    
    show hanako emb_timid_sun at centersit
    with charamove

    "She leans forward with the intention of waking up Lilly…"
    
    show hanako emb_strain_sun at centersit
    with charachange

    "…gets caught on her dress…"

    "…and falls onto Lilly."
    
    show hanako emb_shock_sun at centersit
    show lilly basic_surprised_cas at twoleftsit
    with vpunch

    "Lilly wakes with a start, her arms flailing about, trying to work out what happened."
    
    show hanako emb_downsad_sun at centersit
    with charachange

    ha "I'm sorry Lilly! I'm sorry I'm sorry!"

    ha "I just… fell a little…"
    
    show lilly basic_weaksmile_cas at twoleftsit
    with charachange

    "Lilly collects herself pretty quickly, considering her rude awakening."

    li "My my, that's alright Hanako."

    li "Accidents like this happen."
    
    show lilly basic_weaksmile_cas at twoleft
    with charamove

    "Holding her head, Lilly stands up."
    
    show hanako emb_downtimid_sun at center
    with charamove

    "Hanako collects the basket, and stands up with her."

    hi "I suppose it's time to head home then, eh?"

    li "Yes, I think I would like to bathe and spend some time in my own bed."
    
    show lilly basic_displeased_cas at twoleft
    with charachange

    li "I can't say that sleeping on the ground is very comfortable…"

    "Lilly starts to sway mid-sentence, and I grab her shoulder to right her."
    
    show lilly basic_weaksmile_cas at twoleft
    with charachange

    li "Oh, thank you, Hisao."
    
    show lilly basic_sleepy_cas at twoleft
    with charachange

    li "I felt a little light-headed there."

    hi "I know how you feel."

    li "I'm not sure about you, but I don't fancy walking home."

    hi "Then how are we going to get back to school?"

    #Lilly disappointed/deep thought/something like that
    
    show lilly basic_listen_cas at twoleft
    with charachange

    li "Well, this location was my choice, so I will shoulder that responsibility."

    "Before I can protest, Lilly has started dialing a number on her phone."

    "As she taps away on the keyboard, I notice that each of the buttons has a raised ridge."

    "That explains how she can be so quick to dial numbers I suppose."

    li "Hello? Could I please book a taxi for a pick-up at the Kasaneru park? Thank you."
    
    scene bg school_road_ss
    with locationskip

    "Surprisingly, the taxi arrives not too long after."

    "We all clamor into the back seat, Hanako sitting between Lilly and myself."

    li "Yamaku Academy, please."

    "Taxi Driver" "Sure."

    "Our hour-long walk this morning is decimated by the taxi in a matter of minutes, and in what feels like no time at all, we are standing outside the girl's dorm."
    
    scene bg school_dormext_full_ss
    with shorttimeskip

    #BG change to dorms
    
    show lilly basic_smile_cas at twoleft
    show hanako emb_smile_sun at tworight
    with charaenter

    hi "Well, I have to thank both of you."

    hi "I had a good time."

    li "You're welcome."

    hi "Thanks for lunch, Hanako."

    "Hanako blushes slightly before answering."
    
    show lilly basic_planned_cas at twoleft
    show hanako emb_emb_sun at tworight
    with charachange

    #Hanako smile/blush

    ha "Y—you're welcome."

    hi "Anyway, I'm beat. Can't wait to get into a bath or something…"

    li "You're quite right there."

    ha "M…me too."

    hi "Well then, I'll see you both in school tomorrow?"

    li "I look forward to it."

    ha "N…good night."

    hi "Night Hanako, Lilly."
    
    hide hanako
    hide lilly
    with charaexit

    "We exchange short nods, and the girls disappear back into their dorm."

    "I breathe a sigh of relief. It wasn't a very intensive outing, but our extended nap in the park has really drained me."

    "It takes a supreme effort to walk the short distance to my room and collapse onto my bed, exhausted."

    #Fade to black.

    #Next scene will probably borrow heavily from the old H7, but with a more obvious
    #pointer as to with path you take. I'll have that, and hopefully H7r done tomorrow.
    return

label en_HLT6:
    
    stop music fadeout 1.0
    
    "I can see that Lilly is gently trying to change the topic, so I decide to leave my questioning at that."

    hi "You're right, days like this are nice."

    hi "You can just do whatever you want, whenever you want."

    hi "It's refreshing, in a way."
    
    show lilly basic_giggle_cas at centersit
    with charachange

    #Lilly Ufufufu

    "Lilly giggles a little, tired."

    li "You know, Hanako said something very similar at roughly this time last year."

    hi "Oh, really? What did she say?"
    
    show lilly basic_smileclosed_cas at centersit
    with charachange

    li "Well, we were spending some time in my summer house, and she noted that she liked having the time to herself."

    hi "Summer house?"
    
    show lilly basic_smile_cas at centersit
    with charachange

    li "My family owns a summer house somewhat north of here. I've only been to it a few times, though."

    li "Hanako and I have gone there for the summer break these last two years."

    li "That being said, I would like to go there during winter, even just once. The snow is said to be wonderful near there."

    hi "You like snow?"
    
    show lilly basic_planned_cas at centersit
    with charachange

    li "Mm, it's wonderful."

    "I guess it has a… unique texture."

    "To be honest, it's kind of hard to see what would be so appealing about snow to someone that couldn't see it."

    hi "To be able to own a summer house… how do you have so much money? Housing's horribly expensive nowadays."
    
    show lilly basic_listen_cas at centersit
    with charachange

    li "Ah. …Are you perhaps aware of a company known as Tachibana Enterprises?"

    hi "Tachibana Enterprises… Yeah, I think I've heard of that, somewhere."

    hi "Oh, right! They found some big new diamond deposit in South Africa. It was all over the news for a few days."

    li "Yes, the very same."

    li "…My father is one of the executive board members."
    
    play music music_night

    "My jaw drops open."

    "A board member? Of a diamond mining company?"

    "Even if they're only breaking out into the field, it more than explains how she can afford such things."

    hi "That's… amazing."
    
    show lilly basic_concerned_cas at centersit
    with charachange

    "As I turn to her, I realize I might have touched on an awkward subject for her."

    li "It's… not really that big of a thing…"

    "Seemingly realizing the implications of what she just said, she quickly tries to reassure me."

    li "Ah, sorry. It's just a little… an odd situation. That is the reason for my affluence, in any case."

    hi "I… see."

    "The move doesn't really take away the guilt at my painfully spurious reaction."

    "In any case, it would seem expedient to change the topic."

    hi "Sorry, I'm just feeling kind of tired."

    "With wonderful timing, I summon a deep yawn as if to accentuate the point."
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    li "I have to admit that I am, too. Shall we take a nap?"

    hi "You can, if you'd like."
    
    hide lilly
    with charaexit

    "Lilly slides down the trunk of the tree until she lays flat on the grass."

    hi "I'm going to go check on Hanako."

    li "Ah, good idea."

    "As I flick my eyes back to the sleeping figure of Hanako, I think on Lilly's words."

    "Until now, I'd only seen her scars as physical."

    "I guess they're psychological, as well."

    "And, after what I saw this morning, I can believe that."

    "To know that every single person you meet will be judging you based on your face alone must be pretty taxing."

    "I don't know if I would be able to handle that kind of pressure."

    "Feeling drawn towards the sleeping figure, I stand up and take a few tentative steps towards her."

    "Big mistake."

    "I've been sitting in the shade for far too long, especially after the long walk."

    "By standing up too quickly, I've given myself a headspin."

    "The dizziness forces me to sit back down."

    "I close my eyes for a second to regain my senses…"
    
    stop music fadeout 1.5
    
    scene black
    with shuteye
    with Pause(1.0)
    
    scene bg suburb_park
    with openeye

    "A faint breeze rouses me from my slumber."

    "I rub the sleep from my eyes and take a look around."
    
    scene bg misc_sky_ss
    with locationchange
    
    play music music_tranquil

    "The sky has turned from the deep blue of the day to the yellow-blue of late afternoon."
    
    scene bg suburb_park
    with locationchange

    "I guess we've been out for a while."
    
    show hanako emb_downtimid_sun at tworightsit
    with charaenter

    "Lilly still sleeps against her tree, but Hanako appears to be wide awake, sitting about a foot from Lilly and I, hugging her knees."

    hi "Oh, hey Hanako. Have you been there long?"
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "N…not really."

    ha "I… I only just woke up."

    "She shuffles a little, and I see the picnic basket behind her, packed and ready for the trip home."

    "Who knows how long she's just been sitting there, waiting for us to wake up, but not wanting to disturb us."

    hi "Well then, should I wake Lilly?"
    
    show hanako emb_downsad_sun at tworightsit
    with charachange

    ha "Um… I don't… um…"

    hi "It's okay. Lilly would think it pretty rude to stay asleep whilst we waited for her, don't you think?"

    "Hanako seems to think about this for a moment."
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "O…okay."
    
    show hanako emb_timid_sun at centersit
    with charamove

    "She leans forward with the intention of waking up Lilly…"
    
    show hanako emb_strain_sun at centersit
    with charachange

    "…gets caught on her dress…"

    "…and falls onto Lilly."
    
    show hanako emb_shock_sun at centersit
    show lilly basic_surprised_cas at twoleftsit
    with vpunch

    "Lilly wakes with a start, her arms flailing about, trying to work out what happened."
    
    show hanako emb_downsad_sun at centersit
    with charachange

    ha "I'm sorry Lilly! I'm sorry I'm sorry!"

    ha "I just… fell a little…"
    
    show lilly basic_weaksmile_cas at twoleftsit
    with charachange

    "Lilly collects herself pretty quickly, considering her rude awakening."

    li "My my, that's alright Hanako."

    li "Accidents like this happen."
    
    show lilly basic_weaksmile_cas at twoleft
    with charamove

    "Holding her head, Lilly stands up."
    
    show hanako emb_downtimid_sun at center
    with charamove

    "Hanako collects the basket, and stands up with her."

    hi "I suppose it's time to head home then, eh?"

    li "Yes, I think I would like to bathe and spend some time in my own bed."
    
    show lilly basic_displeased_cas at twoleft
    with charachange

    li "I can't say that sleeping on the ground is very comfortable…"

    "Lilly starts to sway mid-sentence, and I grab her shoulder to right her."
    
    show lilly basic_weaksmile_cas at twoleft
    with charachange

    li "Oh, thank you, Hisao."
    
    show lilly basic_sleepy_cas at twoleft
    with charachange

    li "I felt a little light-headed there."

    hi "I know how you feel."

    li "I'm not sure about you, but I don't fancy walking home."

    hi "Then how are we going to get back to school?"
    
    show lilly basic_listen_cas at twoleft
    with charachange

    li "Well, this location was my choice, so I will shoulder that responsibility."

    "Before I can protest, Lilly has started dialing a number on her phone."

    "As she taps away on the keyboard, I notice that each of the buttons has a raised ridge."

    "That explains how she can be so quick to dial numbers I suppose."

    li "Hello? Could I please book a taxi for a pick-up at the Kasaneru park? Thank you."
    
    scene bg school_road_ss
    with locationskip

    "Surprisingly, the taxi arrives not too long after."

    "We all clamor into the back seat, Hanako sitting between Lilly and myself."

    li "Yamaku Academy, please."

    "Taxi Driver" "Sure."

    "Our hour-long walk this morning is decimated by the taxi in a matter of minutes, and in what feels like no time at all, we are standing outside the girl's dorm."
    
    scene bg school_dormext_full_ss
    with shorttimeskip
    
    show lilly basic_smile_cas at twoleft
    show hanako emb_smile_sun at tworight
    with charaenter

    hi "Well, I have to thank both of you."

    hi "I had a good time."

    li "You're welcome."

    hi "Thanks for lunch, Hanako."

    "Hanako blushes slightly before answering."
    
    show lilly basic_planned_cas at twoleft
    show hanako emb_emb_sun at tworight
    with charachange

    ha "Y—you're welcome."

    hi "Anyway, I'm beat. Can't wait to get into a bath or something…"

    li "You're quite right there."

    ha "M…me too."

    hi "Well then, I'll see you both in school tomorrow?"

    li "I look forward to it."

    ha "N…good night."

    hi "Night Hanako, Lilly."
    
    hide hanako
    hide lilly
    with charaexit

    "We exchange short nods, and the girls disappear back into their dorm."

    "I breathe a sigh of relief. It wasn't a very intensive outing, but our extended nap in the park has really drained me."
    
    scene bg school_dormhisao_ss
    with locationskip

    "It takes a supreme effort to walk the short distance to my room and collapse onto my bed, exhausted."
    
    stop music fadeout 3.0
    
    scene black
    with shuteye
    with Pause(3.0)
    
    scene bg school_room34
    with dissolve
    
    play music music_gentle
    
    #I've gone back to Playlist naming.
    #BG classroom
    
    "Teacher" "Now, Hisao, can you please translate that last sentence for us?"

    hi "Er… “The teacher received the test from the student?”"

    "I'm almost certain that I can hear snickers from the class."

    "Teacher" "That's not quite correct. The verb here shows that it is the teacher giving the student the test, not the other way around, but you were close."

    "Teacher" "Right then, next up…"

    "I sit down, embarrassed."

    "The weekend with Lilly and Hanako seems to have left me a little behind in my studies."

    "Actually, who am I kidding, I haven't studied English in ages."

    "As soon as it got confusing I just gave up, and did anything within my power to avoid it."

    "Reading, watching TV… so long as there was something even vaguely more interesting, English took a back seat."

    "But now, as the class seems to be taking leaps and bounds ahead of me, I think I have to do something about it."

    "I guess there's no choice but to hit up the library at lunch time…"

    #BG Library
    
    scene bg school_library
    with shorttimeskip

    hi "Er, hey Yuuko."
    
    show yuuko neurotic at twoleft
    with charaenter

    yu "Yes? Hello? Oh, you're Hisao, right? It is Hisao, isn't it?"

    hi "That's the one. Looks like you're not as bad with names as you thought."
    
    show yuuko neutral_down at twoleft
    with charachange

    "Yuuko smiles shyly at my comment; I guess her memory doesn't receive many compliments."

    yu "So, er, what can I do for you today?"

    hi "Actually, this is a bit embarrassing, but I was wondering if you maybe had a study guide for basic English?"
    
    show yuuko neutral at twoleft
    with charachange

    yu "English, eh? Let me see, Basic English… Basic English… a study guide for Basic English…"

    "I guess subtlety is lost on Yuuko. Every “Basic English” feels like a dagger in my back."

    "Though, so long as no-one hears, I'll get away with…"
    
    stop music fadeout 1.5
    
    show lilly cane_surprised at center
    with charaenter

    li "Oh, is someone looking for an English textbook, Yuuko?"

    "Damnit. I didn't even notice Lilly approach the Loans counter."
    
    show yuuko smile at twoleft
    with charachange

    yu "Hey Lilly. I was just looking for a study guide for Hisao."
    
    show lilly cane_smile at center
    with charachange

    li "Oh my, is Hisao here?"

    "No point in hiding it…"
    
    play music "bgm/Another_Day.ogg"

    hi "Yeah, hi Lilly. I didn't see you there."

    li "Good afternoon to you. Are you having trouble with your English?"

    hi "Just a bit. I think I'm falling behind the rest of the class…"
    
    show lilly cane_listen at center
    with charachange

    #Lilly shocked a little?

    li "Oh dear, but I thought you were on top of your studies?"

    hi "In science and maths, yeah, but English just seems to slip away from me."
    
    show yuuko closedhappy_up at twoleft
    with charachange

    yu "Found it! English for Busy People!"

    hi "Really?"

    yu "Yes, it's in Reference, section C."

    hi "Thanks."

    yu "But you know, you should just ask Lilly here to help you."

    hi "Oh, are you good at English, Lilly?"
    
    show yuuko smile at twoleft
    with charachange

    yu "Good? She's the best!"

    "Now that I think about it, Lilly does look like she'd be good at English."

    "I mean, there's not too many other blondes with blue eyes around here…"
    
    show lilly cane_emb at center
    with charachange

    li "Oh, now you're being silly, Yuuko."

    yu "You're just being modest."

    yu "You should see her, Hisao. Half of her books are in English."

    yu "I mean Braille."
    
    show yuuko worried at twoleft
    with charachange

    #Yuuko confused

    yu "I mean English Braille."

    hi "I think I get the point."
    
    show lilly cane_weaksmile at center
    with charachange

    li "Well, it isn't as grand as Yuuko makes out, but if you are falling behind, then perhaps I could tutor you after school?"

    hi "Could you? I mean, if it's no trouble, I kinda need the help..."
    
    show lilly cane_smile at center
    with charachange

    #Lilly smile

    li "I'm not sure how skilful I am as a teacher, but I will certainly try to assist."
    
    show yuuko smile_up at twoleft
    with charachange

    yu "You should do it here. It's pretty quiet most of the time, and I'll see if I can find a text that has a Braille version as well."

    hi "You can do that?"

    #Yuuko Smile
    
    show yuuko neutral at twoleft
    with charachange

    yu "You bet. A lot of the texts here are printed in different forms; Braille, Large font…"

    yu "You name it, I'll find it."

    li "Yuuko quite often helps me find books in Braille. The collection here is quite large, as you may imagine."

    hi "That's… kinda cool, really."

    "And I just thought Yuuko was a klutz…"

    hi "So, you can read Braille, Yuuko?"

    yu "No.. I just read the titles on the covers."

    hi "Oh, that's cool I guess."
    
    play sound "sfx/chaimu.ogg"

    #SFX Bells
    #Ah, bells. Classic "I can't think of how to continue this" style.
    
    show lilly cane_surprised at center
    with charachange

    li "Oh, is that the time? I'm afraid we must be off."

    li "Hisao, should we meet here after classes this afternoon?"

    hi "So soon?"

    li "Unless you have some reason to postpone it?"

    "A wave of excuses crashes around my head, but that is exactly the attitude that got me into this mess."

    hi "Sounds good to me. I'll see you after class."
    
    show yuuko neutral_down at twoleft
    with charachange

    yu "I'll have your books here by then, so be sure to stop by."

    li "Of course we will, Yuuko. Thank you, as always."

    hi "Yeah, thanks Yuuko."

    "As Yuuko smiles at us, I get the feeling that she enjoys being helpful, even if it only involves something as trivial as finding some books."

    yu "I'll see you both later!"
    
    stop music fadeout 2.5
    
    scene bg school_scienceroom
    with locationskip
    with Pause(1.5)
    
    scene bg school_scienceroom
    with shorttimeskip

    #BG Classroom

    "As the day draws to a close, I start packing up my things in anticipation of meeting Lilly."

    "After all, it'd be rude to make her wait, especially as she's the one helping me out."

    #SFX Bell ring
    
    play sound "sfx/chaimu.ogg"
    
    play music music_tranquil fadein 1.0

    "By the time the bell rings, my bag is practically packed."

    "A deft flick of the wrist sends the last remaining textbook into the awaiting bag, and I am off."

    "Even with all of my preparation, the front door is clogged with students."

    "However, the back door looks almost clear."

    "I turn on my heels and head for the back of the class."

    #Show Hanako
    
    show hanako def_worry at centersit
    with charaenter

    "As I pass Hanako's desk, I notice that she hasn't moved, at all."

    "Her pencil is still firmly in her hand, and her focus is firmly on the textbook in front of her."

    "Fierce concentration strains at her face, but her pencil doesn't move."

    "My momentum is broken."

    hi "Hey, are you having trouble with that?"

    #Hanako embarrassed
    
    show hanako defarms_shock at centersit
    with vpunch

    ha "H—H—Hisao!"
    
    show hanako cover_distant at centersit
    with charachange

    ha "I… I didn't see you there…"

    hi "That's okay, I guess I kinda snuck up on you."

    hi "Do you need a hand?"

    #Hanako looking away
    
    show hanako emb_downtimid at centersit
    with charachange

    ha "Um…"

    "Mental note: Don't surprise Hanako."

    ha "J—just a little."

    "Damnit. I guess there goes being early for Lilly."

    "Still, I can answer one question and still be on time."

    hi "Which one are you working on?"

    ha "T—This one."

    hi "Let's have a look then…"

    "I look over Hanako's work. Small, neatly-printed characters fill her page, but it only takes me a moment to find her error."

    hi "Ah, right here. You see, that's supposed to be an x squared there, not just an x."
    
    show hanako basic_distant at centersit
    with charachange

    ha "O…oh. I see now. So…"

    "Hanako leans back over her book, makes a few adjustments, and quickly works out the answer."

    hi "That's it, you've got it there."

    ha "T—thanks."

    "A quick assessment of the classroom revels that we are now alone, and I am now late for Lilly."

    $doublespeak(hi,ha,"Um, Hanako…","Um, Hisao…?")

    hi "Oh, my bad. You first, Hanako."

    #ha "D…do you mind if I ask one more?"

    #The choice below is conditional, depending on the attraction points.
    # if(H>(L+2)), then H-path without the choice
    #else if(L>(H+2)), then L-path without the choice
    #else see the choice.

    #If you don't see the choice, then you basically just see what would happen as if you chose that particular line.

    #Choice:
    #1 – Sorry, but I've got to meet with Lilly…
    #2 – Sure (I'm late already)

    #1 feeds into the L path, 2 into the H path.


    #is all of that possible?

    return

label en_choiceHLT6:
    
    
    #Choice:
    #1 – Sorry, but I've got to meet with Lilly…
    #2 – Sure (I'm late already)

    #1 feeds into the L path, 2 into the H path.
    
    menu:
        with menueffect
        
        ha "D…do you mind if I ask one more?"

        "Sorry, but I've got to meet with Lilly…":
            return m1
        
        "Sure (I'm late already).":
            return m2

label en_HLT6a: #Everything after "Sorry, but I've got to meet with Lilly." has been added by memerantoinette to make things flow smoothly
    
    hi "Sorry, but I've got to meet with Lilly."
    
    show hanako emb_timid at centersit
    with charachange
    
    ha "O-oh... okay. I'll s-see you tomorrow, then..."
    
    hi "Alright. Goodbye, Hanako."
    
    show hanako cover_smile at centersit
    with charachange
    
    ha "G-Goodbye... Hisao."
    
    scene bg school_hallway3
    with locationchange
    
    "With that, I head to the library to study with Lilly."
    
    "For whatever reason, that night I spent with Lilly and Hanako watching the fireworks won't leave my mind."
    
    "Looks like I won't be able to get much studying done..."
    
    stop music fadeout 1.0
    
    #"SMSPF" "Lilly route GET! Cut to Lilly act 2."
    
label en_HLT6b: 
    hi "Sure, I'm already late anyway."
    
    show hanako cover_worry at centersit
    with charachange
    
    ha "I-I'm sorry..."
    
    hi "Don't be. I want to help you, after all."
    
    show hanako cover_smile at centersit
    with charachange
    
    "Upon my affirmation that Hanako is indeed worth missing my appointment with Lilly, she smiles."
    
    "I wish she'd do that more often."
    
    with shorttimeskip
    
    show hanako basic_bashful at centersit
    with charachange
    
    "The more we get into studying, the more relaxed Hanako gets."
    
    hi "Well, that should wrap things up. It's getting rather late to still be in class, too."
    
    hi "Do you want to go to the Tea Room, Hanako? We could play chess."
    
    ha "O-Okay..."
    
    stop music fadeout 1.0
    
    #"SMSPF" "Hanabanana GET! Cut to Hanako act 2."
    
label en_HLT6x:
    
    ha "D…do you mind if I ask one more?"

    return

