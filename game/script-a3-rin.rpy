#I switched the intro of R19 and R20, (so actually first you saw the Mutou speech part, and the next scene started with the nurse), to maintain coherence. - Kelper


label en_R19:
    #Obviously open this scene with the title card of Act III, "Distance",
    #unless I-machine handles that and not the script
    # imachine.rpy. d.

    #beepbeep etc

    window hide None
    scene black with fade
    play sound sfx_alarmclock
    $ renpy.pause (1.5)
    scene bg school_dormhisao with openeye
    
    window show dissolve
    
    "The alarm clock rings too early for me."

    "I couldn't get sleep yesterday night, for what feels like the millionth time in my time here."

    "At least it's the too manyeth."

    "Still, I dress up and diligently take my morning medications."

    "In my tired state, I almost manage to forget my appointment with the nurse."

    #ftb whatever
    #nk office

    scene bg school_nurseoffice 
    show nurse neutral
    with shorttimeskip
    play music music_nurse fadein 0.5
    
    nk "So, have you been better now?"

    hi "Yeah, I think I have."

    nk "Is the new medication working?"
    
    nk "No strange pains, nightmares?"
    
    hi "None."

    show nurse fabulous with charachange
    
    nk "What about your insomnia?"

    hi "Ah… that's still there, but it's better now."

    show nurse concern with charachange
    
    "He looks a bit concerned, scrubbing the light stubble in his chin thoughtfully."

    "I get the feeling that he is trying to figure out what I am thinking, with the way he looks at me and the sudden silence."

    show nurse neutral with charachange
    
    nk "I could try to consult your doctor about a sleeping medication that wouldn't have contraindications with your heart medications, if you'd like."

    hi "No thanks. I think I'm eating enough of that stuff already, and it's not that bad. I'm just a bit tired during the day but it's fine."

    #chime
    
    play sound sfx_warningbell

    "The call for class gives the nurse precious little time to argue with me, for which I am glad."

    "He sighs deep and turns to his computer."

    show nurse fabulous with charachange
    
    stop music fadeout 4.0
    
    nk "Right, get going then. Come see me if anything new happens."

    "I nod, pick up my bag and quickly hurry upstairs."
    
    #ftb?
    #classroom

    #A ftb or something to disjoint the preceding part from the following

    scene bg school_scienceroom with fade 
    
    "..."
    
    scene bg school_classroomart with shorttimeskip
    
    play music music_daily fadein 1.0
    
    "I walk straight to the art club classroom after the classes are over."

    "Rin is already there, slumped on her seat and resting her head against the desktop."

    scene bg school_classroomart at right with dissolvecharamove
    
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charaenter
    
    hi "Hi."

    rin "Do something else. I'm trying to listen."

    "Her impoliteness is extraordinarily snappy today."

    hi "To what?"

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "The desk sounds different. It's like the sounds are coming from another world or something. Maybe they are."

    hi "No, I think it's because solid matter transfers sound much better than air. It's amplified."

    hi "That's why the indians listen to the ground for the the buffalos."

    show rin negative_annoyed_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    "Rin abruptly sits upright and turns to look at me with a sour look on her face."

    rin "That's why I think science should be banned."

    rin "It takes the mystery out of everything."

    hi "Would you still like to believe that thunder is caused by angry gods then?"

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "I don't see any problem with that."

    "She is like a child, arguing against reason just because it doesn't suit her current mental state."

    "I don't understand."

    "The teacher arrives, carrying a marble bust of some woman and a vase with red roses on a big wooden tray."

    "He seems to have trouble keeping all of that in balance, so he is striding carefully, which doesn't prevent him from smiling brightly from behind the expressionless bust."

    scene bg school_classroomart at left 
    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) 
    with dissolvecharamove
    
    show nomiya talk at left with charaenter
    
    no "Hello everyone!"

    "How on earth is he always so positive, except when he is giving feedback to us?"

    "It's like he has two personalities, one a jovial and friendly high school teacher and another a bitter and cruel art critic."

    show nomiya smile at left with charachange
    
    no "Today we are going to draw still life. Form two groups and gather around one of these objects."
    
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) with charachange

    no "Practice perspective, shading and proportion."
    
    hide nomiya with charaexit
    scene bg school_classroomart at right
    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    with dissolvecharamove

    show rin basic_deadpancontemplation_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange

    "I look at Rin to see if she prefers one of the subjects over the other, but she just tilts her head, signifying nothing like that one zen expression."
    
    "The club members quickly shuffle their chairs around the classroom to get closer to either the vase or the bust."

    show rin relaxed_sleepy_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    scene bg school_classroomart
    show rin relaxed_sleepy_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8)     
    with dissolvecharamove
    
    "We, or rather I, choose the vase and set to work."

    "…"

    "Well, half of us."

    "Rin is ignoring Nomiya's assignment just like she is suddenly ignoring me."

    "She is doodling something idly with her foot, not even looking at what she is drawing."

    "I try to catch her eyes, but she is looking out of the window."

    "…"

    "Rin's presence is making me uneasy."

    show rin basic_lucid_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charachange

    "She looks almost like she is asleep, leaning back against the chair with her legs resting easily on the desk, now completely given up on the drawing."

    "I don't think that she is acting any different than usual, but after what happened last week…"

    "The more I try to relax and just be myself, the more it feels that something is wrong."

    "I feel that there should be… something, but there is nothing."
    
    show rin relaxed_sleepy_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.7, ypos=0.8) with charachange
    
    rin "What's that word for when you think that you have forgotten something special and you know that if you knew where to start from you'd know how to track the lost thing through your mind?"

    "While her conversation-opener is just as nonsensical as usual, it makes me wonder what her habit of asking other people about words means."

    scene bg school_classroomart at right
    show rin relaxed_sleepy_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)     
    with dissolvecharamove
    
    hi "I don't think there is a word for that… or at least I don't know one."
    
    rin "What about the one for when you are thinking only about one person all the time and nothing else and it makes your stomach hurt and there are stars and possibly even moons in your eyes."

    hi "Lovesick, maybe?"

    show rin relaxed_doubt_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    "Rin furrows her brows and humphs at my answer."

    rin "Why is it so negative? Why sick?"

    hi "Damn, I am no etymologist. Why are you asking me this?"

    "She takes my outburst without as much as a blink of an eye, cooling my temper instantly, and stupidly enough, compelling me to think about the matter even though I don't care about it at all."

    hi "I don't know, probably because of unrequited love and stuff like that. You know."

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "I don't know."

    hi "Uhh… you are not making this easy. Well, I guess that love can be a negative power as well as a positive one or something… damn that sounded cheesy."

    hi "Errr, it makes your brain go all awry. You can't think straight so it's like you are a bit ill… damned if I know."

    "This is so awkward. I stammer with my words and the topic makes me uncomfortable in other ways too. I hope I am not blushing."

    "Rin is her usual calm self, not apparently seeing anything problematic with the situation, which leaves me wondering…"

    "Are we talking about us two specifically, or more generally?"

    "And love… just a few days ago it was just friends."

    "Or is she just playing with me? I can't imagine Rin would do anything like that."

    "Aah, it's driving me crazy."

    "I realize that once again, I have all but given up on actually working on the teacher's assignment in favour of prattling with Rin."

    "I glance at Nomiya, who is shooting disapproving glances at us because clearly neither of us is doing what we are supposed to do."

    hi "Are you going to tell the teacher?"

    show rin basic_surprised_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "You think he doesn't know what a lovesick is?"

    show rin basic_deadpancontemplation_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "Then again, he looks like he might not know. You could have a point"

    "Rin's flexibility at moving from one conversation topic to another is strangely lost when someone else initiates the change of direction."

    "Maybe she has a true one-tracked mind. Can't think of anything but one thing at a time, and when it changes, she forgets about the previous one."

    hi "Not that, about your decision to try getting your paintings on show."

    show rin basic_deadpannormal_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    rin "Oh. I think so."

    "True enough, as the rest of the art class files out of the room, Rin and I stay behind."

    scene bg school_classroomart at left
    show rin basic_deadpannormal_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8)
    with dissolvecharamove
    
    show nomiya dreamy at left with charaenter
    
    rin "Teach."

    rin "I will do it."

    "Nomiya, who was humming to himself while sorting the pencils, turns around with a mixed expression of friendliness and incomprehension on his face."

    show nomiya smile at left with charachange
    
    no "Hmm? I'm not sure if I follow you."

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) with charachange
    
    rin "The gallery person. I can talk with that person. At least yesterday I thought I could."
    
    show rin negative_spaciness_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) with charachange
    
    rin "And today too."

    show rin negative_worried_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) with charachange
    
    rin "I think."

    show nomiya veryhappy at left with charachange
    
    "Nomiya looks over Rin's shoulders at me with a wide smile on his face, but I can only shrug out of modesty."

    "He turns back to Rin, positively beaming."

    show nomiya talk at left with charachange
    
    no "Oh, wonderful! I had almost lost hope!"

    show rin basic_absent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8)
    show nomiya smile at left
    with charachange
    
    no "You are such a hardheaded girl, you are! But I knew that sooner or later you'd understand as well!"

    show nomiya talk at left with charachange
    
    no "I will call to my good friend Saionji and arrange a meeting."

    no "You will need to show your work to her so she can estimate it."

    "Nomiya is talking more to himself than to us and walking in circles around his desk, all the while waving his hands around wildly."

    show nomiya smile at left with charachange
    
    no "You have the paintings in your room, right?"

    show rin basic_awayabsent_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) with charachange
    
    rin "No, but I know where to find them."

    no "You should collect some kind of a portfolio to show to Sae."

    show rin relaxed_nonchalant_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) with charachange
    
    rin "Tomorrow."

    "Rin's nonchalantness is a striking foil to Nomiya's over the top enthusiasm, but neither seems to mind the other."

    no "Very good, very good indeed."

    no "If she accepts you, we can pick the pieces for the actual exhibit together."

    show nomiya talk at left with charachange
    
    no "Let's hope that she will be as enchanted by your talent as all are."
    
    show rin relaxed_doubt_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.8, ypos=0.8) with charachange

    no "Not to get your hopes too high, but I'm sure she'll like them. I have known her for a long time and we are good friends."

    show nomiya smile at left with charachange
    
    no "Well then, I shall go downstairs and make the call. Have a nice day, both of you!"

    hide nomiya with charaexit
    $ renpy.pause(0.5)
    scene bg school_classroomart at right
    show rin relaxed_doubt_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) 
    with dissolvecharamove
    
    stop music fadeout 6.0
    
    "He bustles out of the room and disappears into the hallway."

    show rin relaxed_boredom_close at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8) with charachange
    
    "I can only look questioningly at Rin, who only shrugs her shoulders in the familiar, bored manner."

    window hide dissolve
    scene black with Dissolve(1.5)
    
    return

label en_R20:

    #I don't want ??? to say the next two lines, so what to do? Centered? Or just text box?
    
    scene black
    $ renpy.pause(0.5)
    
    
    centered "Nakai." with dissolve
    $ renpy.pause(0.5)

    centered "{size=36}Nakai!{/size}" with vpunch
    
    
    scene bg school_scienceroom
    show muto irritated
    with openeye
    #classroom and sprites
    play music music_happiness fadein 0.5
    
    window show dissolve
    mu "I asked you a question."
    
    "I shake my head to shake off the dizziness. The teacher is looking at me, and so is everyone else in the class."

    hi "Ah, sorry. I wasn't paying attention."

    "To be honest, I think I was sleeping."

    #"The new medication doesn't seem to be working, or something else is wrong."

    #edition:
    "The nurse changed my old medication to get rid of the side effects."
    
    "But the new medication isn't doing anything about my insomnia"
    
    #end of edition
    
    "I am still so sleepy at days and I have a hard time to get any sleep at nights."

    "At least the nightmares and strange pains are gone."

    "Mutou clears his throat and picks the piece of chalk he had dropped, but doesn't continue from where he left."

    show muto smile with charachange
    
    mu "Knowledge is the base of understanding."

    mu "This is the secondary reason for you being in the school. To acquire knowledge."

    show muto normal with charachange

    mu "The primary one is to learn the rules of society, the norms and ethics that govern your everyday life."

    mu "You do not come to school for the classes, you come to interact with the other people, your classmates who are your equals and the teachers who are your superiors."

    mu "You learn how to form social contacts and maintain them, in other words how to be a part of the society. The school is a microcosm of the entire society."

    show muto smile with charachange

    mu "Locke was the one who realized that, you know? School is not just a place for learning, and you guys of all the kids your age should know that, better than anyone else."

    "He pauses for a moment and lets his eyes sweep over the class to see if the message sunk in."

    "At least everyone shut up and is now staring at him silently, captivated by either his voice or the sudden change of topic from physics to the philosophy of education."

    #emphasize (bold, caps whatever) the word "however" here

    show muto normal with charachange

    mu "{b}However{/b}, my classes are a place for learning."

    "He points at me with the chalk and winks."

    show muto smile with charachange

    mu "So, no sleeping during class. Got it, Nakai?"

    hi "Yes, sir."

    stop music fadeout 5.0
    
    "So his entire tirade was just build-up for scolding me? Unbelievable."

    "And I almost started thinking he had something wise to say…"

    "…"

    scene bg school_scienceroom with shorttimeskip
    
    play music music_normal fadein 0.5

    "The afternoon class is awful. I just want to stand up and walk out of the classroom without caring what the teacher or anyone says."

    "It's not that the lesson is bad, but it's not interesting at all and the classroom is so hot that I feel like I am melting."

    "It's funny. I remember how badly I wanted to get out of the hospital and go back to school."

    "Now, all I can think is the upcoming summer vacation and freedom from the classes and homework."

    "Am I this indecisive?"

    "No, maybe it's the human nature to think only of the situation at hand."

    "At any rate, the heat of the midsummer is unbearable. Students and teachers alike are in almost a delirious state."

    "I can see my feelings being mirrored on almost everyone else's faces."
    
    play sound sfx_normalbell
    $ renpy.pause(0.8)

    #play the end of class tune
    
    scene bg school_hallway3 with locationskip
    play ambient sfx_crowd_indoors
    show crowd with dissolve

    "The hallway is much cooler than the classroom, I notice."

    show emi basic_closedgrin at twoleft        
    show rin basic_awayabsent at tworight
    with dissolve
    
    "In front of the 3-4 classroom, Emi and Rin are having half-animated discussion."

    "Emi is jumping up and down, gesturing something with her hands while she talks, almost like my deaf classmates, while Rin is standing stoically in the middle of the hallway like a statue."

    show emi invis at leftoff with dissolvecharamove
    
    "Emi waves Rin goodbye and dashes past me towards the stairwell. She was in such a hurry she doesn't even notice me."

    #"Rin stays in her place for a moment, then turns around and walks past the art club room towards the end of the hall."
    #edited line: 
    
    "Rin stays in her place for a moment, then turns around and walks towards the end of the hall to the art club room."
        
    show rin invis at rightedge with dissolvecharamove

    "She didn't notice me, either."

    #"For the lack of anything better to do, I follow her to the to the door of the abandoned classroom in the end of the hall."
    #edited line: 
    "For the lack of anything better to do, I follow her."
    
    hide crowd with dissolve

    "She pushes the door open and steps in."

    "I stop in front of the closed door."

    "It reminds me of the last time I stumbled into this room and interrupted Rin's lunch."
    #Flagging this for possible review considering A15-16

    stop music fadeout 4.0

    "That was the first time we met."

    "This time, I'm prepared so I knock lightly on the door and enter."
    
   
    play sound sfx_hammer
    $ renpy.pause(1.5)
    play sound sfx_dooropen 
    $ renpy.pause(0.8)
    scene bg school_classroomart at left with locationchange
    stop ambient fadeout 0.5 
    $ renpy.pause(1.0)

    play music music_soothing fadein 0.5
    
    #"The strange atmosphere of this room is exactly like I remembered."
    #edited line:
    
    "The strange atmosphere is exactly like I remembered."
    
    "The dust floating in the stagnant air scatters the sunlight sneaking in from between the curtains to every direction."

    "It doesn't get too far in before the darkness swallows it."

    #"The smell of dust and chalk reminds me more of an ages-old library than a school classroom, no matter how long it has been unused."

    "I wasn't surprised by Rin's presence this time, but it also seems that she didn't even notice me entering."

    "She is standing in the middle of the room with her back to me, looking like she is petrified."

    "The narrow beams of light are playing on her features, making her look a bit mysterious."

    "A figure shrouded in mystery."

    scene bg school_classroomart at right with dissolvecharamove
    
    hi "Hi."

    show rin basic_awayabsent with charaenter
    
    "Rin doesn't wake up from her thoughts so I walk up to her to see what she is doing."
    
    "There is a big stack of paintings on the floor in front of her."

    "Rin is intently looking at the topmost one, even though the shadows of the room make it hard to see the colours clearly."

    "After a moment, she picks the corner of the paper between her toes and moves it to her right side."

    "The next painting is moved on top of the previous one with considerably less time spent on studying it, but the third one is moved to Rin's left side instead."

    "The silence makes me want to talk about something."

    hi "Did the teacher get you an appointment with that gallerist?"

    show rin basic_absent with charachange
    
    rin "Tomorrow."

    hi "So soon? He sure doesn't waste time."

    show rin basic_deadpannormal with charachange
    
    rin "I guess not."

    "The fourth and fifth paintings go to left side, and the sixth goes to right again."

    hi "So what're you doing?"

    show rin basic_absent with charachange
    
    rin "He said I have to pick a portfolio. So I am picking a portfolio."

    hi "You keep your paintings here? But what if someone steals them or something?"

    show rin relaxed_surprised with charachange
    
    rin "Who?"

    hi "I don't know… someone."

    show rin basic_deadpancontemplation with charachange
    
    rin "Why would a someone do that?"

    hi "Well, why do people steal anything…"

    show rin basic_deadpannormal with charachange
    
    rin "That's what I'm asking."

    hi "Fine, forget it."

    show rin basic_deadpanupset with charachange
    
    rin "Okay."

    "The seventh painting goes to the right side."

    hi "Which side is the “approved” pile?"

    show rin basic_surprised with charachange
    
    rin "Right, obviously."

    "Obviously."

    show rin basic_awayabsent with charachange
    
    "The next painting to be judged is the one that I saw Rin painting in art class a few weeks ago."

    "It goes to the right side."

    hi "So… where do you get your ideas?"

    show rin negative_spaciness with charachange
    
    rin "Don't you know that that is the fifth stupidest question you can ask?"

    hi "Yeah, I do… well no I didn't. What are the first four?"

    show rin negative_annoyed with charachange

    $ renpy.pause(2.5)
    
    #"…"

    hi "Anyway, I felt like asking it anyway."

    show rin basic_lucid with charachange
    
    "Rin breathes out very deeply before answering. Maybe it's a sign of disapproval or something."

    rin "Sometimes… I see or hear or think or speak or remember or dream things that feel like they could be important."

    show rin basic_awayabsent with charachange
    
    rin "Then I paint."

    "She is still leaving the critical part off. The transformation from idea to art, what is that process?"

    "I don't understand."

    "Maybe stuff like this is not something that can be rationally understood."

    "Rin's paintings are so… odd, dreamlike… damn, I can't even come up with a good adjective to describe them."

    "They must be some of the strangest pictures I have seen like… ever, but even so, many of them are very beautiful."

    hi "So you paint dreams, huh?"

    show rin basic_absent with charachange
    
    rin "If I feel like it."

    rin "Dreams sometimes feel real. Those kinds of dreams are good to paint."

    "I shrudder, remembering my nightmares from the first weeks here."

    show rin basic_awayabsent with charachange
    
    rin "What's that word for when you wake up and you are not sure if you are still dreaming?"

    hi "I don't think there is a single word for that… but isn't that sort of like that old philosophy riddle?"

    hi "You know, are you a butterfly dreaming of being Rin who is painting a dream of being the butterfly, or vice versa?"

    show rin basic_deadpancontemplation with charachange
    with Pause(0.8)
    show rin basic_absent with charachange
    
    "Rin furrows her brow for a moment, but then her expression relaxes to its usual pokerface."

    rin "Huh… that was pretty complicated."

    "I feel a smug satisfaction for getting back at Rin for all the confusion her usual banter causes to me."

    rin "I've never dreamt that I'm a butterfly. I was a frog once, though."

    show rin relaxed_doubt with charachange
    
    rin "I was playing with these fairies all night long but one of them rode me around the pond and pulled my hair even though frogs don't have any to make me go where she wanted."

    rin "That was the last time I let Emi sleep in my bed, no matter how much she complains about being cold."

    show rin relaxed_surprised with charachange
    
    "The idea of Emi pulling Rin's hair in her sleep somehow transferring inside her dreams gives me a laugh, making Rin look at me like I suddenly went crazy."

    show rin basic_awayabsent with charachange
    
    "I wave it away, and she turns back to her paintings."

    "On the bottom of the pile there is a bunch of paintings which are painted only half-way… literally."

    "The paint is covering only half, if even that of the canvas, leaving the rest completely blank without even sketch lines or anything."

    hi "What's up with these? Are they unfinished?"

    show rin basic_absent with charachange
    
    rin "Kind of, like a slice of toast you eat only halfway and then forget somewhere."

    hi "Lost the inspiration?"

    show rin basic_deadpancontemplation with charachange
    
    rin "Yeah. And then I couldn't find it from anywhere."

    rin "I can't even remember what I was trying to do. This one was something about upside down, or raspberry jam."

    show rin basic_deadpannormal with charachange
    
    rin "One or the other, I can't remember."

    hi "Too bad. I like these two."

    "I point to two paintings with nice colours, at least in my opinion."

    show rin basic_absent with charachange
    
    rin "I don't think it is a problem to take them and show to the gallery person… but I don't think she'd like to put them on show."

    show rin basic_awayabsent with charachange
    
    "She moves both of them to the right side pile and the moves to contemplate the next painting in the thinning original pile."

    "Rin is bothering me again, although she obviously doesn't realize it."

    "She is acting like nothing of significance happened last week."

    "The first kiss was understandable in a way… she was not clear in the head, not that she ever is, but…"

    "Maybe I am putting too much significance on a thing like that. It's just that…ah, I don't know."

    "This kind of thing is not something I can say I am good at."

    "The last painting in the original pile is sorted to the left side, leaving us with two new piles."

    "Without prompting, I pick up the approved pile and look at Rin questioningly."

    show rin basic_deadpannormal with charachange
    
    rin "Just put them anywhere."
    
    show bg school_classroomart at left 
    show rin invis at right
    with dissolvecharamove

    "I lay the pile on top of one of the desks and then pick up the other pile, taking it to a corner of the room that Rin shows me, which she is using as a storage."

    stop music fadeout 7.0
    
    "I still feel that this is not the best place in the world to store one's paintings, but who am I to argue with Rin?"

    "She seems to be immune to logical arguments."

    "With the portfolio chosen, we walk downstairs out to the quad."

    scene bg school_courtyard with locationskip

    play music music_ease fadein 0.5
    
    "We walk the cherry tree lined path down to the dorms in silent agreement."

    "I know I have to do some homework, the end of trimester is coming soon, along with exams, but I have no idea what Rin is going to do."

    "She doesn't feel like the type who would study a lot."

    scene bg school_dormext_full with locationchange
    
    "As we reach the girls' dormitory, which unfairly is closer to the school and the hall than the boys', Rin stops in her tracks."

    "I turn to see why, but she just stands there, studying me with her eyes."

    show rin negative_spaciness with charaenter
    
    rin "Will you come to see the gallery person tomorrow?"

    "Huh… I didn't think that I'd go. It's Rin's and the teacher's meeting after all."

    hi "If it's fine with you."

    show rin basic_absent with charachange
    stop music fadeout 5.5
    
    rin "It's fine with me."

    hi "Then I'll come."
    
    window hide dissolve
    with Pause(0.5)
    scene black with Dissolve(1.0)
    
    return

label en_R21:
    
    scene black 
    with Pause(1.0)
    play music music_daily
    
    scene bg school_hallway3 with locationskip
    
    window show dissolve
    
    "The next day after school, Nomiya and Rin are waiting for me in the lobby of the main building."

    scene bg school_lobby with locationchange
    show nomiya talk at twoleft
    show rin basic_awayabsent at tworight
    with charaenter
    
    no "Well hello there, Nakai! Tezuka said that she had invited you along."

    hi "I guess so."

    show rin basic_deadpan at tworight
    show nomiya smile at twoleft
    with charachange
    
    "Rin snorts, like she seems to do almost every time I say “guess.” Her fixation with the word is really strange."

    no "Well then, I'll put you to work straight away. You don't mind carrying these, do you?"
    
    show rin basic_absent at tworight with charachange
  
    "He hands me the stack of paintings he is holding, wrapped in between two thick sheets of cardboard and some brown packing paper."

    show nomiya frown at twoleft with charachange
    
    "I feel pretty honored, having Rin's portfolio trusted on me."

    "Then again, it's really hard to carry because it's so big and cumbersome so probably the teacher just wanted to get himself off the hook."

    $ renpy.music.set_volume(0.6, 0.0, channel='ambient')
    play ambient sfx_traffic fadein 0.5
    scene bg school_road_ss with locationskip    
    
    "The bus stop makes me realize that I haven't been to downtown much."

    stop music fadeout 9.0
    
    "The school and the neighborhood offer almost everything one could need, so there is not much incentive to go elsewhere."

    "I wonder if that's intentional, to keep us on our private island, or just the result of our circumstances."

    stop ambient fadeout 0.5
    scene bg city_busride_ss with locationskip
    play ambient sfx_businterior fadein 0.5
    
    "The suburb on the other side of the bus window slowly changes into the higher buildings of the town center."

    "They are not the towering skyscrapers of the city I used to live in, but it's a downtown, nevertheless."

    stop ambient fadeout 0.5
    scene bg city_busstation_ss with locationchange
    play ambient sfx_traffic fadein 1.0
    $ renpy.music.set_volume(0.5, 0.0, channel='music') 
    play music sfx_crowd_outdoors fadein 1.0

    "We step out of the bus at the central station to meet the afternoon sunlight and the busy atmosphere of the town."

    "I look around to see people walking here and there at an unhurried but determined pace, a flock of pigeons taking flight as a car scares them, the flow of traffic in the roads surrounding the station."

    "It reminds me of everything the city was not."

    "The town is not as bustling as the city. It's more… relaxed, casual."

    "One can walk the streets without being assaulted by noise and color and advertisement from every possible direction."

    "One can look up and see the sky high above the buildings, and breathe more freely than in the city."

    "I can't help thinking that I prefer it this way."

    "Nomiya leads us towards the street on the other side of the station square."
    
    $ renpy.music.set_volume(0.25, 1.0, channel='music') 
    scene bg city_street4_ss at left with locationchange
    
    "The portfolio feels uncomfortably large and I can't really carry it properly."

    "I hope it'll be enough if I make it to the gallery without dropping or creasing it."

    show nomiya frown_ss with charaenter
    
    no "The place is not far away."

    "The streets are not crowded to the choking point, which makes walking more comfortable."

    "I walk besides Nomiya, with Rin following behind us."

    hi "Teacher, does this gallerist know that Rin… you know…"

    hi "…Doesn't have arms?"

    show nomiya smile_ss with charachange 
    
    no "Hmm? No, Tezuka asked me not to tell her about it… I don't really understand but I didn't see any harm… "

    no "Speaking of which, where did Tezuka go?"

    scene bg city_street4_ss at right
    show nomiya invis at left 
    with dissolvecharamove
    
    "We turn around to see Rin just had stopped at the previous street corner, staring at the window of a home electronics store."

    "I walk back to her faster than Nomiya, despite my burden."

    "Something probably just caught Rin's fancy and she forgot that she actually had a destination."

    hi "Is something wrong?"

    show rin basic_awayabsent_ss with charaenter
    
    rin "I don't get it."

    "I follow her eyes to the display window. It seems to be perfectly normal, the kind you see at any store like this."

    hi "What? All I can see is an ad for a free gift if you buy a washing machine."

    show rin basic_absent_ss with charachange
    
    rin "That's the point. Aren't all gifts free?"

    show rin basic_awayabsent_ss with charachange
    
    no "Hey you two, hurry up… it's just around the corner."

    "Nomiya's impatience doesn't give me time to argue, not that I'd had wanted to."

    scene bg gallery_ext_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.60) with locationskip
        
    "Nomiya stops in front of a door just around the next corner."

    "Looking through the windows, the place looks like an art gallery so this is probably the place."

    "There is a nameplate in big, red letters over the door."

    scene bg gallery_ext_ss with dissolvecharamove
    show rin negative_spaciness_ss at tworight
    show nomiya smile_ss at twoleft
    with charaenter
    
    rin "Is this really the 22nd corner?"

    hi "Of what?"

    show rin basic_deadpanupset_ss at tworight with charachange

    rin "That's bothering me too. I mean, where to start counting, and which way do you count?"

    hide nomiya with charaexit
    
    "Rin gets worked up over the strangest things. Unlike me, Nomiya ignores her completely and pushes the door open."
    
    stop music fadeout 0.5
    stop ambient fadeout 0.5
    $ renpy.music.set_volume(1.0, 0.0, channel='music') 
    
    play sound sfx_storebell
    scene bg gallery_int at right with locationchange
    play music music_soothing fadein 0.5
    
    "The gallery is very clean looking, and it's very cool inside."

    "The white walls and big windows giving to the busy street make the place very airy and bright."

    "Most of the space is empty, only a few large tables and a counter are on the floor."

    "There are paintings too, of course. A poster advertises an exhibition of an artist I have never heard of."

    "Most his works seem to be portraits or landscapes, of a more traditional style than Rin's abstraction."

    "There doesn't seem to be anyone around here."

    "Nomiya is trying to locate the staff too, judging from the way he is looking around."

    no "Good afternoon? Hello?"

    play sound sfx_dooropen
    
    "The door in the far corner, probably leading to the back room opens almost instantly, and an aged lady steps through it."

    show sae neutral with charaenter
    
    sa_ "Yes, how may I help…"

    show sae smile with charachange
    
    "She stops midsentence after seeing the teacher and smiles."

    "My initial assessment of a strict business lady is immediately banished."

    sa_ "Ah, it's you Shinichi, and I take these two youngsters are your students."

    scene bg gallery_int
    show sae smile at tworight 
    with dissolvecharamove
    show nomiya smile at twoleft behind sae with charaenter
        
    no "Good afternoon, nice to see you again."

    show sae neutral at tworight with charachange
    
    sa_ "Welcome, everyone."

    "She immediately turns to greet me, fixating her gaze first on the portfolio I'm carrying and then my face."

    "I get the feeling of being scrutinized."

    show sae smile at tworight with charachange
    
    sa_ "Ah, and you must be the person Shinichi has mentioned to me? Funny though…"

    show nomiya frown at twoleft with charachange
    
    no "Ah no, this is another student of mine, he just came along. Tezuka here is the one I told you about."

    "The teacher is surprisingly quick to correct the misunderstanding, redirecting the gallerist's attention to Rin, who is idly looking out of the windows and around the gallery."

    show sae doubt at tworight with charachange
    
    "Sae raises her eyebrows in surprise, and I can tell why."
    
    scene bg gallery_int at left
    show nomiya frown
    show sae doubt at right    
    with dissolvecharamove
    show rin relaxed_nonchalant at left with charaenter

    "She quickly collects herself though, and smiles sweetly at Rin."

    show sae smile at right with charachange
    
    sa_ "Ah, I beg your pardon, my dear. Pleased to meet you. I am Sae Saionji, the proprietor of this place."

    sa "Shinichi has told me a little about you, but obviously not everything so I'm happy to meet you in person."

    show rin basic_awayabsent at left with charachange
    
    "Rin seems to be much more interested in the current exhibition than introductions. She is looking around curiously, taking in the atmosphere of a real art gallery."

    show sae neutral at right with charachange
    
    sa "Would you like to look around while I take a look at your paintings?"

    sa "I'm rather proud of my newest find, he is a young artist as well, not as young as you are… but very promising."

    hide rin with charaexit
    with Pause(0.5)
    show sae doubt at right with charachange
    
    "Rin takes up on the offer without saying a word, going around the corner of the room to the main room where most the paintings seem to be on show."
    
    sa "Now then…"
    
    scene bg gallery_int 
    show nomiya smile at twoleft
    show sae smile at tworight
    with dissolvecharamove
    
    "I follow her to the furthest corner of the gallery and flop the portfolio on the big table standing there."

    "I don't bother going after Rin."

    "She probably is in her own world again, immersed in the art."

    show nomiya stern at twoleft with charachange
    show nomiya serious at twoleft with charachange
    
    "Nomiya gives me a quick look when I don't seem to be leaving anywhere, but doesn't shoo me away."
    
    "He spreads some of the paintings on the tabletop to give a better view for the gallerist."

    show sae scowl at tworight with charachange
    
    "The old lady studies Rin's works carefully, absentmindedly brushing her cheek with her fingers while letting her gaze sweep over the paintings."

    "Her eyes remind me of a bird of prey of some sort, they are so sharp and somehow very calculating."
    
    "She takes her time, slowly going over the paintings in order without uttering a single word. Even the teacher looks very nervous."

    scene bg gallery_int at left
    show sae scowl at right
    show nomiya serious behind sae
    with dissolvecharamove
    
    show rin relaxed_doubt at left with charaenter
    
    rin "Is this really the 22nd corner?"
    
    show nomiya frown     
    show sae neutral at right
    with charachange
    
    "Rin returning from the main gallery room instantly breaks the spell of awkward silence."

    "Sae raises her gaze from the paintings to look at Rin, but doesn't answer."

    "It is probably for the best."

    show sae scowl at right with charachange
    
    "She takes stock of Rin's slouchy posture and her dreamy eyes that are again wandering restlessly about."

    "The way Rin seems to be detached from the situation that is supposed to be very important for her manages to annoy even me."

    "I'm afraid this is not going too well for Rin."

    show sae doubt at right with charachange
    
    sa "Did you paint all these, my dear?"

    "Her tone is friendly, but there is something strange in the way she says it."

    #choice reminder

    hi "Wait, are you implying that because Rin doesn't have arms you have a hard time believing she painted these?"

    show nomiya serious 
    show sae scowl at right
    with charachange
    
    "A terrible silence falls into the gallery. I realize that it probably was not the best thing to say in this situation"

    "A shocked teacher and an insulted gallerist are staring at me, making me want to crawl under a rock to hide."

    show rin relaxed_nonchalant at left with charachange
    
    rin "Yes."

    "Rin is the only one is able to take the situation coolly."

    "Actually, everyone else seems to be at a loss of words."

    "I decide that it's probably better to sit down in the corner for the rest of the meeting."

    hi "Sorry."

    show sae neutral at right with charachange
    
    sa "No matter, but you must forgive me too. Shinichi told me that you were talented, but I have to admit I am a bit taken aback."

    sa "You are still a fledgling and searching for a style, maybe, but some of these are very nice indeed."

    "How come everything the gallerist says sounds patronizing to me? I keep my mouth shut this time, though."

    no "Krhm, anyway…"

    show nomiya smile with charachange
    
    no "What wonderful imagination, isn't it?"

    "The teacher decides that it's time to salvage the situation and draw the attention to Rin's art."

    show nomiya talk with charachange
    
    no "I've always said that Tezuka has great eye for composition and colour harmony."

    no "Of course, we'd need to put some of the simpler ones on display too, for the laypeople, right Sae?"

    "The teacher snorts derisively."

    show nomiya stern with charachange
    
    no "You know those philistines!"

    hide rin with charaexit
    
    no "What do they understand about real art? They'd just be at a loss with the abstractions and themes here!"

    show nomiya talktongue with charachange
    
    no "But it'll generate more publicity, and that is good, isn't it?"
    
    scene bg gallery_int 
    show nomiya smile at twoleft 
    show sae smile at tworight 
    with dissolvecharamove
    
    "The gallerist smiles gently at Nomiya's remark and turns back to the paintings."

    sa "Oh, these look interesting."

    "She is studying the pair of half-way painted paintings that I asked about yesterday when we were sorting the paintings."

    #if one of the editors wants to tell me that because Rin sorted the paintings yesterday, they are now in reverse order and Sae should have seen the half-painted ones first, I swear I will track you down and burn your house

    show nomiya veryhappy at twoleft with charachange
    
    no "Ah yes, wonderful usage of negative space, isn't it? The composition and balance is very unique."

    no "Just lovely, aren't they?"

    show nomiya smile at twoleft
    show sae neutral at tworight 
    with charachange
    
    "The gallerist nods absentmindedly while turning her attention to yet another piece."

    "Rin has disappeared somewhere again, a remarkable feat in a place this small."

    "I wonder if I should tell about the paintings being unfinished."

    #choice reminder

    "Just keep your trap shut. You would only make it worse."

    scene bg gallery_int 
    show nomiya smile at twoleft
    show sae smile at tworight
    with shorttimeskip
    
    "The gallerist and teacher have started talking animatedly about the state of the art community in this area."

    show sae doubt at tworight with charachange
    
    sa "To tell you the truth, there has been a decline of new quality art."

    sa "As you know, I specialize in new and rising artists, but lately…"

    show sae neutral at tworight with charachange
    
    sa "The current exhibit you see has been here for too long, but I haven't got anything to replace it with."

    no "Well then, we are only happy to help you, if you would accept our paintings here."

    show nomiya talk at twoleft with charachange
    
    no "Two birds with one stone and so on."

    "Nomiya laughs half nervously, half brashly."

    show nomiya smile at left
    show sae smile at bgright
    with dissolvecharamove
    show rin basic_absent at right with charaenter
    
    "Rin returns from her second trip to the gallery space and walks straight over to the gallerist."

    rin "Hello. One of the paintings there looked a lot like something I saw last week."

    show rin negative_spaciness at right with charachange
    
    rin "I wonder if any of you could help me to remember what it was?"

    show sae neutral at bgright with charachange
    
    sa "Ahh… I am afraid it might be difficult, but could you tell me something about these paintings of yours?"

    "Now that Rin came back, the gallerist seizes the opportunity to attempt discussing with her."

    "Good luck with that, although her skill at ignoring Rin's irrelevancies is greater than what mine was during the first few times I talked to Rin."

    "Maybe the teacher has warned her beforehand."

    show sae smile at bgright with charachange
    
    sa "Are these all of your works? Or do you have more back at your school?"

    show rin basic_deadpancontemplation at right with charachange
    
    rin "Not many."
    
    show sae doubt at bgright with charachange

    "The gallerist contemplates Rin's curt revelation for a moment."

    sa "I wonder if you could paint some more? If your studies allow, that is."

    show rin basic_deadpannormal at right with charachange
    
    "Rin looks at Nomiya, whose face twists into an ugly frown."

    show nomiya frown at left with charachange
    
    no "Ah, you see… the regulations at Yamaku are very strict, Tezuka doesn't really have any place to paint."
    
    no "The dormitory rooms do not have much space and as you know, inspiration doesn't ask for time."

    show nomiya dreamy at left with charachange
    
    no "So, my art club meetings are not enough, even though they have been instrumental to Tezuka's development as an artist."

    show nomiya smile at left with charachange
    
    no "She has been circumventing the regulations with my silent consent, but I would prefer her not to risk getting caught and suspended."

    show rin basic_absent at right with charachange
    
    rin "The teacher would get in trouble too, since I am using his key."

    "…"

    show nomiya frown at left with charachange
    
    no "Yes, that's correct as well."

    show sae smile at bgright
    show rin basic_awayabsent at right
    with charachange
    
    "The gallerist smiles amusedly at Nomiya's embarrassment and raps the tabletop with her long fingernails."

    sa "Hmm, well that is a problem."

    sa "I see…"

    show sae doubt at bgright with charachange
    
    "She ponders the matter. The mood in the gallery is very tense as we wait for her to say something else."

    show nomiya smile at left with charachange
    
    "Nomiya, enthusiastically expecting good news."

    "Me, holding my breath even though I don't know why."

    "Rin, with that cool attitude of hers that seems to be open to everything but closing her own thoughts inside."

    show sae smile at bgright with charachange
    
    sa "Very well, let me suggest this: I can rent you gallery space for an exhibit of your own."

    show rin basic_deadpannormal at right with charachange
    
    sa "It'll probably have to be only a part of this place, unless you can provide enough works for the entire space."

    show sae neutral at bgright with charachange
    
    sa "As for the rental fee for gallery space, I'm certain that you don't have that kind of money, so would you agree on me “buying” lets say, two of your paintings for my own collection and covering the rent with that?"

    sa "As an gesture of goodwill, I'll pay you generously for them."

    show sae smile at bgright with charachange    
    
    sa "We'll call that… an investment for the future."

    "The gallerist sure seems like a tough businesswoman again, now that she is talking about… well, business."

    show sae scowl at bgright with charachange
    
    sa "I'll take the normal commission for the paintings I manage to sell."

    sa "As for the new paintings… there is an old atelier in the top floor of this building."

    show sae neutral at bgright with charachange
    
    sa "It has not been in use for a while, but if you would like to, you are free to use it as your own."

    hi "Would you really do that?"

    sa "I'm always happy to help young and enthusiastic artists like your friend here."

    show sae smile at bgright with charachange
    
    "She turns back to smile at Rin, whose poker face is impossible to read, at least for me."

    sa "So, Miss Tezuka, what do you say?"

    show nomiya frown at left with charachange
    
    "There is an awkward moment of silent expectation before Rin manages to nod her consent."

    "The gallerist smiles and extends her hand confidently, before pulling it back as if something bit her."

    show sae doubt at bgright with charachange
    
    sa "Oh I'm terribly sorry! Please forgive my rudeness, I completely forgot."

    show rin basic_absent at right with charachange
    
    rin "Don't mind."

    "Sae gives a nervous laugh and tries to collect herself."

    show nomiya smile at left with charachange
    
    no "Should we talk about the specifics now or at a later time? At least Tezuka and me have time now, if you don't mind."

    show sae neutral at bgright with charachange
    
    sa "Yes, I would also have a suggestion regarding those…"

    "The gallerist and the teacher start negotiating about dates and fees between themselves, so I take the opportunity to take a look at the main gallery room."

    scene bg gallery_exhibition at right with shorttimeskipsilent
    
    "The paintings are pretty, and somehow much easier to appreciate than Rin's, even though I think I might prefer hers now that I've gotten used to her."

    "I am glad that Rin's meeting went so smoothly, despite her odd behaviour and my blunder."
    
    "I guess the teacher being friends with the gallerist was a big help."

    stop music fadeout 2.4
    
    "The business talks are quickly over, and Nomiya leads us out of the gallery to the street."
    
    play sound sfx_storebell
    play music music_dreamy fadein 0.5
    scene bg gallery_ext_ss with locationskip
    show nomiya smile_ss at twoleft
    show rin basic_awayabsent_ss at tworight
    with charaenter
       
    "The hot summery town and bright sunlight seem to fit my mood perfectly."

    "The teacher too seems to be in very jolly spirits, actually much more so than Rin herself."

    scene bg city_street4_ss with locationchange
    show nomiya frown_ss 
    with charaenter
    
    "She is walking a few steps behind us like on the way here, contemplating something by herself."
    
    "Nomiya is blabbering about something about wonderful and amazing that I'm not listening to, just responding with nods and unintelligible mumbling at appropriate places."
    
    "When he finishes, I slow down my steps so that Rin catches up with me."

    scene bg city_street4_ss at left
    show nomiya invis at right
    with dissolvecharamove
    show rin relaxed_nonchalant_ss with charaenter
    with Pause(0.6)
    
    hi "Why did you constantly wander off back there? You should've talked more with the gallerist lady. She was really nice."

    show rin relaxed_doubt_ss with charachange
    
    rin "I didn't want to look at her looking at them."

    rin "It was like looking at your own autopsy."

    hi "Were you actually nervous about this whole deal?"

    "Well, I suppose Rin has been unusually quiet for the whole day."

    show rin negative_spaciness_ss with charachange
    
    rin "I don't know. I just didn't want to."

    "It is somehow very unlike her to be like this, but I can't help feeling happy for her."

    "For some reason, Rin is still very quiet and thoughtful."

    hi "Hey, you got a deal for your own art exhibition in a real gallery!"

    hi "Aren't you happy?"

    stop music fadeout 6.0
    
    "Rin glances at me from the corner of her eye, looking tentative."

    show rin negative_confused_ss with charachange
    
    rin "I don't know."
    
    window hide dissolve
    scene black with Dissolve(1.5)  
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    return

label en_R22:
    
    scene black 
    play music music_pearly fadein 0.5
    with Pause(1.0)
 
    scene bg school_dormhisao
    with locationskip

    window show dissolve
    
    "I wonder how Rin will cope with the stress."

    scene bg school_dormbathroom
    with locationskip

    "Actually, I wonder if she is one to get stressed in the first place."

    scene bg school_courtyard
    with locationskip

    "I would, but she is not me."

    scene bg school_scienceroom
    with locationskip

    "The exhibition opening is going to be in a month's time, and Rin promised to paint a few more works for the opening."

    "I guess she has to work hard to get the paintings done."

    "The exams are coming up too, but Rin doesn't seem to be the kind who'd stress over stuff like that."

    "She probably just wings most of her exams."

    "At lunch break, I'll go and talk with her about it."

    "Maybe she'd like to eat lunch with me or something."
    
    scene bg school_hallway3 with shorttimeskip

    "Because of Mutou's laxness I have time to get out of the classroom and walk to the door of 3-4 before the lunch bells actually ring."
    
    play sound sfx_normalbell
    with Pause(0.8)
    play ambient sfx_crowd_indoors fadein 1.0
    show crowd with Dissolve(1.0)
           
    "Emi emerges from the classroom along with her classmates, but Rin is not with her."

    "She notices my handwave and skips to me."
    
    show emi basic_happy with charaenter
           
    emi "Hi! What's up?" 
    
    show emi basic_hes with charachange
    
    emi "I don't have lunch for you today, sorry if you were expecting that."

    hi "Ah, no. I was actually looking for Rin. Have you seen her?"

    "Emi shakes her head vehemently, making her pigtails whirl around."

    show emi basic_annoyed with charachange
    
    emi "Nope, the last time I saw her was in the morning. She hadn't slept so she skipped both morning classes again."

    emi "I didn't really like that, but she would have slept in class anyway if I had dragged her here."

    hi "Hadn't slept?"

    "Emi brushes my surprised remark away with a wave of her hand."

    show emi sad_annoyed with charachange
    
    emi "Yeah, sometimes she is like that, when she paints or something."

    emi "On days like this she just takes a short nap so she probably woke up already."

    show emi sad_grin with charachange

    emi "I don't know if she is at her room anymore. Probably not."

    show emi basic_grin with charachange
    
    emi "Did you have something important for her?"

    hi "No, not really. I wanted to talk with her about that art gallery deal she got, but…"

    "Emi's face cracks in a wide smile and she jumps up enthusiastically."

    show emi basic_closedhappy with charachange
    with Pause(0.5)
    show emi happybounce

    emi "Isn't it great? I'm soooo happy for her, I bet everyone will like her paintings and she'll sell a lot of them and make piles of money."

    hi "Yeah, it is great, but I wouldn't expect such a grand success right away. It's not that probable, I suppose."

    show emi sad_pout with charachange
    
    "Emi pouts at my pessimism, looking rather sour."

    show emi annoyedlegs at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.55) with charachange
    with Pause(0.5)
    show emi annoyedlegs at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.5) with dissolvecharamove
    
    stop music fadeout 4.5
    stop ambient fadeout 4.5
    "She places her hands firmly on her hips and rises on tiptoes in an attempt to match my height, or to seem more intimidating."
    
    "Either way, she fails."
    #Thats not suprising Aura, she doesn't have any "tiptoes". - Kelper
    with Pause(2.0)
    
    play music music_running
    play ambient sfx_crowd_indoors fadein 0.5
    show emi excited_sad_close with vpunch
    
    emi "Nooo, Hisao you have to be more supportive! And happy! It's important! Be happy! Do you understand me?"

    "I barely stifle my laugh."

    hi "I'll try to. See you later, I'll try to find Rin from somewhere else."

    show emi basic_annoyed with charachange
    
    emi "If you find her, tell her to drag her butt to class. The exams are soon, she will flunk them all if she doesn't study properly and then she'll be in trouble and all the teachers will scold her."

    "Even when angry, Emi somehow manages to be cute."
    
    show emi basic_closedgrin with charachange

    "Her sudden foul mood doesn't last beyond the last remark and she happily skips down the hallway towards the stairwell."

    hide emi with charaexit

    "Now then…"

    "If I was Rin, where would I hide in?"

    "Even though Emi suspected she might be up already, I should go check her room anyway."

    stop ambient fadeout 1.0
    scene bg school_dormext_full with locationskip
    
    "The smell of fresh-cut grass hits the back of my nose as I walk past the gardens."

    stop music fadeout 3.5
    
    "It is a very summery feeling, unique to the season."

    "Not many people come to the dormitories during the lunch breaks, opting to lounge in the cafeteria or main building instead."
    
    scene bg school_girlsdormhall with locationskip
    
    #play music music_normal fadein 0.5
    
    "My passage is left unseen."
     
    play sound sfx_hammer
    
    "I knock on Rin's door the same way I did last time, three short raps in quick succession."
    with Pause(2.0)
    play sound sfx_dooropen
       
    "The wait between the knocks and the door opening is unnervingly long."

    show rin relaxed_sleepy at right with charaenter
    
    play music music_night fadein 1.0
    
    "Rin is leaning against the doorjamb, as if her legs had great trouble keeping her standing up."

    "Actually, she looks like she has enough trouble with keeping her eyelids open."

    "Rin's drowsy expression reminds me strongly of the last time we were in this situation."

    "At least she is dressed this time around, not that I would have minded that much."

    "As usual, she is just staring at my general direction, waiting for the other party to say something instead of greeting me."

    hi "Umm, hi. Did I wake you up, by any chance?"

    show rin relaxed_boredom at right with charachange
    
    rin "I don't know. Something knocking on the door woke me up."

    "Her words are very groggy, coming out her mouth in one unarticulated blur."

    rin "Was it you or were you behind my door by a completely unrelated coincidence?"

    hi "I thought if you'd like to eat lunch with me or something… well I guess it'd be more like breakfast for you?"

    show rin relaxed_nonchalant at right with charachange
    
    rin "Not hungry."

    "Rin's inherent impoliteness ticks me off."

    "Actually, what ticks me off more is that I can't figure out what she wants from me, if anything."

    "This is not the time to start wallowing in that issue, though."

    hi "Emi told me you hadn't slept at all."

    rin "I forgot."

    hi "To sleep?"

    show rin basic_awayabsent at right with charachange
    
    rin "I was painting… wait."

    show rin basic_absent at right with charachange
    
    rin "What is time?"

    hi "Huh?"

    show rin basic_lucid at right with charachange
    
    "Even Rin realizes that the question didn't make any sense and closes her eyes tightly to concentrate."

    "She speaks much slower next, with a lucid tone."

    show rin basic_deadpannormal at right with charachange
    
    rin "What time is it?"

    hi "Oh. Lunch break, so a bit past noon. If you're not hungry, I guess we could just hang out or something…"

    show rin basic_deadpancontemplation at right with charachange
    
    "My news makes Rin furrow her brow and humph in contemplation, not to mention ignoring my suggestion."

    rin "I think I have forgotten something again and then I forgot what I forgot… I wish I could remember what it was so I could remember it."

    "Her eyes are shifting around as if trying to animate her thought process."

    "When they stop, it seems that Rin has come to some conclusion."

    show rin basic_absent at right with charachange
    
    rin "I have to go to paint now. I can see you later."

    hi "Oh, ok. When?"

    rin "Sometime in the future."

    hi "After classes then?"

    show rin basic_awayabsent at right with charachange
    
    rin "Mmm."

    "I take that as a yes."

    hi "Oh, that reminds me, Emi told me to tell you to drag your butt to afternoon classes."

    hi "She sounded pretty serious so you better go."

    "Rin glances at me, looking surprisingly surprised."

    show rin basic_surprised at right with charachange
    
    rin "Butt?"

    hi "Her word, not mine."

    show rin negative_annoyed at right with charachange
    
    "She doesn't look happy at all."
    
    rin "But I'm tired. Isn't it enough that she is pushing herself for exams?"

    hi "That's called friendship, I think."

    show rin basic_awayabsent at right with charachange
    
    "My lackluster quip is met with a blank stare."

    "Rin is obviously not amused."

    hi "Er, anyway, see you after classes. Is the main building lobby all right?"

    show rin basic_absent at right with charachange
    
    rin "Is something wrong with it? Well, I guess the stairs are a bit worn, did you know that the fourth step is actually loose and someone has twisted their ankle there but it's still not fixed?"

    show rin relaxed_nonchalant at right with charachange
    
    "She suddenly turns halfway around to peer into her room, looking around in search of something."

    rin "You can answer later. I need to find my brushes now."

    "Her mind is so obviously somewhere else now, so I think it's better to excuse myself."

    hi "Ok well, I'll go eat then. I'm starving."

    rin "Be careful."
    stop music fadeout 6.0
    scene bg school_dormext_full with locationskip    
    
    "I walk back outside, feeling a bit confused."

    "I got brushed off pretty swiftly."

    "Well, I suppose she has a lot on her mind now."

    scene bg school_scienceroom with shorttimeskip
    play music music_tranquil fadein 1.0
    
    "After an uninspiring and lonely lunch I drag my own butt to afternoon class, even though I don't particularly feel like it."

    "I have to force myself to pay attention, but only because the teacher is saying that today's topic will be on exam."

    "It's not that I'm too worried about the exams, but I sort of feel obligated to do well after being so long away from school."

    "It'd feel a bit ungrateful to bomb the first exams here."

    play sound sfx_normalbell
    with Pause(2.0)
           
    "The classes are over, so I trudge back downstairs."

    scene bg school_lobby with locationskip
         
    "I sit on the hard bench in the lobby to wait for Rin coming from her own class, if she ever managed to go there."    
    window hide dissolve
    return

label en_R23:

    #This is a faggy scene, because the visualization is almost nothing but a single (chained) CG, but what can I do.
    scene black with fade 
    with Pause(0.5)
    
    scene bg school_lobby_ss with shorttimeskip   
    $ renpy.music.play(music_tranquil, fadein=0.5, if_changed=True)
    window show dissolve
    
    "The afternoon is late already, and so is Rin."

    "Knowing her, she could have forgot that we promised to meet at the lobby after school and go downtown or somewhere else."

    "I haven't really waited for that long, but I'm tired of it already."

    "The school building becomes eerily desolate after the classes are over, since apart from the library there is not much to do and most prefer to hang outside or at the dorms anyway."

    "I'll go find her."
    
    stop music fadeout 10.0
    scene bg school_girlsdormhall with locationskip
    with Pause(0.6)
    scene bg school_gate_ss with locationskip
    with Pause(0.6)
    scene bg school_dormext_full_ss with locationskip
    with Pause(0.6)
    scene bg school_greathall_ss with locationskip
    with Pause(0.6)
    scene bg school_backexit_ss with locationskip
    with Pause(0.6)
    scene bg school_hallway3_ss with locationskip

    #blargh, some locationskip slideshow here, or ask me to write more

    "I push the door to the 3-4 classroom open carefully and peek in."

    play sound sfx_dooropen
    scene bg school_room34_ss with locationchange

    "The classroom would be dark, if not for the yellow light that is falling across the floor."

    "The dust and chalk floating slowly in the air makes the light almost palpable."

    "The entire room bathes in gentle sunlight shining through the windows, washing the shadows away."

    "Only one person is inside the classroom."

    scene ev rin_nap_total at Zoom((800, 600), (0, 0, 800, 600), (20, 0, 760, 570), 20.0) with whiteout
    play music music_serene fadein 4.0
    
    "Rin sits on what I assume is her seat, the window seat on the third row, resting her head against the desk."

    "So she made it to the class."

    "I wonder if she slept through it all, apparently not even Emi had the heart, or capability, to wake her up."

    "I close the door quietly and walk past the desks neatly arranged in even rows to her."

    hi "Rin?"

    "My mouth is suddenly so dry that the word comes out as a puny whisper."

    scene ev rin_nap_close_nohand with locationchange

    "She doesn't answer so I set my bag down on the floor next to hers and lean over her to look at her face."

    "Rin's eyes are peacefully closed, the long eyelashes throwing thin shadows on her cheeks. Her mouth is slightly open and she is breathing quietly."

    "The hair that's usually so messy is today even more so, laying in a complete disorder over half of her face and forehead."

    "Her bag is lying at her feet like a forgotten rag doll, some books and pens fallen out of it all around her seat."

    image ev rinhand = anim.TransitionAnimation("event/rin_nap_close_nohand.jpg", 0.0, Dissolve(1.0),
                                                 "event/rin_nap_close_hand.jpg")
    scene ev rinhand at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.623) with dissolvecharamove   

    "The scene makes me smile for reasons I don't know myself."

    "I touch Rin's head lightly, sweeping a few stray hairs off her ear. Her hair feels warm against my palm."

    scene ev rin_nap_close_nohand at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.623) with locationchange
    
    "Rin stirs, and I retract my hand on reflex, feeling embarrassed for touching her so casually."

    scene ev rin_nap_close_nohand with Dissolvemove(2.0)

    "She looks so vulnerable, like any sleeping person. It's impossible not to feel fondness towards her."

    scene ev rin_nap_total with locationchange

    "I sit on the desktop of whoever is sitting in front of Rin and draw the window slightly open to get some fresh air and, hopefully, wake Rin up without having to resort to cruder methods."

    image ev rinawind = anim.TransitionAnimation("event/rin_nap_total_wind.jpg", 0.2, Dissolve(0.4),
                                                 "event/rin_nap_total.jpg", 0.2, Dissolve(0.4))
    scene ev rinawind with locationchange

    "She doesn't wake up, but I really didn't expect her to."

    "Looking at her makes me sleepy as well. To be honest, I wouldn't mind a quick nap either, but I content myself with leaning against the large window and watching Rin."

    "The light is slowly melting into her auburn hair, softening Rin's outlines so that she seems to be fading into her surroundings."

    "The minute twitches of her muscles, her hair swaying in the air current, the even rhythm of her breathing, it all gives a strong impression of a dreaming girl."

    "Like all sleeping people, Rin looks like she is away from this world."

    "It reminds me of something else she does, but I am left wondering what it is."

    "Rin sleeps, wherever her dream country is."

    "With Rin, it doesn't feel so obvious that she would ever come back. She seems to be so detached from her surroundings even when she is awake…"

    stop music fadeout 20.0

    "The realization hits my consciousness without a warning."

    image ev rinawindclose = anim.TransitionAnimation("event/rin_nap_close_wind.jpg", 0.2, Dissolve(0.4),
                                                      "event/rin_nap_close.jpg", 0.2, Dissolve(0.4))
    scene ev rinawindclose at Zoom((800, 600), (0, 0, 800, 600), (20, 0, 760, 570), 20.0) with locationchange

    "Rin sometimes looks like that when she is painting."

    "Her focused expressions give the same feeling of being on the other side of some imaginary gap than looking at her sleeping face."

    "I feel a pain in my chest."

    "There is no way I can close that gap, to be on the same level with her."

    "It hurts, even though I know that it's impossible for any two people two truly understand each other."

    "But Rin… she is almost literally in another world when she is talking about art, thinking about art or making art."

    "It's a world I, or anyone, can't share with her."

    "I wonder if it's the same thing as sleeping for her. Rin seems to value sleeping a lot, despite her apparent lack of common sense regarding sleep rhythm."

    "What to do?"

    "Rin doesn't show any signs of waking up, so I am faced with the decision to wake her up or wait for her to wake on her own."

    "I choose the latter."

    scene ev rinawind with locationchange

    "Waiting is something I am good at, I found out during my hospitalisation."

    "Even the hospital ward was a more lively place than the school after classes, though."

    "The only sounds in this place are the loud ticking of the clock above the door and the distant voices of students down on the grounds."

    "A real summer's breeze blows inside from the gap I opened, warm and carrying the scent of light."
  
    scene bg misc_sky_ss at Fullpan(20.0) with locationchange

    "I look outside to see where it came from, but I am blinded almost instantly."

    "The windowglass seems to trap all the sunlight within, making it painful to look that way."

    "All I can glimpse through the window are the dark silhouettes of the trees and the perimeter wall against the setting sun's radiance."

    scene ev rinawind with locationchange

    "As I turn back to watch Rin, she stirs again."

    play music music_innocence
    image ev rinawindtears = LiveComposite((800, 600), (0, 0), anim.TransitionAnimation("event/rin_nap_total_wind.jpg", 0.2, Dissolve(0.4),
                                                 "event/rin_nap_total.jpg", 0.2, Dissolve(0.4)), (0, 0), 'event/rin_nap_total_tears.png')
    scene ev rinawindtears with locationchange

    "A single tear worms down from the corner of her eye, slowly making its way across her face before it falls on the desk."

    image ev rinawindtearsclose = LiveComposite((800, 600), (0, 0),  anim.TransitionAnimation("event/rin_nap_close_wind.jpg", 0.2, Dissolve(0.4),
                                                      "event/rin_nap_close.jpg", 0.2, Dissolve(0.4)), (0, 0), 'event/rin_nap_close_tears.png')
    scene ev rinawindtearsclose with locationchange

    "It is tiny, barely a droplet, but it captivates me."

    "Another tear follows the first, and then a third."

    "A feeling of anxiety overcomes me, petrifying me on the spot."

    "It's so strange, seeing Rin's face peaceful as she sleeps, at the same time as tears stream down her cheeks, wetting the wooden desktop her rests her head on."

    "I don't know what to do so I do nothing, just watch the tears roll one by one down her face."

    "I wonder what she is dreaming of."

    scene bg school_room34_ss with locationchange

    "With one final stir Rin wakes up, or maybe it is because of the crying."

    show rin invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.8)
    show rin relaxed_sleepy_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with dissolvecharamove
    with Pause(1.0)

    "She sits upright and yawns so excessively it looks like her jaw might dislocate."

    rin "Ah."

    show rin relaxed_nonchalant_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with charachange

    "She notices my presence, but her reaction is more like lack of one, just an acknowledgement instead of a startled gasp or something"

    show rin relaxed_boredom_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with charachange

    rin "Hello."

    hi "Good morning."

    "She is so groggy she can't even return my smile."

    hi "You…. umm… your cheeks are wet."

    show rin basic_absent_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with charachange
    
    rin "Ah."

    "Rin notices the tears and wipes them on the shoulders of her shirt."

    hi "You cried in your sleep. Was it a bad dream?"

    show rin basic_awayabsent_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with charachange 

    "I recall Rin claiming that she has never had one, but I had to ask anyway."

    rin "No. This just happens sometimes."

    show rin basic_absent_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with charachange

    rin "Did you want something?"

    "She brushes the topic aside."

    hi "Eh… you promised to see me after classes."

    show rin basic_deadpancontemplation_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with charachange

    rin "Oh. Well, it's after classes now and I am seeing you right here."

    "She looks guilty even though she is saying that."

    show rin basic_sad_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with charachange

    rin "I should have come, shouldn't I? I was tired and my feet just wouldn't move so I couldn't come."

    hi "It's ok, you were tired because you didn't sleep at night, right?"

    show rin negative_confused_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with charachange
    
    rin "I was painting all night and then it was morning and I sort of forgot that it would have been a good idea to sleep."

    "She frowns, just a little, to show that she is not satisfied."

    show rin basic_awayabsent_close_ss at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.66) with charachange
    
    rin "I'm going to the 22nd Corner to see the atelier and do something."

    hi "Painting?"

    show rin basic_awayabsent_close_ss with dissolvecharamove
    
    "Rin nods and stands up from her seat."

    show rin negative_spaciness_close_ss with charachange
    
    rin "Do you want to come?"

    "I contemplate for a moment. Rin's invitation is surprising, but it might be just because she stood me up twice today."

    hi "Nah, I'm fine. I would only be in your way and you have to work hard for the exhibition, right? Some other time."

    "I can't read Rin reaction from her face. Whether she is relieved, disappointed or something else, she won't show it."

    show rin basic_absent_close_ss with charachange
    
    rin "Okay. I think I better go now."

    "I step down on floor as well and stretch my back."

    hi "Right, I'll go do some homework then. Please convey my apologies to whoever sits here."
       
    rin "I don't know who that person is."

    hi "You don't?"

    show rin relaxed_doubt_close_ss with charachange
    
    stop music fadeout 8.0
    
    rin "Why would I?"

    hi "But… she sits in front of you."

    "All I get is that nonchalant shrug."

    show rin relaxed_nonchalant_close_ss with charachange
    
    rin "She is not interesting."

    #transition to dorm room

    window hide dissolve
    scene black with fade
    with Pause(0.5)
    
    scene bg school_dormhisao_ss with locationskip
    
    window show dissolve
    "I sit on my desk, feeling pretty stupid."

    "It's not that I have much homework, and I don't feel like starting to study for exams already."

    "Why did I decline her invitation?"

    window hide dissolve 
    scene black with Dissolve(1.5)  
    
    return
    
label en_R24:
        
    scene black 
    with Pause(1.0)
    play music music_daily fadein 0.5
    scene bg school_scienceroom with locationskip
    window show dissolve
    
    "My second-guessing keeps me occupied throughout the following day, diverting my attention from all-important schoolwork to pointless lamenting."
    
    "Maybe I'll get to talk with Rin in the art club. It's not like either usually spends that much time on actual club assignments."

    scene bg school_scienceroom with shorttimeskip
    play sound sfx_dooropen
    with Pause(1.0)
    play sound sfx_doorslam
    scene bg school_scienceroom with vpunch
    with Pause(0.5)
    play ambient sfx_emisprinting
        
    "After the class ends, Emi crashes into our classroom, almost bumping straight into Misha who was about to leave for the student council's office."
    
    "Only Misha's lightning reflexes save her from the patented Emi-tackle, which I'm sure over half of the students in the school have experienced at least once."
    show emi invis at right
    stop ambient
    show emi excited_joy with dissolvecharamovefast
   
    emi "Oh, lucky! I was worried that you had left already so I came as fast as I could because our teacher always keeps us overtime so I'm glad you are still here."

    hi "So I see. So what's up?"

    show emi sad_annoyed with charachange
    
    "Emi's trademark smile shifts to an uncharacteristically concerned expression."

    emi "I was wondering where Rin is. I haven't seen her today, she wasn't even in her room in the morning."

    emi "Did you find her yesterday?"

    hi "Yeah, I did."

    show emi basic_annoyed with charachange
    
    emi "Well, do you know where she is?"

    hi "Er, should I?"

    hi "She said she'd go downtown to that art gallery yesterday."

    emi "Do you think she is still there?"

    hi "You think she slept there? Can't be."

    show emi sad_annoyed with charachange
    
    emi "But where is she then?"

    hi "No idea, but today is an art club meeting, she might come there even if she skipped school."

    show emi sad_pout with charachange
    
    emi "I hope so. Rin is such an airhead sometimes, I can't believe it if she really has been in downtown for over a day."

    #skip to art club room

    scene bg school_classroomart with shorttimeskip
    
    "Unlike I predicted, Rin doesn't appear in the club room, so the club meeting is unbearably dull."

    "At least I have time to focus on today's subject instead of getting distracted by Rin or being distracted to her by myself."

    "I try my best, but there is no way around it: I suck as an artist."
    
    "The teacher doesn't look too happy when he glances at my work, but he keeps his disdain from showing in his words."
    
    hi "Teacher, do you know where Rin is?"

    "Even though he has already turned to give critique to another student, Nomiya turns to regard me."

    show nomiya dreamy with charachange
    
    "The frown from just seconds ago has magically turned into a wide grin."

    no "Oh, she is probably at Sae's place. I haven't seen her today but that might just as well be because I am so busy, rather than anything else."

    no "You know, I have to promote my star student a little and all."
    #start? -SC

    show nomiya smile with charachange
    
    no "Anyway, Tezuka wanted to go work in that atelier so I gave her some supplies and excused her from class for today."

    hi "But, we have exams coming up soon. Won't she…"

    show nomiya stern with charachange
    
    "An unhappy look returns to the teacher's face."

    no "I don't what your relationship is and it doesn't matter."

    "I don't know what our relationship is, either."

    show nomiya serious with charachange
    
    no "Either way you must consider Tezuka here, above all."

    no "What matters is Tezuka's debut exhibition. It's her chance to make a breakthrough, Sae is very well known in the art circles so she might attract a lot of attention."

    show nomiya stern with charachange
    
    no "Don't bother her if she is working, understand?"

    no "It is very important for us that her exhibition is a success."

    "Nomiya's overprotectiveness is a bit creepy, but I suppose it's natural."

    "It is true that this must be a very important thing for Rin."

    stop music fadeout 3.5
    
    "Still, something in the teacher's way of telling me off annoys me."

    hi "All right."

    #skip to bus stop or bus background

    scene bg city_busride with locationskip
    play ambient sfx_businterior
    
    "The bus trip to town, as short as it is, still gives me time to think about what the hell am I doing."

    "Why am I bothering myself, coming all the way here even though Rin would probably be better off without extra distraction?"

    "Even going against Nomiya's advice?"

    "Well, I am regretting turning her offer down yesterday, so that's one reason."

    "I talked her into this."

    "I have to support her."

    "She is my friend."

    "Besides, sometimes a bit of distraction is just the thing one needs to cope with this kind of thing."

    "I chuckle to myself, remembering Rin's mural from the festival and her loony attempts to distract herself without getting too distracted."
    stop ambient fadeout 0.5
    #scene downtown
    scene bg gallery_ext at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.60) with locationskip
    play ambient sfx_traffic fadein 0.2
    "I remember the direction to take from the bus station towards the gallery without too much effort, and soon I find myself staring at the big letters saying “22nd Corner.”"

    "As I have no idea where the atelier room is, I enter the gallery hoping I get answers from the staff."
    stop music fadeout 0.2
    stop ambient fadeout 0.2
    play sound sfx_storebell 
    scene bg gallery_int with locationchange
    play music music_soothing fadein 0.5

    "Inside, the gallerist is intently studying a large painting hanging on the wall, a poon…"

    "She turns around to reckon me, and a smile of recognition spreads on her lips."

    show sae smile with charaenter

    sa "Oh, isn't it the young man from the other day, Shinichi's student… Hisao, was it?"

    sa "You know, I am so glad that even young people show interest to art nowadays…"

    hi "Ah… I was actually looking for my friend. The teacher said that she would be here."

    show sae doubt with charachange
    
    sa "That is possible, I wasn't aware that she is there today though… "

    show sae neutral with charachange
    
    sa "She came by yesterday and I showed her the atelier, but I haven't seen her come today."

    sa "But it's possible that I have just missed her coming."

    show sae smile with charachange
    
    sa "You see, the gallery door is the next one down the street so she could've gone there without dropping by here."
    
    sa "To get there, you need to turn right from here and walk to the next door, then just climb the stairs to the top floor. There is only one door there, you can't miss it."

    "She is gesturing with her hands as she gives the directions, giving me a vivid impression of my deaf classmates' discussions."

    stop music fadeout 6.0
    $ renpy.music.set_volume(0.5, 0.0, channel='ambient') 
    play ambient sfx_rooftop fadein 0.5

    scene bg gallery_ext 
    with locationchange
       
    "I give Sae my thanks, exit the gallery and find the door she was talking about."

    scene bg gallery_staircase with locationchange
    
    "It leads to a dark and damp stairwell, which reminds me of the stairs leading to the roof of the school building."

    "The stairs are steep, so I find myself huffing and puffing long before reaching the fourth floor."

    "An unassuming wooden door waits me there."

    "It is unlocked, so I knock and enter."

    play sound sfx_whiteout
    
    $ renpy.music.set_volume(0.29999999999999999, 2.0, channel='ambient')

    scene bg gallery_atelier at Fullpan(8.0, dir="left") with whiteout

    #description fitting with the actual bg once someone finds it goes here

    "The atelier is really just one big room with the ceiling being lower at one end than the other because the roof of the building is gabled."

    "There is a huge skylight in the ceiling, acting as the sole source of light for the room, the sunlight reflecting off the white-painted walls."

    "I suppose it's good for art or something, to use natural light."

    "There is not much in the way of interior decoration, on the contrary it seems that the room has been used as a storage of some sort for a while."

    "All kinds of boxes and old furniture are scattered beside the walls."

    "The room is a bit dusty, reminding me of the unused classroom in the seniors' hallway."
    #Yeah another act1 flag -SC
     
    show rin back_cas with charaenter
    
    "Rin is standing in the middle of the room with her back to me."

    "She is staring at a half-painted canvas placed on an easel."

    "Not working on it, actually I don't even see paints or brushes anywhere. Just staring."

    hi "Hi."

    rin "Hello."

    "Rin doesn't judge my surprising appearance worthy of turning around, maybe saying more than a mechanical reply to my hello, smiling, anything."

    "She keeps on doing… whatever she is doing, probably some weird creative thing inside her head."

    "Despite halfway expecting this, I feel hurt, but I can't turn my eyes away from Rin."

    "Left uncertain of what to do, I keep on staring at her while my mind races."

    play sound sfx_whiteout
    scene bg gallery_atelier_close at Updownpan(20.0)
    show rin back_superclose at Updownpan(20.0)
    with whiteout
    
    "I don't think I have ever studied anyone's back so intently before."

    "Rin's neck, hidden by her copper-colored hair which is again in complete disarray."

    "The relaxed but rigid posture, reminding me that Rin's physical appearance tends to be as awkward as her trains of thought often are."

    "Her gaunt, delicate shoulder blades, visible through the thin white fabric of her shirt."

    "The contours of her hips, curving down to her thin thighs."

    "It pisses me off."

    $ renpy.music.set_volume(0.10000000000000001, 2.0, channel='ambient')
    play music music_night fadein 1.0

    window hide dissolve
    nvl clear
    nvl show dissolve

    n "\n\n\n\n\nShe rarely seems to be looking at me, both literally and figuratively."

    n "I, on the other hand, am always watching her back, both literally and figuratively."

    n "Whenever she is painting, whenever something catches her fluttery attention, whenever I don't forcefully make her listen to me."

    n "I can't reach through to her."

    n "Rin's heart is uncharted territory, white area of the map, dangerous waters."

    n "The edge of the world?"

    n "If you go too far in you will fall off?"

    image bg fading = anim.TransitionAnimation("vfx/Rinback.jpg", 0.0, Dissolve(16.0),
                                                 "vfx/black.jpg")
    
    scene bg fading with None
    
    nvl clear

    n "\n\n\n\n\nWhat do I think of Rin?"

    n "Some times she is aloof and distant, and it annoys me, other times her passion for things she thinks are worthwhile shines through and it inspires me."

    n "I can't understand her."

    extend "Or myself."

    n "Still, I like her and consider her my friend."

    n "I suppose part of friendship is putting up with the oddities of the people you call friends."

    n "I do admit, there is a lot of putting up with Rin."

    nvl clear

    n "\n\n\n\n\nWhat does she think of me?"

    n "I have no idea. Last week, I thought she might have liked me romantically, with the kisses and all."

    n "It forced me to ponder my own feelings too."

    n "This week, I am utterly confused."

    n "What would she do if I told her I liked her that way?"

    n "Even if I don't? Or do I? Damn, I can't make sense of even my own thoughts anymore."

    n "It must be contagious."

    nvl clear

    n "\n\n\n\n\nEven if I said a thing like that, would it matter?"

    n "Nothing affects Rin."

    n "Nothing."

    nvl clear
    nvl hide dissolve
    
    scene bg gallery_atelier
    show rin back_cas 
    with locationskip

    window show dissolve
    
    "…"

    stop music fadeout 4.0
    
    hi "I'll be going now."

    rin "Ok."

    scene bg gallery_staircase with locationchange
    
    "The wooden door closes behind me, separating me and Rin to our own worlds."
    
    stop ambient fadeout 0.5
    window hide dissolve
    scene black with Dissolve(1.5)
    
    $ renpy.music.set_volume(1, 0.0, channel='ambient')

    return
    
label en_R25:
    
    #this bit maybe needs a larger block for scene transition, I'll expand it later… maybe more Emi worrying about Rin or Mutou or Misha?

    scene black with fade
    with Pause (0.6)
    
    play sound sfx_doorknock        
    centered "BANG {w=0.1}{nw}" with vpunch
    extend "BANG {w=0.1}{nw}" with vpunch 
    extend "BANG {w=0.1}{nw}" with vpunch 
    extend "BANG {w=0.1}{nw}" with vpunch 
    extend "BANG {w=0.1}{nw}" with vpunch 
    extend "BANG {w=0.1}{nw}" with vpunch 
    extend "BANG" with vpunch
    with Pause (0.5)
    
    scene bg school_dormhisao with openeye
    play music music_normal
    window show dissolve
            
    "This is novel. It's been a while since I've been woken up with some unnecessarily early cacophony."
    
    "And just when I started to get back to normal sleeping rhythm."
    
    "I tread across the freezing cold floor to open the door for whoever insists on seeing me this early."

    play sound sfx_dooropen
    with Pause(1.1)
    play sound sfx_doorslam
    
    show emi invis at right with None
    
    show emi excited_sad with dissolvecharamovefast
    
    emi "Rin is not in her room!"

    hi "Good morning."

    play sound sfx_impact 
    show emi excited_sad_close with vpunch
    
    emi "Did you find her yesterday? Has she run away? What if she has gone somewhere and is now lost?"

    show emi excited_hesitant_close with charachange
    
    "I raise my hand to silence Emi and give myself a bit of time to recall yesterday's events."

    "I try to organize the thoughts in my dizzy head so I can be as concise as possible for the obviously overanxious Emi."

    hi "She didn't come to the art club so I asked the teacher, who said that Rin had gone to the gallery."

    show emi sad_pout with charachange
    
    emi "And?"

    hi "Well, I went there and there she was."

    emi "And?"

    hi "Uhh, I forgot to ask, but I think she had been there all the time."

    show emi sad_shy with charachange
    
    emi "Was she painting?"

    hi "Yeah."

    show emi sad_annoyed with charachange

    emi "Was she all right?"

    hi "I didn't ask. She looked fine, maybe a bit sleep-deprived."

    show emi sad_depressed with charachange
    
    "Emi doesn't look happy at my report."

    emi "I have practice today. Could you go and make sure that she is all right?"

    "I hesitate for a moment."

    stop music fadeout 4.0
    
    "After yesterday, I wasn't intending to see Rin for a while."

    hi "Sure."

    #check if that needs a clear, hopefully not

    window hide dissolve
    
    scene black with fade
    nvl clear
    nvl show dissolve
        
    
    $ renpy.music.set_volume(0.2, 0.0, channel='ambient')
    play ambient sfx_businterior fadein 1.0
    n "\n\nThis indecisive, impatient feeling in the back of my head is driving me crazy."

    n "I gave up yesterday, just like I did the day before."

    n "Didn't I decide to try to make most of my life, to savour each day to its fullest?"

    n "In the end, did I manage to change?"

    n "I've never been a reckless person, which is maybe why I've missed some things that people consider “normal” for kids of my age."

    n "I rarely did anything out of a whim, not even mundane stuff like buying candy, or going to a party."

    n "Maybe I need less deliberation."

    n "I just can't seem to be able to cast my dice."

    n "Not even now."

    n "It makes me angry at myself."

    #22nd corner bg

    nvl clear
    nvl hide dissolve
    
    
    stop ambient fadeout 0.5
    with Pause(0.45)
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    scene bg gallery_ext_ss with locationchange
    play ambient sfx_rooftop fadein 0.5

    window show dissolve
    "And so, I find myself in front of 22nd Corner again, this time walking straight past it to the side door leading to the atelier."

    
    scene bg gallery_staircase with locationchange
    $ renpy.music.set_volume(0.4, 0.3, channel='ambient')
    
    "The stairwell smells of mold and wet concrete."

    play sound sfx_dooropen
    "The door is still unlocked, which makes me question the gallerist's sensibility in giving the key to here to Rin."
    
    scene bg gallery_atelier_ss at left
    show rin back_cas_ss 
    with Dissolve(0.8)
    $ renpy.music.set_volume(1, 0.3, channel='ambient')

    play music music_night fadein 0.8
    "As expected, Rin is here again, as if she hasn't moved at all since my short visit yesterday."

    "Who knows, maybe she really hasn't, although I see that the same painting that was on the easel yesterday has progressed a little."

    hi "Hey."

    "Deaf and blind to all except the painting."

    "It can't be helped. This is just the way Rin is."

    "In theory, diverting her attention is not hard. I just need to offer her something equally interesting to what she is currently doing."

    "And I know another trick too."

    "I grasp Rin's shoulder from the spot where the collarbone joins the shoulder and squeeze it gently so that it won't hurt."

    "For whatever reason physical contact tends to bring her back down to earth."

    show rin basic_absent_cas_ss with dissolvecharamove
    
    "With the tiniest flinch, Rin wakes up from her reverie and turns to look at me."

    hi "Hey."

    show rin basic_awayabsent_cas_ss with charachange
    
    "Her eyes try to wander back to her painting but at least she pays some attention to me now."

    rin "Hello."

    "Something in her quizzical expression shows that she is not quite level with the situation."
    
    rin "Didn't you just leave?"

    hi "That was yesterday."

    "My revelation doesn't shock Rin nearly as much as her ignorance of the passing of time worries me."

    show rin basic_absent_cas_ss with charachange
    
    rin "Oh."
    rin "Welcome back."

    hi "Have you been here for two days straight?"

    show rin basic_deadpancontemplation_cas_ss with charachange
    
    rin "I have slept too."

    hi "I mean, physically."

    show rin relaxed_nonchalant_cas_ss with charachange

    "She is averting her gaze, as if she in fact is not completely insensitive to my mood, which admittedly is right now rather sour."

    rin "…yes."

    hi "I know that this is important, but you can't just lay aside everything else and lock yourself up here."

    show rin relaxed_boredom_cas_ss with charachange

    rin "The door isn't locked."

    hi "Have you eaten? Emi is sick with worry for you."

    show rin basic_deadpandelight_cas_ss with charachange
    
    rin "Isn't this place neat? She gave it to me… it's like being a real artist."

    "What is the difference between Rin and a “real” artist?"

    hi "Damn, do you have no consideration for your own wellbeing? How far are you going for the sake of art?"

    show rin basic_awayabsent_cas_ss with charachange
    
    "Rin doesn't give further answers, forcing me to collect my own thoughts too."

    "Isn't this exactly what the teacher said I shouldn't do?"

    "It's too late to regret now."

    "I let Rin go and sit down on the worn-out couch she apparently has been using as a makeshift bed."

    show rin back_cas_ss with dissolvecharamove
    
    "She takes advantage of the situation and returns to her work."

    "Today, there are paints and brushes on the floor and Rin proceeds to pick one up, dipping it into blue paint with some tone name that is too fancy for me to remember."

    "With a steady leg, she brings the brush to contact with the canvas and draws a firm stroke on it."

    "It is followed by a pause of consideration and a change of brush to a smaller one."

    "She continues her work like nothing just happened, already forgotten that I am here."

    "I observe Rin as she slowly slides away from the room again, like I've seen her do before."

    hi "What is it that you paint?"

    "I try to open conversation again, in the hopes of getting at least something out of Rin."

    show rin basic_absent_cas_ss with dissolvecharamove

    rin "I don't think I understand your question."

    show rin negative_spaciness_cas_ss with charachange
    
    rin "You don't know what a painting is?"

    show rin negative_annoyed_cas_ss with charachange
    
    rin "This confuses me, because I seem to recall you being at the art club meeting at least once and— {w=0.3}{nw}" #reminder for the potential {nw} break
    
    hi "No, I meant on a more philosophical level, or something."

    show rin basic_absent_cas_ss with charachange
    
    hi "I mean, it's not possible to get what your paintings are portraying at first glance."

    hi "So, I've been wondering what they are."

    hi "Emi talked about you getting a “right feeling,” the teacher just rambled about your imagination, the gallerist said something about the technical aspects of your style but you yourself won't explain anything even if 
        I ask."

    show rin relaxed_doubt_cas_ss with charachange
    
    rin "Have you asked?"

    "There is a hit of challenge and irritation in her voice, a refreshing change to her lately so nonchalant and emotionless demeanor."

    hi "I just did."

    show rin basic_lucid_cas_ss with charachange

    with Pause(1.5)

    rin "Qualia."

    hi "What?"

    show rin basic_absent_cas_ss with charachange

    rin "Qualia is the word for things that you see and hear and smell and think but can't explain."

    rin "With words, or other things."

    hi "I don't get it. What kinds of things I can't explain?"

    show rin basic_deadpanupset_cas_ss with charachange

    rin "You should talk about colors with some blind person."

    "Her simple example is surprisingly enlightening."

    hi "So, you try to paint the things that can't be put into words, is that it?"

    hi "But, if these things can't be explained by anything, then they can't be communicated by art either."

    show rin basic_awayabsent_cas_ss with charachange

    "Rin blows a stray strand of auburn hair off her forehead and looks up to the sky visible through the opening in the ceiling."

    rin "That's the way it is."

    hi "So what kind of things these qualia are, except colors?"

    rin "All kinds of things."

    show rin basic_absent_cas_ss with charachange

    rin "It's like, everyone in the world has their own idea of a thing, and when you or I say the word for it you never can be sure if the other person is thinking of the same thing."

    rin "Like, try to explain red, or love."

    hi "Well, I don't know… love is a feeling of affection, attraction, caring. Stuff like that."

    show rin basic_deadpancontemplation_cas_ss with charachange

    "Rin looks doubtful, unimpressed at my meek attempt at explaining a deep concept with a few simple words."

    rin "Is that love?"

    hi "Yeah ok, I understand. The associations and thoughts in my head are different from what I am saying"

    hi "But you know, by that definition, isn't almost everything in the world like that… qualia?"

    hi "All words are used to communicate ideas, some ideas just are more universal than others."

    hi "I don't think I could too accurately explain any given experience I've had to another person."

    hi "Each person is an individual, you can't get inside someone else's head."

    hi "It's like that symbols game of yours, everyone associates different things to words."

    show rin basic_deadpandelight_cas_ss with charachange

    rin "You guessed right once."

    hi "I got lucky."

    show rin basic_absent_cas_ss with charachange

    stop music fadeout 18.0

    "My retort silences Rin. She retreats from the conversation, slipping again away from me."

    "She doesn't return to painting, just keeps on looking me with that empty poker face of hers."
    
    "Why did she choose that word?"

    "It is not a game she's playing with my head. Rin is not a disingenuous person, of that I am sure."

    "Maybe it's just my own mind playing tricks."

    "Love, affection, that kind of thing in the context of Rin have made me feel pretty confused lately."

    "When did I start having thoughts like this? I can't remember."

    "Maybe last week was the key."

    "She is a puzzle, a conundrum, an enigma."

    "I feel attracted to it, compelled to solve it, the overtly rational part of my brain won't let me give up."

    "I never would have believed I could be this obsessive about something."

    "Damn, this side of me reminds me of Rin herself, too."

    "Then, why do I hesitate and keep running in circles around her?"

    "Carpe diem, right?"

    $ renpy.music.set_volume(0.0, 2.0, channel='ambient')
    
    hi "Rin."

    "Saying her name with an intention like this makes my mouth dry, as if my subconscious is fighting against what I'm going to say next."

    "Rin looks up from her paint-covered toes and stops wriggling them as there now isn't anyone to observe them curiously."

    "The hard stare of her dark green eyes seems like a portent."

    hi "I like you."

    "The lack of any reaction is like a slap to the face."

    hi "So… ummm… I mean, I'd like to like you as more as friends."

    show rin basic_surprised_cas_ss with charachange

    rin "What is “more”?"
    
    $ renpy.music.set_volume(0.5, 7.0, channel='ambient')

    "The slow, hesitant words coming from between her strawberry-colored lips are not the ones I was waiting for. Neither of the two options, actually."

    "I feel myself blushing heavily, as is the par for course in these kinds of situations."

    "Still, Rin's faux-innocent inquiry feels like grilling over hot charcoals."

    hi "You know… like, romantically and…"

    show rin basic_lucid_cas_ss with charachange

    rin "No."

    rin "We are friends."

    show rin back_cas_ss with dissolvecharamove

    "Rin turns turn around, giving me a cold shoulder and returning back to look at her painting."

    "She makes a move to pick up her brush which lies forgotten on the floor, but decides against it in the last moment."

    rin "I can't talk about that kind of thing."

    rin "So… don't talk about that kind of thing."

    "Rin finally picks up the brush without giving any explanation to her behaviour."

    "Maybe there was something in her voice that gave away some emotion, but I couldn't say what."

    "Rin's shoulders are slumping melancholically as her foot works the canvas in front of her."

    "She won't let me see her face and I know it."

    "Feeling the weight of my heart grow heavier, I stand up to leave, for I can't stay here longer tonight."

    "It's like I have opened Pandora's Box, stepped over some line that Rin didn't want me to cross, and she had to turn me down."

    "I walk across the squeaky floor to the door leading to the stairwell."

    "Rin's quiet voice stops me on my tracks as I'm about to open the door."

    "My hand, still on the brass doorknob is waiting for me to turn it, or to withdraw."

    stop ambient fadeout 2.0
    
    rin "Hisao."

    hi "Yeah?"

    rin "Will you come tomorrow?"

    hi "…"

    hi "Yeah."

    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')

    window hide dissolve
    
    scene black with Dissolve(1.5)
    
    return
 
label en_R26:
    
    scene black 
    with Pause(1.0)
    
    scene bg gallery_staircase with locationskip
    
    $ renpy.music.set_volume(0.3, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 1.0
    
    window show dissolve
    "The day is already folding into dusk when I climb the dark stairs leading up to Sae's atelier that is now Rin's."

    "I am later than usual, but it couldn't be helped. Today was a long day with schoolwork and all."

    "Usual?"

    "It occurs to me that not that many days have passed since our first visit here."

    "People, even me, seem to get trapped into behavior patterns pretty easily."

    "What is perceived as normal is deeply subjective, the sum average of one's opinions and experiences, slowly fluctuating as time flies past."

    "Over my time in Yamaku, I've come to consider hanging out with Rin “normal” just like I've come to consider the school itself “normal.”"

    "Even today, I'm not here for any particular reason, save for Rin's parting words from the day before."

    "It's just something I do, even though today I feel like I'm here against my own will."

    "But here I am, opening the door to the current inner sanctum of Rin's creative process, part expecting and part dreading to see the thin, ungainly form of the girl who I've been thinking of constantly since yesterday."

    play sound sfx_dooropen
    with Pause(0.8)
    scene bg gallery_atelier_ss at left with locationchange
    $ renpy.music.set_volume(1.0, 1.5, channel='ambient')
    
    "Rin is pacing like a caged animal around the room, looking through the skylight at the burgundy-colored dusk."

    "The last light of sun's advance across the sky reflects from the clouds floating over the town, filling every corner of the atelier with blazing orange light."

    hi "Rin."

    "I remember how my voice sounded yesterday when I called her name, nervous and hesitant."

    show rin invis at twocenteroff3 with None
    
    "Today, it's even harder to get the simple word out of my throat, but that feeling is gone."

    show rin basic_absent_cas_ss with dissolvecharamove
    
    "Rin hears me on the first time—was she waiting for me?—and turns around to greet me with that obsidian gaze of hers."
    
    "Although I am sure my face can't hide my feelings, Rin's expression is as expectant and neutral as always."

    "The clouded, slightly absentminded darkness in her eyes is like a wall standing between me and her."

    "…"

    "It is the first awkward silence between us that is truly awkward."

    "Yesterday, both of us said something we can't take back and there is no way it can be undone."

    "I can't even begin to guess what Rin is thinking, but I am feeling the pressure of her lightless eyes on me, compelling me to break the silence."
    
    hi "How's painting going?"
 
    show rin basic_lucid_cas_ss with charachange
    with Pause(0.5)
    show rin basic_absent_cas_ss with charachange
    
    "She blinks, relaxing her muscles which makes me realize how tensed up she was before."

    rin "It's going."

    "Her response gives me pause. Sure, it's something I'd expect Rin to say but her lackluster response sparks my mind to ponder how hard it is to converse with her."

    "Rin either says nothing at all, or too much. Trying to understand her trains of thought feels like wading through the jungles of Borneo, equipped with a wooden spoon and the map of southern France."

    "And even after that, there is no phosphorous line to follow, no easy instructions to solve the puzzle."

    "It's annoying, how her thoughts are both laid out in plain sight and hidden from view every time she opens her mouth."

    "I stare at Rin, throwing my willpower in a childish make-believe attempt at mindreading, only met with predetermined failure."

    "One who doesn't believe in mindreading can't succeed in it."

    show rin basic_awayabsent_cas_ss with charachange
    
    "Rin herself doesn't seem to be bothered by my failure to carry on with the budding conversation, so she glances over her shoulder at the canvas behind her."

    rin "I'm going to start on a new one."

    hi "Oh? That's great."

    "My insincere voice makes me feel sick, but not nearly as much as the way we are acting, feigning that there was no yesterday."

    "The honesty is gone, replaced by tension and sadness that we pretend to not be there."
    
    show rin basic_absent_cas_ss with charachange
    
    stop ambient fadeout 1.0
    
    rin "You need to help me."
    
    "She walks to the low table that houses a multitude of paint supplies. Curiosity wins and I follow her."

    rin "I can't use this thing by myself."

    play music music_rain fadein 4.0
    
    "This thing is a neon green butane lighter, lying next to a pack of cigarettes."

    hi "What's this?"

    rin "Cigarettes."

    hi "Where did you get these?"

    "I'm sounding like a father who caught his daughter red-handed. Rin, however, is oblivious to the fact."

    rin "From the lady downstairs."

    "She answers my harsh questions with innocent accuracy, even revealing her partner in crime, the gallerist."

    show rin basic_lucid_cas_ss with charachange
    
    rin "We will now smoke these."

    hi "What? Why?"

    show rin relaxed_nonchalant_cas_ss with charachange
    
    rin "I don't know. I've never done this. Have you?"
    
    "She accompanies her words with a nonchalant shrug, trying to trap me with her false reasoning and ignoring the point of my question."

    hi "Smoking is bad for you."

    show rin basic_deadpannormal_cas_ss with charachange
    
    "Rin rolls her eyes like it's the least of the concerns here, which it probably is truth to be told."

    rin "So what? I need to do this. I want to paint."

    "She wants to smoke a pack of cigarettes to get inspiration?"

    "Self-destruction for art's sake? I can't believe this."

    hi "Is there anything you would not do? For art?"

    show rin basic_awayabsent_cas_ss with charachange
    
    "Rin thinks for a split second, averting her gaze like she does when she doesn't want to get distracted."

    rin "Some things."

    show rin basic_absent_cas_ss with charachange

    rin "I wouldn't eat marshmallows, or move to live in any cold country, or do any other thing that goes against my moral principles."

    hi "Excuse me, did you say you wouldn't eat marshmallows?"

    show rin basic_deadpannormal_cas_ss with charachange
    
    rin "I don't like eating them."

    hi "That doesn't explain the moral principles."

    show rin basic_absent_cas_ss with charachange
    
    rin "Actually, there are not that many things. Just some."

    "She ignores my bewilderment and swiftly moves on."

    rin "Anyway, this is a thing I would do."

    show rin basic_absent_cas_close_ss with charachange
    with Pause(0.5)
    show rin basic_absent_cas_close_ss at centersit with dissolvecharamove
    with Pause(0.5)
    show prop rin_cigarette_close at centersit with dissolve
    with Pause(0.5)
    show rin basic_deadpannormal_cas_close_ss
    show prop rin_cigarette_close
    with dissolvecharamove
    play ambient sfx_rooftop fadein 0.5
    stop music fadeout 10.0   
    
    "Rin bends down to pick a cigarette protruding from the pack between her lips and turns to me, waiting for my response, her eyebrows curved into two challenging arcs."
        
    "Giving a sigh in resignation, I pick up the lighter and raise it to meet the cigarette."

    "I can feel Rin's warm breath against my quivering hand."

    play sound sfx_lighter
    with Pause(0.6)
    show rin basic_awayabsent_cas_close_ss with charachange
    
    "The flame flickers to life on the third strike of the flint and I try to aim the dancing fire at the end of the cigarette."

    show rin basic_awayabsent_cas_ss 
    show prop rin_cigarette
    with dissolve
    
    "An amber-colored glow spreads into the wrapping paper and tobacco as Rin inhales the first smoke."

    show rin basic_lucid_cas_ss with charachange
    
    "To my surprise, she doesn't cough even though she said she is a first-timer."

    show rin basic_awayabsent_cas_ss with charachange
    with Pause(0.5)
    show rin basic_awayabsent_cas_ss at centersitlow
    show prop rin_cigarette at centersitlow
    with dissolvecharamoveslowish
    
    "Rin seems to remember that it's hard to blow the smoke out without spitting the cigarette out as well and quickly sits down on the floor, bringing her foot to her lips like a circus contractionist."

    "She expertly picks the filter between two toes and blows a steady stream of smoke towards the dim sky beyond the glass of the skylight."

    show rin basic_absent_cas_ss at centersitlow with charachange
    hide prop with dissolve
    
    rin "What's the word for smoke that looks like that?"

    hi "There is no word for that."

    rin "We should maybe come up with one."

    hi "Maybe."

    show rin basic_awayabsent_cas_ss at centersitlow 
    show prop rin_cigarette at centersitlow 
    with dissolve
    
    "Rin looks absentmindedly at the cigarette between her toes and takes another, experimental and quick drag."

    show rin basic_absent_cas_ss at centersitlow with charachange
    
    "Her action and the reaction on her face remind me of how after smelling something disgusting you always have to smell it again, as if to subconsciously confirm that your experience, in fact, was not entirely pleasant."

    rin "It's not very tasty. Feels like inhaling the dust lying on top of a forgotten book about the memories of a dead kingdom."

    rin "Do you want some?"

    "My hesitation surfaces again uninvited, making me freeze in the face of a rather trivial and commonplace challenge."

    "Rin's ability to take everything so coolly is something I am a little jealous of."

    "I've never smoked, but this entire situation is like a replay of yesterday, when my sudden outburst of desire to shed my hesitations caused me to burn my fingers badly."

    "Am I going to give up because of that?"
    
    hi "Give me that."

    hide prop dissolve
    
    show rin basic_awayabsent_cas_ss at centersitlow with charachange
    
    "I take a drag of the cigarette, fighting against the choking feeling in my smoke-filled lungs."
        
    "To my embarrassment, I fail and hack my lungs out."

    "I feel flustered, but maybe I didn't lose too much face in the eyes of Rin, especially as they are again lost in search of something in the surroundings that I can't see."

    "It is less unpleasant on the second try but I still pass the cigarette back to Rin."

    "We are like two unruly kids, smoking cigarettes out of the sight of teachers and parents."

    "After a while, the cigarette has shrunk down to the butt."

    show rin invis at Position(xanchor=0.5, yanchor=0.5, xpos=0.5, ypos=0.90) with dissolvecharamoveslowish
    
    "Rin flops down lying on her back on the floor, her eyes probing the sky opening above."

    "Are the cogs of creativity turning behind those eyes right now?"

    rin "Do another one."

    play sound sfx_lighter
    
    "I mechanically pick another cigarette, light it and place it on Rin's lips before lying down on the floor next to her."
    stop ambient fadeout 1.0
    scene ev rin_wisp_blurred at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) 
    show smoke focused at Transform(function=smoke_func, xalign=0.5, yalign=0.5, subpixel=True)
    with delayblindsfadesilent
        
    play music music_serene fadein 2.0
    
    "A thin haze of steely blue smoke slithers towards the ceiling in very fish-like movements."

    "It billows in the stagnant air of the atelier, twisting and turning around its own immaterial body until it dissipates in thin air."

    rin "Fake if."

    "Not understanding her blurry words, I glance at Rin, who is again having trouble with the cigarette."

    "Now that she is lying down, she can't reach it with her foot."
    #Maybe add an 'easily' in there? -SC

    show smoke blurred at Transform(function=smoke_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve
    show ev rin_wisp2 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve 
    with Pause(0.5)
    show ev rin_wisp3 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve 
    with Pause(0.5)
    show ev rin_wisp4 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve 

    "I pick the cigarette from her lips and place it on mine, abandoning common sense and good reason while I do so."

    "First one should've been enough for me, but I take another drag, still coughing a little at the unpleasant sensation of smoke in my respiratory organs."

    show ev rin_wisp1 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve 

    hi "I remember doing something like this before."
    
    rin "So you have smoked? Doesn't look like it though."

    hi "Nah, lying on my back and looking at the sky with you."

    rin "Oh."

    show ovl rin_galleryskylight at Zoom((800, 600), (0, 0, 1000, 750), (100, 75, 800, 600), 30.0, bilinear=True) with locationchange  
    
    "The wide sky, opening on the other side of our small window into it, is slowly growing darker."

    "It's unreachably high, no matter how we limit our vision."
    
    "I return the cigarette back to Rin's mouth."

    "It feels bad somehow."

    "The space between us, less than my arm's reach, still is there."

    "It is the distance between us, the immeasurably wide chasm of thoughts and feelings that separates us with graver certainty than even light years of physical distance could."

    "By saying the right words, there might be a way to make that chasm narrower, even if it's just a little."

    "I tried to cross that gap with one big step, but Rin turned her back at me."

    "I glance at her from the corner of my eye."
    
    show ev rin_wisp2 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with None
    hide ovl with dissolve   
    
    "Rin is staring upwards, through the smoke-filled ceiling and the skylight at the darkening sky above us."

    "It's almost like she is sleeping even though I know she isn't. Her eyes are open, as is her mouth."

    show ev rin_wisp1 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve
    
    "I take the cigarette from Rin before it falls on her cheek."

    "She doesn't react to my touch in any way."

    "So, this is where we are now."

    "I wonder if we ever can be closer than this."

    show ev rin_wisp3 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve 
    with Pause(0.5)
    show ev rin_wisp4 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve

    "I take a drag of the cigarette and blow a thin stream of smoke upwards."
    
    "These indirect kisses are the only things that connect us right now."

    show ev rin_wisp1 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve 

    "The taste of Rin's lips on the filter, mixed with the ashen taste of the smoke."

    "Her soft lips against my fingers as I press the cigarette on her mouth, as if she was placing kisses on them."

    show ev rin_wisp4 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve
    
    "The ash, softly falling on the floor between us like virgin snow."

    play sound sfx_lighter
    with Pause(0.5)
    show ev rin_wisp2 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve
    
    "As the second cigarette finishes, I already am lighting the third one."

    "The only thing breaking the stillness of the atelier is the inaudible sound of smoke floating towards the first stars blinking overhead."

    show ev rin_wisp3 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve 
    with Pause(0.5)
    show ev rin_wisp4 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve
    
    "Light nausea hits me by fourth or fifth cigarette."
    
    "Before long, the shape of the waxing moon appears in the skylight, shedding her wan light down on us."

    show ev rin_wisp3 at Transform(function=wisp_func, xalign=0.5, yalign=0.5, subpixel=True) with dissolve
    
    "It seems to be tempting us with the fairytale promises of flying to a world of dreams, which always seem to be somehow very moon-centric."

    "I wonder what is up with that."

    hi "It'd be nice to be able to fly."

    "I flinch after realising it was my voice that gave birth to the remark, the bastard child of the almost inebriating smoke and tiredness."

    rin "You can't?"

    hi "You can?"

    rin "Sometimes."

    "She is talking about her dream-visions again I think, but why bother arguing?"

    "This apathy that her flat-out rejection yesterday caused is poisoning my other feelings too."

    "Even coming here feels like mental self-flagellation."

    "Maybe yesterday I said what I said just for the heck of it, but the more I think about it, the worse I feel about it."

    "The vicious cycle of unrequited feelings."

    "I try to push the grim thoughts aside with little success, my mind keeps swirling around what-ifs and only-ifs."

    "Watching the moon slowly creeping higher, I realize that a long time has passed since I came here."

    "It sobers me somewhat, but also reminds me of the sad status quo we are in now."

    hi "It's late. Better get going back to school."
 
    stop music fadeout 6.0
    play sound sfx_rustling
    play ambient sfx_rooftop fadein 1.5

    scene bg gallery_atelier_ni with locationchange

    "I stand up to make leave, but Rin doesn't show any sign of rising up from the floor, thus signalling what I already had half-way guessed."

    hi "Are you going to stay overnight here again?"

    rin "Yeah. It's only half a day tomorrow. Should not be a problem."

    "Trying to pose her reasons as logical rarely works for Rin."

    hi "You've already skipped over half a week. Teachers won't be pleased."

    rin "I don't want to study."

    hi "But what about the exams? Don't you care about graduating? Are you going to bet everything on this…"

    hi "What if this won't work after all?"

    "This is not something I should say to Rin, but I can't stop myself."

    rin "Then I'll do something else."

    "Her lighthearted, easy answer tells me that she really is not concerned in the least about the exams."

    hi "Fine."

    hi "Goodnight."
    stop ambient fadeout 1.0    
    window hide dissolve
    scene black with Dissolve(1.5)
    return
    
label en_R27:

    scene black with fade 
    with Pause(1.0)
    nvl clear
    scene bg school_dormhisao_ni with locationskip
    with Pause(1.0)
    nvl show dissolve
    
   
    play music music_night fadein 0.5    
    
    n "\nThose are the last words I say to her for almost a week."

    n "I just don't feel like going to the atelier at the top floor of 22nd corner anymore and unsurprisingly, Rin doesn't feel like coming to school despite the nearing end of trimester exams."

    n "Or if she does, we don't see each other."

    n "It's an unfortunate drawback of the gallerist giving her that atelier, but it's not Sae's fault."

    n "Nomiya set Rin up so that she can make up the exams she misses later. Our school is very laid-back like that."

    n "Anyway, as we are separated to our own little worlds, I try to pay attention to other things."

    n "Mutou keeps on saying that I should aim for physics or engineering after graduation."

    n "If he keeps that up, soon I will believe in that myself."

    n "Otherwise the days are pretty boring, the pointless kind that you remember as one formless mass of the old same."

    nvl clear

    n "\n\n\nThe catalyst for my next trip downtown comes from an unexpected source."

    n "Mom calls me sometime after dinner, saying that she misses me and that I should come home for the summer vacation."

    n "Why not, I suppose and I miss you too Mom even though it's a half lie but not saying it would break your heart."

    n "I've been fine and so have you, that's dandy."

    n "Yes I will come home over the vacation."

    n "But I think I will stick around until Rin's exhibition opening."

    n "Just a friend. Yes."

    n "I end the phone call with the fifth promise to go home for the vacation."

    nvl clear

    n "\n\n\nI wonder how she is doing."

    n "Not my mother, Rin."

    n "I haven't seen her for a while, and I still keep wondering if she is fine."

    n "She didn't seem to be too stressed, apart from her unusual quietness and seclusion bordering on becoming a full-time hermit."

    n "Well, maybe she is stressed."

    n "She handled the added pressure from schoolwork by ignoring it completely, which is quite like her, but…"

    n "It's not {b}that{/b} late yet. I could go visit her."

    n "I really do wonder how she is doing."
    
    nvl hide dissolve
    play sound sfx_rustling
    with Pause (4.0)
    play sound sfx_doorslam 
    stop music
    scene black with vpunch
    with Pause (1.0)
    
    scene bg gallery_atelier_ni at left with fade
    $ renpy.music.set_volume(0.6, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 0.5
    with Pause (0.5)
    play sound sfx_dooropen
    with Pause(2.0)
    play sound sfx_doorclose
    with Pause(1.5)
     
    
    #enter atelier and Rin… damn I'm very uncertain of using this particular narrative device in a visual novel… it's not the first time I use it and it might look really weird.

    window show dissolve
    
    rin "I can't paint."

    "She is lying phlegmatically on the floor of the atelier, inanimate as if all life was sapped away from her body."

    "How long she has been there, I don't know. From the looks of it, I suppose more or less since she realized that she can't paint."

    "I wonder what is up with Rin and lying on one's back, somehow the two seem to go together very naturally."

    "Anyway, she's been that way at least since I came here and I'm not sure what to do. At least she is talking."

    hi "You have an artist's block?"

    "She moves her eyes from the skylight to me slowly, making it look like the act causes great pains to her."

    rin "That's the word for when you can't paint, right?"

    hi "Probably so."

    rin "It's never been like this."

    hi "Are you nervous? About the exhibition?"

    rin "I pick up a brush then I want to put it down right away."

    rin "And then I do."

    play sound sfx_rustling
    with Pause(3.0)
    play sound sfx_impact

    "She raises her head up with difficulty to look at her bare toes, then drops it melancholically back on the floor with a low thud."

    hi "How long it's been like this?"

    "I sound like a doctor diagnosing a patient. Must be contagious."

    rin "Five."

    hi "Five days?"

    rin "Five dinners."

    "I wonder what that translates to."

    hi "How many times sun has come up and gone down?"

    "She has to think about this for a moment."

    rin "Two and a half."

    show ovl rin_galleryskylight with locationchange

    "I glance at the almost full moon visible through the window."

    "Seeing the half-clouded sky hanging over the town reminds me of something I used to do what feels like a horribly long time ago."

    scene bg gallery_atelier_ni at left with locationchange
    
    "The same impulse I had back then hits me strongly and I turn back to Rin."

    hi "Let's go."

    rin "Where?"
    
    hi "I'll show you my secret place."

    "Yes, Rin was right and I was wrong. I do have a secret place after all, even though I never had imaginary friends or secret languages."

    "It just took me a good while to figure out what it meant."

    hi "I don't know if it works in this town, but we can try."
    
    show rin relaxed_sleepy_cas_ni at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.35) with charaenter
    
    hi "In any case, you need a break. And probably something to eat."

    show rin relaxed_nonchalant_cas_ni with dissolvecharamoveslowish
    
    "I grasp Rin by her short and thin arm and try to draw her up"

    "To my surprise, she complies and stands up with some help from me."

    "I notice again how little Rin weighs."

    hi "Come on."

    show rin basic_absent_cas_ni with charachange

    hi "You need to get your thoughts away from this for a while."

    show rin basic_deadpannormal_cas_ni with charachange
    
    "When they are troubled, most people escape their unhappy lives to a world of fantasy."

    "The solution for Rin is probably to escape from her dream world to the real one."

    scene bg gallery_staircase_ni with locationchange
    
    "Rin doesn't look happy but I ignore her. At least she is somewhat cooperative, walking after me first the stairs down and then out to the street."
     
    scene bg city_street2_ni with locationskip
    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')
    
    "The night has fallen upon the town."

    "It is a gentle summer night, less oppressive than those of fall or winter."

    "The sunlight is replaced by shining neon colours and bland yellow street lights, and the air is easy to breathe."

    "The feeling of the hot summer day lasts long into the evening and night."

    "Now then…"

    "I grab Rin by her sleeve like I've seen Emi do and to my surprise, she obediently follows."

    "The pale street lights are fighting against the all-enveloping darkness as we walk, the guide and the guided although neither knows where we are going."

    "But it doesn't matter."

    "We can't get lost."

    "This is the one moment where the usual silences that have become a ritual between me and Rin fit perfectly."

    scene bg city_street3_ni with locationchange
    
    "We walk side by side, choosing directions by impulse or inspiration, sometimes finding ourselves back at a place we had already seen once or twice."

    "Sometimes finding new places."

    "Rin doesn't ask where we are going. Maybe she doesn't care. Maybe she knows I couldn't answer her."

    "The silence of the night is not scary, after all the lights drive most of it away."

    $ renpy.music.set_volume(0.0, 2.0, channel='ambient') 
    "The air is becoming cooler as the moon progresses along its journey in the cloudless sky."

    scene bg city_streetnight with locationchange
    
    play music music_comfort fadein 4.5
    "I buy some hot coffee and snacks from a vending machine and we sit down on a bench to consume them."

    "There is no time in the night of the town."

    "Thus we spend an uncounted amount of it just sitting there, observing the stillness of the usually so vivid townscape."

    "Still, it's getting very late."

    "Few cars are trickling down the streets and even less people are around."

    "The apparent lack of nocturnal life is somehow very fitting of this place."

    "There are around-the clock shops and cafés, sure, but the atmosphere is like the town itself was slumbering."

    "This town sleeps eight hours a day."

    "The city, bathing in the electric glow of a million lightbulbs, never slept."

    "I have seen it, it's not the first time I'm doing this."

    "It was one of the first times I was left home alone."

    "Both of my parents had business trips neither could cancel, so they deemed me old enough to survive two days by myself."

    "Their misplaced trust in me did not go to waste, as I proceeded to spend the entire night out in the city."

    "Afterwards, I could not say what made me stay in downtown longer than I intended after school."

    "I did not feel like going to home, so I stayed through the evening and eventually through the entire night."

    "I walked long concentric circles around a randomly chosen landmark."

    "For some reason, the nightly city felt fascinating."

    "So I walked its streets."

    "At every intersection it was possible to choose your direction at random because they all lead nowhere."

    "The aimless wandering made me see things differently."

    "The lack of anything to do gave my brains time to mull over… whatever I was thinking about back then."

    "I can't remember anymore."

    show rin basic_absent_cas_close_ni at tworight with charaenter

    rin "Is this it?"

    $ renpy.music.set_volume(0.69999999999999996, 1.0, channel='music')

    "Her voice drags me from my reminiscence."

    "She doesn't sound bored. Rather, her tone is inquisitive, uncertain as to why I dragged her out here but curious to find out."

    hi "Yeah. Have you ever been out all night? It's like a different world."

    show rin negative_spaciness_cas_close_ni at tworight with charachange

    "The remark sends her thinking for a while, looking around as if she was looking for something."

    "The wisps of light reflecting from the corners of her eyes are suddenly very sharp."

    show rin basic_lucid_cas_close_ni at tworight with charachange

    rin "It's not a different world. It's the same world, just asleep."

    show rin basic_awayabsent_cas_close_ni at tworight with charachange

    rin "What do you think this town is dreaming of? Maybe something like car sheep or cloud sheep? Why are dreams always about sheep or phallic objects?"

    rin "I've never seen a sheep dream."

    show rin basic_deadpannormal_cas_close_ni at tworight with charachange

    rin "Do different towns dream of different things?"

    hi "Probably. How could they not?"

    "I answer half joking, half spurring her on. For the first time tonight, Rin seems like a bit of her life has returned to her."

    show rin negative_spaciness_cas_close_ni at tworight with charachange

    $ renpy.music.set_volume(1.0, 5.5, channel='ambient') 
    stop music fadeout 5.5
        
    "She doesn't continue her list of rhetoric questions though."

    "The cool breeze blowing between the buildings seems to steal the conversation before it even really begins."
    $ renpy.music.set_volume(1.0, 0.0, channel='music')
    "Too bad, it looked like Rin would get out of her blue mood."

    hi "Are you cold?"

    "I ask because I am."

    hi "Want go there to get somewhere warm?"

    "We are standing in front of a 24h karaoke place. The red neon light sign is missing the last character, but it doesn't matter."

    show rin basic_deadpancontemplation_cas_close_ni at tworight with charachange
    
    rin "Will you sing?"

    "Rin's pensive expression tells me that she doesn't fancy singing, but it's not the first thing in my mind either."

    hi "No."

    show rin basic_deadpandelight_cas_close_ni at tworight with charachange
    
    rin "Then we can go."
    
    stop ambient fadeout 1.0

    scene bg city_karaokeint_ni with locationskip
    with Pause(1)
    show rin basic_absent_cas_close_ss at centersit2 with charaenter
    $ renpy.music.set_volume(0.35, 0.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 0.5
        
    "The insides of the karaoke parlor are warm and welcoming."

    "A friendly looking lady greets us, and after collecting my money shows us to a room with promises of bringing the coffee I ordered right away."

    hi "Do you want something else?"

    show rin basic_awayabsent_cas_close_ss at centersit2 with charachange
    
    "She shrugs dismissively but more importantly, in asking that I realize how little I really know about Rin."

    "Emi is right, she rarely tells anything substantial about herself."

    "Her preferences, her dislikes… I know something of that, but I feel like I know nothing of her."

    "It's like Rin is open to everything, equally (dis)interested in everything on the outset."

    "Only giving straight answers if asked, and only of things she is certain about."

    "Sometimes she locks herself inside her inner world, shutting everything else out."

    "Other times, her thoughts flow freely from her mind, but they are not organized in a fashion that would make them intelligible to anyone else."

    hi "Do you ever feel like you are trying to reach out for something that is impossible to reach?"

    show rin negative_spaciness_cas_close_ss at centersit2 with charachange

    "Rin turns her gaze from the track catalogue she was absentmindedly shuffling with her feet, tilting her head quizzically."

    "I like how I nowadays manage to catch her attention just by speaking aloud."

    rin "All the time."

    show rin negative_confused_cas_close_ss at centersit2 with charachange
    
    rin "At least I think so. Isn't that just what painting is?"

    "Huh. Never thought about it that way."

    "But she is right, of course. Pictures of ideas."

    "She told it to me before, how art and intent rarely meet, and the end result is only an approximation, an echoing image of the almost Platonic idea the artist has."

    "It's kind of sad, if nobody ever will see what the artists really wants them to see."

    hi "I wish I could understand you."

    show rin basic_sad_cas_close_ss at centersit2 with charachange
    
    "She looks at me melancholically, roused by my thoughts materializing as spoken aloud words."

    rin "Me too."

    "Whether she meant she wished for me to understand her, her to understand me, or her to understand herself, I never ask, nor do I find out"

    show rin basic_awayabsent_cas_ss at centersit with dissolvecharamoveslowish
    
    "Rin lies down on the couch, looking very tired although the sharpness that took over her when we were outside has not left her eyes."
    
    "The fatigue from the walking has piled up on my shins too so I follow suit, claiming the other couch that is perpendicularly placed."

    "Our heads are pretty close to each other, but neither can see the other."

    "We lie there, looking at the ceiling."

    "When the coffee arrives we drink it, banishing the drowsiness for a while."

    "This self-inflicted insomnia is not as bad as the drug-induced one I was suffering from the first weeks here, but I still feel like sleeping would be a good idea."

    "I can't fall asleep though, despite the drowsy feeling and the almost comfortable couch."

    "The ceiling tiles are tempting me to count their number but I resist the urge."

    "At some point I wonder if I should put on some karaoke background music to fill the void of silence, but decide against it."

    "This impulsiveness is strange. First spending the night out in the town, now this."

    "I don't feel like me. But I just needed to do something. Couldn't let Rin stay there lying on the floor."

    "Maybe it spurred from that."

    "I don't know if it will help, but rationally thinking, getting your mind away from something should give you new perspective and such when you get back to it."

    "Problem is, rationality never was a thing for Rin."

    "It doesn't restrict her like it restricts me."
        
    play sound sfx_pillow
    show rin basic_deadpanupset_cas_ss at centersit with charachange
    
    "I feel something slap against my face and then fall along my cheek."

    "It's Rin's sleeve."

    "It's so rare to see her even moving her arms, much less slapping someone with her empty sleeve that I just turn my face to look at her, dumbfounded."
    
    show rin basic_deadpannormal_cas_ss at centersit with charachange
    
    rin "Don't worry."

    "I see her eyes searching for mine, serious and cryptic as they are, I'm not getting any explanation from there."

    "What does she mean? Did she just read my mind?"

    hi "I will."

    show rin basic_deadpanamused_cas_ss at centersit with charachange

    "She half sniffs, half breathes in at my response, Rin's equivalent for the dry chuckle these kinds of jokes are supposed to evoke."

    "Small hints of a smile are wavering on her lips as she turns back to look at the ceiling."

    show rin basic_awayabsent_cas_ss at centersit with charachange
    
    "When she is like this, it makes me feel that maybe there is hope for us."

    "We get along so well for being so different."

    #"It's just, we never {b}really{/b} get along, because we are so different."

    "It's just, we never really get along, because we are so different."

    "Maybe it was Rin's passionate approach to her own art exhibition, maybe it was my careless words, but last week was different from usual."

    "The small friction between us seems to be somewhat volatile, but at least we now seem to be back to normal."

    "Relatively speaking."

    #timeskip

    stop ambient fadeout 1.0
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    scene bg city_karaokeext with delayblindsfadesilent
    play ambient sfx_rooftop fadein 0.5
    
    "When the time is over, we are already ready to leave back into the night."

    "We pick yet another direction to go."
    
    scene bg city_street3_ni with locationchange

    "The wee hours are passing slowly as we measure the streets of the town one step at a time."

    "The relaxed atmosphere that the interlude at the karaoke place created breaks through the night, giving us the sense of wild freedom that this kind of thing is supposed to give."

    "We are finally at ease, not minding the lone and rare passers-by, the eerie darkness, each other, ourselves."

    "We don't talk, save for the single remarks that are spoken into the night of the town and never answered."

    "The details jump into the eye instead of the usual blur they are during the day."

    $ renpy.music.set_volume(0.4, 6.0, channel='ambient')

    scene bg misc_sky_ni with locationchange
    
    "As the sky above the town changes from deep dark blue to grey, I know that our night is soon ending."

    hi "It's almost morning."

    "Rin looks up too and nods at me."

    "It's true. We've been staying up all night, and now the twilight's creeping through the sky, climbing higher by the minute."

    "It feels surreal."

    "Sun won't come up for a while, but I get the feeling that the end of this night really is here."

    scene bg city_street3_ni at left 
    show rin basic_absent_cas_ni at center 
    with locationchange

    hi "Should we get back to somewhere?"

    "My silent companion nods again, twice, her hair waving in the breeze that seems to be heralding the morning."

    hide rin with charaexit

    "Abruptly, she takes off, taking the lead of this walkabout that has so far been in my hands."

    scene bg gallery_ext_ni 
    show rin basic_awayabsent_cas_ni at center 
    with locationskip
    
    #Original: "Rin's navigational skills are probably not any better than mine, but eventually we find ourselves at the bus station.", but the bus station BG I have doesnt look well at night. - Kelper
       
    "Rin's navigational skills are probably not any better than mine, but eventually we find ourselves in front of Sae's place."

    hi "I don't know if this was any help. I've done this a few times before, but it was then more because of a stupid impulse or not being able to sleep or that kind of thing."

    hi "Maybe it was silly and didn't help you at all."

    show rin basic_lucid_cas_ni with charachange
    
    "She just nods as an answer."

    show rin back_cas_ni with charachange

    "Rin turns around to leave, but instead of taking off, she hesitates a moment, and turns back again to face me."

    show rin basic_deadpancontemplation_cas_ni with charachange
    
    $ renpy.music.set_volume(0.29999999999999999, 1.0, channel='ambient')
    
    rin "Touch me."

    hi "What?"

    show rin basic_deadpannormal_cas_ni with charachange
    
    rin "You say that too often. Just do it."

    "Is this some silly dare? No, Rin is not that kind of a person."

    "I raise my hand hesitantly even though I don't know what for I am doing this."

    "Her eyes tell me that she's not going to explain."

    stop ambient fadeout 2.0
    play music music_twinkle fadein 4.5
    show rin basic_absent_cas_close_ni with dissolvecharamove
    
    "A thousand thoughts race through my head as I slowly bring my hand closer to Rin's face and press three fingers against her pale cheek."

    "Rin feels soft and cold."

    show rin basic_lucid_cas_close_ni with charachange
    $ renpy.music.set_volume(1.0, 0.0 , channel='ambient')
    "She closes her eyes on the contact, and visibly relaxes."

    "I can feel her soft breathing, her muscles releasing tension as the tips of my fingers caress her soft cheek."

    "She doesn't rest her head against my palm, or anything else you'd suspect a girl would do, in fact she doesn't react in any way save for her now shut eyes."

    "She just wanted me to touch her."

    "Or maybe anyone would've been sufficient?"

    show rin basic_deadpanamused_cas_close_ni with Dissolve(1.5)
    
    "Once I withdraw my hand, she opens her eyes."

    "It might be just an illusion created by the timid morning sunlight playing in her eyes, but Rin looks like she is holding back a smile."

    "This is the problem with our relationship."

    "Half of the time I have no idea what is going on and  the other half of the time I just fail to understand why things are going on like they are."

    show rin negative_spaciness_cas_ni with charachange
    
    rin "See you."

    hide rin with charaexit
    
    #Original: "Without saying another word, Rin turns around for the final time and starts to walk in the direction of the gallery and the atelier." - Kelper

    "Without saying another word, Rin turns around for the final time and starts to walk in the direction of the atelier."

    #Original: "I watch her go until she disappears around the corner." - Kelper

    "I watch her go until she disappears."

    "As for me?"

    "Well, morning classes are starting in a few hours I guess."

    window hide dissolve
    stop music fadeout 3.0
    scene black with Dissolve(1.0)
    
    return

label en_R28:
    
    scene black
    with Pause(2.0)
    
    scene bg city_street4_ni_ss with locationskip
    play ambient sfx_rooftop fadein 3.0
    window show dissolve    

    "The buses are not yet going, so I'm faced with a choice."

    "Either wait here for the first bus, or walk the distance to the school."

    "I choose the latter, my conscience nagging to me about my lack of exercise despite promising the Nurse otherwise."

    $ renpy.music.set_volume(0.3, 0.0 , channel='music')
    
    play music sfx_footsteps_hard
    
    "So, for the last time tonight, I begin walking."

    "The stars are already gone and the previously dark night sky is turning into pale blue in anticipation of the sun."

    "It has not quite yet risen, barely staying below the artificial horizon of the town's admittedly low skyline."

    "Now that I'm alone, the feeling of emptiness strikes my senses more forcefully."

    "The eerie silence creeps under my skin and into the marrow of my bones. I find myself shivering even though it's not especially cold."

    "It's only because nights are always chilly, I tell to myself."

    "I brace myself against the cold and the quiet air of the empty streets and keep on walking."

    "The school then, where is it?"

    "I am not entirely certain where to go."

    "Is my adventurousness folly, as I haven't lived in this town long enough to get familiar with the local geography?"

    "I'm not exactly certain how to get to the school, but at least I know the general direction."

    "It shouldn't be impossible to find some kind of landmark once I'm closer."

    "As I walk alone the streets, I have time to think about Rin."
    
    window hide dissolve
    nvl show dissolve    
    
    n "Her distance to all things is equal."

    n "That is to say, everything is unreachably far away from her."

    n "Her mind is the center of her universe, and everything else is revolving around it."

    n "It could just as well be that she is living on another planet, or dimension."

    n "I think she tries to reach back, maybe with her art, maybe not."

    n "Still, she remains isolated."

    n "From me and from everything else, even Emi, or the art teacher."
    
    nvl hide dissolve
    nvl clear
    
    image bg dawning = anim.TransitionAnimation("bgs/suburb_roadcenter_ni.jpg", 0.0, Dissolve(60.0),
                                                 "bgs/suburb_roadcenter.jpg")
    
    $ renpy.music.set_volume(0.5, 2.0 , channel='ambient')
    
    scene bg dawning with locationskip
    
    window show dissolve
       
    "The higher buildings of the downtown melt into the houses and flats of the suburb as I make myself towards the hills."

    "The sounds of the waking town are behind me, leaving me feeling even lonelier in the still sleeping suburban streets."

    "Morning is slowly vanquishing the night, leaving the pale twilight behind."

    "The borders surround me from every side."

    "Night's border against the day."

    "The border of the downtown behind my back and the school in front of me."

    "My past, my future."

    "Is that what my time in this school has been so far?"

    "No. Each and every second of our lives all of us are standing on the border of the past and the future."

    "I am no different, no matter what I've been going through."

    "On what border am I really standing on?"

    "On what border is she standing on?"

    "Are we doomed to forever stay in this gray no-man's-land?"

    window hide dissolve
    nvl show dissolve   
    
    n "Once her seclusion became physical it also became somehow more real, even though she's really been like this all the time."

    n "Her attention is fluttery and superficial, annoying in its incoherentness."

    n "She jumps randomly from topic to topic, leaving a trail of paintings and confusing half-finished thoughts in her wake."

    n "But she has grown on me."

    n "I hold her dear to me, at some level."

    n "I really do."

    n "I think."
    stop ambient fadeout 1.0
    nvl hide dissolve
    nvl clear
    with Pause(1.5)
    scene bg school_road with locationchange
    nvl show dissolve
    $ renpy.music.set_volume(1.0, 0.0 , channel='ambient')    
    play ambient music_dreamy fadein 6.0
    
    #"The Shanghai catches me by surprise, as I didn't expect finding it here."

    #"As it's unlikely that it has moved overnight, I assume I got lost, or at least confused of my whereabouts."

    #"Which is not really a different thing from getting lost."

    #"The small café is not open yet but I am glad."

    #"Great, from here I know for sure how to get to school."

    #"The convenience store is nearby and from there it's just walking down the road to the school."

    # Previous lines were scrapped because I cant find any Suburb at night BG that doesnt fuck with the established layout. Ill put them back if I can find one, but its unlikely. - Kelper
    
    n "Have I grown on her?"

    n "Maybe so, I haven't seen her socializing with many other people."

    n "She said she wanted me to be her friend, but in the end, what does that mean?"

    n "Without context, it's just another word."

    n "She kissed me, twice, then she acted like I was mere air."

    n "She wants me to be close, but not too close."

    n "How to break through to her?"
    
    nvl hide dissolve
    nvl clear
    
    window show dissolve
        
    "The gates of the school beckon me from the distance, just when my legs are about to give in."

    "Morning has come for real while I journeyed up here from downtown."

    "I am not the only person out here anymore, as people and cars move about in their busy morning routines."
       
    stop music fadeout 1.0
    scene bg school_dormhisao with locationskip
    
    "Going to class would be futile so I just walk straight to my dorm."

    "The bed has never looked this delightful."

    "I only manage a few half-coherent thoughts before falling asleep."
    window hide dissolve
    scene black with shuteye
    
    nvl show dissolve

    n "This limbo of uncertainty is maddening."

    n "I just can't figure out the way out of there."

    n "What does she want?"

    n "What do I want?"

    stop ambient fadeout 6.0
    
    n "There never seems to be “us,” rarely even “we,” only me and her."

    n "The distance between us exists and it is vast."
    nvl hide dissolve
    with Pause(2.0)  
    
    window show dissolve
    
    #fade to blacker?

    "I sleep late that day."

    scene bg school_dormhisao_ss with openeye
    
    "Really late. It's past the end of afternoon classes when I finally wake up with a massive headache and a somewhat disorientated feeling."

    "This is probably why they say allnighters are not healthy."

    "I have missed taking my morning medications too, so I swallow them now, hoping that it won't be such a big deal."

    #this dinner thing is a chance for side character time/other girls, if future Aura ever wants

    "Eating dinner for breakfast feels disgusting, but I haven't really eaten anything since yesterday's dinner."

    "Wow. Time really got screwed up."

    "Feeling like this, it's futile to even try to do anything sensible."
    
    "The fatigue has its grip pretty tightly around my head, so I loiter around my own room until I become tired enough to sleep again."

    "This day was a waste, but that's how some days are."
    
    window hide dissolve
    scene black with Dissolve(1.5)
    $ renpy.music.set_volume(1.0, 0.0 , channel='music')        
    
    return

label en_R29:
    
    scene black 
    with Pause (1.5)
    scene bg school_scienceroom with locationskip
    play music music_pearly
    window show dissolve

    "The morning class of the next day starts with a pleasant surprise."

    show shizu behind_frown at tworight
    show misha hips_smile at twoleft
    with charaenter
    
    "Despite Shizune's unapproving glare, Misha is kind enough to give me notes of yesterday's classes."

    play sound sfx_impact
    show misha sign_smile_close at twoleft with vpunch
    
    mi "Here you are Hicchan, notes fresh from Shizune's notebook!"

    show misha cross_grin_close at twoleft with charachange

    mi "Now then, I wonder what you could do in return~"

    hi "I can buy you a lollipop or something."
    
    show shizu cross_wut at tworight with charachange
    with Pause(0.5)
    show misha cross_laugh_close at twoleft with charachange
    
    mi "Awww, that would be sweet of you."

    "I wonder if she is just being nicer than usual or too stressed about exams to remember teasing me about being absent?"

    scene bg school_scienceroom with shorttimeskip    
    
    "The classes pass in waiting of the end of school day."

    "I spend some time revising the old stuff from June and May. I missed the first month of school so I had to catch up as fast as I could."

    "It was not a problem, but I felt and still feel like I am working twice as hard as the others."

    scene bg school_dormhisao with delayblindsfadesilent  
    
    "The dinner is somewhere between flavorless and repulsive as usual, but I don't care."

    "I'm feeling good and with my vigor returned, I dare a venture downtown to see Rin after a bit more of schoolwork."

    window hide dissolve
    with Pause(0.5)
    play sound sfx_switch
    scene bg school_dormhisao_ni with None
    with Pause(0.8)
    scene bg city_busride_ni with Fade(0.5, 1.0, 0.8)
    $ renpy.music.set_volume(0.6, 0.0 , channel='ambient')
    play ambient sfx_businterior fadein 1.0
    window show dissolve
    
    "It's late again but I really had to study. The exams are next week already."

    "After all, I don't have the luxury of a teacher backing me up if I fail."

    "I wonder if she got her inspiration back."
    
    stop music fadeout 10.0
    "The bus trip is my new favorite moment of urban zen when the rumble of the engine prevents me from hearing my own thoughts."
    
    stop ambient fadeout 1.6
    scene bg gallery_ext_ni with locationchange
    
    "It is soon over though and I leisurely walk over from the bus station to the 22nd Corner."
    
    scene bg gallery_staircase with locationchange
    
    "The stairwell is as damp and depressing as ever, making me want to run up with haste but then I'd just be out of breath at the top."

    $ renpy.music.set_volume(1.0, 0.0 , channel='ambient')
    "I enter carefully, in case she is in the throes of a creative process."

    scene bg gallery_atelier_ni with locationchange
    
    "The room is dark because of the quickly falling night, but I can see Rin, or rather her silhouette, sitting on the floor."

    "So she's got her inspiration back and moved from easel to painting on the floor."

    "Before I manage five steps I stop, frozen on my tracks."

    "The cognitive ability of a human is commendable, the ironic realization echoes through my mind."

    "From a mere movement of her shadow it took me a fraction of a second to realize something is awry, process what I'm seeing, formulate the answer and blush."

    play sound sfx_whiteout
    scene ev rin_masturbate_away at Zoom((800, 600), (100, 75, 800, 600), (0, 0, 1000, 750), 16.0, time_warp=acdc_warp) with whiteout
    play music music_moonlight fadein 0.5

    "Rin is sitting on the floor with her legs under her."

    "She moves in rhythmical motions back and forth, slowly grinding herself against herself."

    "Her breathing is so heavy it's almost visible in the dim light. It's the heavy panting of one who doesn't have the option of breathing gracefully."

    "Her hips, mere shadows against the dim light shining on her from above, are swinging circularly over and over again."

    "She hasn't noticed me, so engrossed she is in her… pleasure, there is no mistake."

    "The deadlock solves itself before I get to think what to do next."

    "Something in the atmosphere of the room changes, a little thing, consciously unnoticeable, but it changes."

    "A timid air current from the opened door, the sound of my breathing (even though I notice I haven't taken a breath for many many seconds), the aura of my presence."

    "Something catches Rin's senses."

    scene ev rin_masturbate_surprise at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange
    
    "She stops moving, freezes and slowly turns to the door."

    "I imagine, not see the horror on her face, like a fawn's eyes staring at a hunter."

    "I wonder if Rin can see my expression but at least she doesn't have the strength or the spirit to look straight in my eyes."

    scene ev rin_masturbate_away at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange
    
    "So, she droops her chin against her chest, letting her mess of a hair hide her face from me even further."

    "I feel like I should either walk out or walk to her, but I can't do either."

    rin "Don't come."

    "Her words are…defeated, painful as if she was suffering."

    "Rin doesn't have anything else than her shirt on."

    "I can see the last wisps of the twilight against the pale skin of her thighs and bottom."

    "There is no way I can back off anymore, I lost that chance, so I do the next best thing."

    "I quickly avert my gaze even though Rin doesn't see where I'm looking at."

    hi "Rin… what on earth…"

    scene ev rin_masturbate_doubt at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange
    
    rin "I had to."

    rin "Hisao."

    rin "I tried to stop thinking but then I just kept on thinking more and I think lost my mind and now I can't find it."

    scene ev rin_masturbate_away at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange

    rin "I thought that if I did this I could see it."

    "Her voice is raspy, shivering from held back tears or something else."

    "Rin is a person of extremes, but this… was she trying to paint…?"

    "She is shaking, looking like she is physically in pain."

    rin "You know, that feeling. That moment."

    scene ev rin_masturbate_frown at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange

    rin "You must know."

    hi "Umm, ehh… are you talking about… you know, o…org—{w=0.1}{nw}" #reminder for the potential {nw} break

    scene ev rin_masturbate_away at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange
    
    rin "It's amazing."

    rin "It is that."

    hi "What?"

    scene ev rin_masturbate_frown at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange
   
    rin "That. The truth that you always forget when you wake up."
    nvl show dissolve
    
    rinbabble "It's like a white colored needle piercing the place of your mind where you keep everything you are thinking now and it burns out everything but I can't remember I just can't after it passes, 
               I always forget it and there is no way I can do this if I keep forgetting that, and don't want to why do I always have to forget the important things? I have to paint this I have to and 
               I can see it but I can't remember no matter how many times I try it hasn't worked even once since yesterday there is no way for me 
               I keep thinking of you only you and it won't help even if I do it and touch—" #reminder for the potential {nw} break

    nvl clear
    nvl hide dissolve

    "Rin is mumbling her words into the air more than talking to me."

    "It is the rambling, ranting, raving speech of a lunatic, even and steady in tone, but taking the form of a neverending stream of words spawning from between her lips almost simultaneously."

    "I am not sure if she realizes it is me who is present, or that someone actually is present."

    "Maybe I am a voice inside her head."

    "I look down at Rin's sorry figure, cowering on the floor with only the white shirt of her usual attire on."

    "It neither preserves her modesty that is gone nor her body warmth that she doesn't seem to care about."

    "She looks more broken than I imagined a human person being capable of, and the hospital and school have given me some real perspective on that."

    "I remember the hazy blue smoke, and myself wondering what Rin would do for the sake of art."

    "The realization that Rin really is always serious hits me with its entire weight."

    "She really and truly would destroy herself if her art required it."

    #Original line: "I thought she was so silly with her strange ways, insisting on the headphones and whatnot to create art."   - Kelper
    
    "I thought she was so silly with her strange ways, insisting on the earphones and whatnot to create art."

    "I had no idea."

    extend "That was just warm-up."

    "This is Rin."

    "This is her, laid bare in front of my eyes in all possible meanings of the word."

    "Complete isolation here in the top floor of this building, in this room, in her mind."

    "Day after day, working on her paintings with no heed paid to anything else."

    "Obeying her primal impulses, the spring of her creativity."

    "Breaking herself to reach that which she wishes to reach but can't."

    "Slowly wearing herself away in a delirium of creative compulsion that slaves her with more power than any worldly taskmaster could."

    "This… obscene act that she does for reasons I'm not sure if she herself understands."

    "Why?"

    "Why does she have to do this?"

    "I want to ask but I have lost my voice."

    "I can only stand there, petrified by the horrifying realization."

    "The acknowledgement that Rin said she was thinking of me – me! – rages somewhere in the back of my head, but seeing Rin broken like this quickly subverts it."

    "I feel sad, scared, elated, excited, disgusted, worried and a number of emotions I can't remember the name of now."

    "Conflicted."

    "I need to clear my head, so the question that comes out is not the one I wanted to ask."

    hi "Rin… you've been here since yesterday morning… umm… touching… yourself?"

    "My voice is dry and quiet, like sandpaper coming out of my throat."

    "She can see that I'm still mentally wrestling with my first and foremost observation and what is in my mind one of the biggest issues here."

    "What is worse, my mind is still on an overdrive trying to figure out if it's physically possible to do {b}that{/b} without… without fingers."

    scene ev rin_masturbate_doubt at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange

    rin "It doesn't help. Even when I make it feel good, I feel bad."

    "She doesn't continue, doesn't explain. I'm trying to connect the pieces but I don't understand."

    scene ev rin_masturbate_away at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange
    
    "All I can see is her sadness."

    "Rin doesn't shed tears."

    "But she is sad inside, so sad even I can feel it despite the physical distance between us."

    scene ev rin_masturbate_hug at Zoom((800, 600), (0, 0, 1000, 750), (0, 0, 1000, 750), 0.0) with locationchange
    
    "I steel myself, walk to her to crouch down behind her and lightly touch her forehead."

    "It's like in a fever, at the same time freezing cold and burning hot."
   
    "There is a blanket on the couch, but I wrap my arms around Rin instead of fetching it."
    
    "She does not resist my clumsy hug, only slumps her head lower, deepening the shadows hiding her face from me."

    stop music fadeout 12.0
    scene ev rin_masturbate_hug at Zoom((800, 600), (0, 0, 1000, 750), (100, 75, 800, 600), 40.0, time_warp=acdc_warp) with locationchange
    
    "I am not embracing her out of love, nor out of forgiveness for am I in love, or is she sorry?"

    "But I want to hug her."

    "For a moment, the only sound in the room is her heavy breathing."

    "My body warmth, shared between two people, is barely enough but slowly, painfully slowly it spreads from me to her."

    "I wonder if Rin is sick with cold again."

    "It was cold the night we spent out and she's been unclad like this for who knows how long."

    "The small warmth returning to Rin makes me more conscious of her body against mine."

    "Even in the darkness, I can feel the fleeting scent of Rin's hair, the dried paint stuck in her clothes, the skin of her neck."

    "The hardness of her bones and the softness of her flesh."

    "Her heartbeats echoing mine."

    "The hot blood rushing inside me reminds me why I said what I said back then, why I came here even after that, why I am here tonight again."

    "Why I am hugging her now to keep her safe against the cold and the sadness."

    "Rin has really grown on me inside my heart, claiming a small part of it as her own without even particularly trying."

    window hide dissolve
    
    centered "Rin." with dissolve
    
    window show dissolve

    "Even if she wanted to push me away, I can't help this feeling."

    hi "Are you all right, Rin?"

    rin "I'm not. I was wrong."

    rin "There are things that can be wrong."

    rin "Everything is going wrong."

    rin "I…"

    "Her voice cuts out, as there are no more words for her to say."

    "It's not an angry voice nor a sad voice."

    "It is a lifeless voice."

    "It only makes the situation worse, and me more worried about her."

    "I pet her head and arms, the physical equivalent of saying “There, there.”"

    "As Rin doesn't specify exactly what is wrong, I can't reassure her with the sweet nothings that people are supposed to say in these kinds of situations."

    "I'm not sure if she would even listen, or be reassured."

    "She didn't react much to my embrace either, as if she didn't care."

    "Maybe she doesn't."

    "At least she doesn't care if she looks sad or not, there are no facades, no attempts to explain herself, no faux happiness."

    "Rin is honest."

    "But she doesn't cry."

    play music music_heart fadein 8.0
    
    rin "Hisao."

    rin "I can't remember it."

    rin "Will you do it?"

    extend "Will you touch me?"

    rin "It has to be you. Maybe then I can…"

    "Her dry voice is a mere whisper but the strength, her last, is in it, delivering her meaning much more clearly than her words."

    "Does she really mean…"

    "Doubts are surging up and down my spine as I am trying to come up with any other explanation."

    "I can feel Rin's heart beating against my chest like a scared little bird."

    "Her entire body is shivering from her fever, from her fear, from her despair."

    "My brains are fast becoming overloaded with the myriads of thoughts this encounter spawned, but I have to push them all aside."

    "Simplest answers are the best."

    "I don't understand her panic, but I want to be there for Rin."

    "She is someone I care about."

    extend "She is my friend."

    "But this, either, is not something that friends should do."

    "I snuggle my nose against her earlobe which is soft and cold and her hair which smells good and tickles me."

    hi "All right. I'll do it."

    "I whisper to her ear reassuringly, trying to make her calm down."

    "It works at least halfway, as Rin closes her eyes and leans against me as if searching comfort from my warmth."

    hi "Relax. It's all right."

    show ovl rin_galleryskylight at Zoom((800, 600), (100, 75, 800, 600), (0, 0, 1000, 750), 30.0, bilinear=True) with locationchange 
    
    "Even though I said that, I'm on the verge of breaking myself."

    "If I wasn't so nervous, I would laugh at my own nervousness."

    "She wants to be comforted, and I want to comfort her."

    "But in this way…"

    "I move my hand lower, touching the naked skin of her stomach, caressing Rin with my hand."

    "Her muscles contract timidly, evading my touch."

    "Presently, she relaxes and lets me feel her. Trust, acceptance."

    return

label en_R29h:

    scene evh rin_relief_down_large at Updownpan(12.0) with whiteout

    "There was one warm place left in her after all, emitting heat that gets even warmer as I move my hand lower."

    "I touch her carefully, feeling the place that is below the coarse curls of hair which are below the tiny belly button."

    "It feels burning and swollen, soft and smooth."

    "She opens under my touch, inviting my fingers to touch her more."

    "Rin gasps at the contact of my hand and her voice is not of pain nor of surprise."

    "Pleasure."

    scene evh rin_relief_down with dissolve
    
    "She was waiting for me, I can tell from the ease she accepts me with, the moistness enveloping my finger, her quiet sigh as I enter the second one."

    "I move my fingers up and down, in and out, touching her from everywhere, first slowly, then faster."

    "I listen to the subtle signs Rin's body gives, hoping that she can guide me as I can't see what I am doing."

    "Her breathing gets heavier by the moment, spurred on by my exploring fingers."

    scene evh rin_relief_down_large with dissolve
    
    "Rin's hips start moving in the same rhythm as me, guiding me deeper."

    "She turns her head, looking at me from the corner of her eye."

    "I wonder what she sees, but what I see in her almost scares me."

    "The passion in her eyes is like nothing I have ever seen, her dark eyes like two black stones against the moonlit skin of her cheek."

    "I kiss her gently, on the cheek right above the bone with my lips that feel like they haven't tasted water for a thousand years."

    "Rin's body, now rubbing against mine wildly, is possessed by her desire."

    scene evh rin_relief_up with dissolve
    
    "My left hand moves on its own accord, upwards, under the white cotton of her shirt to caress the underside her soft breast."

    "Sweat gleams on her skin, making it slippery under my hands."

    "She breathes in sharp, quick intakes in unison with the pulses of her insides against my fingers."

    "I can feel her heat, burning through her shirt against my chest."

    "I move faster and she moves faster, our primitive instincts blinding all reason as her fever becomes sweat drenching her shirt and her skin, her passion becomes my passion that burns my senses like a wildfire."

    "The fabric of reality unravels into its basic components, her softness, her wetness, her hotness, her sadness are the only things that I think, the only things that I can think."

    scene evh rin_relief_up_large at Updownpan(15.0) with locationchange
    
    rin "Ah…"

    window hide dissolve
    nvl show dissolve

    $ renpy.music.set_volume(0.5, 0.5, channel='music')
    
    n "I push Rin over the edge, into the freefall of the mind-stealing, body-breaking madness that she wanted me to give to her."

    n "Her entire being contracts around my fingers in a violent spasm of blinding, deafening, paralysing desire."

    n "Not only her lust, not only her body, not only her mind, everything that Rin is, ever has been and ever will be is right there, in my embrace, around my fingers."

    n "My gift to her is a moment so long that kingdoms rise and fall, gods live and die and stories are written and forgotten as this girl, the only girl I can ever think of from now on, forgets her mortality for this ephemeral, fleeting moment, the divinity of ecstasy pouring into her small body that barely can stand it without breaking."

    n "Rin is the universe and I am standing in her bright centerpoint."

    $ renpy.music.set_volume(1.0, 1.0, channel='music')
    nvl clear
    nvl hide dissolve
    
    centered "Is this her truth?" with dissolve

    return
    
label en_R29x:

    stop music fadeout 10.0
    scene ev rin_masturbate_hug at Zoom((800, 600), (100, 75, 800, 600), (0, 0, 1000, 750), 40.0, time_warp=acdc_warp) with locationchange
    
    window show dissolve
    "Rin gasps for breath like drowning, returning to reality because she has no other choice."

    "Her entire body is still in the throes of the slowly dying moment."

    "Pearls of sweat are glistening on Rin's forehead as her ecstasy finally lets go."

    "I am feeling my own heat inside of me, but now the spur of the moment is gone and I don't know what to say to Rin who is panting, hot and ecstatic on my arms."

    "Her eyes are wide open, but she looks at me only halfway."

    "She doesn't bother waiting for her breath to even out, squirming to get out of my hold."

    "I release my embrace and she stands up on shaky feet."

    scene bg gallery_atelier_ni at left
    show rin invis at centersitlow
    with locationchange
    
    play sound sfx_rustling
    show rin relaxed_sleepy_pan_close_ni with dissolvecharamoveslowish
    
    "Rin's shirt, wet with sweat is tacked into her back, revealing hints of her shoulderblades and waistline."

    "She takes a tentative step forward, searching for balance, finding it."

    show rin relaxed_sleepy_pan_ni with dissolvecharamoveslowish
    
    "Her legs barely hold her standing. There is no energy in her frame to carry her on."

    #Original line: "Still, as if driven a by a demon, she stumbles towards the couch, where her easel is." (No couch on BG, also grammar mistake) - Kelper

    "Still, as if driven by a demon, she stumbles toward her easel."

    #Original line: "She must've been painting while sitting on the couch, but the canvas is pure white still."(BG has a black canvas) - Kelper

    "She must've been painting while sitting on the couch, but the canvas is pure black still."

    "Then, it is as I suspected. She didn't get her inspiration back so she tried to…"

    "I shudder, standing up myself to see what Rin is going to do."

    "She seems to be reaching out for the empty canvas, even though she doesn't move her short arms at all."

    show rin basic_awayabsent_pan_ni with charachange
    
    rin "I can see it."

    show rin basic_surprised_pan_ni with charachange
    
    rin "I can see it…"
    
    show rin invis at centersitlow with dissolvecharamovefast
    play sound sfx_impact    

    "Rin falls on her knees a step away from the canvas as her feet give in, losing what little strength was in them."

    "I quickly step to her, embracing her again to support her."

    "Rin feels limp, weak, exhausted."

    play sound sfx_rustling
    
    "I reach out for the blanket and wrap it around her and me."

    play music music_twinkle fadein 10.0
    
    "Rin doesn't resist me, she is drained of all strength."

    "Her feverish eyes are glaring hungrily at the canvas, burning with passion, but a different one from the one I saw in her eyes when she looked at me just before."

    "It is different, but I don't know what that means."

    "She closes her eyes and swallows with a loud gulp, trying to relax herself, fighting against the urge to paint."

    "Maybe even Rin realizes that she can't just start painting, not now."

    "She moves her body in my arms, searching for comfortable position in our very uncomfortable position."

    "Her eyelids are drooping dangerously, her strength to keep her eyes open long since gone."

    "I know that look, those mannerisms, that air that surrounds Rin when…"

    "…she is sleeping."

    "She leans against me, closing her eyes and breathes out long one last time before settling into the steady rhythm of sleep."

    "With her last moment of awareness she whispers to me from between her beautiful lips."

    show rin basic_lucid_pan_close_ni at centersit with charaenter
    
    rin "Keep me here."
    
    "Rin drifts deeper into sleep with a deep sigh that releases all remaining tension from her muscles."

    show rin invis at centersitlow with dissolvecharamoveslowish
   
    "I try to shift around to place both of us more comfortably."

    "It takes a while because I don't want to wake up Rin even though she probably wouldn't, but eventually I find a position I am comfortable with."

    show ovl rin_galleryskylight at Zoom((800, 600), (0, 0, 1000, 750), (100, 75, 800, 600), 30.0, bilinear=True) with locationchange 
    
    "I lean against the soft cushions of the couch and breathe in the cool air of the atelier." 

    "Rin's head rests against my chest, as if she was listening to my heartbeats."

    "Echoes of her dream ripple as small twitches on her face, like a cat sleeping the mouse-hunter's dream."

    "The full moon, shining her pale light upon us from beyond the skylight, reflects from the blank canvas standing forgotten on the easel."

    "Its whiteness is glowing against the dark night of the atelier."
    
    window hide dissolve
     
    stop music fadeout 2.5

    scene black with Fade(1.0, 1.0, 0.5)

    return

label en_R30:

    scene black with None
    with Pause(3.5)
    play ambient sfx_rooftop fadein 1.0
    scene bg gallery_atelier with openeye
    window show dissolve
    "I wake up alone."

    show bg gallery_atelier at left with dissolvecharamoveslowish
    
    "Through the grogginess of a freshly awakened mind, I can observe my surroundings only one thing at a time."

    "The morning light shining from the skylight is bright and sky-colored."

    show bg gallery_atelier at right with dissolvecharamoveslowish
    
    "The white walls of the atelier surround me from every side."
    #matched to R24 -SC

    "My neck is stiff and my shoulders are hurting like hell."

    "Why did I fall asleep uncomfortably like that?"

    "I can't even remember when I fell asleep… only the full moon and Rin, warm against me."

    "I can't remember her waking up either, leaving my side."

    show bg gallery_atelier with dissolvecharamoveslowish
    
    "However, she's up already, not far away from me… physically."

    show rin back_cas with charaenter
    
    "As expected, Rin is painting. Her canvas is oddly on the floor, and she is painting while standing on one foot."

    "It looks a bit strange and not entirely comfortable."

    "Rin has that look on her face again, impassive and absentminded, calm but focused."

    "There is only one thing her eyes see now."

    "I watch her working for a while, trying to look past the outer shell of calm into Rin's inner self where her creative process resides."

    "It proves to be impossible, as my x-ray vision is not at its sharpest this morning."

    "I recall her from yesterday. There is nothing of that Rin left."

    "The Rin who had lost her pride and her mind, cowering in shambles on the floor."

    "The Rin in my embrace, her heat against my fingers, her back arching in ecstasy."

    "I recall her desperation, the broken voice of hers pleading me, the fever in her eyes and on her skin."

    "Is she now forming what happened then into a painting?"

    "Is that how her mind works?"

    "The thought weirds me out and excites me simultaneously."

    play sound sfx_rustling
    with Pause(1)
    
    "All kinds of ideas spark into my mind as I stand up from the floor, stretching my stiff muscles, but no amount of flexing gets all stiffness out of my body."

    "Remembering the earphone incident, I refrain from doing anything rash and simply walk to her, sweeping off the dab of blue paint stuck on her cheek."
    # Line before actually said "headphone" instead of "earphone"

    "My gesture only makes the situation worse as the thick paint smears all over her cheek."

    "Luckily, Rin doesn't see that when she turns to look at me, awakened by my touch."

    show rin negative_spaciness_cas with Dissolve(1.0)    
    
    "I make a mental note of her body temperature. It doesn't seem she is sick, at least not anymore."

    "Her lightless, calm stare takes me aback, as there is no emotion I can read from there."

    hi "Umm… good morning. I hope {nw}" 
       
    $ renpy.transition(Dissolve(0.5), layer='master')
    show rin basic_biggerlucid_cas_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.50)
    stop ambient fadeout 1.0
    extend "I didn't..."
    
    #The original line was "hi "Umm… good morning. I hope I didn't..."" which I divided in 2 to accomplish the not-so-worth-it effect of rin jumping at you in the middle of the sentence.
    #I hope people dont mind to much about it - Kelper
    
    play music music_innocence fadein 4.0
    "Rin shakes her head forcefully and then, for no apparent reason (like her actions often tend to happen) she lunges forward, straight into my arms."

    "She presses herself against me, burrowing her face into my shirt despite the fact that my sweaty and crumpled shirt might be a bit unpleasant to burrow one's face into right now."

    "What a clumsy hug hers is, but Rin can't help it."

    "I reciprocate, wrapping my arms around her gaunt shoulders, feeling her bones, brushing her copper-colored hair."

    "The wordless embrace lasts its time, Rin rubbing her face against the rough cotton of my uniform shirt, me holding her."

    "Just holding."

    show rin basic_biggerabsent_cas_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.502) with Dissolve(1.2)
    
    "When she breaks free, I still have no idea what brought this on."
    
    hi "Umm… Rin…"

    show rin negative_biggerconfused_cas_close at Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.50) with Dissolve(1)

    "I pause before getting further, as I stumble with my words and she is not listening."
    
    "I lost my chance, and Rin is not entirely with me anymore, casting yearning glances at her work in progress while trying to maintain eye contact with me at the same time."

    "Maybe she wants to say something, or listen to what I have to say, maybe she wants to paint. Maybe both, or all of them."

    "The conflict makes her look silly, drawing a chuckle out of me."

    "I sigh internally, knowing the futility of trying to discuss with Rin when she is like this."

    show rin basic_absent_cas with Dissolve(1)
    
    "We can talk later. There is time."

    "There is time for us."

    hi "I take it you won't come to school today either?"

    "She has just long enough attention span to answer the only question that pops on my mind, other than, well, everything else that has popped on my mind."

    show rin basic_awayabsent_cas with charachange

    rin "Yeah."

    rin "I'll study over summer vacation."

    hi "Are you sure it's a good idea?"

    show rin basic_absent_cas with charachange
    
    rin "No."

    hi "But you don't have a choice, huh? You have to paint."

    rin "Yes."

    "She answers easily, automatically like it was the most obvious thing in the world."

    "It's great that Rin got this chance, a milestone on the road to become a real artist, but…"

    "She has changed. Now that she has this goal it's like she has become completely obsessed with it, unable to see anything else."

    "The thing that spurs her on, I don't know what it is. But I'm not sure if it's good for her."

    "Yesterday really opened my eyes, in more ways than one."

    "What now? I know Rin wants to paint, and while I'd like to do something completely else, there is her to consider and then there is school too…"

    "I balance between my options for a while, and decide to go with the most rational one."

    hi "Fine, all right. I understand."

    hi "I'll go to school anyway, not all of us have the luxury of being able to skip the exams for our convenience."

    "Besides, I probably would only be in your way if I stayed here, as sad as it sounds."

    "I don't say that aloud though."

    show rin basic_lucid_cas with charachange 
    with Pause(0.5)
    show rin back_cas with Dissolve(1.0)

    "Rin, satisfied with the end of our conversation, nods and turns back to consider her painting."

    "If I wasn't looking and waiting for it, I wouldn't notice the subtle shift in Rin and the air surrounding her."

    "She drifts away, slowly immersing herself into the world of color, canvas and brush."

    "I pick up my stuff and make my way towards the door."

    hi "Bye now."

    "She doesn't answer my quiet words, so locked away she is in her own world."

    "Glancing at Rin's auburn hair one last time, I feel a pang in my heart, a shadow of doubt."

    "It hurts."
    
    stop music fadeout 7.5
    
    "I hope yesterday was not a fluke, not a… I don't know what."
   
    play sound sfx_dooropen
    with Pause(1)
    scene bg gallery_staircase with locationchange
    
    "Walking out of the atelier's door, I'm not so sure anymore."

    #lolskip
    
    window hide dissolve
    scene white with whiteout
    with Pause(1.0)
    
    scene bg school_scienceroom with whiteout    
    play music music_normal fadein 3.0
    
    window show dissolve
    "I make it in time for class, but not for breakfast. Oh well."

    "The classroom is bathing in the gentle light of the sun."

    "In the afternoon, it'll be unbearably hot but for now it's only pleasant."

    "I look at Misha and Shizune's animated discussion about whatever, Hanako staring out of the classroom window, immersed in deep thought."
    "Mutou stumbling into the classroom four minutes late and with no recollection of what was supposed to be today's topic."
    #Last sentence was divided in two cause it didnt fit the text window - Kelper

    "I could never imagine dropping out of school just like that, even if it's only for some weeks."

    "On the other hand, Rin doesn't seem to have much problem with the thought, or going through with it."

    "She's really carefree."

    "Then again, somehow I got caught along to her insane isolation, going to see her whenever I could, even if we ended up hurting each other."

    "Or did we? Maybe only I got hurt."

    "Even so, today too I'll go see her again."

    "I think… I hope she needs it as much as I do."

    #lolskip

    scene bg school_scienceroom_ss with shorttimeskip

    "Late in the afternoon, I realize that today is a Thursday and thus an art club meeting."
    #flagging the start of the timeline problem -SC

    "It's the last club meeting before the summer vacation because of the exams."

    "Without Rin, it feels pretty pointless to go there, but I want to talk with the teacher."

    scene bg school_classroomart_ss with locationskip

    "The meeting itself is not worth mentioning, as my skills with water colors are not worth mentioning."

    "The teacher tries to encourage and advice me without sounding too condescending, but he's not doing a too good job of it."

    "If nothing else, joining the art club has taught me that I like art, except when I myself am not doing it."

    "After the fruits of everyone's labor have been piled into a neat stack on the teacher's desk, he clears his throat to give a little speech."

    show nomiya talk_ss with charaenter

    no "That's it for this trimester, everyone!"

    "His voice is pretty loud and way too enthusiastic for it to be genuine."

    show nomiya smile_ss with charachange

    no "The next meeting is after the summer vacation, on the Thursday of the first week of next term."

    no "I hope to see everyone there again!"

    show nomiya veryhappy_ss with charachange

    no "Have a nice vacation!"

    hide nomiya with charaexit

    stop music fadeout 4.0
    
    "Everyone wishes the teacher a good summer vacation too and start making leave to dinner"

    "I intentionally stay behind, waiting until we are alone in the classroom."

    "The teacher is looking through the paintings, some of which are actually pretty nice."

    "Rin is not the only one with artistic talent in the club, although I guess she is easily outclassing everyone else."

    hi "Excuse me, teacher…"

    play music music_happiness fadein 2.0

    show nomiya smile_ss at center with charaenter

    no "Hmm? What is it, Nakai?"

    "He raises his eyebrows questioningly, smiling widely."

    hi "It's about Rin…"

    show nomiya frown_ss with charachange

    no "Oh? Is something wrong with Tezuka?"

    hi "No, but…"

    "I hesitate for a split second, not certain how to say what I want to say, giving the teacher enough time to start blabbering by himself."

    show nomiya smile_ss with charachange
    
    no "I saw her a few days ago when I was passing by at Sae's gallery."

    no "She said she'd get one or two more paintings done for the exhibition."

    show nomiya talk_ss with charachange
    
    no "I was quite pleased, she is a surprisingly hard worker even though she usually feels so lazy, doing what she wants instead of the assignments…"

    "He seems to notice my anxiety and realizes he is digressing, shutting up before finishing the thought."

    show nomiya smile_ss with charachange
    
    no "Ah, but you had something to talk about. What is it?"

    hi "I don't know… she feels detached from everything, as if she can't think of anything else than the exhibition."
    
    show nomiya frown_ss with charachange
    
    no "Well, isn't that good? She focuses on her painting, as she should do."

    hi "Yeah, but it feels more like an obsession or something… I went to see her too and…"

    show nomiya serious_ss with charachange    
    
    no "Have you been bothering her?"

    "He cuts in before I finish saying what I meant to say, instantly looking quite irritated."

    hi "No… I don't… think so."

    hi "I'm just concerned because she's stopped coming to school completely and she feels strange."

    hi "Stranger than usual, at the very least."

    show nomiya stern_ss with charachange
    
    no "Humbug! This is much more important for her than some lousy physics class."

    no "This is exactly why this school is so flexible, to give every student a chance to fulfill themselves."

    show nomiya serious_ss with charachange
    
    no "Tezuka is a painter, so she should paint, no? And have an exhibition. That's what artists do."

    "His counterarguments are not very convincing, but I'm having a hard time to make any kind of rebuttal."

    hi "Speaking of the exhibition… did you know that she didn't want to take up on the chance to have the art exhibition because of her arms?"

    show nomiya frown_ss with charachange
    
    "My revelation seems to surprise the teacher. I wonder if I should've kept it secret but it can't be helped now."

    "Damn, my mouth moves too fast for my brain when I'm agitated."

    no "Oh that was it? I didn't, but why would Tezuka be like that? She's never struck me as a student who is too conscious of her disability."

    no "Sure, some kids here are like that, especially ones who have only recently… you know."

    show nomiya dreamy_ss with charachange
    
    no "But not her."

    "Nomiya's assertiveness is understandable, as I was surprised too when Rin told me why she initially didn't like the idea."

    "Now that I think about it… what did she explain to me about not wanting people to see her…"

    hi "I think… she fears that people will look at her paintings in a different way when they find out that an armless girl painted them."

    show nomiya talk_ss with charachange
    
    "Nomiya bursts into a completely unexpected laughter, which doesn't manage to remove the tension between us, maybe because it sounds so fake."

    no "That's completely ridiculous! It will only give her more publicity and good name. It's one of the best things about her imago as an artist."

    no "We can play this to her advantage."

    show nomiya smile_ss with charachange
    
    no "Trust me Nakai, I know how these things work."

    hi "But what if she doesn't want to use it?"

    show nomiya stern_ss with charachange
    
    "The teacher makes and ugly face at my argumentative question."

    no "Oh that's just stupid."

    $ renpy.transition(dissolve, layer='master')
    show nomiya serious_ss
    extend " Of course she does."

    #Last sentence didnt start with a space, originally. - Kelper

    no "She knows the realities of being an artist just as well as I do."

    no "Anonymity is not popular. You just can't be faceless and nameless and expect you will do fine in the art world."

    show nomiya smile_ss with charachange
    
    no "You need name, and fame. That's what it's all about. And Tezuka's… condition will give her both."

    no "Of course it'd never work without her talent, but it's something like a plus."

    show nomiya frown_ss with charachange
    
    no "Or do you disagree with my three decades worth of experience in the art world, Mr. Nakai?"

    "My grudging silence is interpreted as a no and Nomiya turns to shuffle the turn-ins of today's assignment."

    show nomiya smile_ss with charachange
    
    no "I have to say, I'm very excited about her exhibition."

    no "At such a young age, and so wonderful skill and style!"

    show nomiya dreamy_ss with charachange

    "He's talking to the air, to relax the mood that got a bit too negative."

    show nomiya talk_ss with charachange

    no "I take it that you will be attending?"

    hi "Yeah, I suppose."

    show nomiya smile_ss with charachange
    
    no "Well, we'll meet there next."

    scene bg school_hallway3_ss with locationchange
    
    "I walk to the hallway, not entirely satisfied with the conclusion of the discussion that was more like argument."

    stop music fadeout 3.5
    
    "My message didn't get through, to say the least."

    window hide dissolve
    
    scene black with Dissolve(1.5)    
    
    return

label en_R31:

    scene black with None
    with Pause(1.5)
    play music music_another fadein 1.0
    scene bg school_gate_ss with fade
    window show dissolve
    "The days seem to be getting warmer at the same rate we are getting closer to the summer vacation."

    "Today too, the warm sunlight hits my eyes when I walk down the steps of the main entrance."

    "It really is summer."

    "I watched the winter slowly turn into spring through the window of the hospital room, but the summer seems to have sneaked up on me."

    "The change of seasons is so subtle. Every day seems to be like the previous, but slowly and surely, the cycle continues."

    "You won't notice it unless you pay attention."

    "One day it's just like “Oh, it really is summer.”"

    scene bg school_road_ss with locationchange
    
    "School is like that, too."

    "Every day is the same. Class, recess, lunch, sometimes exams. It's the same, day to day, year to year."

    "But one day, we will graduate."

    "Then what?"

    "I might have some idea what I'd do, but I don't have a goal like Emi or Rin have."

    scene bg city_busride_ss with locationskip
    $ renpy.music.set_volume(0.4, 0.0, channel='ambient')
    play ambient sfx_businterior fadein 0.5 
    
    "Speaking of her, I wonder what Rin is up to. Still painting, probably."

    "Her subject matter for this new work makes my ears hot, but it's not the only thing in my mind now."

    "I would like to talk with her, to make some things clear, to… I don't know."

    "I still am not sure what I feel or what she feels."

    "I do want to find out, though."

    "The air conditioning in the bus is broken, making the trip resemble the crossing of the Styx."

    scene bg gallery_ext_ss with locationskip
    stop ambient fadeout 0.5
    stop music fadeout 4.0
    
    "I welcome the more fresh air of the downtown as I leisurely walk down to the gallery and the atelier that waits for me at the top floor."
    
    $ renpy.music.set_volume(1.0, 0.0, channel='ambient')
    play ambient sfx_rooftop fadein 1.0
    scene bg gallery_staircase with locationchange
    with Pause(1.0)
    play sound sfx_hammer
    with Pause(1.0)
    
    "I knock and enter before the answer that is probably not coming anyway."

    "Except, the door won't open."

    play sound sfx_hammer
    with Pause(1.0)
    "I try again, but there is no mistake."

    "The door is locked, for the first time ever."

    "Could Rin be out?"

    "Maybe she is at school fetching a change of clothes or whatever, and we've missed each other."

    hi "Rin? Are you in there?"

    "I try to shout through the door to rouse her."

    "The lack of answer doesn't really give any clue, as knowing Rin, she might just {b}choose{/b} not to answer."

    
    play sound sfx_doorknock
    with Pause(1.0)
    "I bang the door loudly a few times, to make sure she is not sleeping or something, before turning to walk back outside."

    "Maybe she ran out of supplies. She could be getting some paints or some such."

    "The gallerist might know."

    rin "Hisao."

    "The voice, suddenly coming from somewhere very close, stops me on my tracks two steps away from the door."

    hi "Rin?"

    "Or maybe she is standing on the other side of the door, after having locked it for some reason."

    hi "Why is the door locked?"

    "I try the handle again to ascertain that she didn't unlock it."

    stop ambient fadeout 2.5
    rin "I locked it."

    "Well, that's obvious, but her motive is the thing I wanted to know."

    hi "Oh. Why? Are you all right?"
    
    "A pause follows, the heavy kind that precede something bad."

    play music music_rain fadein 3.0
    
    rin "I can't see you now."

    rin "I can't see you for a while."

    "The finality in her voice, the tiredness in it, is not one to argue with."

    "She states it like the fact that it is, without explanation."

    "She can't see me now, or for a while."

    "Oh. So that's how it is?"

    hi "You locked the door.. to keep me out?"

    rin "I did."

    "I'm trying not to think the connotations of this revelation."

    "I'm trying really hard to keep my cool."

    "I'm trying and failing."

    hi "How long is this “while” of yours?"

    "I'm grinding my teeth together, the anger flowing in my veins instead of blood."

    rin "I don't know."

    hi "Is it because of the painting?"

    rin "Yes."

    "My neurons are close to boiling point, but all I can do is pretend I am calm and try to make sense of this."

    hi "Why?"

    "No answer."

    hi "Won't you even explain?"

    "No answer."

    hi "Why are you doing this?"

    "No answer."

    "Every question I ask just makes me angrier, every question unanswered makes me feel more hopeless."

    "Only silence is left for me to ask questions from."

    "…"

    "I won't bother with that. I won't bother with this anymore."

    "Just when I thought we could finally solve the problem with not getting anywhere even though we hang around each other constantly."

    "Just when she… damn, she let me do that, she practically begged me for it."

    "This one-sided decree of separation is typical. So typical."

    "Should I have expected this? To get treated like she won't consider my feelings at all?"

    "…"

    hi "Whatever."

    "I turn around and leave her to whatever she wants to do without me."

    stop music fadeout 3.5
    
    #The sentence before started with "extended", for some reason - Kelper
    
    #the following segment might get nuked if I decide to write Sae away (2mny side characters) but I wrote it anyway. Besides, I REALLY dislike this kind of thing where someone needs to give the protagonist a mental roundhouse kick to make things straight.

    scene bg gallery_ext_ss
    with Fade(0.5, 1.0, 1.0)
    $ renpy.music.set_volume(0.20000000000000001, 0.0, channel='ambient')
    play ambient sfx_traffic fadein 1.0
    
    "The gallerist is standing in front of the gallery, attaching a large poster into the window."

    "It's an advertisement of Rin's exhibition."

    "That's right. The opening is not too far off."

    "Funny how I had almost forgotten about the exhibition being something… real."

    "All I have seen are the effects it has on Rin, not the other things that concern the exhibition."

    "The gallerist must have been working hard too."
    
    "As I walk closer, she recognizes me too and after a decisive whack to stick the poster on the glass, turns to reckon me."

    show sae neutral_ss with charaenter
    
    sa "Well well, if it isn't Shinichi's student."

    show sae smile_ss with charachange
    
    sa "You went to see your friend?"

    "She throws a meaningful glance upwards, to the windowless top floor of the building."

    hi "I meant to but she didn't want to see me."

    "I spit out the words, trying to sound as neutral as I can in this adrenaline-filled state of mine."

    show sae scowl_ss with charachange
    
    "She raises her eyebrows more as a polite gesture rather than from surprise."

    "The calm, calculating stare, not unlike Rin's, is compelling me to continue even though she didn't say a word."

    hi "She wanted to work rather than see me, or something like that."

    hi "Did you know that she practically lives up there now?"

    play sound sfx_lighter
    with Pause(0.5)
    show sae scowl_smoke_ss with charachange
    
    sa "Sure. I've let her use my shower whenever she didn't want to go all the way back to your dormitories. My apartment is one floor below the atelier."

    "Her easy acceptance is crushing. First Rin, then the teacher and now this."

    "Am I the only one who is still sane? Is this supposed to be normal?"

    "Is this how it's supposed to be?"

    "Maybe my face tells the gallerist everything she needs to know about my thoughts, maybe not."

    "At any rate, she easily catches the mood and with a sigh, crosses her arms and leans against the windowglass."

    show sae smile_smoke_ss with charachange
    
    sa "I'll tell you a story."

    "I'm not in the mood for stories right now, but I'm not in the mood to care about it if she tells one, either."

    show sae neutral_smoke_ss with charachange
    
    sa "My husband was and is an artist too."

    sa "We were young and foolish, well at least I was… we were studying art at the same school… this was the time I met your teacher too, by the way."

    show sae smile_smoke_ss with charachange
    
    sa "Anyway, I fell madly in love with him, or maybe with his art."

    sa "He was… brilliant, his genius was shining brightly whenever his brush touched a canvas."

    "Her voice is reminiscent, almost revering as she describes her husband."

    show sae neutral_smoke_ss with charachange
    
    sa "He must have frequent and intimate conversations with the muses to produce something so beautiful."

    show sae doubt_ss with charachange
    
    sa "That's what I thought anyway."

    sa "Silly, isn't it?"

    show sae neutral_ss with charachange
    
    sa "But I found out even genius has its cost. Everything, absolutely everything was second to art, be it social life, getting a job or me, it was not important."

    show sae scowl_ss with charachange
    
    sa "That's fine, but he just… could not think of anything else at times."

    "Sounds familiar."

    sa "It seems that artists can't take work as just a job, you know? It's something more… fundamental to them."

    show sae doubt_ss with charachange
    
    sa "It was hard to live with a person like that. Hard to be married to a person like that."

    show sae neutral_ss with charachange
    
    "She takes a pause to see if I understood."

    "I understand, but I don't see what she is trying to say."

    "I guess the point of this story has not emerged yet, or I have missed it."

    "Has she guessed that I like Rin? I suppose it's not too far-fetched, after all I've been coming here pretty often."

    hi "So, how did you cope with it?"

    show sae smile_ss with charachange
    
    "My question, probably the exact one she was waiting for, draws a dry chuckle out of her."

    show sae smile_ss with charachange
    
    sa "I didn't. I divorced from him after one year, two months and fifteen days of our marriage."

    show sae neutral_ss with charachange
    
    sa "It was impossible."

    sa "There was no way for us to get along, no matter how madly I was in love with him."

    show sae doubt_ss with charachange
    
    sa "Eventually I realized that was just how he was, there was no changing him."

    sa "I had to either accept it or move forward."

    show sae scowl_ss with charachange
    
    sa "I made my choice."

    stop ambient fadeout 2.0
    
    sa "The same goes for you."

    play music music_sadness fadein 1.0
    
    sa "If you try to keep this girl from expressing herself, it'll only backfire."

    show sae neutral_ss with charachange
    
    sa "No, let me rephrase. You won't be able to keep her from painting, if she must."

    sa "Either deal with it, or forget about her."

    "She stands up straight again and digs the pocket of her jacket for a cigarette and a lighter."

    "I guess she finished."

    play sound sfx_lighter
    with Pause(0.5)
    show sae neutral_smoke_ss with charachange
    
    "My mouth tastes of bile. I want to swallow the taste away but there is a huge lump right in the middle of my throat."

    "I want to say something to her, to argue, to rebuke."

    "But I have already given up. I think I gave up back on the wrong side of that door already."

    hi "I see."

    hi "I'll be going. Thanks for the story."

    show sae scowl_smoke_ss with charachange
    
    stop music fadeout 3.5
    
    sa "You're welcome."

    window hide dissolve
    
    scene black with Dissolve(1.5)
    $ renpy.music.set_volume(1.0 , 0.0, channel='ambient')
    return

label en_R32:

    scene black with None
    with Pause(1.5)
    play music music_night
    with Pause(0.2)
    scene bg school_scienceroom with fade
    
    window show dissolve
    
    "The day after that, I'm brooding. There is nothing much to be said about that, except the strong impulse to hit myself with a blunt object in the forehead, an impulse I never give in to."

    scene bg school_scienceroom with shorttimeskip
    
    "Second day. Anxiety seeps in. I start doubting my doubt and if feels stupid, especially since I still can't think about anything else than Rin."

    scene bg school_scienceroom with shorttimeskip
    
    "Third day. Japanese exam {b}and{/b} world history exam. Great. The thing I hate most about her is that she can make me feel this awful even though I should be focusing on entirely different stuff right now."

    scene bg school_scienceroom with shorttimeskip
    
    "Fourth day. We have a math exam. It goes how it goes. I don't care."
    
    scene bg school_scienceroom with shorttimeskip

    "Fifth day. Nomiya asks me again if I will attend the exhibition opening. I can't say no to him even though I seriously want to. I just don't want to discuss with him anything Rin-related so it's better just to take the path of least resistance."

    stop music fadeout 2.0
    scene bg school_dormhallway
    show rin basic_absent at center
    with shorttimeskip
    
    "Sixth day, the day before the exhibition opening, Rin is standing in the hallway in front of my room when I return to the dorms after dinner."

    play music music_rain fadein 6.0 
    
    hi "What are you doing here?"

    "My tone is angrier than I intended, but it's just as well. I'm a little disappointed that I seem to be unable to restrain myself, but it seems it can't be helped."

    "Also, what really pisses me off is how coolly Rin just stands there, like she just happened to coincidentally hang around here where she has no business to be."

    "This is not good, I'm already this irate even though it's been six days and she hasn't even opened her mouth yet."

    show rin basic_deadpan with charachange

    rin "Finished painting."

    hi "Shouldn't you be at the gallery, to prepare for the exhibition?"

    show rin basic_awayabsent with charachange

    rin "They said no."

    "I guess the gallerist does that part then, getting the paintings framed and on the walls and whatnot."

    hi "So, why here?"

    show rin basic_deadpannormal with charachange

    rin "Felt like it."

    "This same old stupid pattern emerges again, me asking her questions to which she replies with answers that don't answer anything because it's the only other way we can converse apart from me listening to her blabbering about whatever which isn't "
    "...really a conversation."

    #Previous sentence splitted in 2 for having the nasty habit of not fitting the text window - Kelper

    "Is this a play? Are there some unseen roles that we have unknowingly set ourselves into, dictating the rules of engagement whenever we see each other, inevitably leading to us hurting each other?"

    "Her nonchalant answers accompanied by even more nonchalant shrugs leave me none the wiser. I guess I should be happy that the exhibition preparations are complete."

    play sound sfx_dooropen

    scene bg school_dormhisao with locationchange
    show rin invis with None
    
    "I open my door and walk in with her in tow."

    "I didn't invite her in nor did I tell her to stay out. I'm too apathetic to care."

    show rin basic_awayabsent at centersit with Dissolvemove(0.5)
    show rin basic_absent with Dissolvemove(0.3)
    
    stop music fadeout 6.0
    
    "She claims my bed without asking permission, making me wish that I had taken the time to make the bed before I left in the morning, then stands up again like she was sitting on hot coals."

    "I half-lean against the single corner of my desktop that isn't cluttered with stuff to rest my legs at least a little bit."

    show rin basic_awayabsent with charachange

    "Rin spends a few moments glancing curiously around my room, which makes me remember she has never seen it before."

    show rin basic_absent with charachange

    "As the room is small, she runs quickly out of things to look at, but nothing else transpires, allowing the uncomfortable silence take over the atmosphere of the small room."

    "The mood is chilly to say the least, and both of us are on guard, waiting for the other to play first."

    hi "So…"

    "I give up because she never would and try to open conversation because it seems that she wants to say something and I want to get over with it."

    "Why else would she be here if she didn't want to talk?"

    "I don't know what to say myself. I wanted to be angry, I am angry, but I can't bring myself to yell at her or anything."

    "Despite this apathy, my voice catches her attention and she tries to search for the words as well, but it seems that she is not entirely certain as to why she's here either."

    show rin basic_absent_close with dissolvecharamove
    
    "And so, Rin simply takes a few steps to close the distance between us and rises on the tips of her toes to even out the height difference…"

    window hide dissolve

    show rin basic_lucid_superclose at center with charachange
    
    centered "“It's impossible.”"

    centered "“There was no way for us to get along.”"

    window show dissolve
    
    "It's a reflex and almost as an afterthought, the words “no,” “yes” and “maybe” surface into my mind simultaneously."

    "My hand is between her lips and mine, a wall that I raised to guard against… something."

    show rin basic_surprised_close with charachange
    play music music_moonlight fadein 0.5
        
    "Her breath feels warm against my fingers. The scent of her skin lingers about, the mysterious indescribable sensation that captures me and draws my eyes deep into hers."

    "The look in her eyes is surprised, quizzical as to why the impertinent hand prevented her advances."

    "Her eyes are really big and glistening with moisture, and staring right into my own with a soft gaze that I'm having a hard time to match."

    "Rin's half-open mouth makes her look even more confused, although the sensual way her lips are arching is signaling something completely else."

    show rin basic_upset_close with charachange
    
    rin "Please."

    show rin negative_angry_close with charachange

    rin "I need you."

    "The words come from her throat as a coarse whisper meant only for me, bypassing her tongue and teeth without giving them any chance to interrupt."

    show rin negative_angry with Dissolve(0.15)
    with vpunch

    "They sober me in an instant, and I clumsily flinch back to get a little bit of distance between us, painfully bumping against my desk in the process."

    "Maybe it's her choice of words, maybe the way she says it, but something in it puts me off."

    "Something is wrong, something is terribly wrong again."

    hi "Need me for what?"

    "All the unpleasant feelings emerge again and I feel my heartbeat suddenly increasing at least tenfold."

    "Talk about mood-shattering, but it was actually her who tried to break my original bad mood, or something like that."

    "Rin's eyes go out of focus and back again as her body relaxes from its tensed state and she stands upright again."

    show rin basic_deadpanupset with charachange

    rin "I don't think I was thinking about anything. Why do you draw patterns in that dust on your night table?"

    show rin basic_awayabsent with charachange

    rin "There is a word for that kind of thing but I can't remember…"

    "Her remark almost throws me off track and I glance over her shoulder at the small table next to my bed but I can't see anything from this distance."

    "So she needs me for nothing specific?"

    "Just, happened to came by because she thought I'd be glad to see her after she shut me out, no complaints accepted, for a week."

    "Completely altruistic motives?"

    "Felt like it?"

    hi "Bullshit. I can answer myself."

    hi "To play mind games with whenever you want, to kiss whenever you want, to ignore whenever you want, to fulfill your whims whenever you want?"

    hi "Is that it? What you need me for?"

    "I'm sounding very angry again, even to myself."

    extend " Good."

    show rin basic_absent with charachange

    "Rin too finally catches the mood and her curious expression changes instantly to something more uncharacteristic."

    rin "No—" #reminder for the potential {nw} break

    "She leaves it to that, her eyes restlessly wandering around, searching the room as if the words she tries to find were written in the tapestries of my walls."

    hi "Then what?"

    show rin negative_confused with charachange
    stop music fadeout 2.0
    
    rin "I needed to paint so—" #reminder for the potential {nw} break

    "Paint."

    "My vision is filtering through the blood-red lens of unbridled anger."

    play music music_tragic fadein 2.0

    hi "Don't give me that, Rin! I am not some fucking muse of yours, free to be abused for the sake of painting!"

    hi "I am not some medium for whatever you aspire to, I am me!"

    hi "So what if I don't know anything about my future?"

    hi "I care for things too, I want some things too! Even I can dream of other things than nightmares!"

    "I am yelling already but I'm way past the point of caring about things like that."

    show rin negative_sad with charachange

    "Rin looks down at her toes and wiggles them a little melancholically while she takes in my outburst without saying anything to defend herself."

    "Only after I have finished she tries to respond somehow."

    show rin basic_sad with charachange

    rin "I can't do anything else. Or I can do all sorts of things, but I… can't…do."

    show rin basic_upset with charachange

    rin "It's everything. It's the only thing."

    "Yeah, that much I've figured out by myself, thanks. Art first, everything else second, or thousandth."

    hi "What about me? Am I nothing? Mildly interesting because I am mildly interested about art?"

    hi "Ever paused to consider things from perspective other than yours?"

    show rin basic_surprised with charachange
    
    "I snarl the words from between my teeth, they taste like poison anyway."

    "Rin is positively alarmed by now. So at least she not completely dense, but it seems that she just doesn't understand what I'm angry about."

    "I can't believe even she could be so stupid."

    show rin negative_sad with charachange
    
    rin "I didn't want to—" #reminder for the potential {nw} break

    "This time it's Rin herself who interrupts her in midsentence."

    show rin basic_upset with charachange

    rin "Don't you understand? I can't."

    hi "Can't what?"

    hi "You never explain yourself! How am I supposed to understand anything if you never say anything?"

    hi "Why don't you ever talk?"

    hi "Say something!"

    "Venting my anger at her feels satisfying and being satisfied about it feels terrible but I am not going to stop myself now."

    show rin negative_annoyed with charachange

    "Not wanting to face my anger toe to toe, Rin turns around to steadfastly look out of my window even though there is nothing to look at."

    "The worst of my ire gone, I shut up as I can't be bothered to keep on yelling at the back of her head, so the silence finally returns."

    "Through my adrenaline-distorted vision I try to discern some hints of her reaction."

    "My output was not the best kind but I hope Rin got the clue that she just can't ignore everything else whenever she feels like it."

    "I'd hate it if she didn't. She never ever listens to anything, she's so unaffected by the world around her."

    "Not this time, it seems."

    "Her body is shaking like from held-back tears, but I already know that Rin is not crying."

    "Still, did I go too far?"

    hi "Look, I—{w=0.3}{nw}" #reminder for the potential {nw} break

    show rin negative_angry with charachange
    
    rin "Go away."

    rin "Go away Hisao."

    "Her voice is tiny and tired as she says this, but I hear the words clear as day."

    "…"

    "What is there to say anymore?"

    hi "This is my room."

    "The blunt, hollow remark is a fitting coda for this unpleasant discussion that became an even more unpleasant and very one-sided yelling match."

    show rin basic_lucid with charachange

    "After a moment of collecting herself Rin just gives up, I can see it from the way she slumps her shoulders, and walks out."

    hide rin with charaexit

    "Even though she deliberately looks to the other direction, I can see how she's biting the corner of her lip so hard it might start bleeding if she won't stop."

    "As she makes her exit I realize that she left the door open when she came in and my yelling must've echoed round the dorm hallways."

    "Sigh."

    "After she is gone, I am left alone in the room with my guilt."

    "As the thumping in my chest slowly subdues, the anxiety gains room."

    "Somehow, I feel that none of this would've ever happened if not for me."

    "No matter how infuriating, unbearable and outrageous Rin is, she is not the Rin I thought I knew."

    "Or maybe I only thought I knew her, or maybe I knew the Rin that she isn't, or…"

    "…"

    "Was it me who caused all this by talking Rin into taking her chances with the exhibition?"

    "Am I directly responsible for Rin becoming like she has been for the past weeks?"

    "I can't think of any other explanation for her weird behavior than the exhibition and all the things that came along with it."

    "Maybe it was the only way that could've brought us closer but all it did was separate us further away from each other and now, beyond the reach of either of us."

    play sound sfx_impact2 
    with vpunch

    "As there are no fitting blunt objects nearby, I bang my head hard against the wall."

    play sound sfx_impact2
    with vpunch

    stop music fadeout 6.0
   
    "Twice, to make sure it hurts for real."

    window hide dissolve
    scene black with Dissolve(3.0)
    
    #Act 3, "Distance", end.

    return