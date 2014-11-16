label en_H11:
    
    #H11 – Eighteen Four
    #Start of Act 3 – "Party line" or something like that.
    #Feels a little short, and I'm not sure if I like the conclusion. Will look at it at the end of Act 3

    scene bg school_miyagi_ss 
    show hanako basic_distant_close_ss
    with locationchange

    "The tint of the room slowly changes from the shine of the afternoon to the orange of dusk."

    "A clock lazily ticks by the second, counting in the background, on the verge of hearing."

    "But, no matter how long I wait, the outcome cannot be changed."

    "The ceramic playing piece makes a small click against the board."

    show hanako basic_normal_close_ss 
    with charachange

    "Like a wound spring, Hanako makes her move only moments after mine."

    "It's embarrassing. In comparison to my 5-minute moves, she seems to know exactly what she wants to do."
    
    show hanako basic_smile_close_ss 
    with charachange

    play music music_tranquil fadein 3.0

    ha "Mate."

    hi "Again… What does that make this? 3-2?"
    
    show hanako cover_bashful_close_ss 
    with charachange
    
    ha "S-stalemates don't count."

    hi "Damn. You're getting better at this every day."

    "Chess seems to have become a popular pastime for the two of us; hiding away in the tea room, playing a game or two after classes."

    "This room is like an isolation chamber inside the already insular school that is Yamaku."

    hi "Do you fancy another game?"
    
    show hanako basic_worry_close_ss 
    with charachange

    ha "I… I have to finish my homework…"

    hi "Oh. Well, I'll see you tomorrow then."
    
    show hanako basic_distant_close_ss 
    with charachange

    ha "But… what about this…"

    "Hanako points to the pile of teacups surrounding the mostly-empty chess board."

    hi "Don't worry about it, I've got it."
    
    show hanako basic_normal_close_ss 
    with charachange

    ha "Oh… okay…"
    
    show hanako basic_bashful_close_ss 
    with charachange

    ha "S-see you."

    hi "Later."

    hide hanako
    with charaexit

    "Hanako departs as I start cleaning up the area."

    "Outside, the occasional whistles and cheers from the sporting clubs become less frequent, eventually approaching silence."

    "A part of me still wants to be in some kind of team, but I've grown accustomed to this small room and the two girls that inhabit it."

    "As I am putting away a set of cups and saucers, I hear someone at the door behind me."

    hi "Oh, did you forget something, Hanako?"
    
    show bg school_miyagi_ss at bgright
    with charamove
    
    show lilly invis at left
    with None

    show lilly basic_weaksmile_ss at twoleft
    with dissolvecharamove
    
    li "Not quite, Hisao."

    hi "Ah, Lilly, sorry. What's up?"
    
    show lilly basic_smile_ss at twoleft
    with charachange

    li "I take it from your reaction that Hanako isn't around?"

    hi "Yeah, she left about five minutes ago. She should be back at the dorm by now."

    li "Actually, Hisao, it was you that I was looking for, preferably without Hanako around."
    
    hi "Oh, really? This sounds slightly suspicious, if I do say so myself…"

    show lilly basic_giggle_ss at twoleft
    with charachange

    li "Now Hisao, it's nothing like that. Hanako's birthday is in a little under a month."
    
    show lilly basic_weaksmile_ss at twoleft
    with charachange

    li "It's not really something that she looks forward to, but I like to try to cheer her up, and I was hoping that you'd help me out."

    hi "Well, sure. But what do you mean she doesn’t look forward to it?"
    
    hide lilly
    with charaexit
      
    show lilly invis
    with None
    
    show lilly basic_reminisce_close_ss at centersit
    with dissolvecharamove

    "Lilly feels her way to a seat at the table. Following her lead, I sit down across from her."

    li "I don't think it's really anything that's worth mentioning, but I don't think Hanako places all that much importance on her birthday."
    
    show lilly basic_weaksmile_close_ss at centersit
    with charachange

    li "But I think that things like birthdays should be celebrated; they're not an ordinary day, so you should at least do something out of the ordinary."

    hi "Hmm. I think I get your point. So, what do you have in mind?"
    
    show lilly basic_satisfied_close_ss at centersit
    with charachange

    li "Well, Hanako would never admit it, but she has a bit of a soft spot for Karaoke. I thought we could maybe book out a room for the three of us."

    #Suriko, don't worry. The actual party will be in Lilly's room, but this is
    #before Lilly knows she has to go away.

    "Karaoke? Hanako?"

    "My initial reaction is one of shock, but the more I think about it, the more it makes sense."

    "Hanako, in a small room, just letting loose. I wonder though; will she be able to sing with me hanging around?"

    hi "I can't see any problem with that. When are we talking about?"
    
    show lilly basic_smile_close_ss at centersit
    with charachange

    li "Wednesday three weeks from now."

    hi "That's a fair way's off; why bring it up now?"
    
    show lilly basic_planned_close_ss at centersit
    with charachange

    li "I was hoping that you would be able to do me a favour and help me around town on Sunday."
    
    show lilly basic_weaksmile_close_ss at centersit
    with charachange

    li "The last few years, we've had to resort to staying in our dorm. It's hard for me to find anything in the city without a guide, and it's hard to surprise someone if they have to lead you somewhere."

    hi "Ah, I've got you. So you want me to sneak out with you so we can find somewhere without raising suspicion?"
    
    show lilly basic_smile_close_ss at centersit
    with charachange

    li "Exactly. If we go this week, then Hanako won't be able to make the link."

    hi "Very crafty. So I guess I'll meet you at the gates then? What time?"
    
    show lilly behind_displeased_close_ss at centersit
    with charachange

    li "Let's see, the first bus leaves at nine of a Sunday, but I think that is a little early."
    
    show lilly basic_weaksmile_close_ss at centersit
    with charachange

    li "How about ten?"

    hi "Sounds good to me, I'll see you there."
    
    show lilly basic_smile_close_ss at centersit
    with charachange

    li "Well then, that's settled. Goodnight, Hisao."

    hi "Night."

    hide lilly
    with charaexit
    
    with Pause(0.4)

    "A birthday party for Hanako, eh?"

    "She doesn't seem like the kind of person who would be thrilled about that, but Lilly does have some kind of a point."

    "In a place like this, it's important to celebrate the \"ordinary\" things in life, like birthdays."

    "Just another reminder that we aren't totally separated from the rest of the world."

    "Outside, the very last whistle blows as the sun's light dwindles from the sky."

    "A trip into town with Lilly. It doesn't seem like that bad of an idea."

    "I've nearly been here a month and have barely ventured past Auramart and the Shanghai."

    "Then again, heading into town isn't really something that you associate with Hanako."
          
    "Hmm."

    "Outside of class, I only seem to hang out with Lilly and Hanako."

    "Whenever I consider going into town, my first though is \"I wonder if Hanako would come along?\"."

    "I laugh a little to myself."

    "I wonder if this is how Lilly found herself spending so much time with Hanako?"

    "Altering her habits so as not to put Hanako into any compromising situations?"

    "Well, it's not like it's such a bad thing. Hanako seems to have opened herself up a lot more from when I first met her."

    "Maybe all she needed was someone to approach her as opposed to avoiding the shy girl at the back of the classroom."
    
    stop music fadeout 4.0

    "I think I'm going to look forward to this party."
    
    return
    
    #---------
label en_H12:
    #H12 – Unexpected Alliance

    scene bg school_hallway2
    play sound sfx_doorclose
    with locationchange

    "I continue to ponder my predicament with Hanako and Lilly as I close to door to the tea room."

    mi "Oh ho ho… and just what were you doing in there, Hisao?"
    
    play music music_shizune fadein 0.5

    show misha perky_smile_close at closeleft
    show shizu behind_blank at tworight
    with charaenter

    "Damn. I was so lost in my thoughts that I didn't even see the entire Student council creeping up on me."

    "Misha can be surprisingly stealthy when she's only talking with her hands."

    hi "Just cleaning up. Wouldn't want to leave any school property in a mess, would we?"
    
    show shizu basic_normal at tworight
    with charachange

    shi "…"
    
    show misha cross_smile_close at closeleft
    with charachange

    mi "How very considerate of you, Hisao. But before we get too far…"
    
    show bg school_hallway2 at bgright
    show shizu invis at rightedge
    show misha cross_smile_close at twoleft
    with Dissolvemove(0.3)
    
    play sound sfx_dooropen
    
    with vpunch

    "Without warning, Shizune pushes past me and opens the door to the tea room."
    
    show shizu adjust_happy at right
    with dissolvecharamove

    shi "…"
    
    show misha sign_smile_close at twoleft
    with charachange

    mi "Whilst I cannot approve of your use of this room, I am impressed that you keep it in a better state than most club rooms."
    
    show shizu adjust_smug at right
    show misha perky_smile_close at twoleft
    with charachange

    mi "As a reward, you will come with us to dinner."

    hi "Um, Misha, shouldn't that be \"you can come with us…\"?"

    show misha hips_grin_close at twoleft
    with charachange

    mi "Nope. Shicchan said what I said. If I didn't say things properly what good would I be?"

    "I fight back the urge to point out the numerous time that Misha's translations have been less than perfect."

    "Besides, forcing me to go to dinner with them seems like something Shizune would say."
    
    show shizu behind_smile at right
    with charachange

    shi "…"
    
    show misha perky_smile_close at twoleft
    with charachange

    mi "Oh, and before you go getting any strange ideas, we're not trying to recruit you anymore."
    
    show misha cross_smile_close at twoleft
    with charachange

    mi "You've already been tainted by Miss Satou's laid-back ways. You're no longer of any use to us."

    hi "Huh, so you've got no interest in \"used goods\" then?"

    show shizu adjust_blush at right
    with charachange

    show misha perky_confused_close at twoleft
    with charachange

    shi "…!"

    mi "That's not what I meant. But now that the festival is over there's really nothing much to do unless there's some kind of crisis."
    
    show shizu adjust_happy at right
    with charachange
    
    show misha hips_grin_close at twoleft
    with charachange

    mi "So don't worry about it! We'll manage just fine without you!"
    
    show misha hips_smile_close at twoleft
    with charachange

    mi "We see each other all the time in class anyway."

    "From what I can tell, Misha and Shizune are being sincere. And they haven't mentioned the council at all in class for at least a week." 

    "Then again, I wouldn't put a feint like this behind them. I've got to be on my guard."

    "It would have been good to have an excuse, like helping Hanako with her homework, but that boat has already sailed."

    "Ah well, it would be good to get out of school with someone else for once."

    hi "That's true enough. Anyway, I didn't really have any plans for this evening, so I guess I can come with you."

    show shizu basic_happy at closeright
    with charachange

    show misha sign_smile_close at left
    with charachange

    shi "…"

    mi "Well that is good news! Come on, we have a reservation. If we don't hurry we'll lose our seats."

    stop music fadeout 2.0
    
    scene bg suburb_shanghaiint at right
    show misha hips_smile
    with shorttimeskip
    
    play sound sfx_storebell

    #show shizu behind_smile at tworight

    mi "Phew~! We made it!"
    
    hide misha
    with charaexit
    
    scene bg suburb_shanghaiint at Fullpan(3.0, dir="left") 
    with None

    "I cast my eyes across the barren café. I'm a little disheartened to think that we pretty much ran the whole way down the hill to the Shanghai."

    hi "Made what? There's not a soul here! Is the place even open?"
    
    show bg suburb_shanghaiint at left
    show shizu behind_smile at tworight
    show misha sign_confused at twoleft
    with charaenter

    play music music_dreamy fadein 6.0

    #show misha sign_confused at twoleft
    #with charachange

    mi "Doesn't rushing to an appointment make it all the more worthwhile?"
    
    show misha perky_smile at twoleft
    with charachange

    mi "If there is no pressure, then there is no relief, right?"

    hi "I don't follow you, but whatever. Anyway, should we sit down? I'm a little tired after that trip…"
    
    show misha hips_grin at twoleft
    with charachange

    mi "Sure sure sure sure~! We reserved our usual table, so we can sit over there."
    
    hide misha
    hide shizu
    with charaexit

    show bg suburb_shanghaiint at bgleft 
    with charamove_slow
    
    show misha invis at twoleft
    show shizu invis at tworight
    with None

    show misha perky_smile at twoleftsit
    with dissolvecharamove
    
    show shizu behind_blank at tworightsit
    with dissolvecharamove

    "Misha takes the lead, bounding to \"her\" table. Shizune and I follow in a comparatively demure manner."

    "I guess I wasn't the only one left a little winded by Misha's walking pace."

    "Misha sits upright in the booth and starts fidgeting with everything in sight."

    yu "Oh… sorry, I didn't hear you come in…"
    
    show bg suburb_shanghaiint
    show misha perky_smile at centersit
    show shizu behind_blank at rightsit
    with dissolvecharamove
    
    show yuukoshang invis at leftdooropen
    with None

    show yuukoshang panic_up at Position(xanchor=0.5, xpos=0.22)
    with dissolvecharamovefast
    
    show yuukoshang panic_up at Position(xanchor=0.5, xpos=0.19)
    with dissolvecharamovefast

    "A concerned-looking Yuuko bolts out from the back room of the café and practically skids to a halt at our table."
    
    show yuukoshang neutral_up at Position(xanchor=0.5, xpos=0.19)
    with charachange

    yu "Are you ready to order?"
    
    show shizu adjust_happy at rightsit
    with charachange

    shi "…"
    
    show misha hips_grin at centersit
    with charachange

    mi "Right, we'll have three curries, thanks. Extra rice for Hisao. He's a boy, you know~."
    
    show yuukoshang worried_down at Position(xanchor=0.5, xpos=0.19)
    with charachange

    "Yuuko fumbles with her order book, the tip of her tongue sticking out from the corner of her mouth."
    
    show yuukoshang neutral_down at Position(xanchor=0.5, xpos=0.19)
    with charachange

    yu "O-kay. Three curries. One extra rice. I'll be back in a minute…"
    
    show yuukoshang neutral_down at Position(xanchor=0.5, xpos=0.10)
    with dissolvecharamove
    
    show yuukoshang neurotic_up at Position(xanchor=0.5, xpos=0.19)
    with Dissolvemove(.4)

    "She takes no more than a step and a half before pirouetting around with a look of terror on her face."

    yu "I'm sorry would you like any drink! Drinks!"

    hi "Just a pot of green tea I think. Don't think too much about it."
    
    show yuukoshang worried_down at Position(xanchor=0.5, xpos=0.19)
    with charachange

    yu "R-right. I'll be back soon."
    
    show bg suburb_shanghaiint at bgleft
    show yuukoshang invis at offscreenleft
    show misha perky_smile at twoleftsit
    show shizu behind_smile at tworightsit
    with dissolvecharamove
    
    hide yuukoshang
    with None

    "Yuuko disappears through the staff entrance with the determination of a hurricane."

    hi "I didn't know they did curry here…"

    show shizu basic_sparkle at tworightsit
    with charachange

    shi "…" 
    
    show misha cross_grin at twoleftsit
    with charachange

    mi "I expected as much. That is why I took the liberty of ordering for you."
    
    show misha perky_smile at twoleftsit
    with charachange
    
    show shizu adjust_happy at tworightsit
    with charachange

    mi "Many people find it hard to adjust to the Shanghai's unique ordering system, so until you adjust, feel free to use us as your guides."
    
    show misha sign_smile at twoleftsit
    with charachange

    mi "That's right, Hisao. A café with no menu is a bit of a strain on the brain."

    hi "Yeah, I still don't get that. Are they trying to be trendy or something?"
    
    show shizu basic_normal at tworightsit
    with charachange

    show misha perky_sad at twoleftsit
    with charachange

    mi "Hmm… I think it's because Yuuko probably forgot to write them out. And since the owner rarely comes out here he hasn't noticed."

    hi "You don't say…"

    show misha hips_laugh at twoleftsit
    with charachange

    mi "Wahaha~! At least that's my theory!"
    
    show shizu behind_blank at tworightsit
    with charachange
    
    with Pause (0.1)
    
    show shizu invis at tworight
    with dissolvecharamove
    
    hide shizu
    with None
    
    show bg suburb_shanghaiint
    show misha hips_smile at centersit
    with dissolvecharamove

    "Shizune, obviously disinterested in our conversation, excuses herself through Misha."

    "The tiny cogs in my mind turn, and a connection is made."

    hi "Hey, Misha, you go into town a bit, don't you?"
    
    show misha perky_smile at centersit
    with charachange

    mi "Yeah, why?"

    hi "I don't suppose you know if there's any good karaoke places around, do you?"
    
    show misha hips_grin at centersit
    with charachange

    mi "Oh! You want to try some out? We can go after this if you'd like!"

    hi "It's already late, and it's a school night. I have things I need to do, you know."

    show misha perky_sad at centersit
    with charachange

    mi "Aw. I hardly ever go to karaoke because of… well… you're smart. You can figure it out…"
    
    hi "Well, I didn't mean it like that. I…"
        
    "I consider telling her that it's for Hanako and Lilly's sake, but decide not to. Lilly's involvement would annoy Shizune, and if Misha knew that Hanako liked karaoke she could tease her."

    hi "…I just wanted to know what's in town, you know? I haven't been there much."

    show misha cross_grin at centersit
    with charachange

    mi "Well, there are a couple of places. There's one in the game centre, there's one of those big complex ones on the main street, and then there's that little one near the station."

    hi "Right, thanks. I'll look into them,"
    
    show misha hips_laugh at centersit
    with charachange

    mi "When you do, be sure to invite me! Wahaha!"

    hi "I'll keep it in mind."

    #show shizu cross_wut at tworight
    
    show shizu invis at right
    with None
    
    show bg suburb_shanghaiint at bgleft
    show misha hips_grin at twoleftsit
    show shizu behind_smile at tworightsit
    with dissolvecharamove
    
    with Pause (0.1)
    
    show shizu basic_normal2 at tworightsit
    with charachange
    show misha sign_smile at twoleftsit
    with charachange
    show shizu adjust_frown at tworightsit
    with charachange
    show misha perky_confused at twoleftsit
    with charachange
    show shizu behind_blank at tworightsit
    with charachange

    "Shizune returns to the table and exchanges a glut of sign with Misha."

    "Judging by Shizune's mixture of bored and irritated reactions, I can only assume Misha is telling her about my question."

    "Typical. I only thought to ask because Shizune left us alone for a second. I didn't want to insult her."
    
    show shizu adjust_happy at tworightsit
    with charachange

    shi "…"
    
    show misha cross_grin at twoleftsit
    with charachange

    mi "Shicchan says that if you're so desperate to make a fool of yourself then she won't stop you."
    
    show misha hips_smile at twoleftsit
    with charachange

    mi "But if you want to take me out, you'll have to ask her permission first."

    hi "Ah, no, damnit… I didn't mean it like that. I was actually asking for someone else…"

    show shizu cross_angry at tworightsit
    with charachange

    show misha sign_confused at twoleftsit
    with charachange

    mi "Oh really? And who might that be?"

    hi "If I say then you'll get annoyed."
    
    show shizu basic_frown at tworightsit
    with charachange

    shi "…"
    
    show misha cross_frown at twoleftsit
    with charachange

    mi "In that case then I already know. I've half a mind to cancel this dinner, but since we've already ordered it would be unfair on Yuuko."
    
    show misha hips_frown at twoleftsit
    with charachange

    mi "Instead, you can pay for our meals."

    hi "I don't have that kind of money? Wait, how much is the curry here?"
    
    show shizu behind_frustrated at tworightsit
    with charachange

    shi "…"
    
    show misha sign_confused at twoleftsit
    with charachange

    mi "In that case you can pay for my portion. I'll pay for yours and Misha's."

    hi "How does that make any sense?"
    
    show shizu adjust_frown at tworightsit
    with charachange

    shi "…"
    
    show misha hips_frown at twoleftsit
    with charachange

    mi "You'll be buying me dinner as repayment for this insult."

    "I can't tell if this is for show or if Shizune is genuinely insulted. Still, better be safe than sorry."

    hi "That doesn't make any sense. Look, I'll pay for everyone. It was my mistake anyway…"

    show misha perky_smile at twoleftsit
    show shizu behind_smile at tworightsit
    with charachange

    "Halfway through my sentence Misha and Shizune start to grin, and I realise I've been had."
    
    show shizu adjust_smug at tworightsit
    with charachange

    shi "…"
    
    show misha cross_laugh at twoleftsit
    with charachange

    mi "Why, thank you ever so much, Hisao. You are quite the gentleman."

    hi "Yeah yeah, you got me. It's my shout."
    
    show misha cross_smile at twoleftsit
    show shizu adjust_happy at tworightsit
    with charachange

    mi "For the record, Shicchan may not be able to sing, but that doesn't mean she can't have a good time."
    
    show misha perky_smile at twoleftsit
    with charachange
           
    mi "Maybe one day we could all go to the karaoke place in the game centre. That way everyone is happy."
           
    hi "Why do I get the feeling that you'd somehow manage to con me into paying the bill there too?"

    show misha hips_laugh at twoleftsit
    with charachange

    mi "Wahaha~! You make it sound like we're conspiring against you, Hisao! You know we'd never do that!"

    "But you just did exactly that… Or perhaps Misha doesn't even realise what they just pulled…"

    hi "Somehow, I don't feel that I can trust you. Still, maybe one day we'll do that."

    show misha cross_smile at twoleftsit
    show shizu behind_smile at tworightsit
    with charachange

    mi "I'll hold you to that, Hisao."

    yu "I'm sorry to keep you waiting!"
    
    show yuukoshang invis at offscreenleft
    with None
    
    show bg suburb_shanghaiint
    show yuukoshang neutral_up at left
    show misha cross_smile at centersit
    show shizu behind_smile at rightsit
    with dissolvecharamove

    "Yuuko finally appears carrying a tray with our curry."
    
    show yuukoshang neutral_down at left
    with charachange

    "After a few tense seconds, the tray finds its way safely to our table."
    
    show bg suburb_shanghaiint at bgleft
    show yuukoshang invis at offscreenleft
    show misha perky_smile at twoleftsit
    show shizu behind_blank at tworightsit
    with dissolvecharamove

    hide yuukoshang
    with None
    
    "Misha and Shizune start to eat their food, and out of some kind of instinct I pour the tea."

    "I must have acquired the habit after watching Lilly and Hanako having trouble with the same action."

    hi "Is that enough, Shizune?"

    show shizu basic_angry at tworightsit
    with charachange
    
    shi "…"

    "It takes me a moment to realise the problem. Both Misha and Shizune have their hands full with their food. Communication is impossible."

    "Still, she could have just nodded…"
    
    show shizu basic_normal at tworightsit
    with charachange

    "Our meal passes in silence, and I'm honestly appreciative of the extra rice. I still can't work out why they bothered to order it for me though."

    show misha cross_smile at twoleftsit
    show shizu behind_smile at tworightsit
    with charachange
    
    mi "Mmm! That was good. What do you think, Hicchan?"

    hi "You're right, it was better than expected. This place is full of surprises."
    
    show shizu adjust_happy at tworightsit
    with charachange
    show misha sign_smile at twoleftsit
    with charachange

    mi "Now then, karaoke! If you're not going tonight, then how about Sunday?"

    hi "Actually, I have plans this Sunday. Maybe some other time?"

    show misha cross_frown at twoleftsit
    show shizu adjust_frown at tworightsit
    with charachange

    mi "You say that, but do you really mean it?"

    hi "Yes, I guess."
    
    show misha perky_confused at twoleftsit
    with charachange

    mi "Are you really busy this Sunday?"

    hi "Really."
    
    show misha sign_confused at twoleftsit
    with charachange

    mi "Doing what?"

    hi "I'd prefer not to say."

    show shizu cross_angry at tworightsit
    with charachange

    shi "…"
    
    show misha cross_smile at twoleftsit
    with charachange

    mi "Hmm. Sounds suspicious to me.  Still, it's not our way to pry into people's personal lives."

    hi "You're kidding, right?"

    show shizu adjust_smug at tworightsit
    with charachange

    shi "…"
    
    show misha hips_grin at twoleftsit
    with charachange

    mi "We may be kidding, we may not be. Don't forget to pay the bill now!"
    
    show shizu invis at tworight
    show misha invis at twoleft
    with dissolvecharamove
    
    hide shizu
    hide misha
    with None
    
    play sound sfx_storebell

    "Before I can say another word, the girls are out the door."

    "I grudgingly pay the bill, which isn't anywhere near as dear as I thought it would be."

    "At least Shizune and Misha are still Shizune and Misha. I've been hanging out with Hanako and Lilly so much that I've barely talked to them outside of class."

    "It's nice to know that they're still as playful as ever, at least in their own, manipulative definition of \"playful\"."
    
    stop music fadeout 6.0

    "And when they're not pushing their Student Council line they're kinda fun to hang out with."

    "Well, fun, but expensive. I hope I've got enough money left over this week for the trip into town."
    
    scene black
    with dissolve
    
    return
    
    #---------------
label en_H13:
    
    play music music_daily fadein 2.0
    $ renpy.music.set_volume(0.40000000000000002, 0.0, channel='ambient')
    play ambient sfx_park fadein 2.0

    scene bg misc_sky 
    with locationchange

    "A light breeze blows the scent of early summer around my head as I wait for Lilly."

    "Small white clouds litter the sky, breaking up the monotony of the blue."

    #Following section will probably change when we can see the Lilly Casual outfit

    li "Hisao? Are you here?"

    "Lilly's voice lilts on the breeze as if they were one and the same thing."

    "I stop gazing into the sky to examine Lilly."
    
    $ renpy.music.set_volume(0.80000000000000004, 1.0, channel='ambient')

    scene bg school_gate 
    show lilly cane_surprised_cas at center 
    with locationchange

    "She's wearing a peach off-the-shoulder sweater and tan ankle-length skirt, in addition to tan sandals."

    "Her outfit is a much closer fit than the school uniform, accentuating her figure in all the appropriate places."

    "It's strange, I would never have thought that such an unflattering color scheme could be so alluring."

    hi "Yeah, I'm over here Lilly. Near the gate."

    hi "Were you able to sneak away from Hanako?"
    
    show lilly cane_weaksmile_cas
    with charachange

    li "Yes. It's not uncommon for me to go out of a weekend, so she didn't seem to notice anything suspicious."

    hi "Cool. Well then, the bus arrives in a few minutes, should we head to the bus stop?"
    
    show lilly cane_smile_cas 
    with charachange

    li "Indeed. It's a long wait if we miss this one."

    "Lilly is right. The bus into town only comes once an hour on Sundays."

    hi "I hope you don't mind, but I asked around for some suggestions. I've never really been into town here so I was curious."
    
    show lilly cane_ara_cas 
    with charachange
    
    li "Of course I don't mind. Proper prior planning prevents poor performance, or so they say."
    
    #Ha! Eat that, Translators!
    
    show lilly cane_smile_cas 
    with charachange
    
    li "I also know of a place, though I have only been there once."
    
    "Of course. How would Lilly know that Hanako liked karaoke if they'd never been?"
    
    "Maybe Lilly sneaks Hanako into town regularly to sing a little?"
    
    hi "Well, it's probably one of the places I looked up anyway, so we should be able to find it pretty easily."
    
    show lilly cane_smileclosed_cas
    with charachange
    
    li "What thorugh research. I'm a little envious."
    
    hi "To be honest, I did only look it up this morning. And I had to skip breakfast to make it here on time."

    show lilly cane_concerned_cas
    with charachange

    li "Hisao, we haven't even gotten on the bus and you're already wanting to stop for lunch?"

    hi "I think that it would be research vital to the success of Hanako's party."

    li "That doesn't sound too convincing…"
    
    show lilly cane_listen_cas
    with charachange

    li  "Oh, here comes the bus…"
    
    scene bg school_road 
    with locationchange

    "I look down the road to see the bus trundling up the hill."
    
    stop music fadeout 6.0
    
    "Now that I can see it I can clearly hear the straining engine above the background noise."

    "It's amazing how much sensory information the brain simply throws away."
    
    stop ambient fadeout 2.0

    "The bus only takes a few seconds to reach the bus stop, and within a minute we are on our way to town."

    scene bg city_street1 
    with shorttimeskip

    play music music_ease fadein 2.0
    $ renpy.music.set_volume(0.40000000000000002, 0.0, channel='ambient')
    play ambient sfx_traffic fadein 2.0
    
    "The town is much like any other town, save for the raised walkways."

    "After alighting from the bus Lilly directs me up some stairs to the walkways, which totally separate the pedestrians from the traffic below."

    "It feels a little weird, walking around a city as casually as you would in a park, but with cars rushing around underneath you."

    "But as I ponder the engineering marvel that is the raised walkway, a strange sensation envelops me."

    hi "L-Lilly!"
    
    show lilly invis at twocenteroff2
    with None

    show lilly cane_giggle_cas_close
    with dissolvecharamove

    li "Did I startle you?"

    "Lilly has wrapped her arm around mine, extending her cane in front of her with her other hand."
    
    show lilly cane_smileclosed_cas_close
    with charachange

    li "I'm sorry, but it is a lot easier this way here. People seem to find it easier to avoid two people instead of just the one."

    "It's not the first time this has happened, so I shouldn't be so surprised, but at the time Lilly only held onto my sleve."

    show lilly cane_arablush_cas_close
    with charachange

    li "Now Hisao, you wouldn't be getting embarrassed right now, would you?"

    hi "What's there to be embarrassed about? Clearly I'm just helping you out…"
    
    "No sooner have the words left my mouth do I realise that I mean it. Lilly is holding onto my arm for guidance, and that is that."
    
    show lilly cane_cheerful_cas_close
    with charachange

    li "Well, if you are helping me out, how about we start searching, instead of loitering here arm-in-arm."

    hi "Right. Right. If my memory is correct, it should be this way."

    scene bg city_street2
    with locationchange

    "We wander around the walkways of the town, Lilly merrily tapping away with her cane whilst I keep an eye out for the karaoke bar Misha mentioned."
    
    "I can't bring myself to tell her that I heard about it from the Student Council. It would sour her mood."

    "The city seems to be fairly lively, though spacious. Crowds spread across the walkways, but never thick enough to cause much human traffic."

    "Multi-story stores branch off from the walkways, connected to it by smaller bridges."

    hi "So, do you come here often? To karaoke, I mean?"
    
    show lilly cane_smile_cas_close
    with charaenter

    li "No, I've only been a few times."

    "There goes my theory of Songstress Lilly and her Chorister Hanako. Maybe one trip was enough for Lilly to realise Hanako liked it."

    "The Karaoke bar is located between two clothing stores, adorned with flashing neon signs and honky little speakers playing radio ads on a loop."

    hi "Are you sure this is the right place though? It looks a little garish…"
    
    show lilly cane_weaksmile_cas_close
    with charachange

    li "Ah, I do remember someone saying that. However, it does have quite a few private booths."

    hi "Fair enough. Hanako might like this place after all."

    "Though, in my mind, I cannot imagine Hanako liking a place like this. I hope Lilly is right…"
    
    show lilly cane_cheerful_cas_close
    with charachange

    li "Well then, shall we go in?"

    hi "What, now?"
    
    show lilly cane_satisfied_cas_close
    with charachange
    
    stop music fadeout 6.0

    li "I don't see why not, since we found the place so quickly."

    hi "Well, I'd actually prefer to get some lunch first…"

    show lilly cane_ara_cas_close
    with charachange

    li "I'm sure that they have food inside. Besides, we should make sure that this place is good for Hanako, shouldn't we?"
        
    hi "Fine, I get it. Let me just get a room for us."
    
    stop ambient fadeout 1.0
    play music music_another fadein 4.0

    scene bg city_karaokeint
    with locationskip

    "Inside, I order a plate of snacks and a room for an hour."

    "The interior is a little more subdued than the exterior, and the rooms are little more than a bench and a table surrounding the main screen."

    show lilly basic_smile_cas
    with charaenter

    li "So, what should we sing?"

    hi "Don't tell me… we need to test the integrity of the gear? Are you sure that this is really for Hanako's sake?"
    
    show lilly basic_cheerful_cas
    with charachange

    "Lilly flashes me a mischievous smile for the shortest of moments."

    li "But of course. Everything needs to be perfect, or else there is no point. And of course this is for Hanako, but that doesn't mean we can't enjoy it, too."

    hi "Okay okay, let me punch in a song for you. What do you want?"
    
    show lilly basic_listen_cas
    with charachange

    li "Hmm, is Kagerou in there?"

    #Ha! finally managed to get a scene name that I can keep.
    #Though we could easily change this if required.

    "I scroll through the list of songs on the control panel, and select the song from the menu."

    "The great wheels of automation turn over, and soon the melody is flooding from the speakers at high volume."
    
    show lilly basic_smileclosed_cas
    with charachange
    #to replace once mic prop is drawn

    "Lilly reaches out her hand, and I place the mic in it."

    "Even without the cues from the monitor, Lilly seems to not miss a beat. I guess she knows the song by heart."
    
    "As she stands there, swaying gently in time with the music, I begin to realise why I wasn't embarassed that Lilly took my arm."
    
    "Lilly is a vision of beauty, but she and I are nothing more than friends."
    
    "She and I could \"hang out\" for years on end, and that would be all we ever do."

    "The song finishes quickly enough, breaking my concentration. Lilly holds out the mic for me."
    
    show lilly basic_cheerful_cas
    with charachange

    li "Your turn, Hisao."

    hi "Eh, maybe in a bit. I want to finish these off first…"

    "The plate of snacks, listed on the menu as \"enough for four!\", is barely filling my stomach."
    
    show lilly basic_giggle_cas
    with charachange

    li "Well, I guess that's okay. This is only a test run, after all."

    hi "Is that all you wanted to do today? To do a test run?"

    show lilly basic_smile_cas
    with charachange

    li "Well, mostly. Unless there is anything that you'd like to do, I'm happy with just this."

    hi "Really? Well then, fair enough. I would have thought that you'd want to go shopping or something like that…"
    
    show lilly basic_ara_cas
    with charachange

    li "My my, Hisao, you wouldn't be trying to turn this into a date, would you?"

    hi "No, it's not like that. I just haven't spent much time in town, so I don't know what else there is to do."
    
    show lilly basic_smileclosed_cas
    with charachange

    li "I think it's much like any other city. If you know where to look, you can find anything that you want to do."

    hi "You make it sound like you've been to a lot of cities…"
    
    show lilly basic_smile_cas
    with charachange

    li "Only a few, both here and in South Africa."

    hi "South Africa? What were you doing there?"

    show lilly basic_oops_cas
    with charachange

    li "Oh, did I not tell you? My family lives in South Africa, but my father was originally from Japan. That is why I am here now."

    hi "Right… I guess that makes some kind of sense. Why South Africa though?"
    
    show lilly basic_displeased_cas
    with charachange

    li "My parents are involved with mining, and that work keeps them there, but they do come back here occasionally."

    hi "So then, why do you stay here?"

    show lilly basic_reminisce_cas
    with charachange

    li "It is a slightly complicated matter, however this school is part of the reason. There isn't anything like it in South Africa."
    
    show lilly basic_weaksmile_cas
    with charachange

    li "Also, it is easier to become a teacher here."

    hi "Oh, so you want to teach, and not stay in the mining business?"
    
    show lilly basic_planned_cas
    with charachange

    li "Yes, I'd like to teach languages. And my eldest sister, Akira, is to inherit the company, so I don't need to stay in mining."

    "Being a teacher would suit Lilly perfectly. She has the attitude and the patience to deal with anyone."

    "You only need to see the care that she puts into dealing with Hanako to notice that."
    
    show lilly basic_smile_cas
    with charachange

    li "And what about you, Hisao? What are your plans for your future?"

    hi "To be honest, I haven't thought about that much recently."

    hi "Before… well, before my attack, I wanted to do something active, like maybe something to do with sports, but that's out of the question now."

    "In fact, I don't think I've thought at all about a \"future\" for some time now. It seems almost futile."

    show lilly basic_pout_cas
    with charachange

    li "Now that just won't do, Hisao."

    hi "Eh? What won't?"
    
    show lilly basic_sleepy_cas
    with charachange

    li "Not planning for the future. This is your last year of school. After this, you will have to fend for yourself one way or the other."

    hi "It's not like I don't know that, I just haven't put much thought into it since then…"
    
    show lilly basic_concerned_cas
    with charachange

    li "Well, I can understand that. But you can't let something that might happen affect what will happen."
    
    show lilly basic_oops_cas
    with charachange

    li "You will finish school and you will need to find a job. But if you get hung up on your problems too much, you'll miss your chances."

    hi "Okay, okay, I'll think about it."

    show lilly basic_weaksmile_cas
    with charachange

    li "I think that would be a good idea. Anyway, onto the next song. I believe that it is your turn…"

    hi "Fine fine, just don't expect too much."
    
    hide lilly
    with charaexit

    "Lilly and I use the remainder of our time in the karaoke booth to make sure that it is completely adequate for Hanako's party."

    "Before we realise it, the phone on the wall rings and the attendant asks if we would like an extension."

    "We politely refuse, and I pay for the room and the snacks on the way out."

    stop music fadeout 2.0

    $ renpy.music.set_volume(0.40000000000000002, 0.0, channel='ambient')
    play ambient sfx_traffic fadein 2.0

    scene bg city_street2 
    show lilly cane_smileclosed_cas_close 
    with shorttimeskip
    
    "Once we are out on the street again, Lilly takes a hold of my arm once again."
    
    show lilly cane_smile_cas_close 
    with charachange

    li "Well then, shall we head back now?"

    hi "To be honest, I'd like to find some more food first. A plate of snacks is no substitute for a real meal."
    
    show lilly cane_weaksmile_cas_close 
    with charachange

    li "That's true. And since you payed for the karaoke, it would be rude of me not to pay."

    hi "Really? That sounds good to me. Know of any good places around here?"
    
    show lilly cane_cheerful_cas_close 
    with charachange

    li "There is a small take-away shop near the bus stop. We could eat on the bus on the way back."

    hi "Perfect. I think I remember my way back to the bus stop; it wasn't that far."
    
    hide lilly
    with charaexit

    "Amazingly, I manage to find the bus stop on the first try, and the take-away place not too long afterwards."
    
    stop ambient fadeout 3.0
    
    "We both order, get our food, and board the bus."

    scene bg school_dormext
    with shorttimeskip
    
    play music music_tranquil fadein 4.0
    
    show lilly cane_planned_cas
    with charaenter

    li "Thank you for today, Hisao. I'll ring that place and make a booking for Hanako's birthday."

    hi "Not a problem; thanks for lunch."
    
    show lilly cane_weaksmile_cas
    with charachange

    li "Any time, Hisao. But now I must be getting back. If I'm gone too long Hanako may find out."

    hi "Sure thing. I'll be sure to keep it a secret too. Later."
    
    show lilly cane_smile_cas
    with charachange

    li "Later."

    hide lilly
    with charaexit

    "As Lilly leaves, I reflect a little on her words in the karaoke bar."

    "Am I dwelling on my condition too much?"

    "Lilly seems to get around just fine, as does Shizune."

    "Even Emi and her mechanical legs are able to keep running."

    "So what makes me any different?"

    "That is a question that I can't answer right now, but maybe that is the real point of this school, to help us work that out for ourselves."

    "Damn, I'm going to be thinking this over all night. That's the exact opposite of \"not dwelling\" on something."
    
    stop music fadeout 6.0

    "Nevertheless, with the trip into town over, I need to start looking into getting this week's homework done. Plus I need to do my laundry, have a bath, make my bed…"

    "The list just keeps going on, and with no time to do it in. It's times like this that I almost want to be back in class…"
    
    return
    
label en_H14:
    
    show white
    with locationchange
    
    window hide

    #show movie

    #play movie "video/note.mpg"
    
    
    centered "A note from the editor" with dissolve
    
    nvl show dissolve

    n "It is at this point that cpl_crud's original Act 3 'ends'."
       
    n "In all, a total of 10 scenes are missing from the Prerelease. They are known to have existed internally; in fact, one of these scenes, H23 'Waterfall,' can be found online rather easily."
    
    n "Outside of that, though, we're only left with what we can infer from proceeding scenes, code strings, and comments."
    
    n "In fact, the point where the script disappears is almost exactly the point at which the Alpha script clearly deviates from the Final one."
    
    n "These scenes would normally transition into the various 'bad' endings, which make up the entirety of Act 4 on their own."
    
    n "\nThe story behind the good, or \"True,\" ending is infinitely more complicated, however. It includes a branchoff from the existing Lilly alpha script, though the exact manner through which this would occur is still not entirely clear."

    n "I'll do my best to fill in the gaps where I can, though."
    
    n "-Alphabro"
   
    nvl hide dissolve

    nvl clear

    window show

label en_choiceH14:
    menu:
        with menueffect
        #choice:
        "First off, which ending do you want to proceed to?"

        "True/Good Ending":
            return m1
        
        "Bad Endings":
            return m2

label en_H14a:
    
    window hide

    nvl show dissolve
    
    n "\nThe case of the Hanako \"True\" route, or Hanako's singular good ending:"
    
    n "\nWhen KS was still relatively early in development, there was a plan considered in which Hanako's primary route would ONLY consist of bad endings, as shown in the script for Act 4."
    
    n "However, once the player had completed one of these endings, it would open up a new choice menu within the Lilly route, nearing the middle/end of Act 3."
    
    n "At this point in the route, the player would get to choose whether they wanted to either follow Lilly's request to watch over Hanako, or to tell Lilly that she was the one that needed to be cared for instead."
    
    n "Choosing to watch over Hanako would lead to her true ending, the complete Acts 4 and 5 that follow."
    
    n "\n\nIn a somewhat ironic way, Lilly's route would quite literally result in Hanako's good ending."
    
    nvl clear
    
    n "Where this causes serious issues, however, is in the fact that it's not exactly clear HOW this split was meant to occur."
    
    n "Because the ending is a continuation of the events of the Lilly route and not the Hanako route, it would seem that it would be a simple split directly from the Lilly route into the Hanako True ending."
    
    n "However, a few things that would seem to contradict that are:"
    
    n "1. The relatively romantic nature of the dialogue directed towards Lilly throughout the rest of the route, considering it's her route"
    
    n "2. A comment existing at the exact point that the scene L20 would transition into HT1, that reads \"The rest of this could well be summarised in the beginning of HT1 as part of a flashback.\" This would imply that the split isn't exactly direct if it would require a flashback/summary of the scene to lead into the Hanako True ending."
    
    n "\nThe best way that I can think to do this transition using the available scripts and limited knowledge of the developer's plans, then, is to summarize the main plotpoints of the Lilly route leading up to the True ending, then provide you with the specific Lilly route scenes that HT1 stems off from."
    
    #n "Due to the rather late realization of this layout for the route/scripts, though, the scenes copied from the Lilly route will not contain scene direction in this release."
    
    nvl clear
    
    n "Events leading up to the True Ending:"
    
    n "\nThe trio celebrates Lilly's birthday at Hisao's dorm, where he gives her a Musicbox that he bought from the antique store."
    
    n "In a similar vein as the party scene in the Final version of the route, they have a visitor and get drunk before the night is over. However, Akira isn't the one that provides the drinks; instead, Yuuko shows up with wine and nearly gets caught in the process."
    
    #n "Lilly has a party in her dorm room where the trio get drunk. Unlike in the Final version of this scene, Akira doesn't show up with wine; instead, Yuuko is the one who provides the drinks and nearly gets caught in the process."
        
    #n "Hisao chooses not to make Hanako go out for dinner when she feels somewhat uncomfortable about the idea, therefore avoiding Waterfall and the bad endings."
    
    n "Lilly visits the hospital for an operation after she contracts tonsillitis, removing her from school for a 1 to 2 week period. This causes Hisao and Hanako to spend substantial amounts of time together."
    
    #n "When Hisao visits Lilly in the hospital before the operation, she asks him to make sure to watch over Hanako for her. Hisao promises to do so."
    
    #n "This also means that the trio have to cancel Hanako's surprise karaoke birthday party. Her birthday passes while Lilly is in the hospital."

    n "Hanako begins to grow slightly more confident over time, somewhat unlike her breakdowns and seclusion in her Final route."
    
    n "\n\nThe Act begins a few days after Lilly's initial hospitalization. Hisao is studying in his room after a few days of restlessness."
    
    #n "Yuuko no longer works as the school's librarian and is replaced. She does still work at the Shanghai, however."
    
    #n "There is a confrontation between Hisao and a wheelchair-bound boy in the cafeteria. Shizune intervenes."
       
    #n "The act opens as a continuation of a missing library scene."
    
    #n "Hisao has just reached out to help Hanako up from her usual reading spot. Hanako is surprised due to something Hisao says/offers just before the scene begins."
    
    #stop movie
    #hide movie
    
    nvl hide dissolve

    nvl clear

label en_H14b:

    window hide

    nvl show dissolve
    
    n "Events leading up to the Bad Endings:"
    
    n "NOTE: The bad endings currently have no art or scene direction."
    
    n "Hisao begins to have adverse reactions to his medications, including phantom visions and fatigue."
    
    n "He decides to not take his medication before going with Hanako and Lilly to the Shanghai, hoping to avoid suffering more side effects before he can talk with the nurse about changing medications."
    
    n "As the trio are eating, a group of younger kids comes into the Shanghai and they begin to give Lilly and Hanako unwanted attention."
    
    n "Hanako begins suffering a breakdown, and as Hisao tries to take her outside, the kids see her scarring. They begin to call the girls freaks, causing Hanako to become even more upset and run away."
    
    n "Hisao runs after her, but begins to suffer from a heart attack. He collapses on the ground, the world fading around him as Hanako runs back to him."
    
    n "The last thing that he remembers is Hanako pounding her fist into his chest in an attempt to keep him alive."
    
    nvl hide dissolve

    nvl clear
    
    return