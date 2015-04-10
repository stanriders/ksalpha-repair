label en_H24:

    # # # # #
    # I hope KS-alpha translation groups (if they exist) will use this project.
    # Every line of code added by me is tagged with "# [str]", just in case.
    # # # # #
    
    # # # # #
    #Act IV Title: Mors Mortis (Lol latin for cause of death)
    #probably a place holder. I suck at titles.

    #Starts white

    scene white # [str]
    with None # [str]

    "Blinding light wakes me from my reverie."

    "I won't lie; my chest hurts like a bitch."

    "On the upside, the rain seems to have stopped."

    "Groaning, I try to move."

    mystery "Easy there, you really shouldn't move…"

    #fade from white
    scene bg hosp_room2 # [str]
    with Dissolve (1.5) # [str]

    play music music_rain fadein 4.0 # [str]

    "The blinding light fades away as the doctor moves his torch away from my eyes."

    "Doctor" "Pupil function normal. Tell me son, what's you're name?"

    "I see, I'm in a hospital."

    "Even the simple act of breathing is an exercise in pain."

    hi "My… my chest hurts."

    "Doctor" "That's a strange name."

    "Doctor" "Still, I can understand the confusion."

    hi "Nakai… Hisao… Nakai…"

    "I wheeze out every word in individual breaths"

    "It feels like there's a tonne of lead on my chest."

    "Doctor" "Bingo. Looks like you're coming back to normal."

    "Doctor" "I realise you'll have a lot of questions, but for now, try to rest."

    "Doctor" "Your chest will take some time to heal I would think."

    hi "W…wha…"

    "The doctor squeezes my shoulders gently."

    "Doctor" "I'll explain everything in time."

    "Doctor" "But for now, you're still feeling the effects of the anaesthetic."

    "Doctor" "Nurse, could you take Hisao here to the ward? I think he'll be fine for the moment."

    "I try to protest, but the doctor is right."

    "I relax back into the hospital pillow as my bed is wheeled from the emergency room to a private ward room."

    "Nurse" "Just relax, you have some visitors."

    "Nurse" "I'll send them in now."

    "I try to turn my head to face the door, but the pain is unbearable."

    "Two sets of footsteps approach, punctuated by the distinct “click, click” of Lilly's cane."

    show lilly cane_sad_cas at twoleft # [str]
    with charaenter # [str]

    li "Hisao?"

    "The footsteps break into a trot, and I hear the cane clatter to the floor."

    show lilly cane_surprised_cas at twoleft # [str]
    with charachange # [str]

    "Lilly's face appears in my vision, her sightless eyes desperately searching out in vain."

    "The torment on her face is obvious, and I try to move my hand to clasp hers."

    "But it's hopeless; I can barely breathe, let alone move my hands."

    hi "L… Lilly… w… where's Hana… Hanako."

    show lilly cane_sad_cas at twoleft # [str]
    with charachange # [str]

    "A second face appears in my vision…"

    show yuuko worried_up at tworight # [str]
    with charaenter # [str]

    hi "Yuu…ko?"

    "Doctor" "Girls, I appreciate your concern, and I think Hisao does too."

    "Doctor" "But I think we should have a little talk."

    "Doctor" "Hisao, your parents are on their way here now, they'll be here by morning."

    hi "Wh… what's going on?"

    hi "Where… is Hanako."

    "Doctor" "Ah. Well, I should start from the beginning then."

    "Doctor" "Girls, you're welcome to stay, if you'd wish."

    "The doctor toggles the controls on my bed, raising its back so that I can see the room."

    "Yuuko guides Lilly into a chair, and then sits next to her."

    "The doctor closes the door to the room, and takes a deep breath."

    "Doctor" "Hisao, you had another heart attack."

    hi "F…figures."

    "Doctor" "Thankfully, your friend… well… for want of a better word, she saved you."

    "Doctor" "At least, she kept you alive until the ambulance arrived."

    "Doctor" "Though, I can't say much for her methods. She seems to have broken most of your ribs."

    "The vision of Hanako bringing down her fists onto my chest flashes in my memory."

    hi "So… where is she."

    "Doctor" "That… isn't so simple."

    "Doctor" "Your friend Hanako… well, like you, she had a relapse."

    "Doctor" "She's currently in the Oiwa ward."

    show lilly cane_oops_cas at twoleft # [str]
    with charachange # [str]

    li "Oiwa ward? What's that?"

    "Thank you Lilly… I don't think I can talk much more like this…"

    "However, the look on the doctor's face doesn't fill me with confidence."

    "Doctor" "The Oiwa ward is our mental health facility."

    hi "Mental Health?"

    "I ignore the raging pain in my chest."

    hi "Relapse… wha…"

    "I can take no more. I sink back into the bed."

    "Doctor" "Easy now. I'll explain the rest for later, but for now, you need your rest."

    "Doctor" "Once your parents get here, we have to discuss your future."

    "Doctor" "Girls… I'm going to have to ask you to leave now."

    show lilly cane_displeased_cas at twoleft # [str]
    with charachange # [str]

    li "Hisao… we'll be back."

    hi "Lilly… check… check on Hanako."

    show lilly cane_smile_cas at twoleft # [str]
    with charachange # [str]

    li "I will, Hisao. Please, rest. We'll come back tomorrow."

    hide lilly # [str]
    with charaexit # [str]
    hide yuuko # [str]
    with charaexit # [str]

    "The doctor ushers out the girls, then returns my bed to a horizontal position."

    "Doctor" "Here, this will help with the pain."

    "The doctor injects something into the drip bag hanging next to my bed, and instantly I feel the pain start to drift away."

    "Doctor" "We'll speak in the morning."

    scene black # [str]
    with Dissolve(2.0) # [str]

    "I have so many questions, but the drugs slowly flooding my system gently force my eyes closed."

    "Velvet sleep lines my eyelids, and I drift away from consciousness."

    stop music fadeout 1.0 # [str]

    window hide # [str]
    with Pause(2.0) # [str]

    #Fade through black
    #shorttimeskip # [str]

    mystery "Hisao? Hisao?"

    scene bg hosp_room2 # [str]
    with openeye #fade # [str]
    play music music_rain fadein 4.0 # [str]

    "I gently return to the land of the living."

    "My parents and the doctor fill my vision."

    hi "Mom? Dad?"

    "Dad" "We came as soon as we heard."

    "Dad" "How are you feeling?"

    "The latent painkillers allow me to speak a little easier."

    hi "Like… like shit."

    "A faint, non-convincing smile creeps across his face."

    "Dad" "Good… good."

    "Doctor" "I'm sorry to interrupt, but we should really discuss the problem."

    "Doctor" "Hisao, are you alright to talk?"

    hi "Yeah… a little."

    "Doctor" "Okay. Now, did you notice anything strange before your last attack?"

    "In short, rasping sentences, I explain the last week's events."

    "Hanako's break down, the strange events of the end of the week, and the final incident in the Shanghai."

    "For a time, the doctor doesn't respond, but reads through the notes attached to his clipboard."

    "He reaches the end, thinks for a moment, then starts again from the beginning."

    "Without warning, he places the clipboard on a table."

    "Doctor" "You say that you were having trouble keeping track of time?"

    hi "Yes, I think."

    "Doctor" "You were pretty confused, right?"

    hi "Yeah."

    "Doctor" "At any time in the past couple of weeks, did you miss your meds and try to make up for lost time? Or did you take any other medication?"

    hi "Not that I can remember…"

    "Another pause."

    "Doctor" "I don't think that medication will work for you, Hisao."

    hi "I'm sorry?"

    "The doctor sighs, and rubs the bridge of his nose."

    "My mother, sitting in one of the visitors' chairs, starts to sob a little."

    "Doctor" "People your age occasionally have some strange reactions to these medications, but we thought we had managed to get lucky in your case."

    "Doctor" "A lot of the time, it's simply nightmares, or a bit of insomnia."

    "Doctor" "But it seems that, in your case, it's much worse."

    "Doctor" "Unchecked, you could… well… you could lose your mind."

    "I see my father wrap his arm around my mother and pull her towards him."

    "“Ah” I think."

    "“That's where I get that from…”"

    "Doctor" "What I'm going to suggest may seem a little extreme, but, at the very least, it won't have these side effects."

    "Dad" "Anything… we'll try anything."

    "I want to pitch in my support, but great waves of fatigue crash down upon my mind."

    "As a sign of my consent, I simply wave my lips and nod my head."

    "The doctor correctly interprets my motions, takes a deep, mournful breath, and speaks."

    "Doctor" "I want to install a pacemaker."

    "Dad" "A pacemaker? Don't they only install them in geriatrics?"

    "Doctor" "Normally, yes. However, with your son's reaction to the standard medication, I think it's worth the risk."

    "Doctor" "I'll leave you to think about it, Hisao. But I'd like to show your parents some more information, if that's alright with you…"

    "Summoning my strength, I manage to ask one last question."

    hi "How's Hanako."

    "The doctor's concerned face tells me all I need to know."

    "Doctor" "She's safe. I'll come back to visit you shortly."

    "There's something about the term “She's safe” that seems so contradictory."

    hi "Can I see her?"

    "Doctor" "Not… just yet. Neither of you are in a state that would allow that, I'm afraid."

    "Without saying more, he shuffles into the corridor and closes the door behind him."

    "Through the thin door, I hear his voice fade away as he begins explain the pacemaker to my parents."

    "No sooner have I relaxed back in the pillow there is a gentle knock at the door."

    hi "Come in."

    "There is the sound of fumbling, but eventually the door opens."

    play sound sfx_dooropen # [str]
    
    show lilly cane_weaksmile_cas at tworight # [str]
    with charaenter # [str]

    "Out of the corner of my eye I catch Lilly's golden hair appearing in the doorway."

    hi "You came back."

    show lilly cane_smile_cas at twoleft # [str]
    with charamove_slow # [str]

    li "Of course; we are friends."

    "There's something about the way she says this that fills me with hope."

    "When I was in hospital last time, it almost felt as though my classmates visited solely out of obligation."

    "Lilly, on the other hand, seems like she would visit daily until the end of time."

    li "Some of the other people from the school wanted to come and see you, but the nurse won't let anyone just yet."

    li "But I can assure you that everyone wishes you well."

    hi "Thanks…"

    "Something about me doesn't doubt that."

    "There's a strange camaraderie at Yamaku, probably because everyone there has spent a fair amount of time exactly where I am now."

    "It's a lot easier to appreciate a situation like this if you've been in it before."

    "But, for now, only one question is on my mind."

    hi "How's Hanako?"

    #Lilly concerned.

    show lilly cane_sad_cas at twoleft # [str]
    with charachange # [str]

    li "I… I can't tell."

    hi "What?"

    li "Please, Hisao, be calm."

    li "The doctors won't let anyone see her just yet, and they won't tell me what's going on."

    li "They just say that she's not allowed to see anyone until she “calms down.”"

    hi "What's that supposed to mean?"

    show lilly cane_reminisce_cas at twoleft # [str]
    with charachange # [str]

    li "I… I'm not sure."

    "…"

    li "Hisao… just how much do you know about Hanako?"

    hi "Well, the fire, her being orphaned, and that she's here… why?"

    #Lilly pout

    show lilly cane_pout_cas at twoleft # [str] (seems unappropriate!!!) 
    with charachange # [str]

    li "That's all I know too, but I believe that we are missing something."

    hi "Why's that?"

    li "Hanako's accident happened when she was a child, yes?"

    hi "That's what I've been told…"

    show lilly cane_sleepy_cas at twoleft # [str] (seems unappropriate!!!) 
    with charachange # [str]

    li "Then why is it that she only joined this school in the junior year of high school?"

    #I'm not sure what the correct term for that is, but here it would be equivalent to year 10.

    "Memories flash behind my drug-addled eyes."

    "The nurse said something similar, didn't he?"

    "That Hanako and I were alike; we fell ill as adolescents."

    "And the doctor here… a relapse? Relapse of what?"

    "Concentration and concern tighten my chest, causing unbearable pain, and I groan involuntarily."

    li "Hisao? Are you alright? Should I call for a nurse?"

    hi "N… no, I'm fine. But I need to think…"

    show lilly cane_weaksmile_cas at twoleft # [str]
    with charachange # [str]

    li "I understand. I'll see if I can find out more."

    hi "Please…"

    hide lilly # [str]
    with charaexit # [str]

    "Lilly departs with her standard “Click Click,” and again, I am alone."
    
    window hide # [str]
    
    return

label en_H25:

    with Pause(0.1) # [str] (that somehow fixes game crash)
    scene bg hosp_room2 # [str]
    with shorttimeskip # [str]

    window show # [str]
    
    "It feels like hours before my parents return from their conference with the doctor."

    "Their ashen faces don't bode well for me."

    "Dad" "Hisao… son… We think that the pacemaker is the right choice."

    hi "Oh… but… then what's the matter?"

    "Doctor" "There's very few pacemakers that are designed for people your age."

    "Doctor" "You've still got a bit of growth left in you, and a fairly long life to look forward to."

    "Doctor" "As a result, you would always have to be within reach of a well-equipped hospital."

    "Doctor" "Of course, you would have to have constant check ups, but I think that, eventually, you'll lead a fulfilling life."

    "Call me sceptical, but his repetition of “life” is worrying."

    hi "So, when do we do this then?"

    "The doctor grimaces."

    "Doctor" "Normally, I'd schedule the procedure immediately, but I'm concerned about the damage to your chest."

    "Doctor" "Ignoring the broken bones, there's a lot of damaged and inflamed tissue in your chest cavity."

    "Doctor" "I'm afraid that surgery, at this point, would only put you at further risk."

    "Doctor" "The procedure to install the pacemaker involves heavy chest reconstruction as is."

    "Doctor" "We can re-set your ribs then, but we need to wait for the swelling to go down at the very least."

    hi "I see…"

    "As if to confirm his diagnosis, I look down upon my chest for the first time since the incident."

    "He's right; I look I volunteered to be a punching bag; dark, green-edged bruises mottle my skin."

    "The normal, smoothly-curved shape of my chest is jarred with swollen lumps and sunken areas where my ribs are still being set."

    hi "So… what happens now?"

    "Doctor" "We'll have to keep you here, under surveillance, until it's safe to operate."

    "Doctor" "After that, it'll probably be another week whilst we monitor the pacemaker's functions, then after that you'll be free to go."

    hi "And… how long will that be?"

    "Once again, the doctor's face falls."

    "Doctor" "That… could be some time. Possibly a month before we can operate."

    "Doctor" "Since we're still not sure which of your medications you reacted to, we'll use that time to run some tests."

    "Doctor" "In the meantime, I've let your school know that you're alright, and that you can accept visitors, if you wish."

    hi "Thanks."

    "I spy my parents, helpless and mourning, and for some reason, it makes me uncomfortable."

    "As much as I care for my family, I can't help myself but ask my next question."

    hi "What's wrong with Hanako?"

    "The doctor pauses for a moment, and my parents look at me quizzically."

    "I can see it in their faces; “Why is he asking about this girl?.”"

    "But I don't care what they think anymore. If I can't do anything for myself, then maybe I can do something for her."

    "Simply lying here, not knowing how she is doing, is worse than any other pain I've felt to date."

    "Doctor" "I'm not really the best person to speak to you about that, however I will send in someone shortly."

    "Dad" "Hanako… that's the girl that saved you, right?"

    "It would appear that they haven't been told the whole story, but that's alright."

    "Explaining everything would take far too long."

    "And I don't want to see how they react to me having a girlfriend just yet, either."

    hi "Yes, that's right."

    "Dad" "Well, then, the least we could do is pay her a visit for you."

    "Doctor" "I'm afraid that's not quite possible. Her doctor has forbidden anyone to see her, at least not for the moment."

    "Dad" "That's preposterous! We can't thank the person who saved our son?"

    "Doctor" "I'm afraid that's the case. I'm sorry, but I'm going to have to leave now. I'll call you when I have more information."

    "The doctor walks out, and my parents take place by my bedside."

    "Mom" "Hisao… are you going to be alright?"

    hi "I think so; but I guess I won't be able to tell until after the operation."

    hi "What about you guys? Where are you staying? What about your work?"

    "Dad" "We're staying at a hotel a few blocks from here."

    "Dad" "And we've both taken leave from work."

    hi "You don't need to stay here on my account."

    hi "You heard the doctor, he won't be able to operate for about a month."

    hi "I can't ask you to stay here that long…"

    "Mom" "But… "

    "Dad" "He's right, dear. We can't afford to stay here for that long."

    "Dad" "Would you be able to manage by yourself?"

    hi "I've been okay so far… well… mostly okay…"

    hi "And besides, my friends for school here are… different."

    hi "It's like they understand, 'cause most of them have been in this situation themselves."

    hi "I can't ask you to risk your jobs on my account…"

    "My father seems to agree with this, but my mother is less convinced."

    "Mom" "But Hisao! We can't just leave you here!"

    "Dad tries to comfort her."

    "Dad" "Hisao's right. We can't stay here forever."

    "Dad" "This is the safest place in the world for him."

    "Dad" "And we can come back for the surgery, okay?"

    "My mother, on the verge of tears, nods an nearly imperceptible nod."

    "Mom" "Okay…"

    hi "Thanks for coming up… It means a lot… really."

    hi "I'm sorry for troubling you."

    "My father ushers my mother out of the room."

    "Dad" "We'll see you soon, 'kay?"

    hi "'kay."

    "For some strange reason, I'm relieved that they are gone."

    "Everything that's happened in the past couple of months, all the people that I've met…"

    "I feel like I can no longer understand the world they are in, just as they can't understand my world."

    "But…"

    "At least they care."

    "I suppose that's enough."

    "Once again, my thoughts turn to Hanako."

    "She would have had to go through her troubles alone."

    "I can't even imagine how that would have been."

    "…"

    play sound sfx_doorknock2 # [str]
    
    "A firm knock on the door startles me."

    hi "Come in?"

    play sound sfx_dooropen # [str]
    
    "Doctor 2" "Hisao? I'm Hanako's doctor; do you mind if we have a little talk?"

    hi "Hanako? How is she? What's the matter with her?"

    hi "When can I see her?"

    play sound sfx_lock # [str]
    
    "The doctor comes into my room slowly, and locks the door behind him."

    "He looks a good deal older than my doctor, but has a much gentler demeanour."

    "Just by looking at me, he makes me feel a little more comfortable."

    "Before talking, he toggles the controls on my bed until I am almost sitting upright."

    "He then moves one of the chairs so that we are looking eye-to-eye, and sits down."

    "Doctor 2" "Now there, I know this will be hard, but I'll have to ask you to keep your questions for a moment."

    "Doctor 2" "This… may not be all that easy on you."

    "Doctor 2" "Truth be told, I shouldn't even be telling you this, what with confidentiality."

    "Doctor 2" "But I know that that two of you are close, and your doctor said that it might help you relax a little."

    "Doctor 2" "And, due to your condition, I'd like you to stay calm."

    "Doctor 2" "Can you do that for me?"

    "Fighting against my broken ribs, I take a deep breath."

    hi "Yes. Sorry."

    stop music fadeout 4.0 # [str]

    "Doctor 2" "Tell me… what do you know of Hanako's condition?"

    hi "Well, she was in a fire when she was younger, and got pretty scarred."

    hi "And that made her self conscious, I guess."

    "Doctor 2" "And that's all?"

    hi "That's all I know…"

    #Oh dears, monologue GET.
    #I don't know how else to tackle this, so I'm open to suggestions.
    #as it stands, I think the best thing would be to overlay the following
    #over 4-5 CGs, if that's not too much of an ask.

    play music music_moonlight fadein 3.0 # [str]

    "Doctor 2" "That's all she's ever told you?"

    hi "That's all she's ever told anyone as far as I can tell…"

    hi "But I heard something about a relapse, and our nurse said something about her problem starting in adolescence or something…"

    "Doctor 2" "Relax… I'll get to all of that in time."

    "Doctor 2" "So, you know Hanako's accident happened at an early age."

    "Doctor 2" "In fact, she was still in her second year of elementary school."

    "Doctor 2" "Once she got out of hospital, she returned to her old school, albeit under the care of a foster family."

    "Doctor 2" "At the time, we decided that the more “normal” we could keep her life, the better it would be for her."
    
    "Doctor 2" "She seemed to think that the fire was somewhat her fault, so the sooner we could get her back in a daily routine, the better."

    hi "Wait… you were there?"

    "Doctor 2" "Pardon? Oh, yes."

    "Doctor 2" "I've been caring for Hanako ever since then."

    "The doctor rubs his eyes a little, as if rubbing away some distant memory."

    "Doctor 2" "As I was saying, Hanako returned to her elementary school, and things seemed to be going fine."

    "Doctor 2" "For some reason, young children can be fairly accommodating, even with someone as scarred as her."

    "Doctor 2" "And, as I'm sure you've noticed, she's managed to conceal the worst of them."

    "Doctor 2" "For a time, she didn't show any of the usual symptoms of someone who had been through such a traumatic experience."

    "Doctor 2" "But, things changed when she entered middle school."

    "Doctor 2" "Teenagers aren't so forgiving, especially when struggling to find a new pecking order, like in a new school."

    "Doctor 2" "It wasn't long before Hanako was victimised and bullied into her shell, which is probably the Hanako you know."

    "Doctor 2" "But, she is strong. Incredibly so."

    "Doctor 2" "She managed to simply contain it within herself; and survive alone."

    "Doctor 2" "Of course, at this point, none of us realised anything was wrong."

    "Doctor 2" "She had survived elementary school unscathed, and never spoke of any of this in our sessions, so we assumed it was just smooth sailing."

    "Doctor 2" "But, near the end of middle school…"

    "Doctor 2" "… there was an incident."

    "Doctor 2" "We don't know if it was meant to be a prank, or if it were sincere, but a boy called Hanako out, to confess to her."

    "Doctor 2" "What actually happened, we don't know."

    "Doctor 2" "All we know is that, for some reason, Hanako ran away, and the boy chased her."

    "Doctor 2" "However, in the chase, the boy was hit by a car…"

    "Doctor 2" "…and killed, instantly."

    "Doctor 2" "Hanako saw the whole thing, and it sent her over the edge."

    "Doctor 2" "Nearly eight years of trauma, of bad memories, taunts, stares, isolation…"

    "Doctor 2" "Hanako cracked."

    "Doctor 2" "Like most mental disorders, it's hard to give her condition an exact name."

    "Doctor 2" "So, after a few months in a mental ward, we were able to establish a regime of medications that would keep her calm."

    "Doctor 2" "There were some minor side effects, but for the most part, she seemed to be able to cope on her own."

    "Doctor 2" "She was able to make a friend, who she managed to confide in, and I think that helped a lot."

    "Doctor 2" "And, I think you helped her a lot too… she even mentioned you in our last session before this incident."

    "Doctor 2" "But, in a way, you re-opened old wounds that had never quite healed."

    "Doctor 2" "But, perhaps this is for the best."

    "Doctor 2" "She's been holding so much inside her tiny mind for so long… in some ways, she's never grown past 6-years-old."

    "Doctor 2" "For now, we'll just have to monitor her."

    "Doctor 2" "She's almost totally non-responsive, but that should pass in time."

    "The doctor sighs, and takes a deep breath."

    "Doctor 2" "I guess this is a lot to take in all at once, especially in your condition."

    "Doctor 2" "I'll call for your doctor, and get you more painkillers."

    "Doctor 2" "You should try to rest."

    "Doctor 2" "I'll keep you informed about Hanako."

    "Doctor 2" "You're dear to her."

    "Doctor 2" "That makes you dear to me, too."

    play sound sfx_doorclose # [str]
    
    "Without waiting for my reply, he stands up, and strides out of the door."

    "I get the impression that this wasn't too easy for him, either."

    stop music fadeout 2.0 # [str]
    scene black # [str] (not sure)
    with shuteye # [str]
    with Pause(1.0) # [str]
    window hide # [str]
    return
    
label en_H26:
    scene black # [str] (JUST IN CASE!)
    scene bg hosp_room2 # [str]
    with openeye # [str]
    
    window show # [str]
    
    show lilly cane_smile_cas at twoleft # [str]
    with charaenter # [str]

    "The first visitor to my room, once again, is Lilly."

    "However, instead of bringing along Yuuko, she is joined by a pair of familiar faces."

    play music music_happiness fadein 1.0 # [str]

    show lilly cane_planned_cas at leftoff # [str]
    with charamove # [str]

    show shizu adjust_happy at twocenteroff2 # [str] (fixme!!)
    with charaenter # [str]
    show misha hips_grin at tworight # [str]
    with charaenter # [str]

    mi "Hicchan! We heard you were skipping school, so we had to come and check on you."

    show shizu behind_smile at twocenteroff2 # [str]
    with charachange # [str]

    shi "…"

    show misha cross_laugh at tworight # [str]
    with charachange # [str]

    mi "That's right! It's our job as council members!"

    "The simple act of receiving visitors lifts my spirits, and throughout the afternoon a virtual parade of students marches through my room."

    #hide lilly # [str]
    #with charaexit # [str]
    hide misha # [str]
    with charaexit # [str]
    hide shizu # [str]
    with charaexit # [str]

    "As I expected, the reactions of the students here is totally different from those at my last school."

    "There, everyone seemed to be shocked seeing me in a hospital bed, and didn't know what to say beyond “Get better.”"

    "But here, it's almost as if it's totally natural to see a friend immobilised in a hospital bed."

    show emi excited_happy at twocenteroff3 # [str]
    with charaenter # [str]

    emi "Only a month, eh? That's nothing. And you miss your exams… lucky!"

    hide emi # [str]
    with charaexit # [str]

    "Thankfully, most of them also realise that I can't talk all that much, but that doesn't seem to phase anyone."

    "They take it in turns to sit in my room, sharing their stories of studying and the day to day running of the school."

    "When the next visitor enters, they bid their farewells, and vacate the chair."

    "Throughout the entire affair, Lilly stoically sits in the chair closest to the door."

    stop music fadeout 2.0 # [str]

    "Around six, the last of the visitors departs, leaving Lilly and I alone."

    hi "Lilly… I have some news of Hanako. Could you close the door?"
    
    show lilly cane_oops_cas at leftoff # [str]
    with charachange # [str]
    
    "The troubled look Lilly gives me at the mention of Hanako reminds me that this won't be easy for either of us."

    # not literal animations, eh? [str]
    #show lilly cane_oops_cas at rightedge # [str]
    #with charamove # [str]
    show lilly cane_oops_cas at center #twoleftoff # [str]
    with charamove_slow # [str]

    "Still, she gently gets out of her chair, pushes the door closed, and finds her way to the chair next to my bed."

    play music music_drama fadein 2.0 # [str]

    li "So… I take it you've learnt something?"

    hi "Lilly, you once told me that Hanako told you everything about her condition…"

    hi "What exactly did she tell you?"

    "Lilly looks a little shocked, but manages to speak."

    li "She told me that her parents were killed in a fire, and that she was badly burnt."

    show lilly cane_surprised_cas # [str]
    with charachange # [str]

    li "… Is that wrong?"

    hi "No, no it's not wrong, but it turns out that it's only half of the story."

    li "Whatever do you mean?"

    hi "Hanako… is mentally unstable."

    show lilly cane_displeased_cas # [str]
    with charachange # [str]

    "Slowly, and trying to remember everything the doctor from the day before told me, I explain Hanako's condition to Lilly."

    "Her face tells me that this is the first that she's ever heard of this part of the story."

    "I finish by telling her about Hanako's present condition, and her isolation from the world."

    "For a time, neither of us can speak."

    show lilly cane_surprised_cas # [str]
    with charachange # [str]

    li "I… never knew. After all this time, she still didn't trust either of us enough…"

    li "Or perhaps, she just didn't want us to know, or didn't even realise herself."

    hi "It's probably a combination of both."

    hi "Either way, I can't imagine how she's feeling right now."

    li "You are right, I would imagine that it would be quite lonely…"

    hi "I just feel so helpless. I can barely move, let alone getting around."

    hi "I just want to see her… to let her know that I'm there…"

    show lilly cane_concerned_cas # [str]
    with charachange # [str]

    li "As do I. I can't imagine that her isolation is helping her."

    li "Tomorrow, I will speak with her doctors."

    li "Perhaps we can persuade them to let us see her."

    "How Lilly keeps a level head at times like this astounds me."

    hi "That… thank you, Lilly."

    show lilly cane_weaksmile_cas # [str]
    with charachange # [str]

    li "My my, I'm not just doing this for you, Hisao."

    li "Hanako is quite precious to myself as well, you know."

    "A glimmer of a smile flashes across Lilly's face, and in that moment, I know that everything is going to be fine."

    stop music fadeout 2.0 # [str]

    "Lilly is quite the capable negotiator, so she should be able to organise something…"

    "… right?"

    "Just as Lilly turns to leave, a nurse turns up with a trolley of food."

    "Nurse" "Oh, I'm sorry miss, but visiting hours just finished."

    #Lol one shot.

    show lilly cane_sleepy_cas # [str]
    with charachange # [str]

    li "That's quite alright, I was just making my way out."

    hide lilly # [str]
    with charaexit # [str]

    "As the nurse feeds me my dinner, my thoughts once again turn to Hanako, alone in her room."

    "Hanako, suffering, all alone."

    "A pang of guilt floods through my body."

    "If I had only taken her somewhere else the other day, we would have been fine."

    "If I had only taken heed of Lilly's words of warning instead of being wrapped up in my fledgling romance."

    "If I had only seen Hanako's inner self instead of absorbing myself in how she acted…"

    "Gah this is getting me nowhere."

    play music music_soothing fadein 2.0 # [str]

    "Nurse" "You're thinking about your friend, right?"

    hi "How did you know?"

    "The nurse smiles, gently."

    "Nurse" "The story of you two spread through the hospital like wildfire."

    "Nurse" "The tragic fate of two lovers separated by their illnesses, it's not something we get here often."

    "Nurse" "It's kind of romantic…"

    #For some reason, I'm now thinking of Asa's blond waitress friend from Shuffle! (Can't
    #remember her name though. Ma ma ma!"

    "I see a slight glaze come over the nurse's eyes, and for a short time she stops feeding me to bask in the drama of the story."

    hi "I wish it were that easy for us…"

    "Instantly, the nurse snaps back to reality."

    "Nurse" "Well, I suppose it's not going to be easy now, but it's for the best."

    "Nurse" "Both of you need your rest now, as painful as that may be."

    "Nurse" "And, when you think about it, it will only be a week or two before you can see each other."

    "Nurse" "It's not that long of a wait…"

    "Although she says this so casually, all it does is remind me of the fact that I've only known Hanako for a little over a month."

    "A week apart seems like an eternity, and the month that my doctor wants to keep me in here feels as long as my entire existence."

    "The nurse sees me contemplating this, and gives me a look that says “Ah, youth!.”"

    "I can't help but feel a little pissed off by that."

    "At the conclusion of my meal, the nurse collects the scattered dishes onto her trolley, and leaves me."

    "Nurse" "Just remember, this is what's best for both of you. You'll be together again in no time."
    
    stop music fadeout 2.0 # [str]
    
    play sound sfx_doorclose # [str]
    "The door closes with a click, and I am alone."

    "I feel so helpless here, unable to even get out of my bed."

    "Gently, I touch the tender areas of my chest, hard enough to feel the pain, but soft enough to not cry out."

    "Hanako sure did a number on me, eh?"

    "It seems like every rib is broken in some way or another."

    "But… it only seems to hurt when I move my chest or arms too much."

    "I wonder…"

    "Using my hips as a pivot, I swing around so that I am perpendicular to the bed."

    "White hot pain shoots across my chest, but it is gone again in an instant, replaced by the dull, background pain that I'm now accustomed to."

    "I summon up my strength, and, holding my breath, I slide myself off the bed."

    "The impact of my feet hitting the floor echoes through my bones, and I almost cry out in pain."

    "Collapsing back I the bed, I realise that, with a bit of effort, I can stand on my own."

    "The effort, however, has exhausted me, and I quickly fall into a fit of sleep."

    #timeskip
    window hide # [str]



    scene black # [str]
    with shuteye # [str]

    with Pause(1.0) # [str]

    mystery "Hisao…"

    mystery "Hisao…?"

    scene bg hosp_ceiling #misc_ceiling #hosp_room2 # [str]
    with openeye # [str]

    show lilly cane_satisfied_cas_close at Position(xanchor=0.5, xpos=0.15, yanchor=1.0, ypos=1.15, rotate=70) # [str]
    with charaenter # [str]

    "A gentle voice recalls me from the void, and I open my eyes to see Lilly's face hovering above my bed."

    hi "Lilly… what time… no, what day is it?"

    show lilly cane_ara_cas_close at Position(xanchor=0.5, xpos=0.15, yanchor=1.0, ypos=1.15, rotate=70)  # [str]
    with charachange # [str]

    "Lilly tires her best to laugh, but it sounds horribly forced."

    scene bg hosp_room2 # [str]
    with locationchange # [str]

    show lilly cane_weaksmile_cas at twoleft # [str]
    with charachange # [str]

    play music music_pearly fadein 0.2 # [str]

    li "It's Saturday morning, Hisao."

    li "I was able to come earlier today."

    hi "Oh, thank you."

    hi "But don't you have to study for exams as well?"

    li "I bring my books with me and read them on the bus, plus I have all evening."

    li "Really, it's no bother."

    "Diligent as always."

    "If she were capable of taking notes for Hanako and I I'm sure that we'd both return to little pink notebooks jammed full of exam notes."

    hi "You really are something else. You know that, right?"

    #lilly blush
    show lilly cane_cheerfulblush_cas at twoleft # [str]
    with charachange # [str]

    li "My my, Hisao, you're embarrassing me."

    li "However, there is something else that I wanted to discuss with you."

    hi "Oh, really? What's going on? Did you find something out about Hanako?"

    #Lilly srs bsns
    show lilly cane_reminisce_cas at twoleft # [str]
    with charachange # [str]

    li "It would appear that Hanako is staying in the hospital's locked ward."

    hi "Locked ward? She's not in trouble for what she did, is she?"

    li "Oh my no. But it is the only place in the hospital where she can be constantly monitored."

    show lilly cane_sad_cas at twoleft # [str]
    with charachange # [str]

    li "Her doctors are really concerned about her."

    li "What I did find out though is that, during visiting hours, we should be able to sign ourselves into the locked ward."

    hi "Eh? Like, as visitors?"

    li "That's right."

    li "Whilst the name sounds intimidating, it's really just a place where patients can be monitored."

    li "It's mostly for psychiatric patients, and visitors can help a lot of them through tough times."

    show lilly cane_weaksmile_cas at twoleft # [str]
    with charachange # [str]

    li "It's practically encouraged."

    stop music fadeout 4.0 # [str]

    "Thoughts turn through my head."

    "If it were possible to get into the ward, then perhaps I could see Hanako."

    "As much as her doctors have warned against it, I can't stand not knowing how she's going."

    #"And the mixture of hope and fear on Lilly's face tells me that she feels exactly the same way."
    window hide # [str]
    return

label en_choiceH26:
    #Choice
    #1) Go to visit Hanako
    #2) Follow the doctor's orders
    menu:
        with menueffect
        
        "And the mixture of hope and fear on Lilly's face tells me that she feels exactly the same way."
        
        "Go to visit Hanako.":
            return m1
            
        "Follow the doctor's orders.":
            return m2

label en_H27:

#H27 – Dulce et decorum est
#So we all know, the title of this scene is from the old Latin saying:
# Dulce et decorum est pro patria mortis
#"It is both glorious and honourable to die for one's country.
#It is also the name of a poem by an Aussie War poet
#No, I don't remember his name. His poem had a gas attack though.
#Also, as my "penultimate" scene, I would like for this title to stay.


    hi "I tried it out last night, and I think I can walk, especially if you help me."

    li "Are you sure, Hisao?"

    hi "You know it as well as I do."

    hi "Hanako needs us, and we need her."

    hi "Locking her up like this is just… too sad."

    #lilly determined
    show lilly cane_displeased_cas at twoleft # [str]
    with charachange # [str]

    li "You are right. How can I help?"

    "With a bit of a struggle, I manage to stand up."

    "The jolting movement sends bolts of pain coursing along my nerves, causing me to bite back a whimper."

    li "Hisao? Are you alright?"

    hi "Y…yeah. I'm just a little tender, is all."

    li "Here, take my shoulder. Don't be shy now…"

    show lilly cane_smileclosed_cas_close at twoleft # [str]
    with charachange # [str]

    "I graciously accept Lilly's offer, and lean on her shoulder."

    "She extends her cane forward, and starts to lead me."

    "I chuckle to myself against my protesting ribs."

    li "What's the matter?"

    hi "Oh, it's nothing."

    hi "I was just thinking that it's strange that you're the one that's leading me around for once."

    #lilly giggle
    show lilly cane_giggle_cas_close at twoleft # [str]
    with charachange # [str]

    li "I daresay you're right. It is a bit strange."

    scene bg hosp_hallway # [str]
    with locationchange # [str]

    "We make our way into the ward's hallways, blending into the crowd of the infirm and their guests."

    "Lilly seems to know the general route, and before long I start seeing signs directing us to the “Psychiatric care ward.”"

    "Our pace is woefully slow, but every time we try to speed up, I feel the jagged edges of my broken ribs softly tearing apart my chest."

    "I feel the hot blooming of blood under the surface of my skin, and look down at my chest."

    "As expected, new, bright bruises are forming before my eyes."

    "They spread out from the small lumps where my ribs are dislocated, and are rapidly covering the entirety of my chest."

    "Still, we've come this far already."

    "Hanako needs us."

    "A little bruising will clear up in no time."

    li "Are you sure you're alright, Hisao?"

    hi "I'm fine. Besides, we're in a hospital."

    hi "What's the worst that can happen."

    li "I suppose you are right."

    li "I guess I'm as afraid of losing you as Hanako is…"

    "Lilly's words carry with them a strange mixture of melancholy and concern."

    "I'm almost moved to tears not only by her sincerity, but also by the fact that she considers me close enough to care about."

    "It's the first time that I've ever had anyone care for me in that kind of way."

    "I take a deep of a breath as my body will allow, and squeeze Lilly just a little."

    li "Eeh?"

    "Her surprised squeal makes me laugh."

    "It's just like Lilly; refined yet somehow surprising."

    hi "Thank you, Lilly. For everything."

    li "Y…you're welcome, Hisao."

    li "But whatever brought this on?"

    hi "Nothing, and everything."

    hi "Just… thank you."

    "We say nothing more until we reach the doors of the locked ward."

    #Scene change. Yes, I know, new BG RAGE. I *may* be able to get these though.
    
    # nah, just using hack and unused school bg [str]
    image bg school_hallwayextra = 'bgs/school_hallwayextra.jpg' # [str]
    scene bg school_hallwayextra # [str]
    with locationchange # [str]
    
    "The glass doors look ominous, surrounded by a number of magnetic locks and sensors."

    "To the right of the door is a little window, manned by a nurse in a far-too-flowery uniform."

    "Nurse" "Hello, how may I help you?"

    li "Good day. We're here to visit our friend, Miss Kadono."

    "Nurse" "Oh, I see. Please, sign in here."

    "Nurse" "I believe Miss Kadono is in the common room right now."

    li "Thank you ever so much."

    "I sign the log book that the nurse hands me through the small window for both Lilly and myself."

    "The nurse retrieves the book through the window, makes a couple of notes, and then toggles a button on her desk."

    "There is a low, electronic buzz, and a click as the door's lock is deactivated."

    "We pull the door open, and walk into the ward."

    "Inside, the ward look just like any other."

    "Patients walk around in their gowns, talking to each other, or watching TV in the small common room."

    "However a detailed look around reveals the sad truth of the ward."

    "Many of the patients have the far-away gaze of people no longer connected to the world."

    "One man, who could be no older than 40, rocks from side to side on his chair, oblivious to his surroundings."

    "An elderly woman in the common room is silently mouthing her half of a conversation to the vacant space beside her."

    "Lilly and I walk past room after room of patients simply gazing out of windows."

    "Whilst the usual disinfectant smell of a hospital is as prominent here as anywhere else, there is also a subtle trace of sweat and human filth filling the air."

    #If only I were making this all up…

    hi "It's… unbearable."

    li "I can only imagine. This is no place for Hanako."

    hi "The name you gave at the front desk…?"

    li "I had my family do some research on my behalf."

    li "We have friends at this hospital."

    li "But, please… ask no more."

    "Lilly's quavering voice tells me more than I ever wanted to know."

    "The ward's main corridor is simply nameplate after nameplate."

    "It looks just like a normal corridor, save for one small detail."

    hi "The locks… are on the outside?"

    li "Of course. Some patients are required to be retained inside their rooms."

    hi "I see."

    "We continue down the hall in silence."

    "Each door has a small, reinforced glass window in it."

    "Against my better judgement, I can't help but peek through each and every one."

    "As we progress, the rooms become more barren, and the patients more unhinged."

    "One by one, items of furniture are removed."

    "By the time we reach the door marked “Ikezawa,” the contents of the room are limited to a bed and a small night stand."

    "I close my eyes, right myself, and then peer in through the door."

    #This will require a new sprite set of three sprites. If this is too hard, then I will add
    #another line putting her in the same clothes as H23.
    
    # # # [str] (no longer truth!)
    #window hide
    #nvl show dissolve
    #n "I'm sorry, but next scene will not have visuals because there's no suitable bg and sprites for upcoming events." 
    #n "So i leave it for you to imagine."
    #n " - [str]"
    #nvl hide dissolve
    #nvl clear
    #window show
    # # # [str]

    scene bg hosp_paddedroom # [str]
    show hanagown evil_hosp at Position(xanchor=0.5, yanchor=1.0, xpos=0.55, ypos=1.15) # [str]
    show hanako_oiwadoor # [str]
    with locationchange # [str]
    
    "Hanako sits in the corner of the room, hugging her knees."

    "Her long, matted hair hangs over her face and legs, as if someone dumped a pile of old thread upon her curled frame."

    "Her hands grip her shins so tightly that the color has been washed from them."

    "I can't bear to see it, and have to grasp the door handle and Lilly's shoulder to prevent myself from collapsing."

    "It's as if her tiny body were worked into an artwork entitled “Destitution.”"

    li "Hisao? What is it?"

    hi "She… oh lords… "

    "Lilly, sensing that no words will help, covers my hand with hers, and gently squeezes."

    "Drawing strength from Lilly, I toggle the door's lock, and make my way into the room."
    window hide # [str]
    
    scene bg hosp_paddedroom # [str]
    show hanagown evil_hosp at centersit # [str]
    with whiteout # [str] ('cause dissolving door looks terrible)
    
    play sound sfx_lock # [str] 
    play sound sfx_dooropen # [str]
    
    window show # [str]
    
    "The sterility of the room extends beyond disinfectant; even the senses are washed clean by the room."

    "Bright, fluorescent light reflects off the bare-white walls."

    "Sounds are deadened by the soft panels attached to the walls, making hearing anything difficult."

    "It is totally devoid of any kind of stimulation."

    "Behind me, I hear Lilly come in through the door."
    
    play sound "sfx/doorslam.ogg" # [str] (meh)
    with Pause(0.8) # [str]
    play sound sfx_lock # [str] 
    
    "With a hiss of gas and a click, it swings itself shut, and locks."

    li "Oh, no. I'm sorry, Hisao… I didn't notice…"

    hi "It's… okay…"

    "My words are laboured; my consciousness is focussed only on the crumpled form of the girl in front of my eyes."

    li "How… is she?"

    hi "Not good."

    "The combination of concern for Hanako and my injuries make walking difficult, and I can barely stagger across the room to her."

    "As I get closer, I hear a quiet muttering."

    ha "…"

    ha "… im …"

    ha "… k … ed…"

    hi "Hanako?"

    "She makes no response."

    "She's so cut off from reality that she doesn't even seem to have noticed our presence."

    "As I get closer, I see a plate of food set down next to her, untouched."

    "Has she not eaten a thing since that day?"

    "… Has she even moved since then?"

    "I squat down to bring myself level with her cowed head."

    "Moving my head gently towards hers, I start to pick out words in her incessant muttering."

    ha "I… k…d… im…"
    
    stop music fadeout 4.0 # [str]
    
    ha "I… k…d… em…"

    ha "I killed him…"

    ha "I killed them all…"

    #If there were some kind of "shock" effect, now would be the time to use it.
    play sound sfx_heartfast # [str]
    show heartattack alpha  # [str]
    with Dissolve (0.1) # [str]
    hide heartattack alpha  # [str]
    with Dissolve (1.5) # [str]
    
    "Hanako's words strike me to the core."
    
    play music music_drama # [str]
    
    hi "Hanako? HANAKO!?"
    
    show hanagown normal_hosp at centersit # [str]
    with charachange # [str]
    
    "I brush away the hair covering her face to reveal her eyes."

    "Her cold, dead eyes, unable to focus on anything."

    "In the dim distance, I can hear Lilly's voice."

    li "Hisao? Hisao?! What's going on? Where are you?"

    "The lack of sensory input must be doubly frightening for Lilly, but that is the least of my concerns."

    "I gently wrap Hanako's hand with mine."

    hi "Hanako, I'm here. Look, I'm here."

    hi "I promised I'd never leave you, right?"

    hi "Hananko?"

    ha "I killed them all…"

    "Her eyes skitter around in their sockets, searching for answers she will never find."

    "I grab her shoulders, and try to shake her back to reality."

    hi "Hanako, I'm here. Look at me! Talk to me!"

    li "Hanako? Hisao? Are you there? What's going on?"

    "At the sound of Lilly's voice, a faint glimmer of recognition appears on Hanako's face."

    hi "Lilly! Keep talking!"

    li "Hisao? What's going on?"

    hi "I don't know, but I think we're getting there!"

    hi "Just keep talking!"

    li "Hanako? Are you there, Hanako?"

    li "It's Lilly, remember?"

    li "We go to school together, we live next door to each other, remember?"

    "With each sentence, Hanako's murmurs fade in volume, and her rapid eye movements slow down."

    li "Remember? You, me…"

    "Her eyes stop."

    li "… and Hisao…"

    "At the mention of my name, Hanako's body tenses."

    show hanagown worry_hosp at centersit # [str]
    with charachange # [str]
    
    "Her head snaps up, locking her eyes with mine."

    "For a brief instant, relief floods my body, nullifying the pain and torment."

    hi "Hana…"

    #SFX Screech. Has to be done.
    
    show hanagown shock_hosp at centersit # [str]
    with charachange # [str]
    
    "Hanako's screech pieces my eardrums and burrows directly into my brain."

    "Her eyes, now totally awake, regard me in pure, abject terror."

    show hanagown shock_hosp at center # [str]
    with charafast # [str]
    with vpunch # [str]
    
    "She stands blot upright, throwing me to the ground."

    "As I try to collect my broken body, she bolts for the door."

    hi "Ha… ha…"

    "I try to speak, but my lungs feel like they are trapped by my disjointed ribcage."

    "All I can manage is to wheeze the first syllable of her name."

    "Lilly lies on the floor, knocked over by Hanako on her rush to the door."

    "Hanako grabs the doorknob, desperately trying to wrench the door open."

    "But it's no good. The door doesn't so much as budge."

    "I finally manage to stand up, the heat of internal bleeding now like a fire in my chest."

    hi "Ha… haaaaa…"

    "Spittle sprays from my mouth as I try to speak."

    "I reach out as far as I can, and stumble across the room towards Hanako."

    ha "Getawaygetawaygetaway"

    "If I can just make it to her, then I'm sure I can comfort her."

    ha "GetawaygetawaygetawayGETAWAYGETAWAYGETAWAY"

    "The terror that grips Hanako is unlike any that I've seen before."

    "Her eyes are bloodshot and tearstained."

    "Her body quakes, and she falls back against the door, her feet still desperately trying to push her through the solid panel."

    hi "H…"

    "Before I can even start to try to call her name, I find myself coughing."

    "An iron taste fills my mouth, and I see a spray of crimson emerge between Hanako and I."

    "I plead with my eyes for her to calm down, and raise my arm out to greet her."

    ha "Getawaygetawaygetaway YOU'RE SUPPOSED TO BE DEAD!"

    "Like a cornered animal, Hanako lashes out at me."

    play sound sfx_crunchydeath # [str]
    # # dat rotozoom madness again
    scene bg hosp_paddedroom at RotoZoom(0,-6,0.1,1.0,1.2,0.1, xalign=0.5, yalign=0.52) # [str]
    show bloodred at Alpha(0.2,0.2,0.2) # [str] (i'm suprised that it's actually work)
    with Dissolve(0.1) # [str]
    with vpunch # [str]
    
    "There is a sickening crunch as we collide, with Hanako pushing me square in my chest."
    

    "As I collapse to my knees, I cough again."

    "This time, it's no longer a spray of blood, but a downpour."

    "I feel the hot liquid slowly flow down my chin, and see the red stain on the floor ahead of me."

    "Gargling blood and froth, I try again to call out to my love."

    hi "…"

    "But words are no longer possible."

    "Every breath brings a gurgle from my lungs, and every exhalation brings ever more blood."

    "My strength fails, and I tumble from my knees and onto the floor."

    "The bright room grows ever dimmer."

    "In the distance, I see Hanako clawing at her eyelids."

    "It's as if the two halves of her mind are at war. One cannot bear to witness the terror any longer, but the other is forcing her to watch."

    "I summon my last reserves of strength, and reach out for her as she collapses in a heap."

    show passoutOP1 # [str]
    with None # [str]

    "As my froth-corrupted lungs fill with blood, the coughing stops."

    "The room gently, quietly, dims out of existence."
    
    scene black # [str]
    with Dissolve (1.5) # [str]
    with Pause(1.0) # [str]
    window hide # [str]
    return


label en_end_hanakobad1:
    # Hanako bad end 1, after H27
    scene endscreen with dissolve #black with dissolve # [str]
    with Pause(1.5) # [str]
    
    stop music fadeout 1.0 # [str]
    
    scene black with dissolve # [str]
    centered "~ hanako bad end 1 ~" with dissolve
    return

label en_H28:

    window show # [str]
    
    hi "I… I think we should wait for the doctor's approval."

    show lilly cane_sleepy_cas at twoleft # [str]
    with charachange # [str]

    "Lilly's face drops in disappointment."

    "I daresay mine did too."

    li "That… is probably wise."

    hi "Well, Hanako's doctor told me that he's known her since the fire."

    hi "I can't imagine that he'd ask us to do something so drastic without reason."

    li "You are right. But Hisao… it's difficult."

    li "I can't imagine what it's like for her to be trapped, alone…"

    hi "I know. I don't think I can stop myself either."

    hi "I've been practicing getting up, just in case."

    #Lilly shocked
    show lilly cane_surprised_cas at twoleft # [str]
    with charachange # [str]

    li "Hisao! That's dangerous! You should rest!"

    "I can't help but chuckle at Lilly's concern."

    hi "I guess you're right."

    hi "The quicker I get better, the quicker I can get out of here, right?"

    #lilly smile
    show lilly cane_smile_cas at twoleft # [str]
    with charachange # [str]

    "Lilly flashes her golden smile at me, and, almost instantly, I feel relieved."

    li "I'll visit you every day, Hisao."

    li "And I'll keep as much of an eye on Hanako as her doctors will let me."

    "Once again, the mood in the room drops slightly, as if the temperature just dropped 10 degrees."

    hi "Lilly…"

    li "Yes, Hisao?"

    hi "I… I want to see her."

    show lilly basic_smile_cas_close at twoleft # [str]
    with charachange # [str]

    "Lilly reaches out for my hand, and I grasp it gently."

    li "So do I. But, we must remember, this is for her sake."

    hi "You're right. I just hope that she's alright."

    li "I'm sure she is. This is one of the best places for her right now."

    li "And, as an added bonus, you two can now say that you're living under the same roof."

    #lilly smile.
    show lilly basic_cheerful_cas_close at twoleft # [str]
    with charachange # [str]

    "I let out a little sigh of relief at Lilly's roundabout humour."

    hi "I'm sure she'll be pleased to hear that."

    "The sound of the nurse with her food cart can be heard approaching the door."

    show lilly cane_smileclosed_cas at twoleft # [str]
    with charachange # [str]

    li "I guess I must take my leave now."

    "Lilly exits the room just as the nurse appears in the doorway."

    hide lilly # [str]
    with charaexit # [str]

    "The nurse bows slightly to Lilly, who disappears beyond the doorframe."

    play music music_twinkle fadein 0.5

    "Nurse" "That's the same girl as yesterday, isn't it?"

    hi "Yes, that's Lilly."

    "The nurse smiles a little."

    "Nurse" "Isn't it nice that she visits every day?"

    hi "It's a comfort, that's for sure."

    hi "The last time I was like this, people stopped visiting after about a week."

    "The nurse nods slowly in agreement."

    "Nurse" "We see it all the time with patients your age."

    "Nurse" "Once the hype of having a student in hospital wears off, no-one comes to visit."

    "Nurse" "It's heartbreaking, really."

    "Nurse" "Though I think the students at your school are a little different."

    hi "You've got that right."

    "Nurse" "Well then, shall we start your dinner?"

    #my apologies if the NVL below is incorrectly called.
    window hide # [str]

    nvl show dissolve # [str]

    n "Days became weeks, which finally became a month."

    n "True to her word, Lilly visited every day."

    n "And, every day, the same news:"

    n "“They still won't let me see her.”"

    nvl clear

    n "Each and every day, without fail."

    n "We're not allowed to see her."

    n "Then, one Saturday…"

    nvl hide dissolve # [str]

    nvl clear

    "Doctor" "Well, I think you've healed enough now."

    "Doctor" "If it's alright with you, I'd like to schedule your surgery first thing Monday."

    hi "The sooner the better I think. I feel so weak just laying here."

    "That's not entirely true."

    "With the help of the nurses and Lilly, I've managed to start walking around quite comfortably."

    "Doctor" "I like your spirit."

    "Doctor" "Once you've recovered from this surgery, I think you'll find life a lot easier."

    hi "Do my parents know yet?"

    "Doctor" "I was about to go and let them know. Would you like to speak to them."

    "For a moment, my choice wavers."

    hi "I… think it'd be better if you told them."

    hi "I'll talk to them when they arrive."

    "The doctor smiles, knowingly."

    "Doctor" "I understand. I'll call them now."

    # timeskip? 
    
    "I lie back on my bed, and examine a ceiling far too familiar to me."

    "The strange, yellowing stains are somewhat like clouds."

    "You can spend hours tracing shapes in your mind with them."

    "Also, it tunes your other senses in a strange way."

    "I swear that I can hear Lilly's cane from further away each day, its staccato clicking echoing down the halls and into my room."

    show lilly cane_satisfied_cas at twoleft # [str]
    with charaenter # [str]

    li "Hisao…"

    hi "Lilly…"

    $ doublespeak (hi,li, "I have good news")

    #Lilly giggle
    show lilly cane_giggle_cas at twoleft # [str]
    with charachange # [str]

    "We both chuckle slightly at our similar thoughts."

    hi "You first…"

    li "No, I must insist…"

    hi "Well, I saw the doctor this morning, and he said I'm good for surgery."

    #lilly smile
    show lilly cane_smile_cas at twoleft # [str]
    with charachange # [str]

    li "That's wonderful!"

    show lilly cane_smileclosed_cas at twoleft # [str]
    with charachange # [str]

    li "However, I think you'll be more pleased at my news…"

    "I feel my eyes snap open, and I sit bolt upright."

    hi "Hanako?"

    "Lilly nods eagerly."

    li "She's not allowed to be released just yet, but they did allow me to see her."

    hi "And? How is she? Can I see her?"

    stop music fadeout 3.0 # [str]

    #lilly frown
    show lilly cane_concerned_cas at twoleft # [str]
    with charachange # [str]

    li "She… isn't the best of sorts."

    li "For a while, she thought that she had killed you, and it wasn't until after she had calmed down her mind that the doctors could talk to her."

    li "She's still fairly medicated, and the doctors believe that contact with you should be limited until both of you are settled."

    "The thought of not being able to see Hanako before my surgery is gut wrenching."

    hi "So… when will I see her next?"

    li "If she remains as she is now for the next few days, as early as Wednesday."

    "I dance a victory dance in my mind."

    hi "I should almost be ready to be discharged by then."

    li "How very fortunate. I shall let Hanako know now."

    "My heart skips a beat."

    hi "You're… going to see her now?"

    li "Yes, I thought I would tell her that you're doing well."

    hi "Wait! Tell her…"

    "Damnit, I am no good at this."

    "I've had the best part of a month to think of what to say, yet, when it comes to the crunch, I've got nothing."

    hi "…tell her that I miss her, and that I can't wait to see her."

    #Lilly giggle
    show lilly cane_giggle_cas at twoleft # [str]
    with charachange # [str]

    li "You two are so alike."

    hi "Huh?"

    "Lilly stands up, making ready to leave."

    show lilly cane_smile_cas at tworight # [str]
    with charamove_slow # [str]

    "At the door, she turns back to face me."

    li "Hanako said exactly the same thing."

    hide lilly # [str]
    with charaexit # [str]

    "As she waltzes out into the corridor, I feel a wave of joy overtaking my body."

    "The simple fact that Hanako is thinking of me after all this time fills me with a strange, child-like glee."

    "The stains on the ceiling now paint a different picture."

    "What once was an angry dragon now looks like two kittens."

    "…"

    "Damnit I'm going insane just lying here."

    "I get out of my bed, and peer out the window."

    "Hospital grounds always depress me."

    "The patients, in their pastel gowns, being lead around by their usually over-dressed visitors."

    "The patients wear half-hearted smiles, knowing that their time with their friends will be limited."

    "The visitors' smiles seem forced too, as if they have to have to put on a brave face for the patient."

    "The veneer of happiness just seems so unnecessary."

    "But today, things are different."

    "Today, instead of false happiness, I see hope."

    "I see people willing to take time out from their day to remind their friends that they are important to them."

    "I see patients genuinely happy in the fact that they are still cared for."

    "I see a reflection of a person desperately wanting to see someone."

    window hide # [str]
    scene black # [str]
    with shuteye # [str]
    with Pause(1.0) # [str]

    return

label en_H29:

    #This entire scene is the "Loli flashback".
    # Most of it is set at night or on fire, so I think VFX would do most of it
    #However, I would like a CG of the last scene; Hanako burnt, in the snow, out the front
    #of her ruined house.
    #alternatively, the entire thing could be cut.
    #I also don't think I want to do this in NVL.
    #it carries more weight line-by-line
    
    window hide None
    
    scene white
    with dissolve
    #show n_vignette # [str] (i'd be very happy if that work)
    with Pause(2.0)
    
    play sound sfx_powerout
        
    scene black # [str]
    with dissolve # [str]
    
    centered "*Fzzzt*"
    
    "The lights of the town went out with the sound of dying electricity; a blackout caused by excessive snowfall."

    "In a small, two-bedroom house near the station, the quiet scratching of pencil on paper stopped."

    "The shadowed figure responsible for the noise sighs, places the pencil on the paper, and then stands up."

    "Carefully feeling her way around the house, she retrieves the items that she is looking for, and breaths a sign of relief."

    play sound sfx_lighter
    
    with Pause(0.5)
    
    play sound sfx_lighter

    "The tiny sparks from the lighter light up the tiny kitchen like a strobe."

    "Finally, the lighter manages to take hold, and a meagre flame flickers at its mouth."

    "The shadowed figure carefully lights two candles, then extinguishes the flame."

    "In the weak yellow light of the candles, the figure resolves into a young woman in casual clothes."

    "Walking carefully, as to not spill too much wax, she returns to her study."

    "The plans spread out on the table in the centre of the room are once again visible; nothing more than a collection of lines on an otherwise blank sheet."

    "The walls of the study are decorated with hand-rendered drawings of various buildings, each accompanied by a photo."

    "Against the far wall stand two deep chests, full of hand-drawn plans."

    "The woman carefully places the candles on either side of the desk, and picks up her pencil once more."

    "In a short time, she is once again working at full pace, the scratching of the pencil nearly matching the flickering light from the candles."

    "And so the woman continues, drawing away into the night."

    "Before long, the lines on the paper are connecting, forming the outline of a house."

    "A new house."

    "She buries her head deeper into the plans, making the most of the weak candle light."
    
    play music music_hanakofire fadein 0.1

    "She is so engrossed in her work that she doesn't hear the soft sobbing and padding of feet until their owner wraps its arms around her legs."

    ha "Mommy…"

    #Dear lords I hate that spelling. I'd much prefer "Kaa-san" over "Mommy"
    #oh no you don't

    "The woman looks down, startled."

    "Her daughter, in her flannel pyjamas and carrying her favourite plush rabbit, is wrapped firmly around her leg, crying."

    ha "It's all dark, mommy…"

    "The woman puts down her pencil, and picks up her daughter, placing her on her lap."

    "Mother" "Shhh now, Hana-chan." # [str] (just a small change that feels absolutely appropriate to me)
    #"Mother" "Shhh now, Hanako."
    
    #If we do ever decide to drop honourifics, this should be changed to whatever Lilly calls
    #Hanako.

    "Mother" "What's the matter?"

    ha "It's dark, and I can't sleep. Where are the lights, mommy?"

    #gargh this is killing my scene

    "The woman gently strokes her daughter's hair before gently kissing the top of her head."

    "Mother" "Come on now, I'll fix that for you."

    "The woman picks up one of the candles, now covered in hardened rivulets of wax, and helps her daughter stand up."

    "The daughter stumbles slightly, and bumps the desk, but neither of them notices beyond that."

    "Hand in hand, they walk into the next room, where a man lays sleeping on the edge of a double futon."

    "Next to him lay another two pillows; the small family always sleeps together."

    "The woman guides her daughter into the futon next to the sleeping man, and places the candle at the head of the futon."

    "Mother" "There you are, see? Now there's light here."

    "The man stirs into consciousness."

    "Father" "Eh? What's going on here?"

    "Mother" "There was just a little blackout, and the night light went out."

    "Mother" "I brought a candle for Hanako to get to sleep by."

    "The man smiles slightly, and wraps an arm around his daughter."

    "Father" "Don't you have a great mother, Hanako?"

    "Father" "Say “Thank you.”"

    ha "T…thank you mommy."
    
    $ renpy.music.set_volume(0.025, 0.0, channel='ambient')
    play ambient sfx_housefire fadein 2.0

    "The daughter hugs her plush rabbit tightly as her mother smiles and leaves the bedroom."
    
    play sound sfx_doorclose
    $ renpy.music.set_volume(0.05, 1.0, channel='ambient')

    "As she slides the door to the bedroom closed, she hears a strange sound…"
    
    $ renpy.music.set_volume(0.1, 2.0, channel='ambient')

    "…smells a strange smell…"
    
    $ renpy.music.set_volume(0.15, 2.0, channel='ambient')
    
    # orange blaze. looks awful. [str]
    #scene expression Solid("#c46e2e")  # [str]
    #show n_vignette alpha # [str]
    #with dissolve # [str]
    
    "…and realises that the corridor is much brighter than it ought to be."
    
    $ renpy.music.set_volume(0.2, 2.0, channel='ambient')

    "She gasps, and rushes to the next room."

    "She tries to enter the blazing room, but the intense heat drives her back."

    "Her desk has collapsed into a pile of burning firewood, the floor around it blackened by the smoke."

    "The drawings on the wall curl away and disintegrate as they burn."

    "Smoke billows from the cracks in the drawing chests in puffs as the smouldering fire inside them draws air through the same cracks to survive."

    "Flames leap across the ceiling in mesmerising patterns."

    "The woman, too shocked to scream, falls over backwards, and can do nothing but sit and stare as her livelihood is consumed by the flames."

    "A picture frame, ablaze and losing its integrity, smashes to the floor."

    "The noise rouses the sleeping man, who enters the corridor."

    "Father" "What's going on… oh my god…"

    "As the pair stare into the inferno, the wall separating the study and the bedroom buckles and falls."

    $doublespeak ("Father", "Mother", "Hanako!")

    "The woman tries to get to her feet but slips."

    "The man, already standing, makes for the bedroom."

    "He opens the door, providing a second supply of air for the flames."

    "In an instant, they increase their brightness and intensity, and shimmering waves of heat separate the man and his daughter."

    "Their eyes meet, and the man knows what he must do."

    "Using his arms as a shield from the flames, he charges towards his daughter, scooping her up into his chest."

    "She screams an airless scream, but it is lost to the ever-increasing roar of the fire."

    "Even as he barrels through the short hallway to the house's front door, he feels the flames lick against his body, instantly blistering skin and vaporising hair."

    "As he fumbles with the lock, he feels the heat of the fire upon his back, and hears the structure of the house slowly staring to crumble."

    "Opening the door seems to take an eternity, and as soon as he has it open a fraction, the back draft of air slams the slab of wood into him and his daughter, sending them flying."

    "Enraged by the fresh air outside, the fire screams and reaches out towards its flesh-based enemy."

    "Clawing his protesting body along the floor, breathing in lungfuls of smoke, the man makes his way towards his daughter."

    "She is curled tightly around her plush rabbit, her flannel pyjamas blackened and covered in glowing trails of smouldering fire."

    "Her skin is lost amongst the ashes of her clothes; as charred as the walls around her."

    "The man summons the last of his strength, and shoves the small girl out through the door and onto the pristine white snow outside."
    
    $ renpy.music.set_volume(0.1, 4.0, channel='ambient')

    "He hears the hiss of the melting snow turning into steam at the door, but he can see that his daughter is now safe from the flames."
    
    "She stirs, and turns towards him, her tiny hand pushing through the snow towards him."
    
    scene white # [str]
    with dissolve # [str]
    
    stop ambient fadeout 4.0
    stop music fadeout 4.0

    "He smiles slightly as the walls finally buckle, sending the roof crashing down around him."

    window hide
    
    scene black
    with dissolve
    
    with Pause(1.0)
    
    return

label en_H30:

    #Obviously, this starts with a timeskip, and in darkness
    scene black # [str]
    with None # [str]
    #with Pause(3.0) # [str] (needed?)

    mystery "Are you awake, Hisao?"

    scene bg hosp_postop # [str]
    with Dissolve (1.5) # [str]
    play music music_rain fadein 2.0 # [str]

    "My groggy brain floats back into consciousness, and I slowly become aware of my surroundings once again."

    "A dull, pulsing pain emanates from my chest."

    "Fuzzy shapes resolve themselves into the faces of my parents and my doctor."

    hi "Huh?"

    "Dad" "Looks like you made it through okay then."

    hi "Made it through what?"

    "Doctor" "It's alright, you're probably still confused from the anaesthetic."

    "Doctor" "Minor confusion is common with long procedures like this."

    "I start to look from side to side, confirming that I am in the post-op room."

    hi "My pacemaker…?"

    "Doctor" "Is working fine."

    "Doctor" "I'm pleased to say that everything was a success."

    "Memories start to trickle back into my mind."

    "My parent's arrival at the hospital."

    "The doctor explaining to all of us exactly what was going to happen."

    "Hanako wishing me well through Lilly."

    "Not eating for a day before the surgery…"

    "Doctor" "So, how are you feeling?"

    hi "Hungry."

    "The doctor laughs a little."

    "Doctor" "Well then, let's get you some food, shall we?"

    "Doctor" "Nurse, could you please take Hisao here back to his room?"

    "The nurse nods, and summons some orderlies to wheel my bed back to my room."

    scene bg hosp_hallway # [str]
    with locationchange # [str]
    
    "As I watch the fluorescent lights whiz by overhead, I as my parents a question."

    hi "How long before they'll let me out?"

    "Dad" "Well, they wanted to keep you overnight to make sure that you were fine, but you should be fine to go tomorrow…"

    "Tomorrow."

    "The thought of being able to leave sets me ablaze."

    "Finally, I'll be free."

    hi "And, how long are you up here for?"

    "Mom" "Unfortunately I have to return to work on Thursday, so we'll have to leave tomorrow."

    "I feel a twinge of regret."

    "Not at the fact that they are leaving me, but that it is not sooner."

    "Has living away from home really changed me this much?"

    scene bg hosp_room2 # [str]
    with locationchange # [str]
    
    "We arrive in my room, where the nurse already has a tray of food waiting for me."

    "There's another thing I can't wait to get away from; hospital food."

    "Seventeen specifically designed menus that will cater to your body's needs without so much has disturbing your sense of taste."

    "Yes, seventeen."

    "I've been counting."

    "If I'm not mistaken, today is “Pale brown stew with bits of carrot.”"

    "Bummer. I really could have done with some “Thick white sauce on chicken.”"

    "No matter. I wolf down the food with vigour."

    "Dad" "Wow, you really were hungry."

    hi "I haven't eaten in over a day."

    "Dad" "Oh, yeah. That."

    "Dad" "So, how're you feeling?"

    hi "Alright, I guess. My chest hurts a bit, but apart from that…"

    "Dad" "That'll probably get worse as the painkillers wear off."

    "Dad" "I remember having my appendix out. I thought I was fine for the first half hour and then BAM."

    "Dad" "I could barely stand up."

    "Once again, I am reminded of how little I have in common with my parents now."

    "We continue to trade small talk until a passing nurse reminds us of the end of visiting hours."

    "Dad" "Well, we'll be off now."

    "Mom" "Take care, love."

    hi "I will. Thanks for coming up, it means a lot."

    "My parents give me the standard hospital smile, and then leave for their hotel."

    "As soon as they are out of sight, I unbutton my gown slightly to inspect my throbbing chest."

    "A bright red scar bisects my newly-healed ribcage, bound together by a number of stitches."

    #Or do you guys use scutches instead of stitches?

    "There's a little bruising where they must have moved my ribs around, but it's nothing compared to the damage that Hanako wrought on me."

    "Hanako."

    "Now that I'm better, it's only a matter of days before I'm allowed to see her."

    "I wonder if she's changed?"

    "Lilly mentioned that she wasn't quite herself, but I can't really believe that."

    "Or is it that I don't want to believe that?"

    "I flop back onto my familiar bed, once again greeted by my roof-stains."

    "Still feeling the effects of the anaesthetics, I blink twice, and fall asleep."

    stop music fadeout 2.0 # [str]

    #timeskip/eye close thing.
    window hide # [str]
    scene black # [str]
    with shuteye # [str]
    with Pause(1.0) # [str]

    scene bg hosp_room2 # [str]
    with openeye # [str]

    play music music_daily fadein 4.0 # [str]

    "Doctor" "Come on now, no need to sleep in this late…"

    "My doctor wakes me on his morning rounds for my checkup."

    hi "What's the bad news?"

    "The doctor flips through my chart and tuts a few times."

    "Doctor" "Well, it looks like we might be able to get you some fresh air, after all."

    "I can feel the smile creep across my face."

    hi "Does that mean…?"

    "Doctor" "Well, your vitals are fine, and you've passed all the post-op checks."

    "Doctor" "We can remove your stitches as an outpatient, and, let's face it, you've taken up a valuable bed for far too long."

    "He gives me a cheeky smile, and places my charts back in the holder at the end of my bed."

    "Doctor" "I'll just go clear this with the Chief of Medicine and start the discharge paperwork."

    "He grabs my shoulder in a friendly manner."

    "Doctor" "You're a tough kid. You'll do fine, mark my words."

    "He gives me a reassuring shake and heads out the door."

    "I can hardly believe that I'm about to go home."

    "Well, back to the school at least."

    "I know full well what awaits me there, too."

    "My teachers made it blatantly obvious that as soon as I was well, then I'd have to sit my tests."

    "Although they have afforded me a week of study to prepare."

    "I guess they're used to this kind of thing."

    "The doctor doesn't take long in returning to me."

    "Doctor" "Well, the Chief isn't totally happy about letting you go right now, but at least you're close by."

    "Doctor" "And we've briefed the nurse at your school about looking out for you."

    "Doctor" "If you can promise to report to him twice daily for the first week I think we can let you go."

    hi "If it means finally going home, I think I'd jump through flaming hoops."

    "Doctor" "Sounds good to me."

    "Doctor" "But, there's just one last thing before I can let you go."

    hi "What? I'll do anything!"

    "The doctor smirks."

    "Doctor" "You have a visitor."

    stop music fadeout 2.0 # [str]

    "The doctor walks out of the door, and talks to someone just out of view."

    "He takes a step back, and motions to let someone into the room."

    #A music change would be nice here. Something music-boxy.

    "It feels like my heart stops."

    show hanabad emb_downtimid_sun # [str] (yay new sprites!)
    with charaenter # [str]
    
    play music music_twinkle fadein 2.0 # [str]

    "A fragile figure appears in the doorway, her hands clamped together near her waist, her head cowed."

    "Taking small steps, she walks towards my bed."

    hi "Hanako…"

    "My voice is barely a whisper as I call her name."

    "I throw back my bed sheets and leap to my feet, ignoring the ache in my chest."

    hi "Hanako? It's really you, isn't it?"

    "I can hold back no longer."
    
    show hanabad emb_downsad_sun_close # [str]
    with charachange # [str]
    
    "I race across the room and gather Hanako's frame into my arms, embracing her in a hug that threatens to re-open my scar."

    hi "Hanako, I've missed you so much."

    hi "How are you? You look thinner? Did they treat you well?"

    "I release Hanako and hold her at arms length."

    hi "Hanako? Is something the matter?"

    "Slowly and purposefully, Hanako raises her head to look me in the eye."

    show hanabad emb_sad_sun # [str]
    with charachange # [str]
    
    $ renpy.music.set_volume(0.0, .5, channel="music") # [str]

    "Only now do I notice that she's wearing the same clothes that she wore on that fateful day."

    "Only now do I realise that she looks as if she hasn't eaten in a week."

    "Only now do I realise that her hair is unkempt, her usually perfect fringe hanging in tatters over her face."

    "Only now do I see her eyes, distant and empty."

    ha "Hisao… you're alright…"

    "Her words are forced, her voice deadpan."

    "Just what is going on here?"

    show hanabad emb_downtimid_sun # [str]
    with charachange # [str]

    hi "Hanako, what's the matter? Please, what's going on?"

    ha "Well… I suppose you know now, don't you?"

    ha "They told me they told you everything."

    ha "So I suppose that means you know everything."

    "Hanako talks in her monotonous voice, gazing lazily at my face."

    hi "Hanako, what's going on here? What did they do to you?"

    ha "Oh, don't mind me."

    ha "I'm just tired."

    ha "They're trying a new medication on me, and for some reason I'm always tired."

    "I can barely believe the sight before my eyes."

    "Hanako is a shadow of her former self."

    "Once again, I pull Hanako into my embrace."

    hi "That's okay. You can be tired as long as you want."

    hi "I'm free now, so I won't ever leave you again."

    "Those words act like some trigger, and Hanako gently wraps her arms around my body."

    ha "I'm free too."

    ha "So long as I take my medication."

    "Her words sound like they've been drilled into her head."

    "From the corridor, I hear a familiar noise."

    hi "Lilly?"

    show hanabad emb_timid_sun # [str]
    with charachange # [str]

    ha "Oh, Lilly's here?"
    
    $ renpy.music.set_volume(1.0, 2.0, channel="music") # [str]
    
    show hanabad emb_downtimid_sun at twoleft # [str]
    with charamove # [str]

    show lilly cane_surprised_cas at tworight # [str]
    with charamove # [str]

    li "My my, I didn't expect you to get here so soon, Hanako."

    li "I take it that Hanako has told you the good news, Hisao?"

    hi "Yes, I just heard now."

    hi "And I get discharged today, so we get ot go home together."

    #lilly ufufufufu
    show lilly cane_smile_cas at tworight # [str]
    with charachange # [str]

    li "You make it sound coincidental, Hisao."

    li "However, Hanako insisted that she was to stay in the hospital as long as you did."

    li "Because she wanted to go home with you."

    "I look back at Hanako, who nods slightly."

    ha "I thought that I should at least do that much."

    ha "You came here because of me…"

    hi "Now, don't be silly! From what I heard the only reason I'm alive is because of you…"

    ha "But… I made you chase me…"

    ha "It's my fault…"

    "I squeeze Hanako with my whole body, and feel the wound in my chest protest against the movement."

    hi "Don't be silly. None of this is your fault."

    hi "Now, I'll just get dressed and we'll be off."

    hide lilly # [str]
    hide hanabad # [str]
    with charaexit # [str]

    "True to my word, I get dressed and meet the girls in the hallway."

    scene bg hosp_hallway # [str]
    with locationchange # [str]

    "There, I find them talking to my parents and my doctor."

    "Dad" "All set?"

    hi "Yes. Um, Mom, Dad, this is…"

    "My dad gives me a thump on the back."

    "Dad" "Lilly here explained everything to us."

    "Dad" "This is the girl that saved you, right?"

    "Dad" "And now we've finally met her."

    "I look down at Hanako, sitting in one of the seats in the corridor."

    "Despite my father's energetic reaction, she simply sits there, her gaze downcast."

    "Dad" "Come on, I'll give you all a lift back to the school."

    "Dad" "I've already signed all the papers that we need to, so you're good to go."

    "Like an excited sheep dog, my father herds us all into the waiting hire car in the Hospital's car park."

    scene bg hosp_ext # [str]
    with locationchange # [str]
    stop music fadeout 2.0 # [str]
    
    "I take one last look at the hospital, trying to search out my window."

    "I haven't seen it from the outside yet, but it's just like every other hospital."

    "Banks upon banks of bleak windows set into a grey concrete building."

    "How long will it be before I am carted back here in yet another ambulance?"

    "Sensing my thoughts, my father pushes me into the waiting back seat of the car."

    "Dad" "Come on, you just spent a month here. Do you really need to look at it any more?"

    hi "You're right. Let's go."

    stop music fadeout 2.0 # [str]

    "The car's engine roars into life, and I slowly watch the hospital disappear into the distance, my hand gently wrapped around Hanako's."

    window hide # [str]
    scene black # [str]
    with dissolve # [str]
    
    with Pause(2.0) # [str]
#
#    return
#
#label en_H31:
#    with Pause(0.1) # [str]
    
    #BG: Dormroom
    scene bg school_dormhisao_ss # should be not _ni? [str]
    with shorttimeskip # Dissolve (1.5) # [str]

    "My parents seem to take forever to leave, fussing over me at every step."

    "Hanako barely says a word, despite my father's bet attempts at goading her on."

    "But, unlike her usual self, she didn't flinch, nor retreat."

    "She just sat there, slowly sipping her drink, whilst my parents fussed over her."

    "Lilly also attracted a fair deal of attention, especially when she accidentally told them that she visited me every day."

    "Of course, she responded in the most refined manner, which impressed my parents no end."

    "She even bowed to them as they drove off in the hire car."

    "Thankfully she never mentioned her parents, otherwise I'd never hear the end of it."

    "I can imagine my parents trying to arrange a marriage after hearing of something like that."

    "Together, Lilly and I put Hanako to bed, who seems barely interested in either of us, and falls straight asleep."

    "Tomorrow, both of us have a meeting with Mutou to discuss how we are going to make up for the exams that we missed."

    "But for now, I'm looking forward to sleeping in my own bed, in my own room."

    "A thin layer of dust covers everything in my room, and the faint smell of mildew floats on the air."

    "Everything is exactly as I left it on the morning the three of us set out for the Shanghai."

    "Dirty clothes, piled in a heap next to the door. My laptop's screensaver gently changing colours in the dying sunlight."

    "But the one thing that I am interested in is my bed; the covers still thrown away from my mad scramble to get up."

    "As I change into my bedclothes and lay down, I feel the cool mattress against my skin."

    "It's strange, for the past month my bed has almost constantly been warmed by my body."

    "This cool bed is a bit of a novelty."

    "I pull the crumpled sheets over my body and fall asleep."

    scene black # [str]
    with shuteye # [str]

    with Pause(1.5) # [str]

    return

label en_H31:
    with Pause(0.1) # [str]
    #sleep timeskip
    
    play sound sfx_alarmclock # [str]

    scene bg school_dormhisao # [str]
    with openeye # [str]
    #with locationchange # [str]

    play music music_dreamy fadein 0.3 # [str]

    "For the first time in weeks, I am woken by my alarm."

    "I dress in my uniform and make my way to the girl's dorm."

    scene bg school_dormext_full # [str]
    with locationchange # [str]

    "The rest of the students are preparing for the final day of their exams, or have already started their holidays."

    "As a result, the usually lively dorm area feels more like a ghost town."

    "Our meeting with Mutou isn't until after the first exam has started, so I simply wait for Hanako outside her dorm."

    "The school's uniform feels constricting after a month of hospital gowns."

    "Even now, only a few minutes into the day, I can see dots of red and yellow seeping through my shirt where it rubs against my scar."

    "I guess I'll have to ask my mom about how to remove stains like these…"

    show hanabad emb_downdetermined # [str]
    with charaenter # [str]

    "Eventually, Hanako emerges from the dorm, her eyes bloodshot, her hair in a mess."

    hi "Good morning, Hanako!"

    "I try to put on a cheery face for her, knowing that she isn't feeling too well."

    ha "Morning."

    hide hanabad # [str]
    with charaexit # [str]

    "Without waiting for me, she starts walking towards the main building."

    "I step out to catch up with her, but her pace is too much for me to keep up with her."

    scene bg school_hallway3 # [str]
    with locationchange # [str]
    stop music fadeout 3.5 #2.0 # [str] (longer!)

    "Only when she stops in front of the door to the teacher's office do I mange to reach her side."
    
    show hanabad emb_downdetermined at tworight # [str]
    with charaenter # [str]
    
    "My panting gives away the fact that I have done very little exercise in recent history."

    hi "That's some pace you've got there."

    ha "I just want to get this done with an go home.{w=0.4}{nw}" # [str] (insta-linechange!)

    play sound sfx_doorknock2 # [str]
    
    "Without giving me time to reply, she gently knocks on the door."

    mu "Come in."

    "Hanako just stands in front of the door, her hand still raised, as if she were going to knock again."

    "I step in close to her, and slide the door open."

    play sound sfx_dooropen # [str]
    
    scene bg school_scienceroom # [str]
    with locationchange # [str]
    play music music_another fadein 0.3 # [str]

    show muto normal # [str]
    with charaenter # [str]

    mu "Ah, Nakai, Ikezawa, you made it. Please, take a seat."

    "I make my way into the room, and Hanako follows shortly after."

    mu "Now, I realise that both of you have had a rough time in the past few weeks, so I'm here to help you."

    mu "We'll let you sit your exams individually in a week's time."

    mu "Of course, they won't be the same as the one the others took, so don't try and cheat like that!"
    
    show muto smile # [str]
    with charaenter # [str]
    
    "Mutou lets out an unconvincing laugh, which he quickly covers up after seeing our lack of reaction."

    "Seeing that his attempt at a joke has failed, he hands Hanako and I a thick stack of paper."

    mu "Well then, here is the material you'll be tested on."

    mu "I'll be in this office every day from ten to seven if you need me."

    mu "In that sense, I guess you're luckier than your normal student; you get to study with a teacher."

    mu "Well then, any questions?"

    hi "I think I've got you. How about you, Hanako?"

    "Hanako looks up from the floor long enough to shake her head, then looks back at the floor."

    mu "Well then, that's pretty easy."

    mu "The timetable for your exams is on the second page there. Don't be late."

    mu "Oh, and Nakai, I'm expecting great things from you on the science exam."

    mu "Good luck."

    stop music fadeout 1.4 # [str]
    
    hide muto # [str]
    with charaexit # [str]
    
    "Mutou turns back to his overflowing desk, and Hanako stands up, making her way for the door."

    "This time, however, I'm expecting her burst of speed, and at least manage to keep pace with her on the way back to the dorms."

    scene bg school_dormext_full # [str]
    with locationchange # [str]

    play music music_hanako fadein 0.1 # [str] (maybe instaplay?)

    "Before she opens the door to the girls' dorm, I grab Hanako's hand."
    
    show hanabad def_worry_close # [str]
    with charaenter # [str]
   
    ha "Huh?"

    hi "Hey, I was wondering…"

    hi "Do you want to come to my room and we can start looking over these notes?"

    hi "There's a lot of them."

    "Hanako looks at me with her lifeless eyes."
    
    show hanabad emb_downtimid_close # [str]
    with charachange # [str]

    ha "Maybe later."

    ha "I'm going to bed."

    hi "But you just got up?"
    
    show hanabad emb_timid_close # [str]
    with charachange # [str]
    
    "For a second, a glimmer of life flashes across Hanako's face."
    
    show hanabad emb_downtimid_close # [str]
    with charachange # [str]
    
    "It vanishes almost as quickly as it appeared."

    ha "I… I'm sorry."

    ha "I'm really tired."

    ha "Maybe later…"

    "For some reason, I feel that this is some “real” Hanako talking now, and I can't help by sympathise with her."

    hi "Sure. You rest all you need to; I'll be in my room if you need me."

    "I lean in and kiss Hanako on the cheek."

    "She doesn't react, save from muttering on the edge of audibility:"

    ha "Please don't…"

    hide hanabad # [str]
    with charaexit # [str]

    "Without saying another word, she enters the girl's dorm, and vanishes."

    "Shocked, I walk back to my room, and start flicking through the wad of paper Mutou gave me."

    stop music fadeout 2.0 # [str]
    #timeskip
    #with Pause(1.0)

    scene bg school_dormhisao # [str]
    with shorttimeskip # [str]

    "After working all morning, I have barely scraped the surface of Mutou's notes."

    "It's not that the revision problems are hard, but I can't get my mind of Hanako."

    "Lilly and I decided that leaving her in the care of her doctors was the right thing to do, but this seems a little extreme."

    "I drop my pencil, and decide to go for a walk."

    "Besides, I have to check in with the nurse at some point today."

    #BG change to nurse's office.
    scene bg school_nurseoffice # [str]
    with shorttimeskip # [str]
    play music music_nurse fadein 0.2 # [str]

    show nurse neutral # [str]
    with charaenter # [str]

    nk "Ah, Hisao. I've been expecting you."

    "The nurse reaches across his desk and opens a large, cream folder."

    nk "Come on in, take a seat. Let's have a chat."

    nk "How's life?"

    hi "I won't lie. I've been better."

    #smile
    show nurse grin # [str]
    with charachange # [str]

    nk "Well, I kind of expected that."

    nk "I can see from your shirt that you're still only fresh from the chopping block."

    nk "Mind if I take a look?"

    "I oblige the nurse and unbutton my shirt."

    show nurse concern # [str]
    with charachange # [str]

    "He turns the desk lamp to illuminate my chest, and examines the scar thoroughly."

    nk "Hmm. I guess the lead surgeon went home early and left this to the new guy…"

    hi "What?!"

    nk "Oh, nothing to worry about, but it's not the neatest sewing I've ever seen."

    nk "But that's fine, I'll heal in no time."

    nk "How are you feeling otherwise?"

    hi "Good. I was a bit puffed after a quick walk, but I think that's just from lack of exercise."

    nk "That's to be expected."

    nk "You're not feeling anything strange, like extra heartbeats or muscle spasms, are you?"

    hi "Not at all."

    nk "No trouble sleeping last night?"

    hi "None whatsoever."

    nk "Decreased sexual performance?"

    hi "What?!"

    #Nurse laugh
    show nurse grin # [str]
    with charachange # [str]

    nk "Sorry, couldn't help myself."

    nk "Anyway, you seem fine. Check back in with me after dinner and I'll take your vitals for your doctor."

    nk "Is there anything else you'd like to ask me?"

    "For a moment I pause, but decide to ask anyway."

    hi "Well, I do, but it's not about me…"

    #Nurse "knowing look" or srs bsns. Whatever we have.
    show nurse concern # [str]
    with charachange # [str]

    nk "Ah. Let me guess; Hanako?"

    "I nod, not quite knowing how to ask him what I want to know."

    "Thankfully, he seems to see straight through me."

    nk "It's nothing to worry about."

    nk "Her doctors have prescribed her new medication to try and level her out a little."

    nk "Of course, with a condition such as hers, it takes some time to fine-tune the dosage."

    nk "She'll be back to normal before you know it."

    hi "Thanks. It's just… a little hard."

    nk "I know. Mental illness is never easy, but we all have to be strong, not only for Hanako, but for each other."

    nk "How can we expect her to become stable if all those around her are losing their minds as well?"

    "The nurse's words strike something in my core."

    "Even if she doesn't look it, Hanako is counting on me."

    "I've got to be there for her when she needs me, even if that means just being silently by her side."

    nk "Wait, before you go, let me give you something for that scar…"

    "The nurse hands me a box of children's band-aids, this time shaped like unicorns."

    hi "Thanks. You enjoy doing this, don't you?"

    #nurse smile
    show nurse fabulous # [str]
    with charachange # [str]

    nk "Whatever makes you think that?"
    
    stop music fadeout 2.0 # [str]

    #BG change to room
    scene bg school_dormhisao # [str]
    with shorttimeskip # [str]

    show hanabad emb_downdetermined at twoleft # [str]
    with charaenter # [str]
    
    "I open the door to my room, and see a figure sitting at my desk, slowly turning the pages of revision problems that I finished this morning."

    hi "Hanako, are you feeling better now?"

    ha "A little."

    play music music_hanakohscene fadein 0.1 # [str]

    "She says that, but she looks just as dishevelled as she did this morning."

    "No, she looks even worse. She obviously slept in her uniform, it's usually loose fit now creased all over."

    hi "Did you come here to study?"

    ha "Yes, and to apologise."

    hi "Apologise? For what?"

    ha "This morning."
    
    hide hanabad # [str]
    with charaexit # [str]
    # check if it's working as i want! [str]
    
    show hanabad emb_downtimid_close # [str]
    with charaenter # [str]
    
    "I walk over to Hanako, dropping the nurse's novelty band-aids on my bed as I pass it."

    hi "Don't worry about it."

    hi "I'm always going to be here for you, just like I promised."

    hi "I'll wait forever, if I have to."

    ha "What will you wait for?"
    
    show hanabad emb_timid_close # [str]
    with charachange # [str]
    
    "Hanako looks at me, bluntly."

    hi "I… er… I'll wait for you?"

    "The lack of conviction in my words only serves to make me seem more pathetic."

    "This isn't how I imagined “being there for her.”"

    "Hanako sighs, and drops the notes onto my desk."
    
    show hanabad def_strain_close # [str]
    with charachange # [str]
    
    ha "That's it, isn't it?"

    ha "You'll wait for me."

    ha "Because that's what you want, isn't it?"
    
    show hanabad def_angry_close # [str]
    with charachange # [str]
    with Pause(0.5) # [str]
    
    ha "Me."

    "I try to read Hanako's face, but her eyes tell me nothing."

    "If anything, they look bored."

    #I can't believe I'm about to do this, but I sincerely hope I do it right.

    hi "T…that's not right."
    
    show hanabad def_strain_close # [str]
    with charachange # [str]
    
    "Hanako stands up purposefully, drawing close to me."

    ha "Isn't it?"

    ha "Then tell me, do you love me?"

    "My throat swells up, and I can barely force out my words."

    hi "Yes. Yes, I love you, Hanako."
    
    show hanabad emb_downtimid_close # [str]
    with charachange # [str]
    
    ha "Why?"

    "She doesn't ask the question accusingly, nor angrily."

    "It's more a statement of fact than a question."

    "And… it's something I can't answer."

    hi "I… don't know."

    ha "Huh."

    "She takes a deep breath, and exhales slowly."
    
    ha "My doctors told me that I should feel more free to express myself."

    ha "They put me on these medications to relieve my anxiety."

    ha "And… I can feel that. It's like… nothing can really move me anymore."

    hi "It's okay Hanako… I spoke to the nurse about you just then and he said this is normal…"

    #Hanako almost angry or something
    show hanabad def_angry_close # [str]
    with charachange # [str]
    
    ha "Normal?"

    ha "So I guess this is what normal is like then."
    
    # that looks like a bit of overkill, but it looks kinda good [str]
    hide hanabad # [str]
    with charaexit # [str]
    show hanabad def_strain # [str]
    with charaenter # [str]
    show hanabad def_strain at centersit # [str]
    with charamove_faster #charafast #charamove # [str]
    
    "Hanako sits on my bed."
    
    ha "You still haven't answered my question."

    hi "Huh?"

    ha "What it is that you'll wait for."

    ha "I guess I should save you the trouble."

    "Without warning, and in slow movements, Hanako unbuttons her shirt."

    # that's kind of a hack, i guess
    stop music fadeout 4.0 # [str]
    play music music_hanakofinal fadein 4.0 # [str]

    play sound sfx_whiteout # [str]
    
    hide hanabad # [str]
    with None # [str] (instahide)
    
    # I REALLY HOPE THIS WILL WORK [str] (and it actually does!)
    image ev hanako_scars_d = 'event/hanako_scars.jpg'
    scene ev hanako_scars_d # [str]
    with whiteout # [str]

    "It falls to the bed, soundlessly, revealing her chest and torso."

    "Her right side is almost completely scarred, the grafted skin stretched like an ill-fitting sheet."

    "In a state of shock, I can do nothing as she shucks off her dress, kicking it to the floor."

    ha "This is what you're waiting for, isn't it?"

    ha "I've seen it. The way you look at me."

    ha "Well, now you can see it for yourself."

    hi "H…Hanako… why?"

    "I am frozen to the spot in shock."

    "Hanako, usually too shy to even talk, now sits on my bed, naked save her panties, bra, and socks."

    ha "Is this not what you were waiting for?"

    ha "Is this not what lovers do?"

    "My mouth flaps in the air, desperately trying to form words that I know will never come."

    "Hanako lies back on my bed, and my heart races."

    "I'm not sure if it's my imagination, but I think I can feel the pacemaker starting to reel my hard back into line."

    "Or maybe it's the odd mix of emotions running through my mind."

    ha "You said you loved me, right?"

    #ha "Is this not what you've been waiting for?"
    
    window hide # [str]
    
    return

label en_choiceH31:
    menu:
    #Choice point.
    # 1- Advance
    # 2- Tell her to get dressed.
    #1 leads to the below. 2 will be covered in H32
    # both are bad ideas.
    # Also, I lack the eloquence to come up with good labels for the choices.
        with menueffect
        
        ha "Is this not what you've been waiting for?"

        "Advance.":
            return m1
         
        "Tell her to get dressed.":
            return m2

label en_H31a:

    "Instinct spurs my legs forward, and I soon find myself straddling Hanako."

    "I slide my hands over her skin, feeling the change between her natural skin and the grafted tissue."

    # new stuff, yay! [str]
    scene evh hanako_bed_boobs_neutral_d # [str]
    with whiteout # [str]
    
    "Instinct and lust take over, and I feel myself cupping her breast with one hand whilst removing my pants with the other."

    "Hanako's eyes are closed, but otherwise she wears the face of someone waiting for a bus."

    "It's a necessary inconvenience for her."

    "In the back of my mind, I can hear myself screaming at me to stop."

    "This isn't how it's supposed to happen."

    "But it's too late."
    
    scene evh hanako_missionary_underwear_neutral_d # [str]
    with whiteout # [str]
    
    "My lust has taken control of my faculties, and I feel myself tearing aside her panties to clear a path for my member."
    
    scene evh hanako_missionary_neutral_d # [str]
    with locationchange # [str]
    
    "As I enter her, I lean down and kiss her lips."

    "She doesn't even flinch, and I realise that I may as well have kissed a corpse."

    "As I thrust into her, I watch her face."

    "No reaction."

    "Wait…"
    
    scene evh hanako_missionary_hate_d # [str]
    with locationchange # [str]
    
    "Her eyes snap open, regarding me with a mixture of disgust and contempt."

    #A reference of the look I'm looking for:
    # http://i8.photobucket.com/albums/a37/ko … lolwut.jpg

    ha "I was right."

    ha "This is what you were waiting for."

    ha "Are you done yet?"

    "The voice in my head screams, and my body convulses in abject terror."

    "Somehow, I manage to avoid collapsing onto Hanako's listless frame, and stand up next to my bed."
    
    scene bg school_dormhisao # [str]
    with locationchange # [str]
    
    show hanagown nude_disgust_close # [str]
    with charaenter # [str]
    
    "Her empty eyes are locked onto mine, following me wherever I turn."

    "I try to step backwards, only to trip on my half-removed pants."

    "I feel my world tumble rapidly, but Hanako's gaze never leaves mine."

    play sound sfx_crunchydeath # [str]
    scene bg misc_ceiling # [str]
    with vpunch # [str]
    
    "My neck connects with the corner of the desk with a sickening crack."
    
    
    "In an instant, I can no longer feel my body."
    
    #Use this to do a transition that lasts over multiple lines of text
    #I've heard that it doesn't work with filters, so you'll have to implement the im.MatrixColor manually
    #This is taken from Rin's route, scene R34
    #Originally done by Kelper
 
    # anim.TransitionAnimation( pre, ???, function, post ) [str]
    image fortheloveofgodcomeonworkWORKALREADY1 = anim.TransitionAnimation("bgs/misc_ceiling.jpg", 0.5, Dissolve(6.0), im.MatrixColor('bgs/misc_ceiling.jpg', im.matrix.tint(0.4, 0.4, 0.4) * (im.matrix.saturation(0.01))))
    show fortheloveofgodcomeonworkWORKALREADY1
    
    # gosh, i ever though that making a simple dissolve from regular to filtered bg can be THIS problematic [str]
    
    "I watch as it limply tumbles to the ground, more an assortment of limbs than a living organism."
    
    # and his world turns all gray... [str]
    #image bg ceiling_gray = death('bgs/misc_ceiling.jpg') # [str] 
    #show bg misc_ceiling_death # [str]
    #$ renpy.transition(Dissolve(6.0), layer='master') # [str]
    #with Dissolve(6.0) # [str]
    #show hanakoa4_deathbg # [str]
    #with Dissolve(6.0) # [str]
    

    
    "Eventually, the macarbe dance of my body comes to an end, my head lying at an impossible angle."
    
    "Hanako lies on the bed, dead still, her face showing no emotion whatsoever."
    
    "My face feels cold; I'm probably only being supported by the small pacemaker in my chest now."

    "As my life drains away, Hanako does naught but watch my palloured face."
    
    show passoutOP1 # [str]
    with None # [str]
    
    "The world slowly loses color, the room turning from shades of grey to black."
    
    "Just before the last glimmer of light blinks out, I hear a single word at the edge of my dying hearing."
    
    ha "Disgusting."

    window hide # [str]
    
    scene black
    with None

    #Bad end. You are now dead.
    #There's my true feelings, TC.
    #How do you like me now, eh?

    #Also, please let me know if this isn't depressing enough. It's rather late right now.
    #I'm more than willing to edit the shit out of this scene for maximum effect.
    #PS: Sorry weee. No-one should have to draw this kind of thing.
    
    
    return

label en_end_hanakobad2:
    # Hanako bad end 2, after H31a
    scene endscreen with dissolve #black with dissolve # [str]
    with Pause(1.5) # [str]
    
    scene black with dissolve # [str]
    centered "~ hanako bad end 2 ~" with dissolve
    stop music fadeout 2.0 # [str]
    
    return

label en_H32:

    "My body remains frozen, but a single word manages to escape my lips."

    hi "No…"

    "Once again, a flicker of recognition passes across Hanako's face."

    ha "No…?"

    "She raises her body up onto her elbows, her hair flowing off her body like a waterfall."

    "My mind, somehow inspired by my single word, manages to catch up with my flapping mouth."

    hi "Not like this…"

    hi "Hanako, I love you, but you're still not well."

    hi "So please… please don't do this."

    "My knee buckles, and I lurch forwards."

    "Shakily, I pick up her short, green dress from the floor, still warm from the contact with her body."

    hi "Please… get dressed."

    "I hold out the dress with a quivering hand, and for a moment, neither of us can do anything but look at each other's ashen faces."

    "Eventually, Hanako sighs, and takes the dress from me."

    scene bg school_dormhisao # [str]
    with locationchange # [str]

    "I watch in shock as she dresses silently."
    
    show hanabad emb_downtimid_cry # [str]
    with charaenter # [str]
    
    "She teases her hair into a semblance of its usual glory, and moves to leave my room."

    "Her head is bowed lower than I've ever seen it before, and as she passes me, she whispers in a voice full of tears."
    
    show hanabad emb_downtimid_cry at rightedge # [str]
    with charamove_faster # [str]
    
    ha "sorry"

    #sic, no punctuation/caps.

    hide hanabad # [str]
    with charaexit # [str]
    
    "She leaves at a pace somewhere between walking and running, rapidly disappearing beyond the door jamb."

    stop music fadeout 3.0 # [str] (not sure if appropriate, check!)

    scene bg school_dormhallway # [str]
    with locationchange # [str]

    "It takes me a moment to summon the courage to give chase, but she is nowhere to be seen."

    scene bg school_dormext_full # [str]
    with locationchange # [str]

    "Depressed, I walk to the girl's dorm."

    scene bg school_girlsdormhall # [str]
    with locationchange # [str]

    "Hanako isn't here."

    "As I stand in her doorway, dejected, Lilly approaches me."
    
    play sound sfx_dooropen # [str]
    
    show lilly basic_surprised at leftoff # [str]
    with charaenter # [str]
    
    li "Hisao? Is something the matter?"

    hi "It's Hanako. She's… not Hanako anymore."
    
    show lilly basic_reminisce at leftoff # [str]
    with charachange # [str]
    
    li "I… I think we should have a talk, Hisao."

    scene bg school_dormlilly # [str]
    with locationchange # [str]

    "Lilly leads me into her room, and I close the door behind us."

    "My body, still in some state of shock, goes through the motions of preparing tea in Lilly's dainty set."

    "Once we are settled with a small cup in front of us, Lilly begins to speak."
    
    show lilly basic_reminisce at centersitlow # [str]
    with charaenter # [str]
    
    li "I… I must apologise for not warning you."

    li "Hanako hasn't been the same lately."

    hi "But, that's just the medication, right?"

    hi "The nurse said she'd get better…"

    hi "Right…?"

    show lilly basic_sad # [str]
    with charachange # [str]
    
    "The look on Lilly's face doesn't fill me with confidence."

    play music music_sadness fadein 0.1 # [str] (hope it's not too late)

    li "I've been speaking with her doctors for some time now, and they warned me that this may happen."

    li "Usually, the patient is strong enough to come back on their own."

    li "But sometimes…"

    "Lilly chokes, unable to continue."

    hi "That can't be right!"

    hi "She's still Hanako!"

    "Lilly reaches out across the table, her hand colliding with my chest."
    
    show lilly basic_reminisce_close # [str]
    with charachange # [str]
    
    "She slides it up to my shoulder, the contact silencing me."

    li "Sometimes, people don't come back."

    li "The strain on their hearts is just too great."

    li "Our Hanako…"

    "Crystal tears start to flow from the corners of Lilly's sightless eyes."
    
    show lilly basic_sad_close at centersitlow # [str]
    with charachange # [str]
    
    li "… may never come back."

    "Hanako's zombie-like eyes flash into my memory, lying on my bed, her pale skin exposed to the world."

    "Through her tears, Lilly continues."

    li "The doctors… her doctors…"

    li "…they said that the medications that she is on will keep her “balanced” for as long as required."

    hi "No… no that can't be right."

    "Lilly's grip on my shoulder tightens."

    li "Please, Hisao, you have to understand."

    li "We need to be strong for her."

    show lilly basic_surprised # [str]
    with charachange # [str]
    
    "In a fit of confused rage, I knock away Lilly's hand."
    
    hi "How we be strong for her if it's not even her!"

    hi "Just how long will we be waiting for?"

    hi "The Hanako I just saw was not Hanako. She was barely even a person."

    li "Hisao…"
    
    show lilly basic_sad # [str]
    with charachange # [str]
    
    hi "Enough!"

    hi "It's their fault."

    hi "Hanako would never be like she is now."

    hi "It's all the doctor's fault!"

    #Lilly pleading
    show lilly basic_oops at centersit # [str]
    with charamove # [str]
    
    "Lilly raises up on her knees, her hand desperately searching out for me."

    li "Hisao, please!"

    li "I know this is hard, but we have to trust them!"

    li "We promised, remember!"

    "Our promise in my small hospital room seems so far away now."

    "I wonder, did I make the wrong choice?"

    hi "No… we promised to do what was right for Hanako."

    hi "This… this isn't right."

    hi "I'm going to put a stop to this."

    "Lilly tries to stand up, but in her haste, she trips on the small table, crashing over it."
    
    # move before text? [str]
    with vpunch # [str]
    play sound sfx_impact2 # [str]
    show lilly basic_oops at Position(yanchor=0.0, ypos=1.75) # [str] (should work?)
    with charamove # [str]
    
    hide lilly # [str]
    with charaexit # [str] (maybe None?)
    
    "A shower of broken china rains down upon the room and the girl sprawled across its floor."

    "It takes every last drop of my enraged determination to turn away from her."

    li "Hisao… please…"

    scene bg school_girlsdormhall # [str]
    with locationchange # [str]
    play sound "sfx/doorslam.ogg" # [str] (meh)
    
    "I exit her room, closing out her pleading whimpers with her door."

    scene bg school_dormhanako at bgright # [str]
    with locationchange # [str]
    play sound sfx_dooropen # [str]
    
    "As I enter Hanako's room, I notice that she still hasn't returned."

    "Good."

    "This makes it easier to do what I have to do."

    "I open her drawers with no sense of order, throwing clothes, study tools and underwear about the undecorated room."

    "Drawer after drawer, I become like a demon, tearing apart Hanako's room."

    "My vision blurs, and I wipe my eyes with the sleeve of my shirt."

    "It leaves my face tear-stained."

    "Eventually, I find what I am looking for; a small, white plastic bottle."
    
    show pills # [str]
    with dissolve
    
    hi "Lithium Carbonate…"

    #In case you're wondering, it's the stuff Stabby-tan was on when he tried to kill me.

    hi "Just what the hell have they got you on?"

    "I stare at the tiny bottle in my hands as my feet carry me to the bathroom in the hall."
        
    hide pills # [str]

    scene bg school_dormbathroom # [str]
    with locationchange # [str]

    "Twisting the top open releases a smell all to familiar to me; the chalky odour of medication."

    "The tiny white ovals flow from the upturned bottle, making a staccato melody as they splash down into the pool of water in the toilet's bowl."
    
    stop music fadeout 4.0 # [str]
    
    "Emotionlessly, I push down the unassuming silver button, sending Hanako's pills away in a swirl of water."

    "As my rage dies down, I hear a quivering breath behind me."

    show lilly basic_sleepy at twoleft # [str]
    with charaenter # [str]
    
    li "What… did you just do?"

    #with vpunch # [str] (meh, doesnt look like collapsing to the floor)
    
    "Lilly's broken voice breaks me, and I collapse to the toilet's floor, still holding the pill bottle in my hand."

    hi "I…"

    "My words come in sobs."

    "I barely realised that I was crying."

    hi "don't… know…"

    play music music_drama fadein 0.1 # [str]
    
    hide lilly # [str]
    with charaexit # [str]
    show lilly basic_sad_close at centersit # [str]
    with charaenter # [str]
    
    "Lilly carefully guides herself to the floor by my side, and wraps her arms around me."

    "Broken, I let out sobs of despair."

    "Lilly gently coos and shushes in my ear, rocking slightly to calm me."

    "We sit there on the floor of the bathroom, until a scraping noise distracts us."
    
    show lilly basic_sad # [str]
    with charachange # [str]
    
    "Wiping the dampness from my face, I stand up and help Lilly to her feet."
   
    "Supporting each other, we enter the small hallway to find the source of the disturbance."
    
    # positioning isnt working [str]
    scene bg school_dormhanako at bgright # [str]
    with locationchange # [str]
    
    show lilly basic_sad at tworight # [str]  
    show hanabad emb_downtimid at twoleftsit # [str]
    with charaenter # [str]
    
    "Hanako sits on the floor of her room, quietly folding the clothes scattered around her room."
    
    ha "Oh. Hello Lilly, Hisao."

    "Hanako shows no emotion towards either the state of her room or the arrival of Lilly and myself."

    "She acknowledges us and then goes back to slowly folding her clothes."

    "As if it were the most natural thing in the world."

    "I try to speak, but once again find my throat choked."

    "Instead, I slip the empty bottle into my pocket, fall to my knees, and start to fold a blouse."
    
    show lilly basic_sleepy at tworightsit # [str]
    with charachange # [str]
    
    "Lilly too kneels upon the floor, and I hand her a shirt."

    "Sensing the situation, she too starts to fold Hanako's clothes."

    "Before long, the scattered clothes have been assembled into tidy piles, which Hanako noiselessly sorts into their rightful drawers."

    "As she reaches her underwear drawer, she lets out a brief, but bored exclamation."
    
    show hanabad emb_downdetermined at twoleftsit # basic_distant # [str]
    with charachange # [str]
    
    ha "Oh. They're gone."

    "It was the drawer that contained her pills."

    "I thrust my hand into my pocket, feeing the plastic bottle with my fingertips."

    "Pangs of guilt arc through my body like electricity."

    hi "Hanako… I…"
    
    show hanabad emb_downtimid at twoleftsit # [str]
    with charachange # [str]
    
    "Hanako pauses only for a moment before moving onto the next drawer, as if nothing had happened."

    "Lilly and I stand up whilst Hanako finishes sorting her laundry."

    ha "I'm going to bed now."

    "Without waiting for a response, Hanako unbuttons her blouse and lies down on her bed."

    scene bg school_girlsdormhall # [str]
    with locationchange # [str]
    
    show lilly basic_concerned # [str]
    with charaenter # [str]
    
    "I usher Lilly out of the room in an embarrassed rush."

    hi "I think… that I've had enough for one day."

    hi "I'm going to see the nurse and go to bed."

    "Outside, the afternoon sun is still high above the treetops, but I am gripped by a mind-numbing fatigue."

    stop music fadeout 3.0 # [str]

    "Lilly simply nods, and returns to her room."

    #timeskip to dorm
    scene bg school_dormhisao_ss # [str]
    with shorttimeskip # [str]

    "As promised, I went to see the nurse before retiring."

    "He diligently took my vitals and noted them down in my folder."

    "Thankfully, he wasn't as chatty as he was this morning."

    "I don't know what I would have said if he had asked me how my day was."

    "Collapsing on my bed, I catch a faint whiff of Hanako's scent from my bed sheets."

    "Guilt and desire mix together in my mind, further compounding my desire to close my eyes and end this wretched day."

    #eyesclose
    window hide # [str]
    scene black # [str]
    with shuteye # [str]
    with Pause(2.0) # [str]

    scene bg school_dormhisao # [str]
    with openeye # [str]

    "Wednesday brings with it the end of exams for the rest of the students."

    scene bg school_dormext_full # [str]
    with locationchange # [str]

    "Those that haven't already left for their holidays are sleeping in, and I don't see a single soul as I return from the nurse's office and head for the girl's dorm."

    scene bg school_dormhallground # [str]
    with locationchange # [str]

    "I push through the main doors, and enter the building."

    "Inside, a pair of girls still in their pyjamas are watching the TV."

    scene bg school_girlsdormhall # [str]
    with locationchange # [str]
    
    "They barely even register my existence as I make my way up the stairs to Hanako's room."
    
    show expression Solid("#00000022")  # [str]
    show hanako_door_base at right  # [str]
    show hanako_door_door at left  # [str]
    with locationchange # [str]
    
    play sound sfx_doorknock2 # [str]
    
    "I knock lightly on the door, and, to my delight, I hear a slightly muffled, yet familiar, voice."

    ha "C…coming."

    "There is the sound of flustered movement from inside, but I eventually hear footsteps approaching the door."
    
    # oh gawd, that ADVANCED SCRIPTING SHIT! [str]
    # so i just copied this stuff from a4-true. [str]
    scene bg school_dormhanako # [str]
    show hanako cover_worry_close at twocenteroff # [str]
    show expression Solid("#00000022")  # [str]
    show hanako_door_base at right  # [str]
    show hanako_door_door at left # [str]
    with locationchange # [str]
    
    play sound sfx_dooropen # [str]
    show hanako_door_door at leftdoor # [str]
    with charamove # [str]
    
    show hanako cover_worry_close at twocenteroff # [str]
    with charachange # [str]
    
    "Through the opening door, I see a relieving sight."

    "Hanako stands before me, her eyes cast down, her hair perfectly groomed."

    "Her loose uniform hangs from her frame, clean and familiar."

    "Her free hand rests against her shy face."
    
    show hanako cover_smile_close at twocenteroff # [str]
    with charachange # [str]
    
    ha "Oh… G… good morning Hisao."

    "Her voice lilts, the minute variations in tone washing me in relief."

    hi "Good morning Hanako. How're you feeling?"
    
    show hanako cover_distant_close at twocenteroff # [str]
    with charachange # [str]
    
    "She rubs her head slightly."

    ha "I… I have a bit of a headache."

    hi "Well, that's no good, is it?"

    hi "Do you want a drink of water?"

    "She nods slightly in agreement."

    "I hold out my hand for her, and she tenderly accepts it."

    scene bg school_courtyard # [str]
    with locationchange # [str]

    "We walk outside to the nearest vending machine, and I buy us two drinks."

    scene bg school_gardens2 # [str]
    with locationchange # [str]
    play ambient sfx_park fadein 4.0 # [str]
    show hanako basic_normal_close # [str]
    with charaenter # [str]
    
    show hanako basic_normal_close at centersit # [str]
    with charamove # [str]
    play sound sfx_can # [str]

    "Sitting on a nearby bench, Hanako sheepishly drinks, holding the small can with both hands."

    hi "How's things?"

    ha "I… feel like… like the fog has lifted from my brain."

    "She takes another sip from her drink, contemplating her next words."

    ha "Hisao…?"

    hi "Hmm?"
    
    show hanako basic_worry_close at centersit # [str]
    with charachange # [str]
    
    ha "I… I'm sorry."

    ha "I didn't mean…"

    "I rest my head on her shoulder."

    #Surprise/blush
    show hanako basic_bashful_close at centersit # [str]
    with charachange # [str]
    
    hi "It's okay."

    hi "You don't have to apologise."

    "Hanako, stunned into silence, takes another sip of her drink."

    hi "We'll get through this, together, okay?"

    hi "You, me, even Lilly."

    hi "We'll all be fine, okay?"

    "The can pauses against Hanako's lips."
    
    show hanako basic_smile_close at centersit # [str]
    with charachange # [str]
    
    ha "Okay."

    "We finish our drinks, and just sit on the bench for a while, my head still resting on Hanako."

    hi "Say…"

    ha "Hmm?"

    hi "Let's go on a date."
    
    show hanako basic_distant_close at centersit # [str]
    with charachange # [str]
    "Hanako breathes in a little in shock, though not as much as I expected."

    ha "W…where would we go?"

    hi "I don't know… you choose."

    "For a moment Hanako contemplates, toying with the empty can in her hands."

    ha "Let's go to the park in the town."

    hi "Sounds good to me."# Have you got all you need?"
    
    show hanako basic_smile_close at centersit # [str]
    with charachange # [str]
    
    "She nods soundlessly."

    hi "Right then, let's go!"
    
    stop ambient fadeout 3.0 # [str]
    
    "Excited by the slowly returning Hanako, I jump to my feet, and pull her up."
    
    # so, in the train scene hanako wears casual clothes, while should shool uniform
    # lets pretend she changed clothes before going "on a date" [str]
    
    #"We dispose of our cans, and head to the bus stop in front of the school."

    #BG Station
    scene bg city_busint # [str]
    with shorttimeskip # [str]
    play ambient sfx_businterior fadein 0.2 # [str]

    "Hanako was unusually silent on the trip in, so I try to goad her into talking."

    hi "Which way was it again? To the park…"

    ha "It… might be faster to take the subway…"

    hi "Oh, really? Well, let's do that then."

    stop ambient fadeout 2.0 # [str]
    scene bg city_tokyostation # [str]
    with locationchange # [str]
    play ambient sfx_crowd_outdoors fadein 0.2 # [str]
    $ renpy.music.set_volume(0.3, .5, channel="ambient") # [str]
    
    "We enter the station complex and take the escalator down to the subway platform."

    scene bg city_subway # [str]
    with locationchange # [str]
    
    "I check the map, and sure enough, the town's central park has its own station."

    hi "Wow, we'll be there in no time, right?"

    "Hanako nods in agreement, but says nothing."

    "The morning crowds have died down on the subway platform, leaving it almost bare."

    "Within minutes, the red-and-silver train pulls up alongside the platform, and we board an empty carriage."

    stop ambient fadeout 0.5 # [str]
    with Pause(0.5) # [str]

    scene train_scenery_subway #train_scenery2 # [str]
    show evfg hisao_trainride_subway #hisao_trainride # [str]
    with locationchange # [str]
    $ renpy.music.set_volume(1.0, .5, channel="ambient") # [str]
    play ambient sfx_trainint fadein 0.5 # [str]

    # no event cg, so had to remove it [str]
    #"We sit next to each other, and I take Hanako's hand, placing it in my lap."

    hi "Are you still feeling okay?"

    ha "My head still hurts a little."

    "I stroke her hand."

    hi "Should we stop off somewhere and get some painkillers?"

    ha "No… I should be fine."

    ha "I… hate pills."

    "The train pulls away from the station, and I pull Hanako close to me."
    
    stop ambient fadeout 0.2 # [str]
    
    #BG change to the park auditorium thing from H19 or whatever it was.
    scene bg suburb_park # [str]
    with shorttimeskip # [str]
    play ambient sfx_park fadein 0.2 # [str]
    
    show hanako emb_downsad_cas_close at tworightsit # [str]
    with charaenter # [str]

    "The sun gleams off the concrete roof of the park's stage, bringing with it the fury of the summer heat."

    hi "It's been a while, eh?"

    "As soon as we disembarked from the train, Hanako made a beeline for this place…"

    "…the place where we first kissed, the auditorium in the park."

    "Once again, there is not a person in sight, yet we sit together on the bench furthest from the stage."

    ha "Am I…"

    "Hanako sighs before going on."
    
    show hanako emb_sad_cas_close at tworightsit # [str]
    with charachange # [str]
    
    ha "Am I a bad girl?"

    hi "What? No, don't be silly."

    hi "Whatever makes you say that?"

    "Hanako takes a deep breath."

    ha "All I've ever done is hurt you."

    ha "But I still want to be with you."

    ha "That makes me a bad person, doesn't it?"

    hi "Hanako, none of this is your fault."

    hi "I want to be with you, and you want to be with me."

    hi "Nothing else matters, right?"

    hi "I promised you that, remember?"

    "I search her face for any signs of understanding, but find none."
    
    show hanako emb_downsad_cas_close at tworightsit # [str]
    with charachange # [str]
    
    #stop ambient fadeout 0.2 # [str]

    ha "Can I… see it?"

    hi "See what?"

    ha "Your chest…"

    $ renpy.music.set_volume(0.5, .5, channel="ambient") # [str]

    play music music_moonlight fadein 2.0 # [str] # music_hanakofinal?

    "Confused, I unbutton my shirt, revealing the unicorn-shaped band-aid."

    "Hanako shifts her gaze to the gap in my shirt, and I carefully remove the novelty dressing."

    "Beneath it, the crimson line of my scar shows, dissected by stitches."

    "Hanako reaches out a shaky hand, and traces her finger along the line of the wound."

    "I fight the urge to wince at the pain, biting down on the insides of my cheeks to prevent Hanako from noticing."

    ha "I… did this… didn't I?"

    hi "Of course not. I was like this before we even met, how could it possibly be your fault?"

    "I take her trembling hand in mine."

    ha "I thought I killed you…"

    ha "All I do is hurt and kill…"

    ha "I'm a bad person…"

    "Before she can say another word, I bury her face into my aching chest."

    hi "You're not a bad person."

    hi "You're just Hanako."

    hi "You're just feeling a little sick from the pills, is all."

    hi "You're not a bad person."

    "I feel her body convulse in sobs, and her salty tears sting my open wound, but I continue to just hold her against me."

    "If nothing else, I have to be here for her, from now until forever."

    stop music fadeout 2.0 # [str]
    #time skip or something.
    scene bg suburb_park_ss # [str]
    show hanako emb_downsad_cas_close_ss at tworightsit # [str]
    with shorttimeskip # [str]
    
    $ renpy.music.set_volume(1.0, .5, channel="ambient") # [str]

    "As the sun starts to turn in the sky, heading for its sleeping place, Hanako pulls away from me."

    ha "I… I want to go."

    hi "Okay. Shall we walk back?"

    ha "No… I don't feel well."

    ha "Can we take the train again?"

    hi "Sure thing."

    "Taking Hanako by the hand, we walk back to the subway platform."

    stop ambient fadeout 0.2 # [str]

    #BG platform. 
    scene bg city_trainstation_ss # [str] (maybe city_tokyostation?)
    with locationchange # [str] (shorttimeskip?)
    play ambient sfx_crowd_outdoors fadein 0.2 # [str]
    $ renpy.music.set_volume(0.3, .5, channel="ambient") # [str]
    
    "The afternoon crowds are starting to build, and the platform is a lot more crowded than before."

    "Hanako tugs gently on my hand, and leads me towards the end of the platform."

    "Through our light contact, I feel her tremble slightly."

    "PA" "The next train to arrive on platform two is the local train to Sendai Station."

    play sound sfx_trainchime # [str]
    "PA" "The train is approaching, please stand behind the yellow line."
    
    stop ambient fadeout 3.0 # [str]
    
    "The steady gust of wind that precedes the train forces me to look away form Hanako for a second to shield my eyes."
    
    # i'm sorry, feelings, i must have done this ;C [str]
    play music music_hanakofire # [str]

    "The trembling stops."
    
    with Pause(1.0) # [str]
 
    ha "I'm sorry."

    ha "I won't hurt anyone else anymore…"

    "Hanako releases my hand, and steps backwards."

    "I try to reach out to her, but it is too late."
    
    play sound sfx_heartfast # [str]
    show heartattack alpha  # [str]
    with Dissolve (0.1) # [str]
    hide heartattack alpha  # [str]
    with Dissolve (1.5) # [str]
    
    "The speeding train collides with her frail body just as I reach the edge of the platform."
   
    with Pause(1.0) # [str]
    
    "I was too late…"

    scene black # [str]
    with Dissolve (4.0) # [str]
    with Pause(1.0) # [str]
    window hide # [str]
    
    return
    
label en_end_hanakobad3:
    # Hanako bad end 3, after H32
    scene endscreen with dissolve #black with dissolve # [str]
    with Pause(1.5) # [str]
    
    scene black with dissolve # [str]
    centered "~ hanako bad end 3 ~" with dissolve
    stop music fadeout 1.0 # [str]
    return