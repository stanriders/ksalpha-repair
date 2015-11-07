label en_S20:
    scene black
    with None
    play sound sfx_alarmclock
    scene bg school_dormhisao
    with openeye

    
    "The familiar sound of my alarm wakes me up. I pick up my clock and read the time. It's past noon already; I've really slept in late. I turn off the alarm, but don't get out of bed just yet."

    play music music_twinkle fadein 5.0
    
    "Last night, I confessed to Shizune. Somehow, these words continue to run through my mind, even a day after the fact."
    
    "I can still recall her expression: Just a little surprised, her dark eyes dropping to look at her hands as they wove around each other tentatively, searching for the right words, the right response."

    "In the end, she had settled on one word. One gesture. “Okay.” She looked so different there, unguarded and deep in thought."

    "After that, she had grabbed my hand, rubbing my fingers between hers as if she were feeling a piece of cloth to check the quality of it, and her hand had felt like silk as her fingertips brushed against mine."

    "Then, Shizune had taken a seat on the roof, pulling me down with that soft but firm touch just as the fireworks from town began to burst before us in the black night sky."

    "It was the second time I had sat on that roof, gazing at the fireworks with the air around me so still and cool that it's like I was in a bubble, far away from the rest of the world, with only Shizune beside me."

    "Neither of us made any move to communicate. There was nothing more that I could have said to her, anyway."

    "As I dwell on this memory of last night, another thought slowly forms in the back of my mind before materializing fully."

    "Misha had never come back last night."

    "It's because of her transparency that I know why. Misha really is Shizune's opposite… Shizune is always so analytical and cautious, so competitive and so reserved. Misha is nothing like that, she is much easier to read."

    "Yesterday, —no, these past few weeks, she was probably thinking about that moment, when I would confess to Shizune. What a friend, to care with such intensity about a friend's happiness."

    "My thoughts return to Shizune. She's my girlfriend now… I've never had a girlfriend before."

    "I've come close, but then…"

    "That's an unpleasant thought. An unpleasant memory. I push it away, feeling bad just for thinking it."

    "Shizune is my girlfriend now. Just a few months ago, I wouldn't have believed that I could fall in love with her. She was just the cute girl who bossed me around, and somehow roped me into joining the student council…"

    "I guess my problem is that I don't know where to go from here."
    
    stop music fadeout 3.0

    "But, I have no regrets. I like Shizune. A good thing to do would probably be to go see her now. Taking a quick shower and throwing on a clean set of clothes, I think of where she could be."
    
    play music music_pearly fadein 2.0
    scene bg school_dormext_full
    with locationchange
    
    "Her dorm room aside, it's likely she's in the student council room as usual. Even with school out for the summer, there are summer classes. The work really does never stop."
    
    scene bg school_courtyard
    with locationchange
    
    "I've always thought that she really liked that room, too. She does seem to stay there even at times when she has nothing to do. Maybe it's because it's the one place that is truly hers. Shizune is the only one with the key to the student council room."

    scene bg school_hallway3
    with locationchange

    "She spends more time there, I imagine, than she does in her dorm room. I head over there, passing some of my classmates who had to end up taking summer courses along the way."
    
    play sound sfx_dooropen
    scene bg school_council
    with locationchange

    "The door to the student council room is unlocked. I open it. Shizune is sitting with her back to me, staring out the large window behind her desk at the school grounds, which are almost empty even at this time of day."

    "With her back turned to me like this, she is defenseless. I mull over the idea of sneaking up on her and surprising her, but suddenly, she turns around in her chair and spots me, putting an end to that idea."

    show shizu basic_normal
    with charaenter
    
    "A little surprised at my presence, Shizune quickly recovers and resumes her normal, stoic expression. After a pause, she signs:"

    ssh "Hi."

    hi "Hello."
    
    show shizu behind_smile
    with charachange

    "Shizune manages a smile that looks well-intentioned but comes off as a bit forced."

    "It seems like she doesn't know what to say either."
    
    show shizu behind_blank
    with charachange
    
    stop music fadeout 4.0

    "The room is still, the unbroken silence making the air feel thick and heavy around me. Shizune seems different. I know that it's because she is carefully deliberating each and every word she could use."

    "I can still remember that she was the one who told me that that was the one benefit of sign language: The fact that you could be afforded the luxury of being able to think through everything you “say” before you say it."

    "But this kind of thought is excessive, and I have never seen anything like it before."

    "Maybe Shizune was a little freer with her words than she was implying. I smile as I entertain that thought. That would make her a hypocrite. Or, more plausibly, maybe I've just caught her off guard today."

    "Seeing that I've stopped looking directly at her, Shizune raps her knuckles lightly against her desk three times."

    "Even with my attention on her, she hesitates before signing:"
    
    show shizu adjust_blush
    with charachange

    ssh "Let's go on a date."
    
    play music music_another fadein 2.0

    "Shizune turns her head to the side, trying to hide the flush of pink color spreading across her face, but I can feel her watching me out of the corner of her eye, waiting for my reply."

    hi "Sure."

    "I nod my head. It feels like there is more that I could say, almost like my reply is lacking, but I can't think of anything more that I could say."
    
    show shizu behind_smile
    with charachange

    "Either way, it seems to satisfy Shizune. She returns my nod with an understanding one of her own, then turns her chair around towards her desk with one hand and sits down."

    ssh "Usually, it's the man who asks his girlfriend out on dates in a relationship."

    "At first, I think she is making another one of her usual jabs at me, but the thoughtful expression on her face leads me to doubt that possibility, and eventually, I am unsure whether it is a joke or a musing."

    hi "Well, I was going to ask you if you wanted to go somewhere, but you beat me to the punch."

    "It's an obvious lie. That isn't what I set out to do when I came here. In fact, I don't know what I was planning to do when I came here today. It's likely, though, that that is what I would have done in the end."

    "Suddenly, Shizune pushes herself out of her chair and tries to grab me from across the desk. Unfortunately, I pull away reflexively, but not fast enough."
    
    show shizu cross_shock_close
    with characlose
    hide shizu 
    play sound sfx_impact2
    with vpunch

    "Shizune's hand catches the lapel of my jacket, and we both go tumbling down, my falling body pulling her over the desk as we plunge towards the ground. It happens in less than a second, but with frightening clarity."

    "I can feel Shizune shaking on top of me, her head buried in my shirt. It takes me a second, but I realize she is struggling to keep from laughing."

    hi "Hey, I'm glad you think this is funny, but show a little more tact in front of the guy who broke your fall."

    "I forget to sign it to her, blurting it out. Shizune doesn't seem to notice this, pulling away immediately, her face turning bright red as if to say “I'm sorry, I'm sorry.” I imagine her saying it in an apologetic, nervous voice, like Yuuko's."

    "Aside from the soreness in my back, this is actually a nice feeling. I almost want to grab her and pull her closer."

    "Standing up, Shizune brushes the dust off her clothes and attempts to straighten out the winkles before uneasily offering a hand to help me up. I take it, and pull myself up."
    
    show shizu adjust_blush
    with charaenter

    ssh "Sorry."

    "She shrugs."
    
    show shizu behind_smile
    with charachange

    ssh "I was trying to be spontaneous."
    
    show shizu behind_blank
    with charachange

    ssh "Are you hurt?"

    hi "My back hurts."
    
    show shizu basic_normal2
    with charachange

    "Her eyes shift towards the floor."

    ssh "Sorry, that is because of my carelessness."
    
    show shizu adjust_frown
    with charachange

    ssh "…But, you know, you shouldn't pull away when someone is trying to give you a hug. Don't you know how rude that is?"

    ssh "You can't say that you are totally without blame. …And in the end, that's what really matters."

    "That familiar, challenging look is back on her face, but the traces of red on her cheeks gives away that she is still embarassed, and probably can't wait to put this behind her."

    "I think that despite that, Shizune is happy. It's as if she is unsure how to handle the feeling."

    hi "Let's go somewhere tomorrow."
    
    show shizu basic_normal
    with charachange

    ssh "I'm busy tomorrow. How about the day after?"

    hi "Okay."

    "A brisk exchange; done almost without thought. We could have discussed anything, and it would likely have ended the same way."

    hi "Where do you want to go?"
    
    show shizu adjust_frown
    with charachange

    "Shizune frowns and pushes her glasses up delicately with her pinky finger."

    ssh "Hey, are you going to have me decide everything?"

    ssh "It will be boring that way. I know, you can surprise me."
  
    show shizu adjust_happy
    with charachange
    
    ssh "I'm entrusting this to you, so don't screw up! Do it properly!"
    

    "Despite the edge in her words, there is a content smile on her face, and her posture is relaxed."
    
    hide shizu
    with charaexit

    "Done with everything she wanted to say, Shizune turns her attention towards the ledger on her desk, which I notice for the first time."

    "I guess the student council never gets a break here. This might explains why membership seems to be kind of at a low."

    "I can't see a lot of people willing to work as much as I've seen Shizune and Misha work, or as much as I myself have worked."

    "There were many times when the workload piled up so high that it was like I could see a mountain before me, immeasurably high and unsurmountable."

    "And to not even have summers free, that is a little much."

    "None of it ever seems to bother Shizune, however. She reads through the ledger with nothing other than a sense of professionalism, a ballpoint pen between her fingers ticking back and forth like a metronome in tune with her thoughts."

    hi "Do you need any help?"
    
    show shizu behind_smile 
    with charaenter

    "Shizune looks up at me gratefully over the top rims of her glasses, but ultimately shakes her head “no.”"

    ssh "I'm almost done, so I don't need any help."

    hi "Where is Misha?"
    
    show shizu basic_normal 
    with charachange

    ssh "She ran off to the convenience store. That was a little less than an hour ago. I would have went with her, but she said she wouldn't be long."

    hi "What did she need?"

    ssh "Food, of course."

    hi "Of course…"

    "I keep thinking that maybe they should invest in a mini-fridge, or at least start buying food in bulk, since they apparently go through a lot of it."
    
    show shizu behind_blank 
    with charachange

    ssh "We know the cashier at Auramart, so we can always get a great deal. Is there anything you like to eat? I'll keep it in mind for the next time I go there."

    hi "It's fine."

    ssh "Suit yourself, but if you see something you like, I won't share it with you."

    hi "That's kinda cruel, don't you think?"

    show shizu adjust_smug 
    with charachange
    
    "Grinning, she waves her hand at me dismissively."

    ssh "Individual packages are individual for a reason!"

    hi "But you're not going to buy just one of everything, right? Or you could get an economy-size."

    ssh "I could, but then if you don't like it, I'd be stuck with an unnecessarily large amount of food."

    ssh "See? I can't buy something for you if you won't tell me what you like."

    "She gives me a sly, knowing wink."
    
    show shizu behind_smile
    with charachange

    "Shizune looks the most at ease during moments like these. I don't know how to describe it, somewhere between playfulness and rivalry."

    "What a problematic personality, although I'll admit that when she smiles like this, she looks very cute."

    "I decide to go to the library. I could use a few novels to read, and maybe I can even find another sign language book. I can still remember how Misha told me to keep on sharpening my knowledge of it."

    "She had said it with such humorlessness, devoid of any of her usual good cheer, almost as if she were burdened with something. Recalling it makes me feel cold. I had forgotten lately how down Misha has seemed these past few weeks."

    "It always comes up, and then slips out of my mind."

    "As I turn and start to leave the student council room, Shizune rushes over to me."
    
    show shizu behind_frown
    with charachange

    ssh "Hey, where are you going? If we wait a little longer, Misha will be back. You can at least stay for lunch."

    "The offer is tempting. I wonder how Shizune would feel if she knew that I was going to learn more sign language."

    hi "I'll pass, I have to head to the library today."
    
    show shizu behind_blank
    with charachange

    "Shizune cocks her head almost imperceptibly to the side, looking slightly skeptical."

    ssh "Okay."

    ssh "Don't forget our date."
    
    play sound sfx_doorclose
    scene bg school_hallway3
    with locationchange    

        
    stop music fadeout 2.0
    

    "Leaving the student council room, I realize that I am a little hungry. I haven't eaten since last night. Maybe it wasn't such a great idea to pass on Shizune's invitation."
    
    scene bg school_lobby
    with locationchange

    "I can always grab the books and then head back, though. Problem solved."
    
    scene bg school_courtyard
    with locationchange

    "Feeling pleased with myself for figuring out the answer to such a problem, I decide to reward myself with a can of juice. I'm not just hungry, but thirsty, too, so this all worked out for the best."

    play sound sfx_footsteps_soft
    
    "As I put a coin into the vending machine outside of school, I hear footsteps crunching through the grass behind me."
    
    play music music_comedy fadein 1.0
    play sound sfx_impact2
    with hpunch

    "Before I can turn around, two arms with a heavy bag of groceries in each swing around my shoulders from behind. The bags hit me squarely in the face, causing me to wince and let out a yell."
    
    
    mi "Hi~cchan~!"

    "Somehow, I knew it was Misha. I try to relax, still feeling kind of foolish as she pulls me around in her vicegrip, the bags in her hands hitting my chest."

    hi "Okay, okay, you can let go of me now."
    
    show misha hips_grin
    with charaenter

    "The moment I can get a glance at her, I see that she looks a little worn out. Her chipper demeanor belies the fact that she still seems to have a tinge of depression clouding her face."

    "I'll admit she's getting better at hiding it, though."

    mi "How have you been, Hicchan?"

    mi "I'm sorry about not making it to see the fireworks yesterday! How were they?"

    hi "They were nice."

    "I can see where she is going with this."

    hi "I confessed to her."

    mi "Way to go, Hicchan~! Of course, Shizune already told me everything, so I knew."
    
    show misha cross_laugh
    with charachange

    mi "Hahahahaha~!"
    
    show misha cross_grin
    with charachange

    mi "But~! Now, you should take her on a date, Hicchan."

    hi "Yeah, we were just talking about that, actually. I don't know where to take her, though."

    hi "Do you have any good ideas?"

    hi "Ah, I can't trust you, though. If I ask you of all people where to take her, you'll probably end up spilling it all to her. Then the surprise is ruined."
    
    show misha hips_frown
    with charachange

    mi "That's not fair! You really think I would tell her, Hicchan?"

    hi "Yes. Yes, I do. I really think you would tell her."

    mi "Awww, you're so cold, Hicchan."
    
    show misha hips_laugh
    with charachange

    mi "Hahaha!"

    "Her laughter seems forced, as if she feels obliged to let it out. I can't ignore it any longer."
    $ renpy.music.set_volume(0.0, 2.0, channel="music")
    hi "Hey, Misha, everything is okay, right?"
    

    
    show misha sign_confused
    with charachange

    mi "Eh? What do you mean, Hicchan?"
    
    show misha perky_confused at centersit
    with charamove
    show misha perky_confused at center
    with charamove

    "She drops the bags onto the grass temporarily to stretch her fingers."

    hi "You've seemed kind of down the past few weeks. Is there anything wrong?"
    
    show misha cross_grin
    with charachange

    "Misha smiles broadly and lets out another laugh. This time, it sounds like the real thing."
    
    show misha cross_laugh
    with charachange

    mi "Wahaha~!"
    
    show misha cross_grin
    with charachange

    mi "You're worried about me, Hicchan? Thanks~! I'm really, really glad~! Ah~! Don't worry about it, though."

    mi "I've just been a little tired lately, yup~!"
    
    show misha perky_smile
    with charachange

    mi "I'm very happy now, though. Hicchan is happy, and Shizune is happy. So, I am happy, too."

    "Such a strange and implaceable expression; indistinct from the blending of quiet wistfulness and simple joy."

    "A million thoughts run through my mind simultaneously, speculations as to what could be upsetting her, but in the end, I take too long to ask her. The window of opportunity slides shut."

    show misha sign_smile
    with charachange
    
    $ renpy.music.set_volume(1.0, 2.0, channel="music")
    
    mi "Hicchan~! Do you want to guess what's in these bags?"
    
    show misha perky_smile at centersit
    with charamove
    show misha perky_smile at center
    with charamove

    "She raises them to her head with some effort and then shakes them like a set of keys."

    hi "Food?"
    
    show misha hips_grin
    with charachange

    mi "Wow, right on the first try!"

    "…"

    hi "Well, I can see food through the bag. And it says “Auramart” on the side, so I know where it's from. And I can see a box of cookies sticking out of the top. And…"

    "I feel almost insulted somehow."
    
    show misha cross_laugh
    with charachange

    mi "Ahahahaha~!"

    mi "You're right, you're right! Hm… maybe this was a little too easy for Hicchan."
    
    show misha sign_smile
    with charachange

    mi "Okay, okay! It'll be much harder next time, so be on your guard!"

    mi "Hey, Hicchan, this is a lot for Shizune and me. If you didn't eat lunch yet, now's your chance!"

    hi "Shizune said the same thing. Okay, I'll take you both up on the offer. I'll take the bags."

    "Instead of handing the bags to me, Misha puts them on the floor so I can pick them up. An uncharacteristic action."
    stop music fadeout 1.0
    
    scene bg school_council
    with locationchange
    play sound sfx_dooropen

    "When we open the door to the student council room, Shizune is standing by the door, as if she were waiting all this time."
    
    play music music_shizune fadein 1.0
    show shizu behind_blank
    with charaenter

    ssh "Hello, Misha."

    ssh "Hisao, why are you here?"

    hi "Why am I here? You invited me to lunch."

    ssh "But, you turned it down."

    hi "Well, I was hasty."
    
    show shizu adjust_frown
    with charachange

    "She cocks an eyebrow skeptically, then regards me with a chagrined look lined with teasing humor."

    ssh "You shouldn't be hasty. All this sign language, and you have already forgotten the most basic thing. Remember?"

    ssh "You have to think things through! And not just words before you say them, but everything! Everything!"

    hi "I haven't forgotten that at all."
    
    show shizu adjust_smug
    with charachange

    "A smile flashes across her lips."

    #ssh "If you say so. Just to be safe, maybe I should pick where we go on our date…"

    return

    #a choice, save the result for later?

label en_choiceS20:
    menu:
        with menueffect

        ssh "If you say so. Just to be safe, maybe I should pick where we go on our date…"

        "If you want to.":
            return m1

        "No.":
            return m2

label en_S20a:
    #1) If you want to

    hi "If you want to."
    
    show shizu behind_frown
    with charachange
    
    "Shizune shakes her head firmly."
    
    ssh "No."

    ssh "I was kidding. Don't take everything so literally."

    return

label en_S20b:
    #2) No

    hi "No, you can't. I've already decided on where to take you, and it would ruin the surprise."
    
    show shizu behind_smile
    with charachange

    ssh "You have already decided? That was fast."

    ssh "Maybe you do have potential after all."

    "Fortunately, she couldn't tell that I was totally lying."

    return

    # choices end

label en_S20c:
    
    show shizu behind_blank
    with charachange

    ssh "Okay, let's set up, and then we can eat."

    mi "Okay, okay~!"
    
    hide shizu
    with charaexit
    
    stop music fadeout 3.0

    "After unpacking everything, we spend a few minutes deciding what to dig into."

    "Helping myself to a box lunch, I eat as fast as I can and then thank Shizune and Misha for the meal before I head to the library."
    
    scene bg school_library_ss
    with locationskip
    play music music_tranquil fadein 1.7

    "It's deserted. The lights aren't even on. That's okay, though. As I peruse the shelves, I let my thoughts wander."

    "Misha has been depressed since she told me she was going to visit her family. So she doesn't get along with them… I wonder if it's her siblings, or her parents, or both."

    "I feel terrible. Even moreso because I feel like I could have said something, or done something. I mentally chastise myself for this. I feel pretty powerless, but even so, I could have said something."

    "Eventually, my thoughts drift towards Shizune, partly to get away from that depressing subject. I did make a date with her. I don't know the town well enough to know where a good place to go would be."

    "But I have a whole day to look into it."

    "Picking out a sign language book, I think about how strange it feels to be going on a date with her. How will she act? Will she dress up for the occasion? I wonder what kind of outfit she will wear."

    "Either way, Shizune seems to be happy."
    
    scene bg school_dormhisao
    with locationskip
    
    "Finding all the books I came for and more, I head back to my room. Maybe I can get on the internet from my phone and look up nice places to go in town."
    
    "Tomorrow is my date with Shizune. As soon as I confirm that fact, I roll over and decide to go back to sleep."

    "It's a little hard to do so, however, because a nagging thought keeps popping up in my head:"

    "I never really set a time with Shizune for this date. It would be pretty bad if Shizune were to knock on the door tomorrow at the wrong time, all dressed up and expecting to go out now."

    stop music fadeout 2.0
    
    "Nevertheless, I'm very tired, so eventually I begin to feel myself nodding off."
    
    scene black
    with shuteye
    return

label en_S21:

   
    scene bg school_dormhisao
    with openeye

    play music music_daily fadein 3.0

    "When I wake up again, I can tell that I have been asleep for awhile."

    "Although I can't see my clock right now, I can see out the window, and just from the position of the sun, I'd guess it's at least a few hours past noon."

    "As I get out of bed, I think about tomorrow's date again."

    "If I've learned one thing from working with Shizune all this time on the student council, it's that she's very punctual, and often early anyway just to be safe. And like most punctual people, she's focused a lot on time."

    "That could be what time it is, to when something begins, to how long it will take. I'm sure that the uncertainty of the situation is bothering her. I should set a time with her today."

    "I think back to her words the last time I saw her: “Surprise me.”"

    "She trusts me at least that much, huh?"

    "Or…"

    "This could be another test. It seems a little paranoid of me to think that, but it does make an awful lot of sense, considering who I'm dealing with."

    "But in a way, aren't the two things one and the same? At least a little, I'd say."

    "I can remember the gentle motions of her hands as they traced the words so carefully into the air: “I'm entrusting it to you, don't screw up!”"

    "And then I think about the expression she had on her face during it; a mischievous smile belied by the expectant glimmer in her eyes that showed she was actually looking forward to it, as much as I'm looking forward to it."

    "Yeah. All this means that I can't screw up, doesn't it?"

    "Today, I should at least set a time with her, so that we'll be on the same page."
    
    scene bg school_dormext_full
    with locationchange

    "After I take a quick shower and throw on my clothes, I head outside, and no sooner than the fresh air hits me I don't know where to find Shizune again. I feel like hitting myself and have to work to keep from falling to my knees."

    "What failure. The worst part is I've made this mistake before."
    
    stop music fadeout 1.0

    "I let out a little laugh in disbelief, and jump as I hear a much more enthusiastic laugh shatter the air coming from behind me."
    
    play music music_comedy fadein 1.0

    mi "Hey, Hicchan~!"
    
    play sound sfx_impact2
    with hpunch

    "Before I can raise my guard, she barrels into me, pushing against my back as if she plans to jump over me like in a game of leapfrog."

    "It's all I can do to keep from being thrown face first to the ground."

    hi "What the hell? Be careful, you almost knocked me over."
    
    show misha perky_sad
    with charaenter

    mi "Sorry, sorry sorry sorry~!"

    "Disturbed by how similar she sounds to Yuuko, I forgive her."

    hi "It's okay, no harm done. I don't think you could knock me over, anyway."
    
    show misha cross_smile
    with charachange

    mi "Hahaha~. You sound confident today, Hicchan. Is that why you were laughing?"

    hi "No."

    mi "Well, your laugh wasn't very full of confidence~! You need to put more energy into it, Hicchan."

    hi "I don't think I'm a very energetic person."

    hi "Why were you laughing?"
    
    show misha hips_grin
    with charachange

    "Misha closes one eye, thinking deeply, before throwing her hands out to her sides."

    mi "Hmmmm… I don't know~! I saw you laughing, so I decided to laugh too!"

    mi "It's good for you, it'll make you live longer, Hicchan. You should laugh more."
    
    show misha cross_laugh
    with charachange

    mi "Wahahahahaha~!"
    
    show misha cross_grin
    with charachange

    mi "Come on! Laugh with me!"

    "Although I'm not very good at forcing myself to laugh, I'll do it anyway to humor her."

    hi "Hahaha…?"
    
    show misha hips_frown
    with charachange

    "Misha frowns, and she cocks her head to the side."

    mi "That wasn't very good, Hicchan. Come on, try harder! Like this: Hahahaha~!"
    
    show misha hips_laugh
    with charachange

    mi "Hahahahaha~!"

    "I feel a bit silly. If someone were to see me right now…"

    "Nevertheless, I've done this much, so I might as well keep giving it a shot."

    hi "Hahaha! …How was that?"
    
    show misha cross_grin
    with charachange

    "Misha does a small hop and claps briefly."

    mi "That's perfect, Hicchan~!"

    "Why do I feel like a pre-schooler? The feeling is only increased as Misha starts patting me on the shoulder. This level of congratulatory gesture is really too much."

    "Suddenly, her hand stops moving, and becomes limp and heavy on my shoulder."
    
    show misha perky_sad
    with charachange

    mi "A~hahaha~…!"

    mi "It's kind of hard to do, isn't it?"

    "Her gaze drifts downwards, like she is afraid to meet mine."

    mi "But, Hicchan, it's okay for now. It needs practice, though. Just a little."

    "She rubs her ear thoughtfully, still not looking directly at me. Her tone has changed as well. She seems more nervous, more hurried, but so slightly that I wouldn't have picked up on it at all if it wasn't so unfamiliar."

    show misha perky_smile
    with charachange
    
    mi "Wow, Hicchan~! It seems like there are a lot of things you have to practice, aren't there? So~! I hope that means you are going to do just that."

    mi "It's hard to laugh on cue, isn't it?"

    "She just said that. With each word, her voice loses that lilting quality and continues to get lower."
    
    show misha perky_sad
    with charachange

    mi "I'm sorry, Hicchan. It's a little weird, isn't it? It's a weird thing to teach someone."

    mi "Can you please forget it? It seems like I'm trying to make Hicchan into a more fake person."

    mi "So, can you please forget I said anything?"

    "Some of the cheer creeps back into her voice, but it's too late. I've already started thinking back to how sad Misha was even just a few days ago. Somehow, it had slipped my mind, but now, I can see that she is seriously depressed."

    hi "Is everything okay?"

    "It's a little blunt, but I don't know what else to say, and it has to be better than not saying anything at all."

    "Misha's hand keeps weighing on my shoulder, as if it's pulling me downwards. She claps my back again in a weak attempt at showing her energy."
    
    show misha perky_smile
    with charachange

    mi "Yup~! Of course, Hicchan."

    "Her voice cracks, just for a second. Misha's head drops, and she stares at my shoes, arms stiff at her sides. Neither of us even so much as make an attempt to speak."

    "I don't know what she will do. All I can think of is what she might do. Is she going to play it off like nothing? That would probably be the least awkward thing, but it seems unlikely. It seems unlikely that she would, and that she could."

    "Misha tries her best, though."

    mi "Hahahaha~!"

    mi "I've been standing here a long time, right? Right, right~!"

    mi "I always get distracted and take too long, and say something stupid. It looks like I did it again, huh, Hicchan? I just wanted to go to the store, and I…"
    
    show misha perky_confused
    with charachange

    mi "Hm. Did I depress you, Hicchan? I didn't really mean, it, okay? Don't take it the wrong way."

    mi "I'll… go now. Tomorrow is your date with Shicchan, right?"

    hi "Yeah. About that… I have to set a time with her for it. Do you know where she is right now?"

    "I feel guilty as I say it. It sounds like I'm brushing Misha aside, but if she thinks that, she doesn't show it."
    
    show misha sign_smile
    with charachange

    mi "Nope~! Ah, what about if I give you her cell phone info?"

    hi "Cell phone?"

    "What immediately pops into my mind is how strange it is for a mute person to have a cell phone, but I suppose she can still use it to check and send mail, right?"

    mi "What, Hicchan, you didn't think Shicchan had a cell phone, right? Hahahaha~! We live in modern times, there is no one without a cell phone."

    hi "Actually, I don't really use mine that much. I don't think I have it on me right now."

    mi "Huh, that's so strange, Hicchan… Well, whatever~."

    "She's back to her bubbly old self, but the feeling of unease won't go away. It continues to gnaw at me. A person's personality can't change so suddenly, and without reason."

    mi "I'm going to get going now. Bye, Hicchan~!"

    hi "Wait!"

    "I yell it out just as she hunches down, like a sprinter about to get ready to break into a run."

    mi "Huh?"

    hi "…You didn't give me her address or anything."

    "It's the first thing that comes to mind."
    
    show misha perky_confused
    with charachange

    mi "Oh! You're right, Hicchan, you're right, you're right… Sorry…"

    hi "Besides that, I'm going to tag along with you today. I have some stuff I need from the store, too. We might as well go together."

    "Realizing how it sounds, I think about the implications of my words and wonder if they could be misinterpreted. Misha is silent before she lets out a barely audible, reserved sigh of relief."

    show misha cross_smile
    with charachange
    
    mi "Okay, Hicchan."

    "She pauses before breaking into a peal of laughter and running ahead of me."
    
    hide misha
    with charaexit

    hi "Wait! What about Shizune's address?"
    
    stop music fadeout 1.0
    
    "But she doesn't seem to hear me, and I have to struggle to keep up with her."
    
    scene bg suburb_konbiniext
    with shorttimeskip
    play music music_ease fadein 2.0
    
    "After I buy some school supplies to get it out of the way now instead of a week before classes start again, and Misha buys what appears to be at least ten thousand yen worth of hairspray and curlers, we leave Auramart."

    "I had to buy a pen and pad to write down Shizune's e-mail on, since I obviously didn't have one on me. Oh well, they didn't cost much anyway."

    scene bg suburb_roadcenter
    with locationchange
    
    "As we start walking back to school, Misha seems sullen again. Her mood had gradually gotten more and more subdued as we had come into town. She hasn't said anything now in almost half an hour."

    play sound sfx_rumble
    
    "All of a sudden, my stomach growls. The sound would be almost menacing if it weren't so embarrassing. Misha turns to me, smiling wryly."
    
    show misha cross_smile
    with charaenter

    mi "Are you hungry, Hicchan?"

    hi "Well, I think the answer to that is pretty obvious, huh?"
    
    show misha cross_grin
    with charachange

    mi "Haha! I'm hungry, too. Let's get something to eat, Hicchan~."

    "I turn my head towards her and notice that we are right in front of the Shanghai. Before I can protest, Misha pulls me in through the doorway, the two of us and her huge bag of hair care supplies getting us momentarily stuck in the door."

    scene bg suburb_shanghaiint
    with locationchange
    play sound sfx_storebell
    
    "It's a good thing the shop seems all but deserted or I would never live this down."

    "It looks like Yuuko isn't in today, just a brusque looking guy who must be the cafe owner. Misha orders two sandwiches, one for each of us, and drinks as well."

    "When our food is ready, Misha pays for it and brings it to a table in the corner before sitting down and digging in."
    
    show misha perky_smile
    with charaenter

    "It's too quiet in here today. The atmosphere is almost depressing. I try to alleviate the bad mood with a joke."
    
    stop music fadeout 1.0
    show misha perky_sad
    with charachange
    
    hi "Hey, isn't it a little presumptuous to order for someone without asking them how they feel?"
    
    play music music_sadness fadein 3.0

    "Unexpectedly, Misha begins to sob quietly, without tears."

    hi "Misha, what's wrong?"
    
    hide misha
    with charaexit
    play sound sfx_storebell

    "She doesn't answer, although she makes an effort to stifle herself. I ask for a bag and start packing our food into it as quickly as possible, turning my head when I hear the bell above the cafe door ring to signal someone opening it."
    

    "Misha has already left. I hurriedly follow after her, carrying her bags as well, seeing as how she apparently forgot about them in her rush to leave."

    scene bg suburb_park_ss
    with locationchange
    play ambient sfx_park fadein 1.0
    
    "I catch up to her in the park a few blocks away."
    
    show misha perky_smile
    with charaenter

    "Her familiar happy-go-lucky expression is back on her face, the only evidence of what just happened being a single tear in the corner of her eye that she takes great care to discreetly wipe away before she starts speaking."

    mi "Hi, Hicchan."

    hi "Don't say that. Misha, is there something wrong? You've been acting like this for the past week."

    "I calm down a bit and let out a sigh."

    hi "You don't have to tell me, if you don't want to. But I have noticed it."
    
    show misha sign_sad
    with charachange

    mi "Is it really that noticeable, Hicchan?"

    "So quiet, and toneless, and flat."

    hi "Yeah."

    mi "Well… it's okay. If you can see it, then that is okay, a little."
    
    mi "Does Shicchan notice it too?"

    hi "I don't think so."
    
    show misha perky_sad
    with charachange

    mi "Then… that is okay…"

    hi "It's not okay."

    "I feel myself becoming a little angry at her. It's her indifference to it all. Strange, that an indifferent person like me could find someone else's indifference so troubling. I guess this makes me a kind of hypocrite."

    "Misha's gaze goes over my head and after a long pause, she finally speaks."
    
    show misha sign_sad
    with charachange

    mi "Whatever happens to me is fine, as long as Shicchan is happy. I have always believed that, Hicchan. I still do."

    mi "You, too. Maybe because of that I've been thinking about the future a little more than normally, but… I'm fine."
    
    show misha perky_smile
    with charachange

    mi "I'm crying right now because I'm happy. Please believe me."

    "Despite that, there are no tears flowing from her eyes. It looks like I have no choice, though, but to accept what she says."

    mi "Hicchan, you brought the food?"

    "She giggles a little."

    mi "That's why Shicchan likes you. You are thoughtful, even if she sometimes says that you're a little stupid."

    hi "She says that?"

    "I'll take any chance I can get to dispel the awkwardness that I can feel pressing down on me."

    mi "Yeah. Let's eat, Hicchan."

    "Without waiting for my answer, Misha reaches for the half-eaten sandwich in the bag at my side and starts to eat it, leaning against a knotted old tree. The smile gradually returns to her face in time."

    show misha cross_smile
    with charachange

    mi "Hicchan…"

    "She balls up her trash and tosses it into a garbage can after taking a minute to aim, getting it in like a basketball player sinking an important shot."

    mi "Perfect! Goal~!"
    
    show misha sign_smile
    with charachange

    mi "Ah… I feel much better now. I'm sorry, Hicchan. I'm really okay, really, really~! Don't worry about me, okay? Okay~."

    mi "I'm going to go on ahead. Don't worry about me, okay? I'm sorry I made you worry. I just lost my composure, a little."
    
    show misha hips_laugh
    with charachange

    mi "Hahaha~!"
    
    show misha hips_smile
    with charachange

    mi "Tomorrow is your date with Shicchan. I hope you two have a great time~!"
    
    hide misha
    with charaexit

    "She takes her bag out of my hands and bows with uncharacteristic severity before turning around and running off, waving goodbye, but not looking back."

    "Feeling drained, I plop down in the nearest bench. The bags in my hand fall to the ground, and I barely notice them go."

    "I'm still disturbed by a lot of the things Misha said today. The way she acted, and the way she spoke, were so alien. The incongruity between the Misha of today and the one I think of is so great that I find it more than slightly unsettling."

    stop music fadeout 3.0
    
    "But I push those thoughts out of my mind. Or, I at least try to. I would e-mail Shizune, but I don't have my cell phone on me. So, the only thing that I can do now is sit here and think."

    "Even that, however, becomes difficult after awhile with all the stuff that's happened today."

    "Stretching out my legs and finishing off the bottled juice that Misha bought for me before to go with my sandwich, I realize that it's getting dark. It's probably time I should get back to Yamaku myself."

    "Tomorrow is my date with Shizune, after all."

    "I can't bring myself to leave this thing with Misha unresolved, though."
    
    stop ambient fadeout 1.0
    
    scene bg school_road_ss
    with locationchange

    "As I walk up the road to the school, these two thoughts duel each other in my head for attention, and continue to do so until I go to sleep."
    
    scene black
    with locationchange

    return

label en_S22:
    
    play ambient sfx_doorknock
    scene bg school_dormhisao
    with openeye

    "I wake up to the sound of someone knocking thunderously loud on my door. Squinting as my eyes adjust focus and get used to the light, I look over at my door and see it shake violently with each crashing blow against it."

    "Who could it be? It certainly sounds like an angry mob, or a stampede of animals, but I am pretty sure I haven't angered enough people for there to be a mob after me, and I don't know of any zoos in the area, so both of those are highly unlikely."

    "The only logical answer, really, is that it's either Kenji or Shizune."

    hi "Yeah, hold on."
    
    play sound sfx_dooropen
    
    stop ambient 
    
    scene bg school_dormhallway
    with locationchange

    "It's kind of chilly today. I throw on a jacket and open the door to find Shizune standing there."
    
    play music music_shizune
    
    show shizu behind_blank
    with charaenter

    shi "…"

    hi "Hi, Shizune."

    "I forget to sign it, and even when I catch myself, I have to stop to yawn before I can complete the motion."
    
    show shizu behind_frown
    with charachange

    ssh "Every time I come here, you look like you just got out of bed. You have to look at least presentable if someone is coming to see you."

    hi "Hey, that doesn't apply when someone shows up unannounced. Like you."
    
    show shizu adjust_angry
    with charachange

    "Her eyebrows quickly turn dowards and she glares at me sternly."

    ssh "That is incredibly rude, even if you do have a point. What I wanted to tell you was that you should sleep earlier. It's better for your health."
    
    show shizu behind_blank
    with charachange

    ssh "…Do you remember what day it is?"

    hi "Of course."
    
    show shizu basic_normal
    with charachange

    "Shizune bites her lip and then starts signing while looking away from me."

    ssh "What time do you want to meet up?"

    hi "Well, we're meeting now, aren't we?"
    
    show shizu behind_frustrated
    with charachange

    ssh "Sometimes I think you cannot help but give a wise answer. It's really important that I know the time that you want to leave."

    ssh "…And where you want me to wait for you, too. I don't want to have to wait for you for too long, and I especially don't want you to forget it, that would really be the worst."

    hi "I'm sure you would come drag me out of here if I were to forget our date."
    
    show shizu adjust_blush
    with charachange

    "Her face reddens slightly at the word “date.” I can't help but smile a little at this."
    
    show shizu cross_angry
    with charachange

    ssh "That wouldn't be proper that all, you would seriously have me come here to have to remind you about something like that? Don't even joke about that!"
    
    show shizu adjust_frown
    with charachange
    show shizu behind_frown
    with charachange
    with Pause(1.0)
    show shizu adjust_frown
    with charachange

    "She adjusts her glasses, and barely ten seconds pass before she does it again."

    "I was going to ask her when she would like the date to be, but I guess she's leaving this, too, up to my judgement."

    "It's pretty obvious that she really feels the need to be on top of this, though. It's probably killing her to not know."
    "What a leap of faith, then, to leave it all up to my discretion. I wonder how she would feel if she knew how bad I was at this sort of stuff."

    hi "How about at one?"
    
    show shizu basic_normal
    with charachange
    
    ssh "Okay. By the front of the school?"

    hi "Yeah."

    ssh "Okay…"

    "She closes her eyes and taps the side of her head, committing it to memory. Finished, she toys with the temple of her glasses as if to straighten them once again."
    
    show shizu adjust_happy
    with charachange

    ssh "I'm looking forward to it. That doesn't mean that you have to try too hard, though. You'll just end up looking stupid if you do."

    ssh "Bye."
    
    hide shizu 
    with charaexit
    
    stop music fadeout 2.0
    scene bg school_dormhisao
    play sound sfx_doorclose
    with locationchange

    "Turning quickly, she leaves the dorms without waiting for a reply. I close the door and immediately fall facefirst into bed."

    "I can't say with 100\% certainty what time it is, but I've gotten pretty good at guessing it from the amount of light coming in through the window. Give or take half an hour, I can get it right nine times out of ten… unless it's raining or something."

    "The more time passes, the more anxiety I start to feel. I really, really haven't thought any of this through, have I?"

    "Well, not having a plan can be… acceptable at times. In some cases. A date could be one of those, right? I think Shizune would probably hit me if I were to tell her that, but I believe that it's the truth."

    "Of course, I do need a general idea of where we're going to go first. Then, the momentum can take over, but I'm pretty sure winging everything from start to finish is not the best route to take."

    "Letting out a sigh, I wince when I consider the likelihood of me probably winding up doing that anyway."

    "But it was Shizune who told me to be more spontaneous, so…"
    
    scene bg school_dormhisao
    with locationskip
    
    play music music_daily fadein 1.0

    "I heat up a quick breakfast in the dorm kitchen and eat it at the desk in my room. The act of eating makes me wonder where Shizune would want to eat. It brings to mind that I have only seen her eat junk food."

    "Despite that, she has a great figure. Maybe it all goes to her chest."

    "By the time I start getting ready to go out, I realize I'm cutting the timing a little close. Despite that, I manage to run out to the front of the school a few seconds before 1 PM."
    
    scene bg school_gate
    with locationchange
    
    show shizu behind_frown
    with charaenter

    ssh "You are never early."

    "Checking my watch, I see that it is exactly one o' clock."

    hi "But I am punctual. Look at what time it is."

    "I tap my watch for emphasis and then wince as she plants her heel in my toe."
    
    show shizu behind_smile
    with charachange

    ssh "You seem smarter today."
    
    show shizu behind_blank
    with charachange

    "I'm tempted to make another smart remark, and open my mouth to deliver one, but can't really follow through and just drop it as Shizune shoots me a puzzled look. I can't resist saying something, anything."

    hi "You know, if you keep doing that, I'm going to need new shoes."
    
    show shizu adjust_happy
    with charachange

    "I get ready to dodge another foot-stomp, but Shizune instead resumes fiddling with her glasses."

    ssh "Don't worry, I'll take responsibility. I'll buy you a new pair."

    hi "That sounds like something I should say."

    show shizu adjust_blush
    with charachange
    
    ssh "You're… an idiot."

    "Her face flushes a deep red, but she manages to pull herself together and stands up with her back ramrod straight."
    
    show shizu basic_normal
    with charachange

    "What is she thinking about? It's making me nervous."

    ssh "Are we going to go now?"

    hi "Yeah, sure."
    
    scene bg school_road
    with locationchange

    "Shizune starts to walk towards town, turning her head to look back over her shoulder at me every few seconds to make sure I'm keeping up."
    
    show shizu basic_frown
    with charaenter
    hide shizu
    with charaexit

    "She looks a little annoyed having to keep on slowing down to less than her usual speed for me, but I've never understood why it always seems like she's in a rush. It fits her personality, but there's really no need for her to walk so quickly."

    "The impatient frown on her face is actually kind of cute, now that I think about it. I decide to tell her that the next time she looks at me."

    hi "Wait a second."
    
    show shizu basic_normal
    with charaenter

    shi "…?"

    hi "That expression you just made was kind of cute."

    "She doesn't respond, her eyes darting away from mine. She starts looking closely at the ground and begins to walk backwards down the path slowly and methodically. The ease with which she does this is amazing,"

    "…But it still seems unsafe. Still walking backwards, she signs:"

    ssh "What expression?"
    
    show shizu basic_sparkle
    with charachange
    show shizu basic_normal
    with charachange

    "I catch a glimpse of mischief in her eyes and the hint of a smile on her face before she looks away again. A feeling of dread overcomes me."

    "Could this be another game? She's toying with me again, and, worryingly, her eyes glitter with excitement when she discerns that I've caught on."
    
    show shizu basic_happy
    with charachange

    "She shifts her weight from one foot to the other, uncrossing her arms and letting them swing back and forth at her sides. Looks like she is really enjoying this. What about this is so fun that she feels so comfortable in the attack?"

    #"I'll play with her, though."
    
    return

label en_choiceS22:
    #another set of choices, because you wanted more choicesmenu:
    menu:
        with menueffect

        "I'll play with her, though."
    
        "Not this one.":
            return m1

        "Well, maybe it wasn't that cute.":
            return m2

        "You look cute when you're mad.":
            return m3

label en_S22a:
    #if you pick 1 or 2:
    
    show shizu adjust_frown
    with charachange

    "Shizune raises an eyebrow indignantly, but for the most part seems to accept this answer."

    ssh "So it appears you know how to play the game."

    hi "What game? What are you talking about? What is this game?"

    ssh "You know."

    hi "You mean the one where you mess with my head and put me in a bunch of lose-lose situations?"

    "I'm pretty sure that my sign language isn't good enough yet that she understood all of that."

    ssh "Yeah, that's right. More or less."
    
    show shizu behind_smile
    with charachange

    "She smiles warmly, seeming to momentarily lose herself in other thoughts, before she lets out a short, soundless giggle."

    ssh "Come on, let's pick it up a little."
    
    hide shizu 
    with charaexit

    "She turns to face the correct way and starts walking faster."

    return

label en_S22b:
    # if you pick 3
    
    show shizu cross_angry
    with charachange

    "Shizune frowns, even though her cheeks are rapidly turning a light shade of pink."

    ssh "You think my anger is funny?"

    hi "I didn't say funny, I said cute. And, yes."
    
    show shizu adjust_frown
    with charachange

    "She looks as though she's about to say something. Her fingers weave back and forth between each other thoughtfully, but in the end, her hands drop to her sides again."

    "Did I win?"
    
    show shizu behind_frown
    with charachange

    ssh "Okay, you win this one."

    "She signs it grudgingly, as if reading my mind, then a soft smile forms on her face."
    
    show shizu behind_smile
    with charachange

    ssh "Come on, let's pick it up a little."
    
    hide shizu
    with charaexit
    
    stop music fadeout 3.0

    "She turns to face the correct way and starts walking with a little more urgency."
    
    return

label en_S22c:

    #end split
    
    scene bg suburb_roadcenter
    play sound sfx_time
    with shorttimeskipsilent
    
    play music music_soothing fadein 2.0

    "In town, I make the mistake of asking Shizune if she wants to get something to eat, and we end up going to another fast food place. I guess this is really what she enjoys eating."

    "As I pay for our food, Shizune offers to pay for half. It's more than generous seeing as how she ordered twice as much as I did, meaning it's way more than half the bill. I still pay for everything out of etiquette, but it was nice of her to offer."

    "Since it's a beautiful day, Shizune quickly takes the boxes with our food in them and rushes out the door before I can even get my change."

    "By the time I'm out the door, she is already halfway down the street, although she has stopped to wait for me. As soon as I get close, she runs away again, until we end up at the same park I came to yesterday."

    scene bg suburb_park
    with locationchange
    play ambient sfx_park fadein 1.0
    
    "Seeing this place again so soon immediately reminds me of how sad Misha looked the other day."

    "I consider bringing it up with Shizune, but recalling Misha's words stop me from doing it. She had said that she would be fine as long as Shizune didn't know."

    "Nevertheless, I'm concerned. But Shizune looks so happy that I can't bring myself to talk about it. Partly, it's because I'm also enjoying our date. I can't ignore that fact."

    "I feel like a selfish and terrible person."
    
    show shizu behind_smile
    with charaenter

    ssh "We can sit down here."

    "Shizune signs to me after placing the food down on a little table in the shade. She taps her foot as she looks at me."
    
    show shizu behind_frustrated
    with charachange

    ssh "Come on, I can't eat unless you sit down and eat, too."

    hi "That's really polite."
    
    show shizu adjust_blush
    with charachange

    shi "…"
    
    show shizu adjust_frown
    with charachange

    "She pushes her glasses up and nose and then glares at me with a sense of urgency."

    ssh "The food is getting cold."
    
    show shizu adjust_frown at centersit
    with charamove
    
    stop music fadeout 2.0
    
    show shizu basic_normal at centersit
    with charachange

    "As we eat, a silence falls over us. It's a little strange to me, since I'm used to having conversation when I eat with people, but with Shizune, it seems like that would be kind of difficult."


    "As focused as she is on eating, anyway, she probably wouldn't pay attention even if I did try to sign something to her. The look of concentration on her face and the way she methodically picks apart her food and eats it is really interesting."

    "I find myself unable to eat because I'm distracted by it."

    "Eventually, we finish eating, but remain still in our seats at the table, our empty plates in front of us. Shizune plays absentmindedly with a plastic fork, bending it back and forth on the surface of the table."

    "After a short while, she puts it down and signs:"
    
    show shizu behind_sad at centersit
    with charachange
    
    ssh "Soon, I'll have to go back home."

    hi "What do you mean?"
    
    show shizu basic_angry at centersit
    with charachange

    ssh "A few times a every year, I have to go back to see my family. It's like a business trip."

    "She looks agitated. I can tell she isn't very comfortable talking about this, and the fact that she refers to it as a business trip doesn't strike me as a good thing."

    ssh "It's likely that I could be there for a week."

    hi "I'll go with you."

    "I choose my words carefully, making sure she sees them. It takes a while for her reply to come."
    
    show shizu basic_normal at centersit
    with charachange

    ssh "Okay. If you want to."

    "I try to read deeper into her expression, but Shizune's poker face has gotten a lot better, and it's a lost cause."

    ssh "It's getting late. I'm sorry, but I'm going to have to cut our date short."

    "The way she signs it to me, with her fingers slowly, thoughtfully cutting through the air, heavy with reluctance, makes it easier for me to take."

    hi "Alright."
    
    show shizu behind_frown at centersit
    with charachange

    ssh "I'm really sorry."

    "Shizune pauses."
    
    show shizu behind_smile
    with charamove

    ssh "I really enjoyed today."

    hi "I'm glad, but we didn't do a lot…"

    ssh "That is fine."
    
    show shizu behind_blank
    with charachange

    "She bites her lip and shrugs before continuing."

    ssh "I'll explain it some other time."

    ssh "…Do you want to go back together?"
    
    play music music_running fadein 1.0
    
    show shizu basic_happy
    with charachange
    show shizu basic_happy at offscreenright
    with charafast
    hide shizu

    "With that, Shizune offers me her arm. As soon as I reach out to take it, however, she starts running before I barely manage to touch the sleeve of her blouse."
   
    "She laughs playfully, waving me over towards her, and daring me to try again. Is this a game of tag, now?"

    "Okay, I'll play along this time, too."

    "Ignoring the shortness of my breath, I chase Shizune all the way back to the dorms."
    
    stop music fadeout 3.0
    stop ambient fadeout 1.0
    
    scene black
    with dissolve

    return

label en_S23:
    
    scene bg school_dormhisao
    with locationchange
    play music music_daily fadein 0.5
    
    "Today, I'll get to see Shizune's home."

    "It's odd, all this time, I've never given any thought to what Shizune's house would look like. I've only wondered what her dorm room looked like."

    "I don't know anything about Shizune's family, so any attempt at guessing what her home is like would just be that: a guess. It's not too big a concern of mine, since I'll be able to see it in a little while."

    "What I want to know more about, in any case, is Shizune's family. Shizune has never mentioned them once, so the prospect of meeting them is very interesting."

    "I finish tying my tie in a standard windsor knot and put on my jacket, getting nervous when my fingers brush over a small hole in one of the sleeves that I had never noticed before."

    "In retrospect, I suppose this jacket has been through a lot on my behalf. Maybe I should at the very least get a spare."
    
    scene bg school_dormhallway
    with locationchange

    "Shizune, Misha, and I agreed to meet up at the front gate of the school. Shizune had said that with a location that obvious, it would be impossible even for me to not see them."

    scene bg school_dormext_full
    with locationchange
    
    "I think I am getting used to Shizune being my girlfriend. I had expected everything to change when I made my confession, but for the most part, she is still the same girl as she always was."

    scene bg school_gate
    with locationchange
    
    "Running across the grounds, I quickly catch sight of Shizune and Misha waiting impatiently by the gate."
    
    show shizu behind_blank_cas at center
    with charaenter

    "Shizune is wearing a sharp, fashionable dress."
    
    "It makes sense, since we're on holiday, but it's still jarring. It's almost too much for a quiet place like Yamaku. Thinking back to what she wore at the Tanabata festival, I'm starting to notice a trend with her."
    
    "All of her clothes are very tasteful and mature; very well thought out. So, then, I wonder why she herself is so immature."
    
    show bg school_gate at bgright
    show shizu behind_blank_cas at tworight
    with charamove
    
    show misha perky_smile_cas at twoleft
    with charaenter

    "Misha's outfit is a little less thought out. She is wearing a skirt and a t-shirt with something written in English on it. “Bush/Cheney 2004?”"

    hi "That's, uh… an interesting shirt."

    mi "Eh?"

    hi "Do you know what it says on it?"

    "An expression halfway between concern and confusion appears on her face."
    
    show misha perky_confused_cas at twoleft
    with charachange

    mi "Hm… Not really, Hicchan. What does it say? Is it something dirty?"

    hi "No. Where did you get it?"

    mi "I… don't know."

    "I decide to let it drop for now."

    "She is still having a hard time trying to balance that immense suitcase on her head, struggling visibly with the effort."

    "Shizune has packed far more sensibly, having just two small bags at her side. When she sees me, she gives me a wave. Misha hops up and down a few times in acknowledgement, her hands fumbling with her suitcase."

    show misha sign_smile_cas at twoleft
    with charachange

    mi "Ready to go, Hicchan~?"

    hi "Yeah."
    
    show shizu basic_normal_cas at tworight
    with charachange

    ssh "You seem to be traveling light."

    hi "Well, it's only going to be a few days, right?"
    
    show shizu adjust_frown_cas at tworight
    with charachange

    "Shizune looks at her own luggage and frowns."

    ssh "You packed less than I did. How insulting."

    hi "Huh?"

    ssh "You will look very foolish and very rude carrying less luggage than a lady, Hisao. You should have packed more than me, to be polite."
    
    show shizu adjust_smug_cas at tworight
    with charachange

    ssh "However, your shortsightedness plays out to my advantage. We are now switching bags."

    "With that, she quickly takes my bag from me and starts walking toward the station."
    
    show shizu adjust_smug_cas at offscreenright
    with charamove

    mi "Hey, Shizune…"
    
    show misha sign_sad_cas at center
    show bg school_gate at center
    with charamove

    "Misha whines, barely holding up under her massive suitcase, so large that it covers her from the sun. She looks like Atlas holding up the world."

    "Of course, with her back to Misha, Shizune doesn't hear her at all. Misha lets out a sigh, then quickly lets her suitcase fall off her back, almost being pulled down with it."
    
    show misha hips_grin_cas 
    with charachange

    mi "Hicchan~! It's the same for me, too, right? Right? Okay~! Okay, okay, okay~!"

    mi "I'll carry Shizune's bags, and you can carry mine! Wahahaha~!"

    hi "I don't think so."

    mi "Aw, come on!"

    hi "No."

    "She has to be kidding. If this thing were any larger it would be the size of a compact car. The sinister dark pea color also gives me an uneasy vibe. Misha's luggage looks like something used to transport bodies."

    hi "Why did you pack so much, anyway? What's in here? Where do you even get a suitcase this large?"
    
    show misha hips_smile_cas 
    with charachange

    mi "It's a secret, Hicchan. You aren't supposed to ask a girl what she has in her luggage, anyway, didn't you know?"

    "How eerily like something Shizune would say."

    "Noticing that she is walking towards the station alone, Shizune stops, spinning around to face us on her heel and stomping over."
    
    show bg school_gate at bgright
    show shizu adjust_angry_cas at tworight
    show misha hips_smile_cas at twoleft
    with charamove

    ssh "What are you two doing?"

    "She sees Misha holding my bags, and me trying to prop hers up against my leg."

    ssh "Are you making Hisao carry your luggage for you?"

    mi "Maybe…"

    ssh "You shouldn't tease him like that."

    mi "Huh?"

    hi "What?"

    "It's like I've stepped into a parallel universe where everything has been switched around except myself."
    
    show shizu adjust_smug_cas at tworight
    with charachange

    ssh "He is my boyfriend, so only I can do that."

    "There is a smile on her face as she signs it, but her fingers tiptoe around the word “boyfriend” unsteadily, as if grasping for something more."

    "Shizune seems to have problems with that word, a blush spreading across her face when she signs it. With her reserved personality, and the way she has gone on so many times about the weightiness of certain words, I can't say I'm surprised."

    show shizu basic_angry_cas
    
    ssh "We're going to be late unless we hurry."

    mi "Really, Shizune? We should hurry up, then~!"

    hi "Hey, seriously, what's in this thing?"
    
    show misha perky_smile_cas at twoleft
    with charachange

    mi "It's a secret, it's a secret~!"

    ssh "You are very nosy, you should respect a person's privacy."

    "An idea springs into my head."

    hi "Okay, but I'm just going to tell you ahead of time, I plan to ride this thing like a sled all the way down the mountain."
    
    show shizu cross_shock_cas at tworight
    show misha sign_confused_cas at twoleft
    with charachange

    "Misha starts frantically waving her hands, her face strained with a nervous grin. Shizune does the same."

    mi "No, no, you can't do that, Hicchan!"

    ssh "Don't do that!"

    hi "So, judging from your reactions, whatever is in here, it's pretty fragile, isn't it?"

    "I turn to Shizune, telling Misha to translate to her with a nod of my head to get it across as clearly as possible."

    hi "And, you clearly have something invested in the contents of this suitcase, or else you wouldn't have just lost your cool."
    
    show shizu adjust_frown_cas at tworight
    with charachange

    "I smile and nod arrogantly, content with my mental checkmate, then wince as Shizune throws my bag into my stomach."

    ssh "You are such an idiot."
    
    show shizu adjust_happy_cas at tworight
    show misha cross_laugh_cas at twoleft
    with charachange

    "Despite that, she raises her hand to her mouth to hide the fact that she is giggling. Misha breaks into a peal of hysteric laughter and gives me a quick, mocking salute."

    mi "Hahaha!"

    mi "That was nicely done, Hicchan~! Hahaha!"

    hi "Ah, thanks, I know it was. But I was being totally serious about riding it down the mountain, though."
    
    hide shizu
    hide misha
    with charaexit

    "Before they can stop me, I run ahead, pretending to lower the suitcase onto the ground like a sled."
    
    play sound sfx_impact
    with hpunch
    
    "I feel both of them grabbing me from behind, and lose my balance, sending all three of us to the ground; something that has happened quite a few times, actually, now that I think about it."

    
    stop music fadeout 2.0
    
    #lawl some kind of fade out

    #no train station background needed, and no train. I am skimping on these backgrounds

    #Transitions that skip plot-related shit are ballin

    scene bg city_trainstation
    show crowd
    play sound sfx_time
    play ambient sfx_crowd_outdoors fadein 1.0
    with shorttimeskipsilent
    
    "Disembarking from the train, I uncomfortably ease my way past my fellow passengers, dragging the massive suitcase behind me."

    "Looking at my watch, I see that this has been quite the long ride. I guess it's a good thing that I slept through most of it, then."

    "After carefully maneuvering my way down a heavily trafficked set of stairs, I find myself on a clean, mostly empty street lined with lavish and expensive-looking houses."
    
    stop ambient fadeout 1.0
    scene bg shizu_houseext
    with locationchange
    
    show shizu adjust_happy_cas at tworight
    show misha perky_smile_cas at twoleft
    with charaenter
    
    play music music_soothing fadein 0.5

    shi "…"

    hi "What? I didn't catch that."

    mi "Shizune is asking if you can guess which house is hers, Hicchan."

    "I look around. This is a very long street, there must be at least twenty houses here, and a lot of them look completely identical. In neat rows, they seem to stretch into infinity as they eventually disappear behind what looks to be a public park."

    hi "Well, these houses all look the same. I guess that's the point, isn't it?"
    
    show misha hips_grin_cas at twoleft
    with charachange

    mi "Yup!"

    hi "Then, that means this isn't very fair."

    ssh "Okay, I'll tell you."

    "With a grand gesture meant to build up suspense, she points her finger off into the distance."

    hi "…You live in the park?"
    
    show misha cross_laugh_cas at twoleft
    with charachange

    "Strange. As Misha laughs, I stop to consider that maybe Shizune could be homeless. It would explain why up until today I've only ever seen her in her school outfit. This seems like the kind of thing that a woman would want to hide, though."

    show shizu behind_smile_cas at tworight
    with charachange

    "As I'm continuing this train of thought, Shizune quickly jabs me in the shin with her heel playfully."

    ssh "No, of course not. Stop being silly. Those are the grounds."
    
    hide shizu
    hide misha
    with charaexit

    "I had had the feeling that Shizune's family was well off, but the grounds look to be so expansive that I can't find the house on them. I can only imagine what the actual house must look like, it could be a castle, for all I know."

    "The closer we get, the clearer it becomes that Shizune's house occupies an incredible amount of land. If it weren't for the imposing steel gates and the almost comically out-of-place mailbox with the Hakamichi name on it, this really could be a park."

    "As I dread the thought of carrying Misha's suitcase all the way to wherever the actual house may be, I breathe a sigh of relief when I see a car and driver waiting just beyond the gate. He bows politely and takes the luggage from my hands."

    "As the car starts moving, I try not to think about how vast the grounds must be if you need a driver to make it to the main house. This is a pretty nightmarish front yard."

    "As if reading my mind, Shizune looks at me and then quickly starts to sign."
    
    show shizu basic_normal_cas
    with charaenter

    ssh "It's not that far away to the house, this is just a one time thing because I thought you might be tired."

    ssh "It's really not that far."
    
    stop music fadeout 1.0

    "Despite that, it takes a very long time to finally arrive at the house, which looks… "
    
    scene bg shizu_houseext
    with shorttimeskip
    play music music_another fadein 0.5
    
    "exactly like the ones we had seen before on the street."
    
    hi "Huh?"

    "Shizune doesn't notice my surprise at all, not surprising seeing as how she is looking in a totally different direction."

    "Misha, however, looks over at me quizzically as we are more or less hauled into the reception room by an eclectic team of hired help."
    
    scene bg shizu_living
    with locationchange
    
    show misha hips_smile_cas
    with charaenter

    hi "Hey, why is this house exactly the same as the other houses we saw?"

    mi "What do you mean, Hicchan?"

    hi "I mean—" #reminder for the potential {nw} break
    
    play sound sfx_impact
    with vpunch

    "I am almost knocked to the floor as someone throws Misha's suitcase into my back."

    hi "What the hell?"

    hi "…Anyway, this house is exactly like the other houses we saw on the street…. You don't think so?"
    
    show misha perky_smile_cas
    with charachange

    mi "I never really noticed."

    hi "But they're the same color and everything. They are all the exact same house, just this one has illogically massive grounds. This is a big house and all, but you don't think it's weird that it's… You really never noticed that it's…?"

    show misha hips_grin_cas
    with charachange

    mi "Nope~! What are you talking about, Hicchan?"

    "There is the sneaking suspicion that she is playing with me, but Misha's innocuous smile dispels most of those thoughts."

    "Nevertheless…"
    
    hide misha 
    with charaexit

    "I tap Shizune on the shoulder and then start signing the same question to her, but I'm cut short by the sound of a door flying open."
    
    play sound sfx_impact2
    
    show jigoro neutral at center
    with charaenter

    "A very serious looking, giant bear-man is standing in the doorway in front of us. I assume he is Shizune's father."
    
    show jigoro neutral at rightwallopen
    with charamove
    
    show jigoro neutral at rightsit
    with charamove

    "Without even acknowledging our presence, he walks into the room almost stomping the ground with each step before taking a seat in an ornate chair. He stares at us harshly, waiting for us to sit down as well."

    "I find the closest seat and slide into it, dropping the suitcase in my hands onto the floor at my side before turning to face Shizune's father."

    hi "Hello."
    
    show misha perky_smile_cas at twoleftsit
    with charaenter
    
    mi "Hi."

    "Misha also chimes in with a polite greeting. I watch Shizune out of the corner of my eye. She seems to be staring at the floor, picking at her fingernails wistfully as her dad impassively looks at her expectantly."

    hi "I'm sure Shizune wants to say hello, too."

    "His head snaps up and he speaks for the first time."
    
    show jigoro angry at rightsit
    with charachange

    hx_ "Who?"
    
    show misha perky_sad_cas at twoleftsit
    with charachange

    "Misha bites down on her tongue, suddenly looking very pained."

    "I wonder for a second if this is not Shizune's father, but I can't think of a polite way to ask who he might be."

    hi "Shizune—" #reminder for the potential {nw} break

    hx_ "I don't want to hear someone else's words coming out of your mouth. If there is someone in this room who wants to talk to me, I want to hear them, not you, boy. Who are you, anyway?"

    "The aura of hostility this man projects is so thick I can almost feel it pushing me back like a solid wall."

    hi "I'm Hisao Nakai. I'm your daughter's boyfriend."
    
    show jigoro laugh at rightsit
    with charachange

    "To my amazement, he starts laughing. It makes me angry, what does he find so funny?"

    hx_ "Really? I see. I have some respect for you now. I have some matters to discuss with Shizune now, I would appreciate it if you would please leave us alone for a bit. Feel free to wander around the grounds at your leisure."

    hi "Hey…"
    
    show jigoro neutral at rightsit
    with charachange

    hx_ "What is it?"

    hi "What are you going to discuss? I can translate it, a little."
    
    show misha sign_smile_cas at twoleftsit
    with charachange

    "Misha jumps in, finally finding her voice."

    mi "It's okay, Hicchan, after all, that's my job, isn't it~?"
    
    show jigoro angry at rightsit
    with charachange
    
    show misha perky_sad_cas at twoleftsit
    with charachange

    hx_ "You, be quiet. I don't like hearing your kind unless it is absolutely necessary."
    
    show jigoro smug at rightsit
    with charachange
    

    
    hx_ "Anyway, Nakai, in spite of that, she has a point. I can communicate through this… "
    
    show sc_comp at Transform(alpha=0.0,xalign=0.5, yanchor=0.5, ypos=0.7, subpixel=True)
    with None
    show sc_comp at Transform(alpha=1.0,xalign=0.5, yanchor=0.5, ypos=0.5, subpixel=True)    
    with dissolvecharamovefast    
    
    with Pause(0.5)
    
    "He points to an ancient-looking, black laptop sitting on the table."
    
    show sc_comp at Transform(alpha=1.0,xalign=0.5, yanchor=0.5, ypos=0.5, subpixel=True)
    with None
    show sc_comp at Transform(alpha=0.0,xalign=0.5, yanchor=0.5, ypos=0.7, subpixel=True)
    with dissolvecharamovefast
    
    hide sc_comp
    with None
    
    hx_ "So you are not needed here. There are two guest rooms, feel free to pick whichever one you want. They are the ones marked “Guest.”"

    "I can't take more of his attitude. I have never met anyone more combative, it's like his intent is to actively antagonize Shizune, Misha, and I. I can feel it pushing me down like an actual force of some sort."

    hi "Who are you to say something like that?"
    
    show jigoro angry at rightsit
    with charachange

    "He frowns and places his hand on his chin as if thinking it over momentarily."

    hx_ "Who am I? Who am I? I know who I am. Do you know who you are? Who are you?"

    hi "Hisao Nakai."

    hx_ "Shut up. Who are you?"

    hx_ "Who are you to tell me how to live my life? Do you know who I am? Do you know the things I have been through? The things I have seen? The things I have done? You could never even comprehend it. You are just a child."

    hx_ "You wouldn't understand in a million years, not even if I were to walk across this room right now and punch you in the forehead with brass knuckles with a brief chronicle of my life experiences on them, leaving my autobiography imprinted on your face."

    "He pauses."

    hx_ "And I asked you a question, boy. Who are you?"

    "…"

    hx_ "I'm going to have to ask you to leave. On your way out, there is a table to your right with copies of my autobiography. You may take one if you so choose."

    hide jigoro
    hide misha
    with charaexit
    
    show shizu behind_sad_cas
    with charaenter
    
    "I open my mouth to protest, but Shizune looks at me as if she does not want me to say anymore, and Misha seems to share this opinion with her, hurriedly trying to push me out the door."
    
    stop music fadeout 2.0

    "For now, I guess there isn't anything I can do. I feel powerless, and the feeling is compounded as I glimpse the look on Shizune's face. She looks so sad and distant, and understandably so."

    "I remember how she looked the same way when she told me that she had been called back home. It's the same expression as from that time. And up until we had stepped into this house, she had seemed happy."

    "I briefly consider storming back in and punching Shizune's dad in the face, but that is just a fantasy. I can't leave it at this. I feel compelled to do something, but I know there is nothing I can do."
    
    play music music_soothing fadein 0.5
    scene bg shizu_park
    with locationchange

    "Sickened by my inability to do anything, I find it very hard to appreciate how nice the grounds of Shizune's house are. The grass is soft and springy and seems to go on for miles. The air is unimaginably fresh and everything is so green."

    "It is a very peaceful and soothing atmosphere, but there is an everpresent bitterness lingering in the back of my mind that won't go away and prevents me from enjoying it."

    mystery "Hi! Who are you?"

    "The voice comes from behind me. It sounds high-pitched and enthusiastic, like a child's."
    
    show hideaki surprise at center
    with charaenter

    "Turning around, I see a slim-figured girl in shorts standing in front of me. With those glasses and that dark, short hair, she looks a lot like Shizune. She looks younger than Shizune, though. Maybe this is her little sister."

    hi "Hi. I'm Hisao Nakai. I guess you would want to know what an unfamiliar guy is doing walking around your property, huh?"

    hi "I'm a friend of Shizune. From school. She's in the house if you want to see her."
    
    show hideaki happy
    with charachange

    hh_ "Really? I'm glad Shizune is back. It's very nice to meet you, too, I'm Hideaki Hakamichi."

    "Hideaki? That means this person is a man. I was about to say that I hadn't known Shizune had a sister. I really dodged a bullet here."

    hi "I didn't know Shizune had a brother, but I kind of figured you two were related. So she is your big sister?"
    
    show hideaki normal
    with charachange

    "Immediately, Hideaki's amiable smile fades into a neutral one with a hint of chagrin to it."

    hh "What do you mean by that? How did you suspect we were related? Are you saying that I have a physical similarity to my older sister that may give away the fact that we share the same blood? Are you saying we look alike?"

    hi "…So, she is your older sister."
    
    show hideaki thinking
    with charachange

    "Hideaki bites his lip."

    hh "I suspect you have met my father, Jigoro?"

    hi "Yeah, I have. He's, uh…."

    "What can I say?"
    
    show hideaki normal
    with charachange

    hh "I am aware that you may not agree with the way that my father sees my sister. I wish he would be a little easier on her at times, too. I don't really harbor any ill will towards her."

    "Letting out a tired sigh, he adjusts his glasses in a way that is identical to how Shizune does it. It must be a family thing. He certainly seems as sharp as Shizune is, and the way he speaks is very clear and educated."

    show hideaki darkside
    with charachange
    
    hh "I hope you are aware, however, that I must destroy her."

    hi "Huh?"

    "What?"
    
    show hideaki serious_up
    with charachange

    hh "I am two years younger than Shizune, but currently, I stand in line to inherit the family business. It is less a question of gender, or even competence. It is because of her condition."

    hh "Solely because of that, I believe. Therefore, it is my goal to surpass her in everything. Then, I will be a man who stands on his own merit. I love my sister, but for one person to move up, another must be knocked down."

    hh "I have to be better than her. More driven and more competitive. Better. Faster. Stronger."

    hh "Every morning, I wake up, and I brainstorm ways in which I can put myself above Shizune, or lower Shizune's power. When I eat breakfast, I think “I am going to eat this so I can gain sustenance from it and stay alive so I can surpass Shizune.”"
    
    show hideaki closed_up
    with charachange

    hh "You must think I'm a terrible person."

    "I don't know how to react. How can he say that with such an innocent and nonchalant face? I can detect regret in his voice, however, and I know that he really does not like the fact that he thinks in such a way."

    "But he is right; for one person to move forward, someone else has to be forced the other way. This, however, is too extreme."

    "I can't bring myself to dislike Hideaki, though, because he seems to genuinely care for Shizune, even with all his talk of destroying her. I think if he had the opportunity to, he wouldn't."

    show hideaki normal
    with charachange
    
    hh "You're her boyfriend, aren't you?"

    hi "Yes, I am."

    "He looks me up and down."
    
    show hideaki confused
    with charachange

    hh "You seem like a nice guy. Why do you like my sister?"

    "At first, it sounds like he is putting her down, but there seems to be real curiosity there."

    "Why do I like Shizune? Even now I don't know if I can really put the answer into words. Can I really simplify it so easily?"

    hi "I like her because I fell in love with her. It's as simple as that. I don't think I could get you to understand it unless I told you it all from the beginning, so that's all I can say for now."

    show hideaki serious
    with charachange
    
    hh "….I see. I guess there is no way around it, then."

    hh "I want to gauge your intelligence. A problem: I have twelve 10 yen coins. One of these coins is counterfeit. I have a balancing scale, and can use it a maximum of three times. How would I find the counterfeit coin, Professor?"

    #hi "Hm…"

    return

label en_choiceS23:
    menu:
        with menueffect
        
        hi "Hm…"
        
        # lawl three choices with the same outcome
        "Well you would weigh them three times…":
            return m1
        
        "You would only need to weight them twice…":
            return m2

        "It's simple, you don't even need the scale…":
            return m3

label en_S23a:
    
    show hideaki normal
    with charachange

    hh "No, idiot."

    hi "Huh?"

    hh "If I have twelve 10 yen coins, and one of them is fake and therefore unusable, I would have 110 yen. I could barely afford a candy bar with that."

    hh "I would take all the coins and go buy a candy bar, because I don't care enough to measure out the weight differences of a handful of pocket change and can't be bothered with something so stupid. You should have known this."

    show hideaki evil
    with charachange
    
    hh "Even Shizune would have known this. You are inferior to Shizune. Thank you, this means my greatest threat is still Shizune."

    hi "So… this was a trick question?"
    
    show hideaki surprise
    with charachange

    "Hideaki laughs, looking surprised."

    hh "Hahaha."
    
    show hideaki happy
    with charachange

    hh "A normal person would get angry. Okay, I think you're an okay guy for my sister."

    hh "She has never had a boyfriend before."

    hi "I know."
    
    show hideaki thinking
    with charachange

    "He nods distantly."

    hh "As long as you understand, then."
    
    show hideaki normal
    with charachange

    hh "So what were you doing before? Touring the grounds?"

    hi "Something like that, but they're really expansive. I guess you could say I was wandering around, to be more accurate."

    hh "Alright, then I'll give you a tour. I have some time, anyway."

    "Taking a quick glance at his watch, he nods satisfactorily when he confirms he has “enough time.”"
    
    show hideaki happy_up
    with charachange

    hh "I have a girlfriend of my own."

    hi "Hey, before we start, can I ask you a question? Why does the house look exactly like all the other houses in this area?"
    
    show hideaki closed_up
    with charachange

    hh "Hm… well, I'll let you figure that one out on your own. It's another riddle. You are sharp enough that my sister likes you, and that you could like my sister, so consider it another test."

    "After a quick tour of the grounds, which include an assortment of benches and fountains much like a real park, it starts getting dark, and Hideaki asks if I want to head inside and eat dinner."
    stop music fadeout 1.0
    scene bg shizu_living
    with shorttimeskip

    play music music_another fadein 1.5
    
    "The long table is eerily empty at dinnertime. There is no sign of Shizune, Misha, Shizune's father, or Shizune's mother. Hideaki doesn't seem bothered by this, helping himself to heaping servings of potatoes and beef with childlike relish."

    "I don't feel particularly hungry at first, but this is the first meal of the day, so I end up overeating a little."
    
    scene bg shizu_guesthisao
    with locationchange

    "After dinner, I find my luggage waiting for me in front of one of the guest rooms. Misha seems to have occupied the other one, and the lights are out, so I take that as I sign that she does not want to be disturbed."

    "I can only imagine what she went through today. She must feel terrible."

    "Entering my temporary quarters for the next few days, I slide into the bed, which is far more comfortable than the one in my dorm room. There is no contest. Even for a guest room, this is quite luxurious."

    "Although I have trouble falling asleep, it comes to me eventually."
    
    stop music fadeout 2.5
    scene black
    with shuteye
    
    return

label en_S24:
    
    scene bg shizu_guesthisao
    with openeye
    
    play music music_another fadein 0.5

    "I wake up, feeling incredibly refreshed. This was the best sleep I've had in possibly years."

    "If only my doom room mattress was this comfortable. For a second, I mull over the idea of stealing it, but the idea seems less and less plausible every time I think about how I would accomplish this."

    "After stretching my arms and legs out a little, I stand up to take a shower out of habit, and scold myself for forgetting where I am. This raises a good question, though:"

    "Where is the bathroom in this house? I suppose I should have asked someone yesterday, but hindsight is 20/20. I open the door to go look for it and find Hideaki standing stoically in front of me. I jump back in surprise."

    show hideaki normal at center
    with charaenter

    hi "Aah!"

    hh "Good morning to you, too."

    hi "You surprised me."
    
    show hideaki happy
    with charachange

    hh "I know. That was the intent."

    hh "Normally, if someone unexpectedly greets you at the door, the smart thing to do would be to attack them to neutralize their potential as a threat. But you did not do that. Shizune would have done that."

    show hideaki thinking
    with charachange

    "He pauses and nods his head very softly, a thoughtful look on his face."

    "I try to dismiss what I just heard as him caring very deeply for his sister. It must be nice to have a brother who's always thinking about you. Almost makes me wish I had a sibling."

    hi "Hey, wouldn't that be assault?"
    
    show hideaki normal
    with charachange

    hh "No, it would be a misunderstanding. …Mistakes have been made, in the past. How are you? Did you sleep well?"

    hi "Yeah, I did. Do you know where I can find the bathroom?"
    
    show hideaki serious
    with charachange

    hh "Yes. It's down the hall, the last door on the right. It's not the only bathroom in the house, though. I will leave it to you to find the remaining bathrooms, and hide a coded message in each one. Assemble them all and I'll give you money."

    hi "Huh?"

    "It seems like Hideaki likes to kid around as much as Shizune."

    hi "Heh, that's funny."
    
    show hideaki confused
    with charachange

    hh "What is the joke?"

    hi "What? So you're not…?"
    
    show hideaki closed_up
    with charachange

    "He closes his eyes and turns his head from side-to-side emphatically."
    
    show hideaki normal
    with charachange

    hh "Anyway, I just wanted to tell you that breakfast will be served late today. I arranged for this because I did not know what time you usually wake up, and was taking that into consideration to be a better host."

    hh "We're having a western style breakfast. It is very hearty, but a more traditional breakfast can also be arranged, if you want."

    hh "Would Shizune have done this? Am I a better host than Shizune?"
    
    show hideaki serious
    with charachange

    "Hideaki leans in closer expectantly, a trait that it appears is shared between him and Shizune. He looks intently at me, waiting for my answer. This level of competition is really too much. How does he not explode or something?"

    return

label en_choiceS24:
    menu:
        with menueffect
        
        "Well, this is pretty accomodating behavior, so maybe I should say yes. Then again, I have this urge to say “no” just to mess with him."

        "Yes.":
            return m1
        
        "No.":
            return m2

label en_S24a:

    #choice incoming

    #1) Yes

    "I should say yes. Although his motives are questionable, he did go out of his way for me. He is also reminding me of Yuuko, a little."

    hi "Yes."
    
    show hideaki evil
    with charachange

    "Hideaki tents his fingers in satisfaction."

    hh "This is a good day."

    return

label en_S24b:

    #2) No

    "I decide to say no, just to kid with him a little."

    hi "No, she's a better host. You're close, though."
    
    show hideaki angry
    with charachange

    hh "Damn!"
    
    show hideaki thinking
    with charachange

    "Hideaki hits his palm with his fist and frowns before letting out a defeated sigh and regaining his usual composure. He rubs his temples, deep in thought, and then cooly says:"

    show hideaki serious_up
    with charachange
    
    hh "Okay, let's go to a club."

    "As impressed as I am by his hospitality, this is too much. I also question the legality of him going to whatever kind of club he might be thinking of."

    hi "It's okay. I was just kidding, you're very hospitable."

    hh "I see."

    return

label en_S24c:

    #choices over
    
    show hideaki normal_up
    with charachange

    "His expression softens."

    hh "How has Shizune been doing at school? Not just her grades. Is she getting along with everyone?"

    hh "…Not that I want to know, of course. It's just that I need to know how she is doing, since she is my rival and all. I need this information so I can better plot out how to destroy her. Although I suppose since you like her, you aren't a reliable source."

    hh "Usually, Shizune has not had many friends. Because of that, I have to call into consideration the motives of anyone who befriends her."

    hh "Just because of Shizune's condition, she shouldn't be taken lightly, or thought of as vulnerable. She can probably kill any person who is not me with her bare hands. But not me, because I have specifically trained to defeat her."

    show hideaki happy
    with charachange
    
    "He smiles, which is an unbelievably huge relief to me, because for a while there I had thought he was serious about that last thing. Please let him have been joking about that, please."

    show hideaki normal
    with charachange

    hh "I do not want anyone looking down on Shizune. I do not want anyone thinking she can be used. Shizune isn't stupid. Of course, you probably know that, at least. She is my enemy and any insult against her is an insult against me."

    hh "I have some respect for her."

    "There are breaks between his words that tell me it's very hard for him to say them, but I can see where he is going with this. So, he really does care about Shizune. It's an interesting way of showing it, but my first impression of him was right."

    hi "I think it's nice you're so concerned for her."
    
    show hideaki ohshit
    with charachange

    "Almost comically, he suddenly freezes. Everything stops, even his breathing, as if he suddenly turned to stone. It takes him a while to recover, to the point where I start to worry I may have caused him a heart attack."

    show hideaki angry
    with charachange
    
    hh "That is not funny. We are never revisiting this again, hopefully."
    
    show hideaki normal_up
    with charachange

    hh "You seem alright for my sister. Mikado, too. I'm really… sort of… …glad that she has such nice friends. Don't get too attached to her, though, since I will destroy her someday."

    "Mikado? He must mean Misha."

    hi "Thanks."

    hh "Yes. Anyway, breakfast will be in exactly two hours. If you need a snack or anything else before then, well, we are sort of understaffed at this exact moment, so I guess you can shout really loudly and I or someone will come to help you."

    hide hideaki
    with charaexit
    
    "With that, he gives a very conservative bow and leaves."
    
    scene bg shizu_living
    with locationskip

    "After showering, I kill some time before I head down to have breakfast. Hideaki is there, but I don't see any sign of Shizune, Misha, or Jigoro."
    
    show hideaki normal
    with charachange

    hh "Enjoying the meal?"

    hi "Yeah. I was just thinking that it's kind of empty here. And, hey, you're not really helping by sitting all the way on the other end of the table."
    
    show hideaki happy
    with charachange

    "Hideaki laughs. He has a very genuine laugh, but it's also very reserved and only just barely long enough to get the message across. If I had to describe it in one word, I'd call it efficient."

    hh "They are not as patient as you and decided to eat breakfast a little earlier. They are probably still eating outside, since the two of them thought it would be nice to enjoy their meal out on the grounds."

    hh "I assume you are very eager to go and find them."

    hi "How can you tell?"

    hh "You are inhaling your food."

    "I put my fork and knife down, a little ashamed. It's really because the food is delicious, and this is the first real, hearty meal I've had in a long, long time. Hanging out with Shizune and Misha, about half of my meals have been fast food."

    hi "Sorry."

    hh "It's okay. Go on, be with the woman you love. I heard that you know sign language. In fact, I heard that you learned it solely to communicate with her. Is that true?"

    "I'm hesitant to answer."
    
    show hideaki normal
    with charachange
    
    hh "…Hm."

    hh "My girlfriend wants to move to Africa. Can you believe it? Africa. There are areas of the continent that still do not know the discovery of the wheel. Terrible, isn't it? There is nothing there except for lions and AIDS."

    #That's Africa, folks. Lions and AIDS.
    
    show hideaki closed_up
    with charachange
    
    hh "I envy you, really. …Oh well. I'll mail you a postcard of myself standing next to a lion."
    
    
    "I finish the last of my bacon, eggs, and toast and attempt to take the dishes to the kitchen out of habit before Hideaki stops me and tells me that it won't be necessary. With that, I head outside for the grounds."
    
    stop music fadeout 2.0
    scene bg shizu_park
    with locationchange
    
    play ambient sfx_park fadein 1.0
    
    
    "In the light of the morning, they look even wider and more expansive than they did yesterday. I feel like I'm out in the wilderness, on some great plain, but a quick glance at the house behind me reminds me that I'm not."
    
    scene black
    with hands_in
    
    "A pair of hands covers my eyes from behind me. I am barely surprised, having been through this, what, three times already? At least that much."
    


    hi "Hi, Misha."

    "No ear-shattering laughter bursts like a grenade over my shoulder. Now I really am surprised. I try to turn around, but the person covering my eyes turns with me once before letting go."
    
    scene bg shizu_park
    show shizu behind_smile_cas
    with hands_out
    play music music_shizune

    ssh "Hello."

    "She waves, smiling warmly. Shizune looks infinitely better today, a far cry from how sullen and weary she looked yesterday. That's a relief. This cheerfully exuberant mood she seems to be in right now is a rare one for her, but it's my favorite."

    hi "Good morning."

    hi "I was looking forward to having breakfast with you and Misha, but I heard you guys decided to go ahead and eat without me."
    
    show shizu behind_blank_cas
    with charachange

    ssh "You eat very, very late."

    hi "I don't. You think that this is the usual time for me to eat breakfast? Because if that is what you think, you are wrong. I eat way earlier than this."

    ssh "And yet we are having this conversation."
    
    show shizu behind_smile_cas
    with charachange

    "Shizune laughs, covering her mouth with a dainty hand."

    ssh "I forgot to ask you what you think of my house. It's not bad, isn't it?"

    "I want to ask why it looks exactly the same as all the other houses, but I bite my tongue. It might be rude."

    hi "It's nice. How many guest rooms do you have? The one I slept in was very comfortable. So comfortable I want to take the mattress back to school."

    ssh "Is that so? Go ahead, then, it's yours."

    hi "Are you serious?"
    
    show shizu basic_sparkle_cas
    with charachange

    "Her eyes flash mischievously."

    ssh "Of course. I'll let you take anything in the house that you want, as long as you carry it yourself."

    hi "I knew there was a catch."

    ssh "No, there isn't. I said anything you want. I would consider it a personal favor if you were to take something of Hideaki's."
    
    show shizu basic_normal2_cas
    with charachange

    ssh "Have you seen Misha?"

    hi "No, I just got here. I thought she was with you."

    "She shrugs nonchalantly, but I can see the concern in her face. There is a definite sense of urgency in the way she moves her hands and the way she shifts her weight from one foot to the other, as if unsure of which one to stand upon."

    ssh "She wanted to play hide-and-seek, and ran off before I could tell her to act her age."

    ssh "Help me look for her."
    
    hide shizu
    with charaexit

    "A command? It's been a while. I'd put up some resistance, but I'm interested in finding Misha as well, so it would be pointless. Somehow, I think Shizune knows this, and this is her idea of playing around with me."

    "I hope so, because it would validate all the previous times where I thought she was just kind of pushy."
    
    stop music fadeout 1.0

    "Eventually, not finding Misha anywhere, we decide to split up to cover more ground, and to meet back in fifteen minutes. After Shizune goes off in her own direction, I continue where I left off."

    "After about five more minutes of wandering aimlessly, I see a familiar bright pink haircut out of the corner of my eye and run as quickly as I can towards Misha, but the sound of a harsh voice makes me slow down."
    play music music_pearly fadein 2.0
    scene bg shizu_garden
    with locationchange
    
    show misha perky_sad_cas at center
    show jigoro angry at offscreenright
    with charaenter

    "Misha is there, but standing in front of her is Shizune's dad. Misha is stiff and shrinking before him with fear, cringing each time he speaks. My first instinct is to immediately step in, and I follow it, quickly making my way over to them."

    hi "Hi, Misha."
    
    show misha sign_smile_cas
    with charachange
    


    "Misha quickly returns my greeting by giving me a wave, looking eager to get out of here. Before we can make our exit, however, Jigoro Hakamichi moves in front of us with surprising speed."
    show misha perky_sad_cas at twoleft
    show jigoro angry at tworight
    with charamove
    
    hx "Hello, boy."

    hi "Hello."

    "His eyes are cold and piercing, as if he's trying to kill me with a gaze. I try my best to return it."

    hi "I've been looking for you, Misha. Shizune, too. I guess I found you, so I win the game, right? Let's go back."
    
    show jigoro neutral at tworight
    with charachange

    hx "Yes, please send her back. However, I would like to speak with you, Nakai."

    "I'm shocked that he wants to talk to me specifically, although I have a sneaking suspicion he just wants to chew me out for interrupting him while he was talking to Misha."

    "That is fine with me, though."

    hi "Misha, Shizune is waiting for you in front of the house. I'll come by in a few minutes, okay?"
    
    hide misha
    with charaexit
    
    show jigoro neutral at center
    with charamove

    "Misha nods and leaves. I haven't heard her speak all day. It only makes me angrier at Shizune's dad, who watches impassively as Misha leaves, and waits until she is completely out of sight before speaking."

    hx "You make a very poor white knight."

    hi "What do you want to talk to me about?"
    
    show jigoro angry
    with charachange

    hx "I was going to talk to you about your pink-haired intellectual sinkhole of a friend, but now I would like to shift the discussion to the subject of your sickening lack of manners. Your lack of manners, they are sickening."

    "I grit my teeth unconsciously."

    hi "I could say the same to you."
    
    show jigoro smug
    with charachange

    hx "That is not true. I have been extending my pinky this entire time. See?"

    "Seizing on the look of confusion that I can't stop from spreading across my face, he smirks with self-satisfaction before effortlessly continuing from what he was talking about before."

    hx "Anyway, as I was saying before, I would like to talk to you about your friend. The one who proves that the worst thing about the gene pool is that there is no lifeguard."

    hi "Stop talking about Misha like that. She has a name, you know."
    
    show jigoro neutral
    with charachange

    "He looks up slightly as if considering it as a possibility, then puts his hands out in front of me, as if measuring quantities of something in each one like a scale."

    hx "You already have some of my respect. Now, you can attempt to gain more, or lose it. Answer this question, please: Why do you defend Misha? Is it because you care about her?"

    hi "Yes."

    hx "Then, if you care about her, tell me: Have you noticed that that girl is very depressed?"
    
    stop music fadeout 3.0

    "I'm caught off guard. Of course I'd noticed it, but the fact that he noticed it too is a shock to me. A feeling of regret puts a sour taste in my mouth as I realize that I've been avoiding it this whole time."

    "How many times has it been that I made up my mind to talk to her about it, only to get sidetracked and forget about it completely? I feel sick."
    
    show jigoro angry
    with charachange
    play music music_moonlight fadein 5.0
    
    hx "So, you have. And yet, you haven't discussed it with her at all. You just stand by even though you can see what's wrong with her. Is that the behavior you display towards someone you care about?"

    hx "You probably think, and justify it with the thought, “I can't confront someone else's problem, that's their business and none of mine.” It is a common mentality. A disgusting one."

    hx "What is your excuse? If you noticed it, if you were smart enough to notice it, why did you do nothing? Please enlighten me. I want to know this. Did you merely forget? You meant to do it, but couldn't find the words, or the time?"

    hx "Was it because you doubted your power to speak with her? Is it fear that stops you from doing it? Is it just laziness, even? Or, could it be you hate her, and you want to see her in despair? Unlikely, but who knows, it could be. Is that it?"

    hx "Well?"

    "I don't know what I should say."

    hi "I forgot. That's all…"

    hx "Inaction, too, can be a crime. Your vapid, airheaded friend is sad, and you tell me that you can see it, but you forgot?"
    
    show jigoro neutral
    with charachange

    hx "Well, I suppose you could have said that you hoped everything would sort itself out. Then, I would have lost all respect for you. Your answer, although blisteringly stupid, allows me to maintain the small amount of less-dislike for you that I have."
    
    hx "Hope is a farce. Hope is a crutch, an enabler that people use to defend inaction and a lack of self-reliance and self-respect."
    hx "The concept of hope is something that I find very insulting, because “hope” really means gambling on the possibility that everything will turn out fine."

    show jigoro angry
    with charachange

    hx "Is that something to be encouraged? Blind dependence on luck? Of course not. Now, what will you do? Are you going to go back to my cripple daughter and her brainless friend and continue to do nothing, or will you punch her in the face?"

    hi "I'll talk to her."
    
    show jigoro laugh
    with charachange

    "It seems to have been the answer he had been waiting for. Jigoro lets out a gruff chuckle, and even the slightest hint of empathy disappears from his face."
    
    show jigoro smug
    with charachange

    hx "I doubt that very much, boy. Do you have the fortitude to do such a thing, really? It is the dream of every ignorant young boy to be the hero who saves the princess and slays the dragon, but reality is quite different."

    show jigoro angry
    with charachange

    hx "You are not a brave hero, the princess is oftentimes just a woman, and the dragon cannot be slain, if there is a dragon at all. That is why many choose to bow their heads and not try."

    hx "Only people with the requisite drive can succeed."
    hx "People with daring, who can trample over fear and disregard idealism to focus on doing, instead of theorizing, so that they do not have to regret, to find themselves saying “I wish,” “I should have done this, or that.”"

    show jigoro neutral
    with charachange
    
    hx "Tell me, Nakai, have you ever done anything great with your life? Have you ever done anything amazing, that set you apart, or are you content to be normal? Have you ever, even, done anything truly impulsive? Or even stupid, or dangerous?"

    "I guess I haven't."
    
    show jigoro smug
    with charachange
    
    stop music fadeout 1.0

    hx "…Ha."
    
    play music music_pearly fadein 4.0

    hx "Shizune sees you as her equal. What does that mean to you?"

    "Shizune sees me as her equal?"

    "I think about how Misha said everything was fine so long as Shizune could not tell she was sad. Can Shizune tell? Is there a possibility that she would know? If she could, would she talk to Misha about it?"

    "She probably would. How ironic. I knew Misha was depressed and said nothing. Shizune likely would, if only she knew. But she isn't guilty of inaction, I am."

    "Does Shizune have the drive that her dad is talking about? Yeah, how could she not? She's always working, spending more time working on the student council than some people do at actual paying jobs."

    "So why does he look down on her?"
    
    show jigoro angry
    with charachange

    hx "I look down on Shizune because she is genetically inferior. Aside from that, you want me to respect her work ethic? Dedication and ethic are not drive. Hard work and dedication without ambition only makes someone a very efficient tool."

    hi "So you think that Shizune just works for no reason? If there is one thing I know, it's that she always thinks things through before she does anything. So, why would she work for nothing?"

    hi "I think it's to prove that she can manage things. Like your company."
    
    show jigoro neutral
    with charachange

    hx "My son will inherit the business, he is not genetically flawed."

    "I can feel my anger flaring up at him, but it seems to be that that is what he wants me to do."

    hi "What's more driven than doing all that to prove a point to you? She also handles more work than any school employee I've ever seen, maybe more than the principal."
    hi "Isn't undertaking that kind of task proof of ambition? What's more ambitious than that?"

    hx "I will never consider Shizune equal to Hideaki."

    hi "So do you consider Hideaki your equal?"
    
    show jigoro laugh
    with charachange

    hx "Hahahahaha… That is a good one. That was funny. I am amused."
    
    show jigoro smug
    with charachange

    hx "Hideaki is not my equal until he kills me and takes over my company in a firey, bloody coup. Unfortunately for him, that will never happen, as I am ridiculously strong and he is pathetically weak in comparison."

    hx "We are done here for today. Goodbye."
    
    hide jigoro
    with charaexit

    "I have never felt more powerless in my life. I've never been brushed off like this, so rudely. Before I can say anything to Jigoro, though, he is already gone."

    "Feeling defeated, I walk back towards the house, my face burning with guilt as I think about Misha. I don't think I'll be able to look Shizune or Misha in the eyes. With each footstep, I even start to dread seeing them."
    
    stop ambient fadeout 1.0
    scene bg shizu_houseext
    with locationchange
    stop music fadeout 1.0

    "When I get back to the house, Shizune is waiting for me, leaning against the white house, methodically cleaning her glasses. Misha is nowhere in sight."
    play music music_daily
    show shizu basic_normal2_cas
    with charaenter

    hi "I'm back."

    hi "Did you see Misha?"

    ssh "Yes, she said was feeling tired, so she went inside. Why?"

    hi "I just have to talk to her about something."
    
    show shizu adjust_frown_cas
    with charachange

    "Shizune pushes her glasses up and stares at me, frowning."

    ssh "Are you feeling alright?"

    hi "Yeah."

    "I watch her hands fidget slightly as she searches for what to say next, finding myself unable to look directly at her."
    
    show shizu behind_sad_cas
    with charachange

    ssh "I'm sorry."

    hi "For what?"

    ssh "I saw a picture of my mother yesterday. It made me remember how affectionate she was. All this time, I haven't told you that I like you even once. I'm sorry."

    hi "It's okay."
    
    show shizu behind_blank_cas
    with charachange

    ssh "…Hisao, let's go somewhere tomorrow."

    hi "Where?"

    ssh "I'll think of something."

    "I look at her face and feel as though I want to hug her when I see the contemplative look on her face that appears just a bit wistful in this light, but I still feel weak, like there isn't enough strength in my arms."

    "Almost as if answering my wish, Shizune grabs my hand lightly, almost like for a handshake, and runs her thumb over the lines of my palm before letting go."
    
    show shizu behind_smile_cas
    with charachange

    ssh "Hey, I'm over here. Tomorrow, okay?"

    hi "Okay."

    "It's a date, then. But right now, I still have to walk to Misha. Excusing myself, I head inside to go look for her."
    
    hide shizu
    with charaexit
    
    stop music fadeout 1.0

    return

label en_S25:
    
    scene bg shizu_living
    with locationchange

    "I enter the house and scan the area, looking for Misha, but can't find her anywhere. I guess this means the only place she could be is her room, whichever one that is."

    "It seems like the guest rooms are all in one area, so I start there. It's not too difficult; my guest room is the first one, so I only have to knock on the door of each one from there."
    
    play sound sfx_doorknock2
    
    "Before I even get that far, though, I hear faint sounds of movement coming from behind the door to my right. I knock gently on it and wonder if this is Misha's room."

    "I hear the person on the other side get up and walk towards the door. When it opens, Misha is standing there, her arms dangling limply at her sides."

    play sound sfx_dooropen
    show misha perky_sad_cas
    with charaenter
    
    mi "Hi, Hicchan. Is there something that you need?"

    hi "Yeah, I kind of wanted to talk to you."

    mi "Oh."

    "She scrunches up her eyebrows in hesitation. Her facial expressions are as transparent as usual. I can see her tongue run over her teeth as she stands there, deep in thought."

    mi "Okay."

    mi "…Well, don't just stand there, Hicchan."
    
    scene bg shizu_guestbed
    with locationchange

    "She stands to the side to let me in. I notice Misha's guest room is identical to my own, down to the smallest detail, and, on that note, that both rooms are depressingly white and sterile, like those in a hospital."

    "Misha quietly sits on the bed, looking expectantly at me as she cleans her fingernails with an air of agitation. She only waits a minute for me to speak, cutting through the silence on her own before I can finish formulating my thoughts."

    show misha perky_sad_cas
    with charaenter

    mi "I always get a little depressed around this time of year, Hicchan. It's nothing to worry about."

    "She seems to know why I'm here."
    
    play music music_sadness fadein 5.0

    hi "You've said that at least five times now. So, it is something to worry about. I'm worried about it."

    hi "If Shizune knew, she would be worried about you too."
    
    show misha perky_smile_cas
    with charachange

    mi "It can't be helped, Hicchan. And I'm not sad at all. Didn't I tell you, Hicchan? I'm happier now than I have ever been."

    mi "I made a friend. That's you, Hicchan~! And, Shicchan made a friend. So~! All in all, this was a good year."

    mi "…Yeah…"

    hi "Then why are you acting so depressed?"
    
    show misha perky_sad_cas
    with charachange

    "Misha flinches at my sudden question, tensing up as if she is expecting to be hit. I immediately regret saying it so harshly."

    mi "We're going to be graduating soon, isn't it normal to feel a little sad? I'm going to have to say goodbye to you and Shicchan."

    "I never thought about it like that before. She has a point. After this year, which seemed so long before this moment, but seems so short now in retrospect, what will happen?"

    "We're all from somewhere different, and school is the common thread that pulled us together. When we graduate, are we going to drift apart?"

    "It wouldn't be the first time."

    "It's painful to think about. When I think of how little time I've spent with Shizune, it's like a knife in my heart."

    "Time. If only there was more time. I try not to think about the grander implications of that sentence."

    hi "It's not like people can never see each other again after graduation. I'm going to try to keep in touch, and you and Shizune are so close. Do you think graduating from high school really means the end of everything?"

    hi "You just have to try."
    
    show misha perky_smile_cas
    with charachange

    mi "You're so inspirational, Hicchan."

    "The way she says it is so terribly sad, and so hollow that I know she doesn't believe it for a second. The air is choking me, and this room, it seems smaller now than before."

    hi "Don't just dismiss it like that."

    mi "It's more than that, Hicchan."

    hi "Then, what is it?"
    
    show misha perky_sad_cas
    with charachange

    "Misha's eyes dart from side-to-side, and up and down. Her breath catches in her throat, and she stops moving entirely before letting out a subdued sigh."

    mi "Hicchan, I wish you and me could change places."

    hi "What do you mean?"

    mi "Shicchan~… really loves you. You might be the first person she has ever really loved in that way, too. Do you notice the way she looks at you, Hicchan?"

    mi "I wish she could look at me that way."

    hi "What are you saying?"

    mi "I love her."

    mi "I'm in love with Shicchan. I love her."

    mi "…Geez, Hicchan, you're so slow~…"
    
    show misha hips_laugh_cas
    with charachange

    mi "Hahaha~!"
    
    show misha hips_grin_cas
    with charachange

    "Even though she puts on her trademark grin, there is unmistakable anxiety tinging her laughter that gives it a hollow ring. It feels like she is almost running from what she just said, which brings home the full meaning of her words."
    
    show misha perky_sad_cas
    with charachange
    
    "She lowers her head when she sees the blank expression of shock on my face."

    mi "It's true. Ah, you're probably shocked. That's normal."

    mi "I confessed my feelings to Shicchan once, too."

    mi "She can't love me in the same way."

    mi "I wasn't surprised… Maybe I knew that it was impossible. But, I said what I said. Something that can never be taken back. …That is why, Hicchan. If Shicchan thinks I'm depressed, she will blame herself."

    mi "She is the kind of person who can't separate herself from bearing burdens. At first, I resented her, because she continued to be my friend afterwards."

    "I can see droplets of tears forming in the corners of her eyes and it's like if I touch her, she would shatter to pieces."

    mi "I realized that that is also a kind of love. It's just not the same, though. And in the end, I fell in love again~…"

    mi "Stupid, stupid~."

    mi "In the end, I couldn't stop myself from being a selfish person."
    
    mi "So~! …I love her more and more every day, now. I thought I would be okay if I was able to just be with her, but now that we're going to be graduating, our lives will go in different directions."

    show misha perky_smile_cas
    with charachange
    
    "With a smile, she points to the right with left hand, and then to the left with her right."

    mi "Like this~!"

    mi "And Shicchan should be happy in her direction."
    
    show misha sign_sad_cas
    with charachange

    mi "So~! Everything is for Shicchan."

    mi "So… Please be a good replacement for me, Hicchan."

    hi "Hey, you make it sound like you're dying or something."

    mi "No, of course not. But Shicchan fell in love with you, and you told her you love her back."
    
    show misha cross_smile_cas
    with charachange

    "Misha's mouth curls into an impish smile."

    mi "So, I'm going to make sure that you make Shicchan happy. Understood, Hicchan?"

    mi "I won't accept anything else."

    "She lets out a warm giggle, and I can see that she's more like her old self. I'm glad that the dark cloud over her seems to have dissipated and respond in kind."

    hi "You sound kind of like her, there."
    
    show misha cross_laugh_cas
    with charachange

    mi "Ahahahaha~!"
    
    show misha cross_grin_cas
    with charachange

    stop music fadeout 5.0
    
    "Misha smiles a little more genuinely this time."

    mi "I feel much better now."

    hi "I'm happy about that."

    "I take another glance around the room. She didn't really make herself at home here, although since I can't recall hearing it said to either of us, I can't say that it's too weird."

    "Despite that, it still hangs heavily on my mind. These guest rooms really are luxurious, but at the same time, they seem impersonal, and without any color."

    "Against the vast whiteness of the sheets, Misha looks so small and out-of-place."
    
    show misha perky_confused_cas
    with charachange
    
    play music music_friendship fadein 2.0

    mi "Hey, Hicchan, you really love Shicchan, right?, right? Please tell me honestly."

    "The answer is obvious, and yet I wonder about answering too quickly."

    hi "Yeah, I do. Of course I do, or else I wouldn't have come this far. You don't have to doubt that."
    
    show misha perky_smile_cas
    with charachange

    mi "I'm glad…"
    
    show misha perky_smile_cas_close
    with characlose

    "Misha stares deeply into my eyes, her face uncomfortably close to mine. Another one of the traits she's lifted from Shizune, I guess. She does this for almost a minute."

    mi "Okay, Hicchan, I believe you~."

    # lawl a split

    return

label en_S25a:

    #1) The part where you do not bang Misha

    "Satisfied, she falls backwards onto the bed, throwing out her arms."
    
    hide misha
    with charaexit

    mi "I'm happy, now. As long as Shicchan is happy, I'm happy."

    mi "And I'm happy that you want me to be happy, too. But, you can't make everyone happy… Do you understand, Hicchan?"

    mi "Of course, Shicchan would rather be with you than me. If that is what she wants, though, I am going to do my best to support her."

    mi "I'm going to become a better person for you and her, like you did."

    mi "I'm going to go to sleep, and when I wake up, I'll be a sunnier person. Just like before…"

    mi "You should go spend some time with her, Hicchan, instead of with me~. Okay? Okay~."

    "I take this as my cue to leave."
    
    play sound sfx_doorclose
    scene bg shizu_guesthisao
    with locationchange

    "Closing the door behind me, I head to my own room and sit down. I had always thought Shizune and Misha were close, but I never expected that Misha might have actually loved her."

    "I don't have any feelings about it. Maybe a part of me always considered it a possibility, to the point where it doesn't surprise me as much as it should."

    "Despite the severity of it, I have to admit that I do also find it very interesting. For a moment, the thought flashes into my mind of what a nice relationship that would be."

    "The image of Misha caressing Shizune and leaning forward to kiss her fills my head. How would Shizune react to that? Would she blush cutely and be unable to move? Misha would probably be the aggressive one there, for once."

    "As my thoughts get increasingly more wrong, I try my best to ignore this line of thinking."

    "…"

    "Misha, is it really necessary to try so hard to be a saint for Shizune?"

    "I think about the things she said. In the end, I keep returning to her question to me. Do I love Shizune?"

    "Yeah. I do. I do, but I realize that I've never used that word with her. I didn't even say it today."

    "I'm an idiot."

    "It feels pretty disgusting… to doubt yourself."

    "But I know that I love Shizune. It's not my duty to be with her. The decision was mine. If it wasn't for my feelings, I wouldn't have said a damn thing, but I did, because I was so sure."

    "I still feel the same way. Nothing has changed since then. Isn't that my mistake? That nothing has changed? That I didn't even try to change anything?"

    "Shizune's smiling face appears in my mind. What a gentle smile. So rare, that maybe only Misha and I have seen it. How many times have I returned that warm smile with one of my own?"

    "She really is more fragile than I initially thought."

    "For some reason, I feel so weak, and tired. A part of me wants to rush out to meet her, but I feel too tired to even stand."

    "Tomorrow."
    stop music fadeout 3.0
    scene black
    with shuteye

    #end scene

    return

label en_S25h:

    #2) The part where you bang Misha

    stop music fadeout 2.0


    "At this distance, I can smell the distinctive scent of alcohol on her breath for the first time."
    
    play music music_night fadein 1.5

    "Where could she have gotten alcohol? When? How much has she had?"

    hi "Misha, have you been drinking?"

    mi "All the guest rooms have some liquor, Hicchan."

    "Her voice has gotten quieter, and a little sheepish. Suddenly, Misha moves forward and grabs my arm."
    
    mi "Hicchan, what about me? Do you like me?"

    "She squeezes herself against me. It seems like she's trying to get inside my clothes, and my arm is enveloped by softness. I don't think anything much about that."

    hi "Yeah."
    
    show misha perky_sad_cas_close
    with charachange

    mi "I like you, too. Maybe if I was different…"

    mi "Hicchan, I'm a really selfish person, right?"

    hi "Stop saying stuff like that."
    
    stop music fadeout 5.0

    mi "I want to do something selfish and stupid."

    "Her head buried in my chest as it is, and with her voice dropping lower and lower each time she speaks, it's hard to understand her."

    mi "Hicchan, can you comfort me today? Just today."

    mi "You can say no, if you don't want to. I'm just saying something stupid, and…"

    play music music_moonlight fadein 4.0
    
    "A hollow ringing fills my ears, as if my eardrums have burst. Misha doesn't so much trail off as my brain stops registering what she's saying."

    "Before I can answer, she takes the initiative and pushes forward against me even harder, until I have to stand up. Wordlessly, she slips her hands towards my belt buckle and undoes it with a visible air of guilt."

    scene white
    with flash

    "We both topple onto the bed, with me on top of her. I can't think anymore. This is the point of no return."

    "I run my hand up Misha's plump, silky thigh and hear a sharp intake of breath, but she doesn't tell me to stop."

    "As I feel my way up towards her groin, I feel a touch on my manhood that makes me shiver. But neither of us tells the other to stop."

    "And as I reach her most precious point…"

    mi "Aa… aahh…"

    "…I realize that Misha is way more decisive than me, and that we can't stop now. The leading edge of my hand stops at her panties, and I start pulling them off, feeling a soft, warm wetness behind them."

    "Without thinking, I press my fingers against her and hear Misha let out a small, restrained mewing sound."

    "She feels for my pants, seeming eager to return the favor, as unnecessary as it is, but it's hard for her to do so with me on top of her like this."

    "Misha's hands touch my hips and move across my chest. With my free hand, I start to feel her chest, amazed at the tenderness and shape of her breasts even through her clothes."

    "She looks as though she is about to say something, but stops herself and removes her shirt instead. I notice that her bra unhooks in the front and wonder if I should."

    "I undo her bra and brush it aside, massaging her chest with one hand. Misha's breathing becomes heavier and more pronounced. Our eyes meet, and a deep red color flushes across her cheeks."

    mi "Is it nice?"

    hi "Yeah."

    "This is wrong. For the first time, it hits me how wrong this is, but I can't seem to stop. Misha's face mirrors my own guilt."

    hi "Are you ready?"

    "Misha clasps her hands around me and nods. I slip her skirt off and look at her naked body. She has such a curvy figure for that cute face, and her skin is so pink and smooth."

    mi "This is my first time with a man. It's strange."

    hi "I'm putting it in now."

    mi "Please do it quickly…"

    mi "Ow…"

    "Misha tenses a little, but I'm beyond noticing. I flex, and I feel, and I grab. At some point, she raises her leg to wrap it around the back of mine, but I don't know if either of us is doing anything but going on automatic."

    "I notice her teeth are clenched to stop herself from making too much noise, but each time she has to take a breath, it slips out."

    mi "Haah~… haaah… haah~…."

    "Her arms wrap around my shoulders, her fingers curling and uncurling as they feel their way across my back as if searching for something."

    "Her actions only pull us closer together, and push me deeper inside her."

    "Finding a rhythm, I continue to drive myself into her, everything around me a haze except for her and myself, as if I'm intoxicated."

    mi "Hnn… Shicchan…"

    "I almost stop for a second, and immediately a bad taste fills my mouth as I'm pulled forcibly back to the reality of the situation."

    "I'm a pretty low person for this."

    "But where we are now, it's too late."

    "I keep on going, Misha's body pressed against my own, her breasts rubbing themselves on my chest. She pushes herself tighter against me, leaning into each thrust."

    "Her soft cooing in my ear makes me keep going, as does the hot, slick tightness around my member. Eventually, her leg twisting around mine, she tenses up in orgasm, her smooth neck rubbing across my cheek."

    "It takes a minute for her to separate herself from me, silently, her hair tickling my chest as she carefully rolls a few inches away."
    
    scene bg shizu_guestbed
    with flash
    
    stop music fadeout 3.0

    mi "…Hicchan?"

    mi "…Nevermind."

    mi "I just wanted to know what it was like. I'm sorry. I'm really sorry…"

    "I feel around for Misha's hand and caress it. How light and delicate it seems, even as it grabs me so tightly around my wrist."

    "There is no joy in what just happened. The more time passes, and the more the silence between us grows thicker, the dirtier I feel."

    "Her hand continues to grasp mine tightly. I wonder what she's thinking. Does she feel the same way I do? There is nothing in me now but a void, and the only things that form in the void are guilt, regret, and fear that I can't bear to look at."

    mi "I've done a really terrible thing, right, Hicchan?"

    "My weak fingers squeeze hers back."

    hi "No."

    "Inwardly, I yell at myself, because I can say so much more. I could… but I can't even begin to put it into words. And where would I start? And how could I dare?"

    mi "If Shicchan were to find out…"

    mi "I…"

    "A pause."

    mi "I've done another thing that can't be taken back."

    mi "All I do is hurt her."

    "Something inside me pushes me increasingly harder to say something."

    hi "It's fine."

    "My head hurts. My mind is white-hot with panic, but at the same time, I can think calmly. An unexplainable feeling, but I'm grateful for this opportunity, because I know the horrible place I'd be without it."

    hi "I love Shizune, too. I like her even more than I had thought. Now, I'm sure."

    hi "I just comforted you. And I learned something about myself, so don't feel bad."

    hi "I really love you both."

    "Misha seems to accept this. Her grip on my hand loosens, and she rolls a little further away. When she speaks again, her voice has regained some of its cheer. Of course, I have no idea if she's just putting on another happy face for me."

    mi "Thanks, Hicchan."

    mi "I'll go to sleep. When I wake up, I'll be a different person. A better person for you and Shicchan."

    mi "So, don't worry about me, okay?"

    hi "Okay."

    "I trust her. Getting up slowly, I put on my clothes and leave as she covers herself with the sheets, wrapping herself between them like a cocoon."
    
    scene black
    with dissolve

    return

label en_S26:
    play music music_tranquil fadein 2.0
    scene bg shizu_guesthisao
    with openeye

    "The next morning, I wake up later than normal, my familiar alarm clock not there to remind me to get up at the usual time."

    "Strange how I almost miss it, even with the whole back and forth love-hate relationship we have had up until now."

    return

label en_S26a:

    #1) if you banged Misha

    "I can't stop myself from thinking about the events of yesterday. My heart skips a beat as the reality of what I did sets in."

    "I recall Misha's face under me; her arms grasping across my back, and the feeling of her writhing legs interlocked around my own. Thoughts of Shizune run through my head in contrast and only make it worse."

    "What a terrible feeling. Despite what I said to Misha, I still feel a crushing sense of guilt over it."

    "Not all of my words were hollow, though. This regret is proof that my feelings towards Shizune are real. It's a small comfort."

    "Trying to brush aside the gnawing, unsettling thoughts that keep resounding in my mind, I force myself to get up and go eat breakfast."

    return

label en_S26b:

    #2) if you did not bang Misha

    "I think about what Misha told me yesterday."

    "You're going to become a better person, Misha? That's not necessary."

    "It's enough that you can continue to stand by Shizune. How long have you stood by her, even after she turned you down? And how much courage did it take to continue to be her friend, when you found out she didn't see you as more than that?"

    "I really can't imagine."

    "I'm glad that she's a little happier now, though."

    "My thoughts drift to Shizune. The thought of Misha confessing her feelings to her and then kissing her forcefully returns to my mind. It seems inappropriate, but I'm not exactly objecting…"

    "The Shizune of my imagination blushes a deep red and pushes Misha weakly back, stepping backwards, opening her mouth as if to speak, but unable to, of course."

    "Misha grabs her shoulders, pulling herself up against Shizune, both of them against the wall."

    "Seized by the moment, she touches Shizune's neck gently, running her hand down it in a gentle caress as her other hand traces a path downwards to the waistband of her skirt."

    "No, this is getting too inappropriate…"

    "Trying to shake this train of thought off my mind, I decide to go have breakfast."

    return

label en_S26c:

    # end
    
    scene bg shizu_living
    with locationchange

    "It's a large meal. They say that breakfast should be the heartiest meal of the day, but this really seems like a little too much. There isn't a single free square inch of space on this plate."

    "Eating as much as I can, I excuse myself from the table, forgetting for a second that I'm alone at the table. It looks like the servants eat somewhere else, and they vanished as soon as they set my plate down in front of me."

    "Usually, Hideaki, at least, is here, but not today. It's not like I've never eaten alone before, but it looks like I've been eating in the company of others enough that I have gotten used to it."
    
    stop music fadeout 2.0
    
    "The clink of my plate and utensils sliding into the sink resounds throughout the quiet of the kitchen. It's unsettling, and lonely. Hating the atmosphere, I decide to go outside and get some fresh air."
    
    scene bg shizu_houseext
    with locationchange
    
    "I step outside, and the first thing I see is Shizune. It's almost as if she were waiting for me. In fact, she doesn't even react with surprise when she sees me. How? There's no way she could have known I was about to step through the door."

    show shizu behind_blank_cas
    with charaenter

    "For a moment, I contemplate the possibility that she has been standing out here for awhile, just waiting for me to come out so that she could act unsurprised and aloof. Didn't Hideaki do this? Yeah, it's entirely possible."

    "I'm jolted back to earth by her poking me sharply in the chest with an outstretched finger."
    
    play music music_shizune fadein 1.0
    
    show shizu adjust_angry_cas 
    with charachange

    ssh "I'm right here! How long are you going to keep spacing out, thinking to yourself? What about a “good morning?”"

    ssh "Good morning to you, too, Hisao."

    hi "Good morning, Shizune."

    ssh "Don't patronize me."

    hi "What? But—… Hey, what the hell?"
    
    show shizu adjust_happy_cas
    with charachange

    "She drops her hard edged expression in favor of a softer one upon seeing my indignation."

    ssh "You have to be more forceful, and more forward-thinking. And you're going to have to learn to think on the spot if you want to get the best of me. I'm going to keep on doing this until you learn."

    ssh "I'll keep testing you, as per our agreement."

    "An agreement? This is the first I've heard of anything like that, but it's nice to see that Shizune is back to normal as well."

    hi "What agreement?"
    
    show shizu adjust_blush_cas
    with charachange

    ssh "I said that I would try harder for you, didn't I? That is what I'm doing. If I can't meet you with my best, and challenge you, then I'm looking down on both of us."

    "Shizune's face is tinted red as she says this, her normally steely eyes evasive and wide, betraying the cold front she tries to put on with the harsh, swishing strokes she cuts into the air to get her message across."

    hi "Well, you seem to be back to normal."
    
    show shizu basic_sparkle_cas
    with charachange
    
    ssh "What does that mean?"

    "Her eyes sparkle with the strong glare of competition. She knows exactly what I mean; this is just another one of her games. Better go for the safe answer."

    hi "It means what it means."
    
    show shizu adjust_frown_cas
    with charachange

    ssh "What does that mean?"

    "I can foresee myself getting locked into an infinite loop here. I guess there's no choice. It's time to do something bold."

    hi "Hey, what happened in 1961 that won't happen again for four thousand years?"
    
    show shizu basic_normal_cas
    with charachange

    "Shizune stops dead in her tracks, just in time, because I can see that she was about to really unload on me. She taps her fingertips together rhythmically, deep in thought."
    
    show shizu basic_frown_cas
    with charachange

    "She's becoming visibly agitated by the question, seemingly unable to find an answer to it."

    hi "Give up yet?"
    
    show shizu behind_frustrated_cas
    with charachange

    ssh "No, stop distracting me. I'm concentrating. I'm not that good at history."

    "Shizune doesn't give up this last admission gracefully, but it's with it that she finally lets out a sigh and glares at me grudgingly in “defeat.” It's unlikely that she would ever admit it."

    hi "It's the year. 1961 looks the same upside-down as it is right-side-up. That won't happen again until 6009."
    
    show shizu behind_blank_cas
    with charachange

    "For a second, it looks like she might attack me, but instead she nods."

    ssh "How clever."

    ssh "And I was thinking it was something like the farthing ceasing to be legal tender, or the United States ceasing diplomatic relations with Cuba, or Charlie Brown successfully flying his kite."

    hi "Yeah, a lot of people make that mistake."

    "I try not to reveal that I have no idea what she's talking about. What obscure knowledge. Her grades in history are probably better than mine…"

    "Nevertheless, I've finally beaten her. Before I can bask in my victory, she starts signing, interrupting my moment of glory."
    
    show shizu cross_angry_cas
    with charachange

    ssh "Stop being so smug. Do I lord it over you every time I know something you don't? If I did, I wouldn't be able to stop."

    "She's turning red, clearly very agitated. Well, it was a pretty simple riddle, but she shouldn't be bothered this much about it."

    hi "Okay, okay. Don't get so worked up over it."
    
    show shizu behind_frustrated_cas
    with charachange

    ssh "It was so obvious… How could I not have known? How?"

    "Her expression softens into a smile."
    
    show shizu behind_smile_cas
    with charachange

    ssh "I'm actually very happy right now."

    ssh "I always thought you needed to take more initiative, since this whole time, you seemed content to follow my pace."
    
    show shizu basic_happy_cas
    with charachange

    "Her smile widens playfully."

    ssh "Of course, even with this, it's not enough. You're still an idiot most of the time."

    hi "I am not."

    ssh "I think you are, ergo, you are. Consensus is the same as verification."

    hi "What does that mean?"
    
    show shizu adjust_smug_cas
    with charachange

    "Shizune's posture changes, becoming much straighter. She adjusts her glasses with great relish."

    ssh "It's like this: One of the fundamental laws of both scientific analysis and academic logic is the law of common agreement."

    ssh "As long as over 50\% of the people in a group agree on the acceptance of a fact, term, or practice, it becomes correct or true. This principle has allowed for great strides in human achievement."

    ssh "For instance, until more than 50\% of the western world agreed that the earth was round, it would have been impossible for Columbus to reach the West Indies by water travel, due to it being flat."

    ssh "Acceptance of a spherical world caused the earth to round itself into a ball, allowing for nautical passage to the new world. Where would we be without the human ability to reach a consensus on a simple issue?"
 
    hi "How does this relate to…?"
    
    show shizu adjust_happy_cas
    with charachange

    ssh "Right now there are two of us, and I think you're an idiot. Therefore, you are."

    hi "But I don't think I'm an idiot, so it's actually evenly split."
    
    show shizu adjust_smug_cas
    with charachange

    ssh "I always give my opinions a little more weight, due to merit."

    "She closes her eyes and signs it with a strong air of confidence. Does she really believe that? I can't tell. No, it can't be."

    hi "…You can't do that!"
    
    show shizu adjust_happy_cas
    with charachange

    ssh "I already did."

    show shizu behind_smile_cas
    with charachange

    "Before I can start thinking up a proper argument, she starts laughing. The same silent, soundless laugh as always. Her expression is so warm when she laughs, but I still get the feeling that she is hiding something."

    ssh "Fine, I'll admit that maybe you're a little smarter than before. But, don't feel like you're allowed to gloat so freely. This only makes me feel more competitive."
    
    show shizu basic_sparkle_cas
    with charachange

    ssh "My heart is beating, can you hear it? Don't worry, I'll have my revenge, when you least expect it."

    "What an atypical amount of enthusiasm."

    "Despite the good natured grin on her face, I'm not exactly feeling very reassured by it. She seems totally serious. It can't be, right? This could actually be her revenge, right here: trying to instill paranoia in me. If so, it's working."
    stop music fadeout 2.0
    ssh "…And of course, you had better do your best to try and keep up."
    
    show shizu behind_blank_cas 
    with charachange
    
    play music music_comedy fadein 1.0

    "Suddenly, the door of the house swings open behind me and Misha leaps out onto the grass as if she is trying to break a long jump record. As she walks over to us, I can see she left two foot-shaped imprints in the meticulously cut grass."
    
    "Someone isn't going to be too happy about this."
    
    show shizu behind_blank_cas at tworight
    with charamove
    
    show misha cross_grin_cas at twoleft
    with charaenter

    mi "Hi~ Hicchan, Shicchan~!"

    "She waves vigorously at us, flailing her arm in a circle so fast it's like she intends to try and generate lift with it."

    "Misha seems much more upbeat today. I guess that stuff about waking up as a different person was true, but isn't this still just an act? It is, and nothing can change that."

    "Despite that, I am fine with accepting it…"
    
    show misha cross_smile_cas at twoleft
    with charachange

    mi "Hm~ hm~, it sounds like you two were talking about something fun."
    
    show shizu adjust_blush_cas at tworight
    with charachange

    "Shizune blushes, fidgeting with her glasses. She attempts to sign something, but only gets as far as turning her hands in a steady circle as she tries to formulate her thoughts into words."

    ssh "…"

    mi "Hahaha~! Keep going, Shicchan~."
    
    show shizu basic_normal_cas at tworight
    with charachange

    ssh "Hisao, let's go somewhere, like we talked about yesterday."
    
    show shizu behind_smile_cas at tworight
    with charachange

    "She turns her head slightly to Misha and her hands form the words:"

    ssh "All three of us, of course. We can look around, and maybe go window shopping, and get some food, of course."
    
    show misha hips_grin_cas at twoleft
    with charachange

    mi "Wahaha~! Shicchan! A date, hm? Is it really alright for a man to go on a date with two girls at once? That sounds too much like something you would see in a romantic comedy."

    hi "It's okay. We always went places together, all three of us. So, what's weird about that? It's just the way it is."
    
    show misha perky_confused_cas at twoleft
    with charachange
    show misha hips_grin_cas at twoleft
    with charachange

    "A flash of emotion appears across Misha's face, vanishing even faster than in the blink of an eye, so quickly that all I could do was to perceive the change, and not her feelings."
    
    show shizu adjust_happy_cas at tworight
    with charachange
    
    ssh "That is good. Of course, you'll pay for everything, won't you, Hisao?"

    hi "Hahaha… No. Absolutely not."
    
    show misha hips_smile_cas at twoleft
    with charachange

    mi "So decisive, Hicchan~."

    ssh "You need to be this decisive more than just in situations where you need to protect your wallet for it to count."

    mi "Ah! Shicchan, where are we going to go, anyway?"

    ssh "We can decide that when we're outside."

    "Outside? It hits me again just how large the Hakamichi estate grounds are. I had almost completely forgotten, too. My thoughts drift back to when we had to be driven across what seemed like vast plains of land just to get to the house."

    "I hope we're taking a car."
    
    stop music fadeout 1.0
    
    scene bg shizu_park_ni
    play sound sfx_time
    with shorttimeskipsilent

    # fade transition of some kind

    # yeah I'm skipping this shit due to no art
    
    play music music_night fadein 1.0

    "By the time we get back, it's gotten quite late."

    "The night air is so cool and clean, but I can barely breathe with Shizune and Misha pulling me by the arms."

    "Looking back, today wasn't so bad. We went shopping, and it was nice to see both of them smiling like they used to. It's been awhile since I've seen them so happy."

    "So it's a small price to pay that I had to carry everything they bought."

    "Nevertheless…"

    hi "Hey, Misha, tell Shizune that she could help me carry one of these bags."
    
    show misha hips_smile_cas_close at closeleft
    with charaenter

    mi "Eh? But~, it looks like you already have that taken care of Hicchan. Besides, Shicchan looks like she's in such a good mood, so there is no reason to bother her, right?"

    mi "If you're going to ask her, don't get me involved in it, Hicchan. So cruel~."
    
    show misha hips_laugh_cas_close at closeleft
    with charachange

    "Her laughter explodes like a bomb blast in my ear."

    hi "Really? Well, okay then. I was just asking since I kind of have my hands full right now, so I couldn't do it myself."

    hi "You could lend me a hand, and it would solve everything."
    
    show misha sign_smile_cas_close at closeleft
    with charachange

    mi "Hm~ hm~… Hey, Shicchan~…"

    "Shizune stops as Misha taps her on the shoulder."
    
    show shizu behind_blank_cas_close at closeright
    with charaenter

    shi "…?"

    mi "Hicchan wants you to help him carry the bags."

    ssh "You can help him."

    mi "Awww…"

    hi "Hey, don't back down so easily. Shizune, take a bag!"
    
    show shizu behind_smile_cas_close at closeright
    with charachange

    "Shizune giggles."

    ssh "I can't hear you, Hisao, so I can't help you. It's a shame, too, because you seem so forceful right now."

    hi "Hey!"

    "Before I can think of a way to adequately express my outrage, or at least have Misha express it for me for the time being, she swoops over and grabs half of the load from me before signing with her free hand."

    ssh "I don't understand a thing you said, obviously, but you seemed passionate. Be like that more often."

    "Hard to make it out, as condensed as she makes the message, but that seems about right."

    hi "Fine, I will."
    
    show shizu behind_frustrated_cas_close at closeright
    with charachange

    ssh "I just said I can't hear you."
    
    scene bg shizu_houseext_ni
    with locationchange

    "We make it back to the house. The scenery looks oddly different at night. Without the sunlight bathing the grounds, they look so depressingly empty and lonely."
    
    scene bg shizu_living
    with locationchange

    "Dinner has probably come and gone. It really is late."

    "I think of retiring for the night, and Shizune wishes me a good night cheerfully, even though she doesn't stick around for me to return it. I guess it's the thought that counts. …Does that even apply here?"

    "As I head to the bathroom to brush my teeth, I run into Misha in the hallway."
    
    stop music fadeout 0.5
    
    show misha perky_smile_cas
    with charaenter

    mi "Oh, Hicchan."

    mi "It's good that you're here. Lucky~, right?"
    
    show misha sign_smile_cas
    with charachange

    mi "Hm~. I want to say something, so, please don't interrupt me, okay, Hicchan?"

    mi "…"
    
    play music music_friendship fadein 3.0

    return

label en_S26d:

    # this only goes in the part where you had sex with Misha

    mi "Thank you, Hicchan, for not acting differently around me today."

    mi "I've been thinking, about yesterday."

    mi "You're not going to tell Shicchan about it, right? Of course not. You shouldn't, either way."

    "She is controlling the flow of our conversation. I've seen Shizune do this so many times, facing slightly away as to be able to plausibly deny anything I say. You're really kind of smart."

    mi "I'm happy now. Not really… I know that now and then, I'm going to feel sadness because of her, but my guilt, and my sadness, is a kind of validation too."

    mi "Those kinds of feelings prove that I want to see Shicchan happy. Those kinds of feelings are the kind that hold up even in court, you know."

    "I remember Shizune saying that too. The kind of evidence that holds up in court, huh? If feelings count, then it seems almost too easy. Is it really?"
    
    show misha sign_smile_cas
    with charachange

    mi "How are you feeling, Hicchan? Do you feel the same way? You understand, don't you?"

    mi "Haha~. That's why I was a little worried, and why I can't trust you, Hicchan~."

    mi "It's hard for a man to lie to a woman, so…"

    mi "But, doesn't that mean that if it's so easy for me… haha~…"

    "Misha looks oddly at peace."
    
    show misha cross_smile_cas
    with charachange

    mi "Shicchan is different when she is with you. Do you know what sets you apart from everyone else, Hicchan?"

    mi "It's your reactions. You responded to her, every time, and always stood your ground. You never ran."

    hi "I tried to, a bunch of times."
    
    show misha cross_grin_cas
    with charachange

    mi "Ha~. No, Hicchan, it was like a metaphor, Hicchan. An expression, an expression."

    "I can't help but smile. What a thing, coming from her."

    mi "That's all."

    mi "Goodnight, Hicchan."
    
    stop music fadeout 2.0
    
    scene black
    with dissolve
    
    return

label en_S26e:

    # Alternatively, this if you did not have sex with Misha.

    mi "Thank you, Hicchan, for not acting differently around me today."

    mi "Didn't I say that I would be a better person from now on for both of you~?"

    mi "Yesterday, Hicchan, I had a selfish thought for a second, that you would comfort me. I've thought that way about Shicchan too."

    mi "But~, it's a very selfish way to think. “I should think better about my friends.” That is what I said to myself."

    mi "I'm happy. Both of you were having so much fun, so I was happy too. I think I can continue to feel this way to the end."

    "Misha looks oddly at peace."
    
    show misha cross_smile_cas
    with charachange

    mi "Shicchan is different when she is with you. Do you know what sets you apart from everyone else, Hicchan?"

    mi "It's your reactions. You responded to her, every time, and always stood your ground. You never ran."

    hi "I tried to, a bunch of times."
    
    show misha cross_grin_cas
    with charachange

    mi "Ha~. No, Hicchan, it was like a metaphor, Hicchan. An expression, an expression."

    "I can't help but smile. What a thing, coming from her."

    mi "That's all."

    mi "Goodnight, Hicchan."
    
    stop music fadeout 2.0
    
    scene black
    with dissolve

    return
    
label en_S27:
    
    play music music_daily fadein 1.0

    scene bg school_gate
    with locationchange

    "It's been over a week since I've seen Yamaku, so arriving back at the school gates, it almost feels like my first day again."

    "…Actually, that really wasn't exactly a great day."
    
    show shizu behind_frustrated_cas at twoleft
    show misha hips_smile_cas at tworight
    with charaenter
    
    "Shizune nudges the back of my leg with her foot, telling me to hurry up already and get going. I can see that she is holding a piece of luggage in each hand, so I guess I can let it slide this time."
    "Still, there has to be a nicer way to get the point across."

    mi "What Shicchan is saying, Hicchan, is that you should hurry up! Hurry up, Hicchan~!"

    "I can pick up that much by myself, thanks. I decide to have a little fun with the both of them."

    hi "No. I refuse to move. In fact, I kind of like it here, so…"

    "My own hands full as they are, I can't sign a thing, so Shizune looks at Misha expectantly."

    show misha sign_smile_cas at tworight
    with charachange
    
    mi "Hm, Hicchan says he won't move at all, because he likes to stand around."
    
    show shizu cross_angry_cas at twoleft
    with charachange

    shi "…!"

    shi "…!"

    "Shizune frowns crossly and starts shaking her arms, trying to communicate while still holding onto her suitcases. This is really not working. Misha laughs, finding it all very amusing."

    show misha hips_grin_cas at tworight
    with charachange

    mi "Hahaha~! Hicchan, I think Shicchan is saying something like, “You're blocking the way, idiot! Move!”"

    hi "It's just a joke."
    
    show misha sign_smile_cas at tworight
    with charachange

    stop music fadeout 3.0

    mi "Shicchan, Hicchan said: “Why don't you make me?”"

    shi "…"

    hi "That's not what I said!"
    
    play music music_running fadein 2.0

    mi "Hm~, Hicchan, I think Shicchan would probably say something like, “I will! Brace yourself~!”"
    
    hide misha
    with charaexit
    
    show shizu cross_rage_cas_close at center
    with characlose

    "At that moment, Shizune starts pushing me with her shoulder, prodding me to move backwards into the school with the suitcases in her hands as she steadily tries to move forward like a bulldozer."

    "Unfortunately for her, I have the high ground by a few inches, and I'm also a lot taller, so I think I've won this round. Although the way she keeps jabbing me with her luggage is starting to hurt."

    "The feeling of her chest pressed up against mine is nice. She doesn't even seem to notice. Her large breasts are simultaneously soft and firm. It's distracting, and I almost fall over."

    "Eventually, I get caught up in her enthusiasm to compete and start pushing back, but every time I do, she comes back with more strength than before, until eventually I find myself being moved backwards."

    "It's too late to settle this like normal people. I can see Shizune won't stop now. Misha, I'll get you for this."

    "Shizune backs up for a second before trying again to dislodge me from where I'm standing as Misha watches our clashing bemusedly."
    
    show misha cross_laugh_cas at right behind shizu
    with charaenter

    mi "…And then Hicchan says, “Ha~, you are 100 years too early to defeat me! My defense is unbreakable!” “Oh no, his level is above everyone else I've faced before. Okay~! It's time to use my special attack! Take this!”"

    hi "Stop saying weird stuff! You! This is all your fault!"

    mi "Wahaha~! Both Hicchan and Shicchan sound so alike! It's just a joke, Hicchan. This is like watching a sumo match~!"
    
    show shizu cross_rage_cas_close at closeleft
    with charafast
    
    with vpunch

    "I charge forward to push Shizune back, but feel only air in front of me as she quickly moves to the side and I nearly trip."
    
    show shizu adjust_blush_cas_close at closeleft
    with charachange
    show shizu adjust_blush_cas_close
    with charamove

    "Shizune drops her suitcases and attempts to catch me, but there is really no need, and I doubt she would have made it anyway."

    hi "Thanks."
    
    show shizu behind_smile_cas_close
    with charachange

    "She smiles. A warm feeling starts spreading through my chest, and then immediately stops as Shizune quickly steps backwards through the school gates and cheerfully throws up a V for victory before picking up her bags again."
    
    hide shizu
    with charaexit
    
    stop music fadeout 1.0

    "She starts running towards the school, not waiting for Misha or I at all. I almost want to call out to her, but catch myself in time."
    
    show misha cross_laugh_cas
    with charamove
    
    play music music_daily fadein 3.0

    "Suddenly, Misha starts clapping me on the back, almost making me drop all my things."

    return

    #split

label en_S27a:

    #1) If you banged Misha in S25
    
    show misha perky_smile_cas
    with charachange

    mi "Shicchan is so bright lately. She is treating you like an equal, Hicchan. She looks so happy."
    
    show misha sign_smile_cas
    with charachange

    mi "This is the first time that she has ever been in love, I think. You're her first boyfriend, and you will share a lot of other firsts…"

    mi "But~! I won't try and steal her away. Because of that, though, there are responsibilities that you have too, Hicchan, to preserve her happiness. It's all because of me again, so please bear with my selfishness again, Hicchan."

    mi "Hahaha~."

    mi "I'm going to go unpack my things now. Later, Hicchan~!"
    
    hide misha
    with charaexit

    return

label en_S27b:

    #2) If you did not
    
    show misha perky_smile_cas
    with charachange

    mi "Shicchan is so sunny lately. She treats you like an equal, Hicchan. It's interesting, right?"
    
    show misha sign_smile_cas
    with charachange

    mi "Hicchan, do you think it's possible for your first love to work out? Is it real?"

    mi "I'm going to work really hard to see if it is. But~, there's responsibility on your shoulders too, Hicchan, because of that. I know you know that, though."

    mi "Hahaha~!"

    mi "I'm going to go unpack my things now. Later, Hicchan~!"
    
    hide misha
    with charaexit

    return

label en_S27c:

    #end split

    "She quickly dashes off, leaving me alone in front of the school."
    
    scene bg school_courtyard 
    with locationchange

    "I decide to take a brief look around. It looks like a lot of people have gone away for the holidays. Not surprising, since I would imagine it would get pretty boring just staying up on this mountain for a month."

    "This whole place sort of has that isolated quality."

    "It's been at least 20 minutes, and Shizune still hasn't come out of the school building. I wonder what she could be doing in there."

    "The first place I think to look is the student council room."
    
    scene bg school_council
    with locationchange

    "The door is already open a crack when I get there, so I nudge it open with my foot and step inside to find Shizune directly in front of me, looking at the room carefully, as if she is inspecting a picture on the wall to see whether it's crooked or not."

    "Turning around, she notices me and jumps back in surprise."
    
    show shizu cross_shock_cas
    with charaenter

    ssh "What are you doing?"

    "Her eyes flicker to my hands and she calms down when she sees the suitcases I'm holding."
    
    show shizu behind_blank_cas
    with charachange

    ssh "I see. One of those is mine, anyway. Maybe it was a little rude to just run over here like that. Can you put it on the desk?"
    
    hide shizu
    with charaexit

    "After I put her bags and mine down, I hear her moving closer to me, but she stops and walks over towards the window instead."
    
    show shizu basic_normal2_cas
    with charachange

    ssh "I was just about to leave, since I'm done with what I came here for."

    hi "What did you come here for?"
    
    show shizu adjust_happy_cas
    with charachange

    "Shizune taps her finger against her head, half pretending to think about it, but mainly doing it to tell me that it's obvious."

    ssh "This room is just as important to me as my dorm room, or my room at the house. And, I spent more time in here than in the other two combined. I'm attached to it."

    hi "How did you get in here, anyway? Don't you have to turn in your keys for the summer?"
    
    show shizu adjust_smug_cas
    with charachange

    ssh "Don't be silly. I made my own set."

    hi "Huh? But, the keys say “Do Not Copy” on them."
    
    show shizu behind_blank_cas
    with charachange

    ssh "“Do Not Copy?” …There is a lot of gray area in those words."

    hi "What…? Gray area?"

    ssh "Plus, I'm the student council president. I have a divine right to have my own set of keys."

    hi "Divine right?"
    
    show shizu behind_frustrated_cas
    with charachange

    ssh "Stop repeating me."

    "She seems annoyed. This isn't repeating; it would be really silly to repeat anything in sign language, right? Yeah, that would be silly."

    ssh "Yes, it would be, and yet you are doing it."

    hi "Am I signing what I'm thinking?"

    ssh "At least it shows the right mindset, even if it shows a dumb mind…"
    
    show shizu behind_blank_cas
    with charachange

    "She walks over to the bag I put on the table and takes out some familiar looking books from it."

    hi "Aren't those the school records?"

    ssh "Yes."

    "Her attitude is so nonchalant, as if to say “what of it?”"

    hi "Why did you take school records home with you?"
    
    show shizu basic_normal_cas
    with charachange
    
    ssh "Because, I wanted to be able to look at them in case I felt nostalgic for this place. Am I not supposed to?"

    "Somehow, she manages to give off a feeling of being offended, as if what she did were totally normal and not even slightly strange."

    hi "I'm pretty sure you're not supposed to."

    ssh "As student council president, it's my birthright to have access to these records at all time."

    hi "You can be born a student council president? Whoa."

    hi "…Anyway, the point is it still seems kind of dodgy."

    hi "What else is in here? I hope you don't think you have the right to borrow a bunch of school supplies either, because that's, like, stealing."

    "I reach into the bag she just took the school ledgers out of and feel something soft inside and pull it out. It's the stuffed cat doll I won for Shizune at the festival."
    
    show shizu cross_rage_cas
    with charachange
    
    "She hurriedly grabs it out of my hand and holds it behind her back, nestled in the crook of one arm, before putting it down on the chair behind her and launching into a flurry of motions."

    ssh "You're not supposed to just stick your hand into a woman's personal belongings like that!"

    "Everything that follows is too quick for me to catch, but it seems vaguely threatening, so I don't have any complaints."

    "Still, I'm surprised that she would carry it around with her. I had wondered for a while if she even cared about it or remembered it. It's really not a particularly special stuffed animal."

    show shizu adjust_blush_cas
    with charachange

    ssh "This is the first stuffed animal I have ever owned, so I am attached to it, too. I brought it in case I would miss it. That is what I do, I take something along if I know I'm going to miss it."

    "Her face is bright red."

    ssh "Do you understand?"

    ssh "This doll kind of reminds me of you, anyway."

    hi "Are you saying I look like a cat?"
    
    show shizu behind_smile_cas
    with charachange

    "She smiles, and then playfully hits me with the doll."

    ssh "No, you are not that cute. You are idealistic, you could have said nothing when I told you I made my own set of keys and took important documents home with me, but you did."

    ssh "That is good, that you don't compromise. I guess some people would say it isn't a good quality to have, but I like it. If you give it up, I think I'll hate you."
    
    show shizu basic_normal_cas
    with charachange

    "Shizune pauses, her hands flitting back and forth in front of her chest in hesitation. It's one of the few times I've ever seen her really hesitate to do anything."

    ssh "And, also, you… wore yourself out to win this for me. That was really stupid and unnecessary."
    
    show shizu behind_smile_cas
    with charachange

    ssh "It was also a little admirable, though. A little. So, there was some value in it. You really wanted to win, right?"

    ssh "You almost looked a little cool."

    hi "Thanks."
    
    show shizu adjust_happy_cas
    with charachange

    "She giggles and pushes her glasses up."

    ssh "I tease you a lot. Why don't you tease me back?"

    hi "It's pointless."

    ssh "Is that so?"
    
    show shizu behind_sad_cas
    with charachange

    "Shizune looks down at the floor, a sad expression on her face, one that lingers for a while in the stillness and silence of this empty building."

    ssh "Sometimes, you are so easygoing that I think that it's really too much, and I wonder if I'm just bothering you."

    ssh "I've always believed that competing is the best way to grow, because a person has to have a goal in front of them if they want to become more than what they are, right? Wanting to grow is how you succeed…"

    #ssh "It's true in everything. Even in relationships. Do you think so?"

    return

    #lol it's a choice

label en_choiceS27:
    menu:
        with menueffect
    
        ssh "It's true in everything. Even in relationships. Do you think so?"

        "Yeah, people have to always strive for more.":
            return m1
            
        "You can be happy with what you have.":
            return m2

label en_S27d:

    #1) Yeah, people have to always strive for more

    hi "Yeah. I agree. People should strive for more."

    ssh "Exactly."

    ssh "So how is it that you can be so calm all the time? Am I worrying too much?"

    "This is the first time I have ever seen doubt on Shizune's face. Her eyes sparkle softly in the dim light that floats through the curtains of the student council room. They are so wide and clear."

    "Is she looking up at me for an answer? Why me? You're smarter than me, aren't you? I can't give you an answer, anyway."

    hi "Your life probably has more meaning than mine."

    "I forget to sign it, but I don't think she was looking at me, so she probably didn't even notice I said anything."

    return

label en_S27e:

    #2) You can be happy with what you have

    hi "I don't know. There is nothing wrong in being happy with what you have, right?"

    ssh "I don't know how that feels. I just want to become a better person."

    "This is the first time I have ever seen doubt on Shizune's face. Her eyes sparkle softly in the dim light that floats through the curtains of the student council room. They are so wide and clear."

    "Why is she looking up at me? She looks so lost. Do you want me to give you some kind of answer? I can't. I really can't."

    hi "That is one of the reasons I like you. I wish I had that kind of drive, and your talent. If I had those things, then maybe, I'm sure I wouldn't be as easygoing."

    "I forget to sign it, but I don't think she was looking at me, so she probably didn't even notice I said anything."

    return

label en_S27f:

    # lawl end splits

    "Shizune holds the stuffed cat in her lap and sits down in the chair it occupied just a few minutes ago."
    
    show shizu behind_sad_cas at centersit
    with charamove

    ssh "I understand that the kind of attitude that I have isn't the best."

    ssh "When you won this for me, you tried really hard. Was it because you liked me even that far back?"

    "I nod my head. Yeah, I did. By then, my mind had long since lost any doubt about that."

    hi "I'll tell you a secret. You are my first girlfriend, and I wondered if it was possible to really love the first person you fall in love with. I mean, they say that first loves never really work out, because you're usually so immature."

    hi "I had forgotten it, but I remembered again today. And I really want it to be true. So everything up until now, you can say that it was all working towards that."

    show shizu basic_normal2_cas at centersit
    with charachange
    
    ssh "I see."

    ssh "It's not that big a secret that I'm your first girlfriend, however. Why is that even worth keeping so secret? Do you have some kind of reputation that I should know about?"

    hi "No, of course not."

    ssh "Well, okay, then. I'll tell you a secret, then. It's only fair."

    shi "…"

    shi "…"

    "She is hesitating again, struggling inwardly with herself. Debating with herself as to whether she should go on. I can tell by the nervous look on her face. Is the length of each pause proportional to the weight of her thoughts?"

    "If so, then what is she going to say?"
    
    show shizu basic_frown_cas at centersit
    with charachange

    ssh "What are you looking at me like that for?"

    ssh "Just forget it."
    
    show shizu behind_blank_cas at centersit
    with charachange

    "She stretches as if waking up from a long nap."
    
    show shizu behind_smile_cas at centersit
    with charachange

    ssh "Let's do some boyfriend and girlfriend things this week."
    
    show shizu behind_frustrated_cas at centersit
    with charachange

    ssh "You had better not be thinking that implies something dirty, though. I know that is what you're thinking."

    show shizu behind_frown_cas at centersit
    with charachange
    
    ssh "I'm serious."
    
    "Shizune furrows her eyebrows sharply to show how serious she is."
    
    show shizu behind_smile_cas at centersit
    with charachange
    
    ssh "We can go get some junk food."
    
    

    hi "Is that what you missed all this time? Junk food?"
    
    show shizu behind_smile_cas
    with charamove

    "She laughs, and then starts moving towards the door, holding the cat doll close to her chest in the crook of her arm and jingling her keys with the other. Does she mean it's time to leave?"

    hi "Hey, you didn't answer the question."

    "Her shoulders move up and down in a simple shrug that doesn't give anything away."

    "As best as she can with her hands full, she makes a rudimentary series of signs."

    ssh "See you tomorrow."

    "And then she shakes her keys once again, as if to say if I don't get out, she'll lock me in. Is that even possible? Well, I'd rather not find out."
    
    stop music fadeout 1.0
    
    scene bg school_dormhisao
    with locationskip

    "When I get back to my dorm room, it looks so bare that it's almost alien. I didn't have a lot of personal effects to start with, and I had taken almost everything that was here with me. Except for my alarm clock, of course."

    "Oops. It looks like I'd forgotten to turn the alarm off while I was away, too. I'm surprised no one broke the door down and destroyed the place."

    "I'm too tired to unpack. There are so many thoughts swirling in my head, and I don't think I can handle trying to sort all of them out today. Definitely not after that long train ride and the walk up here."

    #"The most pressing thing on my mind is…"

    return

    #lawl choices

label en_choiceS27a:
    menu:
        with menueffect

        "The most pressing thing on my mind is…"

        "The future.":
            return m1

        "Shizune.":
            return m2

        "Misha.":
            return m3

label en_S27g:

    #1) The future

    "…"

    "Is the future something that someone like me should really be concerned with? I mean…"

    return

label en_S27h:

    #2) Shizune

    "…"

    "“Let's go eat some junk food,” huh? Really? Hahaha, okay."

    return

label en_S27i:

    #3) Misha

    "…"

    "I wonder if she'll be okay. After all, isn't she the one who really needs worrying about?"

    return

label en_S27x:

    #end choices

    "I'll deal with that kind of stuff later, though."
    
    scene black
    with dissolve

    return

label en_S28:
    
    scene bg school_dormhisao
    play sound sfx_doorknock2
    with openeye
    

    "The next morning, I awaken to a cautious knocking on my door, and can see that someone is standing in front of it from my bed by the shadow of two feet coming through the crack between it and the floor."

    "Dragging myself out of bed, I see that it's far too early for this kind of thing. Six in the morning, way before my alarm would go off if this weren't summer, where it's also customary to sleep in a little."

    "I decide to make whoever's calling on me wait it out a little in a display of passive-aggressive revenge and take the time to gulp down my medication and do a few stretches before opening the door."

    play sound sfx_dooropen
    scene bg school_dormhallway
    with locationchange
    
    hi "Hello."

    play music music_kenji fadein 0.2
    
    show kenji neutral
    with charaenter

    ke "Sup?"

    hi "I had a feeling it was you."
    
    show kenji tsun
    with charachange

    "It was either going to be him, Shizune, or Misha, and the other two never drop in this early."

    "Kenji seems to be trying to do his best to look as offended as possible, puffing himself up and running his hand through his hair like a preening rooster."
    
    show kenji neutral
    with charachange

    ke "So I was thinking about how tans are usually in style during the summer, and planning how I could steal a heat lamp from the cafeteria so I could use it to tan myself and also keep food warm, and I came here to ask if you wanted in on it."

    show kenji tsun
    with charachange
    
    ke "…Only to find out that you weren't answering your door. I had to carry out the operation all by myself. Shit was hard. And on top of that, you know those holes in the wall that electricity comes out of?"

    hi "Outlets?"
    
    show kenji neutral
    with charachange

    ke "Cool, so you know. Yeah, I needed one of those things that makes one set of outlets into two for my heat lamp. I came over here to borrow one, but then I remembered you weren't here, so you ruined my plans again with your absence."

    ke "I guess what I'm saying here is, do you have one of those hole doublers I can have, dude?"

    hi "Why would I have one of those?"

    ke "Yeah, I guess you're not as practical as I am."

    hi "What?"
    
    show kenji tsun
    with charachange

    ke "Where were you, man?"

    "I've mostly gotten used to his habit of cutting me off and moving on into a totally different line of conversation like that only because he shares it with most of the people I've grown to know lately, but it's still very jarring."

    hi "I was at Shizune's house. She went home for awhile and I decided to go with her. I guess you're right and I should have put a note up or something?"
    
    show kenji happy
    with charachange

    ke "I'm right? …Yeah, I am right. Of course I am. Badass."

    "He smiles and nods, rubbing his chin thoughtfully."
    
    show kenji tsun
    with charachange

    ke "When did you get back? Why didn't you pop in and say hello or something? Damn, what rudeness."

    hi "I got back yesterday. I was really just tired. Jetlag."

    ke "Jetlag?"

    "He doesn't seem convinced."

    hi "Well, it wasn't that far. I got here by train. Trainlag, I guess?"

    ke "Train…lag? Yeah I have never heard of that."

    hi "It's a growing phenomenon. In Tokyo."
    
    show kenji happy
    with charachange

    ke "Really… Oh, well. It doesn't matter anyway."
    
    show kenji tsun
    with charachange

    ke "Could have at least told me you were leaving, man. We're like, dorm buddies, or some shit. That's a sacred bond, at least until one of us gets a better room. And I kind of need you. In a non-homosexual way. Like to pick up my mail."

    show kenji neutral
    with charachange
    
    ke "If you did tell me and I just forgot, you can totally ignore this."

    ke "Oh yeah, I also signed over all my mail to you, so I'm going to need you to get it later on."

    hi "What?"

    "He quickly changes the subject again. It's almost like he expected it. This has to border on precognizance."
    
    show kenji happy
    with charachange

    ke "Hey, let's go hang out somewhere. We can hit the town. Maybe hit on some women. It's a weekday, right?"

    hi "Are you out of your mind? It's too early. Look at the time."
    
    show kenji neutral
    with charachange

    ke "So? That's a good thing. We can beat the rush, duh. Step up your game, Hisao."

    hi "What? What does that even mean?"

    hi "Beat the rush?"

    "That reminds me of Shizune. I contemplate asking him to never say it again."
    
    show kenji rage at left
    play sound sfx_impact
    with vpunch

    "Suddenly, Kenji jumps back and presses himself against his door like he is trying to force himself right through it. I follow his line of sight and see Shizune standing a small distance behind me."

    stop music fadeout 0.5
    play music music_tension fadein 0.5
    
    
    show shizu behind_smile at tworight
    with charaenter
    
    ssh "Good morning."

    show shizu behind_blank at tworight
    with charachange

    ssh "Are you in the middle of something?"

    ke "Who is that? Wait, a woman? Are we still in the male dorms? Where am I? What the hell?"

    "Shizune doesn't seem to notice him and just keeps looking at me for an answer."

    hi "Kind of."
    
    show kenji tsun at left
    with charachange

    ke "What's that, some kind of signal?"
    
    show shizu adjust_happy at tworight
    with charachange

    ssh "Okay. Do you know why I'm here today? I'll give you one guess, because I'm going to expect a little more from you today."

    ke "Hey, Hisao, what is that? Is she casting a spell?"

    hi "This is Shizune. My girlfriend. She's the student council president."
    
    show shizu behind_blank at tworight
    with charachange

    ssh "Who is this? One of your friends? Are you going to introduce us?"

    hi "Kenji, do you want me to introduce you to her or what?"

    ke "But you just did that. And, no. Why would you do that?"

    ke "Look at her. She looks so hostile. Like she's going to kick me in the groin. Can't take that chance… I have a legacy."

    stop music fadeout 0.5
    
    play sound sfx_dooropen
    
    show kenji tsun at offscreenleft
    with charamove
    
    play sound sfx_doorclose
    
    hide kenji
    
    show shizu behind_blank 
    with charamove

    "Without another word, he turns and opens the door to his room, then slips inside and closes it behind him soundlessly. It's immediately followed by the clacking of ten different locks slamming into place."

    play music music_shizune fadein 1.0
    
    ssh "Who was that? One of your friends? Why didn't you introduce us?"

    "She hasn't budged an inch. None of this seemed strange to you? Really?"

    hi "His name is Kenji. He kind of had some other stuff to take care of. He's also a little shy."

    ssh "I see."
    
    show shizu behind_smile
    with charachange
    
    show shizu behind_blank
    with charachange

    "The corners of her mouth lift in a very brief smile."

    ssh "You never answered my question. Can you guess why I am here? Nevermind, I'll just come out with it:"

    ssh "Yesterday, you said that we would go out and get some junk food together, and I've decided to collect on that voucher."

    hi "You said sometime this week."

    ssh "I couldn't wait, and it's not right for a man to keep a girl waiting needlessly long for anything. I'm doing you a favor. Are you ready?"

    "Shizune seems particularly playful today, although like always there is a hint of aggressiveness in every one of her actions."

    "I do want to go somewhere today, just the two of us. And yet, a part of me wants to argue with her, just to toy with her a little bit. Am I picking up aspects of her personality? It's pretty funny."

    hi "I'm not, actually. Where are we going to go this early, anyway?"
    
    show shizu behind_smile
    with charachange

    ssh "This is the best time of day to wander around town. The grass will be freshly cut, and all the stores will be just opening. When we order out junk food, it will be freshly made and cooked in a new batch of oil."

    ssh "If we get some coffee, we can be guaranteed that it's just brewed and hasn't been sitting out there all day."
    
    show shizu behind_blank
    with charachange

    ssh "Of course, none of that matters unless we leave soon."

    hi "I need to shower and get dressed."
    
    show shizu adjust_frown
    with charachange

    "She looks crestfallen, frowning at the news and adjusting her glasses halfheartedly, unwilling to accept it."

    ssh "Disappointing… You're really the worst, ruining the natural flow of my day like this. Human beings should live their lives in motion, and now it's like you brought my anticipation to a grinding halt…"

    hi "You can't wait fifteen minutes?"
    
    show shizu behind_smile
    with charachange
    stop music fadeout 1.0
    "She crosses her arms and rolls her eyes, but returns my smile. She isn't even half as bad tempered as she lets on, I think."
    
    

    scene bg school_gate
    with shorttimeskip
    play music music_tranquil fadein 2.0
    
    "It's almost noon when we get back. My stomach is heavy from all the food I ate today, though it's offset by the lightness of my wallet."
    
    show shizu behind_blank
    with charaenter

    hi "I don't know how you can be totally unaffected by all that junk food…"

    ssh "I'm always active."

    "What a simple answer."
    
    hide shizu
    with charaexit

    "This is usually where we say our goodbyes, so I wave goodbye to her and start heading back to my room. I'm really tired today. Shizune practically pulled me by the arm halfway across town and back."

    "Who knew that she had so many favorite restaurants? Organized by ranking on a typed list, no less."
    
    scene bg school_dormext_full
    with locationchange

    "Halfway to my room, I realize that Shizune is still following me."
    
    show shizu basic_normal
    with charaenter
    

    ssh "I just had a thought: I've never seen the inside of your room. Why can't I? Is there a problem with that?"

    hi "No, of course not."

    "Even if I had anything to hide, I don't have the strength to challenge her right now. She trails me all the way back to the dorms and then into my room."
    
    scene bg school_dormhallway
    with locationchange
    play sound sfx_dooropen
    scene bg school_dormhisao
    with locationchange
    
    show shizu behind_blank
    with charaenter

    "Her head takes in my room in one long, analytical pan. It reminds me of the motion of a surveilance camera. I can't read her face, but she looks like she's thinking, “So, this is your room?”"

    "She stops rather harshly at the rows of medicine bottles that line the top of my dresser, and I step in front of her to try and stop her from saying anything about them. Out of sight, out of mind."

    "Shizune is too smart for that, though, and I can see from her face that she already saw them, and probably knows what they are. Despite that, she doesn't say anything, although I know that she probably thought of it."

    stop music fadeout 0.5
    
    show shizu basic_normal
    with charachange

    ssh "Do you like this school?"

    "How am I supposed to answer that? Well, she is the student council president, and takes a lot of pride in her work. Sometimes it kind of borders on megalomania. I don't exactly hate it, it's just a school."

    ssh "It's okay, I won't get mad if you say no just because I'm the student council president."
    
    show shizu basic_angry
    with charachange
    
    play music music_drama fadein 3.0

    ssh "I don't like this school."

    ssh "It's so isolated. A lonely school on top of a mountain. And the people in it… It's like a place where parents drop off the children they are ashamed of so they can be free until the holidays."

    ssh "…But maybe that is kind of cynical?"

    "Actually, I've had that thought myself a few times. While everyone here seems mostly happy, I don't doubt that that's how it is in some cases. Is that true for her?"

    show shizu behind_frown
    with charachange

    ssh "Misha sometimes says that I make trouble for her, because the student council never did any work before I arrived. I'm the one who volunteered the student council to take on so much responsibility."

    ssh "My selfishness is the reason you had to go through so much. Do you hate me?"

    hi "No. Why did you do that?"
    
    show shizu basic_angry
    with charachange

    ssh "Because I'm selfish. And, because I wanted to be the student council president, but the position itself seemed like a joke when I got it. What's the use of a title if it's not earned? I don't want to be talked down to."

    "There is passion in her eyes, but she seems kind of sad."

    ssh "I don't like other deaf people. Or most disabled people in general. They isolate themselves because they don't want to face the reality of what they are. That makes them just as bad as the people who they are afraid will judge them."
    
    show shizu behind_frown
    with charachange
    
    ssh "I'll… become a normal member of society."

    "…"
    
    show shizu behind_sad
    with charachange
    
    ssh "I do that too sometimes, though. Hisao, am I just as bad as them?"

    hi "It seems like you just want to be normal."
    
    stop music fadeout 1.0

    "That answer seems to satisfy her."
    
    show shizu behind_blank
    with charachange

    ssh "Close your eyes."

    hi "What?"

    ssh "Just do it."
    
    scene black
    with shuteye

    "I do my best to try and keep them open just a little bit, but she's smart and touches my eyelids with her fingers to make sure I really have them closed."
    
    play sound sfx_rustling

    "I feel her hands moving my arms behind my back and tying them together by the wrists, and open my eyes."
    
    scene bg school_dormhisao
    show shizu basic_angry_close
    with openeye

    hi "What are you doing?"

    play music music_heart fadein 2.0

    ssh "I tied your hands. It's not a little red string of fate, but it will do."

    ssh "I don't think I have ever told you that I love you. I'll say it right now, but I don't want you to sign it back, and this is to make sure of it. Okay?"

    "Her lips are set in a determined line, and her eyes are downturned. She looks almost angry, but I can see that she is forcing her expression to look that way. Her natural aggressiveness carries over even here, to this."

    ssh "I love you."

    ssh "I'm about to give myself to you completely, so if you're cheating on me by dating other girls in other save files, I'll never forgive you."

    "What is she saying? She presses forward against my body, bending over me so that she can look directly at my face, our knees touching."

    hi "Hey, Shizune, this isn't another joke, is it?"

    "With my hands literally tied, I know it's meaningless to ask. She won't understand. It's more reflexive than anything. I can feel my body growing hotter as she starts leaning against the chair to support her as she draws herself closer against me."

    "I can't believe it."

    "Her eyes are so large and dark. They really are quite beautiful this close up. So clear and round. I can see myself reflected in them, and I look so small."

    hi "Shizune—" #reminder for the potential {nw} break

    "Before I can continue, Shizune raises a finger next to her ear and wags it admonishingly, quickly turning it into a very simplified gesture."
    
    show shizu adjust_happy_close
    with charachange

    ssh "Shut up."

    "Her hands undo my belt, and I can feel my pants sliding down, stopping at my ankles, my shoes preventing her from taking them all the way off."

    return

label en_S28h:
    
    scene white
    with whiteout

    "Shizune pauses, then starts to remove my underwear. Just like her, she does it slowly, tentatively. I can feel her chest pressing against me, rising and falling with each one of her deep breaths."

    "She pokes my hard erection with her index finger, her face reddening as she runs the rest of her fingers down the underside of it. I have to struggle not to let out any noise. It's really quiet."

    "Even though a lot of students have gone home for the holidays, there's always the off chance someone might pass by. The walls are thin. It's difficult to do so with Shizune tapping, touching, and stroking me like this, though."

    "It seems like she's done looking at it intellectually. She moves back a little awkwardly. That combined with the redness on her face and her evasive eyes belie her inexperience."

    "My breath catches in my throat and I grind my teeth together when I feel Shizune's tongue wrap around my rod before she envelops it with her whole mouth, slowly slipping it past her soft lips."

    "She flattens her tongue against the base of my member and starts sliding it backwards towards the head. It feels like the lower half of my body is burning up."

    "The knot around my wrists prevents me from doing anything but trying to brace my back against the chair as Shizune's tongue continues its assault on my penis, pressing and twisting around it."

    "Her warm breath tickles as it blows against my crotch and only serves to inflame me further. I feel terrible being unable to move; it feels almost like I'm chained down as my senses are bombarded by the feel of Shizune's hot tongue"

    "bathing my shaft, lubricated by her slick saliva. Somehow, I think that that might even have been her intention. I don't think I can hold out much longer."

    "This is unreal. The stimulation is making my head spin as she traces a path up and down my length slowly. Agonizingly slowly, her whole mouth trembling as she looks up at me, trying to read my expression as I try and read hers."

    "Those eyes. I can't bear to look at those deep eyes staring at me almost questioningly."

    "The blood pounds in my head, almost feeling like a headache. My heart beats faster and faster to the point where I think it might burst as Shizune's delicate fingers tap against my waist, tracing the bones of my hips."

    "She is so sensual. How can she be so good at this?"

    "Unable to withstand it any longer, my semen bursts in Shizune's mouth, the feeling only aggravated by her tensing up against my legs from the sensation."

    return

label en_S28x:
    
    scene bg school_dormhisao
    show shizu adjust_blush_close
    with locationchange
    
    "I open my eyes. Shizune's usually cool face appears troubled. Embarrassed. She really is a shy girl. Even she can't believe what she just did."

    "Her bright pink tongue moves across her lips, from one side to the other. It seems so seductive, even though it's easy to see that she didn't mean it to be."
    
    hide shizu
    with charaexit

    "She slips behind me and unties my hands, but I feel too drained to move. It doesn't matter, anyway, as she comes back around to where I am."
    
    show shizu basic_normal2
    with charaenter
    with Pause(1.0)
    show shizu adjust_blush
    with charachange

    "Shizune plays with her fingers almost in a dreamlike state, before snapping out of it and pushing her glasses up the bridge of her nose. She looked so distant for a second there."
    
    stop music fadeout 4.0

    "Her head rises as if she is about to say something, but then she starts moving briskly to the door, blushing bright red. I quickly get up to stop her, almost tripping over my pants. How uncool."
    
    show bg school_dormhisao at bgright
    with charamove

    "None of that factors in my mind, though."

    hi "Wait!"

    "I grab her arm and she stiffens up before breaking free. As if on second thought, she turns to me and starts signing."
    
    show shizu behind_blank
    with charachange

    ssh "I'm going now. I have to think."

    "Before I can respond, she emphatically shakes her head from side to side, shutting me down before I can even raise my hands."

    ssh "Please pull up your pants."
    
    show shizu adjust_happy
    with charachange

    "A smile forms on her lips, one that she tries to cover with a dainty hand almost immediately."
    
    show shizu basic_normal2
    with charachange

    "Like an afterthought, her hands form a sentence slowly, unsure of themselves."

    ssh "Nothing that I do is without reason…?"

    "Is that a question?"
    
    hide shizu
    with charaexit
    
    play sound sfx_impact2

    "Before I can ask, she leaves, the door almost slamming shut behind her and piercing the silence of my room."

    "It's a weird feeling to be left alone like this."
    
    scene black
    with dissolve

    return

label en_S29:

    #short scene is really short
    
    scene bg school_dormhisao
    with locationchange
    
    play music music_night fadein 0.2

    "It's been two days, and I haven't seen Shizune since then."

    "I've heard that sex changes almost everything in a relationship. But, I don't feel any differently from before. If anything has changed, then it has only for her."

    "The thought scares me. There is still a lot I don't know about Shizune. What I have from the pieces of her life I picked up from her and Misha is the image of a person that I like. A person that I want to know more about."

    "I wonder how she feels."
    
    stop music

    "The smallness and impersonality of my dorm room are starting to get to me. Throwing on a jacket since it looks unusually breezy outside, I head outside and decide to take a walk around the school grounds."

    scene bg school_courtyard
    with locationchange

    "The weather today is nice. The school looks very tranquil, but it's not enough to make me feel soothed in any way."

    "As I finish a can of coffee from the vending machine, I glimpse a familiar pink haircut rapidly approaching from behind me in the corner of my eye and immediately know what is coming next. I don't move as a pair of hands cover my eyes."

    scene black
    with hands_in

    mi "Guess who~!"

    hi "Hi, Misha."
    
    scene bg school_courtyard
    with hands_out

    "She giggles and then lets go."
    
    show misha hips_grin
    with charaenter
    
    mi "Hi, Hicchan~!"

    mi "How are you?"

    hi "I'm alright, thanks."

    mi "Really? That's great~!"
    
    play sound sfx_can_clatter

    "She follows me as I walk over to throw my empty can into a trash basket, bobbing up and down on the balls of her feet. There is a silence between us, and I can tell that she isn't here for no reason."

    "Maybe I have been underestimating Misha all this time."
    
    show misha cross_smile
    with charachange

    mi "Hicchan, did you and Shicchan have a fight?"

    "There is an inquiring smile on her face that seems exaggerated when combined with the soft and lilting concern with which she asks her question."

    hi "No."
    
    show misha perky_confused
    with charachange

    mi "Ah. Okay…"
    
    hi "Why are you asking? How is she?"
    
    show misha perky_smile
    with charachange

    mi "I was just curious, Hicchan. Shicchan came back to her room and she was blushing. And then~! The past few days, she told me that she just wants to think."
   
    show misha sign_smile
    with charachange
    
    mi "So~! I thought that maybe, you two had had a fight. I'm happy, now that I know better."

    mi "Unless Hicchan is lying to me. If you and Shicchan did have a fight, you should both make up as quickly as possible. There is no good in just letting something sit for a long time, it'll only lead to bigger problems."

    hi "Where is she now?"

    mi "Hm~… In the student council room, I think."

    "Hearing about the student council room reminds me of something Shizune had said the last time I saw her."

    hi "Hey, Misha, Shizune asked me if I resented her."
    
    show misha hips_frown
    with charachange

    "A concerned look immediately appears on her face, and I wave my hand in front of me to dissuade her fears."

    hi "No, no, it's not like that. Really. She meant because she roped me into the student council, and because it's her fault that the student council has that much work. She was afraid that maybe you would kind of resent her for it, too."

    hi "I couldn't answer her."

    "Because she had tied my hands behind my back."

    hi "The only thing I was mad about was that I couldn't say anything back. The next time you see her, can you just tell her that I don't resent her for it at all?"

    hi "I actually really like her. If it wasn't for everything that happened, my life would be… totally different."
    
    show misha sign_confused
    with charachange

    mi "Why don't you tell her yourself, Hicchan?"

    "Misha, you are really earnest. I guess you've got me there."

    hi "Haha… well… Yeah, she has kind of been avoiding me lately, I think."

    hi "So, I kind of need your help. If you see her, can you please tell her that?"
    
    show misha cross_smile
    with charachange

    mi "Of course, Hicchan~!"

    "She gives me a small salute, and I really look at her for the first time today. Everything she says, she is signing with her hands out of habit."

    hi "Misha, how did you get into this school?"
    
    show misha perky_sad
    with charachange

    "As soon as I ask, I wonder if maybe I've gone too far, and try to pad it out a little."

    hi "I have a heart problem, but I'm pretty sure that you and Shizune both know that."

    hi "Shizune told me that she hates this school, because it's like a place where disabled kids are sent to be isolated from the rest of society."

    "I'm just digging myself deeper."

    hi "You don't have to answer it if you don't want to. Just forget it."
    
    show misha perky_smile
    with charachange

    mi "Hm… No, it's fine. There is nothing wrong with me at all, Hicchan~."

    mi "This is an expensive school, and hard to get into. You're right about that."

    mi "I'm… a special case… Yeah~! Let's go with that, Hicchan~."

    "Talking about it looks like it upsets her, and I'm as eager to move away from the subject as she is."

    mi "Hicchan, can we sit down and talk for a little while?"

    hi "Oh? Sure."
    
    show bg school_courtyard at bgleft
    with charamove
    show misha perky_smile at centersit
    with charamove

    "Looking relieved, Misha stretches her arms and takes a seat right on the grass."

    hi "Right here?"

    mi "Yup~! Is there something wrong?"

    hi "No, not at all."

    "After checking for bugs and dirt, I sit down next to her. She watches me the whole time."

    return

    #split

label en_S29a:

    #1) If you had sex with Misha

    mi "Hicchan, did you and Shicchan… do anything?"

    "Misha starts laughing when she sees my expression."
    
    show misha cross_laugh at centersit
    with charachange

    mi "Hahaha~. I see."
    
    show misha cross_smile at centersit
    with charachange

    mi "Oh, well~! It was bound to happen eventually…"
    
    show misha perky_confused at centersit
    with charachange

    "Misha pauses and lets out a sigh."

    mi "Was I your first?"

    "The guilt in her voice is staggering, and cuts into me like a knife, the feeling only amphlified by the growing silence. Maybe this question was on her mind since the very beginning."

    "In the end, I can't answer."

    mi "I see."

    "…"

    return

label en_S29b:

    #2) If you did not have sex with Misha

    mi "Hicchan, did you and Shicchan… do anything?"

    "She bursts out laughing when she sees my expression."

    show misha cross_laugh at centersit
    with charachange

    mi "Hahaha~. I see."
    
    show misha cross_smile at centersit
    with charachange

    mi "Oh, well~! It was bound to happen eventually, right? Right~."

    "Her next words are preceded by, and delivered with, the melancholy of someone who feels they are being left behind."
    
    show misha perky_sad at centersit
    with charachange

    mi "Shicchan's life keeps moving on."

    hi "You have a life too, you know."
    
    show misha  hips_grin at centersit
    with charachange

    mi "Wahahaha~! Yeah~! Of course~! I know that, Hicchan."

    "…"

    return

label en_S29x:

    # end splits
    
    show misha sign_smile at centersit
    with charachange

    mi "I have always thought that, since I don't like myself, maybe I should love everyone else."

    mi "So~! I don't want to resent you, Hicchan. Even though I do, sometimes."

    mi "And, I really hate myself, sometimes."

    mi "It's really kind of strange, isn't it?"
    
    #hide misha
    #with charahide
    
    show misha sign_smile at Transform(xanchor=0.5, xpos=0.5, ypos=2.0)
    with charaexit

    "Misha lets herself fall backwards, so that she is lying on the grass."

    mi "Ah~ well…"

    mi "That is only because I can't feel very happy unless the people around me are happy. Which makes me a shallow person? It's just how I am, though."

    mi "Lately, Shicchan seems so happy, though. And~! You're happy too, with Shicchan, right?"

    mi "So, I'm glad."

    mi "Heh~."

    "Her eyes close. She looks peaceful. Then, they shoot open again, and Misha shoots her arm outwards towards me, shaking it when I don't seem to get the message."

    mi "I want to get up now. Pull me up, Hicchan~!"
    
    show misha perky_smile at center
    with charamove_slow

    "I oblige and pull her up, her fingers tightly gripping mine. She stands up and stretches, then tries to look over her shoulder."

    mi "Hicchan, do I have grass on my back?"

    hi "No. Well, not much, anyway."

    mi "As long as it's not much, that's okay~!"

    mi "Thanks for listening to me, Hicchan."

    mi "I'm… a little stupid. I have a bad short term memory, Hicchan. But, I have a really great long term memory."

    mi "I wonder what the me ten years from now will be like. Or twenty years. Thirty. Forty. Fifty."

    mi "I wonder what kind of things I'll remember then. I… have to decide now, you see. I'll try hard to remember the things I want to remember, and maybe I can just forget things I want to forget."

    mi "So~! I'm going to try and remember you and Shicchan."

    mi "Ah, no… You told me back then that just because we're going to be graduating soon that that doesn't mean we'll never see each other again, didn't you? You're right, it shouldn't."

    mi "I won't have to try to remember, because it's not really the end of anything, right, Hicchan~?"

    "Her hands held at her sides like that, she looks so happy that I can't bring myself to do anything but agree."

    hi "Yeah, you're right, it's not."
    
    stop music fadeout 10.0

    #btw I kill her in the next scene.

    return

label en_S30:

    #sup? this scene is from Misha's point of view

    scene black with dissolve
    centered "~ Misha's POV ~" with dissolve
    
    "I have always been really happy when the people around me are happy, too."

    "Because of that, lately I think more and more about what my life will be like when I will leave Yamaku."

    "It was really lucky for me that I was able to get into this school, and even luckier that I could meet Shicchan. If it wasn't for that, then I don't know if I would be here today."

    "I am who I am, so… I wouldn't, probably."

    "In just a few months, me, Shicchan, and Hicchan will all go our separate ways. It's like how a lot of flowers bloom on the same tree, but then when they fall, they never all fall together, do they?"

    "I'm right~! Haha…"

    "I only had a few friends in grade school, and in middle school, too. I remembered them for a long time after we stopped going to school together, but then they stopped talking to me. Their lives moved on, and I forgot them."

    "Shicchan… Is Shicchan going to forget me when she leaves this school?"

    "Will I have to forget Shicchan?"

    "I can't do that. Never. But, I know it will happen."

    "Hicchan said that just because we won't be going to school together, that doesn't mean that friendships have to end. If you fight hard enough for it, you can hold onto a friendship."

    "If I have to work so hard for it, though, then it's pointless. Of course I'll give it my 100\%! But it doesn't meant anything if Shicchan were to move on and stop being my friend. If she wouldn't try, then I don't think I could."

    "After all, then I would just be in Shicchan's way~."

    "If that happens, I don't know if I could go on."

    "It's likely that that will be what happens."

    "I only have ever loved Shicchan, even from the first day we met."

    "Shicchan once told me that she doesn't like Yamaku because it's where parents send the kids they are ashamed of."

    "It's true, Shicchan. I'm one of those children nobody wants. I have always been bullied, because I'm different. Isn't that something that I can't change? I'm really sorry. The things that are wrong with me, I can't change."

    "Not enough was wrong with me that I could get into Yamaku, so I had to make up a lie, that I wanted to be a sign language teacher. I don't like to lie, but the person I am now is a big liar, so…"

    "Shicchan, I wanted to talk to you, so I learned sign language, even though I wasn't very good at it, and I'm forgetful."

    "You told me that a human being doesn't need a meaning, or a purpose, or respect; those can all be gained if you work hard enough."

    "I'll really become one; a sign language teacher. If I'm something, then I'll be a real person to you, right, Shicchan?"

    "The only person I have really had is Shicchan."

    "Shicchan, I really, really love you."

    "I wish I could just interpret for you forever."

    "I know it's unrealistic, though. You would hate me eventually, because I wouldn't be a person moving forward in life."

    "If Shicchan were to hate me, I would probably die."

    "Haha~. If Shicchan and I keep going, then we'll drift apart. But the same thing might happen if we stay together."

    "I guess I'm just not the right person for you, Shicchan."

    "So~… I've been thinking about “that” for a long time…"

    "Maybe it's better if I didn't exist."

    "…"

    "I talked with Hicchan the other day. It's hard for me to understand Hicchan, but he seems like a good person. I feel a lot better now, because I was able to tell someone how I feel."

    "The things I want to tell Shicchan would be silly to her, and I don't know if I could sign all of that to her. And~! Shicchan has her own life."

    "Shicchan and Hicchan are a real couple now. I'm so glad. I was able to see them both fall in love."

    "Even if it's not me, I'm still really glad…"

    "Am I really glad?"

    "I'm really, really glad. I really am."

    "I really am…"

    "Hahaha~."

    "Hm~ hm~… It's time for a shower. I like the feeling of warm water against my skin. I'll feel refreshed."

    "Haha…"

    # fade

    "Yay~! I'm done, and my hair is almost totally dried. The person who told me that I looked cuter with my hair like this was Shicchan. I don't even really remember what I looked like with my hair straight."

    "I try the doorknob, because she always leaves her room unlocked when she is inside. It's open."

    "Shicchan is sitting at her desk reading a book. She sees me and waves hi."

    mi "Morning, Shicchan~!"

    ssh "Good morning."

    "I laugh and plop down on her bed. It's soft, she has different sheets than I do."

    mi "How are you, Shicchan?"

    ssh "I'm doing well. It's very early for you to be up. Is there something different about today?"

    mi "Yup~! Well, no. Well, yes and no, Shicchan. I talked with Hicchan, and he told me to tell you that he doesn't resent you at all."

    ssh "Really?"

    mi "Yup. I don't know what you two were talking about, but he said that it doesn't matter if the student council has so much work, or that he has to put up with so much work because of you."

    mi "He said that if it wasn't for you, his life wouldn't be the same. Hicchan really likes you, Shicchan."

    "Shicchan doesn't say anything, she just thinks."

    mi "Shicchan, did you tell Hicchan that you didn't know if I might hate you for that?"

    ssh "Yes, I did."

    mi "Well, you don't have to worry about that, Shicchan~! I don't resent you at all, either. I feel the same way."

    "Shicchan gets up from her desk and walks over to me."

    ssh "Thank you. I'm happy that you think that way."

    "I'm really happy, too~…"

    mi "Really, Shicchan? Okay~! Let's go out somewhere, then~!"

    ssh "What do you mean?"

    mi "Shicchan, it's no good for a young girl to stay inside all the time. And~! We haven't gone out together in a long time. Soon, Shicchan is going to be going on more and more dates with Hicchan, so we have to hang out together now~!"

    "Please bear with my selfishness, Shicchan. She smiles and starts putting on her jacket."

    ssh "Okay. Where should we go?"

    mi "Hm… Anywhere."

    ssh "You should decide. I'm thankful to you, so I want it to be someplace you want to go."

    "Anywhere is fine though. Where we go doesn't matter to me, Shicchan."

    # transition to the inside of some kind of clothing store. Or a mall. It doesn't really matter.

    "Me and Shicchan haven't really gone out together by ourselves in a long time, so I'm really happy."

    "We eat lunch, getting what we each want from two different restaurants. I'm not as active as Shicchan, so I can't eat all the things she eats."

    "Then, we go shopping. It's her idea, because she thinks that I could use more clothes. Okay~! I'll pick out some cute clothes for Shicchan too!"

    "The two of us go to one store, because they have nice skirts, but Shicchan wants to go to another store because they sell things at a better price, so we go there and start shopping."

    "I already bought a lot."

    "I even have a new blouse now. It's cute, but I don't know if the color will go with my hair."

    ssh "I'm going to blame you for that. With your hair color, it's hard to find anything that goes well with you."

    mi "Hahaha~! Sorry, Shicchan. Hm~… Hey~! Shicchan, this time it's my turn. I'll pick out something that will look cute on you."

    "She blushes. Shicchan is a little bit of a tomboy, so she doesn't like dressing up in clothes that are too feminine, but I want to see her like that."

    mi "Aw~… Come on, Shicchan? Just for today?"

    ssh "Fine."

    mi "That's great! I'm really glad."

    mi "Hahahaha~!"

    "I see a jacket that would look great on Shicchan's body. Her figure is nice, like a model."

    mi "How about this, Shicchan?"

    "After awhile, Shicchan gets annoyed because I keep making her put on new things."

    ssh "Stop! Stop!"

    mi "Wahaha~! What is it, Shicchan?"

    ssh "I'm beginning to think you are just playing with me."

    mi "Yup. But I like teasing Shicchan a little now and then~."

    "I want to hug her. Okay~! I'll do it."

    "As soon as my arms are around her, Shicchan freezes and gets very stiff. I let go of her."

    "Ah, that's right, Shicchan. You don't like it when people touch you. I guess you're unfamiliar with it, right? Right…"

    "So I'll never be able to hold Shicchan. It's okay if you don't hold me back, as long as I can feel Shicchan's warmth. At least, that's what I've been telling myself all this time."

    "Shicchan, even if I can't touch you, I'll still love you."

    "Right?"

    mi "Shicchan—" #reminder for the potential {nw} break

    "Haha~. My voice cracked. Am I sad?"

    "Shicchan's face is so concerned. Please stop looking at me like that, Shicchan. Please, don't…"

    "I hold my stomach and pretend to groan."

    mi "Haha~! Shicchan, I'm going to go somewhere else, just for a little bit, okay? Okay~!"

    mi "I'm just a little sick, don't worry about it~! Don't worry about it, okay, Shicchan? Okay~!"

    mi "I'll be right back, Shicchan~."

    # transition to some other place

    "Haha~."

    "I lied to Shicchan again."

    "That look on your face hurts me."

    "Maybe it would be better if Shicchan didn't care about me. But that is what I want."

    "Shicchan, do you like me?"

    "If you do, why did you reject my feelings?"

    "I want to hit myself. That's wrong. It's not like that… Thinking like that is really, really…"

    "Stupid Misha~…"

    "Shicchan, we're really too different."

    "Maybe it would be better if you were to just forget about me."

    "I'll… start to resent Shicchan someday."

    # some other transition to outside

    "We're leaving the store now. We really were there for a long time."

    "I spent a little too much of my own money, but it's okay."

    "Today was…"

    "I'm following behind Shicchan, like always. She turns back to look at me over her shoulder. Are you checking to see if I'm following you, Shicchan? Well, of course."

    "But…"

    "Shicchan, do you look over your shoulder because you're really the one looking out for me?"

    "…I see."

    "I'm sad."

    "No matter what I do, I'll never be the right person for Shicchan."

    "Shicchan and me are separated by too many things. The me that I am now will never be able to change any of them."

    "I don't think I ever will be able to."

    "It really makes me sad."

    play sound sfx_crash
    
    "To my right, I hear a loud noise, like a car horn. It's a bad noise. When you hear something like that… it's not something that you are supposed to hear. It means something is wrong."

    "I wonder where that car is going. Is it going to hit me?"

    "I turn in the direction of it."

    "This must be fate, right? After all, I have lived so long, and I never know what to do next. It can all be over if I just… don't move."

    "Haha~…"

    "Shicchan is growing smaller in front of me. See, Shicchan? Even without me, you will always be okay. Not like me without Shicchan."

    "Maybe it's because of that, that's why Shicchan has always seemed so tall compared to me."

    "It's because we're really, really different."

    "Shicchan is always so serious."

    "She always thinks about everything so deeply. I want her to smile more, because her smile is so cute. When Shicchan smiles, I feel the same way."

    "So, I thought, “Maybe I can be Shicchan's umbrella. I'll be whatever Shicchan needs me to be. I'll make Shicchan smile. Then, I'll be happy, too.”"

    "I always walk behind you, Shicchan, so I can catch you if you fall, and look out for you."

    "But I wonder if you ever needed that from me."

    "It looks like this is where it ends, though."

    "I don't really want to move."

    "I don't know if I can move."

    "I can see Shicchan still walking ahead of me."

    "Shicchan, with your back to me, I guess it's like I don't really exist. I can see you walking away. But~… That's really obvious, isn't it? Because Shicchan's life will always be moving forward."
    play sound sfx_crash
    play sound sfx_crunchydeath
    
    #sup? hit by a bus. Maybe some kind of agonizing 'hit by a bus' sound effect here

    scene bg misc_static with Dissolve(2.0)
    play music music_static fadein 2.0
    "When I wake up again, everything hurts. Shicchan is sitting over me. She looks really tall, but Shicchan has always looked like that to me."

    "I feel stupid."

    "Everything I do is the wrong thing, always. Even this time."

    "Even going out today was my idea. If it wasn't for me, Shicchan wouldn't be here right now."

    "Shicchan is crying. I can't feel my arms. My chest, it really hurts. Everything hurts. I wonder what I look like right now. Am I still small, compared to Shicchan? The way I look right now, I probably look smaller than even before."

    "I'm sorry, Shicchan. I can't grow as a person like you. If I could, then maybe everything would be different. I won't even be able to change from this, will I? If this was Shicchan, wouldn't you just try harder?"

    "I wish I could hug Shicchan. Shicchan, we have been together for a long time, right? Right. I never even hugged Shicchan. Or held her hand slowly. I want to do all those things. Just once, at least…"

    "I…"

    "Shicchan told me once that human beings can do anything. Human beings have infinite potential, right, Shicchan?"

    "If you want, if you really believe, and if you work hard, you can do anything. Isn't that what you said? I want to believe that. Now I remember. That time, you did hold my hand. That time, Shicchan was able to be my umbrella."

    "So, maybe…"

    "If I really believe, and try, and have hope…"

    "I don't know what I want to do, but at least for now…"

    "Please work! Please!"

    "…No, it's not going to work. I'm not like Shicchan."

    "I don't know if I can even move. My ears are ringing. If I tried to talk, what would happen?"

    "I'm scared."

    "I have to do something…"

    "Ah, I know~. I'll try to look happy for Shicchan like always."

    "Shicchan, I wanted to be like your Yamato Nadeshiko. I want to to be by your side forever. Isn't that what it means? To always help the person that you love, and to always be with them?"

    "Is it silly?"

    "…"

    "See? I'm smiling. So please cheer up, Shicchan."

    "…"

    "I'm really stupid."

    "…"

    window hide
    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.1)
    hide heartattack alpha
    with Dissolve (0.7)
    with Pause(0.7)
    window show
    
    "…"
    window hide
    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.1)
    hide heartattack alpha
    with Dissolve (0.7)
    with Pause(0.7)
    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.1)
    hide heartattack alpha
    with Dissolve (0.7)
    with Pause(0.7)
    window show

    "…"
    stop music fadeout 10.0
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
    with Pause(0.05)
    play sound sfx_heartstop
    show heartattack alpha 
    with Dissolve (0.1)
    show heartattack residual
    with Dissolve (0.8)
    show passoutOP1
    with Pause(7.0)
    scene black
    with None
    #yeah i guess act 3 ends here

    window hide dissolve
    return
