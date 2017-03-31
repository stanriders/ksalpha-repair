﻿label en_S31:

    window hide None
    
    scene black 
    with dissolve
    centered "~ Hisao's POV ~" 
    with dissolve
    
    play ambient sfx_businterior fadein 0.5
    
    #play music music_moonlight fadein 2.2
    scene black
    with Dissolve(3.0)
    
    scene bg city_busride_ss 
    with locationchange
    
    window show dissolve
    
    "I found out what happened through an email from Shizune on my cell phone. I didn't even notice it until almost 5 PM."

    "It's a bad habit I have, that I frequently forget to check or charge my phone, sometimes for days at a time."

    "So I didn't find out about the accident until almost six hours after it happened."
    
    stop ambient fadeout 1.5 

    scene bg hosp_ext_ss
    with shorttimeskipsilent
    
    $ renpy.music.set_volume(0.7, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 0.2

    "By the time I got to the hospital, it was too late."
    
    $ renpy.music.set_volume(0.2, 1.0, channel='ambient')
    scene bg hosp_hallway 
    with locationchange
        
    "“Shiina Mikado,” huh? It's kind of funny, that I didn't know your full name until then."

    "I'm a pretty lousy friend."

    "Afterwards, I was asked to answer some questions about Misha to the police. They were going to rule it as a suicide."

    "But that can't be right. The last day that I saw her, she looked so happy."

    "Unless that, too, was a lie."

    "I still refused to believe it. I told them that I refused to believe it. It's not denial, really. It's just that it I'm so sure they were wrong."

    "Despite…"

    "Misha, I was able to defend you at least this once. I hope I did a good job."

    "I'm sorry."

    stop ambient fadeout 1.5
    "…"
    
    #stop ambient fadeout 1.0
    
    #scene bg city_funeral
    #Lets try how this looks like, shall we? - Kelper
    #Also, this one confuses me. Should we show him while still in the graveyard/funeral? He talks about it in past tense. - Kelper
    $ renpy.music.set_volume(0.8, 0.0, channel='ambient')
    play ambient sfx_park fadein 1.0
    scene bg city_graveyard
    with shorttimeskipsilent
    
    #$ renpy.music.set_volume(0.2, 0.0, channel='ambient') 
    
    #play ambient sfx_crowd_indoors fadein 0.2

    "There was a surprisingly small number of people at the funeral."

    "In the days after, I was able to rationalize it. Bit by bit. I had to."

    "It's the summer, after all. And Misha was pretty sociable, but she really didn't hang out with a lot of people. I think really only Shizune, myself, and Yuuko knew her all that well."

    "Even so, it's depressing."

    "I don't think her parents were there."
    
    stop ambient fadeout 1.0
    
    #Felt like the depressing music should stop here -md01
    #stop music fadeout 7.0
    
    scene bg school_dormhisao 
    with shorttimeskipsilent
    
    $ renpy.music.set_volume(0.2, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 0.5
    "I haven't seen Shizune since that day."
    
    $ renpy.music.set_volume(0.2, 0.0, channel='sound') 
    play sound sfx_hammer
    
    $ renpy.pause(0.5)    
    
    #The next few lines were originally written like this. I changed them up so they flow better with some scene direction -md01
    #"A knock at the door takes me out of my reminescing. I'm grateful to whoever it is for that. Without thinking, I open the door. It's Hideaki. He has a bag on the floor next to him that he picks up when he sees me."
    
    "A knock at the door takes me out of my reminiscing. I'm grateful to whoever it is for that. Without thinking, I open the door."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='sound')
    
    play sound sfx_dooropen
    
    $ renpy.pause(0.5)
    scene bg school_dormhallway
    show hideaki normal 
    with Dissolve(1.0)
    play music music_night fadein 5.0
    $ renpy.music.set_volume(0.0, 6.0, channel='ambient')  
    show hideaki normal at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    with charamove
    
    show hideaki normal at center
    with charamove
    
    "It's Hideaki. He has a bag on the floor next to him that he picks up when he sees me."

    hh "Good morning."

    hi "Yeah."

    "It's his usual greeting, but his tone is different. I can tell pretty clearly that this is a hollow formality. It's strange seeing him without the intense energy he usually has."

    "I'm grateful to him. He's the one who arranged everything for the funeral."

    hh "How are you holding up?"

    "It's a hard question. What am I supposed to say? How should I answer that? I don't think there is any way for me to respond to it correctly."

    hi "Fine."

    hh "I see."
    
    show hideaki serious
    with charachange

    hh "How is Shizune?"

    hi "We haven't spoken in a while."
    
    show hideaki normal
    with charachange

    hh "I see. Would you like to go see her now? That is why I'm here. I thought maybe she could use some cheering up."
    
    show hideaki normal_up 
    with charachange

    hh "I'm… not really good at that, though. If you could lend me a hand, I would appreciate it. I'm sure she would be happy to see you, too."
    
    show hideaki serious_up
    with charachange

    hh "I'm also a little nervous about seeing her by myself. You being there will ease the tension a little. And, obviously, I need you to translate for me."
    
    show hideaki serious
    with charachange

    hh "We can go whenever you're ready."
    
    hi "Do you think Shizune would be okay with having visitors? She looked pretty down the last time I saw her."  

    "Actually, that would be an understatement."
    
    #Experimenting with this placement, now it's gonna play as soon as you open the door. - Kelper
    #play music music_night fadein 5.0
    
    show hideaki normal
    with charachange

    hi "So…"
    
    show hideaki sad 
    with charachange

    hh "You're right."
    
    hh "…"

    hh "Do you know why it was I who made arrangements for Mikado's funeral?"
    
    show hideaki thinking
    with Dissolve(1.0)

    "He pauses. I don't know if he expects me to answer him or not."
    
    show hideaki normal
    with Dissolve(1.0)

    hh "It would make more sense if Shizune had done it. Obviously."

    hh "But, it seems like after everything that happened, Shizune has decided to stop doing anything, or even thinking."

    hh "It's weird."

    "I don't think Hideaki has ever seen Shizune like that before."
    
    show hideaki serious_up 
    with charachange

    hh "I want to cheer her up. Don't you?"

    "That is a pretty simplistic way to look at it. Things aren't that easy. It makes sense for him to be able to say that kind of thing, though. He is Shizune's brother, after all."

    "Shizune would always act like that too, like every obstacle in your way could be easily taken down so long as you tried hard enough. If you kept going constantly, you could overcome anything. I think that was the gist of what she believed."

    "I still can't believe it fully. This time, though, I'll go with it, like always. Just because I have always wanted to believe in something like that."

    hi "Let's go right now, then."
    
    #Trying this background - Kelper
    #scene bg school_dormext_full 
    scene bg misc_sky at Fullpan(20.0)
    with fade

    "Outside it's like nothing has changed. The sun is shining pretty brightly in the sky. Any minute now, I expect Misha to grab me from behind and put her hands over my eyes."
    
    scene black
    with shuteye
    
    scene bg school_dormext_full_fb
    show noiseoverlay
    with flashback_slow
    
    $ renpy.pause(1.0)
    
    #Not sure of the hands in/out are a good idea here. -md01
    scene black 
    #I modified the hand thing, it was just too fast. New definition on line 1369, in ui_settings - Kelper
    with hands_inslow
    
    mi "Surprise~! Guess who~!"

    "…"
    
    #scene bg school_dormext_full_fb
    #with hands_out
    
    scene bg school_dormext_full with Dissolve(1.0)
    #with flashback_slow

    "Heh. I've dealt with it so long that it's kind of become a habit of mine to be on my guard for it. I guess I can stop now, huh?"

    "My eyes are kinda starting to sting."
    
    show hideaki serious
    with charaenter

    hh "Are you alright?"

    "We have to stop for a little while because of me."
    $ renpy.music.set_volume(0.5, 2.0, channel='ambient')
    stop music fadeout 3.6
    
    scene bg school_girlsdormhall 
    with locationskip
    
    
    $ renpy.music.set_volume(0.2, 0.0, channel='sound') 
    play sound sfx_hammer
    
    "Hideaki knocks on the door to Shizune's room reflexively before trying the knob and finding it unlocked."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='sound')
    play sound sfx_dooropen
    
    $ renpy.pause(0.5)
    
    $ renpy.music.set_volume(0.3, 0.5, channel='ambient') 
     
    scene bg school_dormshizune at left
    with locationchange

    "This is the first time I have been in Shizune's room. It's very plain and utilitarian, although I can see a personal touch here and there."

    "She still has the doll I won for her back then, on top of her desk."
    
    #show shizu behind_blank at tworight
    #show hideaki serious at twoleft 
    #with charaenter
    #show shizu behind_sad at Position(xpos=0.9, ypos=1.1) with charachange
    
    #I think this is a better cue for this music, it's weird to play a dramatic song over the room's description - Kelper
    
    stop ambient fadeout 3.0
    show shizu basic_normal2 #at tworight
    #with charachange
    with Dissolve(1.2)
    #with Pause(0.5)
    play music music_moon fadein 0.5
   
    "When I get close enough for her to notice me, she looks up, and then quickly turns her head away."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    "She is sitting in her bed, back against the wall. There is a box of books beside her that she keeps held to her side."

    "The expression on her face is devoid of emotion, but I can see faint red tinges around her eyes."

    "It really is kind of unsettling seeing her like this."
    
    scene bg school_dormshizune at center
    show shizu basic_normal2 at tworight
    with dissolvecharamove
    
    show hideaki serious at twoleft
    with charaenter
    
    hh "Hisao, can you please translate what I say to her?"
    
    

    "I don't have the heart to tell him that she won't even look in my direction. I'll try, though. I'll keep moving in front of you if I have to, Shizune."
    
    show hideaki happy at twoleft 
    with charachange

    hh "Hello, Shizune."

    hh "Are you doing okay?"

    shi "…"
    
    show shizu behind_blank at tworight
    with charachange

    "Shizune's eyes seem to stare past us, instead of focusing on us. She nods as if to acknowledge our presence, but doesn't lift her hands to greet me at all."

    hi "Hi, Shizune."

    shi "…"

    "She doesn't move from where she is. In fact, the closer we go to her, the smaller she seems to get."
    
    show hideaki happy_up at twoleft
    with charachange

    hh "I have a present for you. It's a laptop computer. I made sure it was a slightly older model, since I know you like old fashioned things."

    hh "We can talk through this."
    
    show shizu basic_normal2 at tworight
    with charachange

    shi "…"
    
    show hideaki sad at twoleft 
    with charachange

    hh "Don't you want to talk to me?"

    "Shizune's hands remain limp at her sides even as Hideaki places the laptop in front of her."
    
    show hideaki serious at twoleft 
    with charachange

    hh "Shizune, is there anything I can do for you at all?"

    shi "…"

    "Although I'm translating for Hideaki, I hope Shizune realizes that I consider myself to be speaking for the both of us. Unfortunately, it looks like she is actively trying to avoid looking at either of us."
    
    show hideaki serious_up at twoleft
    with charachange

    hh "I came all the way out here to see you. Please… do something. Can you at least look at me?"
    
    show hideaki sad at twoleft 
    with charachange

    hh "Why won't you answer? I… sort of care."
    
    show hideaki thinking at twoleft
    with charachange
    
    hh "…"
    
    show hideaki sad at twoleft
    with charachange

    hh "Fine, if you're going to be that way, then I understand completely. I'll be back some other time."
    
    show hideaki invis at Position(xpos=0.2) with dissolvecharamove
    
    $ renpy.pause(0.7)
    
    play sound sfx_doorclose
    $ renpy.pause(0.6)
    hide hideaki
    scene bg school_dormshizune at center
    show shizu basic_normal2
    with dissolvecharamove

    "After Hideaki leaves, I try to get a response out of her. I at least try to get her to look at me."
    
    "I'm about as successful as he was."

    "What am I doing? There is nothing I can do right now."

    hi "I'll come back when you're feeling better, okay?"
    
    scene bg school_girlsdormhall with locationchange
    
    stop music fadeout 7.0

    "As soon as I leave, I start to regret that I couldn't do something for her. I wasn't able to cheer her up at all. Really, I couldn't do anything at all."
    
    window hide dissolve    
    
    scene black 
    with Dissolve(1.5)
    
    return

label en_S32:

    #After the scene after this scene, the path splits into good and bad ends

    # I will probably rewrite this scene.
    $ renpy.music.set_volume(0.3, 0.0, channel='ambient')  
    play ambient sfx_rooftop fadein 0.5
    scene bg school_dormhisao with dissolve
    
    window show dissolve

    "I'm going to visit Shizune again today."

    "The last few days, all I've done is sulk. The thought that wouldn't leave me alone for even a second was how Shizune had looked the other day."

    "I guess someone is trying to tell me that I can't just leave things like that. I wanted to do more. I could have done more. I should have been there for her, in some way."

    "I could have even given her a hug. Although maybe that would have been cheesy. I'm not some kind of hero."

    "I'm not good with these kinds of situations. I could really use your help right now, Misha. Of course, that's impossible."

    "Putting on my shoes, I head for Shizune's room again."
    
    $ renpy.music.set_volume(0.5, 0.5, channel='ambient')  
    scene bg school_girlsdormhall with locationskip

    "When I'm standing in front of the door, I freeze. I'm a little afraid. She might not look at me again, and if that happens, I don't know if anything I do will matter. Even if she does look at me, I'm not sure I can face her."

    "Her eyes were always so dark and piercing, filled with the spirit of her life. What will they look like now?"

    "The truth is, I've already been here three times since I first came to visit with Hideaki."

    "The first time, she wouldn't respond to me, no matter what I did. After that, both times, the door was locked."

    "Could it be locked even today?"

    "If you're going to just shut me out like that, Shizune, I don't think I could live with myself."

    "I turn the doorknob, fillwed with a sense of dread that seems almost inexplicable. The door clicks open."
    
    play sound sfx_dooropen
    
    $ renpy.pause(1.3)
    
    #I feel like there should be a CG for this scene. -md01
    $ renpy.music.set_volume(0.3, 0.5, channel='ambient') 
    scene bg school_dormshizune
    show shizu behind_blank
    with locationchange
    
    #This track was set before I started. Is this a fucking joke? -md01
    #play music music_cellosolo fadein 0.2

    hi "Hi, Shizune."

    shi "…"

    hi "Are you feeling better?"

    "I almost want to kick myself at how terrible that sounds. What a crappy thing to say."

    "You opened your door again. Didn't you tell me that you never did anything without a reason? Yeah, multiple times. Did you leave your door unlocked because you want someone to talk to?"

    "If that's the case, then answer me, at least once."

    hi "Shizune, please. I'll turn on the laptop. You can type whatever you want to say to me, but please say something."

    "I know that I probably got half of that wrong, but I'm sure she got the message."

    "I press the power switch on the computer and watch as it quietly hums to life in front of her."

    hi "Here you go. It'll just take a second. Can you just talk? A little?"

    hi "I'm worried about you. That's why I'm here. So, please talk to me."

    "At first, I am already about to give up. After all, I've been around her long enough to know that her will is stronger than I could probably dare to guess at. And that means if she doesn't want to talk, then it's all on her terms."

    "Just like always."
    
    show shizu basic_normal2
    with charachange

    "Then, surprisingly, she pulls the laptop closer to her and starts typing. After a few seconds, she erases what she has been writing and starts to sign."
    
    stop ambient fadeout 3.0    
    play music music_sadness fadein 3.0
    
    show shizu behind_sad
    with charachange

    ssh "Do you know what these are?"
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient') 
    "Shizune takes out a book from the box at her side. She had this then, too. I take the book from her and look at it. It seems like an ordinary marble notebook, although it's been used quite a bit."

    "I flip through it. Every corner of it is filled with a large, childish handwriting and numerous doodles."

    ssh "These are Misha's."

    "There is little life in her hands as they shakily form words in the air."

    ssh "Read them."

    "It's disrespectful to read a dead person's private journals like this, isn't it?"
    
    show shizu basic_angry
    with charachange

    ssh "They were going to throw away everything in her room. I found these."
    
    show shizu behind_sad
    with charachange

    ssh "All this time, I never knew. But do you know what cuts me deepest?"

    "She flips through another one of Misha's journals, then points to a line scrawled at the bottom of a page."

    window hide dissolve
    play sound sfx_rustling
    $fixedwritten_note("I wish I could really speak to Shicchan.")
    window show dissolve
    "Before I can absorb it, she flips further through it and points at another line."
    window hide dissolve
    play sound sfx_rustling
    $fixedwritten_note("Shicchan, I wish I could talk to you more freely.")

    play sound sfx_rustling
    $fixedwritten_note("I wish I could express my feelings better to her.")

    play sound sfx_rustling
    $fixedwritten_note("They are both so happy. It's hard to keep laughing like this sometimes.")

    play sound sfx_rustling
    $fixedwritten_note("I wonder if Shicchan loves me.")

    window show dissolve
    "…"

    hi "What are you saying? There was no way you could have known. And you couldn't have done anything, anyway…"
    
    show shizu basic_normal2 with charachange

    ssh "Stop signing. It's not necessary."

    "What does that mean?"
    
    #I really wanted to pause the track and resume it below, but it appears that renpy can't do that, so here is this
    #stop music fadeout 0.5
    #$renpy.music.set_volume(0.0, delay=1.0, channel='music')
    #This doesn't work though, completely cuts the mood off. I'm not sure what you wanted to achieve here - Kelper
    
    ssh "I lied."

    #Again, is this a fucking joke? This doesn't fit AT ALL! -md01
    #When ever I hear this track I think of Kenji going on about feminists with a moon base.
    #play music music_tension fadein 0.2
    
    ssh "There is a saying that a lot of relationships are built on lies. For me, all my relationships are like that."
    
    show shizu behind_sad with charachange

    shi "…"

    ssh "Misha could have talked to me, like a normal girl."

    ssh "I can read lips."

    "My mind stops, half in disbelief."
    
    #stop music fadeout 0.2

    hi "Really?"
    
    show shizu basic_normal
    with charachange

    "I say it, somehow finding it hard to lift my arms. Shizune nods her head up and down."

    ssh "You are the only one who knows."

    "I want to sit down, but I almost can't feel my legs. If I move even an inch, will I stumble or fall? And if I do, how will she interpret it, with those eyes that never miss a thing?"
    
    #Music comes back in after dramtic pause
    #play music music_hanako fadein 2.0
    
    #$renpy.music.set_volume(1.0, delay=5.0, channel='music')
    
    ssh "I started liking you because of the things you said to me."
    
    #I love how inexplicable this sprite choice is. Why is she angry? Works great even if it was unintended. I'll be sad if this goes to make place for a CG. - Kelper
    show shizu behind_frown with charachange

    ssh "I'm deaf. It's fun to mock a deaf person when they can't hear what you're saying. Even when they are standing right in front of you, they can't understand."
    
    show shizu adjust_frown
    with charachange

    ssh "It's really funny, isn't it?"

    "For just a second, she drops her guard. Even at a time like this, in such a state, Shizune never fully lowered the wall around her, but just now, I was able to see her past."

    "There's little I know about you. I underatand now, though."

    "Your hands move so sadly, and so bitterly."

    "Like a person speaking from experience."
    
    show shizu basic_normal2
    with charachange

    ssh "You never said anything bad about me, even though you could have. That is when I started to like you."

    ssh "You spoke to me even when you didn't have to. So I grew to like you."

    ssh "And I love you because you were willing to learn sign language for me. There, you exceeded my expectations, and I was surprised."
    
    show shizu behind_smile with charachange

    "She smiles very faintly, remembering it."
    
    show shizu behind_sad
    with charachange

    ssh "I should have confessed to you. You know that I'm always cautious, though. I was afraid. I led you around for a long time. Misha wrote that she wanted to help me. So she did."

    ssh "I'm a cunning and deceitful woman."
    #Hahah - Kelper
    
    show shizu basic_angry
    with charachange

    ssh "Selfish, too."
    
    #show shizu behind_frown
    #with charachange

    ssh "I was even jealous because I thought you might have liked her more than me."
    
    #show shizu behind_blank
    #with charachange
    
    show shizu basic_normal2
    with charachange

    ssh "Misha did so much for me. I would sometimes wonder if I took her for granted. I'm not good at expressing my emotions."
    
    #show shizu basic_normal2
    #with charachange

    ssh "I'm not really good at reading other people's emotions either, am I? Or else I would have seen this coming."

    ssh "If she were here right now, I would tell her how much I loved her as a friend. I'm sorry."
    
    show shizu behind_sad with charachange

    ssh "I'm really sorry."

    "Tears start forming in the corners of her eyes. She tries hard to hold them back, but I wonder if this time, she still has the strength."

    "Shizune's head is bowed, as if she is awaiting some sort of divine punishment. That's probably exactly how she feels."

    ssh "Do you hate me?"
    
    stop music fadeout 8.0
    $renpy.music.set_volume(0.5, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 8.0
    "Right now, I can't even process what just happened. I'm numb from shock. There was no way that I could have known, but thinking back, it all makes so much sense."

    "You were right, nothing you do is ever without reason. I get it now. That's how you're able to be so aggressive, launching yourself into the world as fearlessly as you do. And at the same time, you can be so cautious and patient."


    "I always wondered how a person could have that kind of duality."

    "And I'm also a little offended that you played with me in such a way."

    "I still love you, though."

    "Even if I feel emptied out, like a balloon that has lost all the air in it."

    "But that is just shock. Even if right now, I feel like I can't breathe, it's just temporary…"

    #Doesn't it sound better here? - Kelper
    stop ambient fadeout 1.0
    hi "I don't hate you."
    play music music_friendship fadein 3.0
    show shizu behind_blank with charachange

    "Talking to Shizune with my voice is strange. It's an unfamiliar sensation."
    $renpy.music.set_volume(1.0, 0.0, channel='ambient')
    #WTF is with this track? Was it the "we need different music for this, so here's a placeholder" track? -md01
    #play music music_cellosolo fadein 0.2
    
    #play music music_friendship fadein 1.0

    ssh "You don't care that I lied?"

    "It's not that I don't care. It's just that there is no way to fully adjust to learning something like this. I would need more time. Time to sort it all out. Time I don't have right now, with her looking expectantly at me, trying to read my expression."

    "Were you just too deep in the lie that you thought you could never tell the truth?"

    "And are you that sick of yourself now that you can tell me?"

    "Do you want me to hate you?"

    "I hate it when I have to look so deeply into Shizune's every action. I'm not a mind reader, and sometimes, I think that she wants me to struggle to find out what she's thinking. It's always been that way, hasn't it? Just sometimes more than others."

    "But, at least you told me."

    hi "Hey, are you going to be honest with me from now on? I really like you, even despite all of this. Because of that, I don't like seeing you like this."

    hi "Weren't you supposed to be someone who would become a productive member of society? You said that, didn't you? If it's true, then stop acting like this. I'm pretty sure she wouldn't want you to dwell on this forever, too."

    hi "There was no way that you could have known all of this stuff. Now it's too late, but that's no excuse to… punish yourself like this. Is that what this is?"

    hi "If that is how you see it, then, yeah. I don't care if you lied to me."

    hi "Now, you can understand me, can't you? That's good. I can talk to you like I've always wanted to."

    hi "Okay?"
    
    show shizu basic_normal2
    with charachange

    "She doesn't look convinced."

    hi "The reason I learned sign language is because I wanted to talk to you. Now I can. And it wasn't a waste of my time. I still need it to understand you. And it'll look good on my college application."

    "I smile, hoping she'll return it."
    
    show shizu basic_angry with charachange

    "Shizune looks down at her hands, twisting her fingers around each other before she replies."
    
    ssh "You're too understanding."

    hi "It's because I like you."
    
    show shizu behind_frustrated
    with charachange

    ssh "Don't be an idiot. Please leave."

    hi "No."
    
    show shizu cross_angry_close with characlose

    "Shizune pulls herself up and starts walking towards me. Does she plan to push me out the door?"

    "I stand my ground, and she continues to walk into me."
    
    
    show shizu behind_sad_close with charachange
    play sound sfx_pillow
    with vpunch

    "She stops and presses her head against my chest, as if she's too tired to lift it again. For a second, I'm afraid she'll fall, but she grabs my shoulders and presses herself against me. Her tears are soaking into my shirt."

    "I hug her back."

    "This is the first time that you have ever leaned on me. That means that there is a pretty big responsibility on my shoulders now, doesn't it?"

    "It hurts that you lied to me. I'm not going to do anything stupid because of it, though. I'm… your support now, right?"

    "And you're also supporting me."

    "I'm fine with this."

    stop music fadeout 5.0
    "I've always met your expectations before, right? This time, I'll exceed them again."
    window hide dissolve
    #I don't dislike this fade to white but it's too long and makes it seem the game has ended (?), fade to white is used in very very very few instances, let alone one as long as this one - Kelper. 
    #scene white with Dissolve(5.0)
    scene black with Dissolve(1.5)
    
    #Great scene all in all, really - Kelper
    return

label en_S33:

    #After this, path splits into good and bad ends
    
    #Lets try some stuff - Kelper
    #scene bg school_dormhisao with Dissolve(2.0)
    scene black with dissolve
    #window show dissolve

    #This wasn't originally part of the NVL. I'm gonna take Alphabro's advice and use NVL as a direction tool. - Kelper
    #"I have time now to think about yesterday."
    
    play music music_rain fadein 1.5
    
    #window hide dissolve
    
    nvl show dissolve

    n "I have time now to think about yesterday."
    
    n "In front of Shizune, I was able to put on a brave face, and support her. Now that I'm by myself, though, I can't stop thinking about the things she told me."

    n "Even though she deceived me, I can't bring myself to feel angry at her."

    n "You really strung me along, waiting for me to ask you out first."

    n "Even if you did, I think I always had a feeling that was the case. In fact, when Misha asked me if I liked you or not, I had a feeling that you had put her up to it. That kind of behavior isn't unique to just you."

    n "Maybe those weren't the exact circumstances, but I had always thought that it was a possibility in the back of my mind. So, I'm not really surprised."

    n "As for that other thing…"

    nvl clear

    n "I wonder how long you have been pretending that you aren't able to read lips."

    n "That, too, was something I had suspected a few times, when I noticed your expression change just slightly, reacting to things you couldn't possibly have heard."

    n "Hey… Once, you even told me to shut up. I really should have known."

    n "…"

    # 1) If you cheated on Shizune with Misha, this should appear

    if seen_scene("S25h"):

        n "I cheated on you, anyway. With that being the case, I wonder if I could ever muster up the will to resent you, as if to say your lie was worse."

    # end detour

    n "Even now, I can't shake the feelings of depression that has hung over me since Misha's accident. It's made worse by the fact that I've been reading her journals since yesterday."

    n "I'm a pretty quick reader. I'm already up to the parts of her life that I was there to experience with her."
    
    nvl hide dissolve
    nvl clear
    
    #window hide

    play sound sfx_rustling
    $fixedwritten_note("Today, a new student came to school. His name is Hisao Nakai. I'm going to call him Hicchan~! It's more cheerful if everyone has a nickname.")

    play sound sfx_rustling
    $fixedwritten_note("Shicchan, I'll do my best so you and Hicchan can be together. Anything less would be really selfish. It's more important for Hicchan and Shicchan to be happy than for me to be happy. If my friends are happy, I'll be happy too.")

    play sound sfx_rustling
    $fixedwritten_note("I don't care if Hicchan replaces me in Shicchan's heart. It might be that there was never a place for me there in the first place.")
    
    nvl show dissolve

    n "Did Shizune manage to read this far?"

    n "Here's another reason why you should respect the belongings of the dead."

    n "I said some harsh things when confronted with the possibility of the accident… having not been an accident."

    n "I didn't want to acknowledge the alternative. I still don't. But the more I read, the more that doubt grows in my mind."

    n "Was I wrong?"

    n "I miss you, Misha. I don't know what to do, or even what to think. And, because you left, Shizune has been different ever since. She blames herself. She hates herself. So, maybe she thinks that it was a suicide."

    n "If it was then why couldn't I see it earlier? She was pretty depressed. I should have thought about it."

    n "You seemed so happy, though."

    n "Right now, I hate every thought going through my mind. I wish I could just stop thinking for a while. Just for a short while. No matter how hard I wish for it, the reprieve never comes."

    n "Maybe I should take a walk and get some fresh air to clear my head."
    
    nvl hide Dissolve(1.5)
    
    #I think this looks better now. The black background gives the scene.. something. What do you think? - Kelper
    
    scene bg school_gardens3 with Dissolve(2.0)
    with Pause(1.0)
    #Originally written like this -md01
    #"I head outside and start walking around the school perimeter, with no real place to go in mind. Circling around once, I stop at the front gate. I could always go to town, but I feel apprehensive about the idea somehow."

    window show dissolve
    "I head outside and start walking around the school perimeter, with no real place to go in mind."
    
    scene bg school_gate with locationchange
    
    "Circling around once, I stop at the front gate. I could always go to town, but I feel apprehensive about the idea somehow."

    "It's too lively today, maybe…"

    "I need some place quiet, so I can just think."
    
    scene bg school_lobby with locationskip

    "The most deserted place on a school campus during the summer break is the school itself."

    "I walk through the doors and start roaming through the empty hallways, but it quickly becomes obvious to me that coming here was a mistake. Every door is locked, including the door to the student council room, which is the first one I check."
    
    stop music fadeout 5.0
    
    #Lets see what the night filter does to make the library look dark, but with some sunlight -md01
    #Tested. Night filter looks like crap. I guess I'll stick with the normal library pics for now. -md01
    #Thank god for Sapiens. - Kelper
    
    $renpy.music.set_volume(0.2, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 0.5 
    scene bg school_librarynolights with shorttimeskipsilent
    #Clock sound annoyed me - Kelper
    
    "The only place I find open is the library."

    "I start walking amongst the bookshelves, almost tripping once or twice on piles of books scattered here and there. Weird how messy it is today."
    
    $ renpy.music.set_volume(0.2, 0.0, channel='sound') 
    play sound sfx_footsteps_hard
    with Pause(2.2)
    #If you do this, then the lower volume doesn't work - Kelper
    #$ renpy.music.set_volume(1.0, 0.0, channel='sound') 
    
    show yuuko smile_down_nl with charaenter
    
    #I'm never good with song choices. How does this sound to you?. I thought it needed something not too overly dramatic. Nocturne is always my to-go song. - Kelper
    play music music_night fadein 1.0
    stop ambient fadeout 3.5
    "Hearing footsteps behind me, I turn around and see Yuuko staring at me."
    
    yu "Welcome!{w=0.2} …To the{w=0.3}{nw}"
    $ renpy.transition (charachange, layer='master')
    show yuuko panic_down_nl
    extend "… library?{w=0.2}{nw}"
    $ renpy.transition (charachange, layer='master')
    show yuuko panic_up_nl
    extend " Oh, it's you."
    #I like that little effect. Text tags are pretty useful - Kelper
        
    $ renpy.music.set_volume(1.0, 0.0, channel='sound') 
    
    yu "I'm sorry. Really sorry about that. Hello, Hisao."

    "Did she mix up her jobs just now? That almost cheers me up a little."

    hi "Hi, Yuuko. What are you doing here?"
    
    show yuuko worried_down_nl with charachange

    yu "I'm the librarian?"
    
    "Yuuko tenses up, having a very visceral reaction."

    show yuuko neurotic_up_nl with charachange
    yu "…Am I no longer the librarian? I… I need this job."

    #Can i chalk up for the light in bg school_library as being natural sunlight? I don't think Hisao would have mentioned the lights if it wasn't dark in there.
    #Maybe I'll get an anon to photoshop a picture of the library with the lights off, but with the sun coming in? -md01
    #Meh. Changed the line because fuck the lights. They're not important. -md01
    hi "I know, it's just that all the lights are off, and the place seemed empty."
    
    #hi "I know, it's just that it's the middle of the summer, and the place seemed empty."
    
    show yuuko worried_up_nl with charachange
    
    #play music music_kenji fadein 1.0
    #Kenji music doesn't belong here. I know, I know. But still. - Kelper
    
    yu "Um, it's actually… complicated. Someone has been stealing a lot of books from here, and I was okay with it when they were stealing books that we had more than 3 copies of, but…"

    yu "Lately whoever it is has gotten bolder, and, ah, um… stealing books… only one copy of them. I wanted to read some of them… it's… So now, it's personal."

    hi "I see."

    yu "I won't leave until I catch them."
    
    #This doesn't look good to me. - Kelper
    #show yuuko neurotic_down_nl with charachange

    "Her face reddens upon spilling all this out to me, and I have to check myself to make sure I'm not making a facial expression that she could take the wrong way. If she thinks I'm mocking her, then she might sulk."
    
    show yuuko neutral_down_nl with charachange

    yu "What are you doing here, Hisao?"

    hi "I just wanted to get my mind off things."
    
    show yuuko worried_down_nl with charachange
    
    #stop music fadeout 2.0

    yu "Oh."

    "From the look on her face, I think she knows what I want to get off my mind."

    "Yuuko was one of the few people who attended the funeral. If she wasn't, I think I would have trouble talking to her as freely as I'm doing right now. Kind of a weird thing to share a bond over…"
    
    #No, wait. Too dramatic - Kelper
    #play music music_sadness fadein 1.0

    hi "Yeah. It's not just about Misha, though. I'm worried about Shizune."

    hi "She seems kind of sick lately."
    
    show yuuko worried_up_nl
    with charachange

    yu "Because of…?"

    hi "Yeah. It's pretty obvious that it's because of that. I don't know what she might do. I mean, how she is going to react. I think I was never ready to imagine Shizune being so depressed."

    hi "I can understand this, though. This is really something that isn't… This is not simple."

    #She is later said to be smiling. - Kelper
    show yuuko neutral_up_nl with charachange 
    
    yu "Of course not."

    "Her voice is so quiet I almost can't hear it. It's awkward, this conversation, and more than just a little. Tiptoeing around Misha's name like this only accentuates the fact that she's gone. That isn't what I came here for."

    "A thought came to me yesterday, after I was done talking to Shizune, and I don't want to revisit it."

    "Shizune."

    "I have never felt so lost in my life."

    hi "Hey, Yuuko."
    
label en_choiceS33a:
    menu:
        with menueffect
 
        hi "Shizune…"
 
        "Tell Yuuko about Shizune's ability to lip read.":
            return m1
           
        "Don't tell her.":
            return m2

    #UNUSED TEXT FOR A CHOICE I DELETED
    #IT'S JUST BEEN REVOKED! -md01

    label en_S33a:    
    
    "I guess I could tell her."

    hi "I'm glad that you're my friend. I'm glad to hear that. More importantly right now, though… You're Shizune's friend, too, right?"
    
    show yuuko worried_down_nl
    with charachange

    "Yuuko looks puzzled."

    hi "Sorry. It's just that I had to try hard to convince Shizune that I don't hate her. But I'm not sure if it really worked. I'm not sure if she has the faith in me I wish she had. It wasn't a lie, but it doesn't matter if she won't believe it."

    hi "So, she might think I hate her. And I'm worried about what she might do if she thinks that."

    "And what would she do? Anything is possible."

    "It's Shizune, after all."

    hi "I guess what I'm asking is, you're not going to resent her for what I say, right?"

    "Stupid question. Obviously a stupid question. She doesn't even know what I'm going to say, and I don't know how she might react. This isn't exactly a small secret, either."

    "I look at Yuuko more closely."

    "She doesn't answer, but considering her personality, I doubt that she would feel any malice towards Shizune. She might even be understanding."

    hi "Shizune can lip read, it seems."

    "I'm afraid to look at her. Ha, being afraid of Yuuko. It's unimaginable."

    yu "Really…"
    
    show yuuko worried_up_nl
    with charachange
    
    #This line here did not have a character code on it. I can only assume it's said by Yuuko. -md01
    yu "Um… How long has she been able to do that?"

    hi "A while."
    
    show yuuko worried_down_nl
    with charachange

    yu "Oh…"

    #I broke and changed up this line so it'll flow better with direction.
    #I'm also not happy with Yuuko's sprites for this. None of them have a "hysterical laughter" quality to them -md01
    #"I start feeling as though I've made a terrible mistake, until Yuuko breaks out into laughter."
    
    "I start feeling as though I've made a terrible mistake..."
    
    show yuuko closedhappy_up_nl
    with charachange
    
    "...until Yuuko breaks out into laughter."
    
    show yuuko happy_down_nl
    with charachange

    yu "Sorry. I'm sorry. I just remembered that I have said a bunch of things to Shizune because I had to… get them off my chest, and I thought that she can't—um, couldn't—hear me, and I wouldn't have to be embarrassed."
    
    show yuuko neutral_down_nl
    with charachange

    yu "Now, hearing this, I'm remembering it, and it's…"
    
    show yuuko neurotic_up_nl
    with charachange

    "Her face reddens, but she laughs again, partly out of nervousness, but she seems happy as well."
    
    "After a pause, Yuuko adds..."
    
    show yuuko neutral_up_nl
    with charachange

    yu "We should all go somewhere together some time."

    #CHanged and moved this line to before the previous one. -md01
    #"She says, after a pause."

    hi "Yeah."
    
    show yuuko neutral_down_nl
    with charachange

    yu "I am sure Shizune will be okay. If it isn't out of bounds for me to say that."

    yu "What you have just told me just means that you have her trust. Or else you would not know it."

    "Really? The way she looked, it hardly seems as if there was trust motivating her."

    label en_S33b:
    #2) Don't tell her

    "It feels like it would be wrong to divulge something that seemed to tear Shizune apart to tell me."

    "And if Yuuko were to feel any differently about Shizune because of me, I don't think I could live with myself."

    hi "Nevermind."

    show yuuko worried_down_nl with charachange
    
    "Uncertainty tinges her smile."
    
    yu "Okay…."
    
    show yuuko neutral_up_nl
    with charachange
    
    "Yuuko looks down at her lap, composing her thoughts."

    yu "Ah… You and Shizune are a couple, right?"

    hi "Yeah."
    
    show yuuko neutral_nl
    with charachange

    yu "They were always together. Sometimes it was like they were two sides to the same person, I always thought…."

    yu "How she must be feeling is perfectly understandable. I understand."

    hi "It's not that simple."

    hi "She's really stubborn. I guess you know that as well as I do. It's part of why I like her, because it can be cute sometimes. Now, it's an obstacle. I can almost see it. It's like some kind of wall."

    hi "And…"
    
    label en_S33c:
    #UNUSED SCENE SPLIT FROM DELETED CHOICE
    #lolnope - md01

    hi "Do you want to know what I'm afraid of?"
    
    show yuuko panic_down_nl with charachange

    "A momentary flash of fear in Yuuko's eyes tells me that we share the same concern, and also that she doesn't want to go there. Neither do I."
    
    show yuuko worried_down_nl
    with charachange

    "The library is quiet. Disturbingly so. I hear Yuuko sigh after awhile, and it's so loud that it almost startles me."

    hi "I don't know what else I can do for her, other than be there for her."

    hi "Even then, what does that mean? Do I just stand there and talk to her? About what? And, what good is that going to do? I need something more to back it up. Shizune also needs more."

    hi "I think I'm… out of my league on this one."
    
    show yuuko worried_up_nl
    with charachange

    yu "You're not going to give up, are you?"
    
    #stop music fadeout 2.0

    hi "Give up?"

    "Hearing it makes me a little angry."

    hi "No, of course not. I don't know what to do, but I'm not going to just sit back. That isn't what Shizune would do. That isn't what the responsibility of the survivors is. People who are left behind have a duty, too."

    hi "What she is doing now is wrong, and I hate it."

    hi "Misha is gone."
    
    show yuuko panic_up_nl with charachange

    "Yuuko flinches visibly at my words and looks as if she might tear up. In that instant, I almost falter."
    
    show yuuko worried_down_nl
    with charachange

    hi "Just because of that, she shouldn't be acting like this. I'm just afraid that if I tell her that, she'll just throw it back in my face that I'm not qualified to talk to her like that. And, it's true. I'm not."

    hi "…For a while, I thought it would be good to just stop thinking about her, because I didn't want to deal with it. I'm a pretty shoddy friend, huh? Shizune would be right to say a person like that has no right to tell her how she should feel."

    "I feel drained."

    "I wonder if Yuuko hates me right now, but if she does, she is doing a great job of hiding it."
    
    show yuuko happy_down_nl with charachange

    yu "I think… that it's important to cherish special memories."
    
    show yuuko neurotic_up_nl with charachange
    
    yu "And that we all make mistakes. What is important is… um… What we learn from them, and how we deal with them."
    
    "She turns bright red and covers her face with her hands."

    hi "That's such a movie line."
    
    show yuuko worried_up_nl with charachange

    yu "It is? I'm sorry."

    hi "It's a good line."
    
    show yuuko worried_down_nl with charachange

    yu "I… that is actually where I heard it…."

    hi "Heh."

    "But, she has a point."
    
label en_choiceS33b:
menu:
    with menueffect
    
    "Should I go check on Shizune, or let her rest?"
    
    "She needs rest right now, leave her be.":
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        window hide dissolve
        scene black with Dissolve(1.5)
        return m1
        
    "I need to check up on her.":
        stop music fadeout 3.0
        stop ambient fadeout 3.0
        window hide dissolve
        scene black with Dissolve(1.5)
        return m2
    
label en_S34:
    #This scene is hella short. So short the whole thing might as well be in NVL mode.
    #Yeah that's right a scene with absolutely no sprites or anything
    
    scene bg school_dormhisao_blurred
    show phone mobile at center 
    with Dissolve(2.0)
    
    #So, this is a problem. Nocturne fits, but it fits in the other scene too, and I think better. Ill try daylight. - Kelper 
    play music music_pearly fadein 2.0
    
    window show dissolve

    "I get a call from Hideaki at around nine in the morning. It seems like he's back to his usual self, as calm and formal as ever. Our conversation is brief."

    hi "Hello?"

    hh "Hello. Am I speaking with Hisao Nakai?"

    "Too formal. I'm pretty sure he's well aware that he is, and I feel the urge to be a little bit of a smartass."

    hi "Yes. Yes, you are. After all, this is my personal cell phone, genius."

    hh "Am I calling too early?"

    hi "Not really."

    hh "I see. That is good. I'll be coming by in a couple of hours. Exactly two hours. Do you think that you could go with me to visit Shizune again?"

    hh "Our last conversation was not a conversation at all. I have been thinking since then about what I want to say to her, but I'll need your help again, of course. I'm sorry I have to keep bothering you with it. It's my fault for not learning sign language."

    "That's right, even Hideaki doesn't know Shizune can read lips… The level of commitment she put into hiding her ability is really something."

    "It's possible that the only person who knows is me."

    hi "Yeah, of course. Don't worry about it."

    hh "Thank you."

    hh "How is Shizune?"

    "A lot of ways to answer that question come to mind."

    hi "You'll see when you get here."

    hh "Alright, then."

    "He hangs up the phone."
    
    show phone mobile_alpha at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.7) with dissolvecharamove
    with Pause (0.5)
    
    scene bg school_dormhisao with locationchange

    "Two hours? I was actually planning on checking up on Shizune today myself, but now, I might as well wait."

    "It still feels weird, having to be so concerned for Shizune. After all, out of the three of us, she was always the one who seemed to actually have a plan for her life. Of course, unexpected things always happen."

    "She was the kind of person who would have taken those into account anyway."

    "I still don't know what I'm going to do with my life. Neither did Misha. I think I look up to Shizune, because of her assertiveness. Maybe I was always attracted to her and her precise, analytical way of looking at things."

    "But it seems like just as I want to change who I am, Shizune was trying to change who she was as well."

    "Now, with the way things are going, I wonder…"

    "I guess the question is: How easy is it for a person to change, when doing so requires you to change everything?"

    "And am I really accomplishing anything by sitting here thinking about this when there is so much more I should be doing?"

    stop music fadeout 5.0
    
    "Especially now, at this important time."
    
    scene bg school_dormhisao with shorttimeskip

    "I lose track of the passage of time in my thoughts, managing to forget the steady ticking of the clock on my wall. When I notice it again, I see that two hours have passed and then some."

    $ renpy.music.set_volume(0.1, 0.0, channel='sound') 
    play sound sfx_cellphone 
    with Pause(1.0)
    
    "I'm weighing the decision to call Hideaki back when the phone starts ringing in my hand."
    scene bg school_dormhisao_blurred with locationchange
    with Pause(0.5)
    show phone mobile_alpha at Position(ypos=1.1) with None
    show phone mobile at center with dissolvecharamove

    hi "Are you here yet?"
    $ renpy.music.set_volume(1.0, 0.0, channel='sound') 
    
    hh "Actually, no."
    
    play music music_drama fadein 3.0
    "His voice is mechanical and strained."
    
    hh "I went to see Shizune. She is… very sick. I'm at the hospital right now. I'm very sorry about not telling you this until now. I was panicked."

    "Hideaki is very good at keeping calm, but the news hits me with the feeling of a stone dropping into my stomach, and I wonder just how sick Shizune is that she would need to be hospitalized."

    "How was she taken there? If I had looked out my window at any time, it's possible I could have seen her and maybe done something. I don't even want to consider that possibility right now."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient') 
    scene bg school_road with locationchange
    play ambient sfx_running fadein 0.5

    "I'm already running before I realize that I don't know where the hospital in this town is. Or if there are even more than one."
    
    scene bg suburb_roadcenter with locationchange

    #Next sentence originally said "walk around so much" rather than "run". Changed it because it served direction better. Yup. Eat that up, Silentcook. - Kelper

    stop ambient fadeout 6.5
    
    "The few people I can find to ask all have the same problem I do, and I only manage to run around so much before I start feeling out of breath, and I start feeling a dull, stinging pain in my chest pulsing in sync with my heartbeat."

    #stop ambient fadeout 6.5
    
    "It's the final sign telling me to just stop. I don't have my cell phone, and I can see a pay phone, but I don't have any money to use it."

    "I feel like I could throw up."

    "…"
        
    #I added "and find out where the hospital is", to fix a continuity issue. He says he is going back to school and next background you use is a hospital background. - Kelper
    
    "There is nothing for me to do but go back to school and find out where the hospital is."
    
    stop music fadeout 2.5

    #scene border removed
    
    scene bg newhosp_ext with shorttimeskipsilent

    #play ambient sfx_rooftop fadein 0.5
    
    "The hospital where Shizune is staying is almost identical to the one I was in less than a year ago."

    "If anything, it seems even bleaker. I guess hospitals tend to look more depressing when you're healthy and visiting someone who is sick than when you are sick yourself."
    
    scene bg hosp_room3 with locationchange

    $ renpy.music.set_volume(0.4, 0.5, channel='ambient') 
    
    "The room Shizune is staying in is painfully sparse, with nothing adorning the walls but a single overly colorful painting that looks out of place in the barren white room."
    
    #Maybe have some anons photoshop some sprites that would match this description? IDK if it's worth it. -md01
    
    #play sound sfx_rustling 
    show shizu behind_blank_gown with Dissolve(1.0)
    
    #The sprites don't really match this description -md01
    #"Shizune looks pale, but still manages to sit up straight when I enter the room, drawing the shirt of her school uniform like a cloak around her slim shoulders barely covered by a hospital gown."
    
    "Shizune looks pale, but still manages to sit up straight when I enter the room."

    shi "…"

    hi "Hello, Shizune. How are you feeling?"

    "I feel a little sick when I say it, and I'm glad she wasn't able to hear me, because it sounds so hollow that it makes my heart sink."

    "I watch a bead of IV fluid slide down the tube that vanishes behind Shizune, where it is connected to the arm behind her back."
    
    shi "…"
    
    show shizu basic_normal_gown with charachange

    "She raises her hands only inches off her bed, and then lowers them again with a second thought."

    hi "Is there something wrong?"
    #play sound sfx_footsteps_hard
    #with Pause(2.6)
    #play sound sfx_sitting
    #with Pause(1.0)
    
    play music music_tragic fadein 2.0
    
    "When she still doesn't reply, I take a seat in the small chair available to me."

    hi "You can understand me, even if I just talk… It's still kind of a surprise to me. I'm still getting used to it."

    hi "I don't know why you're here, but I guess it's serious. I know how you feel, how you felt about Misha dying. You're sick because of that, aren't you?"

    show shizu behind_blank_gown with charachange
    
    hi "Shizune, you have to stop dwelling on it. She was my friend, and I miss her so much. I keep expecting her to come out and surprise me like always. So, I guess I'm being presumptuous saying I know how you feel. I really can't."

    hi "…But… You have a future. You're still alive. Didn't you always make a point of showing me how much you could overcome? Your whole life is like that, because that is how you deal with literally everything."

    show shizu basic_normal2_gown
    with charachange

    shi "…"

    hi "People who are left behind also have a duty. Do you understand?"
    
    show shizu behind_sad_gown
    with charachange

    shi "…"

    "She still doesn't raise her hands to reply to me. She hasn't signed a single thing to me since I got here."

    hi "Shizune, what are you thinking?"

    "Her eyes are as dark and piercing as ever, but so sad, like dulled jewels."

    hi "Please say something."

    "A feeling of deja-vu. Don't just shut down in front of me. I need more than that. I need you to tell me something, so that I can keep going. So that I know what I'm saying is working."

    "Even if it is false hope, throw me something. Do something more than staring at me."
    
    show shizu behind_frustrated_gown with charachange
    with Pause(0.4)
    
    "I get up, and Shizune seems to misinterpret it as me wanting to leave. Her left hand rises and stretches out towards me, and I stop."

    hi "What is it?"

    "Her mouth opens slightly, as if to speak, but nothing comes out."
    
    #play sound sfx_rustling
    show shizu behind_sad_gown at centersit with dissolvecharamove

    "Just doing that seems to wear her out, and Shizune lies down again, her head sinking into her pillow."

    "What are you thinking? And why do you keep reaching out to me like that, preventing me from leaving, if you're not going to answer my questions, or tell me anything?."

    "A response, any one, will do. I just want her to say something. Every second that she doesn't, the more I start feeling like it was futile to come here. To have said anything."


    "Shizune is stubborn, even now. Maybe even moreso. If I accomplished anything at all, all it was as strengthening an already immovable will. Shizune, do you want me to live with that kind of guilt?"

    hi "Can I just ask what it is that you want to do? What's your intention?"
    
    show shizu basic_angry_gown at centersit with charachange

    "She shakes her head almost imperceptibly from side to side."

    hi "I…"

    hi "Is this really necessary?"
    
    shi "…"

    hi "Hey,"

    #stop ambient fadeout 2.5
    
    hi "Are you trying to follow Misha?"
    
    shi "…"
            
    $ renpy.transition (Dissolve(0.8), layer='master')
    show shizu behind_blank_gown at centersit
    extend""
    
    hi "Is that really what you want?"
    #play music music_moonlight fadein 6.5    
    hi "This is… the only time you have ever followed anyone. At least, that I've seen."

    hi "Please don't. Did you talk to Hideaki?"
    
    show shizu basic_angry_gown at centersit with charachange

    shi "…"

    hi "He's concerned about you. You can see it, can't you? And Yuuko, as well. And me. I didn't even want to think about it until now that you want to kill yourself."

    show shizu behind_sad_gown at centersit with charachange

    "Shizune's eyes drop down to her lap at my words."

    hi "You're really going to…"

    "If anyone has the will to do something like that, it is her."

    hi "Shizune, do you understand what you are?"

    hi "You're supposed to be Misha's hope. You read her journals. She really loved you. A part of that was because you're so driven, and so intelligent. Now, you're just going to throw that away?"

    hi "She wrote that it's a big world, and it scared her, but she was able to keep going because she knew that the world had amazing people in it. You were one of those people to her. You're supposed to be an amazing person."

    hi "I'm sure that is who you are."

    hi "So this… is depressing."

    shi "…"

    "Can't you see that I just want you to get better? So just give me some kind of sign that my words are getting through."

    "Please."
    
    show shizu behind_smilelow_gown at centersit with Dissolve(1.0)

    "She smiles very sadly."

    hi "I really love you."

    "I try to glean her feelings from the expression on her face, but it's impossible. A person who can hide their ability to lip read for over a decade. That is the kind of person I'm dealing with."

    "I had always thought that at times, I could see Shizune's true feelings behind that calm, oddly striking gaze. If I ever had that ability, it's left me now."

    "I plead with her some more, but it's futile. I try to dry my eyes with a napkin on the table beside me."

    "She continues to smile regretfully, with that horribly obvious fake cheer."

    hi "I don't want to just keep talking to you. Please just say something back."
    
    show shizu basic_normal2_gown at centersit with charachange

    shi "…"  

    "I'm not getting through to her, I guess."

    hi "I'll be back tomorrow."
    
    "As I walk towards the door, her left hand trembles and raises itself just a bit. She extends her pinkie finger."

    "A promise?"
    
    show shizu behind_sad_gown at centersit with Dissolve(0.8)
    with Pause(1.2)
    play sound sfx_pillow 

    "Her hand reaches out to me once more, and then drops. A wave. I wave goodbye to her, too."
    
    window hide dissolve
    
    stop music fadeout 10.0
    
    #I felt like NVL mode was most appropriate for this scene. It was originally written for a normal dialogue box though. -md01
    scene black with Dissolve(5.0)
    
    $ renpy.pause(0.5)
    
    $ renpy.transition(Dissolve(1.5))
    show walivetext "Later, I would find out that she died just a few hours after I left.{fast}"
    $ renpy.pause(3)
    
    $ renpy.transition(Dissolve(1.5))
    hide walivetext
    $ renpy.pause(1.5)    
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    #play ambient sfx_park
    #with Pause(0.5)
    #scene bg city_graveyard with locationchange
    #with Pause(1.0)
    
    nvl show dissolve
    
    n "Afterwards, I would hear that she probably didn't raise her arms to communicate with me because she was too weak from dehydration to do even that."

    n "But, I know that wasn't it."

    n "The reason she didn't raise her arms to answer me was because if she had, even I could have seen the IV tucked into the crease of her elbow that she had pulled out from under her skin."

    n "The reason she wouldn't let me come closer was likely because if I had, I would have noticed the spreading stain of IV fluid wetting the hospital mattress."

    n "How can anyone living in a first world country die of dehydration? You would have to actively try to do it."

    n "Which is exactly what she did…"

    n "I didn't even find out until a full day after, because my cell phone had run out of battery power."

    n "I was late even in receiving this news."

    n "…"
    
    nvl clear

    n "\n\n\n\n\n\nI reacted like anyone else would."

    n "“I'll be back tomorrow?”"

    n "“I'll be back tomorrow?”"

    n "Were these my last words to her?"

    n "I'm so disgusted with myself."
    
    nvl clear

    n "\n\n\nShe passed out of my life too quickly, but… I was powerless the whole time. And I was powerless after. Looking back, I see all the things I could have done, or could have done better."

    n "So, what was stopping me all those times?"

    n "I don't even have the will anymore to do a thing besides look back on the last few months and regret."

    n "I knew them for less than a year. When I look back on it with that in mind, the time we spent together just seems even shorter."

    n "I didn't even want to join the student council at first."

    n "And I took it for granted. I even kind of hated it; Shizune with her ever confident and aggressively playful manner, and Misha's booming laughter and distinct way of speaking."

    n "Both of them are gone now."
    
    nvl clear

    n "\n\n\nMisha, who was always so happy and smiled so brightly. She had wanted to become a sign language teacher."
    
    n "And Shizune, who always faced the world so aggressively and refused to be denied in everything she did."

    n "Their lives could have went somewhere."

    n "I hate myself the most because the last time I looked at Shizune, all I did was wave goodbye."

    n "Her outstretched hand refuses to leave my memory."

    n "Shizune, what did you mean by that? Were you just waving goodbye for the last time?"

    n "What did you want from me?"

    n "Was it that? Or… Did you expect me to grab your hand, and pull you up out of your sadness?"
    
    nvl clear

    n "\n\n\That was probably it. I had made such a big show of wanting to save you, because I thought I could. I assumed that I could pull at your heart, like you did to me, and you would go back to your old self."

    n "As if such a thing is so easy. If you couldn't do it, then what was I trying to accomplish with such a half-assed effort?"

    n "You relied on me."

    n "It was the first time you truly leaned on me."

    n "And I failed."

    n "Is this how you felt when that happened to Misha?"

    n "I'll spend some time thinking about how to make it up to you."
    
    nvl hide Dissolve(2.0)
    nvl clear
    scene black
    with Dissolve(3.0)
        
    $ renpy.pause(0.5)
    
    $ renpy.transition(Dissolve(1.5))
    show walivetext "I go to sleep later that night, and have a dream. . . {fast}"
    $ renpy.pause(3)
    
    $ renpy.transition(Dissolve(1.5))
    hide walivetext
    $ renpy.pause(1.5)
       
    stop ambient fadeout 2.5
    with Pause(3.5)
    return

label en_end_shizunebad:
    # Shizune bad end, after S34
    scene black with dissolve
    centered "~ Shizune bad end ~" with dissolve
    
    return

label en_S36:

    #These last 2 scenes here did not have any music or sound fx originally. -md01
    
    scene bg school_dormhisao_blurred
    show phone mobile at center 
    with Dissolve(3.0)
    
    play music music_pearly fadein 3.0
    
    window show dissolve

    "I get a call from Hideaki at around nine in the morning. It seems like he's back to his usual self, as calm and formal as ever. Our conversation is brief."

    hi "Hello?"

    hh "Hello. Am I speaking with Hisao Nakai?"

    "Too formal. I'm pretty sure he's well aware that he is, and I feel the urge to be a little bit of a smartass."

    hi "Yes. Yes, you are. After all, this is my personal cell phone."

    hh "Am I calling too early?"

    hi "Not really."

    hh "I see. That is good. I'll be coming by in a couple of hours. Exactly two hours. Do you think that you could go with me to visit Shizune again?"

    hh "Our last conversation was not a conversation at all. I have been thinking since then about what I want to say to her, but I'll need your help again, of course. I'm sorry I have to keep bothering you with it. It's my fault for not learning sign language."

    "That's right, even Hideaki doesn't know Shizune can read lips… The level of commitment she put into hiding her ability is really something."

    "It's possible that the only person who knows is me."

    hi "Yeah, of course. Don't worry about it."

    hh "Thank you."

    hh "How is Shizune?"

    "A lot of ways to answer that question come to mind."

    hi "…She's fine."

    hh "Alright, then."
    
    show phone mobile_alpha at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.7) with dissolvecharamove
    with Pause (0.5)
    scene bg school_dormhisao with locationchange

    "He hangs up the phone."

    "Two hours? I was actually planning on checking up on Shizune today myself, but now, I might as well wait."

    "It still feels weird, having to be so concerned for Shizune. After all, out of the three of us, she was always the one who seemed to actually have a plan for her life. Of course, unexpected things always happen."

    "She was the kind of person who would have taken those into account anyway."

    "I still don't know what I'm going to do with my life. Neither did Misha. I think I look up to Shizune, because of her assertiveness. Maybe I was always attracted to her and her precise, analytical way of looking at things."

    "But it seems like just as I want to change who I am, Shizune was trying to change who she was as well."

    "Now, with the way things are going, I wonder…"

    "I guess the question is: How easy is it for a person to change, when doing so requires you to change everything?"

    "And am I really accomplishing anything by sitting here thinking about this when there is so much more I should be doing?"

    "Especially now, at this important time."

    "…"
    
    stop music fadeout 1.0
    
    scene bg school_dormhisao with shorttimeskip

    "I look at the clock. There is still an hour left. Why am I waiting? I could just go to Shizune right now and see how she is doing. Shouldn't I, anyway?"
    
    play music music_innocence fadein 2.0

    "These past few days, all I have done was think: “What more can I do?”"

    "It's only now that I dare to ask myself what I have actually done. The answer is nothing."

    "So after all I told myself I would do to do more for Shizune, I haven't actually done anything at all. I held her, but didn't say anything to lessen her worries. I observed her, but I didn't make any move to ease her troubles."

    "Even though I thought she might do something terrible."

    "I thought that there was the possibility she could kill herself. And Yuuko apparently thought so, too."

    "Sitting here and waiting won't help. If I'm so worried about her, why did I even leave her alone in the first place? That was a mistake. It really was. But, I'm used to a different Shizune. One I never had to worry about."

    "Did I just want to keep believing in that Shizune? The Shizune that could do anything and would not allow herself to be stopped? I can still remember how she looked under the glow of the fireworks all those weeks ago."

    "That's probably when I started to fall in love with her."

    "Did I just think that that aspect of her personality would break through eventually and, while she wouldn't change back overnight, she would rebuild?"

    "I still think about Misha, so if that is really how it is, then I don't know what to think. It seems so wrong. Shizune and Misha were connected by something more than my tie to either of them."

    "That means that Shizune's wound is that much deeper. You can't even compare the two. Why did I put my hope into such a stupid and ridiculous thought?"

    "Then, I remember something Misha said to me a long time ago."
    
    #I know there is a flashback filter in the final, but I can't be bothered to port it over for one line of text -md01
    #Nevermind, I ported it over anyway -md01
    
    scene bg shizu_guestbed_fb
    show misha sign_sad_cas_fb
    show noiseoverlay
    with flashback

    mi "So… Please be a good replacement for me, Hicchan."
    
    scene bg school_dormhisao
    with flashback

    "It's funny, the things you remember sometimes. Misha, I have been doing a really terrible job of that."

    "I put on my jacket and head over to Shizune's dorm."

    #some transition
    
    stop music fadeout 2.0
    
    scene bg school_girlsdormhall with locationskip
    
    #Changed this line so it'll flow better with the scene direction
    #"When I get to the door, I turn the knob to find it open again. It looks like I've caught Shizune just as she is getting out of bed. When she sees me, she tries to stand up, and then collapses."
    
    "When I get to the door, I turn the knob to find it open again."
    
    
    play sound sfx_dooropen
    
    $ renpy.pause(0.5)
    
    scene bg school_dormshizune
    show shizu basic_normal
    with locationchange
    
    show shizu adjust_blush
    with Dissolve(0.2)
    
    show shizu adjust_blush at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.9) with ease_accel
    play sound sfx_impact
    with vpunch
    
    "It looks like I've caught Shizune just as she is getting out of bed. When she sees me, she tries to stand up, and then collapses."
    
    show shizu basic_frown
    with charachange

    "I run over and try to help her up, but she pushes me away with one hand and, bracing herself against her bed with the other, pulls herself up and back onto the bed."
    
    show shizu basic_frown at center
    with charamove

    "My first instinct is to ask her what's wrong. As soon as I open my mouth, Shizune closes her eyes and decisively shakes her head from side to side, pre-emptively refusing to acknowledge anything like it."

    "I ask anyway. Maybe it's only because she looks so sickly and weak that she answers me."
    
    show shizu basic_normal with charachange

    ssh "I haven't been eating recently. I'm tired."

    "That's…"

    "You don't skip a couple of meals every few days and then collapse like that."
    
    play music music_drama fadein 1.0

    "There isn't even the shred of a doubt to cling onto now. Misha's death wasn't an accident. I was wrong about that, and even now, it hurts to think about. Now, it seems like Shizune wants to kill herself."

    "I'd rather fade away from your life after graduation than lose you like this."
    
    #Has in this sentence was "as"
    "You're precious to me even if our time together so far has been brief."

    hi "I've heard that sometimes something like this can happen. Someone kills themselves and then it saddens someone else they knew enough so that they kill themselves too. And it might go on from there."

    hi "Is that it, here?"

    "She refuses to answer me."
    
    show shizu basic_angry with charachange

    ssh "What are you saying?"

    hi "I'm saying that you couldn't starve yourself here unless you were to try."

    show shizu behind_blank
    with charachange

    shi "…"

    "And that's it, isn't it? You're trying to starve yourself to death? That must take tremendous willpower, which is exactly what she has."

    hi "Shizune, look at me."
    
    show shizu behind_blank_close
    with characlose

    "I grab her by the shoulders and am surprised at how fragile she feels."

    hi "The things that we do affect everyone around us."

    hi "You're so stubborn. It's a good thing, at times, but is this really what you want to apply it to? This is not atoning!"
    
    show shizu basic_normal2_close
    with charachange

    "Damn it, stop turning away from me!"

    "If I were to say right now that I need you, would that be selfish?"

    hi "Shizune, I'm finally able to understand how you think."

    hi "No matter what I say, if it's not good enough to really move you, you just won't even bother to respond. After all, you said that is the only benefit to sign language: That you can fully think out what you want to say before you say it."
    
    show shizu behind_smilelow_close
    with charachange

    shi "…"

    "She smiles softly and nods her head up and down, wavering between happiness that I get it, and regret that it had to go this far before we could finally understand each other."

    hi "Is this really what you want?"

    "Shizune nods again."
    
    show shizu behind_sad_close with charachange

    ssh "Do you hate me?"

    hi "No. I don't hate you."

    ssh "You should."

    "I know. I know you want me to hate you."

    hi "Is that also something you want?"

    "She nods again."

    hi "Well… I don't believe it."

    hi "Because this isn't really what you want, isn't it? If you didn't, you would have locked the door… and you would have found a faster way to do it. It's just how you are. You're cautious, and you never do anything without a reason, right?"

    hi "Even this. Even something like this."

    shi "…"

    hi "I'm not going to hate you, Shizune. You relied on me for something for the first time. How am I going to hate you when you rely on me?"

    hi "You live your life with no regrets. I admire that about you. Is that why you want me to hate you? Am I your last regret?"
    
    show shizu basic_normal2_close
    with charachange

    ssh "Yes. You're right… About everything. Maybe you're right about everything…"
    
    show shizu behind_frown_close
    with charachange

    ssh "Congratulations."

    hi "Don't say that, this isn't a game, Shizune. That isn't even how you really feel. Stop it."

    ssh "That's right."
      
    show shizu behind_blank with charadistant

    "She allows her body to drop backwards, until only the headboard of her bed behind her is holding her up."
    
    show shizu basic_normal2
    with charachange

    ssh "What am I supposed to do?"

    ssh "How am I supposed to feel?"

    hi "I don't know, but this is the wrong way to handle it. This is a really terrible way to atone for anything. Misha wouldn't want it. The people who are left behind when someone dies have a duty to keep living their lives, or maybe even try harder."

    hi "I thought that you would get that more than anyone."
    
    show shizu behind_sad
    with charachange

    ssh "Everything is my fault."

    hi "It's not!"

    "I shout it a little too passionately and wince."

    hi "It's not. You've read Misha's journals. Don't talk like that. It's not."

    hi "And even if it were, what would this accomplish? It's not going to “even out” anything. What's done is done."

    hi "Everyone makes mistakes. The important thing is how we react to our mistakes, and what we learn from them, and how we use them to grow."

    "I smile to myself. Thanks, Yuuko."

    hi "It was my mistake leaving you alone when I knew that this might have been what you were thinking. I worried about it and I didn't do anything about it. That's why I came here today."

    hi "Because I really hate myself."
    
    show shizu basic_angry with charachange

    ssh "Me too."

    shi "…"
    
    show shizu behind_sad with charachange

    ssh "I'm sorry."

    "It's possible that it's only because I'm hoping for it, but I get the feeling that maybe everything now will be okay. That things have at the very least taken a step in that direction."

    "I can believe in it because I know that Shizune, if anyone, has the will to change."
    
    stop music fadeout 5.0
    
    show shizu behind_blank with charachange

    "Her hand brushes against mine, Shizune's delicate fingers gliding softly across my knuckles, tapping and caressing them."
    
    hi "I love you."

    # Removed split
    #STOP RIGHT THERE CRIMINAL SCUM! This split is going back in. -md01

    label en_S36a:

    #1) If you had sex with Misha way back in S25 and.or said you liked her over Shizune in S14:
    #Silly delta, it's S25h and S14b. Get yo shit together - md01

    hi "There were times when I thought that I liked Misha more than you. In the end, I was always in love with you. Your words coming out of her."
    
    show shizu behind_smile
    with charachange

    ssh "In the beginning, I wondered if I could make your heart waver."

    hi "Heh, that's an interesting choice of words."

    "Is that all that you wanted?"

    #END OF REMOVED TEXT (I HOPE)

    label en_S36b:

    #2) If you did not:

    hi "I have since that night at the festival."

    hi "I thought; “You're really amazing, Shizune.” Even here, in this tiny town, where I thought I was just being sent because I didn't have a future, where nobody here had a future, you were there. I was able to believe."

    hi "Misha wrote that the world is bigger than she had thought. It scared her. She was able to keep going because she knew there were amazing people in it like you."

    "Shizune, do you understand now?"

    hi "So… Please continue living."
    
    label en_S36c:

    #end split
    
    show shizu behind_blank_close with characlose
    
    play music music_comfort fadein 3.0

    "She draws herself closer to me, and doesn't let go for a long time."

    "Only now am I able to appreciate it all. The things I gained this year, and the things I've lost."

    "I pull away from her so I can look into her eyes as I speak to her."

    hi "I'll keep trying to exceed your expectations. I love you. Even though you're always playing with me. I'll play with you. Always."

    hi "Because I love you."
    
    show shizu behind_smile_close with charachange

    "Finally, I was able to say it."
    
    ssh "I love you."

    "Her eyes are so beautiful. Shizune's eyelids close over them peacefully and she wraps her arms around me again."
    
    show shizu behind_smile with charadistant
    hide shizu with charaexit

    "She's still tired, and lets go of me to lie down."

    "Eventually, she falls asleep. I sit beside her until there is a knock at the door, which I notice is still hanging open from earlier. It seems like Hideaki is here."

    "A lot can happen in an hour, I guess."

    "Shizune, when you feel better, when this is all over, I wonder how our lives will move on. I wonder how they might diverge."

    "I still have some months to use for thinking about the future."
    
    stop music fadeout 3.0
    
    #This feels like it should have been the end of a scene, but it's not apparently. Added in these transitions to make it feel more like that.
    
    window hide dissolve
    scene black with fade

label en_S37:

    window show dissolve
    
    scene bg school_girlsdormhall
    with locationchange
    
    "I continue to visit Shizune every day, and every time I see her, she seems to regain a little more of her color and her strength."
    
    play sound sfx_dooropen
    
    $ renpy.pause(0.5)
    
    scene bg school_dormshizune
    show shizu behind_smile 
    with locationchange
    
    "I open the door to her room and this time find her standing there, as if she had been waiting for me."

    play music music_another fadein 0.2
    
    ssh "Good morning."
    
    hi "Morning. You're up early."
    
    show shizu adjust_happy with charachange
    
    ssh "Is that right? You are all dressed up nicely today, which means you were up even earlier than I was, to shower, get dressed, and then come over here. Who's up early now?"
    
    hi "Still you."
    
    "I still haven't gotten completely used to talking to Shizune normally, and find myself signing parts of my responses unconsciously. Once it becomes a habit it's hard to break, apparently."
    
    "Her teasingly combative manner is back, and I'm happy to see it return. Mostly happy."
    
    hi "Hey, you're dressed up, too."
    
    show shizu behind_smile with charachange
    
    ssh "I know. I was thinking about taking a walk."
    
    "It's only now that it hits me that Shizune probably hasn't left the dorms in over two weeks, and now that she is healthier, it's starting to bother her to the point where she feels restless enough to want to take a walk just for the sake of taking one."
    
    hi "Really? I guess since I'm here, I'll go with you."
    
    show shizu adjust_smug with charachange
    
    ssh "We can race, and I'll win."
    
    hi "Who knows. Maybe I'll surprise you."
    
    "I start feeling a strange sense of deja vu, as if I've said those words before."
    
    "It's funny, Shizune, but the entire time I've known you, I think I've been trying to think of how I could surprise you. I wanted to. I never stopped to wonder why, and I don't think that before today I could have explained it to myself if I did."
    
    "And I've always wanted to compete with you, but I never thought I would be able to."
    
    "Was I able to surprise you in the end? I'll do it again."
    
    show shizu adjust_smug
    with charachange
    
    show shizu basic_sparkle
    with charachange
    
    hide shizu
    with charaexit
    
    "Shizune smiles and starts to sign something, but then stops herself, and lets her hands fall to her sides as she shrugs and then moves behind me, holding the door open for me and beckoning with her free hand for me to step outside."
    
    scene bg school_gardens with locationskip
    
    "We start walking around the school. The early morning air is crisp and cool, easily one of the things I like best about this school. Wandering aimlessly from location to location, I can see Shizune's gaze consistently going towards the main building."
    
    scene bg school_courtyard_ss with locationskip
    
    "In the end, we wind up in front of it, the last destination on the list. Shizune steps inside and instantly heads to the student council room, as expected."

    stop music fadeout 7.0
    
    scene bg school_council_ss
    show shizu basic_normal2_ss
    with locationchange
    
    #show shizu basic_normal2_ss at Position(ypos=1.1) with charamove
    
    "Unlocking the door with her wrongfully gained copy of the keys, she steps inside and takes a seat on the closest desk to her, seeming to get lost in the ambiance of the room, staring at the orange-tinted sunlight drifting through the windows." #This line originally mentioned the blinds being closed. -md01
    
    ssh "This place has a lot of memories."
    
    hi "Yeah…"
    
    show shizu behind_smilelow_ss
    with charachange
    
    ssh "The three of us spent a lot of time here. But, not enough time, maybe."
    
    "She pauses, taking a minute to clean her fingernails thoughtfully."
    
    show shizu adjust_frown_ss with charachange
    
    ssh "In the beginning, it was just me here, alone. Even when we had other members, for the two days or so that they stuck around, it was all because of Misha."
    
    #Not sure what's going on here. The bit up there just ends and I have no idea what to do with it. It feels like she should go on a bit of a rant, but then Hisao just interupts her. -md01

    #Perhaps the rant would have had something to do with how deceitful she was/is? The bit about her not needing the glasses makes me think so.
    
    hi "…I think you can be cute, too. Like when you adjust your glasses."
    
    show shizu adjust_blush_ss with charachange
    
    shi "?"
    
    "She pushes them up, but more carefully this time, like there is more thought behind the action than usual."
    
    show shizu basic_normal2_ss with charachange
    
    #I changed the commented out line here because the ending bracket spilled over into the next line and it drove my OCD nucking futs. -md01
    #ssh "Even this, I don't really have to do it. My vision isn't that bad. It's mostly because…"
    
    ssh "Even this, I don't really have to wear them. My vision isn't that bad. It's mostly because…"
    
    ssh "It's noticeable. That is all."
    
    "Everything you do… is so carefully calculated."
    
    hi "Then, I wonder if you're cuter without your glasses on."
    
    show shizu adjust_blush_ss with charachange
    
    ssh "Really?"
    
    #I felt these next 2 lines didn't need to be here. They felt awkward. -md01
    
    #hi "Maybe you would be cuter without your glasses."
    
    #shi "…"
    
    "It feels different in here all of a sudden. The mood has changed."
    
    show shizu adjust_noglasses_ss with charachange
    
    ssh "Do you think I'm cuter without my glasses?"
    
    hi "No. I think you're cuter with them on."
    
    show shizu adjust_frown_ss with charachange
    
    shi "…"
    
    #scene white with whiteout
    
    #There are nude Shizune sprites in the final that might be useful here. I'd have to change some dialoge, or get someone to photoshop some stuff, but it could work. -md01
    
    show shizu basic_normal_ss
    with charachange
    
    "Breathing deeply but slowly, she undoes the buttons of her blouse and slides it off herself, shedding it effortlessly but taking care to put it on the back of a nearby chair so it won't get wrinkled."

    play music music_one fadein 5.0
    
    show shizu behind_blank_bra_ss
    with Dissolve(0.8)
    
    shi "…"
    
    ssh "…Do I look okay?"
    
    hi "You look great."
    
    shi "…"
    
    scene white with whiteout
    
    "Blushing, she starts moving closer to me, and she takes my hands in hers. Without warning, she twists them behind my back, and her right hand starts snaking towards my groin, tapping the buckle of my belt lightly along the way."
    
    "I find my breath catching in my throat when I feel her fingers caressing me through the fabric of my pants, which elicits a muted, breathy giggle from her that sounds like a breeze blowing over tall grass."
    
    "Shizune's hand continues to prod playfully at my crotch as she moves the rest of her body closer and closer, standing on the tips of her toes so that we are level with each other."
    
    "Her heavy chest heaves against mine, and her other arm is still holding my arms back, twisting them into a shape like a pretzel each time I try to break free, managing to summon up less resistance with each successive attempt."
    
    "I start to feel heat rising up the back of my neck. As if stoking the fire, Shizune brushes her cheek against mine and breathes softly down my collar, our necks intertwined."
    
    "Lowering herself so that her feet are flat on the ground again, she starts slowly pulling my necktie loose with her teeth, while continuing to push me backwards."
    
    "Eventually, I feel the hard edge of a table hit the back of my legs, and I try to keep myself from falling over, but a quick glance at Shizune's face tells me this is exactly what she wanted. With a quick push, she sends me over it."
    
    "It's the same spacious table we used to sit at months ago doing student council work."
    
    "My arms are still pinned behind my back, with Shizune on top of me."
    
    "This isn't like last time. If I speak, I know she'll be able to understand, but I'm at a loss for words right now. Just to be safe, she kisses me, as if she's afraid I'll say something and disrupt her momentum, but I would be crazy to ruin this moment."
    
    "She suddenly pulls back, pushing her glasses back up the bridge of her nose, trying to look as collected and mature as possible even though she is blushing and there is sweat breaking on her face. The sight makes me smile."
    
    ssh "What's so funny?"
    
    "Shizune starts smiling as well but it seems she can't resist pursuing it."
    
    ssh "I should just stop now, and let you simmer in your lust."
    
label en_S37h:
    
    "Signing that, she undoes her brassiere and lowers herself back onto my chest, gravity pulling her bare breasts out and onto my chest, where they spill across my shirt, separated from me only by a single thin layer of clothing."
    
    "Shizune undoes my belt and starts taking off my pants and underwear, a squeal of surprise escaping her lips when my erection shoots up and hits her hand. The sound is so unguarded and unlike Shizune that it makes me even more excited."
    
    "In one smooth maneuver, she takes off her own skirt and panties, slipping them past her legs and into a neat pile on the floor."
    
    "Inching her way across the table until her knees are touching my elbows, Shizune starts teasing herself with one hand as the other strokes my cock daintily, taking time to trace along each curve and vein as if she is mapping the surface."
    
    "Seeming to sense my anticipation, she lowers herself onto me slowly, her face growing redder by the minute as I am enveloped by the hot, moist contours of her vagina."
    
    "Eventually, she stops once my dick reaches the barrier of her hymen, and then she plunges down on it quickly, drawing herself right up against me simultaneously, muffling a grunt of discomfort by rubbing her head against the V of my neck."
    
    shi "!!"
    
    #I cut up this line because it overflowed out of the textbox -md01
    #"I thrust my hips towards her at the sudden sensation of movement, and Shizune fights against me, trying to pin me back down when I manage to pull my arms out from under me in that moment, her hips thrusting back with even greater force in response."
    
    "I thrust my hips towards her at the sudden sensation of movement, and Shizune fights against me, trying to pin me back down when I manage to pull my arms out from under me." 
    
    "She thrusts her hips back with even greater force in response."
    
    "The table under us rattles under our combined weight, which drives Shizune to start going faster, her breasts compressed tightly between our bodies, hard nipples rubbing noticibly through my shirt, while her lower half bobs up and down on my penis."
    
    #Had to cut up this line too. -md01
    #"I feel like I'm about to blank out from the pleasure as Shizune's canal clamps down tighter and tighter on my rod with each passing second, seeming to undulate as she grinds her crotch against mine harder with each thrust, slowing down only to catch her breath before resuming with double the force."
    
    "I feel like I'm about to blank out from the pleasure as Shizune's canal clamps down tighter and tighter on my rod with each passing second, seeming to undulate as she grinds her crotch against mine harder with each thrust." 
    
    "She slows down only to catch her breath before resuming with double the force."
    
    "Her breathing turns to panting and I feel her tongue lick the side of my cheek; a misaimed kiss, maybe, but I'm afraid to kiss her back because with her enthusiasm we may bump our heads together."
    
    hi "Shizune…"
    
    shi "…nn…"
    
    "An almost inaudible little moan pierces what is for the most part a thick silence, and Shizune starts pistoning her nether regions quickly, nearing her limits and seeming to want to bring it to an end for both of us with that knowledge in mind."
    
    shi "…hhh…. mm…"
    
    "The noises coming from her are like whispers, and would be lost to me if she weren't so close at times that she were letting them out almost right next to my ear, her soft lips and tongue swirling around it while her hips start going faster and faster."
    
    "My hands now free as Shizune's are busy supporting herself, I reach up to grab Shizune."
    
    "Shaking her head, she pushes my arms against the table roughly, managing to get out a noise of disapproval in between gasps. Then, she touches her palms to mine and her fingers lock around my hands, intertwining."
    
    "I can feel myself about to reach the end of my rope and my hips buckle against hers, and Shizune lets out a moan that she quickly tries to stifle as she reaches climax, tightening around my shaft until I shoot my load deep into her."
    
    "Spent of all her energy, Shizune collapses on top of me, chest heaving with deep breaths. My own head is swimming as I pull out of her, and I barely manage to pick it up for a second before it falls back against the table."
    
    #This line too. -md01
    #"The sound of Shizune's contented breathing and the feel of her plentiful breasts moving back and forth across my chest with each sigh grow more arousing with time in the stillness of the student council room, and my erection comes back, slowly growing back to full size between Shizune's inner thighs."

    "The sound of Shizune's contented breathing and the feel of her plentiful breasts moving back and forth across my chest with each sigh grows more arousing with time in the stillness of the student council room."
    
    "My erection comes back, slowly growing back to full size between Shizune's inner thighs."
    
    scene bg school_council_ss
    show shizu behind_blank_nak_ss
    with fade
    
    "Shizune pulls herself off me, letting go of my hands to bring them back up in front of her."
    
    show shizu behind_smile_nak_ss
    with charachange
    
    ssh "You're still excited?"
    
    ssh "Do you want to go again?"
    
    "I pick myself up until I'm sitting upright on the edge of the table, feeling a bit silly in my state of undress."
    
    ssh "It's about give and take."
    
    "Our hands come together again. Is she asking me to take the initiative this time? A part of me wonders if there is more to this than it appears. Is this another test, or something?"
    
    "The way she leans on me, her fingers linking around mine, give me a feeling like as if she were passing a baton to me in a relay race, her touch warm and gentle as she pushes and pulls at my hands trustingly, reluctant to let go."
    
    scene white with whiteout
    
    "Standing up, I move myself behind Shizune and guide her to where I was, so that we have changed places, and then bend her over the table, her breasts flattening against it's surface, and she tries to turn her head back to look at me."
    
    #Yet again. God damn A22 try and contain yourself, you animal. -md01
    #"Tracing a finger around her soft lower folds and the bright pink nub of her clitoris, I plunge in, grabbing onto her hips as I start pumping in and out of her. Shizune's fingernails rake across the surface of the table, holding onto it like a mountain climber scaling a rock wall."
    
    "Tracing a finger around her soft lower folds and the bright pink nub of her clitoris, I plunge in, grabbing onto her hips as I start pumping in and out of her." 
        
    "Shizune's fingernails rake across the surface of the table, holding onto it like a mountain climber scaling a rock wall."
    
    "She seems more sensitive than before, and a little confused now that she isn't in control, but I can see she is already thinking about how to regain it as she tries to get back her usual composure."
    
    "My hand glides around the curve of her stockinged thigh and I carefully tease her clitoral bud, almost losing my balance when she reacts strongly, snapping upwards and back into my groin and nearly pushing us both to the floor."
    
    "Even though I can't see her face, I can tell Shizune is blushing intently."
    
    "I grab her prominent breasts from behind and fondle them as I've always wanted to. They feel even larger than they appear, and overflow my hands, soft and perfectly shaped."
    
    "She squirms under me as I flick my fingers over her nipples, twisting at the stimulation and driving herself backwards with each touch."
    
    shi "nna…"
    
    shi "…hhh."
    
    "Her hands writhe across the surface of the table, and grabbing onto it, she hooks her legs around the back of my ankles, pressing us closer together, connecting us even more closely and entrapping me inside her."
    
    "Her inner walls are so hot and tight, and with her pushing up against me, the friction only increases, sending me over the top."
    
    shi "…nh!"
    
    "As soon as I orgasm, I almost fall backwards and barely manage to land on the chair Shizune put her blouse on earlier."

    stop music fadeout 3.0
    
label en_S37x:

    scene bg school_council_ss
    show shizu behind_smilelow_nak_ss
    with locationskip
    
    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.3)

    hide heartattack alpha
    with Dissolve (0.5)
    
    "A dull, throbbing murmur of pain starts in the right side of my chest, fading in and out. Never enough to cause serious worry, but I worry anyway."
    
    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.3)

    hide heartattack alpha
    with Dissolve (0.5)
    
    "I guess I should have known better. After all, this is also a physical activity."
    
    show shizu behind_blank_nak_ss
    with charachange
    
    #Changed this line so we wouldn't have to get a photoshop of another sprite -md01
    #"In front of me, Shizune picks up her skirt and puts it back on, but abandons the effort to fully dress herself there and leans back against the leg of the table pensively."
    
    "In front of me, Shizune picks up her skirt and starts to put it back on, but abandons the effort to dress herself and leans back against the leg of the table pensively."
    
    "Her eyes dart at me, and I can see that she is thinking about my condition, too. Maybe more than I am myself."
    
    "Shizune, I want a future with you."
    
    "Even if it's unrealistic, it's what I want."
    
    "Before everything that has happened since I met you, I didn't believe I had a future."
    
    "There's still time before graduation. I can still try my best to get into a good college; something I didn't think was in my grasp when I first came to Yamaku. Something I doubted I would be able to live to see when I was in the hospital."
    
    "Whatever it takes, since you have become my goal."
    
    window hide dissolve
    scene black with Dissolve(5.0)
    
label en_S38:

    play music music_daily fadein 4.0
    scene bg school_courtyard with Dissolve(2.0)
    window show dissolve
     
    "Today is my last day at Yamaku."
    
    "When I first came here, I thought that this short year would feel like an eternity. It felt like I was being cast away into a corner to be forgotten, and, immaturely, that is exactly what I thought."
    
    "I didn't think there was anything here worth growing attached to. Of course, I was wrong about that."
    
    "Now, it's like the past year wasn't enough. Just one school year that passed so quickly before my eyes."
    
    "Yesterday was the last official day of school. When I woke up, I had a hollow feeling in my stomach all the way up to the graduation ceremony, and immediately after it ended, I tried to look for Shizune, but got lost in the crowd."
    
    "In the end, after seeing my parents again for the first time since I arrived at Yamaku, and after everything was said and done, I wasn't able to even see Shizune yesterday, even after searching all around the school."
    
    "That is why today is so important. This is the last day I'll be able to see her here."
    
    scene bg school_girlsdormhall with locationchange
    
    stop music fadeout 3.0
    
    "Getting into the dorms is hard, as people are constantly moving in and out of them today, doing some last minute packing and having their final conversations with their friends. If they are going to see each other after today, it'll be hard."
    
    "Whether they go off to different universities, or just lose touch gradually..."
    
    "I've resolved to never let that happen, even if Shizune and I won't be going to the same school."
    
    "I check to see if she's in her room, but someone tells me she hasn't been back since graduation, and my heart skips a beat thinking that maybe she went home early, right after the ceremony. But, there's no point in giving up yet."
    
    "If she isn't here, there really is just one other place she could be."
    
    scene bg school_council
    show shizu behind_blank
    play sound sfx_dooropen
    with locationskip
    play music music_shizune fadein 0.2
    
    #$ renpy.pause(0.5)
    
    "I open the door to the student council room to find Shizune leaning on her desk, facing the door, almost as if she was waiting for me the whole time. It's happened so many times that there are days when I think that could actually be it."
    
    "I've gotten used to most of her quirks, though."
    
    hi "Hi."
    
    ssh "Hello."    
    
    show shizu adjust_happy with charachange
    
    "She straightens up and adjusts her glasses somberly."
    
    hi "I was kind of hoping I'd find you here."
    
    show shizu behind_smile
    with charachange
    
    ssh "I was kind of hoping you would find me here, too."
    
    hi "Heh."
    
    show shizu basic_normal2 with charachange
    
    ssh "I'm sorry I couldn't see you after graduation. I had to sort out some last minute things."
    
    ssh "I've been offered a job at my father's company."
    
    ssh "I'll have to work my way up from the bottom, but the starting salary is still very good."
    
    ssh "Even then, I was thinking that maybe I should just focus 100%% on being a full time student."
    
    ssh "I have enough of my own money to live comfortably in the meantime."
    
    ssh "I'm still thinking about what I should do."
    
    hi "It seems like a tough choice to make."
    
    show shizu adjust_smug with charachange
    
    ssh "It is. But, I've already decided. I'm going to go to school full time. I know that I am qualified for the job, but I don't want anyone to think I'm getting special treatment, or if I advance, that I didn't solely due to my ability."
    
    ssh "Pride over ambition, this time."
    
    hi "I don't see it that way. Besides, you would be overextending yourself if you tried to do it all. Sometimes, you're a little too ambitious."
    
    "Well, a little more than just sometimes."
    
    show shizu adjust_angry with charachange
    
    "Shizune catches the implication in my face and jabs me in the ribs."
    
    show shizu adjust_happy with charachange
    
    ssh "Well, then, what are you going to do?"
    
    hi "Me?"
    
    hi "I'll go to college, and become a teacher. Physics is my best subject. The most interesting subject to me, anyway. So, I'll teach that. Apparently, the test to actually become a teacher isn't too hard, it's really just about time."
    
    show shizu behind_blank with charachange
    
    ssh "It seems like you have it all planned out."
    
    hi "I've been looking into scholarships. I have a few already."
    
    show shizu behind_smile with charachange
    
    hi "What's with that expression? Impressed?"
    
    "Shizune giggles soundlessly."
    
    show shizu adjust_smug with charachange
    
    ssh "No."
    
    ssh "You know, once you plan it out, you're obligated to follow through with it."
    
    hi "I know."
    
    show shizu basic_normal
    with charachange
    
    ssh "Do you think you have the follow-through?"
    
    hi "Yeah. Really."
    
    show shizu adjust_happy
    with charachange
    
    ssh "Are you sure? Once you say “really,” the standards change. I'll hold you to it."
    
    hi "Really."
    
    show shizu basic_normal2 with charachange
    
    ssh "Why so hardworking all of a sudden? You weren't like this when I first met you, slacking off all the time. Misha and I had to drag you kicking and screaming to the student council room."
    
    hi "Hey! I never kicked or screamed."
    
    hi "Anyway, I have a goal now. You're going to succeed, right? If you're going to hold me to my success, I'm going to hold you to yours. And if you're going to excel in what you do, then, doesn't that mean that I have to as well?"
    
    ssh "Who said that?"
    
    hi "Aren't you all about competition?"
    
    show shizu adjust_smug with charachange
    
    "Shizune smiles cockily and raises an eyebrow."
    
    ssh "Oh? And who said that?"
    
    "I'm sure she already knows what I mean. After all, to me, this whole relationship started out as me trying to reach you. Now, I want to be your equal. Maybe even surpass you."
    
    "You give me drive to go somewhere, and the freedom to let that “somewhere” be wherever I want it to be. I feel alive around you."
    
    "Shizune's hand overlaps mine."
    
    hi "You, obviously."
    
    "I've always been competing with you. At first, I didn't like you very much. I didn't know what you wanted from me. So, all I wanted over you was some small triumph I could call my own to stop you from making an ass of me over and over again."
    
    "When I started falling in love with you, I stopped thinking of it like that. Maybe at that point, I started to think of it as... flirting."
    
    show shizu adjust_blush with charachange
    
    "I tell her this, and she looks away, a faint smile appearing on her face, couple with a thoughtful expression. After awhile, she says:"
    
    show shizu behind_smile with charachange
    
    ssh "Am I that important to you?"
    
    "She signs it quite casually, but I can see she is more concerned than she looks."
    
    hi "Yeah."
    
    #I thought this line would be better with the second part in it's own textbox -md01
    #ssh "A person's value is determined by how many people it would take to replace them. To me, you are irreplaceable."
    
    show shizu basic_normal2 with charachange
    
    ssh "A person's value is determined by how many people it would take to replace them."
    
    show shizu adjust_happy with charachange
    
    ssh "To me, you are irreplaceable."
    
    hi "..."
    
    hi "You too."
    
    "Misha said that she was scared that Shizune and her would drift apart after graduation. It's not like the thought hasn't crossed my mind."
    
    "She really is beautiful. Today more than ever. Maybe it's because right now, I'm already starting to think about how I will feel when I start missing her."
    
    #The line above and the line at 2262 were originally right after each other. I didn't think it made much sense that Hisao would be able to hear the sound of a camera shutter from outside while in the council room.
    #It would make even less sense for him to run outside to get the camera, and have him bring it back in to the council room to take her picture.
    #I added in the lines between this and the next comment. Basically, they leave the student council room and make their way out to the school grounds. -md01
    
    show shizu basic_normal with charachange
    
    "..."
    
    "With nothing more that needs to be said, we simply sit and enjoy each other's presence for a while."
    
    "Eventually, Shizune moves to sign something to me."
    
    show shizu behind_smile with charachange
    
    ssh "There's no reason to just sit here in this stuffy room. Lets go outside."
    
    hi "Okay."
    
    stop music fadeout 2.0
    
    #Don't forget to add the ambient crowd fx
    #Edited out the crowd. It didn't work with them only showing up for one line of text before shipping out. -md01
    scene bg school_courtyard
    #show crowd
    with locationskip
    
    #play ambient sfx_crowd_outdoors fadein 1.0
    
    "We simply sit together and watch the students as they wander by."
    
    #"There is little that needs to be said at this point. We both know our remaining time together is short."
    
    scene bg school_courtyard_ss with shorttimeskip
    
    play music music_soothing fadein 2.0
    
    #stop ambient
    
    #"We walk with each other around the courtyard for a few hours."
    
    "The sun is starting to set, and most of the students have left. Some have made their way back to the dorms, but most have left with their parents."
    
    "My mind drifts back to Shizune and what limited time we have left to ourselves. Tomorrow I will be leaving for the train station for the long ride back home, while Shizune will be returning to her own family."
    
    #End me butchering the script -md01
    
    play sound sfx_camera
    
    "The click of a camera's shutter closing brings me out of my thoughts, and I want to smack myself when I realize I don't have a proper camera with me, just what's built into my phone. If I did, I would be able to take a picture of her."
    
    "It was stupid of me not to think of bringing a camera to graduation. Not just for Shizune, but to capture all the other people and memories I've found here."
    
    "Fortunately, I spot a fellow graduate halfway across the school grounds walking with a bulky, expensive looking camera in his hands. It's an instant camera, the kind that develops the photo right after you take it."
    
    "What luck. I didn't even think they made these anymore, and they're rare to start with. I run towards him."
    
    hi "Hey, can I borrow that, just for a second? Just one quick photo."
    
    "He groans about how I must be the hundredth person today to ask, but gives it up anyway. I run back to Shizune and hold the camera up."
    
    show shizu behind_frustrated_ss with charaenter
    
    hi "Smile!"
    
    "Shizune shakes her head from side to side."
    
    hi "You don't like having your picture taken?"
    
    show shizu adjust_angry_ss with charachange
    
    "Adjusting her glasses matter-of-factly, she signs her reply strongly."
    
    ssh "I'm afraid it's a lot harder to make me smile for a camera."
    
    show shizu basic_sparkle_ss
    with charachange
    
    "Her eyes flash mischievously, the golden sunlight reflecting off those two deep, dark blue pools that always seem so curious, and teasingly playful."
    
    "Another game?"
    
    show shizu behind_blank_ss
    with charachange
    
    hi "Oh, come on."
    
    "..."
    
    hi "Well, yeah, I guess it's not like this picture means anything, though."
    
    hi "Because we are going to see each other again, aren't we?"
    
    show shizu adjust_happy_ss with charachange
    
    shi "..."
    
    "She nods."
    
    hi "I said “really,” so the standards have changed."
    
    show shizu basic_normal_ss
    with charachange
    
    ssh "My expectations have changed."
    
    hi "My school won't be that far from yours. I'll..."
    
    "I won't try to do anything. I will do it."
    
    "I'm not going to let a few miles separate us. I'm going to let something that small take away my resolve to be with her? No way."
    
    hi "Every weekend. Let's be sure to see each other every weekend."
    
    show shizu adjust_smug_ss with charachange
    
    ssh "If you're serious, and I'm serious, then a small distance is nothing."
    
    hi "That's right. We'll make it work, right?"
    
    show shizu basic_happy_ss
    with charachange
    
    ssh "You're so serious. I think I am impressed after all."
    
    hi "Heh. ...What about marriage?"
    
    show shizu adjust_smug_ss with charachange
    
    ssh "What about it?"
    
    "Don't be coy."
    
    show shizu behind_smile_close_ss with characlose
    show shizu adjust_smug_ss with charadistant
    
    "Shizune pulls the camera down and I feel her delicate lips touch mine. She quickly jumps back before I can kiss her back."
    
    ssh "Now that you have said that, my expectations have changed again."
    
    ssh "But, I think that it's possible."
    
    hi "Kids?"
    
    show shizu adjust_happy_ss with charachange
    
    ssh "That is also possible."
    
    ssh "If it's a boy, let's name him..."
    
    hi "How about something like... Isamu?"
    
    ssh "Maybe."
    
    ssh "If it's a girl?"
    
    hi "Shiina."
    
    show shizu behind_blank_ss
    with charachange
    
    ssh "Okay."
    
    ssh "It's decided, then."
    
    show shizu behind_smile_ss with charachange
    
    ssh "...I'll hold you to it!"
    
    "Finally, you decided to show me your smile."
    
    "I lift the camera back up, and take her picture."
    
    window hide dissolve
    
    play sound sfx_camera
    scene white with whiteout
    
    stop music fadeout 5.0
    
    scene black with Dissolve(5.0)
    
    #end
    
    return

label en_end_shizunegood:
    # Shizune good end, after S38
    scene black with dissolve
    centered "~ Shizune good end ~" with dissolve
    return
