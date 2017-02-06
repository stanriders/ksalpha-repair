label en_L13:

    scene bg school_dormhallway
    with locationchange

    "As Lilly and Hanako follow me to my dorm room, I'm sweating bullets."

    "This'll be the first time they, and indeed anyone other than Kenji, has been inside."

    "Though Kenji's entrances are more often than not just thinly-veiled excuses to check my science notes."

    "Truth be told, I really don't have any reason to be so nervous."

    "I keep my room reasonably clean, though as much from only having been in there less than a month as any sense of cleanliness, I don't have any hidden porn stashes like a certain bespectacled hallmate, and I don't have any garish posters to speak of."

    hi "Well, this is it."

    "I rest my hand on the doorknob, waiting for the two girls, arm in arm, to catch up."

    play sound sfx_dooropen

    centered "*Clink*"

    scene bg school_dormhisao
    with locationchange

    hi "Welcome to my humble abode."

    show lilly cane_smileclosed at twoleft
    show hanako basic_smile at tworight
    with charaenter
    
    "I give a deep bow and gesture for the two to enter, both giving a polite nod as they pass."

    "Hanako's head almost seems to twitch as she looks around the room, taking in every small detail as if she were examining a crime scene."

    ha "It's… pretty."

    play sound sfx_doorclose
    
    "With a small clunk, the door closes behind us."

    hi "I've hardly changed it since I moved in, so it's still kind of bare."

    "She shakes her head vigorously."

    ha "No, it's nice."

    "I can only give a short nod of appreciation as I scratch the back of my head nervously."

    hi "You can sit on the bed if you'd like, I've only got one chair right now."

    show bg school_dormhisao at right
    with locationchange
    
    show hanako basic_smile at right
    with charamove
    
    show lilly basic_smileclosed at tworight
    with charamove
    
    "Heeding my directions, She and Lilly make their way to the blanket-covered bed, Lilly gently running her free hand along the wall as she goes."

    show lilly basic_smileclosed at tworightsit
    with charamove
    
    "As her hand finds the bed-end, she unloops her arm from Hanako's and takes her seat."
    
    show lilly basic_smile at tworightsit
    with charachange
    
    li "My my, Hisao. This is a nice room."

    hi "Ah, thanks."

    "Considering she's only seen one wall and the end of the bed, using a generous definition of seen, her comment seems to come more from politeness than honesty."

    "I can't exactly fault her for it, though."

    "I grab the chair from the writing desk beside my bed and take a seat as I turn it towards the two."

    hi "At least it's cooler in here."
    
    show lilly basic_weaksmile at tworightsit
    with charachange

    li "Indeed. The forecast says it'll be even hotter tomorrow, unfortunately."

    hi "Just what we need, more heat."

    "As I slump back into my seat, the white bag on my desk catches the corner of my eye."

    hi "Ah, that's right."

    show lilly basic_surprised at tworightsit
    with charachange
    
    li "What is it, Hisao?"

    hi "Here. This is for you."

    "I gently pick the small brown box out of the bag, placing it into the pale hands resting on her lap."

    hi "Happy birthday, Lilly."

    ha "Happy birthday!"
    
    show lilly basic_cheerful at tworightsit
    with charachange
    
    hide hanako

    li "Thank you Hisao, Hanako. I wonder what this could be?"
    
    show lilly basic_listen at tworightsit
    with charachange

    "She slowly lifts the box to her face, running her fingers around the outside and over the intricate designs on the wooden faces. As she does, her thumb suddenly pauses as it feels the bottom."

    "Tracing out the engraved shapes on the brass plate, she silently mouths the letters as she passes over them."

    show lilly basic_smileclosed at tworightsit
    with charachange
    
    "A small smile develops as she resumes running her index finger over the top, feeling out the line between the lid and the box itself."

    "No effort is needed for her to pop open the lid, with her expertly pushing it up with her thumbs."
    
    play music music_musicbox #fadein 10.0
    
    show musicbox open at center
    with charaenter
    with Pause (1.0)
    
    window hide
    
    #Pause, extreme close-up CG of just her face and the music box, with her watching the music box as it plays the tune. Possibly a graphical effect to simulate the cylinder and pins inside moving as well.

    #Maybe remove the textbox and text for a while, so there's just the CG and the music box sound

    with Pause(10.0)
    
    show lilly basic_surprised at tworightsit
    with charachange

    "For what could be as easily hours as seconds, the only sound in the room is the gentle melody playing from Lilly's hands."

    "Lilly's unseeing eyes seem, for a fleeting moment, to be taking in the sight of the small pins playing their tiny tune."

    "Her expression seems completely blank, wholly absorbed in this small musician performing in her snow-white hands."

    "Hanako and I look on silently, as focused on Lilly as she is on the small music box."

    "As the tune finishes, she gently closes the lid and lowers her hands to her lap."
    
    stop music fadeout 2.0 # [str]
    
    hide musicbox
    
    show lilly basic_pout at tworightsit
    with charachange
    
    "On her face is an expression of seemingly contradictory calmness and slight surprise."

    "I can't help but smile."

    "She likes it."

    hi "The Saraband. The music of our meeting."
    
    show lilly basic_reminisce at tworightsit
    with charachange

    "Another silence. No words are needed to see her playing the music once again in her head."

    "For a brief second, she seems to all but lose herself in another world."

    "Wait, what the—" #reminder for the potential {nw} break

    "If I hadn't been watching her so intently, I would have missed it entirely."

    "A face of melancholy."

    "A flicker of sadness that lasted less than a second."

    "A wound opened, and sewn shut in as much time."

    "Before I can react, she takes a breath, her expression returning to normal."

    show lilly basic_smileclosed at tworightsit
    with charachange
    
    li "Thank you, Hisao."

    "The delicateness of her voice gives me a weak smile."

    "There is nought but honesty in it, spoken without so much as a thought."

    "I'm completely lost for words."

    hi "It's nothing."

    "…"

    "Silence."

    "Nothing quite seems appropriate to say afterwards, for any of us."
    
    show lilly basic_surprised at tworightsit
    with charachange
    
    with vpunch

    ha "Ah!"

    "Both Lilly and I suddenly jump at Hanako's uncharacteristic outburst."

    hi "What is it?"

    ha "C—Cake!"

    hi "Cake! Yes! Cake! I'll get the cake!"

    "It may not have been the most gracious silence-breaker, but it was certainly effective."

    "I quickly spin the chair around and stand up, bringing my arms out to grab the cake sitting on the desk."

    "To be honest, it had been a last-minute oh-no-I-almost-forgot purchase, but thankfully they still has a couple of mudcakes in stock."

    "In no time, the cake's sliced, candled and on our plates."

    scene black
    with dissolve

    scene bg school_dormhisao
    with shorttimeskip

    "Considering how big it looked, it was surprisingly easy to finish off."

    "Though the taste probably played a far from trivial role in that."

    "As we lick the last of the icing from our fingers, now well and truly filled, we all slump back in contentment."

    "Even the usually elegant and composed Lilly's lazily leaning back against the wall as she sits on the bed."

    hi "Phew, that was filling."

    li "Indeed. That was a nice choice, Hanako."

    "As I give a thankful smile to her, she looks down and blushes slightly."

    "It's not hard to see the happy look on her hair-covered face."

    "Suddenly, the door to my dorm room flies open just as I begin to open my mouth."

    yu "Good evening, everyone!"

    "Yuuko loudly announces her sudden presence to everyone's surprised faces."

    "Dressed in her usual get-up with a dark-green jacket over the top, my mind struggles to comprehend why this girl is suddenly in my room."

    hi "Yu… Yuuko!?"

    yu "Happy birthday, Li~lly!"

    "She seems unusually happy, all of us quite speechless at her entrance."

    "Hold on, she's carrying a rather conspicuously bulging plastic bag in her hand."

    "And not only that, but there's with several bottle necks clearly visible through the top…"

    li "Ah, th—thank you, Yuuko."

    "Lilly's normally composed face is all but shattered."

    "As she proudly marches over to where we're sitting and sits herself down on the floor between us, the bag thuds to the ground beside her with an audible clank of glass bottles."

    yu "So? Aren't you happy to see me?"

    hi "Um… Yuuko…"

    yu "Yeah?"

    hi "Didn't you say university was holding you up from coming?"

    yu "I was late to the lecture and the professor wants my neck. I'm going to fail the course!"

    "Despite saying this, her delighted expression still holds. A quick sniff's all that's needed to know why, unfortunately."

    "I can definitely detect a faint whiff of a familiar scent on her breath."

    hi "Have you been drinking?"

    yu "Yup!"

    "She grabs into her bag and one-by-one grabs the bottles from inside."

    "As she does, our jaws slowly drop open."

    "Some kind of white wine. The price tag, still stuck to the bottle, doesn't bode well for its quality."

    "Vodka. A brand so cheap even I know it's barely drinkable."

    "After unpacking a final bottle, a golden-brown rum, all Hanako and I can do is stare speechless at the small pile of alcohol on the floor between us."

    hi "Y—Yuuko…"

    yu "Yeah?"

    hi "This is…"

    yu "I brought enough for everybody! It's her birthday, ainnit?"

    hi "That's not the point! Alcohol's not allowed in the dorms!"

    "My voice is higher-pitched than I've ever heard it before, in the throes of entirely unhidden panic."

    "As I say that fateful word, Lilly suddenly freezes in realization."

    li "Alcohol? Yuuko! You know—!"

    yu "Come on, it's your birthday, loosen up a bit~!"

    "Damn, she's drunken more than I thought. This new, brazen nature of hers can't be the result of anything else."

    "Suddenly, my mind gets back into gear."

    hi "Yuuko, how did you know we'd be here?"

    "Hanako and Lilly go distinctly silent, their stares aimed directly at her."

    yu "I went to Lilly's room and knocked but there wasn't an answer, so I guessed everyone must've gone to your room."

    hi "How did you find my room though?"

    yu "Hmm? Oh, yeah, I asked a couple of students for directions. Seems you're quite famous."

    hi "Famous?"

    "There are quite a few terms fit to describe me; “manly,” “brave” and “handsome” being amongst them."

    "…Well, maybe not, but I can't say “famous” comes to mind either."

    yu "They knew your name right away. I just said “Hey, you know where Hisao's room is?,” and one of 'em told me right off the bat."

    "“One of 'em?”"

    "On no."

    "Oh hell no."

    "No, no, dear God, no."

    "I shake my head to try and force my way through the DANGER, DANGER, DANGER signals flaring up through my head."

    hi "Okay, Yuuko, please answer this very, very carefully."

    "I stare at her intensely, causing her to rock back slightly in surprise."

    hi "Think. What did these girls look like?"

    yu "Hmm… Let me see, there was one wierd quiet one who had short hair and glasses, and a taller one that had really crazy hair. It was actually kinda cool, really."

    #Hana, Lilly SHOKKU faces

    "My jaw drops open as my mind hangs a “Sorry, We're Closed!” sign up."

    "An awkward silence fills the room, none of us able to utter so much as a mumble."

    "We're screwed."

    "We're completely and utterly screwed."

    "Even if they don't tell anyone, they're going to make me their slaves."

    "In fact, I'd probably prefer being at the mercy of the principal than those two."

    yu "Eh? Eh? W—what's wrong?"

    "Her head turns from person to person, her face completely blank."

    yu "Hisao? Hanako? Lilly? Anyone?"

    "I collect myself and bury my face in my palm, my elbow planted on the arm of my chair."

    hi "Hey, Yuuko."

    yu "Yeah?"

    hi "Pour me a glass. Vodka. Straight."

    ha "Me too."

    li "Three."

    yu "Now there we go! Now let's drink to life's failures and Lilly's birthday!"

    "As I unprofessionally down a shot poured by Yuuko, I glance forwards at Lilly."

    "What an awful way to spend a birthday."

    "*gulp*"

    scene bg school_dormhisao
    with shorttimeskip

    yu "And this Marius guy's all “We need a solid army!” but the senate's like “Nooooooo” and he gets all the…"

    "I stare blankly at Yuuko with a slightly flushed face as we sit facing each other on the hard floor."

    "I can't help but wonder how many people through history have been on the receiving end of a drunken tirade about ancient Roman politics."

    "To be honest, I'd probably find it quite interesting if I weren't tired, depressed, on the verge of drunkenness, barely able to understand her heavily slurred speech and being assaulted by her alcohol-laden breath with every word."

    "I suddenly jerk out of my thinking as she slams a shot glass onto the ground in front of me."

    yu "And BAM!, he takes out the Gauls just like that. And that's my speech on Gayus Mayrioos, thank you, thank youuuuu—" #reminder for the potential {nw} break

    "And with that, she falls forward onto the ground in the middle of a sitting bow."

    "Thank god for that."

    "Savouring the newfound quiet, I massage my temples."

    "Glancing around the room, Hanako's out cold and peacefully sleeping on her side with her hand as a pillow."

    "The well and truly empty wine bottle lays hapazardly on the floor like unwanted rubbish, the vodka bottle not far away."

    "As hard as Hanako and Yuuko tried — and try they did — they couldn't finish off the rum standing upright between them like the victor of an epic battle."

    "A small groan above me reminds me that Lilly retired to rest on my bed for a bit a few minutes ago."

    "Almost completely devoid of energy, I only just manage to stand up and drag myself to the side of the bed, sitting down and leaning my back to it."

    hi "Good God."

    li "Eugh…"

    hi "Too much to drink?"

    li "My head hurts."

    hi "Yeah, too much to drink."

    "I rest my head back and idly stare at the ceiling. Jesus. What an unmitigated disaster."

    hi "Hey, Lilly."

    li "Yes, Hisao?"

    hi "I'm sorry about today. I wanted to make this birthday special for you, but things kind of… went weird."

    li "It's fine, Hisao. To tell the truth, I had a lot of fun today."

    hi "Really?"

    li "Mmm. I think Hanako and Yuuko did too."

    hi "Hah, that they certainly did."

    "Another groan resounds from the lying Lilly."

    hi "You okay?"

    li "As you said, I just drank too much. What's the time?"

    hi "The time? Uh, it's…"

    "I quickly look over to the digital clock beside my bed, its bright red numerals uselessly beaming at Lilly."

    hi "About twelve."

    li "Curfew's in effect, then."

    hi "Yeah, I guessed as much. You guys'll have to sleep here for tonight."

    "As soon as I say it, I hear the sheets moving as Lilly starts to sit up."

    hi "Ah, no, it's okay, you can use my bed."

    li "Hisao, I couldn't possibly…"

    hi "You're in worse shape than me by any stretch. Get some rest."

    li "But what about…"

    hi "I'll grab some spare blankets and put them over them, don't worry."

    "As I give a deep yawn and stand to retrieve them, I hear her lie back down with a soft thud."

    li "Thank you, Hisao."

    hi "No problem, it's the least I can do."

    "With that, I grab a couple of blankets rolled up at the end of my bed."

    "Quietly walking over to Hanako and then Yuuko, I carefully lay the blankets over them making sure not to wake them up."

    "Though, the thick smell of alcohol coming off their breaths makes me doubtful they'd wake up no matter what I did."

    "I stand and take one last measure of the room."

    "Three girls, all pissed as newts, sleeping overnight in a male student's dorm. What a scandal that'd be if it broke out."

    "I suppose I'll grab Misha and Shizune tomorrow and apologise. While they may take pleasure in finding out even the most banal facts on every student in the school, they don't seem the type to tell tales for no reason."

    "At least, that's what I hope."

    "As I move to sit back down at the side of the bed, I steal one last glance at Lilly."

    "Her sprawling, disheveled figure lies sleeping peacefully, slightly turned to the side."

    "I crouch down to get a better look."

    "Her porclain skin blends in with the white sheets of the bed, a look of slumber-born peacefulness on her face."

    "Usually she seems so confident and forward, always there and caring for Hanako."

    "Now though, she seems painfully delicate."

    "The look she had when listening to the music box floats into my mind."

    "I thought it'd be a nice gift, but I'd hardly expected it to be so moving for her."

    "One birthday after another. Just she and Hanako."

    "Maybe it wasn't the music box she liked."

    "Resigning myself to an uncomfortable sleep, I sit down at the side of the bed once again and rest my tired arms beside me."

    li "Hey, Hisao."

    "Lilly's voice is so quiet I can barely hear it."

    hi "Yeah?"

    li "Thank you."

    hi "Thank you? For what?"

    li "The present."

    hi "Ah."

    "I take a deep sigh, smiling deeply."

    hi "I'm just happy you like it."

    "As I hear a deep breath, it's obvious Lilly's gone to sleep."

    "After closing my eyes, it doesn't take long for sleep to take me as well."

    scene black
    with dissolve

    return

label en_L14:

    scene black

    li "Hisao! Hey, Hisao!"

    li "Hisao!"

    "The whispering voice smashing through my head like a piledriver awakens me from my drunken slumber."

    hi "Huh?"

    scene bg school_dormhisao
    show lilly superclose
    with openeye


    #with openeye_shock

    "Without thinking I suddenly jolt forward, Lilly's face mere millimeters away from mine."
    
    #Should this be before or after the doublespeak? Review
    show lilly superclose_shock
    with Dissolve(0.2)
    
    $ doublespeak(hi, li, "Gyah!", "Ah!")
    
    
    play sound sfx_impact2
    
    show lilly superclose_ouch
    with vpunch
    
    hi "W—Woah!"

    "The impact of our foreheads causes both of us to fall backwards yelp in pain, Lilly sounding more like a squeak toy than a person."

    show lilly basic_concerned at left
    with Dissolve(0.2)
    
    hi "Ow, ow, ow."
    
    play music music_happiness fadein 6.0

    "Massaging my sore forehead with my hand, I look to Lilly."

    "On the floor in front of me in almost an exact mirror of my position, her face is obviously pained."

    hi "You okay Lilly?"
    
    show lilly basic_concerned at left
    with charachange
    with Pause(0.5)

    li "I think so, I think most of the pain right now is from the hangover."
    
    show lilly basic_sad at left
    with charachange

    hi "Hangover?"

    "I suddenly remember the disasterous events of last night."

    "As I do, I suddenly realise I feel surprisingly fine."

    hi "Ah, yeah. Looks like I managed to dodge that bullet at least."

    show lilly basic_surprised at left
    with charachange
    
    li "Oh? It seemed you were partaking of the vodka quite heartily."

    hi "There's one advantage to vodka. It may taste awful, but it can be diluted down to nothing."

    show lilly basic_giggle at left
    with charachange
    
    "Her pained look gives way to an amused grin."
    
    show lilly basic_planned at left
    with charachange

    li "You have my respect Hisao, that was quite the act of quick thinking."

    "Allowing myself the luxury of a quick grin, I stand up and shake off the last vestiges of sleep."

    hi "Need a hand?"

    li "If you would be so kind."
    
    show lilly basic_cheerful at left
    with charachange

    "I reach down and grasp Lilly's outstretched hand, giving a slight heave as she gets up."

    stop music fadeout 10.0
    hi "Woah!"

    "As she does she stumbles dangerously I quickly move forward to stop her from falling, grabbing her in my arms as she stumbles forward."
    
    #I want a CG here
    
    show lilly superclose_ouch
    with charachange
    
    hi "Ah…"

    li "…"

    "Seconds pass as as I awkwardly hold her chest to mine, her head above my shoulder."

    "Every muscle in my body is tense, and my mind entirely blank."

    "Both of us stand rigid, unable to say so much as a word."

    hi "U… U—Um…"
    
    show lilly basic_surprised at twoleft
    with charachange

    "Without a word, she silently pulls herself from my relaxed grasp and stands herself straight."
    
    show lilly basic_emb
    with charachange

    "As she averts her gaze, I only catch a glimpse of her blushing face before she lowers and turns it away."

    "What's written on it doesn't quite look like embarassment, though."

    # I need a kind of "hiding and lowering face" sprite. Both for this scene and a fair few others in act 3. From memory, Hisui in Tsukihime has a sprite very close to what I'm thinking of.

    show lilly basic_reminisce
    with charachange
    
    li "I'm… sorry."

    hi "Hey, it's just the hangover. It's fine."

    li "I'm sorry. I'm really, really sorry."

    "I lower my brow, out of both worry and mild surprise."

    "She doesn't often catch me off-guard, but this is one of those moments."

    hi "Uh… okay. I guess. Um, what were you wanting to say before?"
    
    show lilly basic_sad
    with charachange
    
    li "Hmm?"

    "Her face lifts a little in thought before turning back."

    show lilly basic_reminisce
    with charachange
    
    li "Oh, ah, I can't hear someone."

    hi "Can't hear—" #reminder for the potential {nw} break
    
    show bg school_dormhisao at bgright
    show lilly basic_reminisce at center
    with charamove
    
    show bg school_dormhisao at center
    show lilly basic_reminisce at twoleft
    with charamove

    "I quickly take a look around the room, reminded that, yes, there are other people in the room."

    "Hanako lies resting where she was, miraculously unawakened by our noise."

    "All that lies where Yuuko was though is a neatly-folded blanket and a small note, folded in half and sitting tidily on the neatly folded mound."

    hi "Looks like Yuuko's left."

    "I bend down to grab the note, blinking the last of the sleep out of my eyes."

    "The handwriting's spectacularly neat and easy to read, with a small caricatured smiling face at the bottom of the text."

    # Centered and all on the screen at once with this formatting, or as part of a CG that's just got the note in Hisao's hand.
    
    hide lilly
    window hide
    
    $ fixedwritten_note(u"Hey Hisao,\n\nI'm really, really sorry about last night. I really made a mess of things, didn't I?\n\nI've taken all the bottles and cleaned up the spills, so don't worry about any incriminating evidence. I'll make sure not to draw attention to myself on the way out too.\n\nRegards,\nShirakawa Yuuko\n\nPS. If you need a favour, call me. The phone number's on the other side of the note. {image=vfx/smiley.png}")

    window show
    # End note

    "After a quick check to see the number on the other side, I smile and place the note on my desk."

    "I guess Yuuko isn't such a bad person after all."

    show lilly basic_concerned at twoleft
    with charachange
    
    hi "She left a note. It says she's taken all the bottles and snuck out of the dorms."
    
    show lilly basic_smileclosed
    with charachange

    "Lilly gives a deep, relieved sigh."

    li "Thank goodness. She may drink every now and then, but that's the first time I've seen her go that far."

    hi "Either way, she's apologised for last night."

    li "I had little doubt she would."

    hi "You know, you seem to know her pretty well."

    li "Hmm, let me see here…"

    show lilly basic_displeased
    with charachange
    
    "She pauses a moment, furrowing her brow in thought."

    show lilly basic_weaksmile
    with charachange
    
    li "I met her not long after I met Hanako, and she did introduce herself rather… bluntly."

    "I give a slight chuckle at her glossing over of the event."
    
    hi "That's one way to put it."
    
    show lilly basic_reminisce
    with charachange
    
    "Cradling her head in her hand once again, Lilly grimaces."

    hi "Hangover's biting you in the ass?"
    
    show lilly basic_pout
    with charachange

    li "…Not exactly eloquent, but correct."

    hi "Here, sit on the side of the bed."
    
    show bg school_dormhisao at bgright     #with charamove
    show lilly basic_sleepy at centersit
    with charamove
    
    "Taking one of her hands to guide her over, she turns and sits on the side."

    "I return to sitting where I'd been sleeping before, her stocking-covered legs dangling on the left edge of my vision."

    "Looking over to the clock, I'm unsurprised to see we've slept through my alarm."

    hi "Well, there goes school. It's already nine thirty, and you two're in no shape to go to class."
    
    show lilly basic_surprised at centersit
    with charachange

    li "Mm, you have a point. I guess I did drink a little too much."

    "Thinking back, she drank almost the entire wine bottle by herself."

    "Compared to Hanako and I, she has quite the alcohol tolerance."

    "Yuuko though… Half the vodka, a quarter of the rum, and about a quarter of the wine as well."

    "It's no wonder she ended up completely drunk and singing alongside the rather carefree Hanako."

    "It'd have been quite the sight if Lilly and I hadn't needed to continually quieten the two down lest others hear the drunken racket."

    show lilly basic_weaksmile
    with charachange
    
    li "It seems Hanako's sleeping."

    hi "Yeah, like a log. I'm surprised how well she got on with Yuuko last night."
    
    show lilly basic_giggle
    with charachange

    li "Well, she and Yuuko know each other quite well."

    hi "Not to mention the vodka she drank."

    li "That too."

    "I take a moment to lazily stare at the peacefully sleeping Hanako."

    hi "At least she looks peaceful."
    
    show lilly basic_smileclosed
    with charachange

    li "Thank you, Hisao."

    hi "Again? For what?"
    
    show lilly basic_smile
    with charachange

    li "You've been a good influence on my dear Hanako."

    hi "A good influence… you say?"
    
    show lilly basic_cheerful
    with charachange

    li "Mm. Thanks to you she's become much more confident."

    "I turn up to look at her, my face distinctly flat."

    hi "She doesn't seem that confident."

    "She shakes her head vigorously"

    show lilly basic_concerned
    with charachange
    
    li "Before you came, it wouldn't be unusual for her to skip class out of fright, or recoil away from anyone who even glanced at her."

    hi "Uh… huh."

    "Thinking back to the meeting at the cafe and our trip through town, she does seem less skittish around others."

    "Though around me she still struggles to say so much as an unbroken sentence."

    "I guess shyness is just a part of her personality."

    "Even as I grimace though, Lilly gives a deep, warm smile."

    show lilly basic_smile
    with charachange
    
    li "Thank you, Hisao. She may seem somewhat shy at times, but you've helped her so much."

    hi "Ah… t—thanks."

    "I look away from her kind face, suddenly feeling more than a touch embarassed."

    # Centered, with SFX

    play sound sfx_doorknock
    #centered "*thump* *thump* *thump*"

    hi "Looks like someone's at the door."

    li "Were you expecting anyone?"

    hi "Nah, it's probably just Shizune and Misha coming to see what's up."

    show bg school_dormhisao at bgleft
    show lilly invis at leftsit
    with dissolvecharamove
    
    #hide lilly
    
    "I grunt and stand myself up, walking over the the door."

    "I guess they must already know that Lilly and Hanako are in my room."

    "With a short creak, the door opens easily."

    # Show Kenji sprite
    
    show kenji neutral
    with charaenter
    
    hi "Hey Shi—{w=0.1}{nw}" #reminder for the potential {nw} break

    "Uh-oh."

    "I quickly move my body slightly to the left to block off Kenji's view of the room."

    "Not that he'd be able to see anything past my face anyway, I guess."

    hi "Ah ha, hey Kenji. What's up?"

    ke "Hey man. You have my CD still."

    hi "Ah yeah, it'd still be in my laptop. Hold on and I'll grab it for—" #reminder for the potential {nw} break

    "I suddenly freeze."

    "Stall Hisao, stall!"

    hi "Ah… um…"

    "My mind finally manages to remember the time."

    hi "Hey, uh, what're you doing here at this hour anyway? Shouldn't you be in class?"

    show kenji happy
    with charachange
    
    ke "Nah man, I just got held up a bit. It's cool."

    "I raise an eyebrow at his oddly upbeat nature."

    "I guess there's no other route but to hope he just plain old doesn't see the two girls."

    hi "Uh huh. I'll go grab that CD then."

    "I turn around and stiffly walk out to my desk, nervous as hell about the figure striding in behind me."

    ke "Hey man, what're you doing out of class anyway?"

    "Damn, he has a good point."

    show bg school_dormhisao at center
    show lilly basic_surprised at twoleftsit
    show kenji happy at tworight
    with dissolvecharamove
    
    "As I turn around and rush to throw up an excuse, a voice suddenly beckons from the bed on my left."

    li "My my, is that Kenji?"

    show kenji surprised
    with charachange
    
    ke "Huh?"

    "A few second's silence passes as he tried to place her voice."
    
    show kenji neutral
    with charachange
    
    ke "Oh. Lilly. Hey."

    "Wow, don't show too much enthusiasm there bud."

    hi "You two know each other?"

    "They both turn to me in unison."

    li "Kenji and I are in the same class."

    hi "The same… Well, that makes sense I guess."

    show lilly basic_sleepy at twoleftsit
    with charachange
    
    "Leaving the two to talk between each other, I lean forward and turn the laptop on to eject the CD."

    "…"

    "Apparently the two don't have much to talk about."

    "As an uncomfortable silence fills the room, I can almost feel the waves of irritation being emitted from Kenji."

    "That guy has problems."

    "Finally the laptop finishes logging on. Seizing the opportunity, I quickly eject the CD and pass it to him with the speed of an enraged bull."

    hi "There you go, as good as I got it."
    
    show kenji happy
    with charachange
    
    ke "Thanks man."

    "As he starts to move off, a sudden and rather unwelcome voice comes from the floor."

    show hanabad defarms_worry at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.60)
    with charaenter
    
    ha "Huh?"

    "I look downwards at the once-sleeping figure on the floor, my jaw dropping."

    ha "Lilly? Hisao?"

    "As she groggily props herself up and whipes the sleep out of her eye, I frantically turn to Kenji."
    
    show kenji surprised at tworightsit
    with dissolvecharamove
    
    "Crouching down to rather uncourteously survey her face, his breath catches as she opens her eyes."

    ha "Eh? A—AAAAAAAH!"

    # Centered, with SFX
    #centered "*Thump*"
    play sound sfx_pillow
    with vpunch

    "The two's foreheads slam together with a surprisingly amount of force."

    show hanabad emb_downtimid_cry at centersit
    show kenji tsun at right
    with dissolvecharamovefast
    
    "Kenji's sent reeling backwards as Hanako lowers her blushing face and rubs her forehead."

    ha "Ah! U—u—um, s—sorry! Sorry!"

    ke "Ah, shit, shit, shit."

    li "Ah, are you two alright?"

    ha "I—I—I'm fine."

    ke "Ah shit, my head…"

    hi "That was your fault, dude."

    ke "Damn, she didn't have to headbutt me."

    hi "I'd do—{w=0.25}{nw}" #reminder for the potential {nw} break

    "Well, did{w=0.25}{nw}"

    hi "—the same thing if I were in her position."
    
    show hanabad emb_downtimid_cry at center
    with charamove

    "He takes a moment to regain his composure as Hanako stands up and starts bowing frantically."

    ha "I'm sorry! I'm sorry! I'm sorry!"

    hi "Hanako, stop apologising. He should be the one doing it."

    "I draw a flat look from him."

    "While distinctly unimpressed by my defense of Hanako, it seems as if he's ready to conceed the point."

    ke "Sorry. Sound girl."

    "He practically mumbles it, though all of us just manage to hear."

    ha "Ah, th—that's fine. Um, sorry."

    "I rub my eyes in confusion."

    "Amazingly, he doesn't seem to click that I have two girls in my room for no explained reason."

    hi "Wait a minute, “sound girl?”"

    ke "Well if you have a name for her…?"

    hi "Don't ask me as if she were my pet, dude."

    ha "H… Hanako."

    "Her unexpected response silences the room completely."

    "Unfortunately the deafening silence only serves to further redden her already blushed and hidden face."

    hi "Uh, yeah. Hanako."

    "He adjusts his glasses in a futile attempt to get a better look."

    ke "So you're that girl who Lilly's with all the time."

    ha "…Mmm."

    "A slight nod and almost inaudible response are all she gives."

    ke "Whatever. I'm out of here."

    "As he turns to leave, I breath a sigh of relief."

    "That is, until he look back to me and opens his mouth."

    ke "Hey man, what're you doing with two girls in your room anyway?"

    "His extremely accusative voice kills any hope I had for an easy exit."

    "Come on, I can think of something…"

    hi "They…"

    li "Ah, I was just accompanying Hanako, who'd come to get some science homework from Hisao to give to Mutou. He has a cold at the moment, so he's off class."

    "He eyes her suspiciously, shrugging dismissively."

    ke "Whatever."

    "Thank god."
    
    show bg school_dormhisao at bgleft
    show lilly invis at leftsit
    show hanabad invis at twoleft
    show kenji neutral at center
    with dissolvecharamove
    
    "He turns to leave, with me following him out and taking a hold of the door behind him."

    "He fires off a last hit before walking off."

    ke "Be on your toes, man."

    hi "On my toes?"

    ke "On your toes. Seeya."

    hide kenji
    with charaexit
    
    "And with that, he walks off, seemingly ignoring my thoroughly perplexed expression as I shut the door."
    
    show bg school_dormhisao at center
    show lilly basic_smileclosed at twoleftsit
    show hanabad emb_downtimid at tworight
    with dissolvecharamove
    
    "As I walk back in, I see Hanako folding her blanket and Lilly still sitting on the side of the bed."

    hi "That guy's got problems."

    li "He is somewhat introverted."

    hi "I think it runs deeper than that. Oh, Hanako, don't worry about the blanket. I'll tidy it up later."

    ha "Ah… okay."

    li "Shall we be off then, Hisao?"

    hi "As much as I'd like for you to stay, it's probably best if you leave while everyone's out of the dorms to avoid any more rumours flying about."

    li "And of Shizune?"

    hi "Don't worry, I'll catch up with her tomorrow. Going out to meet her today would be suicide."

    hi "Unless…"

    "Lilly cocks her head inquisitively."

    hi "Hey, do either of you know Misha's phone number?"

    li "Ah, I do."

    "I quickly pull top draw of my desk and grab my cellphone from inside."

    show bg school_dormhisao_blurred at bgright
    show phone mobile
    hide lilly
    hide hanabad
    with charaenter
    
    hi "Shoot."

    "Dialing in the numbers as she says them, I tense as the phone starts to ring."

    "How the hell can I explain this?"

    # Phone conversation.

    mi "Hello, this is Misha."

    "Wow, she sounds completely different on the phone. With such a polite and calm tone, if not for saying her name I'd have thought I'd called the wrong number."

    hi "Hey Misha, it's me."

    mi "Oh ho, so if it isn't the naughty, naughty Hicchan~"

    "Well, there goes that calm, collected image."

    hi "I heard everything. Uh, I should…"

    mi "Ah, hold on a moment, Hicchan."

    hi "Huh?"

    "From the silence at the other end, I guess she must be interpreting the phone conversation for Shizune."

    "Uncomfortable seconds pass."

    mi "Back!"

    hi "Uh huh."

    mi "Shicchan says…"

    "As I hear a near-missable sound of air intake from the speaker, I quickly dart the phone away from my ear."

    mi "WHAT THE HELL DO YOU THINK YOU'RE DOING, HISAO!?"

    "As I gingerly bring the phone back in, I suddenly find myself distancing myself from it once again."

    mi "WE HAD TO DO CROWD CONTROL FOR EVERY STUDENT THAT SAW THAT DAMN WOMAN! DO YOU KNOW HOW MUCH TROUBLE WE JUST SAVED YOU FROM!?"

    hi "Ah, I…"

    mi "Could you hold on a second?"

    "The sudden and total voice change takes me on the back foot, her sugary-sweet voice making me grimace deeply."

    hi "S… sure."

    "In the ensuing silence, I look up to Hanako and the now standing Lilly."

    "Both have somewhat pensive looks on their faces."

    mi "I'm ba~ck."

    hi "I see."

    mi "Shicchan said…"

    "I quickly push the phone out again as if it had suddenly tried to eat my ear."

    mi "AND ON TOP OF THAT, YOU DON'T TURN UP TO CLASS TODAY! ANY OF YOU! WHAT DO YOU HAVE TO SAY FOR YOURSELVES!?"

    "I sink my head low in genuine regret."

    hi "Um… sorry. I'll talk to you more when I see you in person, but thanks for covering for us. We appreciate it."

    mi "No problem, Hicchan~"

    "It's easy to see which person each statement comes from."

    mi "Oh? Shicchan… wants to talk to you?"

    "I raise an eyebrow, both at the rediculousness of the statement and Misha's unusually surprised voice."

    mi "Here, Shicchan."

    hi "Um… Shizu—{w=0.25}{nw}" #reminder for the potential {nw} break

    # End phone conversation

    "Before I can say another word, the phone hangs up."
    
    show bg school_dormhisao at bgright
    hide phone
    show lilly basic_listen at twoleft
    show hanabad emb_downtimid at tworight
    with charachange
    
    hi "Shit, she's not taking this well."

    li "She is covering for us though, as you said yourself."

    hi "Yeah, thank god. Once I talk to them tomorrow this whole mess should be cleaned up."
    
    show lilly basic_smile at twoleft
    with charachange
    
    li "Thank you, Hisao. Hanako, shall we be off?"

    "In all this fracas, I'd have forgotten Hanako to be there if she weren't standing before me she was so silent."

    ha "Mm."

    "Hooking around each other's arms, they start to move out."

    "I quickly walk ahead of them and open the door, giving a quick look down the hallway before they move out into it."

    hi "Well, I guess that's that."

    li "Indeed. Goodbye, Hisao."

    hi "Seeya Lilly, Hanako. I'll meet you tomorrow?"

    li "Mm, though I might be studying during lunch."

    hi "No problem. Bye."

    hide lilly
    hide hanabad
    with charaexit
    
    "With a quick wave, Hanako and Lilly set off down the hallway arm in arm."

    "After watching them walk for a quick couple of seconds, I close the door and lean against it in complete exhaustion."

    "Ah, my pills. I almost forgot."

    "As I walk to the bathroom, I take a much-needed yawn."

    "What a day."

    scene black
    with dissolve

    return

label en_L15:
    scene black with fade
    scene bg school_hallway3
    with shorttimeskip

    "I stand around the corner of the open door to the classroom, quiet as a mouse."

    "On the other side of this door will be Shizune and Misha."

    "I can feel my hands tightening from nervousness."

    "Dammit, what am I afraid of?"

    "They're just two girls, and reasonably logical ones at that."

    "Though coldly logical would probably be a better description."

    "With a deep breath, I turn the corner and confidently stride into the room. Even as I do, I feel as if I'm merrily waltzing into Hades itself."

    scene bg school_scienceroom
    with locationchange
    
    play sound sfx_dooropen
    
    show shizu basic_normal at right
    with charaenter
    
    show misha hips_smile at left
    with charaenter

    "As expected, Misha and Shizune are there, early as always, and standing at my desk waiting for me."

    hi "Hey Misha, Shizune."

    "I say the greeting with as much enthusiasm as I can muster, which is to say, not much."
    
    show misha hips_grin at left
    with charachange
    
    show shizu basic_frown at right
    with charachange
    
    show shizu cross_wut at right 
    with charachange

    "Shizune stares daggers at me as a wry grin forms on Misha's lips."

    "…This isn't going to be fun."

    mi "Good morning, Hicchan~"

    hi "I can explain, but first I want to talk to you."

    "First phase of Operation Dear-God-I-Don't-Want-To-Die: Divide the two and fight on single fronts."

    show misha hips_smile at left 
    with charachange
    
    mi "Hmm, what do you think, Shicchan?"

    show shizu basic_normal2 at right
    with charachange
  
    "A quick nod is the response. Evething's going just as planned."
    
    hide shizu
    
    show misha cross_smile_close at center
    with charachange
    
    "As Shizune turns her back on us, I lean in close to whisper with Misha and hide my mouth from Shizune with my hand."

    hi "So uh, how's she taking it?"
    
    show misha cross_grin_close at center
    with charachange

    "An obnoxiously wide grin"

    hi "That well, huh?"
    
    show misha hips_frown_close at center
    with charachange

    mi "You did put a lot of pressure on us, Hicchan. If anyone found out…"

    hi "Yeah. As I said on the phone, I'm really sorry."

    show misha perky_confused_close at center
    with charachange
    
    mi "You should really be apologising to poor Shicchan, she's the most ruffled."

    hi "And you?"

    show misha perky_sad_close at center
    with charachange
    
    mi "You're not children, Hicchan. I'm well aware of that."

    "My brow lowers."

    hi "You have the wrong idea here."

    show misha cross_grin_close at center
    with charachange
    
    mi "Hee hee, whatever you say, Hicchan~"

    hi "Eugh."

    "I lean back, content that she's only toying with me as she's so fond of doing."

    "As I begin to call Shizune, I suddenly realise the futility of doing so."
    
    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')

    play music music_shizune fadein 5.0
    
    show misha hips_smile at left
    with charamove
    
    show shizu behind_frown at right
    with charaenter

    "A quick tap on the shoulder from Misha though has her turn on her heels and eye me closely."

    "Uncomfortably closely."
    
    hide misha
    
    show shizu behind_blank at center
    with charamove

    "As if they were a well-rehearsed pair of secret agents, Shizune dismisses Misha with a quick sideways glance."

    "Before I can so much as open my mouth, Shizune's note book appears from seemingly nowhere."

    "Scribble, scribble. Scribble, scribble."

    "The pen scrawls its black ink onto the white page at lightening speed."

    # Centered
    
    show shizu behind_frustrated_close at center
    with charachange

    $ fixedwritten_note("Are you aware of the ten o'clock curfew?")

    "Direct, as always."

    "I doubt mincing words will work, so I resign myself to a matching level of conciseness."

    "I scribble my answer onto the small book and slide it over the side of the table back to her."

    # Centered

    $ fixedwritten_note("Yes.")
    
    show shizu behind_blank_close at center
    with charachange

    "Scribble, scribble. Scribble, scribble."

    # Centered

    $ fixedwritten_note("I take you're also aware that students are to be in their own dorms by said curfew, much less together with non-students?")

    "I give the pen a bit of a shake to get the ink flowing after coming up blank on my first attempt."

    # Centered

    $ fixedwritten_note("Yes.")
    
    show shizu behind_frustrated_close at center
    with charachange
    with Pause(2.0)
    
    show shizu basic_normal_close at center
    with charachange

    "As she begins to put pen to paper once again, she pauses and taps it against her cheek."

    "It only takes a couple of taps before her face lightens up, evidently working out what to say."

    "Scribble, scribble."

    # Centered

    $ fixedwritten_note(u"Did you do any… funny things?")

    "What?"

    "I raise an eyebrow and inadvertantly blurt out my thoughts."

    hi "You lost me."
    
    show shizu behind_blank_close at center
    with charachange

    "She looks at me flatly as she grabs the notebook back, writing slowly and deliberately before passing it back."

    # Centered

    $ fixedwritten_note("Did. You. Have. Sex?")
    with vpunch
    
    show shizu behind_frustrated_close at center
    with charachange
    
    "I suddenly jerk backwards and spray spit at the bluntness of her question."

    "Just how close are Shizune and Misha's thought patterns anyway?"

    "Looking back at her though, her stern expression still holds."

    "I rub my eyes and begin to give an answer."

    # Centered

    $ fixedwritten_note("No, I di")

    "Suddenly I come to my senses and put a line through the text, writing a new line below."

    # Both following lines centered, with a strikethrough through "No, I di". If that's not possible, just forget that line.

    $ fixedwritten_note("{s}No, I di{/s}\nI don't recall this being something that's the duty of a student council member to ask.")

    show shizu behind_frown_close at center
    with charachange
     
    "After reading what I've written, she looks up and gives an intense stare."

    "It takes a second for me to click what she means."

    "“I'm not asking this as a student council member, but as a friend.”"

    "As direct as she may be, she gets hung up on the most inane things sometimes."

    "I take the notebook back as I give a noncomittal shrug."

    # Centered

    $ fixedwritten_note("Don't worry, we didn't do anything weird. Unless you want an essay on ancient Roman politics, I'll leave out the details.")

    show shizu behind_sad_close at center
    with charachange
    
    "She takes back the notebook and reads it, raising an eyebrow."

    show shizu behind_smile_close at center
    with charachange
    
    "After a second's reflection, she looks up with a smile on her face and gives an accepting nod."

    "A sigh of relief."

    "I was an idiot to get so worked up about this, though that phone call didn't help."

    "Just as I begin to dwell, a familiar voice beckons from behind me."

    ha "Ah, Hisao?"
    
    hi "Hmm?"
    
    show bg school_scienceroom at bgright
    with charamove
    
    show shizu behind_smile at twoleft
    with charachange

    show hanako emb_blushtimid at rightedge
    with charaenter
    
    show misha hips_smile at left
    with charaenter

    "I turn to see Hanako walking towards us, her hands fidgeting constantly."

    "As she comes in beside me, I quickly put my right hand on the back of her head and bring her upper half down with mine as I bow to Shizune and Misha."

    hi "We're sorry. We're truly, truly sorry. It won't happen again."

    show hanako defarms_strain at rightedge
    with charachange

    ha "Ah, mm. I—It won't happen again."

    show misha hips_grin at left
    with charachange
    
    show shizu adjust_happy at twoleft 
    with charachange
    
    "I tilt my head upwards to see the two smiling."

    show misha hips_smile at left
    with charachange
    
    mi "Hmm, what do you say, Shicchan?"
    
    "Though one of her hands is on her hip, her smile's all that's needed as an answer."

    show misha cross_smile at left
    with charachange
    
    show shizu behind_smile at twoleft
    with charachange
    
    mi "Well, that's settled then!"
    
    show hanako basic_normal at right
    with charachange

    "Hanako and I right ourselves as she quickly brushes her skirt."

    mi "So, Hicchan…"

    hi "Yes?"

    show misha hips_smile at left
    with charachange
    
    mi "How bad was the hangover?"

    hi "Not too bad. Looks like Lilly bore the brunt of it."

    # Sprite change

    "…"
    
    show misha hips_grin at left
    with charachange
    
    show shizu behind_sad at twoleft
    with charachange

    "Misha's smile is as wide as ever as Shizune's faulters."

    mi "So, Hicchan. You did drink after all?"

    hi "…shit."
    
    show misha hips_laugh at left
    with charachange
    
    show shizu adjust_frown at twoleft
    with charachange

    mi "Wahahahahahaha~"

    "I bring my palm to my face in embarassment."

    "I suppose that makes the score two to zero, now."

    scene black
    with dissolve

    return

label en_L16:

    scene bg school_dormhisao
    with openeye

    "I open my eyes to another day and glance over to the glowing red numbers beaming at my face."

    #Is there an alarm clock sprite?
    
    "6:00"

    "Shit. Early."

    "Bloody nightmares."

    "Sitting up and shaking off the last of the night's less than wonderful dream, I give up on the prospect of going back to sleep."

    "Let's see, what to do…"

    "I guess there's not much else to do but finish off some of the science homework."

    "In fact, it probably would've been done by yesterday if not for my masterful procrastination."

    show bg school_dormhisao at bgleft
    with charamove
    
    "I wander over to my desk and pull the science sheets out of my bag."

    "Stoichiometry. Oh joy."

    "Well, I guess it needs to get done anyway."

    # Timeskip

    scene bg school_dormhisao
    with shorttimeskip

    "It doesn't take long for my brain to get focused on the task at hand, with the sheets being completed one by one."

    "Truth be told I prefer physics to chemistry, but neither are overly hard."

    "I guess as far as talents go it's pretty much my only one."

    # Door knocking SFX
    
    play sound sfx_doorknock

    #centered "*thump* *thump* *thump*"

    "The knocking at the door breaks me out of my concentration on the sheet in front of me."

    "Bah, it was boring anyway."

    hi "Right, right! I'm coming!"

    play sound sfx_dooropen
    
    show bg school_dormhisao at bgleft
    with charamove
    
    $ renpy.music.set_volume(1.0, 1.0, channel='music')
    
    play music music_kenji fadein 2.0

    show kenji happy at center
    with charaenter

    hi "Oh, hey."
    
    show kenji neutral at center
    with charachange

    "He pauses to adjust his glasses before speaking, making very sure that I understand he Means Business."

    ke "I'm hearing things man."

    hi "You should probably get that checked out."

    show kenji tsun at center
    with charachange

    "I get the feeling he's distinctly unamused by my attempt at humour."

    ke "I'm serious here. What's up?"

    hi "What's up? About what? What are you talking about?"

    show kenji surprised at center
    with charachange
    
    ke "The rumours, man. Don't tell me you haven't heard them."

    "I may not have my ear to the ground, but the fact that he's heard a rumour before I have is worrying."

    hi "No, I have not heard this rumour you speak of. What is it?"

    show kenji tsun at center
    with charachange
    
    ke "The two lovers having a little walk together at sunset?"

    hi "The two…"

    "The grocery shopping."

    "I probably should've anticipated the result of walking off together with a girl near so many other students."

    "On the plus side at least, the debacle of last week seems to have gone largely unnoticed."

    hi "How many people know this?"

    show kenji neutral at center
    with charachange
    
    ke "Not many."

    hi "Not many?"
    
    show kenji happy at center
    with charachange

    ke "Only those who'd take an interest in you."

    hi "And how many take an interest in me?"

    show kenji neutral at center
    with charachange
    
    ke "Not many."

    hi "I'm not sure whether to feel relieved or insulted."

    "Well, despite saying that, being but one student amongst many has its advantages."
    
    ke "Whatever."

    "I look flatly at him, taking the bridge of my nose in my fingers."

    hi "Yeah, right, anyway. Why are you bringing this up?"

    show kenji tsun at center
    with charachange
    
    ke "It's that Lilly girl."

    "He pauses, obviously waiting for me to urge him on."

    hi "Just say it and stop trying to be dramatic."

    "My attempt to break his pace draws an annoyed look once again."
    
    show kenji surprised at center
    with charachange
    
    ke "I don't know, man. Everyone knows she's filthy rich. She probably has Yakuza connections or some shit."

    show kenji happy at center
    with charachange
    
    ke "Wait, no, mafia. She's foreign, right? If she's foreign and rich I bet she has connections to the mafia."

    hi "You lost me."

    "Skipping right over my confusion, he barrels along with his rant."

    show kenji neutral at center
    with charachange
    
    ke "You don't want to get into that shit, dude. Concrete boots, bodies in trunks and all that. You know where she's from?"

    "Of course I do, she's…"

    "…"

    "Huh."

    hi "I… don't, actually."

    "I make a concious note to check with her sometime. Now that he brings it up, I wouldn't mind knowing myself."
    
    show kenji happy at center
    with charachange

    ke "Sicily. She has to be from Sicily. All those mafia types come from there. Wait, no, Russia. The mafia there is serious business man. Hardcore smuggling and—" #reminder for the potential {nw} break

    hi "Wait, wait, stop, just slow down a sec. What point are you trying to get at here?"

    show kenji neutral at center
    with charachange
    
    ke "You don't know what she'll do, man. I know what girls can do. You don't want to be a part of it."

    "And he goes and loses me again. I honestly think Rin's easier to understand than this guy at times."

    hi "Right. Thanks for the warning."

    show kenji tsun at center
    with charachange
    
    ke "You're not taking this seriously."

    hi "Oh, I'm taking it very seriously."

    "It takes all the resistance in the world not to say “Unlike you.”"

    hi "That's right, you're in Lilly's class aren't you?"

    show kenji surprised at center
    with charachange
    
    ke "Yeah, so?"

    hi "I'm surprised you haven't overheard anything about her."

    show kenji tsun at center
    with charachange
    
    ke "I don't eavesdrop man. I have standards."

    "Says mister “I steal books from the library.”"

    ke "Besides, she's the class representative. You know what that means?"

    hi "I have a feeling you're going to tell me."

    show kenji happy at center
    with charachange
    
    ke "She's in with them, man. The feminists. They pretend to be all cold to one another, but it's just a bluff. I'm on to them."

    hi "I should have known."
    
    show kenji neutral at center
    with charachange

    ke "Damn right you should've, you're the one getting all snuggly with her. Don't think I didn't hear that din coming from your room on Wednesday."

    show kenji tsun at center
    with charachange
    
    hi "…Shit."

    ke "Yeah."

    hi "How loud was it?"

    show kenji neutral at center
    with charachange
    
    ke "Loud."

    hi "This isn't good."

    show kenji happy at center
    with charachange
    
    ke "You were just playing my CD too loud, it doesn't matter."

    hi "But I… wait, what?"
    
    show kenji surprised at center
    with charachange

    ke "You were playing my CD too loud, remember? A couple of the guys down the hall almost came in to check before I told 'em."

    hi "You…"
    
    show kenji happy at center
    with charachange

    "He grins mischieviously as I stare at him in abject wonder."

    hi "I owe you one, man."
    
    show kenji neutral at center
    with charachange

    ke "I'm not going to let you forget that, you know."

    hi "Yeah, I know. Did you come here for any other reason, anyway?"

    show kenji surprised at center
    with charachange
    
    ke "Hmm? Oh, yeah, I need to borrow your English textbook."
    
    hi "Don't you have your own?"

    show kenji happy at center
    with charachange
    
    ke "I lost it."

    hi "You would."
    
    show kenji tsun at center
    with charachange

    "His brow lowers in annoyance."

    "It only takes a few seconds before I sigh in defeat. At least this is better than nicking one from the library, I guess."

    hi "Consider said “favour” cashed-in."

    ke "What? It's just a book."

    hi "Do you want it or not?"

    show kenji neutral at center
    with charachange
    
    ke "Fine, fine. I'll let you off."
    
    hide kenji
    
    show bg school_dormhisao at bgright
    with locationchange
    with Pause(1.0)
    
    show bg school_dormhisao at bgleft
    with locationchange

    "I walk back the desk and grab the thick book from my bag."

    "Already slightly creased from use, it flops lifelessly in my hand."
    
    show kenji neutral at left
    with charaenter

    hi "Here."

    ke "Thanks man."

    hi "Just give it back eventually, okay? I need that thing."

    show kenji tsun at left
    with charachange
    
    ke "Hey, do  I look like the kind of guy that wouldn't give something back?"

    hi "Well, yeah."
    
    show kenji neutral at left
    with charaenter

    ke "Cold, man. Cold."

    hi "Anything else?"

    show kenji happy at left
    with charachange
    
    ke "Nah, that's it. Seeya, and thanks for the book."

    hi "See you."
    
    hide kenji
    
    stop music fadeout 2.0
    
    play sound sfx_doorclose

    "And with that, I shut the door as he leaves."

    "Back to studying I guess."

    scene bg school_dormhisao
    with shorttimeskip
    
    play sound sfx_doorknock

    centered "*thud* *thud* *thud* *thud*"

    "Eugh."
    
    play sound sfx_doorknock

    centered "*thud* *thud* *thud* *thud*"

    "Enough, I can hear you."
    
    play sound sfx_doorknock 

    centered "*thud* *thud* *thud* *thud*"

    "God damnit, again?"

    "I lean myself upright, taking my eyes from the science textbook in front of me."

    play sound sfx_doorknock
    
    centered "*thud* *thud* *thud* *thud*"

    "Whoever it is, they're persistent."

    "Suddenly, there's a pause in the knocking as assorted mumbling's heard from behind the door."

    hi "Alright, alright, I'm coming!"

    "I spin my chair around and push myself out of it with some measure of effort, taking a moment to regain my legs before getting the door."

    play sound sfx_dooropen
    
    show bg school_dormhisao at bgleft
    with locationchange
    
    play music music_daily
    
    show rin basic_absent at left
    with charaenter
    
    show emi basic_happy at right
    with charaenter

    hi "What the… Rin? Emi?"

    hi "Well now, I haven't seen you two in a while."

    "What I'd rather say is “Why the hell are you knocking on my door so persistently?,” but I manage to hold my tongue."

    "As I look at them, I get an inexplicable sense of who was doing the knocking too."
    
    show rin basic_deadpan at left
    with charachange

    rin "Oh, we just…"

    show rin basic_deadpansurprised at left
    with charachange

    rin "…"

    show rin basic_deadpan at left
    with charachange

    rin "Hey, why did we knock on Hisao's door?"

    "I bring my palm to my face and drag it downwards as Emi dons a pained expression."
    
    show emi basic_closedsweat at right
    with charachange

    emi "We were going to ask him if he had time to help us move your painting!"

    "We both look to Rin, who seems to be as much focused on me as a speck of dust that's floating downwards between us."

    show rin basic_surprised at left
    with charachange
    with Pause(1.0)
    
    show rin basic_lucid at left
    with charachange
    
    show emi basic_grin at right
    with charachange
    
    rin "Ah, that's right."
    
    show rin basic_absent at left
    with charachange

    rin "Hisao, could you help us move my painting?"

    hi "I… guess so?"

    show emi excited_happy at right
    with charachange
    
    emi "Right, that's settled then! Come with us, Hisao!"

    hi "Wait, now?"
    
    hide emi
    
    hide rin

    scene bg school_dormhallway
    with locationchange

    show emi excited_happy at right
    with charaenter
    
    show rin basic_absent at left
    with charaenter
    
    "The answer comes in the form of Emi's hand tightly gripping my wrist and dragging me through my door."

    "As she does, I remember something that comes close to slipping my mind completely"

    hi "H—hey, wait, I have to get my medication!"

    "Almost as soon as I say it, I tense slightly."
    
    show emi excited_hesitant at right
    with charachange
    
    show rin basic_awayabsent at left
    with charachange

    emi "Ah, sorry. We'll wait out here then?"

    hi "Yeah, sure. I'll be right back out."
    
    show rin basic_deadpan at left

    rin "Be sure not to choke on the pills."

    hi "Be sure not to what?"
    
    show rin basic_deadpanamused at left
    with charachange

    rin "I almost choked on a pill once."

    hi "Uh huh."
    
    show rin basic_deadpancontemplation at left
    with charachange
    
    rin "It wasn't nice."

    hi "I see."
    
    show rin basic_deadpanamused at left
    with charachange

    rin "So don't choke on your pills."

    hi "I'll make sure not to."

    hide emi
    
    hide rin
    
    show bg school_dormhisao at bgright
    with locationchange

    "Walking back into my room slightly dazed, I make my way to the draw containing my pills."

    "As per my daily ritual, I open the drawer to a marvel of medical science."

    "No matter how many times I see it, though, I can't help but loathe the sight."

    "Let's see, Saturday, Saturday, Saturday."

    "I move my hand up and down until I spot the shelf I keep the day's morning medications on."

    "Here we go."

    "I move from one bottle to another, some cold glass, others hard plastic, and drop the pills from inside into my hand."

    "As my cupped palm fills, I move to the next task."

    "Alright next is… daily."

    "Where the— Ah, there."

    "Like some kind of student pill-swallowing machine, I expertly down each medication one after the other."

    "All the while, taking careful heed not to choke on any of them."

    scene bg school_dormhallway
    with locationchange

    "After a few minute's worth of swallowing, I walk back out in the hall to rejoin Emi and… Rin."

    hi "Huh, that's odd."

    "As I look down the hall they're nowhere to be—" #reminder for the potential {nw} break

    hi "GYAAAAH!"
    
    with vpunch

    "I jump up into the air, pinning my elbows to my waist."

    "As I land and slump in knowledge of what's just happened, I look behind me."

    show emi excited_joy at right
    with charaenter
    
    show rin basic_amused at left
    with charaenter
    
    emi "Told you."

    show rin basic_deadpanamused at left
    with charachange
    
    rin "Hisao, I had no idea."
    
    show emi basic_confused at right
    with charachange

    hi "No idea? About what?"

    show rin basic_deadpancontemplation at left
    with charachange
    
    rin "That you're an athlete."
    
    show emi basic_grin at right
    with charachange

    hi "…what?"
    
    show rin basic_awayabsent at left
    with charachange

    rin "To jump so high you have to be an athlete."
    
    #jump animation?

    "As if to prove her point, she does a standing jump."

    hi "I'm not an athlete. I was just startled."
    
    show rin basic_deadpanamused at left
    with charachange

    rin "Did you choke on your pills?"

    "This girl never lets me forget her ability to change topics faster than a politician under questioning."

    hi "No, I did not. Thanks for the warning."
    
    show rin basic_deadpandelight at left
    with charachange

    rin "Good. Choking on my pill really hurt."

    emi "We should probably get going."

    "I look over to Emi, patiently waiting as Rin and I play mental chess."

    "The fact I have to do so just to try and have a normal conversation with her is worrying."

    hi "Yeah, sure. Lead the way."

    scene bg school_dormhallground
    with charachange
    
    stop music
    
    $ renpy.music.set_volume(0.20000000001, .20, channel='ambient')
    play ambient sfx_rain fadein 2.0

    "As he head towards the door outside, I hear the pitterpatter of rain on the roof."

    "Heavy rain, at that."

    hi "Damn, it's raining?"

    show emi basic_closedgrin at left
    with charaenter
    
    emi "Why did you think we needed your help? If it was fine we could do it ourselves."

    hi "I guess you want me to hold a cover over it or something?"

    show emi basic_grin at left
    with charachange
    
    emi "Exactly."

    hi "We're going to get drenched, aren't we?"

    show rin basic_deadpannormal at right
    with charaenter
    
    rin "Is that a bad thing?"

    hi "Well, yeah. We could get colds."

    show rin basic_deadpancontemplation at right
    with charachange
    
    rin "Huh."
    
    show rin basic_awayabsent at right
    with charachange

    "She looks up contemplatively."

    "I don't even want to hazard a guess as to what she's possibly thinking right now."

    show rin basic_absent at right
    with charachange
    
    rin "If I get a cold Emi will help me, and if Emi gets a cold I'll help her."

    hi "And if you both get colds?"

    show rin basic_deadpan at right
    with charachange
    
    rin "Then the Nurse will help us."

    hi "I don't think he makes house calls for colds."

    show rin basic_deadpanamused at right
    with charachange
    
    rin "I think he might for Emi."

    show emi basic_shock at left
    with charachange
    
    hi "Say what?"

    $ renpy.music.set_volume(1.5, 1.5, channel='ambient')
    
    scene bg school_gardens_rn
    with locationchange

    show rain
    with Dissolve(5.0)

    "Before Rin can reply, Emi pushes open the door to the deluge outside. The sheer force and volume of rain gives a deafening roar, with the wind lashing across the wet concrete."

    hi "Jesus!"

    show rin basic_upset at right
    with charaenter
    
    rin "Uwaaah~"

    show emi basic_concentrate at left
    with charaenter
    
    emi "Alright, on the count of three we'll run to the Hall. Got it?"

    show emi basic_confused at left
    with charachange
    
    emi "…wait, no, we won't do that."

    hide emi
    hide rin
    
    "Just as I open my mouth to ask why, I realize in the nick of time. This could be a problem."

    $ renpy.music.set_volume(0.20000000001, .20, channel='ambient')

    scene bg school_dormhallway
    with locationchange

    show emi basic_annoyed at left
    with charachange
    
    "She closes the door and leans back against it, her brow lowered in thought."

    hi "I could grab an umbrella from my room."

    show emi excited_joy at left
    with charachange
    
    emi "Three people wouldn't fit under it, would they?"
    
    hi "No, but two would."

    emi "And which two would they be?"

    show emi basic_confused at left
    with charachange
    
    hi "Why, the fair ladies of course."

    "I accentuate my offer with a gracious, if slightly overdone, bow."

    "As I look up, I'm slightly disappointed to see a distinct lack of reaction from Emi."

    "I guess only Lilly has that weak spot."
    
    show emi excited_hesitant at left
    with charachange

    emi "But you'll get a cold!"

    hi "Hah, me? Do I look that weak to you?"
    
    show emi basic_grin at left
    with charachange

    emi "Well, yeah."

    show rin basic_deadpansurprised at right
    with charaenter
    
    rin "She has a point."

    hi "Damn, both of you? That's not fair."

    "I sigh, though I guess I brought on that exchange by myself. Emi's not exactly a figure of feminine daintiness, and Rin… is Rin."

    hi "Nevertheless, you two are getting the umbrella. I'll run ahead to the hall."

    emi "But…"

    hi "I'll be fine, it's just rain. Now stay here while I get it."

    "I turn and quickly make my way back to my dorm room, leaving Emi's protests behind."

    scene bg school_dormhisao
    with locationchange

    "Once I get there, it doesn't take long for me to find the umbrella collecting dust leaning against a wall. A quick shake's all that's needed to make it look brand new, the black fabric significantly darker for the effort."

    "Now, to get back to that troublesome duo."

    "Taking the umbrella in hand, I jog back to where the two were waiting."

    scene bg school_dormhallway
    with locationchange

    "Thankfully, they're exactly where they were standing this time"

    hi "Back. Here."

    "I hand the umbrella to Emi, who raises it high to cover her taller companion."

    "Rin looks at it like a bored child, examining every detail of the thoroughly uninteresting object."

    rin "Boring."

    hi "It's meant to keep the rain off you, not be a piece of art."

    rin "It would be neat if it was."

    hi "Well, that's a… wait, no, back on task. Ready, Emi?"

    "She pushes her free fist forward and puffs out her noticably lacking chest to show her readiness."

    emi "Let's go!"

    hi "Righto. I'll run to the hall and open the door for you, okay?"

    "With a quick nod from the determined Emi and bored Rin, I open the door once again."

    emi "Go!"

    scene bg school_gardens_rn
    with locationchange

    show rain
    with Dissolve(5.0)

    "I dash out like a greyhound from the starting blocks, the occasional puddle all but drenching my socks inside my shoes."

    "Thanks to the gardens not being used for any afterschool clubs, it's pretty much a clear path to the hall through the gardens with not a soul in sight."

    "One windy bend after another, I feel the rain hitting my face and already starting to soak through my clothes."

    "As I round the last corner, the door to the hall in sight, A tremendous gust of wind nearly blows me off my feet and sweeps water all over my right side."

    hi "Damnit, damnit, damnit."

    "What a stupid plan this was."
    
    stop ambient fadeout 4.0
    
    scene bg school_auditorium
    with locationchange

    "I swing open the door and burst in, slumping against a wall."

    hi "Argh, I'm soaking wet."

    "As I wait for Emi and Rin to catch up, I jump up and down to shake off the loose water."

    "Girl" "Hmm…?"

    hi "Ah…"

    "I pause and look upwards to where the disembodied voice came from."

    "A familiar figure stands on the stage, a lost look on her face."

    "She looks comically overdressed, the lower half of her face all but hidden behind an oversized beige scarfe."

    "I almost crack up at the rediculous sight."

    li "Excuse me, who's that?"

    hi "Hey Lilly, it's just me."

    li "Ah…"

    "She coughs harshly, her voice noticably husky."

    li "Hisao. Good afternoon."

    hi "'Afternoon. Fancy seeing you here."

    li "I was about to have one last performance in here before everything had to go back to my dormitory and the music room."

    hi "Throat sore?"

    li "Hmm? Oh, j—just a bit."

    "Just as she finishes the sentence, I feel an arm push hard into my upper back."

    hi "Erk!"

    emi "Having a nice chat, Hisao?"

    "I turn back to see both Rin and a grinning Emi retracting the umbrella and proceeding to unceremoniously shake the water off it and onto the floor."

    "Both are, unsurprisingly, much drier than I."

    li "Sorry, who might that be…?"

    emi "Ah, hey Lilly. It's just me and Rin."

    li "Good morning Emi, Rin. What brings you two here?"

    rin "We wanted to get you and Hisao together."

    "My jaw drops open as Emi delivers a sharp elbow into Rin's side."

    "Amazingly, the rather forceful blow doesn't seem to faze her at all."

    rin "Oh, and get my painting."

    "Her pint-sized partner hangs her head and hides it in her hand."

    "Well, I guess it shouldn't be a surprise they'd try something, considering what Kenji said."

    hi "You two…"

    li "My my, it seems as if a plot is afoot."

    emi "Rin…"

    rin "I thought we were just going to tell them?"

    emi "You're making this worse."

    "Rin cocks her head to the side inquisitively."

    rin "I think I'm making it better."

    "The two look closely at each other, Emi's questioning eyes meeting Rin's blank stare head-on."

    "After a scant few seconds, the conflict comes to a peaceful end as Emi shrugs in defeat."

    emi "Well, that's the way things stand I guess."

    "I grin and reach forward, scruffing her hair to her mumbled protests."

    hi "Let's get that painting, shall we?"

    rin "It's in the store room behind the stage."

    "I release Emi's hair from my grip, though she's still blushing furiously."

    emi "I—It's over here. I'll get it."

    "With that, she quickly walks behind the stage, not daring to look back."

    "I turn back to Rin, still wearing a wry grin."

    hi "Didn't you want my help?"

    rin "The umbrella can shelter two people, right?"

    hi "Yeah."

    rin "Then the painting will become a person and I'll get wet."

    hi "The painting will…"

    "It takes a few seconds for me to click exactly what she means. Heaven knows whether it was an intentional riddle or not."

    hi "Oh. You're going to get wet if you do that, you know."

    rin "Does that matter?"

    hi "Yes it matters. You'll get a cold."

    rin "Then Emi will look after me."

    "This girl…"

    hi "I… Ah, forget it."

    rin "I'll need the umbrella"

    hi "Sure, just drop it by my dorm after you're finished with it."

    "I seize upon her rare moment of lucidity as Emi gets back."

    "In her hands is a square canvas the size of her outstretched arms, with the umbrella awkwardly propped upright between her palm and the painting's side."

    "The painting on it seems to be, to my untrained eye, some sort of heavily stylised person."

    "For a second I furrow my brow, losing myself in trying to work out exactly what it's supposed to represent."

    emi "It's great, isn't it?"

    hi "Yeah, it's really good."

    "Most great art's completely unrecognisable, so I guess this must be great art."

    "Satisifed with my questionable leap of logic, I turn to Rin."

    hi "Nice work, Rin."

    "She blankly nods. Whether it's in thanks for the compliment or just acknowledgement that she heard me, I'm not sure."

    emi "So, are we going to take this to your room?"

    rin "I suppose so."

    emi "Aren't you going to get wet? You can't fit under the umbrella together with the painting."

    hi "I told you."

    rin "It's okay, if I get a cold you'll look after me."

    "The statement draws a flat look from Emi, though surprisingly no outright denial."

    "I guess she must've been right."

    emi "Well, we'll be off then."

    hi "Seeya."

    li "Goodbye Rin, Emi."

    emi "Seeya Lilly."

    rin "Bye."

    "As Emi turns to open the door, she suddenly pauses."

    emi "Ah…"

    hi "Hmm?"

    emi "Hey Hisao, could you get the door?"

    hi "Ah, sure."

    "I quickly slide between Rin and Emi, turning the handle with an outstretched arm."

    "Thankfully the weather seems to have calmed down somewhat, reduced to a heavy drizzle."

    hi "You two okay to get that to her room?"

    rin "We'll be fine."

    "And with that, they set off out the door."

    "What a weird pair."

    "I quietly close the door, bringing silence to the hall once again."

    li "They are a cute pair, aren't they?"

    "I turn back to Lilly, still standing on the stage."

    "I guess she must've been listening to us the whole time."

    hi "That's one way to put it."

    "I stretch loudly, trying my best to keep my mind away from just how exhausted my body is after such a short run."

    hi "Don't mind if I just take a seat in the hall do you? I'm completely buggered."

    li "No, that's fine, I can find the cello by myself. I've had more than a little practice navigating backstage."

    hi "Thanks. Hanako's not with you?"

    li "She's still sleeping, it seems."

    hi "I guess it is a weekend after all."

    "As Lilly turns to go backstage, I wander past the stage and up to the rows of seats facing it while running my hand through my wet hair."

    "It doesn't take long after getting seated for her to emerge, cello case in hand."

    "I rest my head in my hand as I watch her get set up, savouring the peacefulness of the hall."

    "It's pretty damn big, to put it lightly, being made to house the entire school's worth of students if need be."

    "Yet, only two people are within it."

    "I smile as I lean back."

    "I wouldn't have it any other way."

    # Start Saraband

    "I breath deeply as the soft, melancholic notes fill the air."

    "Damn, that run tired me more than I thought."

    "I guess it wouldn't mater if I closed my eyes for a bit."

    "As I close my eyes, the scene seemingly imprints itself on my mind."

    "That beautiful siren, playing that melancholic tune."

    "A single, small figure surrounded by the empty expanse of the endless hall."

    # Fade to black

    scene black
    with dissolve

    scene bg school_auditorium
    with openeye

    "Hmm?"

    "I open my eyes groggily."

    "Where…"

    "Oh, that's right."

    "I fell asleep in the hall as Lilly was playing."

    "I rub my eyes and look around the hall, taking careful measure of the stage."

    "She's gone."

    "Just how long did I sleep anyway?"

    "As I turn my wrist to my face, I see that it's already about noon."

    "Jesus, talk about a nap."

    "As I move to get up, I suddenly realise an added weight pressing on my chest."

    "A familiar grey trenchcoat lies draped over my soaked front."

    "I can only smile as I gently take it in my hands and fold it."

    "I suppose I'll give it back the next time I see her."

    scene black
    with dissolve

    return

label en_L17:

    scene black

    ha "Um, Hisao…"

    hi "Go away."

    ha "But, uh, H—Hisao…"

    hi "Leave me alone."

    ha "But…"

    hi "Hmph, let me sleep."

    "Sleeping with Lilly seems to have more than one advantage."

    "Being able to sleep decently without being thoroughly exhausted beforehand would be nice, though."

    ha "Hisao, Emi needs you…"

    "I don't care what Emi wants, leave me alone."

    emi "Look, Hanako. Let me show you how to wake Hisao up."

    "Wait, Emi's going to…?"

    emi "One, Two, and…"

    "This is bad!"

    hi "I'm up! I'm— {w=.5}{nw}"
    with vpunch
    
    play sound sfx_impact

    "My head rockets back down onto the desk, hit with what seems like the force of a sledgehammer."
    
    scene bg school_scienceroom
    with locationchange
    
    show emi basic_closedhappy at left
    with charaenter
    
    show hanako emb_blushtimid at right
    with charaenter

    $ renpy.music.set_volume(1.0000000001, 1.0, channel='ambient')
    play music music_normal fadein 8.0
    
    hi "Ah! My head, my head…"
    
    show hanako emb_downsad at right
    with charachange
    
    show emi excited_happy at left
    with charachange

    "I grimace and hold my sorely aching head in my hands."

    "Hanako's completely shocked at what Emi dared to do, though the perpetrator herself looks unrepentant."

    show emi excited_joy at left
    with charachange
    
    emi "Hisao, I will not allow you to become like Rin!"

    hi "My head… My head…"

    show hanako basic_worry at right
    with charachange
    
    ha "Are you okay, Hisao?"

    "I quickly shake my head and try to put on a brave face for Hanako."

    hi "I'm fine, just dazed."

    show hanako def_smile at right
    with charachange
    
    show emi excited_happy at left
    with charachange
    
    "Judging by her expression, I didn't manage it well. Emi's pint-sized arm is surprisingly strong."

    "Looking around, it seems the last of the students are dribbling out of the room for lunch."

    "Invariably, it's those bound to wheelchairs taking the flank. Poor guys."

    hi "Well, I'm up now. What're you wanting?"

    show emi basic_grin at left
    with charachange
    
    emi "You should ask Hanako that. She's been trying to get you up for ages."

    hi "Hanako has…?"
    
    "I look over to Hanako with slightly sleepy eyes, her hands fidgeting constantly."
    
    show hanako basic_bashful at right
    with charachange
    
    ha "Uh… well… I—I… er…"

    "Emi, lacking in my patience around her, gives her a sharp clap on th shoulder to try and make her come out with what she wants to say."

    show hanako emb_blushtimid at right
    with charachange
    
    ha "I… I was going to ask… if you've seen Lilly… today?"

    hi "Oh."

    "As I begin to answer her, I'm distracted by Emi's overly audible sigh."

    show emi basic_confused at left 
    with charachange
    
    emi "Geez, you made me get him up just for that?"

    show hanako emb_downtimid 
    with charachange
    
    ha "But… what did you…?"

    show emi basic_shock at left
    with charachange
    
    emi "Ah, nevermind! Hisao, seeya later!"

    "With that, she walks out of the classroom as fast as her artificial legs will let her."

    hide emi
    
    play sound sfx_footsteps_hard
    
    "Which, without her running blades on, isn't very fast."

    "As Hanako looks back at her entirely lost, it's pretty obvious what Emi had thought Hanako was going to say."

    "Hanako wouldn't be Hanako if she didn't give every word she said the same amount of thought as a confession."

    hi "So, you haven't seen Lilly today?"
    
    show hanako emb_sad at center
    with charamove

    "She turns back and shakes her hea vigorously."

    show hanako basic_bashful at center
    with charachange
    
    ha "I didn't see her at lunch or before school. Do you think something happened to her?"

    hi "Come on, it's Lilly. She's not exactly going to go and do any extreme sports, is she?"

    show hanako basic_smile at center
    with charachange
    
    ha "I guess so…"

    "The comment doesn't relieve her worrying, though I guess there wasn't much chance of that."

    hi "Well, it's the end of class now. I'll pop up to her dorm and have a check, okay?"
    
    show hanako basic_normal at center
    with charachange

    ha "O—Okay. Thanks. I had work to finish, so…"

    hi "Don't worry about it. I'm kind of curious about why she's not here as well."
    with shorttimeskip
    
    stop music
    
    scene bg school_girlsdormhall
    with locationchange
    
    play sound sfx_doorknock
    
    $ renpy.music.set_volume(1.0000000001, 1.0, channel='ambient')
    
    play music music_heart
    
    centered "*Thud* *thud* *thud*"

    "…"

    "……"

    "Despite my repeated rapping of my knuckles on her door, not a peep can be heard."

    centered "*Thud* *thud* *thud*"

    "…"

    "……"

    "And again, no answer."

    "I take a second to stand back and plan my next course of action."

    "The rattling of the doorknob, though, soon halts any thoughts I'd been having."
    
    play sound sfx_dooropen
    
    show lilly basic_concerned_paj at center
    with charaenter
    
    hi "Hey Li… lly?"

    "With her hair undone and her face looking paler than usual (quite a feat), she looks more like a ghost than a living person."

    hi "You look like crap."

    show lilly basic_oops_paj at center
    with charachange
    
    "The blunt statement doesn't seem to amuse her."

    hi "Sick?"

    "She nods sullenly, noticably remaining silent."

    hi "Virus? Bug? Biological weapon?"

    "She shakes her head before opening her mouth and attempting to speak."
    
    li "My… throa…"

    hi "It's okay, don't speak if it's that painful."

    hi "Oh dear. Want me to grab the nurse to have a look at it?"

    show lilly basic_smile_paj at center
    with charachange
    
    "She looks at me, smiling weakly as if to apologise for troubling me."
    with shorttimeskip

    "In no time I once again stand in front of the door to her dorm, though this time with the nurse beside me."

    centered "*Thud* *thud* *thud*"

    "This time, Lilly opens the door almost as soon as I knock."
    
    show lilly basic_sleepy_paj at center
    with charaenter

    hi "Hey Lilly, I'm back."

    show nurse neutral at left
    with charaenter
    
    show lilly basic_sleepy_paj at right
    with charamove
    
    nk "Good afternoon, Miss Satou."

    show lilly basic_reminisce_paj at rightsit
    with charamove
    
    show lilly basic_reminisce_paj at right
    with charamove
    
    "She gives the best smile she can muster, bowing to him with surprising accuracy."

    show nurse concern at left
    with charachange
     
    nk "Now, I hear from Nakai you don't feel too well."
    
    show lilly basic_concerned_paj at right
    with charachange

    "She gives the same sullen nod as she gave me before."
     
    scene bg school_dormlilly
    with locationchange
    
    nk "Well, just pop over to your bed and have a sit while I get set up here."

    show lilly basic_concerned_paj at right
    
    show nurse fabulous at center
    
    "As per his instructions, she slowly walks over to her bed, checking the edge with her hand before taking a seat on the side."

    "In a perfectly doctorly fashion, the nurse strides in, setting his bag on the ground before opening it."

    "It doesn't take long before he's retrieved a small torch and a stick, holding it to her mouth."

    nk "Alrighty, just open up wide and I'll take a look here…"
    
    "She obediently opens her mouth as wide as she can, the nurse holding down her tongue as he shines the torch in."

    show nurse concern at center
    with charachange
    
    nk "Hmm… mmhmmm…"

    nk "I see… Yep…. Hmmm…."

    "His musings aren't very convincing."

    "Evidently content with the results of his poking around in her mouth, he stand up and brushes himself off."

    hi "What's the verdict?"
    
    show nurse neutral at center
    with charachange
    
    show lilly basic_displeased_paj at right
    with charachange
    #with charamove

    nk "It looks like Miss Satou here has a bad case of the ol' tonsillitis."

    "Damn. I'd been hoping it was just a virus of some kind."

    show lilly basic_concerned_paj at right
    with charachange
    
    "Looking to Lilly, she seems more worried than I about the problem."

    "As the nurse moves to pack up his bag, he looks up."

    nk "With her throat like this, it's likely she'll need to go to the hospital for surgery."

    show lilly basic_surprised_paj at right
    with charachange
    
    hi "How long for?"

    nk "Well, if the usual treatement's done, she'll have to have her tonsils out…"

    nk "I'd peg it at around a week or two. Going by the norm, anyway."

    hi "Damn."

    "before I can ask Lilly as to her thoughts, I see her reach out and try to speak."

    show nurse fabulous at left
    with charachange
    
    nk "Ah, don't do that. It's better that you rest your throat for now."

    show lilly basic_listen_paj at right
    with charachange
     
    "The statement makes her all the more depressed, though by now I can guess as to what she wants to say."

    hi "Don't worry. I'll take care of Hanako for you."
    
    show lilly basic_smile_paj at right
    with charaenter 

    "Her face brightens considerably. She really does care for that girl."

    hi "Is there anything I can do to help?"

    nk "I'll call for an ambulance to come pick her up. For now, just take care of Ikezawa. I know how she is, too."

    hi "Alright, can do."

    nk "I wouldn't worry too much, either of you. It's a routine procedure that a lot of people go through. You should be able to visit her in a day or two."

    "As he begins to walk out the door, I suddenly remember something I'd almost forgotten to say."

    hi "Thanks for checking over her."
    
    show nurse grin at left
    with charachange

    "He gives a cheesy grin to us as he turns back."

    nk "Just doing my job. Take care of yourselves, now."
    
    show lilly basic_smile_paj at rightsit
    with charamove
    
    show lilly basic_smile_paj at right
    with charamove

    "Lilly gives a thankful bow to him as he leaves and shuts the door behind him."
    
    hide nurse
    with charaexit
    
    play sound sfx_doorclose
    
    show lilly basic_emb_paj at center
    with charamove

    "Bereft of energy, she gives a resigned sigh as she rubs her neck."

    hi "You okay?"

    "She gives a silent nod, though she stops as I rest my hand on her head."

    hi "I'll visit you as soon as I can, and Hanako too."

    show lilly basic_smileclosed_paj at center
    with charachange
    "She closes her eyes, pausing for a moment before nodding once again."

    scene black
    return

label en_L18:
    # Open to act 3, title card "Past and Present"

    scene bg school_courtyard at center
    with locationchange
    
    $ renpy.music.set_volume(0.20000000001, 1.0, channel='ambient')

    play ambient sfx_crowd_outdoors
    
    #don't forget to add the crowds here
    
    "Joining the throngs of students leaving the building, I make my way through the courtyard towards the iron gate."

    "The most I could get out of that damn nurse at lunchtime was which hospital she was in."

    "Of all the times to get serious, it's when he plays the patient confidentiality card."

    "Bah."

    "I'll know soon enough. It's not going to be anything life-threatening."

    scene bg school_road
    with locationchange

    "As I round the school gate and reach the nearby bus stop, I take note of the bus schedule attached to a nearby pole."

    "Shit. The next bus that goes anywhere near there's going to be in two hours."

    "I rub my eyes and take a moment to think."

    "It's way too far to walk, so that's right out."

    "A taxi'd be too expensive."

    "Ah ha!"

    "I remember the note I'd grabbed off my desk and shoved into my pocket."

    "I grin as I turn the crumpled paper over, a familiar phone number written in neat cursive writing becoming visible."

    hi "Right, now…"

    "I fish the mobile phone from my pocket, flipping it open and carefully punching in the written numbers one by one."

    "With the last number, I press my thumb on the talk button and bring the phone to my ear."

    hi "Stupid bloody buses…"

    # SFX, ringing

    centered "*ring ring* *ring ring*"

    hi "Huh?"

    "Phone in hand, I turn around."

    yu "Yo."

    "I'm left with my jaw on the ground from amazement."

    "Talk about impeccable timing."

    hi "You…"

    yu "I thought you might need a lift."

    "I rub my eyes to make sure I'm not seeing things."

    hi "Nice timing."

    yu "Hanako coming?"

    hi "Classes held her up. She said she'd come tomorrow."

    "As soon as the words are out of my mouth, a loud wolfwhistle comes from behind me."

    "All I can do is grimace."

    "As I open my mouth to try and cover over the incident, Yuuko looks beside me and calls out."

    yu "Settle down boys, I'm taken!"

    "Boy 1" "Aw, what?"

    "Boy 2" "Hah, shut down!"

    hi "Wait, what the—" #reminder for the potential {nw} break

    yu "Catch!"

    "By reflex I manage to catch the large object she throws at me, and take a brief moment to examine it."

    "Another white helmet with a red stripe down the center."

    "…I wish I were surprised."

    "I push it down onto my head with little effort, making sure to do up the straps carefully."

    "As I fiddle with the clips, the istuation I've gotten myself into dawns on me."

    "I am at a bus stop full of students, getting onto a scooter driven by a woman who's declared she has a boyfriend."

    "Well, it's not like I can help it now."

    hi "That should be it for the helmet, what now?"

    "She sits down and flicks her head to the side, motioning for me to sit behind her."

    "I quickly walk around the scooter and take my seat."

    "It takes a moment's hesistation before I dare bring my arms around her waist to hold on."

    yu "Ready?"

    "Surprisingly enough, she seems unfazed."

    hi "Ready when you are."

    "With a couple of flicks of her wrist, the engine roars to life."

    "Well, putters sickly would be a better description."

    yu "Hold on!"

    hi "I'm holding!"

    "With that, she gives a sharp flick of her wrist on the handle."

    "…To which the scooter responds by descending into silence after a couple of harsh pops."

    hi "It's… not meant to do that, is it?"

    "She seems to deflate in my arms as I let go."

    yu "My scooter… My beautiful scooter…"

    "She turns the handle helplessly, not a sound to be heard from the wounded scooter in response."

    "It looks terminal."

    yu "My scooter…"

    "I pat her on the shoulder to try and calm her down."

    hi "Come on, we'd better get moving. We can just walk it with us until you get it to a repair shop."

    "As she nods in reply, I can't bring myself to look her in the eye."

    "I'm sorry, Yuuko. I don't think that scooter's going to be moving again."

    scene bg city_street1
    with locationskip   

    "I breath a sigh of relief."

    "Though she's still somewhat downtrodden, she seems to have calmed down as we walk through the city."

    "Dutifully taking my turn as wheeling along her scooter, I remember an odd offhand remark she made."

    hi "Hey, Yuuko?"

    "As she looks at me, her downcast expression is traded for innocent curiosity."

    hi "You have a boyfriend?"

    "She pauses for a moment before talking, swaying her head from side to side as she silently deliberates on her reply."

    yu "Well, I think so."

    hi "You… think so?"

    yu "We got pretty close, but it just kind of… ended."

    hi "He left you?"

    yu "No, he just stopped contacting me completely."

    "She gives a whistful sigh as I grimace."

    "That sounds an awful lot like it was ended, no “kind of” needed."

    yu "I would like to see him again."

    yu "He was quiet, and kind of weird, but… he never did anything without good intentions."

    hi "Huh. Sounds like a nice guy."

    yu "He was. He even went to your school."

    hi "He did? Know what class he was in?"

    yu "Hmm, I don't think he ever said. He was always really secretive."

    hi "I see."

    "With that, the conversation dies off."

    hi "Have you heard anything about Lilly yet?"

    yu "Yeah, her parents phoned me about it."

    hi "You're that close?"

    yu "I guess you could say I'm the eyes and ears of Lilly's family."

    hi "Eyes and ears?"

    hi "Wait, you don't mean you spy on her, do you?"

    yu "Well, not really that."

    yu "I keep them informed, they keep me informed. That's how it works."

    hi "So you are a spy for them then?"

    "She simply shrugs."

    "This line of questioning isn't getting me anywhere."

    hi "Anyway, any word on how Lilly's doing?"

    yu "She went into surgery this morning, she should be awake by now though."

    hi "Can she talk?"

    "She shakes her head."

    yu "They said they're not sure when she'll be able to. It shouldn't be over a week, though."

    hi "Being blind, and now not being able to speak on top of it…"

    "I find myself staring ahead, in my own little world."

    "I can't help but feel a pang of embrassment as I look back to Yuuko."

    yu "You know how she is. Something like this wouldn't faze her, not in a million years."

    hi "Yeah, you're right."

    "The rest of the trip passes in silence, though it doesn't take long before we stop at the hospital."

    scene bg hosp_hallway
    with locationskip

    "After a quick check with the receptionist as to where she's staying, we take the elevator up and reach the hallway to her room"

    "The atmosphere of the hospital makes me unbearably tense."

    "Such a horrid place."

    "A place where people come to die."

    "The creak of Yuuko opening the room door brings me out of my dwelling."

    scene bg hosp_room
    with locationchange

    "As I enter behind her, I take a quick survey of the room."

    "Beige walls."

    "White ceiling."

    "Small insipid watercolour painting of a flower hanging on a wall."

    "The sight almost makes me want to throw up."

    yu "Li~lly!"

    "Once again, Yuuko refocuses my mind."

    "Lilly lies on the bed, dressed in white hospital robes and underneath the light blue hospital sheets."

    "Her tall and healthy figure looks strangely small and frail."

    "She smiles and gives a deep nod."

    "As she does though, I can't help but notice the way she's acting."

    "Her usually confident demeanor's all but disappeared. Something's not right."

    hi "Hey Lilly, I'm here too. How're you feeling?"

    "She tilts her head from side to side, as if to say that she's so-so."

    "I move to a a chair beside her bed, Yuuko beside it and leaning over."

    yu "I filled Hisao in on what happened."

    "Another smiling nod."

    "She turns her head to me, a questioning expression on it."

    "At a guess, she's asking how I am. It's only a guess, though."

    hi "Uh… how am I?"

    "Her nod confirms my hypothesis."

    "Trust her to be making sure everyone else is okay, even while she's in hospital."

    hi "I'm fine, so's Hanako. You should be worrying about yourself more, Lilly."

    "With a creak, the door opens once again."

    "An old and somewhat stern looking doctor, clipboard in hand, enters the room."

    "Doctor" "Ah, sorry. Am I interrupting? I can come back later."

    yu "Ah, no, it's fine. Could I have a talk with you for a moment?"

    "Doctor" "Family?"

    yu "Mm, cousin."

    "They both head out the door, leaving Lilly and I alone."

    "…"

    "Silence."

    "It's perhaps the only awkward silence I've ever had around Lilly."

    "I'd been looking forward to meeting her ever since she entered hospital."

    "To come in and see her smiling face."

    "To comfort her if she'd been in pain."

    "To tell her what's been going on in school."

    "But now that I'm here… I can't think of a single word to say."

    "To look at her like this, though, makes me want to help her."

    "With a small sigh at my helplessness, I put my hand on her head."

    "Slightly giving way under it, I gently rub her whispy yellow hair underneath my fingers."

    "As I do, though, her smile seems to dissipate."

    hi "Ah, Lilly, I—" #reminder for the potential {nw} break

    "As I begin to lift off my hand, she quickly moves to take it in her own."

    "Grasping my right hand in her left, her right hand reaches upwards and takes my cheek."

    # Possible CG, if the hospital arc uses Lilly in hospital gown sprites instead of 10498485 chained CGs

    "I can't move."

    "The feeling of her soft, smooth hand."

    "The look of sadness written on her face." 

    "I… I want to help her."

    "But I can't. I don't even know what's wrong in the first place."

    "As I look into her sapphire eyes, their beauty all but lost to her, I gather myself and smile as I take her hands in mine."

    "I have to be there for her."

    "When she tells me, I'll be there."

    hi "It's okay, Lilly."

    hi "I'll take care of everything, don't worry. I'll visit you, so will Hanako and Yuuko."

    hi "Everything'll be fine. I'll make sure of it."

    "She gives a weak smile, taking a moment before nodding."

    "The door swings open as she withdraws her hand, Yuuko half-appearing through the doorway."

    "Her expression, though, is one I've never seen her have before."

    # Yuuko srs bsns sprite

    yu "Sorry Lilly, I have to go now. I'll be sure to come in later."

    yu "Hisao, want to come?"

    "As I look back to Lilly, she shrugs noncomittedly."

    hi "Sure, hold on."

    "I stand and walk over to the door, looking back to Lilly as I enter it it."

    hi "See you tomorrow, Lilly."

    "She raises her arm and gives a small wave."

    "And with that, the door closes."

    hi "What the hell's going on?"

    "It's only a short walk through the hall and down the elevator to reach the lobby."

    scene bg hosp_ext
    with locationskip

    "As I walk outside, I see Yuuko's scooter still propped up on its stands and unattended."

    "I guess Yuuko's as good as anyone to ask about what's wrong with Lilly."

    hi "Hey Yuuko, what's—" #reminder for the potential {nw} break

    yu "Hisao?"

    hi "Er, yeah?"

    yu "You're not her boyfriend, are you?"

    hi "No, I wouldn't say so."

    "Another silence."

    "Yuuko takes a seat on the bench next to the hospital door as I lean against the wall."

    yu "How do you view Lilly?"

    "My breath catches at the unexpectedly blunt question."

    hi "How do I… view Lilly?"

    yu "Mm."

    "I look up to the sky."

    "A light blue screen, punctuated by the occasional whispy cloud."

    "They seem as if they could gently float across the sky for eternity."

    "Sometimes fine, sometimes rainy."

    "Forever lazily floating through that deep blue expanse, carried only by the wind."

    "If only life worked that way."

    "I return my gaze downward."

    hi "I don't know."

    hi "But…"

    "I take a breath, choosing my words carefully."

    hi "I want to find out."

    "Yuuko looks at me, smiling warmly."

    yu "Well, that'll do for now."

    hi "You're making me feel like I've just had an exam."

    yu "If that's the case, you should feel happy you've passed, right?"

    "I look at her flatly as she begins to swing her legs carelessly. This is Yuuko, alright."

    hi "So what was that, anyway?"

    yu "Hmm?"

    hi "Back there, after you talked to the doctor. I assume it's related to how Lilly was."

    yu "Ah. That."

    yu "Lilly's family sent someone to check on her."

    hi "Isn't that your job?"

    yu "Hey, don't misinterpret. I care for Lilly too, you know."

    hi "Uh, Sorry."

    yu "Ah, joke. Sorry, Hisao."

    hi "It's fine, really."

    "…"

    "Silence."

    "As she moves to speak, her legs come to a stop."

    yu "You're really bummed about this, aren't you?"

    "I look away slightly in embarassment"

    hi "Kind of."

    "She gives a short giggle."

    yu "Well, that's not a bad thing."

    "She pauses a moment to choose her words."

    yu "Hey, Hisao."

    hi "Yeah?"

    yu "Do you know where Lilly's from?"

    hi "Uh, no."

    yu "Do you know how many siblings she has?"

    hi "No."

    yu "Her previous school? Her wishes for the future?"

    hi "No, I don't."

    "She suddenly stops her interrogation and sinks into deep thought."

    "What in the world is she doing this for?"

    "With a small smile, she looks back."

    yu "Hisao?"

    hi "Mm?"

    yu "Be sure to visit her often."

    hi "Of course I will."

    yu "Well, in that case we'd better be off."

    "She quickly moves to stand up, and begins to walk over to the parked scooter."

    hi "Hey,"

    "She turns back as I call out to her from the bench."

    hi "You didn't answer my question. What the hell went on in there?"

    yu "It's not my place to tell you."

    yu "Though, I'm sure you'll learn soon anyway."

    hi "You're dodging."

    yu "Maybe I am."

    "I sigh as I stand up."

    hi "Fine, let's go."

    scene black
    with dissolve

    return

label en_L19:

    scene bg school_dormhisao
    with locationskip
    
    play sound sfx_doorknock2

    #centered "*Thump* *thump* *thump*"

    "I look up from the textbook in front of me with lifeless eyes."

    "Two bets who that could be."

    hi "Hold on, I'm coming."

    "I turn and walk to the door, running a hand through my messy hair to try and make myself look somewhat presentable."
    
    play sound sfx_dooropen
    
    scene bg school_dormhallway
    with locationchange

    "With a familiar clank, the door opens to a familiar figure."
    
    play music music_kenji fadein 1.0
    
    show kenji neutral
    with charaenter

    hi "Hey, Kenji."
    
    show kenji tsun
    with charachange
    
    ke "Hey… woah."

    "I look up at him through a lowered brow."

    hi "Huh?"

    ke "Jesus man, you look like shit."

    hi "Thanks. I try my best."
    
    show kenji neutral
    with charachange

    "His eyes narrow."

    "Oh god, here we go."

    ke "Man, have you been eating from the cafeteria?"

    hi "Huh? No, I haven't."
    
    show kenji happy
    with charachange

    ke "Good, good. I see you're aware of their foothold there then."

    hi "“their?”"
    
    show kenji neutral
    with charachange

    ke "The feminist legion."

    hi "I should have guessed."
    
    show kenji happy
    with charachange

    ke "Okay, this is good, they haven't gotten to—{w=.3}{nw}" #reminder for the potential {nw} break
    
    show kenji tsun
    with charachange

    ke "Wait, no, this is bad."
    
    show kenji rage
    with charachange

    ke "Damn man, this is really bad. Do you know how bad this is?"

    hi "No, I do not."
    
    show kenji tsun
    with charachange

    ke "It's bad man. Real bad."

    ke "This means their influence has extended outside the school."

    ke "Where'd you get your meals from dude?"

    hi "Aura-Mart."

    ke "Aura-Mart…"
    
    show kenji neutral
    with charachange

    ke "Right. That makes sense. It looks like my predictions are proving right, though they're moving faster than I expected."
    
    show kenji tsun
    with charachange

    ke "Things are moving fast. Too fast."

    hi "What the hell are you on about?"

    ke "They're poisoning you man. They're poisoning you, me, and any man that eats food that they control the making of."

    ke "These are dark days. Thank god for my cache."

    hi "They're poisoning men, but not women?"
    
    show kenji neutral
    with charachange

    ke "Yeah man. It's all part of their plan. Get rid of the guys, and they'll be free to lord over anyone left in the wake."
    
    show kenji tsun
    with charachange

    "He suddenly sinks into deep thought, seemingly forgetting my presence."

    ke "It looks like they made unexpected headway into the gender-targeting toxins."

    ke "Damn, I need to come up with a plan. We need to come up with a plan."

    hi "Kenji."

    ke "Yeah?"
    
    $ renpy.music.set_volume(0.000001, 1.0, channel='music')
    
    hi "I'm not in the mood for this shit."
    
    show kenji surprised
    with charachange

    "Silence."

    "It's probably the first silence I've ever had around Kenji."

    hi "Sorry, I'm just tired."
    
    $ renpy.music.set_volume(1.0, 10.0, channel='music')
    
    show kenji tsun
    with charachange

    ke "Yeah, you look it."

    hi "What'd you come here for, anyway?"
    
    show kenji neutral
    with charachange

    ke "Uh, just returning that book you gave me."

    hi "Book?"

    "My gaze shifts to his hand, a hitherto unnoticed thick textbook clutched by it."

    hi "Ah, the one I lent you."
    
    show kenji happy
    with charachange

    ke "Yeah. Here man, thanks for the lend."

    hi "Nah, it's nothing."

    "With that, he hands me the heavy book."

    "The weight of it's enough to make me momentarily lower it in surprise."

    hi "Anything else?"
    
    show kenji neutral
    with charachange

    ke "Nah man, I'm good. You, though, need to lay off the food for a while."

    "It takes a second for me to click exactly what he means."

    "Dammit, Kenji."

    hi "Thanks, I'll be sure to. See you."
    
    stop music fadeout 3.0
    
    play sound sfx_doorclose
    
    scene bg school_dormhisao
    with locationchange

    "With that, the door closes."

    "Great, now I'm taking out my lack of sleep on other people."

    "Come on, you can do better than this, Hisao."

    "I rub my eyes in frustration as I lay the book on the desk and check the clock next to my bed."

    "Ten in the morning."

    "I suppose the hospital visiting hours would have started by now."

    # If not handled with CG

    scene bg hosp_hallway
    with shorttimeskip
    
    play music music_night fadein 0.1

    "I stand outside the hospital room door, I hear a muffled conversation from inside."
    
    show bg hosp_hallway at bgright
    with charamove

    "Leaning in and making sure to stay dead silent, I try to work out who it is."

    "…"

    "Hanako."

    "I guess it'd make sense for her to visit as soon as she could."
    
    play sound sfx_dooropen

    "I gently open the door, and take a quick glance inside."

    show bg hosp_room2 at bgleft
    show hanako emb_downtimid_cas at tworightsit
    show lilly basic_listen_pat at twoleftsit
    with locationchange

    "Sure enough, Hanako's sitting beside Lilly."

    hi "'Morning Hanako, Lilly."
    
    show hanako emb_emb_cas at tworightsit
    show lilly basic_smile_pat at twoleftsit
    with charachange

    li "Ah, good morning Hisao."

    "She seems much more spritely today, though her voice is incredibly quiet."

    "The sight of her happy face all but removes the irritation of earlier this morning."

    "As Hanako gives a polite nod, I lean against the wall next to her."

    hi "How're you feeling today?"
    
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange

    li "A fair bit better."
    
    show hanako emb_smile_cas at tworightsit
    with charachange

    ha "She should be out in a week, the doctors said."

    "Hanako expertly takes over as Lilly rests her throat. I guess speaking must still be painful for her."

    hi "Ah, that's good. Surgery go well?"
    
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange

    "She gives a silent nod, seizing on the opportunity to give an answer without using her voice."

    ha "Did it hurt?"
    
    show lilly basic_reminisce_pat at twoleftsit
    with charachange

    li "Well, I'd be lying if I said it didn't."
    
    show hanako emb_downtimid_cas at tworightsit
    with charachange

    "The statement causes Hanako to lower her head in silence."
    
    show lilly basic_smile_pat at twoleftsit
    with charachange
    
    li "Ah, it didn't hurt that much though. After a few hours, there wasn't much pain."
    
    show hanako emb_timid_cas at tworightsit
    with charachange

    "Hanako lifts her head slightly, but still looks downtrodden."

    "It's all too obvious obvious Lilly's downplaying it, and covering up her accidentally honest reply."

    hi "Heard from Hanako about what's been going on in the school so far?"
    
    show lilly basic_weaksmile_pat at twoleftsit
    with charachange

    li "Mm, she's given me quite a good report."
    
    stop music fadeout 10.0

    "Something about her tone of voice as she says it doesn't quite sound right."

    "Ah. So that's it."

    hi "Hey, Hanako?"
    
    show hanako cover_worry_cas at tworightsit
    with charachange

    ha "Hmm?"

    hi "Would you be able to grab a couple of drinks from the shop downstairs?"
    
    show hanako basic_worry_cas at tworightsit
    show lilly basic_listen_pat at twoleftsit
    with charachange

    ha "Ah, sure. I'll go get them."
    
    show hanako basic_worry_cas at tworight
    with charamove
    
    play sound sfx_doorclose
    
    show hanako invis at right
    with dissolvecharamove

    "With that, she stands and leaves the room."
    
    show bg hosp_room2 at center
    show lilly basic_listen_pat at centersit
    with charamove

    "I slump into the seat she'd occupied next to the bed, thankful for a chance to rest my legs."
    
    show lilly basic_weaksmile_pat at centersit
    with charachange

    li "Thank you, Hisao."

    hi "No problem. What's on your mind?"
    
    show lilly basic_oops_pat at centersit
    with charachange
    
    play music music_friendship fadein 3.0

    li "How have you and Hanako been doing?"

    hi "How've we been doing?"
    
    li "I'm worried about her."

    li "I wanted to ask you, as I don't think she would give a truthful answer."

    li "I need you to take care of her while I can't."

    #"Even as she says it, her face is one of concern."

    return

label en_choiceL19:
    # Choice
    # [1] - "You're the one that's injured here."
    # [2] - "I'll take good care of her."
    menu:
        with menueffect

        "Even as she says it, her face is one of concern."

        "You're the one that's injured here.":
            return m1

        "I'll take good care of her.":
            return m2

label en_L19a:
    # Choice [1]

    "My eye twitches slightly in annoyance."

    "Dressed in the white of her hospital gown, her mind is still on others."

    "It's close to maddening."

    hi "You're the one that's injured here, Lilly."

    li "Hmm?"

    "Her expression becomes entirely lost."

    "I guess she hadn't expected me to take her up on it."

    hi "You need to worry about yourself more."

    hi "Every time I talk to you, you think of others. Of how Hanako's doing, or how Yuuko's been."

    hi "Stop it."

    "Huh. That was somewhat more blunt than I'd expected."

    "As I look towards her in trepidation, her face seems to be surprisingly accepting."

    "A choking silence."

    "A shield, making her all but incalculable."

    hi "Sorry. I haven't had a lot of sleep recently."

    hi "I guess I'm kind of grumpy."

    "She shakes her head."

    li "No. That's fine. Thank you, Hisao."

    "Even as she says such a simple, short sentence, she seems distracted."

    "Why can't I figure out what she's thinking?"

    "Until now she's never hidden her feelings, but as she lies there in her bleached white gown, I can't work out a single thing she's thinking."

    "It's infuriating."

    "This girl lying in front of me is infuriating."

    "More infuriating than anything in my life."

    hi "Why?"

    li "Hmm?"

    hi "Why are you not talking?"

    hi "Why aren't you telling me what's wrong?"

    "I suddenly find myself arched over her bed, staring directly into her unseeing eyes."

    "But I don't care."

    "There is only one thing that matters."

    hi "Tell me Lilly, what's wrong!?"

    "Silence falls."

    "She looks up, a blank expression on her face as she finds herself completely lost for words."

    li "Hi… sao…"

    "As she takes a moment to collect herself, I do the same."

    "I fall back into the chair with a long breath."

    li "<Alone.>"

    "She says the word in English, continuing in Japanese."

    li "Yes, that's the key word, the most awful word in the English tongue. Murder doesn't hold a candle to it and hell is only a poor synonym."

    "What in the world…"

    "As I open my mouth to respond, the door opens."

    "Through it comes Hanako, awkwardly carrying three cans of soda."

    # "Soda"? And you Americans still call that thing you speak English?

    li "Thank you, Hanako."

    "As I look back to Lilly, her face is exactly the same as it had been when I walked in."

    hi "Thanks, Hanako."

    "She quickly shakes her head from side to side."

    ha "It's okay."

    "As I get out of the seat and motion for Hanako to take it, I take one of the cans."

    "She and Lilly return to talking about various trivialties."

    "School. The drinks. Lunch. Visiting."

    "I quietly watch them as I sip."

    "Instead of clarification, everything's just become even murkier."

    "Though… I think I can figure her out."

    "I need to be there. To act. To do something."

    "All that remains, is… what do I need to do?"

    scene black
    with dissolve

    return

label en_L19b:

    # Choice [2]

    "I smile deeply."

    hi "I'll take good care of her."
    
    show lilly basic_smile_pat at centersit
    with charachange

    "As she grins, her smile matches mine."

    li "Thank you, Hisao."

    hi "It's nothing."

    hi "I'm surprised by how well she's been coping."
    
    li "It's thanks to you, Hisao."

    hi "I still don't think I helped that much."
    
    show lilly basic_weaksmile_pat at centersit
    with charachange

    "She shakes her head gently."

    li "You've been everything you could be for her."

    li "Thank you."

    "I blush slightly and turn away in embarassment."

    hi "I—I wasn't trying or anything."
    
    show lilly basic_giggle_pat at centersit
    with charachange

    "She giggles lightly."

    li "Nonetheless, even without trying you've been there for her."
    
    show lilly basic_smile_pat at centersit
    with charachange

    li "I'm glad."
    
    #stop music fadeout 4.0

    "With that, our conversation drifts the trivialties of the day."

    "School. Lunch. Visiting."

    "To be able to enjoy such small talk with her."

    "If only I were able to do the same thing with Hanako."
    
    play sound sfx_dooropen
    
    show bg hosp_room2 at bgleft
    show hanako emb_timid_cas at tworight
    show lilly basic_smile_pat at twoleftsit
    with dissolvecharamove
    
    #play music music_dreamy fadein 3.0

    "It doesn't take long before the door opens, with the girl herself coming in through."

    "With the cans of soda pecariously held in her arms, I quickly get off the chair and move over to free her of them."

    li "Thank you, Hanako."

    hi "Yeah, thanks Hanako."
    
    show hanako basic_bashful_cas at tworight
    with charachange

    "She vigorously shakes her head from side to side."

    ha "It's okay."
    
    show hanako emb_emb_cas at tworightsit
    with dissolvecharamove

    "With that, she returns to her seat."

    "I quietly sip from the can as I watch Hanako and Lilly talking."
    
    stop music fadeout 3.0

    "She does seem to be coping well."

    "Maybe Lilly had a point."

    scene black
    with dissolve

    return