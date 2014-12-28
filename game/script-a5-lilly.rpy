label en_L43:

    # Open to act title card "Future"

    scene black 
    with dissolve 
    
    window hide
    nvl show dissolve

    nvl clear
    
    n "…"

    n "……"

    n "………"

    n "That beeping is really quite annoying."

    n "As regular as a metronome, the sharp pulses fire at my eardrums constantly."

    n "Wait… beeping?"

    n "I groggily open my eyes, remaining immobile on the bed."

    nvl clear
    
    scene white 
    with openeye 
    
    n "White."

    n "A horrid, plain white."

    n "Even before my eyes regain focus, I can work out three things."

    show bg hosp_room at bgright 
    with Dissolve (3.0) 
    
    n "One, that I am in a hospital."

    n "Two, that the beeping coming from beside me is an ECG."

    n "Three, that I am alive."

    n "… "

    n "I'm alive."

    n "That's… great."

    nvl clear
    
    n "As the small dimples and lines in the ceiling tiles finally take form, I lever myself up slightly."

    n "The mild pain in my chest is easily overcome as I look around the room."

    n "Well, it's a private ward. That's a plus."

    n "Looking down at myself, the sheer amount of pipes and patches on me makes me look more like some kind of bizarre experiment than a hospital patient."

    n "Content with my observations, I lie back down and stare at the bleached white ceiling."

    nvl clear

    n "So. I'm alone again."

    n "How perfectly fitting."

    n "No, no, I won't go down this road."

    n "I knew this could, nay, would happen eventually."

    n "The fact that I dodged Death's scythe once again, though, is surprising."

    nvl clear

    n "To be honest, my memory of that night is surprisingly clear."

    n "While I can't remember the final moments, I can remember going to Tanabata."

    n "Buying the candy apple, shooting the bear, helping that boy, and sitting on the grass next to…"

    n "…Oh."

    nvl clear

    n "My brain seems to fly in a million directions at once as I remember that person."

    n "Frantically trying to regain my concentration, I cover my face with my hands."

    n "…Promptly causing the catheter in the right to dig into the skin."

    nvl clear
    nvl hide dissolve
    
    window show
    
    hi "Ah, dammit!"

    "For a moment, everything seems to go silent."

    "That is, before the handle of the door slowly opens."

    "Tilting my head up, I see the figure that emerges from the door."

    "…Whereas before my mind seemed to be filling with too much information, now it's completely blank."
    
    show lilly basic_concerned_cas
    with charaenter
    
    "That person that stands there is the one who I'd so nearly said goodbye to."

    "The person that I'd accepted as having been a brilliant but momentary beacon in my abruptly-ended life."

    "Beep, beep, beep."

    "The ECG is the only noise to be heard."

    "As she moves her mouth silently trying to work out what to say, she can only mumble with great trepidation."

    li "Hi… sao?"

    hi "Uh… hey."

    "It seems I've come up trumps as well."

    "She slowly walks towards the bed, her hands slightly ahead of her."

    "Gone is her usual gracefulness, replaced by a paper-thin facade that would break if breathed upon."
    
    show lilly basic_reminisce_cas_close
    with charaenter
    
    "Eventually she reaches the side of the bed, hands gently resting on the side."

    "It's taking every fiber of her being to retain her composure, right now."

    li "Hisao, you…"

    "I give an indulgent smile and bring my arms wide."

    hi "Come here."

    # lilly_hostpital CG [str]
    scene ev lilly_hospitalclosed at bgright
    with whiteout
    
    "With that, she gingerly falls onto my chest, her head resting below my chin."
    
    scene ev lilly_hospital at bgright
    with locationchange
    
    li "Hisao, when we were at the…"

    "Her voice nearly cracks as she tries to spill out all the information she can."

    "I cut her off with a gentle rub of her hair."

    hi "It's okay, Lilly. It's okay."

    "She can only manage a small, silent nod leans on my chest."

    "I'm not quite sure how long we stay like this, but eventually Lilly's soft voice rings out."

    scene ev lilly_hospitalclosed at bgright
    with locationchange
    
    li "I thought… you were gone."

    "Gone. Not dead, gone."

    "She can't bring herself to utter that fateful word."

    hi "I couldn't have died, silly."

    scene ev lilly_hospital at bgright
    with locationchange
    
    li "Hisao?"

    hi "You spent all my money, remember? I couldn't pay the ferryman."
    
    scene ev lilly_hospitalclosed at bgright
    with locationchange
    
    "For a moment she raises her head and looks lost, before smiling and snuggling her head back onto me."

    li "Thank you, Hisao."

    "Her mood somewhat lifted, she picks herself up and regains herself."

    scene bg hosp_room at bgleft
    show lilly basic_weaksmile_cas_close
    with locationchange
    
    "That's the Lilly I'd been wanting to see. She's back to her old, strong self again."
    
    show lilly basic_weaksmile_cas_close at centersit
    with charamove
    
    "Reaching back for a chair, she takes a seat beside me."

    li "I suppose… you're a bit lost?"

    hi "Now that you mention it, yeah. How long was I out?"

    li "Three days. Well, two and a little. This is Wednesday."

    "Three days, huh?"

    "In the grand scheme of things, it isn't that long. That said, I can't imagine it's been pleasant for Lilly, or my parents."

    "Which brings me to my next question, actually."

    hi "Do my parents know?"

    li "Yes. The hospital notified them."

    hi "Have they been in?"

    li "The day you came out of intensive care, they arrived."

    li "It was when they were on their way out that I met them."

    hi "I… see."
    
    show lilly basic_giggle_cas_close at centersit
    with charachange
    
    "She gives a small giggle at my uncomfortableness."

    li "There's no need to be embarassed. They were quite nice."
    
    show lilly basic_smile_cas_close at centersit
    with charachange
    
    "For a second, her calm smile seems slightly disturbing."

    "As I look up the the roof to look away from it, I ask the only question left on my mind."

    hi "How long will I be in hospital?"

    li "The doctor said it would be about three weeks."

    "Three weeks."

    "I hear the words, but for some reason my mind refuses to understand them."

    "Compared to my perfectly lucid thinking of before, my mind's clouded and muddied."

    "Hearing an exasperated sigh, Lilly sharply inhales."

    li "Hisao, are you okay?"

    "I turn back to her."

    hi "I'm fine. It's just… I'm having trouble thinking clearly."

    "She calms significantly, a relieved sigh sneaking past her graceful composure."

    li "It's probably the anaesthetic. I could get a doctor if you'd like."

    hi "No, no, it's fine. As you said, it's probably just the anaesthetic."

    "Doubtful, considering I could think so clearly before."

    li "Sorry for suddenly dumping all this information on you like this."

    hi "Hey, I'm the one asking for it."

    hi "Damn, I guess this means we won't be going to the summerhouse, eh?"

    "She gives a small giggle at my playful tone."

    li "We can always go later. What matters is that you're alright."

    hi "I'll be glad to get all these pipes and plugs off, in any case."

    "As the brief moment of lightheartedness wears off, silence fills the air."

    "It's pretty hard to escape the fact that I'd nearly died there and then."

    "As much as I hate to say it, I can feel a wave of tiredness washing over me as well."

    hi "Sorry Lilly, but I'm kinda tired."

    "She nods gently, before bringing a hand to the side of my cheek."

    li "I'm glad you're okay, Hisao."

    "I take her hand in mine, wires be damned, and smile."

    hi "Thanks. I'm glad that you were around when I woke up."

    "Savouring each other's silent contact for moments on end, we eventually part."
    
    hide lilly
    with charaexit
    
    "With a kind farewell and assurance that she's tell the nurse about my situation, Lilly leaves the room."

    "My gaze returns to that white ceiling."

    "Here I am, once again."

    "In this damned bleached, silent and sterile hospital."

    "I give up on keeping my heavy eyelids open, calling a curtain-close on my discontent reverie."

    "The more things change, the more they stay the same."

    "That is the one thought that flickers through my mind before I fall asleep."

    scene black
    with shuteye
    window hide
    
    with Pause(3.0)
    
    return

label en_L44:
    
    # Sticking with the heart attack schtick for now. Can change it later if it ends up too incongruent with the rest of the path

    show bg hosp_room at bgright
    with openeye
    
    nvl show dissolve

    nvl clear
    
    n "As I wake up from another nap, I glance down at the newspaper sitting on the table over the bed."

    n "It's Thursday. Apparently."

    n "Thinking back to this morning, however foggy my thoughts may be, I can just remember asking for it."

    n "After the doctor explained largely what Lilly had already told me, I'd asked for a newspaper to occupy myself with."

    n "While I count myself as a reasonably patient person, being bedridden with nothing to do would be maddening."

    n "Actually, to say he'd only told me what Lilly has would be a lie."

    nvl clear

    n "On Sunday, I had an acute heart attack."

    n "Soon rushed to hospital, I'd been stabilised and kept in intensive care until late tuesday for observation."

    n "While I'd been unconscious, both my parents and Lilly had visited, with the three meeting."

    n "What a travesty."

    n "A guy's parents meeting his girlfriend purely by chance."

    n "…But I digress."

    n "While that may account for the time before I'd woken up, the period since has been no end of annoyance."

    nvl clear

    n "Aside from the trivialties of hospital life, even reading the newspaper is a task in and of itself."

    n "My eyes can read fine, but my mind seems to be stuck in first gear."

    n "Trying to grasp even the most simplistic ideas right now is like trying to grab running water with an outstretched hand."

    n "And so, I've been reduced to looking at the black and white photos in it, and sleeping."

    nvl clear

    n "I let out a small self-deprecating laugh."

    n "I must look truly pitiable, like this."

    n "Thankfully, my parents visited me in the morning while the doctor was there."

    n "Thanks to him, pretty much every question was deflected away from me and onto him."

    n "My condition (cardiac arrest), the cause (strain), the time (Sunday evening), the treatment (drugs, and three weeks in hospital)."

    n "Everything there was to tell was told."

    n "Which is good, because at the time I was even less lucid than now."

    nvl clear

    n "I lean back and sigh."

    n "Ever since seeing Lilly and my parents, I've realised just how easily I'm taking this compared to everyone else."

    n "I guess the best explanation is the philosophy that I've followed since the first heart attack."

    n "If it happens, it happens. If I die, then that's it."

    n "Life is transient. What's grasped one day can just as easily slip out the next."

    n "Just as easily as I lost my previous life…"

    nvl clear
    nvl hide dissolve
    
    window show
    
    show lilly cane_smileclosed_cas
    with charaenter
    
    "Before I can continue the thought, the pale white door gingerly opens to reveal the ever-pale Lilly, cane in hand. Her face is an all too welcome sight."

    hi "Hey Lilly."

    li "Oh, you're awake?"

    hi "Yeah. I've been in a daze for most of the day, you caught me at a good time though."
    
    show lilly cane_smile_cas_close
    with charachange
    
    "She slowly walks over to the chair beside the bed, resting her cane against the wall as she feels it out."

    li "How are you feeling?"

    hi "Okay, mostly. I just seem to be having trouble focusing my mind on things."

    hi "How's the world outside?"

    li "Outside? Hmm…"

    "I guess she hadn't expected the question."

    li "It may be somewhat unfortunate, but news travels fast."

    hi "Everyone knows?"

    li "Everyone knows."

    hi "Oh boy."
    
    show lilly cane_giggle_cas_close
    with charachange
    
    "Lilly fails to hide her small giggle at my expense."
    
    show lilly cane_smile_cas_close
    with charachange
    
    li "Do you have anything you'd like me to get for you from your dormitory?"

    "I lean back and think before eventually giving a reply."

    hi "Books, I suppose."

    li "Any in particular?"

    hi "All of them, if you could. They'll be sitting on my desk in a small pile. Do you have my key?"

    "She gives an affirmative nod."

    li "Your parents gave it to me."

    "My parents are just as quick to trust as I am, it seems."

    li "I'll go get them now then, if you'd like."

    hi "Sure. I don't think I'll be going anywere, at least."
    
    hide lilly
    with charaexit
    
    "She lets out a small snort of laughter at my carelessness, before opening the door and taking her leave."

    "I suppose there isn't much more to do other than sleep."
    
    # Close eyes, timeskip
    scene black
    with shuteye
    
    with Pause(1.5)
    
    "Poke. Poke, poke."

    rin "Is he awake?"

    emi "No idea."

    "Yes, I'm awake. No thanks to you two."

    "Poke. Poke, poke."

    rin "Is he dead?"

    emi "I don't think he is…"

    hi "I'm not bloody well dead."

    emi "Geh!"

    # Open eyes to scene
    show bg hosp_room at bgright 
    show emi basic_hes_close at tworight
    show rin relaxed_nonchalant at twoleft
    with openeye
    
    emi "Uh, well, uh…"

    emi "It was Rin! Rin was poking you!"

    hi "I find that hard to believe."

    show emi sad_shy_close at tworight
    with charachange
    
    "I look flat-faced at Emi for seconds on end before she grimaces at her grave mistake."

    show emi basic_confused_close at tworight
    with charachange
    
    emi "Oh. Ooooooh."
    
    show rin basic_deadpannormal at twoleft
    with charachange
    
    show rin relaxed_nonchalant at twoleft
    with charachange
    "As I blink my eyes to get a better view, I nod to Rin, of whom promptly nods back."

    "While the two seem to be as bumbling as usual, there's a definite edge to their antics."
    
    show emi sad_angry_close at tworight
    with charachange
    
    "I give a lackadaisical sigh and rest my hand on Emi's head, scruffing her hair a bit to her protest."

    hi "Good to see you. Both of you."

    show emi basic_annoyed_close at tworight
    with charachange
    
    emi "I can't believe you, Hisao."

    hi "What'd I do?"

    emi "What'd you do? I went and had a heart attack!"

    emi "From now on, I forbid you from having heart attacks! You hear me?"

    hi "I don't think they work that way…"

    "In the face of Emi's pouting, I give up any worth in protesting."

    hi "So what've you two been doing? Aren't you meant to be on holidays?"
    
    show emi basic_closedgrin_close at tworight
    with charachange
    
    emi "We were just staying at my mom's house. It's not far to come here."

    "It's only now that I notice two large bags sitting next to Rin."

    hi "Been shopping?"
    
    show rin basic_deadpannormal at twoleft
    with charachange
    
    rin "Art shop was on the way here."

    hi "Ah. That makes sense."

    emi "It took long enough to drag you out of there…"

    rin "The art shop was more interesting than the hospital."

    rin "Can we go to there again after we leave here?"

    "Good grief."

    "Before Emi can reject the proposition, the door handle creaks."
    
    show rin relaxed_nonchalant at twocenteroff2
    with charamove
    
    show lilly basic_oops_cas at left
    with charaenter
    
    
    "Through it comes a (very cute…) nurse, followed by Lilly."

    "Both arms holding the sizable tower of books, her chin rests on the topmost book to hold it in place."
    
    show emi excited_proud_close at tworight
    with charachange
    
    emi "I saw that, Hisao…"

    hi "H—Hey, Lilly!"
    
    show emi basic_closedgrin_close at tworight
    with charachange
    
    "I quickly cut Emi off, lest she tell Lilly of my wandering eyes."

    li "You said it was a small pile…"

    hi "It's only as tall as Emi, and Emi's short. Therefore, it's small."

    show emi basic_confused_close at tworight
    with charachange
    
    emi "Hey!"

    "The nurse, still holding the door, gives a smiling nod of farewell before leaving. I guess she must've been leading Lilly through the halls."

    "Lilly quickly sets the stack of books down beside my bed, dusting herself off after doing so."

    li "I take it that's Rin and Emi?"

    emi "Present!"

    rin "Correct. Ten points."

    emi "Out of?"

    rin "I don't know."

    "Lilly gives an amused smile. The two really are a stage act."

    li "How are you two doing these days?"

    rin "Better than Hisao, I think."

    hi "Touche."

    "Lilly's more than a little put off by the risque quip, no doubt meant in more seriousness than it should be."

    emi "More to the point, how are you?"

    "As she looks to me, I can sense a slight cautiousness in her expression. Despite all of her bluster, she's indisputably worried."

    hi "Well, I'm fine now. Aside from the pipes going into me, I feel pretty good."

    hi "Oh, Lilly?"

    li "Yes?"

    hi "The doctor said I'll be out in three weeks."

    li "Thank goodness."

    emi "Just in time to begin school again, eh?"

    hi "I guess I just wasn't meant to have a summer vacation."

    li "Don't say that. At least you're okay."

    hi "Yeah, true. Thanks to you, I've got something to read while I'm in here as well."

    "Without warning, Emi suddenly stands and claps her hands together."

    emi "Well, we'd better get going."

    rin "Can we go to the art store?"

    emi "Yes, Rin, we can go to the art store."

    "Without another word, Rin begins moving to the door alongside Emi."

    hi "Wait, I thought you weren't going to go to the…"

    emi "We, uh, had planned to, but I'd forgotten. That's it."

    emi "Seeya, Hisao. Seeya Lilly."

    rin "Bye."

    hide emi
    hide rin
    with charaexit
    
    "Lilly and I can barely raise out hands to wave them goodbye before they're out the door."

    hi "Those two…"

    li "Well, their hearts are in the right place at least."

    hi "True. Though, seeing those two does remind me of someone else. How's Hanako doing?"

    li "So far I've only had a short phone conversation with her. She's currently in Kyoto, but'll be coming back up soon."

    hi "She taking it okay?"

    li "Surprisingly so. She was worried, but didn't panic at all."

    hi "Thank goodness."

    li "Oh, what's the time, by the way?"

    hi "The time, uh…"

    "I look over to the analogue clock hanging on the wall."

    "The reason for her asking becomes quite clear."

    hi "Ah. Hospital visiting hours are ending."

    li "Very well. Do you need anything else, while I'm out?"

    hi "Nah, the books should be fine. Thanks for bringing them in."

    "She nods, leaning forward to give me a small, affectionate kiss as she uses her hand to guide her."

    li "See you tomorrow, Hisao."

    hi "Seeya."

    hide lilly
    with charaexit
    
    return

label en_L45:

    show bg hosp_room at bgright
    with shorttimeskip
    
    window hide
    nvl show dissolve

    nvl clear
    
    n "Today was interesting."

    n "That's the first lie I've been trying to tell myself."

    n "The hospital isn't as boring as it first seems."

    n "That's the second."

    nvl clear

    n "Well, the day wasn't entirely without unusual happenings."

    n "After reading through the first couple of books in the veritable tower Lilly brought in, I noticed a single one that I hadn't yet read."

    n "“A Brief History of Time.”"

    nvl clear

    n "I had been planning to read it, but it kept being shuffled down my list of priorities."

    n "…Attending to the amorous advances of a lady tends to have that affect."

    n "But in all seriousness, I'd hardly turned a page until now."

    n "Reading it gave an odd experience."

    n "A mixture of trepidation and unease would be the best description."

    n "Compared to my senses, my mind is pure dissonance."

    n "To borrow a term from Lilly, anyway. Music isn't a hobby I see myself taking up anytime soon."

    nvl clear

    n "I sigh to myself in frustration."

    n "Being cooped up in hospital like this really feels as if I've been neatly moved into a sterilised pocket away from reality."

    n "The future doesn't appear in any tangible form, nor does the present manifest itself in any way."

    n "The past, however, is less restful."

    n "Over and over it replays, dredging up the most banal and the most treasured of memories."

    n "And every time, the blonde-haired girl in that bright yellow field comes to the surface."

    n "Every time I remember her, every time I see her, I get the same feeling of unease as I get when I see that book."

    nvl clear

    n "Well, not that she knows."

    n "Everyone is happy, as long as I am."

    n "With a just simple smile, their worries quickly lift."

    n "As long as Lilly smiles, I don't care."

    nvl clear
    nvl hide dissolve
    
    window show
    # Timeskip
    show bg hosp_room at bgright
    show lilly cane_smile
    with shorttimeskip
    
    "After Lilly arrived, we both began to read in short measure."

    "There are many things about the hospital which annoy me, but the quiet certainly isn't one of them."

    "And so, we both quietly read in each of our own ways."

    "…"

    "Her presence is calming, in a way."

    "Though, as soon as a think a single thought about her, my mind starts twisting."

    "Such a troublesome situation."

    li "Sorry, I just have to go out for a second."

    hi "Hmm? Oh, ah, okay."

    "Her hand gently glides along the smooth wall, her other quickly turning the handle as she find the door."

    "And so, I'm alone once again."

    centered "*Thud* *thud* *thud*"

    "…But not for long, it seems."

    hi "Come in!"

    "As the door opens, I can tell who it is simply by her distinctive hair."

    hi "Hey Misha, Hey Shizune."

    "By now, it's become a reflex to address them both when I see even just one of them."

    "The fact that one is never without the other somewhere in close vicinity is wryly amusing."

    "And, sure enough, Shizune follows Misha through the door."

    hi "Good to see you two—WOAH!"

    "Misha covers the length of the room in an instant, hugging me tightly before I can say another word."

    hi "M—Misha…"

    "Her chest is just as large as it looks, it seems."

    "As she presses it tightly against me, I let my arms flop out to the sides."

    mi "We were so worried, Hicchan~!"

    "We I look over Misha snuggling shoulder, Shizune gives an odd gesture somewhere between a shrug and a nod."

    mi "We heard from Lilly, are you okay? Are you okay?"

    "Lilly… Come to think of it, she mightn't approve of Misha's overexuberance."

    "And then there's Akira's warning…"

    hi "You'll finish me off if you don't let me breathe!"

    "She pauses for a second before bouncing off me and taking her usual place beside her bespectacled partner."

    mi "As sharp as ever, Hicchan!"

    "I wouldn't describe that as sharp, but with Misha in such an excitable mood, I'll let it slip."

    "Apparently detecting my being taken slightly aback, Shizune begins a round of rapid-fire signing."

    "Though, interestingly, towards me instead of Misha."

    "…"

    "…"

    "…"

    "As the signing ends, a calm smile takes it's place on Shizune's face."

    mi "Shizune says…"

    mi "“I'm glad you're well, and hope you have a fast recovery.”"

    "A small grin spreads across Misha's face."

    mi "“But, of course, we cannot let such things get in the way of important council work. We look forward to your help when school begins again after the holidays.”"

    "In any other circumstance, I'd be grimacing."

    "But looking at the two now, I can't help but chuckle."

    "While I've no doubt they'll be harassing me once again as soon as I set foot in the classroom, I can't help but look forward to it."

    hi "You'll get exactly the same answer as you'd have gotten before the holidays, you know."

    mi "But of course! That's why we have to keep trying!"

    "Misha's logic is impeccable."

    "As we talk amongst ourselves, the door cautiously opens."

    li "Hello?"

    "Lilly's voice is full of trepidation, unsure of what the situation is."

    hi "Hey Lilly, it's just Misha and Shizune."

    mi "“Just?” You're so mean, Hicchan~"

    hi "A small win against the forces of the student council. I have to take what I can get."

    "Both of us nervously grin at each other as Shizune and Lilly stand side-by-side."

    "Two black holes of communication, not a meter apart."

    li "Thank you for coming, Shizune."

    "Shizune gives a small nod in return, grimacing slightly as she realises her mistake."

    "She really does dislike not calling the punches."

    "Eventually she retreaes through communication through Misha, signing a brief series of words to her."

    mi "Shizune said that she hopes that Hisao will be okay, and that she is glad that you are there for him."

    "Deftly manouvering around Lilly's blindness, she makes sure to use as lighthearted a tone as she can to make up for Shizune's formality."

    mystery "Just go two more doors down, and it'll be on the left."

    mystery "Ah, thanks. I mean, thank you very much, ma'am."

    "All except Shizune draw their attention to the door."

    "Eventually it creaks open, a scarred face appearing through the crack."

    ha "Is this… Hisao's room?"

    hi "Oh, hey Hanako."

    "As she steps into the room, Shizune taps Misha on the shoulder and gestures for the two to leave."

    mi "Well, we'd better go. Seeya Hicchan!"

    hi "'Bye."

    "She and Shizune wave goodbye to Hanako and Lilly, closing the door on their way out."

    ha "It's nice to see you again. Both of you."

    li "It's nice to have you back, Hanako."

    hi "Yeah. How was the travelling?"

    ha "Hmm? Oh, ah…"

    "Not expecting to have a question directed at her, she takes a moment to collect herself."

    "Her smile's as small and dainty as ever, though the same couldn't be said of her attire."

    "Freed of her loose-fitting clothing, she actually has quite the figure."

    ha "I've only been to Kyoto so far, but it's really nice."

    ha "The people there were nice, and there's some really pretty places there."

    hi "Sounds like you were having a great time."

    ha "Ah, no! It's okay! I wanted to come down and see you!"

    li "It's okay, Hanako. Calm."

    "She gives a meek nod, settling herself expertly. It seems her innocence has far from disappeared."

    ha "I'm glad you okay, Hisao."

    hi "I'm… Thanks. I'm glad you're here."

    "A small silence reigns, all three of us glad for the other's presence."

    li "It's just like old times, isn't it? All three of us here, together like this."

    ha "Mm, it is."

    "I almost agree, but stop myself before I do."

    "The three of us may be together, but we've all changed."

    "Lilly's no longer forcing down her feelings, and Hanako's wings have grown beyond the care that Lilly and I gave."

    "The only thing that's even remotely similar is the three of us being in a hospital, but even then, it was Lilly that was bedridden, not I."

    # Marked for possible expansion

    "The rest of the time Hanako's here is largely spent discussing her trip, and our Tanabata outing."

    "As she leaves, Lilly gives a gentle bow as I smile and wave."

    li "It's nice to see her again."

    hi "Yeah, it is. She's really changed, hasn't she?"

    li "She has. It's wonderful."

    hi "You know, she'd never have gotten to this point if not for you."

    li "In the end, though, you were the one to help both of us."

    "She walks over to the side of the bed, gently bending down and kissing me lightly on the lips."

    li "Thank you, Hisao."

    "As I stare into her deep blue eyes, as unseeing as they are, I can't help but smile."

    "Love really is a fickle thing."

    return

label en_L46:

    window hide
    nvl show dissolve

    nvl clear
    
    n "As I wake up, I try to recall which day it is."

    n "…To no avail."

    n "At least I'm reasonably sure that it's the afternoon right now."

    n "Though the reason for knowing is something I'd rather not recall."

    nvl clear

    n "Soon after the hospital visiting hours had begun, Hanako came in."

    n "While it was mostly smalltalk, one fact became clear."

    n "Lilly, especially during the days just after the heart attack, hadn't been as calm and collected as I'd thought."

    n "Every time she saw me, she'd been putting on a brave face."

    n "Since Hanako left, it's pretty much all I've been thinking about."

    nvl clear

    n "As much as I'd thought our relationship had progressed, she still hides her feelings."

    n "It's when she hides herself to stop me worrying that I become the most concerned for her."

    n "That wall between us is still there after all this time."

    n "But… why?"

    nvl clear
    nvl hide dissolve
    
    window show
    
    centered "*Thud* *thud* *thud"

    hi "Come in!"

    "The plain white door slowly opens, the unmistakable pale arm of Lilly becoming visible."

    hi "Hi, Lilly."

    li "Good afternoon, Hisao."

    "As she walks next to the bed and takes a seat, I only just notice the small beige bag in her hand."

    li "How are you feeling?"

    hi "Same as usual. Yourself?"

    "She gives a smile, though there's a tinge of resignation to it."

    li "Well. I brought something for you."

    hi "Oh?"

    "She reaches into the small beige bag, my eyes tentatively peering in."

    "Eventually she retrieves the only item in the bag, an intricately carved small wooden box."

    "One which looks very familiar."

    hi "That's…"

    "She just smiles and silently hands it to me."

    "Upon closer inspection, it's not the same music box I'd given her. The design is very slightly different, and the colour a little darker."

    "As I turn it upwards to look underneath, I pause."

    "A small brass plate is attached to the bottom, glistening in the dim light of the room."

    "On it is engraved three simple characters."

    "…Hi—sa—o."

    "That time when I'd given the music box to her… She wanted to give that same feeling to me."

    "with a silent breath, I gently pop open the lid."

    # oh hay music

    # some sort of pause or something

    "…The Saraband."

    "As the music plays, my eyes stay fixed on the small performance despite my thoughts being elsewhere."

    "That gentle smile on her face back then…"

    "That's… it. I've been stupid. Really, really stupid."

    "I spent so long trying to enter her heart, I'd admonished her for hiding herself…"

    "But I'd been doing the same. All this time."

    "My lips barely move, my mind still trying to organise it's scattered thoughts."

    hi "Lilly… I…"

    li "Hisao, I want to see every single emotion you have."

    li "Sadness, anger, whatever you feel."

    "The field… that promise…"

    li "But most of all, I want to see your smile."

    "Word… for word…"

    li "Your true smile."

    "My mind barely registers the performance's ending as Lilly's gentle smile fills my thoughts."

    li "Smile when you want to smile. Cry when you want to cry."

    li "I love you, Hisao. So you don't have to hold back any more."

    "Silence."

    "She… knew."

    "All this time, she'd known, and tried to reach me."

    hi "Lilly… I'm…"

    "As the golf ball in my throat strangles my words as they try to form, Lilly's arms reach out to me."

    # CG

    li "It's okay, Hisao."

    hi "I'm sorry, Lilly."

    li "Mm."

    hi "I was… scared…"

    li "Mm."

    hi "I didn't want to lose you… everyone… everything… Not again…"

    li "It's okay, Hisao. I'll be beside you. Always."

    li "I promise."

    "As I grip her tightly, the small pitpat of tears on her back, I savour the feel of her presence. The presence of the love that I'd so nearly lost."

    mystery "Oi, oi, oi!"

    "Lilly gently releases me as I do her, quickly move to wiping my eyes as I look up."

    aki "For a second there I'd thought I'd walked into a funeral reception!"

    li "A… Akira!"

    hi "Pfft… Bwuahahaha!"

    "Lilly looks entirely lost as I burt out into uncontrollable laughter."

    "Akira's cheesy grin belies her cheeky entrance, with Lilly eventually breaking down and laughing just as boisterously as I."

    "As poor Hideaki wanders into the maelstrom of gaiety, the best he can manage is an awkward grin of confusion."

    "This isn't the end. My life has one hell of a lot of kick left in it."

    "Even if it does end up short, my happiness with Lilly will be life a blinding spark of joy."

    return

label en_L47:

    # Entire scene handled through CG

    "As Akira, Lilly and I sit on the grassy embankment, the breeze gently blows through the cloudless sky."

    "A deep blue sky, as endless as life itself."

    li "This is a nice place."

    hi "Yeah. I never knew a place like this was anywhere near Yamaku."

    aki "And I had to be the one to find it, geez."

    aki "Good that you're outta hospital though, Hisao."

    hi "Nobody's more glad than I am. I can't stand hospitals."

    aki "So, you two going back to school tomorrow?"

    $ doublespeak(hi, li, "Yup.")

    "Akira gives an amused grin before looking back out to the river."

    hi "Pity we couldn't get out to the summerhouse during the vacation."

    li "Well, there's always next time."

    aki "You'll be graduating before the next summer vacation, won't ya?"

    hi "Yeah. And then there's college."

    aki "Going to the same one?"

    li "Likely. We both have the scores to meet the entry requirements."

    hi "You sound so sure…"

    li "Don't worry, you're better than I in most subjects."

    hi "I guess we'll work it out in due time."

    aki "That's the way. Just enjoy yourselves in Yamaku while you're there."

    "Lilly gives a sad sigh at the distinction between Akira and us."

    li "Do you really need to go back to South Africa?"

    aki "Yeah. Folks are already out for my blood as it is."

    hi "You weren't meant to stay this long?"

    "She gives her trademark cheeky grin."

    aki "I wasn't meant to come to Japan at all, boy."

    aki "I just couldn't pass up an excuse to go see my favourite sister though~"

    "She leans right and gives Lilly a tight playful hug, cheering Lilly up considerably."

    li "It's nice to see you, though."

    hi "For what it's worth, I'm in the same boat."

    aki "Heh, thanks you two. I'll try and come back sometime."

    li "It's a shame that your business keeps you so busy."

    aki "The place won't run itself, I'm afraid. Still, if it weren't for that I'd never have met Hideaki."

    hi "That reminds me, where is he?"

    aki "Where is he… you say?"

    "Her wild smile is slightly discomforting."

    li "You can't be serious…"

    aki "He's waiting at the airport for me."

    "Lilly hides her face in her hands as I give an amused chuckle."

    hi "Have fun over there, both of you."

    aki "Haha, will do."

    "With a slight heave, she levers herself up with her and and takes to her feet."

    aki "Well, I'd better be off."

    li "Goodbye, Akira."

    hi "'Bye."

    "For a second, the dark-clad figure looks down the Lilly, smiling deeply."

    "And with that, she walks away, one hand held in the air as she goes."

    aki "Seeya later, you two!"

    "A tune with no beat, melody or direction."

    "After a few moments sitting silently, hand in hand, we pick ourselves up."

    "Turning towards her with a deep smile, I hold out my hand."

    hi "Shall we be off, madame?"

    "She takes my hand in hers, nodding with that beautiful warm smile."

    li "Indeed we shall."

    # Ending CG

    "As we set off towards the dormitories, that wonderful smile engraves itself onto my memory."

    "That wonderful smile, that we both share."

    "Because it's together that we'll walk forwards."

    "Forwards… towards our future."

    # End of Lilly path

    return

label en_end_lillygood:
    # Lilly good end, after L47
    scene black with dissolve
    centered "~ lilly good end ~" with dissolve
    return
