label en_L1:

window hide None

scene black 
with dissolve

play sound sfx_alarmclock
with Pause (2.0)

scene bg school_dormhisao
with openeye

window show
"I wake to the annoying din of my alarm clock, its bright red numerals lighting up my face."

play music music_dreamy fadein 2.0

"It's one of the few artifacts that remain from before I came here, having been the same alarm clock I had at home. I'd hoped using it would help ease my transition into this new life."

"No such luck, though."

"I groggily drag myself out of bed, wiping the sleep out of my eyes as I open a couple of the pill bottles strewn on the desk and swallow them dry. By now, the process is starting to become automatic - something I should be glad for, given their purpose."

scene bg school_dormbathroom
with locationskip

"Much more awake than before, I wander into the bathroom."

play ambient sfx_shower fadein 8.0

show steam
with charaenter

"As the shower warms up, my mind begins to wander as my new daily routine begins once again."

"The bright colours of the fireworks fill my mind, as do the two that I spent my time watching them with. It feels strange, to be moved so much by people of whom I know so little."

"Then again, I suppose these aren't normal circumstances. At least now I have some people to talk to, aside from the schoolmate next door."

stop ambient fadeout 2.0

hide steam
with charaexit

"With the time left before school begins today waning, I begin to get ready for class."

$ renpy.music.set_volume(1.0,3.0, channel='music')

scene bg school_scienceroom
with shorttimeskip

"Walking through the door into the classroom, I notice that I'm still somewhat early. I see about five or six students milling around, most of them looking outright rancid."

"It's times like this that I appreciate being a morning person. That said, two students in particular seem just as perky as always."

hi "Hi Shizune, hi Misha."

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter

"I suddenly realise that my greeting would be lost on the former, so I quickly follow it up with a wave. She doesn't seem overly bothered. Or, for that matter, interested."

show shizu basic_normal at tworight 
with charachange

shi "…"

show misha hips_grin at twoleft
with charachange

mi "Hi Hicchan! Are you feeling well?"

"I can only assume her greeting comes from Shizune. It's hard to tell if she's speaking as herself or not sometimes."

hi "Better than most of the others, I guess. I notice you two are still bright and chipper."

show misha perky_smile at twoleft
show shizu basic_frown at tworight
with charachange

"Misha signs this back to Shizune as I say it, leading to what seems to be a somewhat terse response going by her sharp and rapid arm movements."

"Considering the two made such a big deal out of the festival preparations, I probably should've chosen my words more carefully."

show shizu behind_frown at tworight
with charachange

shi "…!"

show misha hips_grin at twoleft
with charachange

mi "Since you're a new student, we've been cutting you some slack. Please don't expect this kind of task-dodging to be allowed in the future."

"Misha looks as if she's about to add her own comment, but quickly goes back to interpreting as Shizune continues signing unabated."


show shizu basic_frown at tworight
show misha sign_smile at twoleft
with charachange

mi "While your contribution to class 3-2's stall is appreciated-"

show misha hips_frown at twoleft
with charachange

"Huh. Word gets out quickly. That, or these two have their finger on the pulse of the school."

mi "-we would prefer your efforts to be focused on the task at hand, that being your own class."

show shizu behind_blank at tworight
with charachange

"As much as I hate to admit it, they do have a point. Before I can respond though, Shizune adds one last addendum to the lecture, which earns a smile from Misha."

shi "…"

mi "Did you enjoy the festival, then? You certainly seem happy enough."

show misha perky_smile at twoleft
with charachange

"Lecture over, I guess."

hi "Yeah, it was good. Did you two enjoy it?"

show shizu behind_smile at tworight
show misha hips_grin at twoleft
with charachange

"Shizune gives a short nod as Misha grins and bounces her head up and down. The contrast, side-by-side, is amusing."

"Out of the corner of my eye, I notice more students starting to trickle into the classroom. A quick glance at my watch confirms that they're a few minutes late."


show misha hips_grin at center
show shizu behind_smile at right
show bg school_scienceroom at bgleft
with charamove

"I look over to Hanako's seat and notice that she's seated and reading a book contently. It makes me wonder just how long she's been there without my noticing."
    
hide misha
hide shizu
hide hanako
with Dissolve(1.0)

"With heavy footsteps coming up the hallway signalling Mutou's arrival, our idle talking comes to an end and I take my seat next to Misha."

"As the door slides open, he strides through with a heavy gait. His posture is even worse than usual, and his eyes are barely staying open. I guess my quip about the staff to Lilly and Hanako was misplaced."

play ambient sfx_paperruffling

"Everyone opens their books as he reaches his desk, and the first class of the new week begins."

stop music fadeout 3.0
stop ambient fadeout 0.5

with shorttimeskip

play sound sfx_normalbell

$ renpy.music.set_volume(0.5, 0.0, channel='ambient')
play ambient sfx_crowd_indoors fadein 2.0

"I rub my eyes as the lunchbell rings out, glad for the temporary reprive from work."

show lilly basic_smileclosed at leftdoor
with charaenter

show bg school_scienceroom at bgright
show lilly cane_smileclosed at tworight
with charamove

"I'm entirely unsurprised when I look over to the door and see Lilly standing there, cane in hand, patiently waiting for Hanako."

"Considering her acceptance of my request to join them yesterday, I decide to spend my lunchtime with them rather than eat alone."

show hanako emb_smile at left
with charaenter
with Pause(0.5)

hide hanako
hide lilly
with charaexit

"Hanako moves surprisingly fast to meet her companion, the two already entering the hallway before I can catch up."

stop ambient fadeout 1.0

scene bg school_hallway3
show lilly back_listen at twoleft
#show lillyprop back_cane at twoleft
show prop lilly_back_cane at twoleft # better solution [str]
show hanako emb_downsmile at tworight
with locationchange

show hanako def_shock at tworight
with vpunch

"Lilly's head turns slightly, registering the sound of footsteps behind her. As Hanako notices and follows her head, she almost jumps in surprise."

show hanako defarms_strain at tworight
with charachange

ha "Hi…Hisao?"

$ renpy.music.set_volume(1.0, 1.0, channel='ambient')
ha "I mean… um… hello, Hisao…"

hi "Hi. Sorry if I startled you."

show lilly cane_smile at twoleft
hide prop
with charachange

"Lilly turns to greet me, her orientation in doing so helped by Hanako."

li "Good afternoon, Hisao. Are you joining us?"

hi "If it's no trouble. Not much else to do, really."

"Lilly gives a small nod, as if to silently brush away any idea that it would be troubling in the least."

scene bg school_staircase2
with locationchange

with Pause(0.3)

scene bg school_hallway2
with locationchange

"We descend one set of stairs and walk down the hallway to the usual room, our pace somewhat quicker than usual thanks to Lilly using Hanako for direction rather than her cane and the railings."

scene bg school_miyagi
with locationchange

"As usual, it's deserted. The sounds of the other clubs can only barely be heard as sunlight streams into the room from outside."

"Looking around the room, I notice a couple of empty easels propped up against a wall that I don't think were there before. The art club must use this room as extra storage."

show hanako emb_smile 
with charaenter

ha "Should I get the chess set out, Lilly?"

"Hanako's voice seems less tense when she's directly addressing Lilly."

show hanako emb_smile at tworight
show bg school_miyagi at bgright
with charamove

show lilly cane_weaksmile at twoleft
with charaenter

li "Yes. I'll make tea while you sort the pieces."

hi "Ah, I can do that for you, if you'd like."

show lilly cane_surprised at twoleft
with charachange

with Pause(0.3)

"She ponders the offer for a moment before smiling, assuring me that I've made the right choice. Her face is remarkably easy to read."

show lilly cane_planned at twoleft
with charachange

li "Very well. Thank you."

show lilly cane_satisfied at twoleft
with charachange
show lilly behind_cheerful at twoleft
with Dissolve(0.5, alpha=True) 
with Pause(1.0)

hide lilly 
hide hanako 
with charaexit

"She slides her retracted cane into the handle of her bag and sets it against a leg of the table, before taking a seat opposite Hanako."

"As I prepare tea for the three of us, I can hear the small wooden pieces being set on the board. I wonder how good Lilly is at chess, given Hanako's surprising skill."

"By the time I place the steaming teacups onto the table, Lilly and Hanako have already moved their first pieces as they nibble at sandwhiches and rice balls from their respective bags."

scene bg tearoom_everyone_noon
show tearoom_hanae happy
show tearoom_lillye smileclosed
show tearoom_hisaoe hsmile
show tearoom_chess
with locationskip

$ renpy.music.set_volume(0.5, 2.0, channel='music')
hi "Here you go."

play sound sfx_teacup

"Hanako gives a small nod as I put down the cup next to her side of the board. Lilly's hand ventures sideways slightly, so I gently place the cup touching the tips of her fingers; a gesture she seems to appreciate."

show tearoom_hisaoe outside
with charachange

"I finally take a seat and silently sip my tea as the two play. It's interesting to see the two's contrasting appearances as they do so."

"Hanako looks closely at the board, her face one of focused concentration. Lilly, on the other hand, keeps her head level and maintains her calm neutrality."

"With passing interest, I note how Lilly's fingers quickly pass over the top of each piece she moves, identifying it before using her pinky finger to trace out the outlines of each square."

"Lilly's gentle voice adresses both of us as she continues to play."

show tearoom_lillye weaksmile
with charachange

li "How was class, now that the festival's over?"

show tearoom_hanae shy
show tearoom_hisaoe hthink
with charachange

"I look to Hanako to see whether she'll answer first, but see that she's doing the same."

show tearoom_hisaoe sigh
with charachange

hi "Not… great. Half the class seemed to be dozing off, even including the teacher. Not to mention a test on top of all that."

show tearoom_hanae happy
with charachange

"Hanako quietly adds her passive agreement, having nothing more to add."

show tearoom_lillye ara
with charachange

li "Ah, I could imagine that being a bit difficult for you."

hi "I think I did fine. Other than the shock of a test so early, science is probably my best subject."

show tearoom_hisaoe hsmile
with charachange

hi "How'd you go, Hanako?"

show tearoom_hanae open
with charachange

ha "Me? Ah… okay… I guess…"

show tearoom_hanae shy
with charachange

show tearoom_lillye thinking
with charachange

"I suspect Hanako's too sincere to be able to pull of lying very well. That much is obvious."

"Lilly's smile slipping very slightly confirms that Hanako probably isn't adept enough at the subject to do well without preparation."

hi "How was your class with the fallout, Lilly?"

show tearoom_lillye giggle
with charachange

li "Surprisingly well, actually. Only one student was absent, which was better than the teacher expected."

show tearoom_lillye smileclosed
with charachange

"With the topic all but run dry, the two concentrate on their chess game once again."

show tearoom_hisaoe lrelief
with charachange
with shorttimeskip

"I can't say I've ever liked the idea of chess as a spectator sport, but given its unique nature, for once I'm rapt in watching the game unfold."

show tearoom_hisaoe outside 
show tearoom_hanae sad 
with shorttimeskip

"As the time wears on, both of the two show a pretty good knowledge of the game. With a couple more pieces than Hanako captured, Lilly has the upper hand, but only slightly."

show tearoom_hanae open
show tearoom_hisaoe hunsure
with charachange

"That is, until Hanako makes a strange move with her queen. Seizing the lapse in judgement, Lilly takes the piece with her knight."

show tearoom_hanae shy
with charachange

"Without hesitation, Hanako moves a pawn to take Lilly's rook on the opposite side of the board, and promoted it to queen. Lilly's face falters as she realises that she just feel to Hanako's trap."

show tearoom_lillye thinking
show tearoom_hisaoe lunsure
with charachange

ha "Check."

show tearoom_hisaoe hsmile
with charachange

hi "That's not bad. Nice, Hanako."

show tearoom_hanae happy
with charachange

"The compliment causes her to flower into a surprised blush."

ha "Th-thank you. I didn't think it would work."

"I look over to Lilly, her fingers having just finished tracing out the position of her remaining pieces in an attempt to extricate herself from the pickle."

li "I think this is checkmate…"

show tearoom_hisaoe lrelief 
with charachange

hi "Hmm?"

"I take another look at the board to confirm."

"Sure enough, her king has nowhere to escape without being threatened by another piece. I guess that answers whether Hanako or Lilly is better at the game."

hi "So it is."

show tearoom_lillye weaksmile
with charachange

"Lilly gives a small sigh as Hanako smiles. From their reactions, this hardly seems an unusual result."

show tearoom_hisaoe lsmile
with charachange

hi "So how long have you two been playing?"

show tearoom_hisaoe hsmile
show tearoom_hanae sad
with charachange

ha "Since… I was young."

show tearoom_lillye smileclosed
show tearoom_hisaoe lsmile
with charachange

"Lilly nods at Hanako's brief answer."

show tearoom_lillye smileclosed
with charachange

li "Hanako taught me how to play soon after I met her. I can beat her every now and again… but I don't seem to have the right mindset for it."

"If she came to Yamaku at the start of high school, but met Hanako when she moved to the dorms, that'd mean she's only been playing for about a year."

show tearoom_hanae happy
show tearoom_hisaoe hthink
with charachange

ha "But… she's better at languages than I am, so…"

show tearoom_hisaoe lthink
with charachange

"Lilly gives an appreciative, if slightly bemused, smile at Hanako's quick reversing of her compliment."

show tearoom_lillye weaksmile
with charachange

li "Well, that's how it is."

stop music fadeout 3.0
play sound sfx_warningbell

"The bell suddenly rings out, heralding the end to lunchbreak much to our surprise."

show tearoom_lillye thinking
show tearoom_hisaoe loops
with charachange

li "Hmm, that lasted longer than I thought it did."

hi "Same. I guess we'd better get back to class."

show tearoom_hanae shy
show tearoom_lillye weaksmile
show tearoom_hisaoe thinkclosed
with charachange

"Hanako's already in the middle of packing up, so I take Lilly's bag and give it to her as I pick up my own, earning an appreciative nod."

play music music_daily fadein 2.0
scene bg school_hallway2 
show lilly basic_smile at twoleft 
show hanako emb_smile at tworight 
with locationskip


"Walking through the hallways back to our classroom, I notice that Hanako seems quieter than before, but also more comfortable."

"Lilly, her hand on Hanako's shoulder, seems to pick up on her assured pace as well, smiling as they walk."

"If I could spend the rest of my time at Yamaku like this, I don't think it'd be so bad. All joy takes is small exchanges of happiness, after all."

scene bg school_scienceroom
with locationskip

play sound sfx_rumble

"As I reach my desk and set my bag beside it, I realize something. or rather, my stomach does."

"I was so busy with those two, I forgot to buy lunch…"

stop music fadeout 2.0

scene black
with dissolve

return

label en_L2:

scene bg school_dormhisao 
with locationchange

"Saturday. My second favourite day of the week."

"This is almost entirely due to the fact that it is the day with the second least amount of school, class ending at the beginning of lunch."

scene bg school_dormhallground
with locationchange

"I make sure to open my door confidently, myself being more than confident of being able to derive enjoyment out of the fine weather and shorter class length."

scene bg school_dormhallground
with locationchange

$ renpy.music.set_volume(0.2000000000000001, 4.0, channel='ambient')
play ambient sfx_footsteps_hard

"I confidently stride down the hallway, and down the stairs to the lobby of the male dorms."

$ renpy.music.set_volume(.5999999999998, 4.0, channel='ambient')

"I confidently look behind me to see who's footsteps are approaching."

$ renpy.music.set_volume (1.0, 4.0, channel='ambient')

"I... lose my confidence in this day being enjoyable."

stop ambient
play music music_kenji fadein 0.5

show kenji happy at center
with charaenter

ke "Hey man. Sup?"

hi "Not much I guess, just looking forward to the afternoon. You?"

show kenji happy_close at center
with characlose

"He wraps an arm around my shoulder too comfortably. Something's up."

show kenji neutral_close
with charachange

ke "Let's step outside, shall we?"

hi "I was just about to, before you stopped me."

show kenji tsun_close
with charachange

scene bg school_dormext_full
with locationchange

"He doesn't take my reaction to his theatrics well. Ignoring him, I stride outside and begin down the steps."

show kenji tsun at center
with charaenter

"It doesn't take too long for him to catch up with me again. I wonder if he wants money, or to rant about another conspiracy. Maybe both."

ke "I've got a bone to pick with you."

hi "Uh huh."

ke "It's about that blonde. You know who I'm talking about."

"For a moment I contemplate feigning ignorance, but realize this will go by quicker if I just let him get it all out."

hi "Lilly? The one from your class?"

show kenji rage at center
with vpunch

"He looks positively shocked at this development. Did he not expect me to be able to answer?"

ke "You're on first name terms with her!?"

"He gathers himself and coughs into his fist. Dramatically, like everything he does."

ke "Well, nevermind that. I'm here to warn you. You know. Man to man."

hi "Warn me about what? Lilly?"

ke "Yeah. You don't know her, man."

hi "I'm pretty sure you don't either."

ke "That's not the point. You're the one spending inordinate amounts of time with her."

"It distresses me that someone like Kenji, who's probably as far out of the loop as one could possibly get, know about such a trivial fact as who I choose to befriend."

"Then again... I am a transfer student, and she's not only the class rep of his class, but also a tall blonde."

"Maybe I should appreciate this ranting as a warning that the rumour mill both exists in this school and that I'm firmly within it."

hi "It's just lunch. Nothing special."

show kenji neutral
with charachange

ke "Look, man, under the bridge. See this bridge? You're under it. A man's gotta do what a man's gotta do to get intel."

show kenji tsun
with charachange

ke "I just want to make sure you don't end up too far under the bridge."

hi "You're losing me, Kenji."

show kenji happy
with charachange

ke "That's okay, lots of people get lost. That's why I'm here to help."

scene bg school_gardens
show kenji neutral
with locationskip

ke "Just be careful around her, okay? She looks all harmless on the outside, but I've heard shit. Bad shit."

show kenji tsun
with charachange

ke "You know the student council, right?"

"He seems to involuntarily shudder as he says the words. Putting him and Shizune in a room together is an amusing mental exercise. I wonder if they've met."

hi "Yeah, Shizune and Misha are in my class. I seem to have dodged the draft, though."

ke "Good man. Good man."

show kenji happy
with charachange

with Pause(3.0) # okay, why? [str]

show kenji tsun
with charachange

ke "But this blonde? She was there. In the student council. Right. Damn. There."

hi "I see. And?"

ke "And she's not there now."

stop music fadeout 3.0

hi "..."

ke "Seriously, think about it. Something must have gone down."

"I stop walking for a moment, giving the idea more thought than I probably should."

"It would explain that fight the two had, at least in part. Wait, no, not really. Even leaving the student council would need a catalyst."

"In the end, it doesn't explain much at all. Other than the fact that their feud goes back some ways."

hi "I guess you have a point. I'm not seeing how that really affects me, though."

show kenji neutral 
with charachange

ke "Okay, now field this one. Lilly's foreign, obviously."

hi "Obviously."

ke "Now, what nationality is she?"

"I open my mouth to give the answer, but realize that I have none. In fact, I've given the matter very little thought."

"Given that she has no accent and acts perfectly Japanese, I suppose it never really seemed important. Now that he mentions it though, I am rather curious."

hi "To be honest, I don't know. Maybe British? They like tea."

"I probably shouldn't resort to stereotypes, but that's the only lead I have."


show kenji happy
with charachange

play music music_kenji fadein 1.0

ke "You're not thinking. Luckily, you have me here to think for you."

hi "Gee, thanks."

"He brushes off the quip effortlessly."

show kenji neutral 
with charachange

ke "Now answer me this: Who has lots of social power, is filthy stinking rich - you know blondes are all rich, right? - has a long history of disputes and used to belong to a much larger organisation?"

hi "The Roman Catholic Church?"

ke "..."

"I can't help but be amused at stumping him so effectively. Being well-read has its benefits."

ke "Well okay, there's that."

ke "But there's also the mafia. Come on. Rich, foreign, there's no way she doesn't have connections to them."

"I have reason to doubt his logical deductions, but he shows no sign of stopping."

show bg school_hallway3
show kenji neutral
with locationskip
# courtyard BG

ke "So you know where I think she's from?"

hi "Italy?"

show kenji tsun
with charachange

ke "Italy's small time, dude. She has to be from Sicily. All those mafia types come from there."

show kenji happy
with charachange

ke "Wait, no, Russia. The mafia there is serious business man. Hardcore smuggling and-"

hi "Wait, wait, stop, just slow down a sec. What point are you trying to get at here?"

show kenji neutral with charachange

ke "You don't know what she'll do, man. I won't get in your way - agents don't operate like that - but I just want you to be careful."

show kenji tsun
with charachange
ke "When the time comes, we'll need all the help we can get. I don't want to lose you, Comrade."

"Well, at least he's concerned for me. Kinda."

stop music fadeout 4.0

show kenji tsun at center
hide kenji

"I wave goodbye to him as we separate out to our respective classes, but I'm not sure that he sees the gesture."

show bg school_scienceroom
with shorttimeskip

play ambient sfx_crowd_indoors fadein 2.0

"Piling my books into my bag, I catch a glimpse of the library books I'd borrowed last week. I may as well return them, considering they took all of two days to finish."

"I briefly consider inviting Hanako along to the library, but she's already gone. I'll probably be better for my studying if I'm alone anyway."

"With a quick stretch and a wave to a couple of classmates who give the same to me, I make my way out of the classroom."

stop ambient fadeout 1.0

scene bg school_library 
with locationskip

"As I open my bag and shove the books throuhg the returns slot in the front counter, I notice another person behind the desk. Old and greying, she must be Yuuko's replacement when she's working in the café."

"I begin looking for a free table, a task made somewhat difficult considering that, despite there not being many students in here, they're all sitting at their own tables."

"Noticing a familiar head of hair, I walk over to one of the tables near the braille section."

show lilly basic_smileclosed
with charaenter
"It's hard to tell whether Lilly's concentrating hard or not, her placid expression holding perfectly still as her finger skates across the dot-filled pages of her book."

hi "Hi. Mind if I sit here?"

show lilly basic_surprised 
with charachange

li "Hmm? Oh, no problem at all..."

"She trails off, evidentgly not quite placing the owner of the voice."

play music music_lilly fadein 10.0

show lilly basic_smile
with charachange

hi "Ah, Hisao."

show lilly basic_smileclosed
with charachange

"She gives a nod of greeting as I sit myself opposite her at the table, plucking a chemistry textbook out of my bag and quickly thumbing to the chapter we're covering in class."

"For a while, we sit there and read in each of our own ways."

"Seeing her though reminds me of what Kenji said this morning. That and the fact that I've never seen someone read in braille before makes he keep throwing glances at her."

"I kind of feel guilty about it given she has no way to realize that I'm doing so, so I decide to just ask her about it. Her lineage isn't exactly a state secret, after all."

hi "Hey Lilly, mind if I ask a question?"

show lilly basic_smile
with charachange

li "Not at all. Is anything wrong?"

hi "Ah, it's not that. I was just wondering... you're at least part foreign, right?"

show lilly basic_giggle
with charachange

"She gives a small giggle before laying down her book."

show lilly basic_cheerful
with charachange

li "I've always been amused at how squeamish people are about that. Akira's mentioned how much she and I look different from the norm before."

show lilly basic_smile
with charachange

li "The details are a bit complicated, but I'm half Japanese, half South African."

"South... African? That's not exactly my first guess. It takes some effort to not blather it out loud."

"I try to conjure images of the place in my mind. I think as far as Africa goes, South Africa wasn't bad to live in... but I'm not really sure."

"My personal guess of Britain was pretty far off base. That does leave another question though."

hi "But no accent?"

show lilly basic_weaksmile
with charachange

li "That's where the details begin. I was born and raised in Japan, despite my mother and grandfather on my father's side being foreign."

hi "I guess that makes sense."

"Hold on, if she moved to the dorms simply due to Akira working longer hours..."

hi "So they don't live near the school?"

show lilly basic_reminisce
with charachange

"She gives a small sigh, as if she didn't expect me to go any deeper. Was her previous frankness just a front?"

li "Not... exactly. We talk every now and again, but I miss them. It's been a long time since we actually met."

"I still feel like I'm not getting the whole story, but I don't really want to go unduly prying into her situation. She already seems depressed enough."

"I almost want to say \"I know the feeling\", but that's assuming entirely too much."

hi "So... what language do they speak there, anyway? I don't know that much about South Africa."

"It takes her a moment to collect herself, appreciating the change in topic."

show lilly basic_smileclosed
with charachange

li "Well, technically Afrikaans. Nobody here teaches it though, so I'm studying English. Most people there know it as well."

hi "I see. Must be troublesome."

li "It's not just teachers either. English books in braille aren't hard to buy or import, but Afrikaans..."

li "Well, there's more demand for local English teachers here anyway, which also makes it more useful."

"Demand for English teachers? For a moment, I wonder why she brings it up."

hi "You're planning to be an English teacher?"

show lilly basic_cheerful
with charachange

"She gives an enthusiastic nod."

"It must be nice, having such a definite future in mind. I've never really given much thought to mine, so I'm kind of envious."

hi "Hmm..."

show lilly basic_smile

li "What's wrong?"

hi "It's just... I could see you as a teacher pretty easily. It suits you."

show lilly basic_emb
with charachange

"For a moment, she's speechless. She lowers her face a little and lets out a nervous giggle, something I've never seen her do before."

"With her role as a class representative and her motherly nature, her being a teacher does seem to be a fitting line of work for her."

hi "Sorry, that was probably a little much. It is true, though."

show lilly basic_weaksmile
with charachange

"Waving her hand in front of her face dismissively, she quickly recollects herself."

li "It's not that, it's just that... only Akira's ever said that before."

stop music fadeout 8.0

"A short, somewhat awkward silence follows the discussion. Without knowing it, I ended up steering into the same awkward topic as before."

"I guess I should try to cheer her up a bit. After all, it was me who went and got her brooding."

hi "Want to go grab lunch at the cafeteria after this?"

"It might pick her up a bit, or at least take her mind off her apparently complicated family situation."

show lilly basic_planned
with charachange

"Going by her smile, it seems to have the intended effect."

show lilly basic_ara
with charachange

li "That's not much of a date..."

"Her wit seems to kick in whenever I get concerned over her. She does have a point though - the food there isn't the greatest."

hi "Shanghai? We could ask Hanako if she wants to come as well."

show lilly basic_surprised 
with charachange

li "Ah..."

hi "What is it?"

show lilly basic_weaksmile
with charachange

li "I almost forgot to say, Hanako's birthday is coming up soon. I was going to go shopping in the city tomorrow for a present."

hi "If that's an invitation, I'd be happy to accompany you."

"The ability to get more used to the layout of the city would probably be a good thing. I haven't even set foot in there, so I'd be hopelessly lost by myself."

show lilly basic_smile
with charachange

"She gives a nod, signalling that she happily approves of this plan for Sunday."

"We eventually get back to our books, though before I begin reading once again I steal one last glance at her."

"Maybe I've been thinking on my situation too much. After all, everybody here would have their own unique circumstances."

"The chance to get outside and clear my head will probably do me good."

return

label en_L3:


return

label en_L4:


return

label en_L5:

return

label en_L6:

return

label en_L7:

return

label en_L8:

   
    scene bg school_scienceroom
    with charaenter
    
    play sound sfx_warningbell

    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')
    play music music_daily fadein 2.0
    
    "The afternoon bell brings a sigh of relief from the class."

    "To be honest, I don't even have the energy to sigh."

    ha "Um…"

    show hanako cover_distant at left
    with charaenter

    "Before I've even thought about getting out of my seat, Hanako appears alongside my desk."

    hi "Hey Hanako. What's up?"

    ha "Um… Lilly and I are going to… um… get together… tonight…"

    ha "Can you come too?"

    hi "You mean for another tea party? I guess so…"

    show hanako basic_smile at left
    with charachange

    "Hanako's face tells me that this was the right response."

    ha "Um… g—great… It's the same ti… ti… time…"

    show hanako emb_emb at left
    with charachange

    ha "Seeyoulater!"

    hide hanako
    with charaexit

    "Hanako stiffly walks out of the classroom, her legs like matchsticks as she recovers from the shock of social interaction."

    "It takes a moment for me to gather the energy to actually get up."

    "In fact, by the time I reach the corridors, I can already hear the sporting clubs making a racket outside."
    
    
 
    scene bg school_courtyard
    with locationskip

    "The walk back to the dorms is as placid as usual."

    "Everyone is either busy with their clubs or being studious in their rooms at this hour."

    "I suppose I should slot myself into the latter category, seeing as I got nothing done yesterday."

    "Still, the afternoon sun and the scented breeze coming from the gardens are telling me just one thing:"

    "“Relax.”"
    
    scene bg school_gardens2
    with locationchange

    "I make my way into the gardens, find myself a patch of grass and lie down."

    "I watch as the clouds above start to take on the orange hue of sunset."

    scene bg school_courtyard
    with shorttimeskip

    "…"

    "By the time I stir from my unintentional nap, the skies above have turned into the dark blue of the early evening."

    "I suppose I should be making my way back. Besides, I wouldn't want to stand up the girls."

    "I have a feeling that the two of them would be able to show me levels of pain unbeknown to man."

    "That, and the fact that they'd be in their pajamas once again. A far from unwelcome sight, really."

    "I gather up my things, which have been scattered by my impromptu nap, and head back."

    stop music fadeout 1.0
    
    scene bg school_dormhisao
    with locationskip

    "As soon as I close the door to my room, there is a fevered knocking."

    play sound sfx_doorknock
    
    play sound sfx_doorknock

    ke "I know you're in there!"

    ke "I have something for you, Hisao!"

    "I drop my bag on the floor and turn to open the door."
    
    play sound sfx_dooropen

    "The idea of Kenji having something for me fills me with inexplicable dread."

    scene bg school_dormhallway
    with locationchange

    play music music_kenji

    show kenji happy
    with charaenter

    ke "Took you long enough. This came for you."

    "It seems that Kenji is one of those impatient people that just has to get to the point without formalities."

    "As he thrusts the letter into my hands, I try the dangerous action of initiating some smalltalk."

    hi "Hey. How are you?"

    ke "Fine, I suppose. Lilly Satou dropped this by. You know, the blind girl. Blonde. Tall. Class rep."

    hi "Yeah, I know who you mean."

    hi "Wait, what? She's a class representative? I've been talking to her recently, but she didn't mention that…"

    show kenji tsun
    with charachange

    "Kenji sours at my mention of talking with her."

    ke "Oh, have you now? I guess you don't need her introduction, then."

    hi "Introduction?"

    "Kenji's eyes narrow as he leans conspiratorially close to me."

    show kenji neutral
    with charachange

    ke "I've gathered data on practically every girl in the school."

    ke "It's a good tactic. If you can go up to a girl and know their names and their hobbies, then they're more likely to trust you."

    ke "For example; “Hey, you're Lilly Satou, right? The cello girl, yeah?”"

    ke "The girls think that you've got some kind of connection then, and will trust you more."

    "Something tells me that Kenji's view on women may not mirror reality."

    hi "Um, great. I'll keep that in mind…"

    "Kenji pats me on the shoulder."

    show kenji happy
    with charachange

    ke "Any time, partner."

    hide kenji
    with charaexit
    
    stop music

    "With a parting wink, he heads back down the corridor to his room. My awkward squirming goes, thankfully, unseen."

    play sound sfx_doorclose

    scene bg school_dormhisao
    with locationchange

    "Closing the door once again, I open the envelope he handed me."

    play sound sfx_paperruffling

    $ written_note("Dear Hisao,\n\nJust in case Hanako didn't manage to ask you to, I'd like to invite you to our teaparty tonight.\nThe location, once again, is my room.\nAs the curfew is ten in the evening, it would be best to arrive well before then.\nBoth Hanako and I would appreciate it greatly if you accompanied us once again.\n\nUntil then,\nLilly.")

    "The paper is some kind of specialty paper, thick to the touch, and with an embossed border."

    "I try studying for a time and manage to get a little done, but I'm really not feeling in the mood."

    "I guess this is the effect women have on men. Maybe there's some truth to Kanji's ramblings after all, heaven forbid."

    "Sighing at my weak will, I close the book in front of me and tiredly stretch before leaving my room."

    scene bg school_dormhallway
    with locationskip

    "In no time, I find myself quietly rapping on Lilly's door."

    ha "Ah, coming!"
    
    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')
    play music music_one fadein 10.0
    
    scene ev lilly_bedroom at center
    with locationchange

    "The door swings inwards, and once again I am treated to the sight of Hanako in her bedclothes, and Lilly behind her."

    scene ev lilly_bedroom_large
    with charaenter
    
    with Pause(2.0)
    
    "Once again, I find giving myself a mental thumbs-up for this little blessing."
    
    scene bg school_dormlilly
    with locationchange

    #show hanako basic_bashful_paj # there's no such sprites [str]
    show hanagown smile # FIXME: check if appropriate; change if not [str]
    with charaenter
    ha "H—Hisao, um, g—g—good evening!"

    "She flicks her head downwards twice in quick succession, making her greeting perfectly clear."

    li "Good evening, Hisao."

    "Lilly's soft, calm voice is a stark contrast to Hanako's."

    "Before I can catch myself, I give her a quick wave over Hanako's shoulder."

    ha "Um, w—would you like to… have a seat?"

    "It's obvious she's trying her hardest to be a good host."

    hide hanagown
    with charaexit

    "With a polite nod, I walk over to the low table in the center of the room and sit obediently."

    show hanagown smile at tworight # FIXME: check if appropriate; change if not [str]
    show lilly basic_smileclosed_paj at twoleft
    with charaenter

    hi "Evening, you two. Thanks for inviting me."

    "Lilly gives a small, graceful nod."

    "It's amazing how accurately she can get a bead on where I am just from a single spoken sentence."

    show lilly basic_smile_paj at twoleft
    with charachange

    li "Have you any preferences for your tea?"

    hi "I'm easy. Surprise me."

    show lilly basic_smileclosed_paj at twoleft
    with charachange

    li "It would be my pleasure. Hanako?"

    ha "I don't mind."

    show lilly basic_ara_paj at twoleft
    with charachange

    li "My my, you're just as decisive as each other."

    li "I'll prepare them now, then. I shan't be long."

    hide lilly
    with charaexit

    "And with that, she stands and moves to the counter."

    show hanagown smile_blush at center # FIXME: check if appropriate; change if not [str]
    show bg school_dormlilly at bgleft
    with charamove

    "Ah, I do so love these times alone with Hanako. She's quite the conversationalist."

    "Maybe that's too harsh. Still, just as always, there's an awkward silence."

    "She always seems to be just on the edge of saying something."

    "Once again, I guess I'll have to be the one to break the silence."

    hi "So uh, how's school going?"

    show hanagown emb_downtimid_paj
    with charachange

    "Hanako furrows her brow in intense thought."

    "I guess it's like her to take such a simple question so seriously."

    show hanagown basic_bashful_paj
    with charachange

    ha "Okay… I suppose."

    "By the barest of margins do I avoid burying my face in my hand."

    "Conversing with her is like drawing blood from a brick. I swear it."

    li "Ah, Hisao?"

    hi "Yeah?"

    hide hanagown
    with charaexit

    show lilly basic_smile_paj
    with charaenter

    "I turn around to see Lilly at the bench, looking at me."

    extend "No, not looking at me. Facing me."

    "My mind seems to be stuck in first gear tonight."

    li "Is Exotic Fire alright?"

    hi "Yeah, that'll be fine."

    "To tell the truth, I'd prefer coffee. It feels slightly improper to say so, though."

    "As she gives an affirmative nod, I turn back to Hanako."

    hide lilly
    with charaexit

    show hanagown smile
    with charaenter

    "…Who's smiling."

    "Why do I feel like I'm several miles out of the loop?"

    "After a few more moments of strained silence, Lilly walks over and sets the teacups onto the table as she sits."

    show hanagown emb_smile_paj at tworight
    show bg school_dormlilly at center
    with charamove
    show lilly basic_smileclosed_paj at twoleft
    with charaenter
    show hanagown basic_smile_paj at tworight
    with charachange

    "As we all take a sip, I take a moment to survey the room."

    "With my attention slightly less distracted by their attire than last time, I notice much more."

    "She has many books, for one. While her reading habits don't match mine, there's a wealth of books both on a bookshelf and in a little stack in front of it."

    "While most only have barely visible bumps where the titles would normally be, most of the ones with printed titles seem to be in English."

    "Secondly, she has no television."

    "While most seem to have small, portable televisions or at least a radio, she has nothing of the sort."

    "It kind of feels anachronistic. I wouldn't be surprised to see such a room before the war."

    extend "The first one, that is."

    "I guess between caring for Hanako, acting as class representative, studying and playing the cello, she has very little time to herself, if any."

    "As affluent as she may be, she does seem to work hard just to maintain the status quo."

    show lilly basic_smile_paj at twoleft
    with charachange

    li "Does the tea meet with your approval, Hisao?"

    "Lilly's voice takes me off balance for a second."

    hi "Ah, mm. It's nice."

    show lilly basic_smileclosed_paj at twoleft
    show hanagown basic_smile_paj at tworight
    with charachange

    "To tell the truth, I've been to busy looking around to really take note of the flavor."

    "The simple statement seems to please both of them, though."

    "I'm forgetting something here, I know it."

    "At least Lilly doesn't have the seemingly impermeable wall between her and I that Hanako has."

    hi "Hey Lilly, how'd you know Kenji knows me?"

    show lilly basic_smileclosed_paj at twoleft
    with charachange

    li "I know lots of things, Hisao."

    "I suddenly feel a chill run down my spine."

    show lilly basic_ara_paj at twoleft
    with charachange

    li "My my, I'm only joking, I assure you."

    show lilly basic_smile_paj at twoleft
    with charachange

    li "Kenji's in class 3-3, after all. I simply asked, and he simply answered."

    hi "Kenji talked with a girl?"

    show lilly basic_oops_paj at twoleft
    with charachange

    "Her smile slips."

    li "So you're acquainted with… that… side of him as well, then?"

    hi "I can't imagine how he must be in class."

    show lilly basic_weaksmile_paj at twoleft
    with charachange

    li "In class, he's outnumbered. It's when he's alone that he gets… difficult."

    li "Of all the people in 3-3, he's undoubtedly the most touchy to deal with."

    hi "Well, he's got good intentions, however flawed his thinking might be."

    "I'm not quite sure that's really true."

    "It only feels fair to try and say something positive about him though, however questionably true it may be."

    show lilly basic_smileclosed_paj at twoleft
    with charachange

    li "Oh, Hisao?"

    hi "Yes?"

    show lilly basic_smile_paj at twoleft
    with charachange

    li "I never said any of this."

    hi "Aye aye, ma'am."

    show hanako basic_bashful_paj at tworight
    with charachange

    ha "Um, s—sorry, but…"

    "Lilly and I both turn to face her in unison."

    ha "It's nearly curfew, I think."

    "I turn my wrist over slightly and glance down at the watch on my wrist."

    hi "Yeah, it's five to ten. I guess I'd better get going. A guy staying in a room with two women until late could give people the wrong idea."

    show hanagown emb_blushing_paj at tworight
    show lilly basic_giggle_paj at twoleft
    with charachange

    "Hanako flowers into full blush as as Lilly gives a lighthearted giggle."

    li "My my, that's a good point. Good night, Hisao."

    ha "Um, g—goodnightHisao!"

    "As I pick myself up with a slight grunt, I gently close the door behind me."

    hide lilly
    hide hanagown
    with charaexit
    scene bg school_dormhallway
    with locationchange

    "Only to have it open with back up again as Hanako steps through, and nearly bumps into me while she's at it."

    show hanagown cover_distant_paj
    with charaenter

    ha "S—Sorry!"

    hi "Ah, no, I should've checked if you were coming before shutting it. Sorry."

    show hanagown basic_bashful_paj
    with charachange

    "We stand there in silence for a couple of seconds."

    hi "I guess I'd… uh… better be going."

    ha "Ah… mm. Good night."

    hi "'Night."

    hide hanagown
    with charaexit

    "As I turn and walk back, I hear Hanako's door shut behind me."

    "Polar opposites, yet they seem to be made for each other."

    "Lilly's motherly personality, and Hanako's shyness."

    "What an odd pair."

    "As I walk back to my dorm room, I silently count myself blessed."

    "Blessed for being able to know these two, however odd they may be."

    scene black
    with dissolve

    return

label en_L9:
    scene black with fade
    scene bg school_scienceroom
    with shorttimeskip

    "I sweat profusely, awaiting the dreaded moment."

    "Each tick of the clock tenses my muscles that much more."

    "It's coming for me."

    "I can feel it."

    "Death."

    "Death in the form of a single sheet of paper."

    "Classmate" "Here."

    "I take the small pile of papers from the student in front of me, plucking off the top piece and passing it backwards."
    
    "As I look to the top right of the page, my fears are realised within that small red circle."

    play sound sfx_sword_draw

    "Fourty-three."

    "I hang my head and sigh in resignation."

    "Cursing under my breath, I can feel the aura of a similar sentiment rising from the entire class."

    "Misery loves company, as they say."

    "As the teacher opens his mouth, the room braces for the inevitable onslaught…"

    play sound sfx_warningbell

    "…only to be saved at the last minute."
    
    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')
    play ambient sfx_crowd_indoors fadein 2.0

    "As we quickly move to collect our bags and leave for lunch poste-haste, the teacher delivers a parting broadside."

    "Teacher" "We'll be discussing the class's test scores next lesson. Needless to say, there will be quite some discussion to be had."

    "A collective groan resounds from the class, now reduced to shuffling out dejectedly."

    scene bg school_hallway3
    with locationchange

    "I push the sheet into my bag as I walk along the hallway, crumpling it in the process."

    hi "Bloody English…"

    "Voice" "HI—SA—O!"
    
    stop ambient fadeout 0.5

    "A woman's stern voice gruffly calls out from behind me."

    "I freeze in the spot, my face becoming like stone. It's as if I can feel my brain disconnecting from my body."

    "My eyes slowly shift right, trying to catch a glimpse of the disembodied voice."

    "…"

    "My face begins to slip as time passes."

    "I decide to risk turning my head, ever so slowly twisting it to the—" #reminder for the potential {nw} break

    with vpunch
    hi "GYAAAAH!"

    "I jump into the air and drop my bag, yelling out in surprise."

    "As I recover and regain my composure, I turn to see…"

    show emi excited_amused
    with charaenter

    hi "Emi!"

    emi "Tee hee!"

    "She stands there with a mischievous grin on her face, hands forward and fingers pointed inwards."

    "Before me is a culprit of waist-jabbing."

    hi "So, it's come to this then?"

    "I crouch down into a prepared stance, a devilish grin spreading over my face"
    
    show emi basic_concentrate at centersit
    with charamove

    "We meet each other's eyes, sizing each other up as we sway slightly, ready to pounce at any…"

    ha "Hisao…?"

    "My smile suddenly flattens, my body snapping upwards and spinning to meet the voice from behind me."

    hide emi
    with charaexit
    show hanako basic_bashful
    with charaenter

    hi "Uh… hi Hanako."

    "I try my best to appear suave, utterly failing in the process."

    "As I notice Hanako's visible eye move to the left, I let myself fall to the right."

    show hanako basic_bashful at twoleft
    show bg school_hallway3 at bgleft
    with charamove
    with vpunch
    show hanako basic_bashful at center
    show bg school_hallway3 at center
    with charamove

    "…Just in time to avoid Emi's tackle, causing her to hit the ground beside Hanako unceremoniously."
    
    play sound sfx_impact

    show lilly basic_surprised at right
    with charachange

    hi "Haha! I win the day!"

    ha "Ah, Emi! Are you—?"

    "Emi turns herself over and thrusts an upturned thumb at Hanako."

    show emi basic_closedgrin at left
    with charaenter
    
    emi "I'm o-kay! If a fall like that did me in I'd never be able to run."
    
    show hanako basic_normal at center
    with charachange

    "She beams a childish smile as she expertly rights herself using her arms."

    show hanako basic_normal at tworight
    with charamove
    show emi excited_happy at twoleft
    with charaenter

    "Even as she's regaining her balance I can see her eyes narrowing in preparation for a second try."

    show emi basic_shock at twoleft
    with charachange

    emi "Ah! Rin!"

    hide emi
    with charaexit
    show hanako basic_normal at center
    with charamove

    "Without a second word, she forgets all about us and bolts off up the hallway."

    "Hanako and I stand speechless, only able to helplessly stand and watch this ball of seemingly boundless energy dash off."

    emi "Oh, ah…"

    show hanako basic_normal at tworight
    with charamove
    show emi excited_amused at twoleft
    with charaenter

    "She suddenly stops herself just before disappearing around the corner to the rooftop staircase, spinning around to meet our bemused faces."

    emi "I hate English too."

    hide emi
    with charaexit

    "And with that, she disappears."

    "All I can do is hang my head and give a long sigh, having been thoroughly left in the dust."

    show hanako basic_smile at tworight
    with charachange

    "As I hear a short giggle coming from beside me, I turn to see Hanako smiling at the corner my attacker rounded."

    show hanako basic_smile at center
    show bg school_hallway3 at bgleft
    with charamove

    "With a quick dusting off, I pick up my dropped bag from the floor."

    hi "'Afternoon. Been busy?"

    ha "You don't like English?"

    hi "Hmm? Oh, uh, nah. I had a test on it a while back, and Emi caught me ruminating about the results."

    show hanako emb_downtimid
    with charachange

    ha "Ah, sorry."

    "She averts her gaze, guilt written onto her face."

    "Anyone would be forgiven for thinking she'd just accidentally reminded me of a dead relative."

    hi "Come on, it's not your fault. How're you doing in it?"

    show hanako basic_bashful
    with charachange

    "She looks up, though still avoids meeting my eyes."

    ha "Alright, I… suppose."

    "An awkward silence passes. They seem all too common around Hanako."

    ha "Oh, um, Lilly asked if you'd like to join us for lunch on the roof."

    "I guess I don't exactly have any pressing commitments to attend to."

    hi "Sure, I'll be right up."

    "She checks the small analogue watch on her wrist, making as small a gesture out of it as possible."

    ha "Um, I'll… go get lunch from the cafeteria… now."

    "She hesitates, seemingly wanting my approval before leaving."

    hi "Go on. You don't need my approval to leave, you know."

    ha "Ah, right. I'll, uh, be going then."

    hide hanako
    with charaexit

    "With a skittish reply, she gives a small nod and quickly makes off towards the cafeteria."

    "I guess she must've forgotten to bring lunch today."

    "As I walk up the hallways, more and more students start passing and coming out of classrooms."

    "By the time I manage to make it to the stairs, I'm having to push my way past busily chatting throngs of students."

    $ renpy.music.set_volume(0.20000000001, 1.0, channel='ambient')
    play ambient sfx_rooftop fadein 2.0

    "I finally manage to get past the last of the crowd and round the staircase, slumping slightly in relief and slowing my pace as I open the door to the roof."

    play sound sfx_door_creak
    $ renpy.music.set_volume(0.5, 0.5, channel='ambient')

    scene white
    with dissolve

    hi "Ah, damn!"

    "I momentarily avert my eyes, all but blinded by the harsh summer sun."

    mystery "Huh?"

    scene bg school_roof
    with locationchange

    show lilly basic_smileclosed at left
    show emi basic_happy at center
    show rin basic_absent at right
    with charaenter

    "As I slowly regain my vision, the surroundings finally take form."
    

    
    "Rin, Emi and Lilly sit tegether on the rooftop, the amazing expanse of the city far below easily visible past the fence around them."
    
    emi "Ah, Hisao!"

    "Rin and Lilly give a quick nod of acknowledgement and a deep nod of greeting respectively."

    "As I start to walk towards the rather mismatched trio, I can't help but mervel at the speed at which Emi devours the rest of her half-eaten banana."

    hi "Hey. Strange to see you three together like this."

    show lilly basic_ara at left
    with charachange

    li "It seems to have been quite the day of coincidences; Emi and Rin decided to eat on the roof as Hanako and I decided to."

    show emi basic_annoyed
    show lilly basic_smile at left
    with charachange

    emi "You stole it! This spot was ours!"

    hi "Simmer down, you can't steal a place in the school."

    "I plonk myself down beside Lilly, the four of us creating a deformed semicircle."

    show rin basic_awayabsent at right
    with charachange

    rin "I think she is right."

    hi "You too?"

    show rin basic_lucid at right
    with charachange

    rin "The butterfly is her accomplice."

    hi "The butter…"

    "As I glance around, sure enough, a small yellow butterfly floats across my field of vision."

    hi "So tell me, how did this butterfly help Lilly “steal” this spot?"

    rin "It scouted out our conversation and told her."

    "I should've known better than to expect sound reasoning from Rin. Regardless, I guess it wouldn't hurt to play along."

    hi "You're telling me she can talk to butterflies?"

    rin "There are people who can talk to horses, called horse whisperers."

    rin "Lilly must be a butterfly whisperer."

    show emi basic_closedsweat
    with charachange

    "I bury my head in my hand as Emi rounds on her strange companion."

    emi "Whisperers don't work like that."

    "Emi and Rin continue their banter as I turn to Lilly, busily finishing off her small box of curry and rice with a pair of burgandy chopsticks."

    hi "So what brought you up here, anyway?"

    show lilly basic_smileclosed at left
    with charachange

    li "A little fresh air every now and again doesn't hurt."

    show emi basic_shock
    with charachange

    emi "Ah!"

    "She breaks off from her vain attempts to introduce the concept of logic to Rin."

    show rin basic_awayabsent at right
    show emi basic_annoyed
    with charachange

    emi "That was why we came up here too!"

    show lilly basic_weaksmile at left
    with charachange

    "Something tells me it was her reasoning alone, and that Rin only got dragged up here on Emi's whim."

    "Then again, the same could probably be said of Lilly and Hanako."

    li "Now, now. We can share."

    "As soon as she says the words, the creaking of the door to the roof can be heard."

    hide emi
    hide lilly
    hide rin
    with charaexit

    "A moment's silence falls over us as everyone's attention focuses on the figure appearing from it."

    show hanako basic_normal
    with charaenter

    hi "Ah, Hanako. You're back."

    ha "Mmm."

    hide hanako
    with charaexit

    "As she slowly walks over to us, she almost imperceptibly tenses as her eyes meet those of Rin."

    "I can't help but raise an eyebrow as she walks over to us and sits next to me, doing her upmost to avoid looking ahead."

    show hanako emb_downtimid at left
    show lilly basic_smile at twoleft
    show emi basic_happy at center
    show rin basic_absent at right
    with charaenter
    
    # ER7 is mandatory, ER5 is optional

    # If Hanako and Rin met in ER7 and ER5

    "Thinking back to their previous run-ins, it's not too hard to understand why."

    "Rin's utter lack of tact takes Hanako severely off-balance, not to mention her lackadaisical approach to changing topics mid-discussion."

    "Not being able to anticipate what she'll say or do next at all must make her more scared of Rin than usual."

    "Well, at least Rin doesn't seem too gung-ho about initiating conversations, much less with someone who's too afraid to even respond."

    # If they met in ER7 but not ER5

    "She may well be shy around others, but this is rediculous."

    "Thinking back, it gives similar vibes to the exchange they had in the cafeteria."

    "I lean myself slightly to the left, whispering to Lilly."

    hi "Have Rin and Hanako met recently before?"

    show lilly basic_smileclosed at twoleft
    with charachange

    li "Why do you say that?"

    hi "Hanako seems kinda, no, very scared of her."

    show lilly basic_weaksmile at twoleft
    with charachange

    li "…Ah."

    "From the tone of her voice, it's all too obvious they've had a run-in some time before."

    li "I once talked with Rin about happenings in class 3-4, and Hanako was with me at the time."

    li "She's… unique."

    "She says the word with a slightly uncomfortable tone, as if she'd scanned an entire dictionary but failed to find an adequate word for her."

    "That said, I'm sure there isn't a single word in any dictionary to describe Rin overly well."

    hi "Yeah, you could say that."

    li "Hanako didn't take well to her questioning, unfortunately."

    show lilly basic_oops at twoleft
    with charachange

    "We sigh in unison, lamenting the quandry of Rin."

    show lilly basic_smile at twoleft
    with charachange

    # End branches

    show hanako basic_normal at left
    show emi basic_grin
    with charachange

    "As Hanako starts to eat the melon bread she bought from the cafeteria, Emi looks at me deviously."

    emi "So, Hisao. What was your score in English?"

    hi "No comment."

    show emi basic_annoyed
    with charachange

    emi "Boo~"

    "She puffs her cheeks and pouts, but doesn't take long for her to bounce back."

    show emi basic_grin
    with charachange

    emi "Alright, if I tell you mine, you have to tell me yours. Deal?"

    hi "Fine, fine."

    emi "Okay, on the count of three, we both say our results."

    emi "One…"

    emi "Two…"

    emi "Three!"

    $ doublespeak(emi, hi, "Thirty-two!", u"…")

    show emi basic_shock
    with charachange

    "I beam a mischievous grin."

    show emi basic_annoyed
    with charachange

    emi "Ah! Evil! Evil! Evil! Evil! Evil!"

    hi "You said it, not me."

    emi "That's the problem! Come here!"

    "She crouches down before suddenly springing forward at me."

    stop music fadeout 1.0

    scene bg misc_sky
    with dissolve
    with vpunch
    show emi basic_closedsweat
    with charaenter

    "Before I can even hope to react, my vision goes spinning upwards as she launches herself into me."

    hi "Ow. Ow."

    emi "Owie."

    "As I blink to regain my senses, I find myself lying with my back on the roof and Emi lying on top of me."

    li "Hisao! Are you okay!?"

    hi "I'm okay. Again."

    show emi basic_hes
    with charachange

    emi "Why didn't you move, Hisao?"

    hi "Hey! You were the one who…"

    hi "Huh."

    show emi basic_confused
    with charachange

    "Emi blinks blankly as she remains on my chest."

    emi "What is it?"

    hi "I… can't feel anything."

    show emi basic_shock
    with charachange

    "A flash of panic flashes across Emi's face, misinterpreting what I said."

    hi "No, I don't mean it like that."

    hi "I mean, I can't feel you at all."

    show emi basic_annoyed
    with charachange

    "A small grin slowly spreads on my face as a look of shock covers Emi's."

    emi "Meanie! Meanie, meanie, meanie!"

    with vpunch
    with vpunch
    with vpunch
    with vpunch

    "All I can do as she playfully bats at my shoulders with her fists is laugh."

    "Even Lilly and Hanako are having trouble surpressing their laughter."

    "That is, until I suddenly feel an unwelcome sensation in my chest."

    "A slow, burning pain right in the pit of it. It takes every fiber of my being to resist the temptation to give in to the panic welling up."

    hi "Emi, stop!"

    emi "Meanie, meanie, mea—" #reminder for the potential {nw} break

    hi "I said stop!"

    show emi basic_shock
    with charachange

    emi "Ah—" #reminder for the potential {nw} break

    "She suddenly freezes, noting the expression of pain on my face."

    hide emi
    with charaexit

    "As she jumps back off me with almost supernatural speed, I sit myself up while holding my arms tightly over my chest."
    
    window hide
    
    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.1)
    
    hide heartattack alpha
    with Dissolve (0.7)
    
    play music music_tragic fadein 0.5

    window hide

    play sound sfx_heartslow
    show heartattack alpha 
    with Dissolve (0.1)

    hide heartattack alpha 
    with Dissolve (0.2)

    with Pause(0.7)

    play sound sfx_heartfast
    show heartattack alpha 
    with Dissolve (0.1)

    hide heartattack alpha 
    with Dissolve (0.2)

    window show

    scene bg school_roof
    with dissolve

    show hanako defarms_worry at left
    show lilly basic_concerned at twoleft
    show emi sad_depressed at center
    show rin basic_lucid at right
    with charaenter

    "With a deep breath, the pain, thankfully, begins to fade."

    "As I look back up, there's only silence and pensive faces to be seen."

    "I guess I'd better explain myself."

    hi "Arrythmia. I'm fine, it's just a heart flutter."

    li "Are you sure? Should we get the nurse?"

    hide hanako
    with charaexit

    "Taking her cue, Hanako quickly picks herself up and begins to dash to the door."

    hi "Hanako, stop. Lilly, I'm fine."

    show hanako defarms_worry at left
    with charaenter

    rin "You look like a wet, wrinkled tomato."

    hi "Huh?"

    "As I bring my hand to my forehead, I can feel the beads of sweat gathered on it and dab them off with my cuff."

    hi "Thanks. I told you, I'm fine. I'm just kind of… fragile, I guess."

    show emi sad_depressed
    with charachange

    emi "I'm sorry, Hisao."

    "She looks down, quietly sniffling. She's on the verge of tears."

    "Dammit. I feel awful."

    "Before I can comfort her though, Lilly gently rubs her hair."

    show lilly basic_weaksmile at twoleft
    with charachange

    li "It's alright, Emi. It's not your fault."

    hi "She's right. Don't feel bad about it, okay?"

    show emi sad_depressed
    with charachange

    "She gives a weak nod after Lilly's efforts to comfort her, with the conversation of before segueing into a solemn silence."

    "I need to break this."

    hi "Hey, Emi?"

    emi "Yeah?"

    hi "Thirty-two is a shockingly bad score."

    $ renpy.music.set_volume(0.20000000001, 1.0, channel='ambient')
    play ambient sfx_rooftop fadein 2.0
    
    show emi basic_annoyed
    with charachange

    emi "W—What was that!?"

    hi "At least I managed to eck out fourty-three."

    show emi excited_proud
    with charachange

    emi "Ha! I won!"

    "…what?"

    hi "And how did you come to that conclusion?"

    emi "I beat you at getting a lower score!"

    "I shouldn't have asked."

    show lilly basic_concerned at twoleft
    with charachange

    li "Emi, you really shouldn't boast about low scores."

    show emi basic_hes
    with charachange

    emi "Boo. I bet you scored high, as usual."

    "Lifting an eyebrow, I inquisitively turn to Lilly."

    hi "You're good at English?"

    show lilly basic_giggle at twoleft
    with charachange

    "She gives a cheeky grin."

    li "Ninety-six percent."

    "No way. All I can do is hang my mouth open in wonder."

    hi "That's…"

    show emi basic_annoyed
    show lilly basic_smile at twoleft
    with charachange

    emi "Foul! Foul!"

    hi "What?"

    emi "Lilly's half-foreign, so she don't count!"

    hi "You still got an atrocious score."

    show emi basic_shock
    with charachange

    emi "Geh."

    show emi basic_happy
    with charachange

    emi "Well, it's not like I need English anyway."

    hi "Just don't complain to me when you fail your exams."

    show emi excited_proud
    with charachange

    emi "I'll just get a running scholarship!"

    hi "Fallbacks don't hurt."

    show lilly basic_concerned at twoleft
    with charachange

    li "He's right, Emi."

    show emi basic_annoyed
    with charachange

    emi "Hmph. Two on one isn't fair."

    hi "This isn't fair either…"

    "With the speed of a striking mantis, I puck an apple from the top of Emi's bag and take a mouthful of the juicy, green item."

    show lilly basic_smileclosed at twoleft
    show emi basic_shock
    with charachange

    emi "Thief!"

    hi "You can take it back if you want."

    show emi basic_hes
    with charachange

    "As she gives a dejected huff, the school bell suddenly rings out."

    "One by one, we pack up out things and begin to head out the door, Emi poking her tongue out at me as she leaves."

    hide emi
    hide rin
    with charaexit
    hide hanako
    with charaexit
    show lilly basic_smileclosed at center
    with charamove

    "In the end, it's just Lilly and I left."
    
    $ renpy.music.set_volume(0.20000000001, 1.0, channel='ambient')
    play music music_lilly fadein 10.0
    
    "As we begin to take our leave, I turn to her."

    hi "Want a hand out?"

    show lilly basic_smile at center
    with charachange

    li "My my, that would be quite gentlemanly of you, Hisao."
    
    "She gently takes the cuff on my left sleeve in her hand, nodding in appreciation."

    scene bg school_hallway3
    with locationchange

    "As we enter the corridor and begin to break off to our respective classes, I pause."

    hi "Hey, Lilly?"

    show lilly basic_smileclosed
    with charaenter

    li "Yes?"

    hi "Um… thanks. For what you did back there."

    show lilly basic_smile
    with charachange

    "She gives an indulgent smile, nodding."

    li "She's strong, but only human. We do worry about you, Hisao."

    hi "Hold on, why would I worry you?"

    show lilly basic_concerned
    with charachange

    "Her smiling face collapses, becoming uncomfortably serious."

    li "Hisao, we are not ignorant of your situation."

    li "Unlike us, you…"

    show lilly basic_sad
    with charachange

    "She suddenly cuts herself short, unsure of whether she should say what she intends to."

    "I give a weak smile and rest my hand on her shoulder."

    hi "Don't. It's enough that I worry about it. I don't want you all to shoulder my burden."

    li "But…"

    hi "If you all worry about it, I have to worry about your worrying."

    hi "…if that makes sense."

    hi "I'm fine, okay?"

    show lilly basic_weaksmile
    with charachange

    "Giving up, she smiles once again and nods, taking my hand in hers."

    li "Very well."

    li "All I ask is that you take care of yourself, Hisao."

    hi "Don't worry, I will."

    hide lilly
    with charaexit

    "With that, we part ways."

    "To be honest, I don't know what I hate more—the fact that I could die at any moment, or the fact that everyone knows as such."

    "I guess I'll just take each day as it comes."

    "If they worry, if anyone worries, I'll smile."

    "I'll smile enough for all their worries to go away."

    scene black
    with dissolve

    return

label en_L10:

    scene white

    scene bg misc_sky
    with dissolve

    "Blue."

    "A deep, cerulean blue."

    "A blue so deep and endless it seems to flow on for eternity."

    "If not for the grass pressing into my hands, I feel as if I could simply will myself upwards and float into it."

    "As I stare upwards, the sight engraves itself on my mind."

    "The blue sky."

    "That wonderful blue sky"

    "A world unto its own."

    "A single drop of sweat coursing down my temple brings me back to a world I'd almost forgotten."

    "The world where it's early morning, and I'm laying on the ground not far from the student dormitories."

    "Feeling close to death after waking up in a pool of sweat is hardly a foreign occurence."

    "Having it happen afterwards though, is."

    "I collect myself and pick my exhaustion-wracked body from the ground."

    hi "It'd be nice if the weather held out."

    scene bg suburb_roadcenter_rn
    with shorttimeskip

    show rain

    li "Hisao, hurry!"

    "I can barely hear Lilly over the deafening pounding of the rain."

    "As I look forward, hands over my head in a futile attempt to keep my head dry, my vision seems to be in greyscale."

    "The dark clouds bleach the entire scene in their dull dreariness, unwilling to let even the slightest sliver of colour survive their grasp."

    "Hanako skitters between shop overhangs as if she were a rabbit darting between bushes, her dress now thoroughly soaked."

    "Even Lilly, her mantle now completely drenched, has forgone her composure entirely and taken to dashing from one overhang to another, her left hand gripping Hanako's and her cane reduced to a deadweight."

    "It's safe to say none of us had anticipated the sudden downpour that accosted us as we so innocently walked into the suburbs this morning."

    hi "Lilly, do you know where we're going!?"

    "I'm reduced to shouting to try and be heard over the deafening roar of the rain, the two girls running far ahead of me."

    li "I know a cafe we can take shelter in!"

    hi "Good, I had no idea where you two were taking me!"

    "A fierce gust of wind sweeps all three of us with water, drawing protests from Hanako."

    hi "What's it called!?"

    li "The Sha—" #reminder for the potential {nw} break

    "The rest of her voice is completely drowned out by an even heavier burst of rain."

    hi "The what!?"

    li "The Shanghai! I know someone there!"

    hi "How far is it!?"

    li "It shouldn't be far now!"

    hi "How… Okay!"

    "I give up shouting as I feel my throat giving out, contenting myself to being dragged around for god knows how long in the freezing cold."

    "It doesn't take long though before Lilly's voice calls out once again."

    li "Hisao, we're here!"

    "They stop just in front of a light brown wall, waiting for me to catch up before going in."

    "As I join them underneath the huge sign announcing in cursive script “SHANGHAI,” I suddenly remember I've come here before."

    "The styling seems like a strange mix between an old Japanese tearoom and… pretty much every country and style I can think of."

    "While it hardly looks swanky, it does have a homely atmosphere. I'm not surprised Lilly's come here before."

    "I push open the glass door and wave Hanako and Lilly in with my free hand."

    hi "Ladies first."

    "They both give a polite nod before entering, both making sure to rub their feet on the small welcoming mat."

    scene bg suburb_shanghaiint
    with locationchange

    "As I step in behind them and wipe my feet, only a quick glance is needed to notice the distinct lack of activity."

    "It seems like it's completely empty, the status quo for the small cafe."

    show yuuko neutral
    with charaenter

    "Girl" "Lilly?"

    "Or maybe not."

    "A single voice beckons from the tables to our right. As I look over, I see a girl that I'd peg to be a few years older than Lilly."

    "With a red sweater, glasses and a befreckled face, I guess the best description of her would be “geeky.”"

    "As she picks herself off the back of the seat, evidently having been sleeping before our arrival, her face seems to light up."

    show yuuko happy
    with charachange

    "Girl" "Well if it isn't Lilly!"

    hide yuuko
    with charaexit

    show bg suburb_shanghaiint at bgright
    with charamove
    show lilly basic_smileclosed_cas at twoleft
    show hanako basic_normal_cas at left
    with charaenter

    "I back to the girls beside me, Lilly's back arched as she bows deeply towards the befreckled stranger."

    li "Good to see you too, Yuuko."

    hide lilly
    hide hanako
    with charaexit
    show bg suburb_shanghaiint at center
    with charamove

    "As Lilly starts to walk towards the table, running her right hand over the seats as she goes, Hanako and I take our cue and silently follow her."

    "Hanako and Lilly slide in the seat opposite, with Lilly propping up her cane beside her as I quietly take the free seat next to the enigmatic “Yuuko”."

    show yuuko happy at tworight
    show lilly basic_smileclosed_cas
    show hanako basic_normal_cas at twoleft
    with charaenter

    yu "Ah, Hanako! You're here too?"

    ha "Ah, mm. Good morning."

    "From Hanako's unusually relaxed tone, it seems she at least knows Yuuko."

    yu "It's been too long since you came, Lilly!"

    li "It has been a while. How are you these days?"

    yu "Same as always…"

    show yuuko worried at tworight
    with charachange

    "Her face slips into a pained expression so quickly that I can't help but suspect it's an expression she's worn many times before."

    yu "I'm only just passing at University, the Shanghai's taking a heap of time out of my studying…"

    "As she speaks, her speech seems to get faster and faster."

    yu "My lecturer doesn't make any sense and scolded me yesterday for being late, Greek history isn't making any sense, all the dates are blending in together…"

    yu "The names fly out of my head as soon as I read them, all the politics are messed up, I''ve got several fees overdue, the number of people I owe money to is rising, all the food in the fridge is going out of date, my phone's broken…"

    "From that point on she starts to incoherently ramble to herself, and I'm completely unable to keep up. This is a girl in complete and all-encompassing despair."

    hi "Um… If I may…"

    "As the strange girl suddenly halts her rambling and flicks her head around to meet mine, I raise a hand."

    hi "Hi."

    show yuuko panic at tworight
    with charachange

    "She suddenly jerks backwards with astonishing speed."

    "Girl" "Ah, I didn't notice you! I'm sorry! I'm sorry! I'm sorry!"

    "As her head suddenly dives upwards and downways in apology, I wave it off and try to calm her down."

    hi "Ah ha, it's fine, really. Uh, I'm Hisao. Hisao Nakai."

    "I offer a hand, which she quickly takes in both of hers and shakes, still apologising furiously."

    show yuuko neurotic
    with charachange

    yu "Sorry, I'm Yuuko Shirakawa. Pleased to meet you. I hope you continue to patronize our establishment."

    "I raise an eyebrow at the seemingly out-of-place greeting."

    show yuuko panic at tworight
    with charachange

    yu "Ah! Wait, I'm not working yet! Sorry, sorry, sorry!"

    "Her head starts bobbing up and down yet again, leaving me completely speechless."

    "I guess I should try to take her mind off this. Or something. Anything."

    hi "Oh, I take it you three know each other?"

    show yuuko worried at tworight
    show lilly basic_smile_cas
    with charachange

    li "Hanako and I used to frequent Shanghai when we first came to Yamaku."

    show yuuko happy at tworight
    with charachange

    yu "Not to mention Lilly's my favourite cousin, of course."

    hi "Oh, so you're related?"

    yu "Mm, though the first time I saw her was when she walked into Shangai."

    li "You saw pictures of me before that, didn't you?"

    "Yuuko suddenly stops and looks upwards in thought."

    yu "Hmm… Ah, you're right."

    "Her previously maudlin face is twisted by a slight smile."

    yu "If I hadn't, I couldn't have—" #reminder for the potential {nw} break

    show lilly basic_surprised_cas
    with charachange

    li "Stop!"

    yu "Caused you to freak out when I hugged you out of the blue~"

    "As I quickly bring a hand over my mouth to stop myself from laughing, Lilly groans loudly."

    show lilly basic_sad_cas
    with charachange

    li "Yuuko…"

    "As I suddenly notice the clock over Yuuko's shoulder, I quickly collect myself and breath out the last remnants of stifled laughter."

    hi "Uh, Yuuko…"

    yu "Yuuko. Just Yuuko."

    hi "Yuuko, the time…"

    yu "Hmm?"

    show yuuko panic at tworight
    with charachange

    "She looks over her shoulder at the clock, suddenly freezing in panic."

    yu "Ah! No! This is bad! Sorry, I have to get changed!"

    hide yuuko
    with charaexit

    show hanako basic_normal_cas at twoleft
    show lilly basic_sad_cas at tworight
    with charamove

    "I quickly shuffle out of my seat to allow her out, with her dashing off behind a door next to the counter aftwards."

    "I rest my hand on the table, looking back to where she'd disappeared."

    hi "Huh. So, uh, that's Yuuko."

    show lilly basic_smile_cas at tworight
    with charachange

    li "You seem to get along quite well."

    hi "Why do I attract the wierdest people?"

    show lilly basic_concerned_cas at tworight
    with charachange

    li "Hmm?"

    "Lilly raises an eyebrow as her voice becomes extremely accusative. Whoops."

    hi "Not you. At least you're relatively normal."

    li "Relatively?"

    hi "Gee I wonder what I'll be ordering!"

    "I loudly proclaim a change in subject, Lilly's protests being all but drowned out."

    "I let myself fall back into the seat Yuuko had been at moments before and hook my arms over the back, I quickly survey the lightly-coloured table."

    "Salt, pepper, small stand with the number 12 printed on it…"

    hi "Huh, that's odd."

    show hanako basic_bashful_cas at twoleft
    show lilly basic_smileclosed_cas at tworight
    with charachange

    "Lilly and Hanako look questioningly at me."

    li "What's the matter?"

    hi "There's no menu."

    show hanako emb_sad_cas at twoleft
    show lilly basic_concerned_cas at tworight
    with charachange

    "Hanako and Lilly tense up, their expressions becoming visibly strained."

    li "N—No menu, you say?"

    hi "Yeah. No menu. How wierd."

    "Hanako quickly looks all around the cafe, seemingly searching for something."

    hi "Uh, Hanako?"

    li "Hisao, I need you to listen carefully to this."

    hi "Uh… okay, what's up?"

    li "Not having a menu is normal for Shanghai. Don't bring it up."

    hi "I see. Wait, how are we supposed to order then?"

    li "They serve coffee and tea here, and also small meals to have alongside them."

    hi "But why don't they just have—" #reminder for the potential {nw} break

    li "Hisao."

    hi "Okay, okay."

    show lilly basic_smileclosed_cas at tworight
    with charachange

    li "Ah, you're back."

    hide lilly
    hide hanako
    with charaexit

    show yuuko happy_shang
    with charaenter

    "I look over to see Yuuko in a waitress's uniform. Well, at least what I think is a waitress's uniform."

    "I have a suspicion whoever the owner is haphazardly stitched together a maid's outfit, a cheongsam and… bits and bobs from other waitress uniforms."

    "As my eyes pan up, I notice her hair done up into two small white buns."

    "How she managed to get dressed in such an outfit and arrange her hair in such a short time speaks of how long she must've worked here."

    "She suddenly flings her upper half downwards so close to the table that I brace in anticipation of her injuring herself."

    "As I look sidelong at Hanako and Lilly, they have exactly the same reaction."

    yu "Welcome to the Shanghai, may I take your order?"

    "Straight into business, I see."

    li "Green tea, please."

    ha "Same here."

    hi "I'll have a coffee, thanks."

    yu "Two green teas and a coffee. They'll be right up."

    hide yuuko
    with charaexit

    show hanako basic_normal_cas at twoleft
    show lilly basic_smileclosed_cas at tworight
    with charaenter

    "As she turns and leaves for the counter, I slump back in relief."

    "I gaze out the large window to my left at the storm raging outside."

    "Just looking at it makes the cafe seem warmer, though the relentless rain still pounds at the windows."

    hi "Well that came on suddenly."

    li "At least we're inside now. We can wait in here until the weather dies down."

    hide hanako
    hide lilly
    with charaexit

    show yuuko neurotic_shang
    with charaenter

    "As I yawn and rest my head in my hand I shift my gaze to Yuuko, busily pouring coffee behind the counter."

    "Her face has to be less than an inch from the clear jug, a look of intense concentration written on it."

    "The more I look at her in that rediculous outfit and hairstyle, the better it actually seems to look."

    "As I watch her preparing our drinks, every move she makes is done slowly and carefully."

    "She eventually finishes pouring the second cup of green tea and ever-so-slowly walks out towards us, all three drinks perched on a pan held in both extremely stiff hands."

    "I tense slightly, fully prepared for the eventuality that she trips and drops everything, hot tea and coffee splashing everywhere in a spectacular fashion."

    "Nonetheless, she finally makes it to the table and hands out all our drinks safely."

    show yuuko happy_shang
    with charachange

    "As she pulls back, I notice a look of massive relief on her face. How this girl is a waitress, I'll never know."

    show hanako basic_normal_cas at twoleft
    show lilly basic_smileclosed_cas at tworight
    with charaenter

    li "Thank you, Yuuko."

    hide yuuko
    with charaexit

    "She gracefully bows and, as the door opens, attends to the coming customers."

    "As I gingerly bring my hand to the side of the cup, checking the temperature of the coffee, I'm amazed."

    hi "Wow, it's just the right temperature to drink."

    "Lilly simply nods as she silently brings her green tea to her mouth, the cup neatly held both from the side and bottom and her eyes closed."

    "Hanako gently lifts her cup, holding it as if it would break if breathed on too heavily."

    "I quickly wolf down the contents of my mug and haphazardly rest my head and arms on the table, letting my head lull to the side."

    hi "Oh, it's clear now."

    show hanako basic_distant_cas at twoleft
    with charachange

    ha "Hmm?"

    "I move my eyes upwards to see her looking outside, the sun illuminating her face."

    "Her features seem somewhat more striking than Lilly's, or at least those visible through her hair. In the sun's light, her scar seems to dance over her face akin to a brilliant rhapsody freely playing across her right cheek."

    hi "Hey, Hanako."

    ha "Hmm?"

    "She looks down at me, the shadows highlighting her features even more as her hair falls across her scar, as if it were curtain-call on the performance."

    hi "You look nice."

    ha "Ah, tha—" #reminder for the potential {nw} break

    show lilly basic_surprised_cas at tworight
    with charachange

    ha "U—Uweeeeh!?"

    "Hanako reels back and blushes wildly as Lilly loudly chokes on her green tea. I can't help myself from chuckling at their reactions."

    hi "Haha, I was wondering what it'd take to get you to say something."

    show hanako basic_bashful_cas at twoleft
    show lilly basic_smileclosed_cas at tworight
    with charachange

    ha "Hisao, don't say things like that."

    hi "You seem unusually quiet though, even for you."

    "Lilly takes a moment to collect herself, wiping her mouth with a knapkin."

    show lilly basic_smile_cas at tworight
    with charachange

    li "Hisao's right, Hanako. You've been awfully quiet."

    ha "It's n—nothing. Really."

    show hanako emb_downtimid_cas at twoleft
    with charachange

    "Her bright red face tilted downward in embarassement, she nervously flicks her eyes from Lilly to me."

    "I pick myself up off the table and stretch noisily."

    hi "Fine, fine. We should get going soon anyway."

    "I suspect nothing will come of trying to tease the answer out of her bar even more nervousness on her part, and judging from Lilly's resuming of quietly drinking the last of her tea, she seems to share my view."

    hi "Finished Lilly?"

    li "Yes, finished. Hanako?"

    ha "Mm, I'm done."

    hide lilly
    hide hanako
    with charaexit

    "As we move to take our leave, I glance back as Lilly and Hanako exit through the door onto the street outside."

    "As Yuuko glances in my direction, I silently raise a hand in farewell, with her returning the gesture as she moves to our table."

    "And here I was, hoping a person Lilly knows would be normal."

    "I should've known better, really."

    scene black
    with dissolve

    return

label en_L11:

    scene black

    mi "Hicchan~"

    hi "Go away."

    mi "Hicchan~"

    hi "Leave me alone."

    mi "Come on, Hicchan~"

    hi "Hmph, let me sleep."

    "After two nights of not being able to sleep at all, the last thing I want is to be woken when I finally manage to."

    "It may be the last period of class, with my pillow being a textbook, but I'll take whatever sleep I can get by this point."

    mi "See Hicchan, even Shicchan wants you to get up~"

    "I don't care what Shizune wants, leave me alone."

    mi "Geez, Hicchan, I'll just have to wake…"

    "Wait, Misha's going to…?"

    mi "…you…"

    "This is bad!"

    scene bg school_scienceroom
    with openeye

    show shizu behind_blank at twoleft
    show misha perky_smile at tworight
    with charaenter

    hi "I'M UP!, I'M UP! YOU DON'T…"

    hi "have to…"

    "…"

    "My face goes bright red."

    "Sitting bolt upright, the students still in class stand and stare at the shouting fool who was sleeping just moments before."

    hi "…Dammit."

    
    play sound sfx_impact
    with vpunch
    
    "I let my head smack back down on the table."

    $ renpy.music.set_volume(1.0, 1.0, channel='music')
    play music music_normal fadein 2.0
    
    show shizu behind_smile at twoleft
    show misha hips_laugh at tworight
    with charachange

    mi "Wahahahahaha~"

    "Misha's trademark uncontrolled laugher reverberates through the classroom."

    show misha perky_smile at tworight
    with charachange

    "As I swivel my mournful eyes to the bespectacled Shizune beside her, she brings her hand to her mouth as she desperately tries to maintain a look of serious disapproval."

    "Narrowing my eyes, I can see the badly-hidden grin spreading across her face."

    hi "Et tu, Shizune?"

    "Shizune looks away quickly as she crosses her arms tightly, barely on the edge of her control."

    show shizu cross_wut at twoleft
    show misha hips_laugh at tworight
    with charachange

    mi "Wahahahahahaha~!"

    "Misha's laugher doubles in volume as she glances at Shizune."

    "I drag my hand down my face in resignation."

    hi "You two…"

    show misha hips_grin at tworight
    with charachange

    mi "Who was the one who slept in class, Hicchan~?"

    hi "Yeah, yeah, it was me."

    mi "Poor Shicchan was having a fit trying to wake you up, Weren't you?"

    "I move my eyes back to the standoffish Shizune, who with a single huff of confirmation returns to looking away with her arms crossed."

    show shizu cross_wut at twoleft
    with charachange

    hi "Why was Shizune trying to wake me up?"

    show misha perky_smile at tworight
    with charachange

    mi "Shicchan wanted to give you the handouts the substitute teacher gave out while naughty Hicchan was sleeping."

    hi "Handouts?"

    show shizu behind_frown at twoleft
    with charachange

    "I suddenly find two sheets of paper thrust down in front of my face."

    "Following the hand holding them, I see the still pouting figure looking down at me with a distinct scowl."

    hi "…ah. Um, sorry about that."

    "No dice. Her irritated face still holds."

    "I clasp my hands together and flick my head downwards in apology."

    hi "Very, very sorry."

    show shizu cross_wut at twoleft
    with charachange

    "She huffs and simply drops the papers on the desk."

    hi "Damn."

    show shizu behind_blank at twoleft
    with charachange

    show misha sign_smile at tworight
    with charachange

    show shizu cross_wut at twoleft
    with charachange

    show misha perky_smile at tworight
    with charachange

    show shizu behind_blank at twoleft
    with charachange

    show misha sign_smile at tworight
    with charachange

    "I look up over my hands to see Shizune and Misha signing frantically to each other, a look of frustration on Shizune's face."

    show shizu cross_wut at twoleft
    with charachange

    show misha perky_smile at tworight
    with charachange

    show shizu behind_blank at twoleft
    with charachange

    show misha sign_smile at tworight
    with charachange

    "It looks to be less of a dialogue and more of a tirade, punctuated with sidelong glances at me."

    show shizu cross_wut at twoleft
    with charachange

    show misha perky_smile at tworight
    with charachange

    show shizu behind_blank at twoleft
    with charachange

    show misha sign_smile at tworight
    with charachange

    "To say it's unsettling is understating things."

    hi "Um…"

    show shizu cross_wut at twoleft
    show misha perky_confused at tworight
    with charachange

    "The two suddenly stop signing and look at me in unison, both having exactly the same look of disapproval."

    "In one fluid motion, Misha's hand suddenly extends high above me and comes rocketing down."

    with vpunch
    centered "*THUD*"

    "Before I can even hope to react, my head is sent bouncing up and down like a jack-in-the-box."

    "I quickly bring my hands to my head, more out of reflex than actual pain."

    hi "Ow! What was that for?"

    show shizu behind_smile at twoleft
    show misha perky_smile at tworight
    with charachange

    "I open my eyes to see the two grinning at each other while exchanging an enthusiastic thumbs-up."

    mi "Shicchan says she forgives you now, Hicchan."

    hi "Could you forgive me with a little less force next time?"

    show shizu adjust_happy at twoleft
    show misha hips_laugh at tworight
    with charachange

    mi "Wahahahaha~!"

    "I look at the two with a flat face."

    "Misha and Shizune: one, Hisao: zero."

    "Giving up on the nap so cruelly stolen from me, I rub my forehead and slowly get up, putting the sheets in my bag before swinging it over my shoulder."

    "With a small bow, I step back a step and move to make my departure, Misha still doubled over laughing as Shizune nods back in a curt farewell."

    "I join the dribble of students exiting the open door, turning the corner into the hallway."

    hide shizu
    hide misha
    with charaexit

    scene bg school_hallway3
    with locationchange

    show hanako basic_bashful
    with charaenter

    "Only to end up face to face with Hanako."

    hi "Woah. Uh, hey Hanako."

    ha "G—Good afternoon, Hisao."

    "Silence passes between us as busily chatting students pass us like a roving school of fish."

    "She's fidgeting constantly, her eyes drawn to her rather unremarkable footwear."

    "I take the bridge of my nose in my fingers as I shut my eyes out of frustration. I'm barely staying awake as it is."

    hi "Hanako, you want to say something. What is it?"

    ha "U—Um, uh…"

    "I open my eyes, looking out from under my drooping brow."

    show hanako def_strain
    with charachange

    ha "I—I, ah, w—wanted to… give you this."

    hi "Hmm?"

    "She holds out a small rectangular piece of paper."

    "As I blink to make out the text through barely open eyes, I slowly start to make out what's written."

    $ written_note("Eggs x2\n\nBread loaf x1\n\nWhole-grain cereal x1\n\nLettuce x1")

    hi "…What?"

    "I look upwards, raising an eyebrow."

    show hanako basic_bashful
    with charachange

    ha "I, ah, th—thought you went to the store on Mondays, so…"

    hi "You wanted me to run errands for you?"

    show hanako defarms_strain
    with charachange

    ha "I—It's okay if you don't want to! I just thought that, um, m—maybe, uhm…"

    "She's panicking, badly."

    "I sigh. Yet another battle lost, though this time by a weakly-fought surrender."

    hi "It's fine, I was going to go anyway."

    show hanako defarms_worry
    with charachange
    
    ha "Ah, no, it's okay! I'll…"

    hi "Hanako. It's fine. As I said, I'll pick up your stuff while I'm there, okay?"

    show hanako basic_bashful
    with charachange

    ha "Ah, okay."

    "She bows deeply, twice, as if to make her gratitude perfectly clear."

    ha "Thank you, I was going to go, but I needed to study for a test tomorrow and…"

    hi "Test?"

    hi "Ah, that's right, science. You've going fairly well in it recently, aren't you?"

    "She brightens ever so slightly."

    show hanako emb_smile
    with charachange

    ha "Mm, I've been spending more time on it than before."

    "I give a smile, though there's less feeling behind it than I'd like."

    hi "Good work, Hanako."

    "As expected, she starts smiling as well, and much more earnestly than I at that."

    hi "I'll grab your stuff and take it to your dorm in the evening. Seeya."

    "With a small wave, we part our ways."
    
    stop music fadeout 1.0

    hide hanako
    with charaexit

    scene bg school_gate
    with locationchange

    "As I carefully dodge and push my way through the throngs of students, I manage to make it out into the courtyard and to the school gate."

    "Making a right-turn, I start my way towards the shopping arcade and leave the dribble of students turning the other way to the bus station."

    scene bg school_road
    with locationchange

    "Slipping my right hand into my pocket, I gently swing my bag in my left as I walk in the orange dusk sunlight."

    "Thankfully the sweltering summer heat's started to die down, making way for a pleasant cool breeze."

    "As I stretch my hands high above my head, a familiar figure takes form, schoolbag in her right hand and a cane in the left."

    hi "Ah, Lilly."

    "She stops and turns around, turning her head slightly to try and work out exactly where the voice came from."

    show lilly basic_listen at center
    #show prop lilly_back_cane at center # uugh, why is it even here? [str]
    with charaenter

    "I quickly catch up to her, coming in beside her and matching her slow pace as we resume walking."

    hi "Hey, Lilly."

    play music music_soothing fadein 2.0
    
    show lilly cane_smile at left
    with charamove

    li "Good evening, Hisao."

    hi "It's that late already?"

    "I glance up at the sky."
    
    show bg misc_sky_ss at tworight
    with locationchange

    "A distinct tinge of orange discolours the cloudless expanse, washing the footpath in its light."

    show bg school_road_ss at center
    show lilly cane_smileclosed_ss at left
    with charachange
    
    li "So, Hisao, what brings you here?"

    hi "Just going to town to grab the groceries, same as every Monday."

    show lilly cane_ara
    with charachange

    li "My my, what a coincidence!"

    hi "Ah, you're doing the same thing?"

    show lilly cane_smile at left
    with charachange

    li "Mm. I usually go grocery shopping on Fridays, but it was raining."

    hi "Makes sense."

    "We continue walking down the street, the familiar sound of her cane echoing through the air as we go."

    "Other than the occasional passing car and the leaves in the branches, there's a blissful silence."

    "Thank god I can finally relax for the first time today."
    
    $ renpy.music.set_volume(.5, 1.0, channel='music')

    "I glance over to Lilly."

    "That porclain face of hers never seems to lack that air of relaxed confidence."

    "I guess the same could be said of her personality, too."

    "She silently walks, her head and eyes staying true to the street ahead of her."

    "I look back ahead and savour the cool air blowing over my face."

    "This is probably the calmest moment I've had since the about-face my life took so recently."

    "And to have it while walking to get some groceries."

    "What a wierd life."

    "I suddenly notice the crumpled-up note rubbing against my hand in my pocket, pulling it out to check the contents."

    hi "Let's see here… Eggs, bread, cereal, lettuce, shaved ham, thyme…"

    show lilly cane_ara
    with charachange

    li "Ah, Hanako has you running her groceries, I see."

    hi "Yeah. Just how much does this girl eat anyway?"

    "My mind suddenly clicks that, yes, there is actually a person beside me."

    hi "W—Wait, how did you—!?"

    show lilly cane_giggle
    with charachange

    "She giggles wholeheartedly."

    li "My my, Hisao,"

    "Her giggles punctuate her words, though she's making little effort to supress them."

    li "Quite direct today, aren't we?"

    hi "Yeah, you got me there. Still, how'd you know?"

    show lilly cane_smile
    with charachange

    li "Hanako buys the same things every week."

    hi "Ah."

    li "Usually I go shopping with Hanako, but seeing as we didn't go on Friday it seems she expected to meet and walk with me today."

    "She gives a small sigh."

    show lilly cane_oops
    with charachange

    li "Sorry, Hisao. It seems in my haste I've ended up leaving you with a burden."

    hi "Nah, it's no problem. I was going there anyway."

    "With that, the conversation trails off."

    show lilly cane_smile
    with charachange

    "Compared to the awkward silences of Hanako, Lilly seems genuinely content to say what she thinks and stay quiet when there's nothing to say."

    "The slick road under my feet is bathed in an orange glow, the occasional fallen leaf crunching underfoot."

    "As we walk I let out a deep yawn, my lack of sleep coming back to haunt me."

    li "My my Hisao, did you not get much sleep last night?"

    hi "I couldn't sleep at all for the last two nights. Bloody insomnia."
    
    stop music fadeout 8.0

    show lilly cane_surprised
    with charachange

    "Lilly's face suddenly becomes shocked. So, she's actually capable of expressing that emotion after all."

    li "T—Two days!?"

    hi "Yeah, it's happened before a few times. My meds screw with my sleeping occasionally."

    li "…Ah."

    show lilly cane_sad
    with charachange

    li "I'm… sorry, Hisao."

    hi "Come on, it's not your fault. At least I shouldn't have any trouble getting to sleep tonight after falling asleep in class."

    show lilly cane_oops
    with charachange

    li "You do worry me sometimes."

    hi "I… worry you?"

    li "Didn't you just worry me then?"

    hi "Point taken."

    "I reach around and scratch the back of my neck."

    hi "Hey, Lilly…"

    show lilly cane_smile
    with charachange

    li "Hmm?"

    hi "Um, thanks."

    li "Ah…"

    show lilly cane_emb
    with charachange

    "She looks down slightly, her white cheeks almost imperceptibly reddening."

    li "My my, Hisao, it's only natural to worry about those around you."

    hi "Still, it's nice to know someone's out there like that."

    "She reddens further."

    "It may be embarrassing to say, but it's the truth."

    "She takes a breath to regain her composure, though her cheeks remain flushed."

    "With a gentle smile, the final downhill walk to the store passes in silence."
    
    stop music fadeout 1.0

    hide lilly
    with charaexit

    scene bg suburb_konbiniint
    with shorttimeskip
    
    play music music_daily fadein 4.0

    "Storewoman" "Welcome!"

    show lilly basic_smile
    with charaenter

    hi "Now, I suppose I'll get my stuff first and Hanako's on the second round."

    li "Mind if I tag along with you?"

    hi "Hmm? Ah… sure."

    "I grab two well-used red baskets from the small stack beside the entrance, handing one to Lilly."

    hide lilly
    with charaexit

    "She lays it on the ground, putting her schoolbag in and sliding her cane between the basket and handles before picking it back up in her right hand."

    "Wait, if she doesn't use her cane…"

    "Before I can complete the thought, she hooks her free arm around mine and gives a small nod of appreciation."

    show lilly basic_smileclosed at center
    with charaenter

    li "Shall we?"

    $ renpy.music.set_volume(1.0, 2.0, channel='music')

    hi "Ah, sure."

    "As we navigate around the store, the odd person occasionally passing us throws a quick glance our way as we go."

    "I guess the Yamaku Academy uniform and the admittedly not-half-bad looking blonde attached to my arm are a double-hit combo."

    "As we reach each isle, I quickly check with Lilly what she needs and grab it along with what I'm wanting, putting our items into their respective baskets."

    "I guess this is the same routine she and Hanako follow every Friday."

    "Come to think of it, Hanako would pretty much be a necessity for her to navigate the store and get what she wants."

    hi "Righto, all that's left is the bread and that should be both lists done. You needing anything else, Lilly?"

    li "No, this should be everything."

    hi "Off we go, then."

    "With a quick side-trip to the bakery section, we make our way to the registers."

    "As per usual, only one register's open and there's a queue a mile long."

    hi "Damn."

    show lilly basic_smileclosed
    with charachange

    "Lilly tilts her head inquisitively."

    hi "Ah, there's a queue. Looks like it'll be a bit of a wait."

    show lilly basic_oops
    with charachange

    li "There always is at this time, it seems."

    "Sharing the same faces of resignation, we relucantly take our place at the end or the line."

    $ renpy.music.set_volume(0.5, 10.0, channel='music')

    hide lilly
    with charaexit

    "One person finishes, the line moves up."

    "Another person finishes, the line moves up."

    "By the time we finally each the head of the line, I'm so close to dozing off Lilly has to gently pat me on the back for me to move up."

    show lilly basic_concerned
    with charaenter

    li "Hisao. Hisao!"
    
    $ renpy.music.set_volume(1.0, 0.29999999999999999, channel='music')

    hi "Hmm? Ah, sorry."

    hide lilly
    with charaexit

    "She gives a short sigh of consternation as I move up, Hanako and I's groceries being put into separate bags."

    scene bg suburb_konbiniext
    with locationchange

    "Storewoman" "Thank you for shopping at our establishment, have a nice day!"
    
    stop music fadeout 5.0

    scene bg suburb_konbiniext_ni 
    show lilly basic_smileclosed
    with locationskip

    "By the time we emerge from the store, Lilly's holding a single bag as I struggle to carry all four, both hands well and truly full."

    "Even without looking upwards it's obvious that a surprising amount of time's passed, the dark road outside being lit by streetlamps."

    "As Lilly retrieves her cane we set out back to the dormitories the way we came, leaving the welcoming warm glow of the store."

    scene bg school_road_ni
    with locationchange

    "Despite the road being bereft of cars, the full bags well and truly make of for the lack of noise, clanking and squeaking together constantly."

    show lilly cane_ara
    with charaenter

    li "My my, Hisao, it's good to see you're eating well."

    hi "I'm a growing guy after all, I need to eat all I can!"

    show lilly cane_reminisce
    with charachange

    li "Hmm, it must be nice, being a man."

    hi "W—What?"

    "Seemingly not noticing, or ignoring, my surprise at the completely out-of-left-field question, she continues on without missing a beat."

    show lilly cane_smile
    with charachange

    li "Weight doesn't really bother you when eating, most of the time."

    hi "Ah, I get what you mean. Women tend to worry about stuff like that more than we do, I guess."

    show lilly cane_ara
    with charachange

    li "Exactly. It makes me somewhat envious to be honest."

    hi "Well, it's not like we can outright ignore it."

    "With an affirmative nod, we continue on our walk."

    show lilly cane_smileclosed
    with charachange

    li "Ah, that's right."

    hi "Hmm?"

    show lilly cane_smile
    with charachange

    li "I haven't given you your invitation yet."

    hi "In…vitation?"

    li "Hmm, I suppose it would be okay to just tell you."

    hi "Tell me what?"

    show lilly cane_cheerful
    with charachange
    
    li "Hisao, you are cordially invited to my birthday party."

    "Now she's laying it on, even for her."

    hi "Ah, you're birthday's coming up? When is it?"

    li "Wednesday."

    hi "Next Wednesday, I assume?"

    li "No, this Wednesday."

    hi "Oh."

    hi "…You know, you should probably tell people these kinds of things in advance."
    
    show lilly cane_cheerfulblush

    li "My birthday isn't such a big event, is it? We'll only be having a small meeting after school in my dormitory."

    hi "Now listen here…"

    "I begin to launch into a scolding, but suddenly realize something."

    show lilly cane_planned
    with charachange

    hi "Wait, how old are you? Turning, that is?"

    li "Eighteen."

    hi "How'd you spend your seventeenth birthday then?"

    show lilly cane_reminisce
    with charachange

    li "Hmm,"

    "She looks downward slightly, lost in thought for a few seconds as she recalls the event."

    li "As far as I remember, it was just Hanako and I having a little party during the night after school."

    show lilly basic_smile
    with charachange

    hi "You know, your birthday's supposed to be a big event, geez."

    hide lilly
    with charaexit

    "Sounds like a pretty lonely way to spend a birthday."

    "Just she and Hanako staying overnight."

    "Having a little party."

    "In her dormitory."

    "All alone."

    scene pink
    with locationchange #dissolve

    return

label en_L11h:

    # Event CG

    scene black
    with dissolve

    li "Hanako…"

    "Affectionately pawing Hanako's face with the backs of her fingers, her face looms barely inches above Hanako's face."

    "Hanako's amethyst eyes shy away to the side, unable to meet the gentle gaze of Lilly."

    "Her hair gently brushed aside, the cheek-born scars play their familiar melody across her face, an unseen rhapsody in red."

    "Nervously held to her chest, her arms tense slightly, her breasts filling out around the smooth backs of her hands."

    ha "L—Lilly… please…"

    "Taking the side of her face in the palm of her hand, her delicate pale lips brush those of Hanako."

    "Hanako's body relaxes, and for a fleeting second, Lilly's breath gently caresses her face."

    "As she pulls back, Hanako returns her gentle gaze."

    "Lilly leans in for another kiss."

    "This time though, it overflows with passion, a lustful grab for Hanako's breath."

    ha "Mmmmm… Mmm…"

    "Lilly's lust flows over into Hanako, the last vestiges of resistance dissolving in the onslaught."

    "What was a trickle of desire is now a raging torrent of passion, the atmosphere between the two changing perceptibly."

    "Hanako slowly raises her arms to hold Lilly's snow-white back, her fingers as touching the flawless skin of her pale shoulderblades."

    "Slowly withdrawing her lips from those of Hanako, Lilly slowly lowers herself to Hanako's full breasts."

    "The hands on Lilly's back helplessly slide off and onto the bed, the gaze of her companion transfixed upon her."

    li "My my, Hanako, such a beautiful body…"

    "A deep breath is the only answer to be given, and the only answer required."

    "She brings her mouth to the nipple of Hanako's right breast, her body tensing slightly as she does."

    "Sliding her mouth over, she closes her eyes as she savours the slight texture."

    "Hanako's breathing becomes deeper as she gently moves her lips left to right, the half-erect nipple giving slightly each way."

    "A slight shudder hails Lilly's tongue touching the tip, affectionately toying with it in her mouth."

    "Backwards and forwards, she gently moves her tongue over the delicate nub, wettening it as it grows ever-so-slightly."

    "She pulls back, sliding her hand back over the wettened breast and smoothly fondling it as she places a featherlike kiss between her soft, smooth breasts."

    li "Hanako, you're so beautiful…"

    ha "L… Lilly… Mmm… please, stop…"

    "Ignoring her objections, she moves her head down Hanako's body, sliding her hand down her side."

    "Affectionately pecking the smooth chest of Hanako as she goes, her last kiss is atop the whispy field between her legs."

    "As a pale hand makes its way around her pronounced curves, Hanako's breath catches as it passes her hip and stops at her thigh."

    "Shuffling backward, Lilly frees her other hand and gently feels down the left side just as smoothly as the right."

    "With the gentleness of a mother nursing a newborn, she rubs the outside of Hanako's legs."

    ha "Mm… Li… Lilly… please…"

    "Her hands gripping the pale white sheets, her breathing becomes even more uneven than before."

    li "My my, you're so sensitive, Hanako."

    ha "L—lilly… Mmm…"

    li "You're so cute, Hanako."

    "Circling her hands on the inside of Hanako's thighs, she gently moves her head forward."

    "Her face makes its way towards the delicate folds between Hanako's legs, already well-dampened."

    "A moment's pause, the labored breathing from above only heightening the excitement, before she moveds forward that last inch."

    "She delicately brings her tongue to the delicate nub in front of her, expertly finding it within the folds of skin."

    ha "Ah! Mmm… p—please… Mmmmn…"

    "Barely able to form a sentence, she surrenders herself to the trickle of pleasure from below, gripping the sheets ever tighter."

    ha "Mmm… Nnn… H—Hah…"

    "Lilly gently removes a hand from atop its resting place, cupping two fingers below her mouth."

    "She pushes them forward slowly, past the initial resistance of her wettened outside."

    ha "Ah, n—no! Please… ah… hah…"

    "As they move in, they give an unrefined, sloppy sound, contrasting to the barely audible licking of her tongue."

    "Once inside they easily move inwards, the warmth from the soft, wet skin almost welcoming them inside."

    "Hanako's delicate body moves slightly on the stained sheets in rythm with the gentle lapping over her most delicate area."

    "As she slowly moves her fingers outwards and inwards, Lilly's cheeks become even more flushed than before, all the more visible on her pale white skin."

    li "My my… Hana… chan…"

    "The excitement flowing into her breathless speech, she squirms her legs, the wetness of her thighs telling of her unbridled lust."

    ha "L—Lilly… Mmmmm… Nn…"

    "Hanako's voice takes on a sharper edge, her excitement rising rapidly."

    ha "Ah, ah, Lilly… ah! Aaaah!"

    li "It's alright, Hanako… Whenever you want to…"

    ha "Ah!… Ah… Nnnnn…"

    "She begins to squirm in excitement, her thoughts frantic and incoherent."

    ha "Lilly! Ah! Aaaah!"

    "Lilly raises her head one final time, taking pleasure from the rapture so tangibly close."

    "She withdraws her tongue and stills her fingers for a second before unleashing an assault upon Hanako's senses, her tongue vibrating quickly."

    ha "Ah! Lilly, I'm… Ah! Aaaaah! Aaaaaaaah!"

    #Fade to white
    scene white
    with Dissolve(4.0)

    return

label en_L11xh:

    scene bg school_road_ni
    with dissolve

    show lilly basic_concerned_ni
    with charaenter

    li "Hisao! Hisao!"

    "I blink my eyes frantically as I return to the world of reality"

    "Okay, let's see here…"

    "Walking, check. Carrying groceries, check. Lilly's beside me, check. My cheeks are flushed, check. My breathing is heavy, check."

    "Wait, that's not good! Not good!"

    hi "Ah, sorry Lilly."

    "As I turn to face her, I suddenly avert my head."

    show lilly basic_concerned at tworight
    show bg school_road at bgright
    with charamove

    "It's kind of embarassing to look at her just after something like… that."

    "She gives another sigh of consternation."

    show lilly basic_oops at tworight
    with charachange

    li "Hisao, what in the world was wrong?"

    hi "Ah, well, uh…"

    "She leans in uncomfortably close."

    show lilly basic_concerned at tworight
    with charachange

    li "Why are you facing away from me?"

    "Ah shoot, she must have heard my voice being directed away from her."

    #"Time for evasive action, I've got to get her off me…"
    return

label en_choiceL11:
    #Choices
    #[1] "I was just daydreaming."
    #[2] "It's nothing."
    #[3] "Tell the truth."
    menu:
        with menueffect

        "Time for evasive action, I've got to get her off me…"

        "I was just daydreaming.":
            return m1

        "It's nothing.":
            return m2

        "Tell the truth.":
            return m3

label en_L11a:
    #Choice [1]

    show lilly basic_concerned at center
    show bg school_road at center
    with charamove

    hi "I was just daydreaming, don't worry."

    li "Hmm?"

    show lilly basic_smile at tworight
    show bg school_road at bgright
    with charamove

    "She leans in even closer, forcing me to move sideways."

    hi "I—it's true, geez."

    li "And who or what, pray tell, was Hisao dreaming about?"

    "Erk. Why must this girl be so observant?"
    
    show lilly basic_giggle

    "Glancing back at her face though, she wears a cute, playful smile."

    "She's… playing with me?"

    "Come on Hisao, think, there's got to be a way out of this."

    #hi "Ah, I was just daydreaming about…"

    return

label en_choiceL11a:
    #More choices
    #[1A] "You."
    #[1B] "You and Hanako."
    #[1C] "Tell the whole truth."
    menu:
        with menueffect

        hi "Ah, I was just daydreaming about…"

        "You.":
            return m1

        "You and Hanako.":
            return m2

        "Tell the whole truth.":
            return m3

label en_L11aa:
    #Choice [1A]

    show lilly basic_smile at center
    show bg school_road at center
    with charamove

    hi "Well… you."

    li "Ah, um,"

    show lilly basic_emb
    with charachange

    "She suddenly looks downward and blushes furiously."

    li "My my, Hisao…"

    "She brings her hand to the side of her face in embarassment."

    "Just how much did she work out about that dream anyway?"
    
    show lilly back_smileclosed
    with charachange

    "I grimace as I watch Lilly continue on walking silently, her face a mixture between dazed and embarassed, her hand still on her cheek."

    return

label en_L11ab:
    #Choice [1B]

    hi "I was dreaming of, uh, you. And Hanako."

    "She suddenly raises her eyebrows questioningly."

    show lilly basic_concerned
    with charachange

    li "Hanako and I, you say?"

    hi "Yeah, just you two having one of your tea parties for your birthday."

    "Please don't drill me on it. Please. Please. Please."

    "Though considering the tightness of my voice though, I have doubts any conclusion could be drawn other than the right one."

    li "Hmm…"

    show lilly basic_smileclosed
    with charachange
    
    with Pause (5.0)
    
    show lilly back_smileclosed
    with charachange

    "She looks back and continues walking."
    

    "I desperately try to read her face, but for the life of me I can't figure out what she's thinking."

    "Is she pissed? Embarassed?"

    "I give a small sigh."

    "She seems to have a way of putting a shield around her, making her completely incalculable."

    return

label en_L11b:
    #Choice [2]

    show lilly basic_smile at center
    show bg school_road at center
    with charamove

    hi "It's nothing, really."

    show lilly basic_smileclosed
    with charachange

    li "Hmm~"

    #"Dammit, she's not going to let it go."

    return

label en_choiceL11b:
    #Even more choices
    #[2A] "Clam up."
    #[2B] "Spill everything."
    menu:
        with menueffect

        "Dammit, she's not going to let it go."

        "Clam up.":
            return m1

        "Spill everything.":
            return m2

label en_L11ba:
    #[2A]

    hi "I told you, it's nothing."

    show lilly basic_concerned
    with charachange

    "Lilly furrows her brow disapprovingly."

    li "Is that so?"

    hi "Yes, it is."

    li "You know lying is bad for you, Hisao."

    hi "I know, I know."

    show lilly basic_smileclosed
    with charachange

    li "Well, I think I can forgive you just this once."

    hi "For…give?"

    show lilly basic_giggle
    with charachange

    "She giggles slightly. Just what is she thinking now?"

    show lilly back_smileclosed
    with charachange
    "I look up to the dark sky as I slump my shoulders."

    "Even as we walk though, I can't help but remember snippets of that wonderful daydream."

    return

label en_L11c:
    #Choice [3]

    show lilly basic_smile at center
    show bg school_road at center
    with charamove

    hi "Well… um… It was kind of you… And Hanako… And you were in your room… Doing… stuff."

    "My throat tightens as I speak, barely letting me squeak out the words."

    "I turn to Lilly, surveying her reaction."

    show lilly basic_emb
    with charachange

    "Forcing herself to look forward, she's blushing quite a bit."

    "Her face seems to have a tiny, almost imperceptible smile."

    hi "…Lilly?"

    show lilly basic_smileclosed
    with charachange

    li "Hmm, so you're a man after all."

    hi "Wait, what's that supposed to mean?"

    hide lilly
    with charaexit

    "She suddenly runs ahead of me and turns, blocking me off."

    "With an adorable smile, she holds her hands behind her as she leans forwards."

    show lilly basic_smile
    with charaenter

    li "No~thing!"

    "She turns back and continues to walk ahead of me, a newfound spring in her step."

    hide lilly
    with charaexit

    "All I can do is raise an eyebrow and give a dazed grin."

    "I don't think I've ever seen this playful and teasing side of her before."

    "As I watch her make her way up the street, I give an indulgent smile."

    "It's a nice side to her."

    return

label en_L11x:

    #End choice sections

    scene bg school_girlsdormhall
    with locationskip

    "Eventually we get to the student dorms, my arms both aching from the weight of two sets of groceries."

    hi "Hah… We're finally here. Phew."

    "I band down to wipe my forehead with the back of my hand."

    "As Lilly stops in front of her door and sets down her bag, she fishes around in her pocket for the key."

    "I turn back to the door in front of me and proceed to knock twice, the bags still in my hand clunking together loudly."

    "After a couple of seconds, the door slowly opens."

    "Though if one weren't looking closely they could be forgiven for thinking it hadn't been moved at all."

    "I twist my head to the side to try and peer through the tiny sliver of a gap between the door and the doorframe."

    hi "Hey Hanako, I've got your stuff."

    ha "Ah!"

    "With that, she opens the door fully, her plain room visible over her shoulder."

    scene bg school_dormhanako
    with locationchange

    show hanako basic_bashful
    with charaenter

    "Sparsly decorated, it's probably even more unremarkable than my room."

    "I hold out my right arm, both bags almost pulling it straight back down with their weight."

    ha "Ah, t—thank you… Hisao."

    "I pass the bags to her, and after the initial transfer of weight she manages to take them easily."

    hi "Hey, no problem. Oh, I met Lilly on the way, she wanted to say sorry for not meeting you to go down there."

    "She quickly shakes her head from side to side."

    show hanako emb_smile
    with charachange

    ha "No, that's fine."

    hi "Uh… huh. Well, I'll be off then. 'Night, Hanako."

    ha "Good night, Hisao."

    "With a deep bow, her groceries held in both hands, I step back and shut the door."

    hide hanako
    with charaexit

    scene bg school_dormhisao
    with locationskip

    "Making my way back to my own dorm, I drop my bags onto the floor with a measure of relief."

    "So, Lilly's birthday's tomorrow."

    "I suppose I'll pick something up for her after school."

    scene black
    with dissolve

    return

label en_L12:

    scene bg city_street1
    with shorttimeskip
    
    $ renpy.music.set_volume(1.0, 1.0, channel='ambient')
    
    play ambient sfx_traffic fadein 2.0

    "Television" "And now we introduce the lovely Mizuki Nanao!"

    "Television" "Hi everyone!"

    "Television" "So, Nanao, are you excited about the reception your…"

    "How banal."

    "I pull myself away from the television facing the streetside with little effort."

    "Compared to life in Yamaku, the town seems like an entirely different world."

    "While Yamaku may have its fair share of hustle and bustle, the shopping arcade's on an altogether different scale."

    "Not to mention the all-too-obvious other differences."
    
    "As I walk past innumerable shops and restaurants, I give only a quick glance to each before continuing on."

    "…Just as I've been doing for an hour already."

    "Present shopping isn't exactly my forte, I guess."

    "Every shop is the same."
    
    
    show bg city_street2
    with locationchange

    "A bright, boldly-colored sign announcing the name and its wares, hoping to rope in unsuspecting customers with sales and the latest modernities. Inside, nothing but gadgets and useless trinkets."

    "I feel like I'm going to expire from this damn heat, too."

    "What an atrocious day."

    "Minutes pass, going past one store to another."

    "Walking across one raised walkway, only to go across another in short measure."

    show bg city_street3
    with locationchange

    "I guess it'd help if I had much idea of the area."

    "Having only moved here less than a month ago, and not having been around town much except for Lilly's outings, I still don't quite know the lay of the land."

    "Finally, I come to a small store beside a newsagency."

    "For once the store windows aren't filled with electronics and computer games, but dolls, stuffed bears and all manner of wood-crafted oddities."

    hi "Othello's… Antiques."

    "An antique store?"

    "Well, if there's anything in this town that'd suit her, I guess it'd be here."

    "I did briefly consider getting a cello for her."

    "A quick search online for prices killed that idea though."

    scene bg city_othello
    with locationchange
    
    stop ambient fadeout 0.5
    
    scene bg city_othello at left
    with locationskip
    
    play sound sfx_storebell
    
    play music music_soothing fadein 0.5

    "As I push the thick wooden door forwards and enter the store, a bell above me rings out."

    "The musty smell of old books and wooden shelves is distinctly anachronistic."

    "Storeowner" "Ah, Welcome!"

    "I look to my left to see an aging man with whitened hair and spectacles that look entirely too small behind the large wooden counter, looking up from a small book."

    "To say he fits the look of his surroundings would be a good description."

    "I politely nod and turn to look around the store."

    "It's quite a bit larger than it looked from the outside, with three large shelves in the middle and wide tables around the outside."

    "Slowly walking and crouching down, I examine the table inside the shop window."

    "At least thirty small dolls, each about the size of an outstretched hand. There doesn't seem to be much variety in terms of make, all of them being ceramic and designed in the same way."

    "The only thing that separates them is their clothing, which spans all the colors of the rainbow and every time period from baroque to modern."

    "Even to my untrained eye, they're of exquisite quality."

    "Putting my tongue to me cheek in thought, I carefully take the price tag attached by a string to one of them to see the price."

    "I grimace."

    "Looks like these are out of the question."

    "Letting out a disappointed breath, I rest the tag on the table, stand, and turn behind me to survey the shelf."

    "Stuffed teddy-bears. Now there's a possibility."

    "I didn't see any in her room the last time I was in there, from memory, despite seeing a good number of porclain dolls, so I guess it's unlikely Hanako would give her one."

    "I look at them closely, occasionally giving them a light rub to see how they feel."

    "One in particular stands out, extremely soft to the touch and well-made."

    "Taking a hold of the tag, I note the name written in cursive English."

    "Steiff… I've heard of that somewhere."

    "As soon as I flip it over though, a familiar pang of disappointment rises again."

    "Damnit."

    "Is there anything in this cursed store I can actually afford?"

    "Though, I guess it's less the store's fault and more mine for having such a paltry budget."

    "Pocket money can only go so far, and my meds cost a rediculous amount to start with."

    show bg city_othello at left
    with None
    
    "I walk around to the table at the far end of the store, this time covered by all manner of wooden clocks."

    "Furrowing my brow as I crouch, I closely examine one that catches my eye."

    "A miniature grandfather clock, complete with moving pendulum."

    "Inside the small glass bubble are the brass minute and hour hands, intricate designs engraved on both."

    "I can only stare at the workmanship that's gone into such a beautiful thing, and for a moment forget the reason I even came into the store."
    
    stop music fadeout 2.0

    "After a minute or two of staring though, I manage to recollect myself, standing and taking a gander at the shelf behind me."

    "Woodcrafts—posable dolls, small kid's toys and sculptures—populate it."

    "As I look through them though, I notice a small box tucked away behind a toy car."

    "I gingerly reach back and pull it out, admiring the intricately carved patterns on the dark, varnished wood as I do."
    
    show musicbox closed at center
    with Pause (1.0)

    "For a moment, I simply stand and admire it, slowly bringing my other hand to open the lid."
    
    show musicbox open at center
    with charachange

    "It only takes a tiny movement to send the springs popping open the lid."

    play music music_musicbox fadein 3.0

    "…"

    "I stare in amazement at the small cylinder inside as it turns around, tiny metal blocks dotting its surface."

    hi "This tune…"

    "Shopkeeper" "Ah, the Saraband."
    
    show shopkeep neutral at left
    with charaenter

    "I look to my left to see the shopkeeper looking at the music box, adjusting his small spectacles."

    "Shopkeeper" "Not the most popular piece, I'm afraid."

    hi "I'm surprised there's a music box for it."

    show shopkeep surprised at left
    with charachange
    
    "Shopkeeper" "You know it?"

    hi "Kind of. A dance, wasn't it?"

    show shopkeep happy at left
    with charachange
    
    "Shopkeeper" "Well now, it is rare to see someone who knows their stuff these days."

    hi "Ah, no, I just… know someone that does."

    show shopkeep neutral at left
    with charachange
    
    "Shopkeeper" "I see."
    
    hide shopkeep

    stop music fadeout 0.5
    
    play sound sfx_switch


    "I carefully shut the lid, feeling a ting of regret as the lid snaps shut and ends the small performance."

    "Turning it around to inspect the delicate pattern, I notice something glinting in the dim light underneath."

    "A brass plate?"

    hi "Ah, sir…"
    
    show shopkeep neutral at left
    with charaenter

    "Shopkeeper" "Yes?"

    hi "Would it be possible to have a name engraved on this?"

    "Shopkeeper" "Certainly, my lad. Give it here and I'll do it now if you'd like."

    "I carefully hand over the box with both hands, treating it as if it were as delicate as a raw egg."

    "Taking it in his slightly wrinkled hands, the old man makes his way to the counter and takes a small handheld drill from behind his shoulder."

    "Wiggling slightly to get himself in position, readying the drill in his hand, he looks up past his glasses at me"
    
    show bg city_othello at center
    
    show shopkeep neutral at center
    with charamove

    "Shopkeeper" "So, what would you like engraved?"

    hi "“Lilly,” please. Uh, could you do it in English?"

    "He gives a wry smile."
    
    show shopkeep happy at center
    with charachange
    
    "Shopkeeper" "Ah, so it's for a little lass, eh? Sure, I'll see what I can do."

    stop music fadeout 0.5
    #play sound sfx_drill.ogg
    
    "With a flick of his thumb, the noise of the drill reverberates through the once-silent room."

    show shopkeep thinking at center
    with charachange
    
    "I stand watching him, transfixed by the assuredness of his work."

    "Despite his hands looking frail and old, he guides the drill with the precision of a surgeon's scalpel."

    "For him, this is a labor of love."

    "I smile, though even as I do the corner of my mouth falters."

    "It must be nice to have something to devote oneself wholeheartedly to."

    "To find something that you take joy in doing, no matter how many years you spend doing it."

    stop ambient fadeout 0.5
    "As the noise suddenly trails off, I come to my senses."

    "To be having such thoughts while shopping in town."

    "How ridiculous."

    "He gently blows on the bass plate, small shavings flying onto the desk in front of him, and hoists it above his face to inspect closely."

    "Shopkeeper" "Well, that should be it. Want to take a look?"

    "I walk up and take the music box, turning it over to admire his handiwork."

    "L—I—L—L—Y"

    "Written in cursive script, I can't see a single fault."

    hi "Amazing. That's perfect."
    
    show shopkeep happy at center
    with charachange

    "He looks up to me and smiles."

    "Shopkeeper" "You expected any different?"

    "As he chuckles, I suddenly realise something I should've asked much earlier."

    hi "Ah, I guess it's kind of wierd to be asking this now, but… how much will this cost?"
    
    show shopkeep thinking at center
    with charachange

    "Shopkeeper" "Hmm… Well, if it's for a little lass, I can't see how I could ask for more than five thousand, five hundred yen."

    "I breath a sigh of relief."

    "It's obvious it really costs more."

    hi "Thank you, sir."

    "Shopkeeper" "Pleased to be of service."

    "I give it to him to bag and give a deep bow as I leave the store."
    
    hide shopkeep
    
    scene bg city_street3
    with locationchange
    
    play sound sfx_storebell
    
    $ renpy.music.set_volume(0.2000001, 0.0, channel='ambient')
    
    play ambient sfx_traffic fadein 2.0
    
    "The familiar ding of the bell signals my departure, a small white bag in hand."

    "I walk through the sunset-tinted town, squinting at the sudden change in light level."

    "Well, it looks like that little expedition turned out well in the end."

    "I take my time walking across the raised walkways, as much out of the nice view as the fact that I'm tired as hell from all the walking before."
    
    show bg city_street4
    with locationchange

    "I absentmindedly yawn, passing yet another shop."

    "Okay, I've got a present for her."

    "Unfortunately, that doesn't really solve the other problem."

    "Yet another lonely birthday in her room…"

    "With Hanako…"

    "No! Bad Hisao! Focus!"

    "I clench my eyes and quickly shake the image out of my mind."

    "Let's see… it's after school for one, so organising an outing at the last minute could be hard."

    "Hmm, now that's an idea."

    "My room's somewhat bare, but it'd be a change to what she's used too."

    "I suppose I could get Hanako to tell her sometime tomorrow."

    "Yeah, that sound like it'd…"

    "Girl" "Ah! You stupid thing!"

    "As I walk down the street on the final leg to the school, I hear a voice coming from around the corner."

    "Furrowing my brow, I pick up my pace to see what's wrong."

    "Girl" "Geez, it's always at the worst times."

    "Girl" "Come on, start you damn…"

    "Just as I start to round the corner a series of hard, metallic thuds ring out."

    "Girl" "Stupid, stupid, stupid, stupid—" #reminder for the potential {nw} break

    scene bg city_street2
    with locationchange

    hi "…Yuuko?"

    "I instantly recognise the figure in front of me, frozen midway into kicking the green Vespa in front of her."

    "Her face has several streaks of oil on it, and the top half of her clothing's well and truly stained."

    yu "Ah…"

    "She collects herself and narrows her eyes as she stares."

    yu "I swear I've seen you before…"

    "I stand still silently, waiting for her to remember."

    "Geez, it was only the day before yesterday."

    yu "Ah, it's you."

    "She holds out her palm, bringing her fist down on it in realisation."

    yu "Hisuou."

    "Well, she came close."

    hi "Hisao. A-O."

    yu "Ah, sorry. I'm not good with names. I always forget them."

    "I couldn't guess."

    hi "It's fine. What's wrong with your scooter?"

    yu "Hmm? Ah, this thing."

    "We both look down at it, the small black engine visible thanks to a small rectangular panel having been removed from the side underneath the seat and placed placed on the ground beside it."

    yu "I was finally going home after a damned long day at work and it broke down. Again. For the fifth time this month."

    hi "Want some help? I'm no mechanic, but I guess another look wouldn't hurt."

    "No mechanic is putting it lightly. I know what each part does and where it goes… roughly."

    "Still, I can't just leave her stranded here without at least trying to help."

    yu "Well, you're welcome to look at it. I doubt it'll do much good though."

    "We both crouch down, with me carefully setting the bag in my hand aside whilst crouching to avoid my uniform getting stained."

    hi "Okay, let's have a look here."

    "First thing's first, there's a fan."

    "I guess that cools the engine."

    "I gently reach in and move it back and forward a bit with my finger."

    "Okay, it's moving. Next."

    "There's a wire coming out the top, so I suppose that goes to the spark plug."

    hi "Spark plug okay?"

    yu "Yep, switched it out and still no luck."

    hi "Hmm…"

    "I return to trying my hardest to look like I know what I'm doing."

    "This is hopeless."

    "I guess it's worth checking the basics, just to make sure."

    hi "Does it start at all?"

    yu "Yeah, it starts, sputters a bit and then dies."

    "She takes her hair with both her oil-stained hands and ruffs it up in frustration."

    "Now she's got both messed-up and oiled-up hair."

    "I quickly distract myself to stop from laughing."

    hi "Um, okay, could you start it so I can hear what it does?"

    yu "Sure, hold on a sec."

    "Oh God, please let it be something simple, please, please, please."

    "She walks around me and starts the engine in short measure."

    "Huh. Everything looks fine."

    "I stand up and walk around to her, glancing over her shoulder at the dials on the handles."

    "My expression becomes flat."

    hi "Yuuko."

    yu "Yeah?"

    hi "Look at the fuel guage."

    yu "Hmm?"

    "As she turns back around to check, she blushes furiously."

    yu "…Ah."

    hi "Well, at least that solves that—" #reminder for the potential {nw} break

    "Before I can hope to complete the sentence, she spins around and flings her arms around me."

    "Though it's probably closer to a wrestler's body-grab than any kind of hug I know."

    yu "Thank you, Hisao! Thank you! Thank you! Thank you! I was going to be late for studying and I was going to have to miss dinner and thank you, thank you thank you!"

    hi "Ah, i—it's okay, really."

    "I can barely force the words out through my lungs being forced inwards."

    "Even as I say that though, I can't help but notice a small detail."

    "Or rather, two small details."

    "Come to think of it, they'd actually be two quite large details."

    "Two large details tightly pressed against my chest."

    hi "Y—Yuuko, it's okay."

    "I'm in heaven."

    yu "Thank you, thank you, thank you!"

    "Thank you, God, for this wonderful moment."

    hi "Yuuko, p—please…"

    "Heaven~"

    "After what seems to be altogether too short a time, she finally releases me from her deathgrip."

    "I take a deep breath to refill my suddenly freed lungs, and to quickly reorient my tostesterone-driven mind."

    yu "Ah, sorry, I got overexcited. I always do that, ah, sorry! I'm sorry!"

    hi "It's okay, seriously."

    "I really can't fathom this girl."

    #Yuukohappy.png

    yu "Thank goodness, now I actually have a chance of getting that thesis done."

    #Yuukodespair.png

    yu "Well, more of a chance than I had before."

    #Yuukoabsolutedespair.png

    yu "Though considering I haven't even started and I only have two days to get it done…"

    #Yuukoabsoluteallencompassingdespair.png

    yu "Ah! I'm completely screwed! Help me, Hisao~"

    "I cautiously take a step back from the girl seemingly on the verge of tears, her arms helplessly reaching out to me."

    hi "Ah, I—I—I don't even know what the thesis is on, I can't…"

    "Her eyes suddenly focus on the almost completely hidden watch on my wrist."

    yu "Ah! The time!"

    "She quickly looks back to the handle on the Vespa, a small digital clock that's obviously tacked on by tape being precariously attached to it."

    yu "Uwah! I need to go, I need to go now!"

    hi "Uh… huh."

    "I raise an eyebrow, reduced to merely watching this hopeless girl."

    "Ducking down, she expertly places the removed panel back in place as I stare worryingly at the fact she screws in the four corner screws with nothing but her fingers to tighten them."

    "Seemingly not noticing my apprehension, she grabs her red and white helmet from the far handle and slides it onto her head, leaving the straps to dangle uselessly beside her face."

    "A green Vespa, and a white helmet with a red stripe down the middle."

    "It's worrying that a blind person has better color coordination than she does."

    yu "Yo, Hisao?"

    hi "Yeah?"

    yu "Thanks for the help."

    hi "Nah, no problem. It's not like I really did that much."

    "As she begins to walk her Vespa home, she stops and turns back."

    yu "Oh, you know about Lilly's birthday, right?"

    hi "Yeah, tomorrow."

    yu "Ah, good. It's good to see she's finally gotten herself a man."

    yu "Well, seeya Hisao. Tell her I send my regards. I'd come, but university's got me by the neck."

    hi "No problem. Seeya."

    "With that, she slowly walks past me, Vespa in hand."

    "I bend down and grab the bag off the ground, checking my knees for any oil stains."

    "Well, time to…"

    #Some sort of flashback effect or something here, I suppose.

    yu "It's good to see she's finally gotten herself a man."

    #End flashback effect, if any

    "Wait, what did she—" #reminder for the potential {nw} break

    "I look back, only to see her muttering to herself as she walks away"

    "Damn, now she's gone and gotten the wrong idea."

    "She's older than any of us, yet she seems just as hopeless as Hanako at times."

    "…"

    "Still, I can't help but mull the idea over."

    "I give a yawn and start off towards the dorms once again."

    "As I walk down the orange-tinted street though, there's a familiar small spring in my step."
    
    stop ambient fadeout 3.0 # [str]
    
    scene black
    with dissolve

    return