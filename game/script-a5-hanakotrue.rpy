label en_HT14:

    #Classic Kotoko.
    #also Lol yuri themes.
    
    window hide None
    
    scene bg school_scienceroom
    with locationchange
    #bg Classroom

    #Act 5 (?) title card… I need to think of a title. Not really good at that. Something "final".
    
    play music music_night fadein 4.0
    
    nvl show dissolve

    n "\n\nWhat a weekend. After leaving Lilly's room, I practically fell straight asleep…"

    n "… without setting my alarm."

    n "\nIf it wasn't for a particularly shrill bird, I would have been late to class."

    n "The run to beat the bells set my chest ablaze, and for all the wrong reasons."

    n "Some people joke about giving themselves a heart attack in situations like that."

    n "It's not so funny when it's a part of your reality."

    n "\nBut that's not the point."

    n "My tardiness neglected my morning conversation with Hanako, and now that there's only a few seconds to the lunch bells, I'm itching to say “Good Morning.”"

    n "…amongst other things, of course."
    
    nvl hide dissolve

    nvl clear
    
    window show

    "Mutou finishes writing the last of the exam timetable on the board, and puts down the chalk."
    
    show muto normal
    with charaenter
    #Mutou serious

    mu "So ends this trimester's lessons. From now until the end of your exams is study time."

    mu "Myself and the other teachers will be available to help you."
    
    show muto irritated
    with charachange
    #Mutou contemplative

    mu "But, I suppose if you have made it this far and haven't absorbed the material, there's very little we can do for you."
    
    play sound sfx_normalbell
    
    hide muto
    with charaexit
    
    stop music fadeout 4.0

    "The bells ring, Mutou leaves the classroom, but no-one moves."

    "The severity of his words seems to hit home with more than a few students."

    "Ashen faces fill the room, but none more ashen than the one closest to me."
    
    show bg school_scienceroom at bgright
    with charamove
    
    play music music_comedy fadein 1.0
    
    show misha sign_confused
    with charaenter
    #misha sad/heh…. heh… heh

    mi "Heh… heh…"

    mi "Hey, Hisao…"
    
    show misha perky_confused
    with charachange

    mi "He's not serious, is he? Heh… heh…"

    "Man, I never thought anyone would knock the wind out of Misha's sails."

    "She still wears her idiotic smile, but her eyes are dead."

    "No, worse than dead."

    "From the nose up, Misha looks like a zombie."

    hi "I don't think it's that bad."

    hi "I mean, you've passed most of your tests to now, right?"

    "No change."

    "Ah well, this is amusing in its own right."
    
    show shizu invis at right
    with None
    
    show bg school_scienceroom
    show shizu cross_angry at tworight
    show misha perky_sad at twoleft
    with dissolvecharamove
    #Shizune pissed off

    "Behind the zombified Misha, Shizune taps impatiently on the desk."

    "Misha, however, doesn't react, so I am left facing a clearly unimpressed Shizune."

    "I try to gesture “what” to her, but to no avail."
    
    show shizu behind_frown at tworight
    with charachange

    shi "…"
    
    show shizu adjust_frown at tworight
    with charachange

    "She sighs, pushes her glasses up on her nose, and points behind me."

    hi "Eh?"

    ha "Good morning, Hisao!"
    
    show hanako invis at offscreenright
    with None
    
    show bg school_scienceroom at bgleft
    show shizu behind_blank
    show misha perky_sad at left
    show hanako basic_smile at right
    with dissolvecharamove
    #Show Hanako Happy

    hi "Hanako! Sorry, I got distracted, and I was late this morning, and… yeah…"

    ha "T—that's okay. I wanted to speak to Misha and Shizune, too."

    hi "Huh?"

    #Misha Eh?
    
    show misha sign_confused at left
    with charachange

    "Misha snaps out of her reverie."

    mi "You want to speak to us?"
    
    show hanako emb_timid at right
    with charachange
    #hanako embarrassed

    ha "Um, well, I ended up making too much for lunch today, and you and Shizune seem to talk to Hisao a lot… and, um…"
    
    show hanako emb_blushtimid at right
    with charachange
    #mabye a more embarrassed Hanako?

    ha "I wanted to know if you wanted to join us for lunch and study…"

    extend " maybe…"

    extend " only if you wanted to…"
    
    show misha hips_grin at left
    with charachange
    #misha excited

    mi "Eh? What's this? You're asking us to come with you?!"

    mi "But you never talk to anyone!"
    
    show hanako emb_blushing at right
    with charachange

    ha "Um, well, I thought that you and Shizune might get lonely…"

    ha "There's no-one else on the council…"

    hi "I thought you said there were a lot of people on the council?" #holy hell, cpl, lay off the "Eh?"'s... -Alphabro
    
    show misha sign_smile at left
    with charachange

    mi "There is, but there isn't."
    
    show misha cross_smile at left
    with charachange

    mi "It's like that."

    hi "Oh, I get it."

    "I don't get it."
    
    show misha cross_laugh at left
    with charachange

    mi "But this is big news! Lunch! Study!"

    mi "Count us in!"

    hi "Um, shouldn't you ask Shizune first?"

    "Shizune sits directly next to Misha, who seems oblivious to her presence."

    "In fact, I think this is the longest that I think I've seen Misha go without signing something."
    
    show misha cross_grin at left
    with charachange

    mi "What? No, Wahahaha~! She'll pretend to say no but she'll come along."
    
    show misha cross_smile at left
    with charachange

    mi "We've seen you work in science."

    mi "We need someone like you that isn't dumb at it."

    "Misha lowers her voice."
    
    show misha perky_smile at left
    with charachange

    mi "Shicchan would never admit it, but she's bad at science."
    
    show misha hips_laugh at left
    with charachange

    mi "But don't tell her I told you that~!"
    
    show shizu behind_frustrated
    with charachange

    "Behind Misha, a shadow rises."

    "Tapping on the desk didn't work."

    "Gently tapping her shoulder didn't work."

    "In a soundless vocabulary, these are the equivalent of “Excuse me” and “Hey! Misha!”"

    "Misha, however, remains oblivious."
    
    play sound sfx_impact
    
    show misha perky_sad at left
    show shizu cross_rage at center
    show hanako defarms_shock at right
    with vpunch

    "The shadow winds up, and delivers possibly the most graphical “I'm Talking to You, Damn it!” that I have ever seen."

    #Misha cry/rubbing head

    mi "Ow… Shizune~"
    
    show hanako def_worry at right
    with charachange

    mi "You didn't have to do that."
    
    show shizu behind_frustrated
    with charachange

    mi "Yes I did, you weren't paying attention."
        
    mi "But I was talking to Hisao…"
    
    show shizu basic_angry
    with charachange

    mi "About what?"
    
    show misha sign_sad at left
    with charachange

    mi "Umm…"

    "Misha's mouth stalls, however her hands go through the pre-programmed movements, spelling out her thoughts directly to Shizune."
    
    show shizu behind_frown
    with charachange

    mi "I should hit you again for being so insolent. Now tell me, what's going on?"
    
    show misha hips_grin at left
    with charachange

    mi "Oh, Hisao and Hanako want to study with us! Aren't we lucky?"

    show shizu adjust_blush
    with charachange
    #Shizune blush

    mi "Really?"
    
    show shizu behind_blank
    with charachange
    
    extend " Well, the council has light duties during the exam period, so I think it is a good idea."
    
    show misha sign_smile at left
    with charachange

    mi "Hey, Shicchan, can we use the council office?"
    
    mi "I don't see why not. Hisao, what do you think?"

    hi "Eh?"

    "I was so wrapped up in Misha's solo dialogue that I only barely registered my name being mentioned."
    
    show hanako emb_emb at right
    with charachange

    ha "It sounds like a good idea."

    hi "Yeah, sure. But lunch first?"
    
    show misha cross_grin at left
    show shizu adjust_happy
    with charachange

    mi "Yippie~! Lunch! We can do that, right?"

    mi "You should always study on a full stomach, right?"

    "I don't even know who is talking anymore."
    
    show misha hips_smile at left
    with charachange

    mi "So, where do we go?"

    ha "Um, I asked Lilly to meet us in the usual spot, so, maybe…"

    mi "Oh, where's that?"

    hi "The roof. It's kind of our place, no-one ever goes there."
    
    show misha sign_smile at left
    with charachange

    mi "You're right! I've never been there!"
    
    show shizu behind_frown
    with charachange

    mi "That's because it's supposed to be out of bounds."
    
    show misha perky_sad at left
    with charachange

    mi "Buu, don't be a killjoy. Hana here has invited us, we can't say no."
    
    show shizu basic_normal
    with charachange

    mi "Hanako invited us?"
    
    show hanako cover_worry at right
    with charachange

    ha "Y—yeah."
    
    show shizu behind_smile
    with charachange

    mi "Huh. I guess we can't refuse then."
    
    show misha hips_grin at left
    with charachange

    mi "Great! Lead the way, Hisao."
    
    stop music fadeout 3.0

    hi "Um, sure."

    "Slightly confused, I head up the narrow stairway to the roof."
    
    scene bg school_roof at bgleft
    with locationskip
    
    play music music_ease fadein 4.0
    $ renpy.music.set_volume(0.5, 0.5, channel='ambient')
    play ambient sfx_rooftop fadein 1.0

    #bg roof.
    #The following scene was originally going to be my finale.
    #It will require a lot of direction.
    #hopefully we can get away without my panning and zooming.
    #You know, like a certain other rooftop scene.
    #I'll include bits that *need* to be seen.

    "The midday sun is a little blinding, but I can clearly make out three shapes sitting near each other."

    hi "Oh, the others are here…"

    mi "Others?"
    
    show emi sad_grin at left
    show rin relaxed_nonchalant
    show lilly basic_smileclosed at right
    with charaenter

    li "Ah, Hanako, Hisao, is that you?"

    ha "Y—yes Lilly. We… brought friends."
    
    show lilly basic_surprised at right
    show emi sad_shy at left
    show rin relaxed_surprised
    with charachange

    emi "Friends?"
    
    rin "Brought?"
    
    show misha perky_confused at offscreenleft
    with None
    
    show bg school_roof at center
    show lilly basic_surprised at offscreenright
    show misha perky_confused at left
    show emi sad_shy at center
    show rin relaxed_surprised at right
    with dissolvecharamove

    mi "Hey, I know you?"
    
    show emi basic_confused
    show rin basic_surprised at right
    with charachange

    $doublespeak (rin,emi,"Who?","Who?")

    mi "Yeah, don't you remember? The art room?"
    
    show emi basic_shock
    show rin basic_deadpan at right
    with charachange
    #Emi embarrassed/ O_O

    rin "I don't think I remember anything like that."

    emi "Don't tell me…"
    
    show misha hips_grin at left
    with charachange

    mi "I knew it! It was kinda dark so…"
    
    show emi excited_sad
    with charachange

    emi "That was a mistake!"

    hi "What's going on here?"
    
    show misha cross_smile at left
    show emi basic_closedsweat
    with charachange
    #Misha ultra happy/ Emi Ultra O_O

    $doublespeak (mi,emi,"It's a secret.", "It's a secret.")
    
    show rin relaxed_doubt at right
    with charachange

    rin "That's twice now, Emi…"
    
    show emi excited_sad
    with charachange

    emi "It was just one time!"
    
    show shizu basic_normal2 at offscreenleft
    with None
    
    show bg school_roof at bgright
    show shizu basic_normal2 at left
    show misha cross_smile at twocenteroff2
    show emi excited_sad at tworight
    show rin relaxed_doubt at right
    with dissolvecharamove

    mi "What was one time?"
    
    show misha perky_smile at twocenteroff2
    with charachange

    mi "Oh, never mind, we just met up once."
    
    show emi sad_shy at tworight
    with charachange

    emi "I was looking for Rin and…"
    
    show rin basic_deadpan at right
    with charachange

    rin "You were looking for me in the art room?"

    hi "I thought you lived in there…"

    ha "You are there a lot of the time."

    li "If I were to search for you, I would look there first."
    
    show rin basic_awayabsent at right
    with charachange

    rin "Huh. I would have looked where I was first."
    
    show misha cross_smile at twocenteroff2
    with charachange

    mi "That makes sense!"
    
    show emi basic_grin at tworight
    with charachange

    emi "Anyway, why are we all here?"
    
    show misha hips_grin at twocenteroff2
    show shizu adjust_happy at left
    with charachange

    mi "Hanako invited us here."
    
    show hanako emb_timid at offscreenright
    show lilly invis at right
    with None
    
    show shizu invis at offscreenleft
    show rin invis at tworight
    show emi invis at center
    show bg school_roof at bgleft
    show misha hips_grin at left
    show lilly basic_surprised at twocenteroff3
    show hanako emb_blushing at right
    with dissolvecharamove

    li "Hanako did?"
    
    show hanako emb_blushtimid at right
    with charachange

    ha "I… I thought we should study together…"
    
    show hanako cover_worry at right
    with charachange
    
    ha "We are in the same class…"
    
    show misha sign_smile at left
    with charachange

    mi "And we have the council room to ourselves."
    
    show lilly basic_ara at twocenteroff3
    with charachange

    li "My my, I don't suppose this is to force you to actually study, is it, Hanako, Hisao?"
    
    show hanako emb_smile at right
    with charachange
    #Hanako Happy blush

    ha "M…maybe."
        
    show bg school_roof at bgright
    show lilly invis at right
    show hanako invis at offscreenright
    show shizu behind_blank at left
    show rin relaxed_doubt at right
    show misha perky_smile at center
    with dissolvecharamove

    rin "You won't study unless you're in the Council Room?"
    
    show rin basic_absent at right
    with charachange

    rin "I guess I have the same rule."

    rin "I have never studied, nor have I been to the Council Room."
    
    show misha cross_smile
    with charachange

    mi "Makes sense."
    
    show shizu basic_frown at left
    with charachange

    shi "…"
    
    show misha perky_confused
    with charachange

    mi "Oh, sorry, it doesn't."
    
    show rin basic_deadpan at right
    with charachange

    rin "You change your mind a lot."

    hi "She's talking for two and thinking for none."
    
    show misha cross_grin
    with charachange

    mi "It's true."
    
    show misha hips_frown
    show shizu adjust_frown at left
    with charachange

    mi "Hey!"

    hi "See?"
    
    show rin relaxed_surprised at right
    with charachange

    rin "Interesting. Who are you?"
    
    show misha sign_smile
    show shizu behind_smile at left
    with charachange

    mi "Shizune."
    
    show misha hips_grin
    with charachange

    mi "And I'm Misha~!"
    
    show rin basic_surprised at right
    with charachange

    rin "Can we be friends?"
    
    show misha perky_smile
    with charachange

    mi "I don't see why not."
    
    show emi invis at tworight
    with None
    
    show bg school_roof at center
    show shizu invis at offscreenleft
    show rin basic_absent at right
    show misha perky_smile at left
    show emi sad_shy at center
    with dissolvecharamove

    emi "Hey… now… be careful."

    hi "Of what?"
    
    show emi basic_hes
    with charachange
    #emi embarrassed

    emi "Nothing!"

    hi "Er, okay."
    
    show bg school_roof at bgleft
    show rin invis at tworight
    show emi basic_grin at twocenteroff2
    show misha perky_smile at left
    show lilly basic_smile at tworight
    show hanako emb_emb at right
    with dissolvecharamove

    li "So, I take it we all will be studying together?"
    
    show hanako emb_timid at right
    with charachange

    ha "W—well, Hisao is good at science, and you're good at music…"
    
    show emi sad_shy at twocenteroff2
    with charachange

    emi "Really? I really really suck at science, can you please teach me?"

    hi "Um, I guess, but…"
    
    show misha cross_smile at left
    with charachange

    mi "Ooh, that's right, Mutou likes you, he's always asking you to explain things."
    
    show hanako basic_worry at right
    with charachange

    ha "Please?"

    hi "I don't really have a choice, do I?"
    
    show lilly basic_oops at tworight
    with charachange

    li "Is the council room big enough for all of us?"
    
    show misha sign_smile at left
    with charachange

    mi "Should be. We can also have a lot of snacks while we study."
    
    show lilly basic_cheerful at tworight
    with charachange

    li "Splendid. Should I bring my tea set?"
    
    show emi basic_happy at twocenteroff2
    with charachange

    emi "You have a tea set?"

    hi "Yeah, a good one too."
    
    show hanako emb_smile at right
    with charachange

    ha "We use it all the time."
    
    show emi basic_confused at twocenteroff2
    show misha perky_confused at left
    with charachange

    emi "Hang on, are you two going out?"

    hi "Yes. Sorry, I didn't send out a memo yet."
    
    show bg school_roof at center
    show rin basic_absent at closeright
    show emi basic_grin at center
    show misha perky_smile at left
    show lilly invis at right
    show hanako invis at offscreenright
    with dissolvecharamove

    rin "Why would you do that?"
    
    show misha cross_grin at left
    with charachange

    mi "Oh, so that's why you two were together."

    hi "You didn't notice?"
    
    show rin basic_deadpanamused at closeright
    with charachange

    rin "She's thinking for none."
    
    show rin negative_spaciness at closeright
    with charachange

    rin "Or is that the other one?"

    "Rin looks thoroughly perplexed, but generally interested by the dual mind of Misha and Shizune."

    "It's the first time I've seen her actually animated in the least."
    
    show lilly invis at right
    with None
    
    show bg school_roof at bgleft
    show misha invis at offscreenleft
    show rin negative_spaciness at twocenteroff2
    show emi basic_grin at left
    show lilly basic_smile at tworight
    show hanako emb_timid at right
    with dissolvecharamove

    li "So, Hakamichi and Shiina…" # "hamakichi", huh... [str]
    
    show emi sad_shy at left
    with charachange

    emi "Who?"

    hi "Shizune and Misha…"
    
    show emi sad_grin at left    
    show rin basic_awayabsent at twocenteroff2
    with charachange

    rin "So that's their names…"
    
    show lilly basic_listen at tworight
    with charachange

    li "…as I was saying, Shizune and Misha will provide the room, Hisao shall provide the tuition, and I shall provide the tea."
    
    show hanako emb_smile at right
    with charachange

    ha "I can make some sandwiches…"

    hi "They're pretty good…"
    
    show lilly basic_smile at tworight
    with charachange

    li "…Hanako can provide the food…"
    
    show emi excited_happy at left
    with charachange

    emi "I can run to the shops and get some snacks really really fast."
    
    show rin relaxed_surprised at twocenteroff2
    with charachange

    rin "I'm not studying, I just want to see Shizukichi and Shii…sha… more."
    
    show rin relaxed_doubt at twocenteroff2
    with charachange

    rin "Shi…chi…shii…sha."
    
    show rin basic_deadpandelight at twocenteroff2
    with charachange

    rin "You sound like a dance."
    
    show bg school_roof at center
    show misha sign_confused at twocenteroff2
    show shizu basic_normal at leftoff
    show rin basic_deadpandelight at tworight
    show emi invis at twoleft
    show lilly basic_oops at rightedge
    show hanako invis at offscreenright
    with dissolvecharamove

    mi "Eh?"

    shi "…"

    "I can see Misha's tireless hands falter as Rin launches into her full “babble” mode."
    
    show lilly basic_cheerful at rightedge
    with charachange

    li "So, it's settled. What time shall we meet, teacher?"
    
    show rin basic_absent at tworight
    show misha perky_smile at twocenteroff2
    show shizu behind_blank at left
    with charachange

    "I am set upon by six pairs of excited eyes, each seemingly more intrigued than the last."

    hi "Um, let's say three o'clock?"
    
    show bg school_roof at bgright
    show misha perky_smile at twoleft
    show shizu basic_normal at leftdoor
    show rin basic_absent at right
    show emi basic_happy at twocenteroff3
    show lilly invis at offscreenright
    with dissolvecharamove

    emi "Three it is! Watch me, I'll be back! Save me a seat!"
    
    show emi basic_grin at tworight
    show rin basic_surprised at right
    with dissolvecharamovefast

    "Emi scoffs the last of her lunch, grabs Rin's sleeve and makes a beeline for the stairwell door."

    rin "Eh? Why am I going? I want to stay with the dancers…"
    
    show emi basic_hes at tworight
    with charachange

    emi "Because I have no mon~ey."
    
    show rin basic_deadpandelight at right
    with charachange

    rin "I shall return, Shichishiisha."
    
    hide rin
    hide emi
    with charaexit
    
    show bg school_roof at center
    show misha perky_confused at twocenteroff2
    show shizu behind_blank at left
    show lilly basic_smile at tworight
    show hanako emb_emb at right
    with dissolvecharamove

    mi "Eh?"

    "Whilst Misha's brain tries to sort through recent proceedings, Hanako spreads out her food on a small blanket."

    "True to her word, she has made far too much for even two people."

    mi "Ooh, you did make a lot. Is it okay?"
    
    show hanako emb_timid at right
    with charachange

    ha "P—please. Help yourself."
    
    show misha cross_grin at twocenteroff2
    with charachange

    mi "I think I will!"
    
    show misha cross_smile at twocenteroff2
    with charachange

    mi "Thank you for the food, Hanako."

    ha "You're welcome."
    
    show misha perky_smile at twocenteroff2
    show shizu behind_smile at left
    with charachange

    mi "Hey, these are good!"

    hi "I told you."
    
    show hanako emb_smile at right
    with charachange

    ha "T—thanks."
    
    show lilly behind_cheerful at tworight
    with charachange

    li "No, thank you, Hanako."
    
    show bg school_roof at bgleft
    show misha perky_smile at twoleft
    show shizu behind_smile at leftoff
    show lilly behind_cheerful at center
    show hanako basic_normal_close at tworight
    with dissolvecharamove

    "Whilst the others are distracted with the food, I lean in close to Hanako."

    hi "Are you sure this is a good idea?"
    
    show hanako basic_worry_close at tworight
    with charachange

    ha "I… I thought it would be better with more people."

    hi "You mean, so we study, instead of… you know…"
    
    show hanako basic_bashful_close at tworight
    with charachange

    #Hanako blush

    ha "S—sorta. But I… I've been in the same class as Shizune and Misha for a while now."

    ha "And they always talk to you in class, so I… I want to talk to them too."

    "I feel a smile creep across my face, and a sideways glance at Lilly confirms that she, too, is grinning."

    "Whilst there is a lot of food, before the might of the five of us, it is gone fairly quickly."
    
    show bg school_roof at center
    show misha perky_smile at twocenteroff2
    show shizu behind_smile at left
    show lilly basic_smile at tworight
    show hanako emb_emb at right
    with dissolvecharamove

    mi "Thank you for that."

    ha "You're welcome."
    
    show misha hips_smile at twocenteroff2
    with charachange

    mi "Well, we have to prepare the council room for this many visitors. If you'll excuse us…"

    hi "Go ahead, I have to go back to my room to get my notes, anyway."

    mi "We'll see you there at three, then."
    
    hide misha
    hide shizu
    with charaexit
    
    show bg school_roof at bgleft
    show lilly basic_smile at twoleft
    show hanako emb_emb at tworight
    with dissolvecharamove

    "Shizune bows slightly, and Misha skips ahead of her, into the stairwell."
    
    show lilly basic_ara at twoleft
    with charachange

    li "My my, that was lively."

    hi "Indeed."
    
    show hanako emb_smile at tworight
    with charachange
    #hanako blush smile

    ha "I… thought it was fun."

    hi "Eh?"

    ha "It was a little busy, but fun."

    hi "I think you're right there."
    
    show lilly basic_smile at twoleft
    with charachange

    li "Are you going to be alright for the study sessions?"

    hi "Sessions?"
    
    show lilly basic_oops at twoleft
    show hanako emb_timid at tworight
    with charachange

    li "Surely we aren't going to all this trouble for one afternoon?"

    "A little piece of me dies inside. Am I going to be stuck teaching six girls for the next two weeks?"

    ha "I… I think I will be fine."

    ha "And it's less of a distraction than… than…"

    show hanako emb_blushtimid at tworight
    show lilly basic_weaksmile at twoleft
    with charachange
    #Hanako super embarrassed

    #Lilly slight blush

    li "Oh, I suppose you are right there."

    hi "Yeah, I suppose we have no choice now."

    hi "It's hard enough getting away with one person watching, let alone five…"
    
    show lilly basic_pout at twoleft
    with charachange

    li "I wasn't watching…"

    hi "Listening, then."
    
    show lilly basic_listen at twoleft
    with charachange

    li "Hisao Nakai, are you, perchance, insinuating that I am some kind of voyeur?"

    hi "No, not at all. But you were…"
    
    play sound sfx_impact
    
    show lilly basic_displeased at twoleft
    with vpunch

    "Lilly swings out in my direction, landing a playful punch on my back."

    "Still, I can't resist hamming it up."

    hi "Hey, ow…"
    
    show lilly basic_planned at twoleft
    with charachange

    li "Be quiet, you. I know that didn't hurt. That wasn't the point."
    
    show hanako emb_smile at tworight
    with charachange
    #Lilly smile, Hanako laugh

    "Lilly's fake seriousness makes Hanako and I laugh, and before long she joins us in laughter."
    
    show lilly basic_smile at twoleft
    with charachange

    li "Come now, that's enough horsing around. How much longer do we have before class?"

    hi "Um, just under an hour."
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "Well then, don't you think that you should prepare?"

    hi "Yeah, you're right. Hanako, do you need a hand?"
    
    show hanako basic_bashful at tworight
    with charachange

    ha "No, I should be fine. I'll see you there."
    
    hide hanako
    hide lilly
    with charaexit
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0

    "I lean over and kiss Hanako before setting off to collect my notes."

    "Just how the hell did I get roped into this?"

    return

label en_HT15:

    scene bg school_council at bgright
    with locationskip
    #bg Student council office.
    #Also Lol directing again.
    play music music_shizune fadein 3.0

    "I enter the student council office, utterly surprised at the changes since the last time I was here."

    "Well, more specifically, the changes that seem to have happened in the past hour."
    
    show shizu behind_smile at tworight
    show misha hips_grin at twoleft
    with charaenter

    mi "Ta-da! What do you think?"

    hi "I'm… amazed. Where did you get…"
    
    show misha hips_smile at twoleft
    with charachange

    mi "Classrooms."

    hi "And the…"

    mi "Staff room."

    "I shake my head at the absurdity of it all."

    "Shizune's desk has been pushed off to one side, and in its place, six classroom desks have been lined up in two rows."

    "Next to the door stands a small blackboard on wheels, fully equipped with chalk, eraser, and wooden ruler."

    show shizu behind_smile at tworight
    show misha hips_grin at twoleft
    with charaenter
    #Misha ultra happy

    mi "Put on the jacket! Do it!"

    hi "Er, okay… but whose is it?"
    
    show shizu adjust_happy at tworight
    with charachange

    shi "…"
    
    show misha cross_smile at twoleft
    with charachange

    mi "Stop asking irrelevant questions."

    mi "When taking on roles such as this, getting the look right is the most important thing."
    
    show misha sign_smile at twoleft
    with charachange

    mi "Besides, if you were to teach us in your uniform, we wouldn't be able to take you seriously!"

    hi "I thought that this was supposed to be a study session?"
    
    show shizu basic_happy at tworight
    with charachange

    shi "…"

    mi "It IS a study session. For us."

    mi "That's right, Hisao. You're going to help us pass!"

    hi "Do I really have to wear the jacket?"
    
    show misha hips_frown at twoleft
    show shizu behind_frown at tworight
    with charachange

    $doublespeak (shi,mi,"…","YES.")

    "Reluctantly, I shrug the jacket onto my shoulders."

    "It smells a little of cigarettes and alcohol."

    "I guess one of our teachers is a fan of the local bars…"
    
    show misha cross_grin at twoleft
    with charachange
    
    stop music fadeout 3.0

    mi "It's perfect, isn't it, Shizu?"
    
    show shizu adjust_smug at tworight
    with charachange

    mi "Indeed. It's as if it were made for you."
    
    li "Is this the right place?"
    
    show lilly cane_smile at offscreenright
    show hanako emb_emb at offscreenright
    with None

    show shizu basic_normal2 at twoleft
    show misha perky_smile at left
    show lilly cane_smile at tworight
    #insert flipped version of Lilly sprite here
    show hanako emb_emb at right
    show bg school_council at center
    with dissolvecharamove
    
    play music music_lilly fadein 0.5

    "Lilly and Hanako appear at the doorway, both carrying armfuls of provisions."

    hi "Yeah, this is it, come on in."

    show hanako basic_bashful at right
    with charachange
    
    ha "Y…you look funny, Hisao."

    hi "Tell them, they're the ones that are making me wear it."
    
    show misha hips_smile at left
    with charachange

    mi "It's perfect, isn't it, Hanako?"

    "The more time I spend with Misha, the more I believe that she would stop functioning if Shizune were to disappear."

    show hanako basic_worry at right
    with charachange
    
    ha "Um… it looks kinda familiar…"

    hi "It's one of the teacher's…"
    
    show hanako def_worry at right
    with charachange
    #Hanako thinking/whimsical/something

    ha "No, not like that."

    ha "Like, from… before."
    
    show lilly cane_concerned at tworight
    with charachange

    "I try to read Hanako's face, but it's impossible."

    "Almost as if she is trying to remember something, but is unsure if she wants to."
    
    stop music fadeout 4.0

    hi "I can take it off if you want…"
    
    show hanako basic_bashful at right
    with charachange

    ha "N—no. It suits you."
    
    show misha cross_laugh at left
    with charachange

    mi "Told you!"
    
    show rin negative_spaciness at offscreenright
    show emi sad_shy at offscreenright
    with None
      
    show misha cross_laugh at offscreenleft
    show shizu basic_normal2 at offscreenleft
    show lilly cane_surprised at left
    show hanako defarms_shock at twoleft
    show emi sad_shy at center
    show rin negative_spaciness at right
    show bg school_council at bgleft
    with dissolveeaseaccel
    play sound sfx_impact
    with vpunch
    
    play music music_emi fadein 0.3

    "Without warning, Hanako lurches forward, nearly dropping the teapot she is carrying."
    
    show emi basic_closedsweat
    with charachange
    
    show emi basic_closedsweat at tworight
    with charamove

    emi "Sorry! I didn't see you there!"
    
    show hanako emb_timid at twoleft
    with charachange

    ha "T—that's okay…"
    
    show rin basic_deadpan at right
    with charachange

    rin "I told you it was too fast."
    
    show emi sad_depressed at tworight
    with charachange
    #Emi Tee-hee/loli tap-self-on-head

    emi "I guess I messed up."
    
    show hanako def_worry at twoleft
    with charachange

    ha "It's alright."

    "Though, in saying that, Hanako makes sure to quickly arrange Lilly's tea set on Shizune's desk."
    
    show emi basic_grin at tworight
    show rin basic_absent at right
    with charachange

    "Following suit, Emi unceremoniously empties her two shopping bags onto the desk, sending boxes of snacks skidding across the table."

    emi "Help yourself, Rin had a bit of money saved up so I went all out!"
    
    show rin basic_deadpanupset at right
    with charachange

    rin "I never said that we should share them…"

    mi "Too late!"
    
    show lilly cane_smile at offscreenleft
    show hanako def_worry at offscreenleft
    show misha sign_smile at center
    show shizu basic_normal2 at left
    show emi sad_grin at offscreenright
    #show emi sad_grin at tworight
    show rin basic_deadpanupset at right
    show bg school_council at center
    with dissolvecharamove

    "Misha opens the box nearest to her, grabs a handful of the chocolate-coated treats, and passes the box to Shizune."

    show rin relaxed_surprised at right
    with charachange
    
    "Rin watches in disbelief."
    
    rin "So, both of you eat?"
    
    show shizu cross_wut at left
    with charachange

    shi "…"
    
    show misha perky_confused
    with charachange

    mi "Of course, what did you expect?"
    
    show rin basic_sad at right
    with charachange

    rin "I… don't know."
    
    stop music fadeout 1.5

    hi "Hey, is this a study session, or are we just going to stand around and eat all afternoon."
    
    show misha sign_smile
    show shizu behind_blank at left
    #show emi sad_shy at tworight
    with charachange

    mi "Sorry teacher! Everyone! To your seats!"
    
    show misha sign_smile at offscreenleft
    show shizu basic_normal2 at offscreenleft
    #show emi sad_shy at offscreenright
    show rin basic_absent at offscreenright
    show bg school_council at bgleft
    with dissolvecharamove
    
    show bg school_council at center
    with charamove

    "The institutionalised part of the girls' brains kicks in, and they shuffle into their seats."
    
    hide hanako
    hide lilly
    hide misha
    hide shizune
    hide emi
    hide rin
    
    play music music_normal fadein 0.3

    hi "Um, thanks Misha."
    
    show misha sign_smile
    with charaenter

    mi "Don't mention it, this is the Class Rep's job."

    hi "You're the Class Rep?"
    
    show misha hips_grin
    with charachange

    mi "No-one else here is qualified!"
    
    show misha hips_smile
    with charachange

    mi "Plus, Shizune makes me say this kind of stuff all the time anyway."

    hi "Right… well…"

    hi "What should we do first?"
    
    show emi excited_happy at offscreenright
    #show rin basic_deadpan at offscreenright
    with None
    
    show misha hips_smile at twoleft
    show emi excited_happy at tworight
    show bg school_council at bgleft
    with charamove

    emi "History!"
    
    show misha perky_smile at twoleft
    with charachange
    
    hi "I thought we were going to do science?"
    
    show emi basic_confused at tworight
    with charachange
    #Emi ???

    emi "I thought History was a science."
    
    show rin basic_deadpan at right
    with charaenter

    rin "History is just the past."

    hi "I guess that's right. Any other suggestions?"
    
    show misha perky_smile at center
    show emi basic_confused at offscreenright
    show rin basic_deadpan at offscreenright
    show bg school_council at center
    with charamove
    
    show misha sign_sad
    with charachange

    mi "I don't get gravity."

    mi "Is it mg or that M&M's thing?"

    hi "M&M's?"
    
    show misha sign_confused
    with charachange
    #Misha confused

    #I should note, I didn't intend to write a 3-page lecture on gravity.
    #Stupid degree.
    #Is it worth keeping? Where should I cut it?

    mi "You know, like gravity was always mg. But now it's MM… something."
    
    show lilly basic_pout at offscreenleft
    with None
    
    show misha sign_confused at tworight
    show lilly basic_pout at twoleft
    show bg school_council at bgright
    with charamove

    li "I believe that Misha is referring to the equation of gravity, where the force is equal to G by M by m on r squared."

    show misha cross_smile at tworight
    with charachange
    
    mi "Yeah, the M&M rule."
    
    show lilly basic_smile at twoleft
    with charachange

    hi "Ah, right. Well, er, the way I remember it is like this."

    "Instinctively, I pick up the chalk and draw two circles on the board."

    "However, due to a lack of experience with chalk, the circles turn out more like blobs."

    hi "Think about two balls in space."
    
    show shizu behind_blank at offscreenright
    with None
    
    show lilly basic_smile at offscreenleft
    show misha cross_smile at twoleft
    show shizu basic_normal2 at tworight
    show bg school_council at center
    with charamove

    shi "…"
    
    show misha perky_confused at twoleft
    show shizu behind_blank at tworight
    with charachange

    mi "Why in space?"

    hi "Well, it's so that we don't have anything else to worry about."
    
    show misha cross_smile at twoleft
    with charachange

    mi "I see."

    hi "Now, what are the things that are going to matter here?"
    
    show misha cross_smile at left
    show shizu behind_blank at center
    show emi basic_confused at right
    show bg school_council at bgleft
    with charamove

    emi "Matter?"

    hi "I mean, what is there that will change the gravity?"
    
    show emi sad_annoyed at right
    show misha perky_confused at left
    with charachange

    "I stare down the barrel of six blank faces."

    "Teaching is hard."

    hi "Um… think of it this way. What do we know about these balls?"
    
    show rin basic_deadpanamused at offscreenright
    with None
    
    show emi sad_annoyed at tworight
    show rin basic_deadpanamused at right
    with charamove

    rin "Neither of them is a ball."

    hi "That's got more to do with my drawing skills, I think."
    
    show emi sad_shy at tworight
    with charachange

    emi "Is it… gravity?"

    hi "Not exactly, that's what we're trying to find."
    
    show hanako emb_timid at offscreenleft
    with None
    
    show emi sad_shy at offscreenright
    show rin basic_deadpanamused at offscreenright
    show shizu behind_blank at offscreenright
    show hanako emb_timid at left
    show lilly basic_surprised at center
    show misha perky_confused at right
    show bg school_council at bgright
    with charamove

    li "The masses of the balls?"

    hi "Bingo."
    
    show lilly basic_smile
    with charachange

    "I draw an M under each blob."
    
    show hanako basic_normal at left
    with charachange

    ha "H—how far apart they are?"

    hi "That's right. Anything else?"
    
    show lilly basic_concerned
    with charachange

    "Once again, blank stares."

    hi "Well, that's actually it, really."

    hi "Now, think about this; if either of the masses gets bigger, would you expect more or less gravity?"
    
    show hanako basic_normal at offscreenleft
    show lilly basic_concerned at offscreenleft
    show misha perky_confused at twoleft
    show shizu behind_blank at tworight
    show bg school_council at center
    with charamove
    
    show misha sign_confused at twoleft
    with charachange

    mi "Le…"
    
    show shizu adjust_frown at tworight
    with charachange

    shi "…"
    
    show misha sign_smile at twoleft
    with charachange

    mi "More."

    hi "Nice save."
    
    show misha cross_grin at twoleft
    show shizu adjust_smug at tworight
    with charachange

    $doublespeak (shi,mi,"…","I'm used to it.")

    hi "And what about the distance. If they get further apart, will there be more or less gravity?"
    
    show shizu adjust_smug at offscreenright
    show hanako basic_normal at twoleft
    show misha cross_smile at tworight
    show bg school_council at bgright
    with charamove

    ha "Less?"

    hi "Right again."
    
    show hanako basic_bashful at twoleft
    with charachange
    
    hi "So now we can put them together. Can anyone guess how?"
    
    show hanako basic_bashful at offscreenleft
    show misha cross_smile at twoleft
    show rin basic_absent at tworight
    show bg school_council at bgleft
    with charamove

    rin "GMm on r squared."

    hi "Uh, right. How did you know?"
    
    show rin basic_deadpanamused at tworight
    with charachange

    rin "She said it before."

    hi "Right. But why is it like this? Why isn't r on the top?"
    
    show rin basic_absent at tworight
    with charachange
    
    show lilly basic_surprised at left
    show misha cross_smile at center
    show rin basic_absent at right
    show bg school_council
    with charamove

    li "Since the force gets less as the distance gets bigger… that means you need to divide, and not multiply?"

    hi "Spot on."

    show lilly basic_cheerful at left
    with charachange
    
    hi "Does that make sense?"
    
    show lilly basic_cheerful at offscreenleft
    show misha cross_smile at twoleft
    show rin basic_absent at tworight
    show bg school_council at bgleft
    with charamove
    
    show misha sign_confused at twoleft
    with charachange

    mi "Then what's G?"

    hi "It's just a constant; something that just keeps everything in line."
    
    show rin relaxed_surprised at tworight
    with charachange

    rin "Like white."
    
    show misha perky_confused at twoleft
    with charachange

    hi "Eh?"
    
    show rin negative_spaciness at tworight
    with charachange

    rin "White doesn't mean much, but it fills in the blanks."
    
    show rin basic_surprised at tworight
    with charachange

    rin "If there was no white, nothing would make sense."
    
    show misha hips_laugh at twoleft
    with charachange

    mi "Oh, I get that!"

    hi "You do?"
    
    show misha hips_grin at twoleft
    with charachange

    mi "Yup. You're so smart, Rin!"
    
    show rin basic_deadpan at tworight
    with charachange

    rin "I can only talk for one person though."

    hi "So, is everyone happy now?"
    
    show rin basic_deadpan at offscreenright
    show hanako emb_timid at twoleft
    show misha hips_grin at tworight
    show bg school_council at bgright
    with charamove

    ha "Um… what is the mg one then?"
    
    show misha perky_confused at tworight
    with charachange
    #Misha confused

    mi "Yeah, why does it change?"

    hi "Well, it doesn't."

    "I draw a circle around part of the gravity equation I've written on the board."

    hi "If you're standing on the earth, then these parts are going to be the same, aren't they?"

    hi "G is a constant, the mass of the earth doesn't change, and the earth is pretty much a sphere, so r is the same everywhere, right?"

    show hanako emb_timid at offscreenleft
    show misha perky_confused at twoleft
    show emi basic_grin at tworight
    show bg school_council at center
    with charamove
    
    emi "Right."

    hi "So, we can work out this part, and it ends up being g."

    hi "And if you multiply that by m, you get the same thing we have here."
    
    show misha sign_smile at twoleft
    with charachange

    mi "Ohhh."

    mi "I can almost remember that."

    hi "Almost?"
    
    show misha perky_sad at twoleft
    with charachange

    mi "I didn't write any of it down."

    "It suddenly occurs to me that Misha never gets the chance to take notes, her hands busy signing the classes directly to Shizune."

    "I feel kind of sorry for her, in a way."

    "Then again, I get the feeling that Shizune's notes would be a lot more legibile and concise, and it's a given that she just copies off those."

    "Their symbiotic relationship never ceases to amaze me."
    
    hide misha
    hide emi
    with charaexit

    "After the girls finish taking down their notes, I erase my scratchings from the board, and ask for the next question."

    "Now that the tone has been set, everyone seems to relax a little, and the questions start coming thick and fast."

    "Electrostatics, stoichiometry, redox…"

    "A full science course in an afternoon."

    "But after each one of my fumbled explanations, I can see a little more understanding in each of the faces before me."
    
    stop music fadeout 4.0

    "And sometimes, just simply saying my thoughts out loud makes it easier to think."

    "It's a lot easier than just reading a textbook."
    
    scene bg school_council_ss
    with shorttimeskip
    
    play music music_daily fadein 1.0

    "We work long into the evening, occasionally passing around boxes of snacks as I write up formula after formula on the small chalkboard."
    
    show bg school_council_ni
    with Dissolvemove(3.0)

    "The sky outside turns dark, and the only thing that stops us is the impending curfew."

    hi "I think we should call it quits there, it's getting late."
    
    show misha cross_smile
    with charaenter

    mi "And we still have to clean up."
    
    show lilly basic_smile at left
    with charaenter

    li "We could all help."
    
    show emi basic_grin at right
    with charaenter

    emi "Yeah, what needs to be done, teacher?"

    "Even though I have no idea where any of this stuff goes, everyone refers to me by the virtue of this assumed position."

    hi "Er, I guess the desks have to go back, and the board."
    
    show shizu invis behind misha at tworight
    show rin invis at offscreenright
    with None
    
    show bg school_council_ni at bgleft
    show lilly invis at offscreenleft
    show misha cross_smile at left
    show shizu behind_blank at twocenteroff2
    show emi basic_grin at tworight
    show rin basic_deadpan at right
    with dissolvecharamove

    rin "And your jacket isn't yours anymore."

    hi "Eh?"
    
    show misha perky_smile at left
    with charachange

    mi "You're still wearing that jacket."

    hi "Oh? Huh, I totally forgot."
    
    show shizu basic_normal at twocenteroff2
    with charachange

    "Shizune extends an arm towards me."

    shi "…"
    
    show misha sign_smile at left
    with charachange

    mi "Here, I'll take it back. I'm the only one with a key to the staff room."
    
    show misha perky_smile at left
    show shizu adjust_happy at twocenteroff2
    with charachange

    mi "The desks go back to 2-3. I'll see you in class tomorrow."

    hi "Ah, thanks."

    "I slide out of the jacket and hang it over Shizune's arm."

    hi "Well then, let's get this stuff back to 2-3."

    emi "Okay!"
    
    hide misha
    hide shizu
    with charaexit
    
    hide rin
    hide emi
    hide lilly
    with charaexit
    
    show bg school_council_ni
    with charamove

    "Shizune and Misha head out to return the jacket, whilst Hanako, Emi and I start carrying the desks back to their classroom."

    "Lilly offers to help, but it is easy enough for the three of us."

    "Rin watches us for a second before skulking after Shizune and Misha, probably to “Uncover their secret” or something equally unbelievable."

    "Having returned the desks, we clean up the last of the snacks, and gather up Lilly's tea set."

    "The four of us leave the room and head back to the dorms."
    
    show bg school_dormext_full_ni
    with locationskip
    #BG night, outside dorms
    
    $ renpy.music.set_volume(0.1,0.0, "ambient")
    play ambient sfx_cicadas fadein 0.3
    
    show lilly basic_smile_ni at left
    show emi basic_grin_ni at center
    show hanako basic_smile_ni at right
    with charaenter

    emi "You were really good in there."

    hi "Um, not really, but thanks…"

    li "No, it is true. You were able to explain things in a simple manner…"
    
    show hanako emb_emb_ni at right
    with charachange

    ha "A…and it was easier than Mutou."
    
    show emi sad_angry_ni
    with charachange

    emi "I know! He always makes things difficult!"
    
    show emi excited_circle_ni
    with charachange

    emi "“Integrate this!” “Differentigrate that!”"
    
    show emi basic_annoyed_ni
    with charachange

    emi "It's impossible…"

    hi "Well, it's not that hard, but he doesn't teach things the easy way."
    
    show lilly basic_surprised_ni at left
    with charachange

    li "Have you ever thought about doing this professionally?"

    hi "What, teaching?"
    
    
    show emi basic_grin_ni
    show lilly basic_planned_ni at left
    with charachange

    li "Yes. You seem to have a knack for it."

    hi "Really?"
    
    show hanako basic_bashful_ni at right
    show lilly basic_smile_ni at left
    with charachange

    ha "You were really good."

    hi "Huh, I've never thought of it."

    hi "It was sorta fun though."
    
    show hanako emb_blushtimid_ni at right
    with charachange
    #Hanako embarrassed

    ha "You… looked good too."

    hi "Well then, maybe I'll have to buy myself a new jacket."
    
    show hanako emb_smile_ni at right
    with charachange
    #Hanako embarrassed smile

    ha "We… should go shopping some time."
    
    show emi excited_amused_ni
    with charachange
    #Emi excited

    emi "Oooh ooh oh! A date! A date!"
    
    show emi excited_joy_ni
    with charachange

    emi "It's a date, right?!"

    hi "Yes."

    extend " And you're not coming."
    
    show emi sad_pout_ni
    with charachange
    #Emi :<

    emi "Aw, but I like going shopping."

    hi "Too bad."
    
    show emi excited_proud_ni
    with charachange

    emi "Next time. You're taking me shopping next time, teach."

    hi "Teach?"
    
    show emi basic_happy_ni
    with charachange

    emi "I like it."
    
    show lilly behind_cheerful_ni at left
    with charachange

    li "It does seem appropriate, especially if we are to study like this on a regular basis."

    hi "Hey, I didn't say anything about this being regular…"
    
    show hanako basic_worry_ni at right
    with charachange

    ha "I think it's too late for that…"

    "At the mention of “late,” I check my watch."
    
    show emi basic_grin_ni
    with charachange

    hi "Crap, it is late, but not that kind of late."

    hi "I better run or I'll miss curfew."
    
    show hanako emb_timid_ni at right
    with charachange

    ha "Oh… I guess you can't stay over every night."
    
    show emi basic_confused_ni
    with charachange
    #Emi confused

    emi "Stay over?"
    
    show lilly basic_pout_ni at left
    show hanako emb_blushing_ni at right
    with charachange

    hi "It's… er… nothing. We just…"
    
    show lilly basic_weaksmile_ni at left
    with charachange

    li "Hisao, Hanako and I were studying late last night, and we accidentally fell asleep."

    show emi sad_shy_ni
    with charachange
    #emi disappointed

    emi "Oh, I thought you meant… something else."

    hi "Hah, what are you talking about? We're high school students…"

    extend " and I really have to go."
    
    show bg school_dormext_full_ni at bgleft
    show hanako basic_bashful_close_ni at tworight
    show lilly basic_smile_ni at leftoff
    show emi sad_shy_ni at twocenteroff2
    with dissolvecharamove
    
    "I give Hanako a quick hug and a kiss, and wave the other girls goodnight."

    ha "Good night, Hisao."
    
    li "Night."
    
    show emi sad_grin_ni at twocenteroff2
    with charachange

    emi "Were you really studying?"
    
    show lilly basic_smileclosed_ni at leftoff
    with charachange

    li "Yes, we were."

    li "Now let's hurry along, we wouldn't want to get caught."
    
    show emi basic_grin_ni at twocenteroff2
    with charachange

    emi "Okay okay. G'night, teach. Thanks for today."

    hi "Don't mention it."
    
    hide lilly
    hide emi
    hide hanako
    with charaexit

    "The girls disappear into the dormitory, closing the door behind them."
    
    stop music fadeout 4.0
    stop ambient fadeout 4.0

    "Well, nothing more for it than to head back to my room."

    "Truth be told, I am beat."

    "I doubt I'll have any trouble getting to sleep tonight."
    
    scene black
    with dissolve

    return
    
label en_HT16:

    #Welcome to my nightmare; the two-week timeskip
    #I hate doing this, but slightly less than how much I hate writing about everyone playing
    #school.

    #also, supersized party scene. 50% larger than most other scenes.
    #Upside, almost done with the path.

    #BG Classroom with fade
    play music music_normal fadein 1.0
    
    scene bg school_scienceroom
    show muto irritated
    with locationchange

    mu "Aaaaand…"

    extend " time."
    
    show muto normal
    with charachange

    mu "Drop your pens and wait in your seats whilst I collect your papers."
    
    hide muto
    with charaexit

    "Mutou ambles along between the desks, students passing their papers to him like offerings to some prophet."

    "After two weeks of relentless testing, it seems that he has the optimum pattern worked out, and manages to collect all the papers with only one pass of the classroom."

    "He drops the large stack of papers on his desk, making a hefty “thump.”"
    
    show muto smile
    with charaenter

    mu "That's it. I'll see you all after the summer break."

    "The class erupts in celebration. With the last exam done, there is nothing between us and four weeks of vacation."

    #I'm pretty sure that the summer vacation is only 4 weeks long in Japan.
    
    hide muto
    with charaexit

    "In the fray of limbs and bodies of our class, two figures approach me."
    
    show misha perky_smile at twoleft
    show shizu behind_smile at tworight
    with charaenter
    #Show misha/Shizune happy

    mi "Um, Hisao, we wanted to say thanks."

    hi "Really? I take it the study sessions helped?"
    
    show misha hips_laugh at twoleft
    with charachange

    mi "Yup yup yup! I don't think I've ever done so well on a science test."
    
    show misha hips_grin at twoleft
    with charachange

    mi "I might even pass first time!"

    hi "Well, it was fun for me too. I think I aced that last one."
    
    show shizu adjust_blush at tworight
    with charachange
    #Shizune blush

    shi "…"
    
    show misha sign_smile at twoleft
    with charachange

    mi "Oh, and Shizune wants to say thanks too."
    
    show misha perky_smile at twoleft    
    show shizu adjust_happy at tworight
    with charachange

    mi "It's hard for her to admit that kind of thing, but you really helped her."
    
    show hanako invis at offscreenright
    with None
    
    show bg school_scienceroom at bgleft
    show misha perky_smile at left    
    show shizu adjust_happy at center
    show hanako cover_smile at right
    with dissolvecharamove

    #show Hanako generic (not embarrassed)

    ha "Hello Misha, Shizune."
    
    show misha hips_smile at left 
    show shizu basic_normal
    with charachange

    mi "Hana! Good timing! How did you do?"

    ha "A—alright I think. What about you?"

    #Misha semi lols?
    
    show misha cross_grin at left 
    with charachange

    mi "Awesome! Everyone's going to pass this time, for sure!"
    
    show hanako basic_smile at right
    with charachange
    #Hanako relieved

    ha "That's good."
    
    show shizu behind_smile
    with charachange
    #Shizune Oh!

    shi "…"
    
    show misha perky_smile at left 
    with charachange

    mi "Oh! That's right!"
    
    show misha sign_smile at left 
    show shizu basic_happy
    with charachange

    mi "The Student Council is going to be having a meeting tonight, and they would like to invite you…"

    hi "Er, you mean you and Shizune are…"
    
    play sound sfx_impact
    
    show misha cross_laugh at left
    show shizu basic_normal
    show hanako basic_normal at right
    with vpunch

    "A swift pain in my chest stops me from continuing."

    "It appears to be caused by an acute case of Misha's Elbow Syndrome."

    #Misha Lols

    mi "Whahaha, of course it's not just us!"
    
    show misha cross_smile at left
    show shizu adjust_happy
    with charachange

    mi "You can only spend council funds on official business!"

    mi "Holding a party and inviting your friends is strictly forbidden!"

    hi "I get it. It's just a meeting then, right?"
    
    show shizu behind_smile
    show misha perky_smile at left
    with charachange

    mi "Right!"

    hi "And I take it that there will be refreshments at this meeting, right?"
    
    show misha hips_smile at left
    with charachange

    mi "Right!"

    hi "And possibly something to entertain us if we have to take some time to ponder a decision, right?"
    
    show misha hips_grin at left
    with charachange

    mi "Right!"

    hi "So then, what is the order of business for this meeting?"
    
    show misha perky_confused at left
    with charachange
    #misha ???

    mi "Eh?"
    
    show shizu basic_sparkle
    with charachange

    shi "…"
    
    show misha sign_smile at left
    with charachange

    mi "Oh, that's right."
    
    show shizu adjust_smug behind misha
    show misha perky_smile at left
    with charachange

    mi "It will be “A debrief on the advantages of peer tutoring as a study aide.”"
    
    show shizu adjust_happy behind misha
    show misha cross_grin at left
    with charachange

    mi "Shizune is really good at thinking up titles like that."
    
    show hanako cover_worry at right
    with charachange

    ha "Who's going to be there?"
    
    show shizu behind_smile
    with charachange

    shi "…"
    
    show misha cross_smile at left
    with charachange

    mi "Everyone that participated in the trial. It is the only way to get definitive results."
    
    show shizu basic_happy
    with charachange

    mi "I would expect that we will be discussing the outcomes well into the night, so I have had curfew waived for us."
    
    show misha perky_confused at left
    with charachange

    mi "You did?"
    
    show shizu behind_smile
    with charachange

    mi "I deemed it necessary."

    hi "Is that even allowed?"
    
    show misha perky_smile at left
    show shizu adjust_smug
    with charachange

    mi "I allowed it, ergo it is allowed."

    hi "That makes perfect sense."
    
    show shizu adjust_happy
    with charachange

    mi "Logic is one of mankind's greatest achievements."
    
    show hanako basic_worry at right
    with charachange

    ha "Have you told the others?"
    
    show misha sign_smile at left
    show shizu behind_smile
    with charachange

    mi "We invited everyone else yesterday. They finished their tests before us."
    
    show hanako emb_timid at right
    with charachange
    #hanako concerned

    ha "Even Lilly?"
    
    show misha cross_smile at left
    with charachange

    mi "Of course."

    hi "Why? Has something happened with Lilly?"
    
    show hanako cover_worry at right
    with charachange

    ha "No, it's not that, it's just…"
    
    show hanako emb_timid at right
    with charachange
    
    stop music fadeout 4.0
    
    ha "Well, never mind."

    hi "Are you sure?"
    
    show hanako basic_normal at right
    with charachange

    ha "Yes, it's nothing."

    ha "I doubt she would do anything…"
    
    scene bg school_council at bgleft
    show lilly basic_smile
    with shorttimeskip
    
    play music music_shizune fadein 1.0

    #BG Councilroom (direct cut)

    li "Welcome! I took the liberty of preparing for the meeting!"
    
    show bg school_council at center
    show lilly basic_smile at tworight
    with dissolvecharamove

    "Once again the council room has been completely transformed."

    "Plates of snacks and cans of drinks cover practically every table surface."

    "Music plays from a small stereo at the back of the room, where Emi and Rin appear to be fighting over the next song to play."

    "Towards the centre of the room, surrounded by a wall of cups, sits a large bowl of red liquid."

    "Little chunks of fruit and ice cubes bob up and down on the surface, as if a ship made of tinned fruit ran into an ice floe."

    "Even from the door I can smell its sickly sweet scent."
    
    show hanako def_worry at twoleft
    with charaenter

    #Hanako shocked/worried

    ha "Uh-oh."

    hi "Uh-oh?"

    hi "Is this what you were worried about?"
    
    show hanako emb_timid at twoleft
    with charachange

    "Hanako simply nods, and hugs my arm in fear."
    
    show shizu invis at offscreenright
    show misha invis at rightedge
    with None
    
    show bg school_council at bgright
    show hanako emb_timid at left
    show lilly basic_smile at twocenteroff
    show misha hips_grin at twocenteroff3
    show shizu behind_smile at right
    with dissolvecharamove

    mi "It looks like everyone is here!"
    
    show lilly basic_cheerful at twocenteroff
    with charachange

    li "Ah, Shizune, Misha, welcome! How were your exams?"
    
    show misha cross_smile at twocenteroff3
    with charachange

    mi "Good good good! And you?"
    
    show lilly basic_ara at twocenteroff
    with charachange

    li "I believe that I did quite well. Hisao's a good teacher, isn't he?"

    hi "Well, I didn't…"
    
    show hanako emb_emb at left
    show lilly basic_smile at twocenteroff
    show misha perky_smile at twocenteroff3
    show shizu basic_happy at right
    with charachange

    li "A toast, to Hisao!"

    "Emi and Rin jump up at these words like servants."

    "Only now do I see the half-empty glasses of punch where they were squabbling."

    "Emi quickly ladles out five more glasses of the red punch, and passes them to us."

    emi "To Hisao!"

    hi "Cheers!"
    
    show hanako basic_smile at left
    show lilly basic_planned at twocenteroff
    show misha cross_smile at twocenteroff3
    show shizu behind_smile at right
    with charachange

    "With the exception of Rin, we all lift our glasses in salute."

    "Then, as one, we empty the glasses."
    
    show lilly basic_smile at twocenteroff
    show hanako emb_downtimid at left
    show shizu cross_stunned at right
    show misha perky_confused at twocenteroff3
    with charachange

    "Shizune and Misha nearly turn green."

    #shizune angry, misha confused

    mi "What's in this?"
    
    show hanako emb_timid at left
    with charachange

    ha "It's as I feared…"
    
    show shizu behind_blank at right
    with charachange

    "Realization dawns…"

    hi "Lilly, did you make this punch?"
    
    show lilly behind_cheerful at twocenteroff
    with charachange

    li "Oh, do you like it? It's a family recipe."
    
    show hanako basic_worry at left
    with charachange

    ha "This is that punch again, isn't it?"
    
    show lilly basic_weaksmile at twocenteroff
    with charachange

    li "Yes, that's right, Hanako. I thought that this was a celebration, so I prepared enough for all of us…"

    extend " hic"

    hi "“hic?” Lilly, do you have the hiccups?"
    
    show lilly basic_pout at twocenteroff
    with charachange

    li "…hic…"
    
    show lilly basic_oops at twocenteroff
    with charachange

    li "No."
    
    show rin invis at offscreenleft
    with None
    
    show bg school_council at bgright
    show hanako emb_timid at twocenteroff3
    show lilly basic_oops at right
    show misha invis at rightedge
    show shizu invis at offscreenright
    show rin basic_absent at closeleft2
    with dissolvecharamove

    "I don't think that I'll be getting any straight answers out of her, so I turn to Hanako."

    hi "So, just what's in this stuff?"
    
    show hanako emb_blushtimid
    with charachange

    ha "Um, I don't know, but it is pretty strong."

    hi "Oh dear."

    hi "We're in for another birthday party, are we?"

    mi "Birthday party?"

    hi "It's nothing."
    
    show rin relaxed_nonchalant at closeleft2
    with charachange

    rin "I have a birthday, but not with a party. Does that count?"

    hi "No, I was talking about Lilly's…"
    
    show bg school_council at bgleft
    show rin invis at offscreenleft
    show hanako emb_timid at left
    show lilly basic_oops at twocenteroff
    show misha perky_confused at twocenteroff3
    show shizu behind_frown at right
    with dissolvecharamove

    shi "…"
    
    show misha sign_smile at twocenteroff3
    with charachange

    mi "Would you perhaps be referring to the incident where that lecherous woman was seen leaving your dorm room?"
    
    show lilly basic_listen at twocenteroff
    with charachange

    hi "Well…"

    extend " yes."
    
    show shizu behind_blank at right
    with charachange

    "Shizune stops to ponder this for a second."
    
    show shizu adjust_happy at right
    show misha cross_smile at twocenteroff3
    with charachange
    
    stop music fadeout 5.0

    mi "If that is the case, then I would like another glass, please."

    emi "Coming right up!"
    
    show misha hips_grin at twocenteroff3
    with charachange

    mi "Me too!"
    
    scene bg school_council_ni at bgleft
    with shorttimeskip
    
    play music music_ease fadein 1.0

    "It doesn't take us long at all to finish the bowl of punch and start moving onto the other drinks that Lilly has provided."

    "The hardest hit seem to be Emi and Rin."

    "It started when Rin stopped being able to hold the cups between her feet."

    "Emi, not wanting her to miss out on the “fun,” started feeding the drinks to her."

    "And, using the excuse that she was now drinking for two, Emi was the first to refill her cups every time."

    "Before long, the two of them were in a hyperactive state; jumping around, singing along with the music, and generally making a mess of the place."

    "Shizune, on the other hand, seemed to lighten up; a girlish blush rising to her cheeks as the alcohol started to take effect."

    "Misha simply grinned like an idiot the whole time."

    "Most of the time she managed to translate for Shizune, but occasionally she seemed to get distracted by watching Rin and Emi horse around."

    "Before long, Shizune stopped bothering with her, and somehow managed to organise a drinking contest with Hanako."

    "Shortly after that, both of them lay, passed out, in the corner."

    "In a way, it was kind of cute to see the two of them practically hugging each other in their sleep."

    "However, I was not the only one to notice this."
    
    show misha hips_grin
    with charaenter

    mi "Aw, doesn't that just warm your heart?"

    hi "Eh?"
    
    show misha perky_smile
    with charachange

    mi "Those two."
    
    show misha sign_smile
    with charachange

    mi "Don't you find it nice that the two girls who hardly ever speak to anyone are now bestest friends?"

    hi "I… guess…"
    
    show misha hips_grin
    with charachange
    #Misha lol

    mi "Or were you thinking dirty things?"

    hi "What?! No!"
    
    show misha cross_laugh
    with charachange
    
    mi "Whahaha, it's okay, Hisao."
    
    show misha cross_smile
    with charachange

    mi "We all know about you and Hana…"

    hi "What? How?"
    
    show misha hips_grin
    with charachange

    mi "So you HAVE been doing dirty things!"

    "Part of my wants to argue, but the alcohol in my system lessens my will to fight."

    hi "Yeah, just a bit. But not so much during the exams."
    
    show lilly invis at left
    with None
    
    li "Thankfully. It was hard to sleep when you are… well…"
    
    show bg school_council_ni at center
    show lilly basic_weaksmile at twoleft
    show misha perky_smile at tworight
    with dissolvecharamove

    "Lilly stumbles towards Misha and I, tearing herself away from Rin and Emi, who seem to be trying to attach one of Emi's legs to Rin's shoulder."
    
    show misha cross_laugh at tworight
    with charachange

    mi "Oh ho ho! So you like an audience!"
    
    show lilly basic_emb at twoleft
    with charachange

    hi "It's not like that! We just… just…"
    
    play sound sfx_impact
    
    show misha hips_grin at tworight
    with vpunch

    "Misha pats me on the back, nearly knocking the wind out of me."

    mi "Way to go Hisao! What a man! If only every girl should be so lucky!"

    hi "Um, thanks."
    
    show lilly basic_smile at twoleft
    show misha perky_smile at tworight
    with charachange

    mi "So, what's your plans for the holidays?"

    hi "Well, Hanako doesn't have anywhere to go, so we were going to stay at my parent's house for a bit…"
    
    show lilly basic_oops at twoleft
    with charachange

    li "Isn't it a little soon to be introducing her to your parents?"
    
    show misha hips_smile at tworight
    with charachange

    mi "Or a little late, if you know what I mean?"

    hi "No, what do you mean?"
    
    show misha sign_confused at tworight
    with charachange
    #Misha, confused

    mi "Um, “No sex before marriage?”"

    hi "What's that got to do with anything?"
    
    show misha perky_confused at tworight
    with charachange

    mi "I don't know, you're the one introducing her to your parents."
    
    show misha perky_smile at tworight
    show lilly basic_smile at twoleft
    with charachange

    li "How did you explain it to them?"

    hi "I asked them after the first week of exams."
    
    show lilly basic_pout at twoleft
    with charachange

    li "Oh, you mean after that Saturday night?"

    hi "Ah… yeah…"

    hi "You knew?"
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "Hisao, I'm afraid there probably wasn't anyone in the dorm that didn't know…"

    hi "Damn, we tried to be quiet."
    
    show lilly basic_emb at twoleft
    with charachange
    #Lilly Embarrassed

    li "You don't have to be…"

    hi "What?"
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "Nevermind."
    
    show lilly basic_smile at twoleft
    with charachange

    li "Isn't it interesting that all of this was Hanako's idea?"

    "However curious I may be, I have never known Lilly to force a topic change this quickly, so I let her slip of the tongue slide."

    hi "What do you mean?"
    
    show lilly basic_planned at twoleft
    with charachange

    li "This whole study group thing."

    li "I would have never have thought to invite this many people."
    
    stop music fadeout 5.0
    
    show misha perky_confused at tworight
    with charachange

    mi "Maybe she just didn't want to be alone?"
    
    show lilly basic_concerned at twoleft
    with charachange

    #I'm not sure about the next bit. Maybe too much "baseball"-ness.
    #There will definitely be mention of the abuse in the "real" path.
    #But this might explain it better… maybe

    hi "What makes you think that?"
    
    show misha perky_sad at tworight
    with charachange

    mi "Well, she never used to talk to anyone, so we all thought she was shy."

    mi "Maybe she was just afraid?"
    
    show lilly basic_surprised at twoleft
    with charachange

    li "Afraid of what?"

    mi "Maybe of us?"

    hi "That doesn't make any sense…"
    
    show lilly basic_listen at twoleft
    with charachange

    li "Maybe it does…"

    hi "What do you mean?"
    
    show lilly basic_oops at twoleft
    with charachange

    li "What if she wanted to have friends, but just never had any?"
    
    show misha perky_confused at tworight
    with charachange

    "Misha screws up her face a little, as if thinking."

    "It's strange. I'm having trouble concentrating on one spot, yet Misha, with the same alcohol content, is thinking straighter than ever."
    
    show misha sign_confused at tworight
    with charachange

    mi "That's not it. If you've never made friends, then you try to."

    mi "You know, like those nerdy kids that always hang around the cool kids, trying to get attention."
    
    show lilly basic_concerned at twoleft
    with charachange

    li "Then what do you think?"
    
    play music music_rain fadein 4.0
    
    show misha perky_sad at tworight
    with charachange

    mi "What if she was abused?"

    hi "What do you mean, abused?"

    mi "Like… you know…"

    mi "THAT kind of abused…"

    hi "What? No…"
    
    show lilly basic_oops at twoleft
    with charachange

    li "If she were abused like that then she would hate men, wouldn't she?"
    
    show misha cross_frown at tworight
    with charachange

    "Misha shakes her head."

    mi "Step daddies aren't the only people that touch their daughters."
    
    show lilly basic_surprised at twoleft
    with charachange

    $ doublespeak(hi,li,"What?","What?")
    
    show misha sign_sad at tworight
    with charachange

    mi "I'm just thinking, what if it was her step mother?"

    "I open my mouth to respond, but I can't find the words to rebut Misha's claims."
    
    show lilly basic_concerned at twoleft
    with charachange

    li "She did seem to take some time to warm up to me…"

    hi "What? No, that can't be right. She'd of told me…"
    
    show misha perky_sad at tworight
    with charachange

    mi "Really? You've known her two months, there's no time to tell you everything."

    #Actually, I kinda do like this way.
    #Stay tuned for the end of the path, wherein Hisao forces Hanako to go to her old house.

    "Emotions and alcohol turn my head into a spinning jumble of thoughts."

    "Some of what Misha is saying is making sense, but it's just so unbelievable."

    "Hanako truly is a lot more cautious with people than you'd expect."

    "But she seemed to open up to me almost straight away; even Lilly said that when we first met."

    "No matter how much I think about it, it still seems like I'm missing a piece of the puzzle."
    
    stop music fadeout 3.0

    "The fire, this alleged abuse… I just can't wrap my head around it."
    
    play sound sfx_impact2
    with vpunch

    "A crash behind me distracts my thinking."

    emi "Sorry, I thought I did it up right…"

    mi "Oh, are you alright?"
    
    show emi invis at leftsit
    with None
    
    show bg school_council_ni at bgright
    show lilly invis at center
    show misha perky_confused at center
    show emi sad_shy at leftsit
    with dissolvecharamovefast
    
    show emi sad_shy at left
    with charamove

    "Misha runs to Emi's side, and helps her onto a nearby chair."
    
    show emi basic_closedsweat at left
    with charachange

    emi "He he, thanks."
    
    show misha hips_smile at center
    with charachange

    mi "It's okay. Here, let me get that for you…"
    
    show misha perky_smile at tworight
    with dissolvecharamove
    
    show emi basic_grin at twoleft
    with dissolvecharamove
    
    play music music_emi fadein 6.0

    "Misha retrieves Emi's leg from the floor and starts strapping it on."

    hi "Huh, looks like you've done that before…"
    
    show emi sad_shyblush at twoleft
    with charachange
    #emi embarrassed.
    #Also, Apologies to Hive and Atwo.

    emi "Well, it was just once."

    hi "What was just once?"
    
    show misha cross_grin at tworight
    with charachange

    mi "Oh, nothing. I just helped Emi here once. No biggie."
    
    show emi basic_hes at twoleft
    with charachange

    emi "Um, about that… story you were telling me in the art room…"

    extend " Could you maybe… tell me how it ends?"
    
    show misha perky_confused at tworight
    with charachange

    mi "Story?"
    
    show emi sad_annoyed at twoleft
    with charachange
    #Emi irritating
    
    emi "You know… that story…"
    
    emi "From that time…"
    
    show misha hips_grin at tworight
    with charachange
    #Misha surprised/realisation

    mi "Oh!"
    
    show misha sign_smile at tworight
    with charachange

    mi "Well, I… I suppose."
    
    show emi sad_grin at twoleft
    with charachange

    emi "I already went and checked out the art room, it's unlocked…"
    
    show misha perky_confused at tworight
    with charachange

    mi "What about… oh…"

    "Misha peers over Emi's shoulder, and I follow her gaze."

    "Rin is curled up under a table, fast asleep."

    mi "Well, are you sure?"

    show emi basic_hes at twoleft
    with charachange
    #Emi hesitant

    emi "I… think it's a good thing to learn."
    
    show misha perky_smile at tworight
    with charachange

    mi "Okay then, shall we go check it out?"

    hi "Um, where are you two going?"
    
    show emi basic_closedgrin at twoleft
    show misha cross_grin at tworight
    with charachange

    mi "That's a secret."

    "Misha winks at me, further confusing me."
    
    show misha cross_smile at tworight
    with charachange

    mi "One day, I might teach you too, Hisao."
    
    stop music fadeout 4.0
    
    hide misha
    hide emi
    with charaexit

    "Misha and Emi disappear into the dark of the hallway, and their footsteps fade off into the distance."
    
    show lilly invis at tworight
    with None
    
    show bg school_council_ni
    show lilly basic_weaksmile at center
    with dissolvecharamove

    li "And then there were two…"

    hi "Yes, I guess things are coming to an end here."

    hi "I guess I'll start cleaning up."

    "I roll up my sleeves and start collecting the piles of cans and empty bags that litter the room."
    
    show lilly basic_listen
    with charachange

    li "About… what we were discussing earlier…"

    hi "Yes?"
    
    show lilly basic_concerned
    with charachange

    li "Do you really think… that Hanako was treated like that?"

    hi "Honestly, I don't know."
    
    show lilly basic_sad
    with charachange
    #Lilly sad
    
    play music music_moonlight fadein 4.0

    li "I've known here the whole time she's been here…"

    li "I tried to care for her, the help her make friends…"
    
    show lilly basic_oops
    with charachange

    li "Was I doing the wrong thing?"

    li "You two were only able to get together once I stopped meddling…"

    hi "Meddling?"
    
    show lilly basic_displeased
    with charachange

    "Lilly flails her arms a little in frustration."

    "It's unnerving to see her so distressed."
    
    show lilly behind_displeased
    with charachange

    li "I…"

    extend " tried to hook the two of you up."

    li "It was stupid of me, I know, but making her happy made me happy."
    
    show lilly basic_reminisce
    with charachange

    li "So after she first started talking to you I tried to force you together."

    li "But it didn't work, and then, and then…"

    show lilly basic_oops
    with charachange
    #It would be so easy to chuck a pityfuck here
    #but I won't

    li "And then I got sick, and you got together after that."

    li "Am I not needed?"

    li "Have I been nothing but a burden this whole time?"

    "Tears flow down Lilly's cheeks as she spirals deeper down into self-pity."

    "I guess drinking probably isn't the best prelude to this kind of conversation."
    
    show lilly basic_concerned_close
    with charachange

    "I wrap my shoulders around Lilly's, and she cries into my chest."

    hi "It's not like that."

    hi "You're Hanako's best friend, anyone can see that."

    hi "Sometimes I think she might love you more than me."

    hi "What Misha said tonight is just a theory."

    hi "And besides, even if it was true, you're not Hanako's step mother."

    hi "You'd never do anything to hurt her, right?"
    
    show lilly basic_pout_close
    with charachange

    li "Right."

    hi "Then there's nothing to worry about, right?"
    
    show lilly basic_reminisce_close
    with charachange

    li "Right."

    hi "Well then, let's get this place cleaned up."

    hi "Hanako and I leave tomorrow morning for my parent's house, and I'd feel guilty leaving this mess."
    
    show lilly basic_listen_close
    with charachange

    li "Okay…"
    
    stop music fadeout 6.0
    
    show lilly basic_sad
    with charachange

    "Lilly peels herself from me, and starts groping around the nearest table, arranging things as best she can."

    hi "Are you going to be alright?"
    
    show lilly basic_weaksmile
    with charachange
    li "Oh, I can work out which ones are empty and which aren't…"

    hi "I mean over the break, without us?"
    
    show lilly basic_smile
    with charachange
    #Lilly smile

    li "Of course, I already have plans."

    li "My elder sister is in the country, so we are going to our summer house in Hokkaido."

    #Something just occurred to me. Wouldn't a home in Hokkaido be a *winter* house?
    #Oosaka, Fukuoka or Okinawa are more summer destinations, right?

    hi "Sounds fun."
    
    show lilly basic_planned
    with charachange

    li "Indeed it is. I shall have to invite you some time."

    hi "I'd be delighted. Maybe next break?"
    
    show lilly basic_smile
    with charachange

    li "Maybe."

    "Before long, we've cleaned up the majority of the mess."
    
    play music music_daily fadein 6.0

    "As if woken by some magical spell, the three sleeping girls stir."
    
    show hanako emb_timid at closeright
    show rin basic_absent at closeleft2
    with charaenter

    ha "W…what happened?"

    hi "You passed out, again."
    
    show hanako emb_downtimid at closeright
    with charachange

    ha "Oh… sorry."

    hi "It's okay."
    
    show hanako basic_worry at closeright
    with charachange

    ha "Who cleaned up?"

    hi "Lilly and I."
    
    show rin basic_deadpanamused at closeleft2
    with charachange

    rin "I supervised."
    
    show hanako basic_normal at closeright
    show lilly basic_pout
    with charachange

    hi "You were awake?"
    
    show rin basic_deadpansurprised at closeleft2
    with charachange

    rin "Yes, but you were doing a good job so I felt compelled to stay out of your way."
    
    show rin relaxed_doubt at closeleft2
    with charachange

    rin "Where's Emi?"

    hi "Oh, Misha wanted to show her something, or something like that."
    
    show rin basic_awayabsent at closeleft2
    with charachange

    rin "Oh well. I really wanted those arms."
    
    show hanako cover_worry at closeright
    with charachange

    ha "Arms?"
    
    show rin basic_absent at closeleft2
    with charachange

    rin "Emi's magical mechanical legs."

    rin "We almost got them to fit, too."
    
    show hanako emb_timid at closeright
    with charachange
    #Hanako puzzled.

    ha "I have no idea what she's talking about."

    hi "It's a long story, I'll tell you on the train tomorrow."
    
    show hanako cover_distant at closeright
    with charachange

    ha "Oh, that's right, the train…"
    
    show shizu invis at offscreenright
    with None
    
    show bg school_council_ni at bgleft
    show rin basic_absent at left
    show lilly basic_pout at twoleft
    show hanako cover_distant at center
    show shizu behind_blank at right
    with dissolvecharamove

    shi "…"

    "Crap. This whole time, Shizune has been standing there, watching our conversation."

    "But, without Misha, there's no way to talk to her."

    "And the party has decimated any method of writing things down."
    
    show shizu basic_normal at right
    with charachange
    
    with Pause(0.2)
    
    show shizu behind_smile at right
    with charachange
    
    show shizu invis at offscreenright
    with dissolvecharamove

    "After fruitlessly trying to sign something to us (I'm sure she assumed it was easy enough to understand), Shizune simply smiles, bows, and leaves."

    hide shizu
    with None
    
    show bg school_council_ni at center
    show rin basic_absent at closeleft2
    show lilly basic_smile at center
    show hanako cover_distant at closeright
    with dissolvecharamove
    
    hi "I guess that was a thank you."
    
    show rin basic_deadpanamused at closeleft2
    with charachange

    rin "She may have offered a challenge."
    
    show lilly basic_oops
    show hanako emb_timid at closeright
    with charachange

    hi "What?"
    
    show rin basic_awayabsent at closeleft2
    with charachange

    rin "You never know."
    
    show rin relaxed_sleepy at closeleft2
    with charachange

    rin "I am sleepy goodnight."
    
    show rin invis at offscreenleft
    with dissolvecharamove

    "Rin pivots on her heels, leans forward, then marches out of the council office."
    
    hide rin
    with None
    
    show bg school_council_ni at bgleft
    show lilly basic_smile at twoleft
    show hanako emb_downtimid at tworight
    with dissolvecharamove

    hi "Well then, I guess we should get some sleep now."
    
    show hanako emb_smile at tworight
    with charachange

    ha "Hmm."

    ha "You know, I was just asleep then…"
    
    show hanako emb_smile_close at twocenteroff3
    with charachange

    "Hanako advances on me, and grabs my shirt."
    
    show lilly basic_weaksmile at twoleft
    with charachange

    li "Perhaps I should leave you two alone?"

    hi "D…don't you need a hand back to your room?"
    
    show lilly behind_cheerful at twoleft
    with charachange

    li "I have my cane, I should be able to find my own way back."
    
    show hanako basic_smile_close at twocenteroff3
    with charachange

    ha "I've moved my bags for tomorrow into your room already, Hisao."

    hi "You did? When?"

    ha "Before the exams."

    hi "Oh, right…"
    
    show hanako basic_bashful_close at twocenteroff3
    with charachange

    ha "Well then, what are we waiting for?"
    
    show lilly basic_smile at twoleft
    with charachange

    li "Don't let me hold you…"

    hi "Um, okay…"

    hi "Thanks for the punch, Lilly."
    
    show lilly basic_ara at twoleft
    with charachange

    li "Don't mention it."
    
    stop music fadeout 3.0

    "With that, Hanako practically drags me by the shirt all the way back to my room."
    
    scene black
    with dissolve

    return

label en_HT17:

    #This may end up being the last scene in the True arc.
    #Can't say for sure, depends on how wordy I get in the train.
    #Also, if the "chat" at Hanako's old house is going to be conclusive enough.
    #Anyway, a conclusion is what I am aiming for.
    #Also, the "Playlist" name for this sence would be "I'm Here".
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    
    play ambient sfx_trainint fadein 2.0
    
    scene bg city_trainscenery
    show train_scenery 
    show train_scenery_fg
    show evfg hisao_trainride at Motion(trainwave, 4.0, repeat=True, bounce=True)
    with locationchange
    #BG Train window.
    
    "Hanako's head rests against my shoulder as the train gently rocks from side to side."

    "After last night's party, both of us are feeling a little under the weather."

    "My mouth feels dirty and dry, and every gentle roll of the train feels like a sledgehammer to my temples."

    "I reach into my pocket, pull out yet another pain killer, and swallow it with a gulp of iced tea."
    
    play sound sfx_trainchime

    "The train lurches a little as it starts to decelerate, and a pre-recorded voice happily chimes over the speakers."

    #I'm not sure about the direct reference here, but I guess that all of the "Tokyo"s can be
    #removed easily.

    "PA" "This train will soon reach its final destination, Tokyo Station."

    "PA" "Please make sure you take all of your belongings with you."

    "I nudge Hanako a little to wake her up."

    #Show Hanako tired

    hi "Hey, Hanako, we're almost here."

    ha "Another five minutes…"

    hi "I don't think that's allowed here."

    "Hanako rubs her eyes, and starts to remember where she is."

    ha "We're here already?"

    hi "You've been asleep for about two hours…"

    ha "Oh… sorry."

    hi "How are you feeling?"

    ha "Better. My headache has gone, I'm just a little tired."

    "No matter how much you like someone, just the slightest amount of pain can make you despise them."
    
    stop ambient fadeout 3.0

    hi "Good for you. Come on, I'll help you with your bags."
        
    #"The train slows to a stop and the doors slide open."
    
    show city_tokyostation at bgright
    show crowd
    with shorttimeskip
    
    hide train_scenery
    hide train_scenery_fg
    hide evfg hisao_trainride
    hide city_tokyostation
    show bg city_tokyostation at bgright
    with None
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    play ambient sfx_crowd_outdoors fadein 0.5

    "Before us lies the complex maze of platforms and escalators of Tokyo Station."

    "Swarms of people move around in pre-determined patterns like ants."
    
    show hanako emb_timid_cas
    with charaenter
    #Hanako concerned

    hi "Are you going to be okay with this?"
    
    ha "I… I'll be fine."

    "Hanako clutches the handle of her bag with both hands, her fingers white with the strain."

    hi "Here, let me take that."
    
    show hanako def_worry_cas
    with charachange

    ha "Eh?"

    "I reach out and try to take her bag from her."

    ha "It's okay, I've got it…"
    
    ha "It's not that heavy…"

    hi "Okay then, can I at least hold your arm then?"
    
    show hanako emb_smile_cas
    with charachange
    #Hanako embarrassed

    "After a second's thought, Hanako switches her bag to her left hand, and holds out her right."

    "I wrap my arm around hers, and we head off towards the local platforms."
    
    $ renpy.music.set_volume(0.3, 1.0, channel='ambient')
    
    scene bg city_subway
    show crowd at centersit
    with locationskip

    ha "So, how much further is it?"

    hi "Well, from here we'll take a local train for about half an hour, then a short bus ride…"

    hi "A little over an hour, maybe?"

    ha "Oh… okay."
    
    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')

    scene bg city_trainstation
    show crowd
    with locationskip

    "We enter the more crowded local section of the station, and become swept away by the crowds."

    "Hanako grips my arm tightly, and I push us through the crowds to our platform."

    #BG platform-city

    #"The line to my parent's house isn't as busy as the inner-city lines, and Hanako relaxes a little."

    hi "Are you holding up okay?"
    
    show hanako emb_timid_cas
    with charachange
    #Hanako not embarrassed but not happy.

    ha "I… I guess."

    ha "No-one is paying attention to us."

    hi "That's just what people are like around here."

    hi "No-one notices anyone. I told you it'd be fine."
    
    stop ambient fadeout 3.0

    ha "Oh, is this our train?"
    
    hi "That's the one. Let's try and get a good seat."
    
    #scene bg city_trainscenerycity
    play ambient sfx_trainint fadein 5.0
    
    scene black
    show train_scenery2
    show train_scenery_fg
    show evfg hisao_trainride2 at Motion(trainwave, 4.0, repeat=True, bounce=True)
    with locationskip

    #Bg train window 2

    "The dense inner city thins slightly as our train ambles outwards."

    "Hanako returns to her slumber, leaving me alone to ponder my headache."
    
    stop ambient fadeout 3.0

    "Thankfully, it has started to subside, though that may be because of my fourth headache pill this morning."
    
    show city_houseext
    show hanako emb_timid_cas at tworight
    with shorttimeskip
    
    hide train_scenery2
    hide train_scenery_fg
    hide evfg hisao_trainride2
    hide city_houseext
    show hanako emb_timid_cas
    show bg city_houseext behind hanako
    with None
    
    $ renpy.music.set_volume(0.1, 0.0, channel='ambient')    
    play ambient sfx_traffic fadein 2.0
    play music music_daily fadein 2.0

    "We transfer to the bus without incident, and before long, we stand before my parent's home."

    #BG houseX outside

    hi "This is it."
    
    show hanako basic_smile_cas
    with charachange

    ha "It looks… nice."

    hi "It's not much, but it does the job."

    hi "It was big enough for us, and pretty close to the city."
    
    show hanako emb_timid_cas
    with charachange

    ha "That's not what I meant."
    
    show hanako emb_downtimid_cas
    with charachange

    ha "It's nice to have somewhere to go back to."

    hi "Oh, I'm sorry… I didn't mean to…"
    
    show hanako emb_blushtimid_cas
    with charachange

    ha "It's okay."

    hi "Come on, let's go inside."

    "I dig my old front door key out of my pocket and open the door."
    
    stop ambient fadeout 1.0
    
    play sound sfx_dooropen
    
    scene bg city_houseint
    with locationchange

    #BG random house interior.

    hi "I'm home…"

    "No answer."

    "The house is still."

    "We make our way inside, and dump our bags in the small living room."

    "On the coffee table rests a short note."

    #Sorry delta, I forgot how to declare notes

    $ written_note("Hi Hisao, thanks for coming to visit.\nSorry, but we won't be home until dinner.\nWe'll see you then.\n\nLove, Mom and Dad.")

    #RAGE

    hi "Huh, looks like we've got the place to ourselves for a while."
    
    show hanako basic_worry_cas
    with charachange

    ha "Oh."

    "We look awkwardly at each other for a moment, and consider the possibilities."

    hi "You know, we could…"
    
    show hanako emb_blushtimid_cas
    with charachange
    #Hanako Embarrassed

    ha "Not here!"

    ha "I haven't even met your parents!"

    ha "And, well…"
    
    show hanako emb_blushing_cas
    with charachange

    ha "I still don't feel so great."

    hi "Oh."

    hi "Fair enough."

    "To be honest, I'm not sure if my head would survive a round with Hanako."

    "Behind the dam of painkillers I can still feel the throbbing of my hangover."

    hi "So, should we go out somewhere?"

    hi "Maybe head back towards the city?"
    
    show hanako cover_smile_cas
    with charachange

    ha "Oh, okay."

    hi "I have a place in mind, I think you'll like it."
    
    show hanako basic_bashful_cas
    with charachange

    ha "Sure. Lead the way…"
    
    #stop music fadeout 5.0

    #I dunno, maybe this next bit should be NVL?
    
    #I'll take up your offer, crud. Saves me some serious headaches with yet another train interior shot- Alphabro
    
    "I take Hanako by the hand, and lead her to the bus stop."
    
    scene bg city_busstat
    with shorttimeskip
    
    window hide

    nvl show dissolve

    n "Both of us seem to be content enough to simply hold each other as we exchange the bus for the train."

    n "\n\"Hisao, I thought the trains to the city were going the other way.\""

    n "\"Oh, we're not going into the city centre, we're going… somewhere else.\""

    #Hanako curious

    n "\"Really? Where?\""

    n "\"It's a secret.\""

    n "\"Tell me!\""

    n "\"Can't. You'll find out when we get there.\""

    n "\"Fine then, I won't talk to you either.\""

    n "\n\nTrue to her word, Hanako doesn't say a thing on the train."

    n "She doesn't break her vow until we arrive at a small suburban station, about an hour from the city."
    
    nvl hide dissolve

    nvl clear
        
    window show

    #BG suburb station
    
    stop music fadeout 5.0
    
    show hanako def_worry_cas
    with charachange

    ha "This is…"

    hi "Yes."
    
    show hanako basic_worry_cas
    with charachange

    ha "How did you know?"

    hi "I had Lilly find out for me."

    ha "How did she…?"

    hi "We looked it up in the papers. Did you know they keep copies online?"

    hi "Something like this is pretty rare, you know?"
    
    show hanako emb_downtimid_cas
    with charachange

    #Hanako sad
    
    play music music_drama

    ha "I don't want to."

    hi "Why not?"
    
    show hanako emb_sad_cas
    with charachange

    ha "I said I don't want to. Let's go home."

    hi "No."

    hi "You've never been back here, have you?"

    hi "I only know how to get you this far, so you'll have to lead the way from here."
    
    show hanako emb_downsad_cas
    with charachange
    #Hanako Crying

    ha "I don't want to!"

    hi "Well, I'm not going to force you, but I think we should at least go there."

    hi "You can't avoid it forever…"
    
    show hanako emb_downtimid_cas
    with charachange

    ha "Why not?"

    hi "Because you're hiding."

    hi "You try to pretend that nothing ever happened, but it did."

    hi "Are you going to try and hide from what happened here forever?"
    
    show hanako cover_worry_cas
    with charachange

    ha "B—but…"

    hi "But what?"

    hi "What happened here is in the past, you can't change it."

    hi "But if you try to ignore it, it will eat at you forever."

    hi "Is that what you want?"
    
    show hanako emb_downtimid_cas
    with charachange

    #At this stage, I'm not sure if this is going as well as I had planned.

    "Hanako doesn't reply, but simply shakes her head."

    #"I check my frustration, and try to take on a milder tone." -c'mon, that just makes Hisao seem more like a dick. I had to comment it out.

    hi "Look, I'm here for you. If you want, we can just catch the next train home and forget about this."

    hi "But we've come all the way out here, so why not take that last step?"
    
    show hanako emb_timid_cas
    with charachange

    "I hold out my hand to the crying Hanako, who looks at me with lost eyes."

    "For a moment, I start to think that this may not have been my greatest idea."
    
    show hanako cover_worry_cas
    with charachange

    "But, even as I consider moving to the inbound platform, Hanako reaches out and takes my hand."

    ha "You promise you'll come with me?"

    hi "Of course."

    ha "No matter what?"

    hi "Not even if you try to run away from me."
    
    show hanako basic_worry_cas
    with charachange

    ha "O…"

    extend " okay."

    ha "It's this way… I think…"

    "Hesitantly, Hanako leads us out of the station, and onto the main street."
    
    scene bg city_street4
    with locationskip

    "The small suburb seems to be made up entirely of middle-sized homes, each with a small backyard."

    "The residents are probably all professionals that have chosen a little extra transit time for a little extra space."

    "However, even this place isn't free of urban sprawl."

    "As we move away from the station, duplexes start to appear amongst the houses."
    
    scene bg city_alley
    with locationchange

    "We turn off the main street, and before long the single houses become the rarity."

    "After a few more turns, we find ourselves surrounded almost entirely by small apartment blocks built on adjacent lots."
    
    scene bg city_apartment
    with locationchange
    
    stop music fadeout 8.0

    "Suddenly, Hanako stops in front of a run-down block of six apartments."

    "It looks to be a few years older than the blocks surrounding it."
    
    show hanako cover_worry_cas_close at right
    with charaenter

    ha "This… this is it."

    ha "This is where we lived…"

    "It could have been any other apartment block in the world."

    "A block of mail boxes sits at the front of a small yard, surrounded by discarded toys."
    
    show hanako emb_downtimid_cas at right
    with charachange
    
    show bg city_apartment at bgleft
    show hanako emb_downtimid_cas at tworightsit
    with dissolvecharamove
    
    #show hanako emb_downtimid_cas at tworightsit
    #with charamove
    
    play music music_innocence fadein 4.0

    "Hanako pushes her way through the waist-high gate, and kneels down in the yard."

    ha "It was here."

    ha "The front door was right here…"
    
    show hanako emb_timid_cas at tworightsit
    with charachange

    "She looks up, as if looking at a phantom house in her imagination."

    ha "I guess that this is where they found me…"
    
    show hanako emb_timid_cas at tworight
    with charamove
    show hanako emb_timid_cas
    with charamove

    "She stands up, and takes a few steps inside the house in her mind."

    ha "And this… this is where my father died."

    hi "It's unbelievable…"

    hi "To think that he was so close…"
    
    show hanako emb_downsad_cas
    with charachange

    ha "They told me my mother was found inside; she never had a chance…"

    ha "But my father grabbed me, and made sure I got out…"

    ha "So close…"
    
    play sound sfx_whiteout
    
    scene ev hanako_park_alone 
    with whiteout

    "Hanako falls to her knees, crying."
    
    show ev hanako_park_away 
    with charachange

    "I kneel at her side, and wrap my arms around her."

    "Again, I am amazed at the difference that two steps made."

    "Here, Hanako's father died, yet barely a metre behind me, Hanako lived."

    "Yet we both managed to cross that border in about a second."

    #"I bend down next to Hanako, and she throws her arms around me."
    
    show ev hanako_park_closed
    with charachange

    "She mouths soundless words into my ears, and I hug her tightly."

    hi "I'm sorry. I shouldn't have forced you to come here."
    
    show ev hanako_park_look 
    with charachange

    ha "No… don't be."

    ha "I'm sorry that I never came before."

    "Hanako pulls away from me, and wipes her puffy eyes."

    hi "Really? Why?"
    
    show ev hanako_park_closed
    with charachange

    ha "I never got the chance to thank my father."

    ha "He could have made it out himself, but he threw me outside instead."
    
    ha "All this time, after everything else that happened…"
    
    show ev hanako_park_away 
    with charachange

    ha "I used to blame him."

    ha "For putting me in foster care, for my foster mother, for what I went through…"
    
    ha "I used to think “Why didn't you just let me die?”"
    
    show ev hanako_park_look
    with charachange

    ha "But… that isn't what he wanted."

    ha "He wanted me to live."

    ha "He knew it was either him or me, and he chose me."

    #Hanako resolute
    
    play sound sfx_whiteout
    
    scene ev hanako_resolute #white
    with charachange #dissolve

    "Hanako stands up, and I stand up with her."

    "Without warning, she tilts her head backwards, and calls out."

    ha "Thank you!"

    #Hanako smile

    "I've never heard her speak so loud, but she is smiling from ear to ear."
    
    scene bg city_apartment at bgleft
    show hanako basic_bashful_cas
    with locationchange

    "She slowly tilts her head back to face me, still smiling."
    
    ha "Thank you too, Hisao."

    #Geh, this feels far to quick and "lol end of story nao" for me.

    ha "I think, without you, that I might have been stuck here forever."

    hi "You don't have to thank me, I forced you to come here…"
    
    show hanako emb_timid_cas
    with charachange

    ha "That's not what I meant."
    
    show hanako emb_downtimid_cas
    with charachange

    ha "I kept on looking at this as an excuse to never move on."
    
    show hanako emb_blushtimid_cas
    with charachange

    ha "But I can't do that forever."
    
    show hanako emb_timid_cas
    with locationchange

    ha "I'm never going to forget what happened here, but I don't want to let it hold me back anymore."

    ha "But… I can't do that alone."

    #So tempted to quote Retake here…
    
    show hanako basic_worry_cas
    with charachange

    ha "Hisao… will you help me?"

    ha "Will you promise me, with no regrets, to stay by my side?"

    hi "Yes… I promi…"
    
    play sound sfx_whiteout
    
    scene white
    with dissolve
    
    "Hanako stops me mid-sentence with a long, deep kiss."
    
    scene bg city_apartment at bgleft
    show hanako basic_bashful_cas_close
    with locationchange

    ha "There, we promised with a kiss."

    "Stranger" "Hey, what are you two doing over there?"

    "A stranger stands at the letterbox, eyeing us with suspicion."
    
    show hanako emb_smile_cas
    with charachange

    hi "Um, we er…"

    ha "I used to live here, so I wanted to show my boyfriend."

    "Stranger" "What are you talking about?"

    "Stranger" "I moved in when this building first opened, and I don't remember ever seeing you here…"
    
    show hanako cover_bashful_cas
    with charachange

    ha "Oh, well, I must have been mistaken."

    hi "We'll be on our way then, sorry for the disturbance…"
    
    stop music fadeout 4.0

    "Stranger" "Yeah, well don't let me catch you around here again or I'm calling the cops."
    
    show hanako basic_smile_cas
    with charachange

    ha "Don't worry, we've got what we came for."
    
    "Stranger" "Just get out of here…"
    
    show bg city_busstat
    show hanako emb_downsmile_cas_close at tworight
    with shorttimeskip

    #BG Train station
    play music music_twinkle

    "Hanako and I wait on the empty train station, our heads resting against each other."

    hi "Are you sure you're really okay?"
    
    show hanako emb_timid_cas_close at tworight
    with charachange

    ha "Yes, I think I'm fine now."
    
    hi "Well then, what now?"

    ha "I think…"

    extend " that I want to meet your parents."

    #hi "Really?"

    #ha "Really."

    #ha "I have some news that they might want to hear."

    #hi "Oh, and what would that be?"

    #ha "I'm late."

    #Lol baby end.
    #Game over.

    #Well, maybe. This is a bit of a Lol ending 'cause I want to ask advice from y'all.

    return

label en_end_hanakogood:
    # Hanako good end, after HT17
    scene black with dissolve
    centered "~ hanako good end ~" with dissolve
    return