# This is the I-Machine, the flow control script for KS.
# Dedicated to Irina ~<3

# this is the new version. See the old one for documentation.

# Start of the actual script and entry point for a new game. Don't change.
label imachine:
    jump_out NOP1


# From here on, actual scene labels.

#######################
#        ACT 1        #
#######################

# Monday
label NOP1: #Out Cold
    call iscene ("NOP1")
    jump_out op_video

label op_video:
    $ renpy.movie_cutscene(vid_op)
    $ renpy.pause(1.0)
    jump_out NOP2

label NOP2: #Bundle Of Hisao
    call iscene ("NOP2")
    jump_out A1
    
label A1: #Gateway Effect
    $ renpy.movie_cutscene(vid_tca1) # [str]
    $ renpy.pause(1.0) # [str]
    #$ tcard(1, "all")
    call iscene ("A1")
    call imenu ("choiceA1")
    #mu "Do you want to introduce yourself to the class?"
    if _return == m1:
         # "Why?":
        call iscene ("A1a")
    else:
        #"Yeah, of course.":
        $ attraction_sc += 1
        call iscene ("A1b")
    call iscene ("A1c")
    jump_out A2
    
label A2: #Enter Stage Left
    call iscene ("A2")
    if seen_scene ("A1a"):
        call iscene ("A2a")
    else:
        call iscene("A2b")
    call iscene ("A2c")
    if seen_scene ("A1b"):
        call iscene ("A2d")
    else:
        call iscene("A2e")
    call iscene ("A2f")
    jump_out A3
    
label A3: #In The Nursery
    call iscene ("A3")
    call imenu ("choiceA3")
    if _return == m1:
        #Ask about the Library
        $ attraction_hanako += 1
        call iscene ("A3a")
    elif _return == m2:
        #Ask about Shizune's three sizes
        call iscene ("A3b") 
    else:
        #I know everything I need to
        $ attraction_sc += 1
        call iscene ("A3c")
    call iscene ("A3d")
    jump_out A4
    
label A4: #Nobody's Room
    call iscene ("A4")
    #call imenu ("choiceA4")
        #ke "It's a lot better that way, keeping only to yourself. You never know who will get you."
    #if _return == m1:
        #"Does that mean I should not get to know you either?":
       # $ attraction_sc +=1
        #call iscene ("A4a")
    #else:
        #"That doesn't make any sense.":
       # $ attraction_fail += 1
        #call iscene ("A4b")
    #call iscene ("A4c")
    jump_out A5


# Tuesday
label A5: #Smalltalk
    call iscene ("timeskip")
    call iscene ("A5")
    jump_out A6
    
label A6: #Risk vd Reward
    call iscene ("A6")
    call imenu ("choiceA6")
        #mi "Not playing like this, you won't~!"       
    if _return == m1:
        #"She has a point. Attack aggressively!":
        $ attraction_sc += 1
        call iscene ("A6a")
    else:
        call iscene ("A6b")
    call iscene ("A6c")
    jump_out A7
    
label A7: #Pseudo Tea Cosy
    call iscene ("A7")
    jump_out A8
    
label A8: #Shared Library
    call iscene ("A8")
    call imenu ("choiceA8")
        #"It takes too many seconds to collect myself and remember what I walked up to her for."
    if _return == m1:
        call iscene ("A8a")
        # "Hi! I'm new here. Hisao Nakai. We're in the same class.":
        if seen_scene("A1b"):
            call iscene ("A8aa")
        call iscene ("A8ab")
    else:
        #"I'm sorry, I didn't mean to startle you. ":
        $ attraction_hanako +=1
        call iscene ("A8b")
    call iscene ("A8c")
    if seen_scene ("A8a"):
        call iscene ("A8d")
    else:
        call iscene ("A8e")
    call iscene ("A8f")
    jump_out A9
    
label A9: #Bizarre and Surreal
    call iscene ("A9")
    call imenu ("choiceA9")
    if _return == m1:
        #She was cute
        $ attraction_hanako += 1
        call iscene ("A9a")
    else:
        #She wasn't cute
        call iscene ("A9b")
    call iscene ("A9c")
    jump_out A10


# Wednesday
label A10: #Lunch Evolution Theory
    call iscene ("timeskip")
    call iscene ("A10")
    if attraction_sc > 1 and attraction_hanako > 1:
        call imenu ("choiceA10a")
        if _return == m1:
            call iscene ("A10a")
        elif _return == m2:
            call iscene ("A10b")
            jump_out A11_2
        else:
            call iscene ("A10c")
    elif attraction_sc > 1:
        call imenu ("choiceA10b")
        if _return == m1:
            call iscene ("A10c")
        else:
            call iscene ("A10a")
    elif attraction_hanako > 1:
        call imenu ("choiceA10c")
        if _return == m1:
            call iscene ("A10a")
        else:
            call iscene ("A10b")
            jump_out A11_2
    else:
        call iscene ("A10a")
    jump_out A11_1

label A11_1: #Short Sharp Shock
    call iscene ("A11")
    call iscene ("A11a")
    call iscene ("A11b")
    if seen_scene ("A10c"):
        call iscene ("A11x")
        jump_out A12
    call iscene ("A11y")
    jump_out A15


label A11_2: #Meet Cute
    call iscene ("A11c")
    call iscene ("A11a")
    call iscene ("A11d")
    jump_out A13

label A12: #Detour Ahead
    call iscene ("A12")
    jump_out A16 
   
label A13: #Sip Part 1     
    call iscene ("A13")
    jump_out A15

#there is no A14

label A15: #It Builds CHaracter
    call iscene ("A15")
    jump_out A16
    
label A16: #A Private Lunch
    call iscene ("A16")
    jump_out A17
    
label A17: #Waylay
    call iscene ("A17")
    call imenu ("choiceA17")
        #nk "Can your promise me to be more serious about this from now on?"
    if _return == m1:
        #"Yeah, I promise. Definitely.":
        call iscene ("A17a")
    else:
        #"Maybe":
        call iscene ("A17b")
    call iscene ("A17c")
    jump_out A18
    
label A18: #THe Other Green
    call iscene ("A18")
    jump_out A19

#Thursday
label A19: #THe Running Girl
    call iscene ("timeskip")
    call iscene ("A19")
    if seen_scene ("A17a"):
        call iscene ("A19a")
    else:
        call iscene ("A19b")
    call iscene ("A19c")
    if seen_scene ("A11b"):
        call iscene ("A19i")
    call iscene ("A19j")
    if seen_scene ("A17a"):
        call iscene ("A19d")
    else:
        call iscene ("A19e")
    call iscene ("A19f")
    if seen_scene ("A17a"):
        call iscene ("A19g")
    else:
        call iscene ("A19h")
    jump_out A20
    
label A20: #Soap
    call iscene ("A20")
    jump_out A21
    
label A21: #Cold War
    call iscene ("A21")
    call imenu ("choiceA21")
          #"It seems to me as insulting as it is confusing. She's gone too far this time."
    if _return == m1:
        #"Don't drag me into this!":
        call iscene ("A21a")
        jump_out A22
    call iscene ("A21b")
    if seen_scene ("A13"):
        call iscene ("A21c")
    else:
        call iscene ("A21d")
    jump_out A23

label A22: #Proof of Competency
    call iscene ("A22")
    if not seen_scene ("A12"):
        call iscene ("A22a")
        jump_out A23
    jump_out A22_2

label A22_2: #Event Horizon
    call iscene ("A22b")
    if seen_scene ("A21c"):
        #this is not possible. I wonder what is supposed to be happening. Seems like it works anyway and this call is not even supposed to be doing anything?
        jump_out A24
    jump_out A24_1

label A23: #contentless flow controller, does not have a name or entry in scene select
    if not seen_scene ("A22a"):
        jump_out A23_1
    if not seen_scene ("A21c"):
        jump_out A23_2
    jump_out A24 #needs no condition; we go to 23_2 in that case anyway, which has one

label A23_1: #Above and Beyond
    call iscene ("A23")
    if seen_scene ("A21c"):
        jump_out A24
    jump_out A23_2

label A23_2: #Things you can do
    call iscene ("A23a")
    if seen_scene ("A21c"):
        jump_out A24
    jump_out A24_1

label A24: #Paint by Numbers
    call iscene ("A24")
    if seen_scene ("A21a"):
        #not sure if this is possible either but it doesn't affect the flow so no big deal
        call iscene ("A24c")
    else:
        call iscene ("A24d")
    call iscene ("A24e")
    jump_out A24_1

label A24_1: # this is just a wrapup, no scene select, no lis entry
    if seen_scene("A17a"):
        call iscene ("A24a")
        jump_out A25
    call iscene ("A24b")
    jump_out A26

#Friday
label A25: #Exercise
    call iscene ("timeskip")
    call iscene ("A25")
    call imenu ("choiceA25")
    if _return == m1:
        call iscene ("A25b")
        jump_out A27
    call iscene ("A25a")
    jump_out A26

label A26: #Invisible Hat
    if not seen_scene ("A25"):
        call iscene ("timeskip")
        call iscene ("A26")
    call iscene ("A26a")
    if not seen_scene ("A22b"):
        call iscene ("A26e")
        jump_out A27_2
    jump_out A26_1

label A26_1: #Home Field Advantage
    call iscene ("A26b")
    call imenu ("choiceA26")
        #"What to do?"
    if _return == m1:
     #"Try to dodge subject":
        call iscene ("A26c")
        jump_out A28
    #"Punch Shizune":
    $ attraction_kenji += 1
    call iscene ("A26d")
    jump_out A27_2


label A27: #contentless controller, etc. #No Recovery
    call iscene ("A27")
    if seen_scene ("A22b"):
        jump_out A27_1
    call iscene ("A27e")
    jump_out A29

label A27_1: #Slow Recovery
    call iscene ("A27a")
    call imenu ("choiceA27")
    if _return == m1: 
        call iscene ("A27b")
        $ attraction_kenji += 1
        call iscene ("A27f")
        jump_out A29 
    call iscene ("A27c")
    if seen_scene ("A25b"):
        call imenu ("choice2A27")
        if _return == m1:
             call iscene ("A27h")
             call iscene ("A27e")
             jump_out A29                                     
    call iscene ("A27i")
    jump_out A28

label A27_2: #No Recovery
    call iscene ("A27d")
    if seen_scene ("A26d"):
        call iscene ("A27f")
    else:       
        call iscene ("A27e")
    jump_out A29


label A28: #No Free Lunch
    call iscene ("A28")
    if seen_scene ("A26c"):
        call iscene("A28a")
    call iscene ("A28b")
    jump_out A36

label A29: #Foot and Mouth
    if not seen_scene ("A25b"):
        call iscene ("A29")
        if seen_scene ("A27f"):
            call iscene ("A29x")
    else:
        call iscene ("A29a")
    call iscene ("A29b")
    if seen_scene ("A25b"):
        call iscene ("A29c")
        jump_out A31
    jump_out A30

label A30: #Mind your step
    call iscene ("A30")
    if seen_scene ("A26d") or seen_scene ("A27b"):
        #I'm actually not sure if this is even possible, but the if statement is here as a safeguard
        call iscene ("A30a")
        jump_out A31
    call imenu ("choiceA30")
    if _return == m2:
        $ attraction_kenji += 1
        call iscene ("A30a")
        jump_out A31
    call iscene ("A30b")
    if seen_scene ("A11c"):
        call iscene ("A30c")
    call iscene ("A30d")
    jump_out A31

#Saturday
label A31: #Support
    call iscene ("timeskip")
    call iscene ("A31")
    if seen_scene ("A25b"):
        call iscene ("A31b")
    else:
        call iscene ("A31c")
    call iscene ("A31d")
    if attraction_kenji > 0:
        call iscene ("A31e")
        jump_out A38
    elif seen_scene ("A29c"):
        jump_out A32
    elif seen_scene ("A24d"):
        jump_out A35
    jump_out A32

label A32: #An Aesthetics
    call iscene ("A32")
    if seen_scene ("A25b"):
        jump_out A34
    jump_out A33

label A33: #Creative Pain
    call iscene ("A33")
    call imenu ("choiceA33")
    if _return == m2:
        call iscene ("A33a")
    else:
        call iscene ("A33b")
    jump_out A38

label A34: #Proper Exercise
    call iscene ("A34")
    call iscene ("A34a")
    jump_out A38

label A35: #Sip part 2
    #Added a third choice to skip to Hanako's good end after the end of Act 1 -md01
    call iscene ("A35")
    call imenu("choiceA35")
    if _return == m1:
        call iscene ("A35a")
        jump_out A38
    if _return == m2:
        jump_out A37
    if _return == m3:
        call iscene ("A35b")
        jump_out A37

label A36: #Shanghaied
    call iscene ("timeskip")
    call iscene ("A36")
    jump_out A38

label A37: #Quiet
    call iscene ("A37")
    jump_out A38

#Sunday
label A38: #Don't Panic
    call iscene ("timeskip")
    call iscene ("A38")
    if seen_scene ("A31e"):
        jump_out A43
    elif seen_scene ("A36"):
        call iscene ("A38a")
        call iscene ("A38e")
        jump_out A44
    elif seen_scene ("A35") or seen_scene ("A37"):
        call iscene ("A38b")
        call iscene ("A38e")
        if seen_scene ("A37"):
            jump_out A42
        jump_out A41
    elif seen_scene ("A33a"):
        call iscene ("A38c")
        call iscene ("A38e")
        jump_out A40
    elif seen_scene ("A34"):
        call iscene ("A38d")
        call iscene ("A38e")
        jump_out A39
    jump_out A43

label A39: #Is Carnival
    call iscene ("A39")
    jump_out E3

label A40: #Clouds in My Head
    call iscene ("A40")
    jump_out R2

label A41: #Promise of Time
    #yes, b is the beginning
    call iscene ("A41b")
    call iscene ("A41a")
    jump_out L1

label A42: #Nc5xb3
    call iscene ("A41b")
    call iscene ("A42")
    jump_out H2

label A43: #The Deep End
    call iscene ("A43")
    #call imenu ("choiceA43")
    #mu "Homolust or Yurilust?"
    #if _return == m1:
    #     # "Gimme sum dindins":
    #    call iscene ("A43a")
    #    jump_out HLT3
    #else:
    #    #"Fuck those feminist whores":
    #    call iscene ("A43b")
    #jump_out badend
    #call iscene ("A45")
    jump_out badend

label A44: #Throwing Balls
    call iscene ("A44")
    jump_out S8

#######################
#   Hana/Lilly Path   #
#######################

label HLT3:
    call iscene ("HLT3")
    jump_out HLT4
    
label HLT4:
    call iscene ("HLT4")
    jump_out HLT5
    
label HLT5:
    call iscene ("HLT5")
    jump_out HLT6
    
label HLT6:
    call iscene ("HLT6")
    call imenu ("choiceHLT6")
        #"Wich katwa wud u fuk?!?!"
    if _return == m1:
        #"Tha blidn 1 lel":
        call iscene ("HLT6a")
        jump_out L13
    else:
        #"Extra crispy, with a large order of fries":
        call iscene ("HLT6b")
        jump_out H11
    jump_out HLT6x
        
#######################
#     Hanako path     #
#######################

label H2:
    call iscene ("H2")
    if seen_scene ("A35b"):
        call iscene ("timeskip")
        jump_out HT1
    jump_out H3

label H3:
    call iscene ("H3")
    jump_out H4
    
label H4:
    call iscene ("timeskip")
    call iscene ("H4")
    jump_out H5

label H5:
    call iscene ("H5")
    call imenu ("choiceH5")
        #Decide weather to go to lunch with Hanako or with Shi/Mi
    if _return == m1:
        #Ask Hanako (Go with SC)
        call iscene ("H5_1")
    else:
        #"Go with Hanako
        call iscene ("H5_2")
    jump_out H6
    
label H5_1:
        call iscene("H5_1")
        jump_out H6
        
label H5_2:
        call iscene("H5_2")
        jump_out H6
        
label H6:
    call iscene ("timeskip")
    call iscene ("H6")
    jump_out H7
    
label H7:
    call iscene ("H7")
    if seen_scene("H5_1"):
        call iscene("H7a")
    elif seen_scene("H5_2"):
        call iscene("H7b")
    call iscene("H7c")    
    jump_out H8
    
label H8:
    call iscene ("H8")
    jump_out H9

label H9:
    call iscene ("H9")
    jump_out H10

label H10:
    call iscene ("H10")
    jump_out H11

label H11:
    $ tcard(3, "hanako")
    call iscene ("H11")
    jump_out H12

label H12:
    call iscene ("H12")
    jump_out H13

label H13:
    call iscene ("timeskip")
    call iscene ("H13")
    call iscene ("timeskip") # not sure, maybe it wont fit here [str]
    call iscene ("H14") # calling a note to describe why the hell we skipped so much [str]
    jump_out H23
    #jump_out H14 # we're not using this choice in route, but gonna keep it for act selection menu [str]
    
label H14:
    call iscene ("H14")
    call imenu ("choiceH14")
    #mu "Which ending?"
    if _return == m1:
        #"Good":
        call iscene ("H14a")
        jump_out L19
    else:
        #"Bad":
        jump_out H23
    jump_out H23

# [str] (Waterfall)
label H23:
    call iscene ("H23")
    jump_out H24

label H24:
    $ tcard(4, "hanako")
    call iscene ("H24")
    jump_out H25

label H25:
    call iscene ("H25")
    jump_out H26
    
label H26:
    call iscene ("H26")
    call imenu ("choiceH26")
    #mu "Visit the insane chick?"
    if _return == m1:
        #"Hell yes":
        jump_out H27
    else:
        #"Maybe not":
        jump_out H28
    jump_out H28

label H27:
    call iscene ("H27")
    call iscene ("end_hanakobad1")
    call credits # [str] (credits)
    jump_out restart

label H28:
    call iscene ("H28")
    jump_out H29

label H29:
    call iscene ("H29")
    if seen_scene ("HT3"):
        jump_out HT4
    jump_out H30

label H30:
    call iscene ("H30")
    jump_out H31

label H31:
    call iscene ("timeskip")
    call iscene ("H31")
    call imenu ("choiceH31")
    #mu "Drugged sex; good or bad?"
    if _return == m1:
        #"Advance":
        call iscene ("H31a")
        call iscene ("end_hanakobad2")
        call credits # [str] (credits)
        jump_out restart
    else:
        #"nope.avi":
        jump_out H32
    jump_out H32

label H32:
    call iscene ("H32")
    call iscene ("end_hanakobad3")
    call credits # [str] (credits)
    jump_out restart

label HT1:
    call iscene ("HT1")
    jump_out HT2
    
label HT2:
    call iscene ("HT2")
    jump_out HT3
    
label HT3:
    call iscene ("HT3")
    jump_out H29
    
label HT4:
    call iscene ("HT4")
    jump_out HT5
    
label HT5:
    call iscene ("HT5")
    jump_out HT6
    
label HT6:
    call iscene ("timeskip")
    call iscene ("HT6")
    jump_out HT7

label HT7:
    call iscene ("HT7")
    jump_out HT8
    
label HT8:
    call iscene ("HT8")
    jump_out HT9
    
label HT9:
    call iscene ("timeskip")
    call iscene ("HT9")
    jump_out HT10
    
label HT10:
    call iscene ("HT10")
    call iscene ("HT10h")
    call iscene ("HT10x")
    jump_out HT11
    
label HT11:
    call iscene ("timeskip")
    call iscene ("HT11")
    jump_out HT12
    
label HT12:
    call iscene ("HT12")
    jump_out HT13
    
label HT13:
    call iscene ("HT13")
    call iscene ("HT13h")
    call iscene ("HT13x")
    jump_out HT14
        
label HT14:
    $ tcard(5, "hanatrue")
    call iscene ("HT14")
    jump_out HT15
    
label HT15:
    call iscene ("HT15")
    jump_out HT16
    
label HT16:
    call iscene ("timeskip")
    call iscene ("HT16")
    jump_out HT17
    
label HT17:
    call iscene ("timeskip")
    call iscene ("HT17")
    $ persistent.hanako += 1
    call credits
    jump_out restart

#######################
#      Lilly path     #
#######################

label L1:
    $ tcard(2, "lilly")
    call iscene ("L1")
    jump_out L2

label L2:
    call iscene ("timeskip")
    call iscene ("L2")
    jump_out L3

label L3:
    call iscene ("L3")
    jump_out L4

label L4:
    call iscene ("L4")
    jump_out L5

label L5:
    call iscene ("L5")
    jump_out L6

label L6:
    call iscene ("L6")
    jump_out L7

label L7:
    call iscene ("L7")
    jump_out L8

label L8:
    call iscene ("L8")
    jump_out L9

label L9:
    #$ tcard(3, "lilly") # not here, argh! [str]
    call iscene ("L9")
    jump_out L10

label L10:
    call iscene ("timeskip")
    call iscene ("L10")
    jump_out L11

label L11:
    call iscene ("timeskip")
    call iscene ("L11")
    call hscene ("L11h")
    call iscene ("L11xh")
    #Choices
    #[1] "I was just daydreaming."
    #[2] "It's nothing."
    #[3] "Tell the truth."
    call imenu ("choiceL11")
    if _return == m1:
        call iscene ("L11a")
        #More choices
        #[1A] "You."
        #[1B] "You and Hanako."
        #[1C] "Tell the whole truth."
        call imenu ("choiceL11a")
        if _return == m1:
            call iscene ("L11aa")
        elif _return == m2:
            #+1 Yuri End
            #+1 Bad End
            call iscene ("L11ab")
        else:
            call iscene ("L11c")
    elif _return == m2:
        call iscene ("L11b")
        #Even more choices
        #[2A] "Clam up."
        #[2B] "Spill everything."
        call imenu ("choiceL11b")
        if _return == m1:
            call iscene ("L11ba")
        else:
            call iscene ("L11c")
    else:
        call iscene ("L11c")
    call iscene ("L11x")
    jump_out L12

label L12:
    call iscene ("L12")
    jump_out L13

label L13:
    $ tcard(3, "lilly")
    call iscene ("L13")
    jump_out L14

label L14:
    call iscene ("L14")
    jump_out L15

label L15:
    call iscene ("L15")
    jump_out L16

label L16:
    call iscene ("timeskip")
    call iscene ("L16")
    jump_out L17

label L17:
    call iscene ("L17")
    jump_out L18

label L18:
    call iscene ("L18")
    jump_out L19

label L19:
    call iscene ("timeskip")
    call iscene ("L19") #Welcome to the Alpha, where everything's screwed up and the choices don't matter
    if seen_scene ("H14"):
        call iscene ("L19b")
        jump_out L20
    elif not seen_scene ("L18"):
        call iscene ("L19b")
        jump_out L20
    call imenu ("choiceL19")
    #mu "Which gril?"
    if _return == m1:
        #"foreign faggot":
        call iscene ("L19a")
    else:
        #"bacon":
        call iscene ("L19b")
    jump_out L20
        
label L20:
    if seen_scene ("H14"):
        $ tcard(4, "hanatrue")
    else:
        call iscene ("timeskip")
    call iscene ("L20")
    if seen_scene ("H14"):
        call iscene ("L20b")
        jump_out HT1
    elif not seen_scene ("L18"):
        call iscene ("L20b")
        jump_out HT1
    elif seen_scene ("L19b"):
        call iscene ("L20b")
        jump_out HT1
    call iscene ("L20a")
    jump_out L21

label L21:
    $ tcard(4, "lilly")
    call iscene ("L21")
    jump_out L22

label L22:
    call iscene ("timeskip")
    call iscene ("L22")
    jump_out L23

label L23:
    call iscene ("L23")
    jump_out L24
    
label L24:
    call iscene ("L24")
    jump_out L25
    
label L25:
    call iscene ("L25")
    jump_out L26
    
label L26:
    call iscene ("L26")
    call hscene ("L26h")
    jump_out L27

label L27:
    call iscene ("L27")
    jump_out L28

label L28:
    call iscene ("L28")
    call hscene ("L28h")
    call iscene ("L28x")
    jump_out L29

label L29:
    call iscene ("L29")
    jump_out L30 #When choices are added, bad end will end the route here

label L30:
    call iscene ("L30")
    jump_out L31

label L31:
    call iscene ("timeskip")
    call iscene ("L31")
    jump_out L32

label L32:
    call iscene ("timeskip")
    call iscene ("L32")
    jump_out L33

label L33:
    call iscene ("L33")
    $ persistent.lilly += 1
    jump_out L34
    
label L34:
    call iscene ("timeskip")
    call iscene ("L34")
    call hscene("L34h")
    call iscene("L34x")
    jump_out L35
    
label L35:
    call iscene ("L35")
    jump_out L36
    
label L36:
    call iscene ("timeskip")
    call iscene ("L36")
    jump_out L37
    
label L37:
    call iscene ("timeskip")
    call iscene ("L37")
    jump_out L38
    
label L38:
    call iscene ("L38")
    jump_out L39
    
label L39:
    call iscene ("L39")
    jump_out L40
    
label L40:
    call iscene ("L40")
    jump_out L41
    
label L41:
    call iscene ("timeskip")
    call iscene ("L41")
    jump_out L42

label L42:
    call iscene ("L42")
    call imenu ("choiceL42")
    if _return == m1:
        call iscene ("L42a")
    else:
        call imenu ("choiceL42a")
        if _return == m1:
            call iscene ("L42b")
        else:
            call iscene ("L42c")
    call iscene ("L42x")
    jump_out L43
    
label L43:
    $ tcard(5, "lilly") # no artwork for now [str]
    call iscene ("L43")
    jump_out L44

label L44:
    call iscene ("L44")
    jump_out L45
    
label L45:
    call iscene ("L45")
    jump_out L46
    
label L46:
    call iscene ("L46")
    jump_out L47
    
label L47:
    call iscene ("L47")
    call credits
    jump_out restart
    

#######################
#      Emi path       #
#######################

label E3:
    $ tcard(2, "emi")
    call iscene ("E3")
    jump_out E4

label E4:
    call iscene ("E4")
    jump_out E5

label E5:
    call iscene ("E5")
    jump_out E6

label E6:
    call iscene ("E6")
    jump_out E7

label E7:
    call iscene ("E7")
    jump_out E8

label E8:
    call iscene ("E8")
    jump_out E9

label E9:
    call iscene ("E9")
    jump_out E10

label E10:
    call iscene ("E10")
    jump_out E11

label E11:
    call iscene ("E11")
    jump_out E12

label E12:
    call iscene ("E12")
    jump_out E13

label E13:
    call iscene ("E13")
    jump_out E14

label E14:
    call iscene ("E14")
    jump_out E15

label E15:
    call iscene ("E15")
    jump_out E16

label E16:
    $ tcard(3, "emi")
    call iscene ("E16")
    jump_out E17

label E17:
    call iscene ("E17")
    call imenu ("choiceE17")
    if _return == m1:
        call iscene ("E17a")
    else:
        call iscene ("E17b")
    call iscene ("E17x")
    jump_out E18

label E18:
    call iscene ("E18")
    if seen_scene("E17a"):
        call iscene ("E18a")    
    else:
        call iscene ("E18b")
    call iscene ("E18x")
    jump_out E19

label E19:
    call iscene ("E19")
    jump_out E20

label E20:
    call iscene ("E20")
    call hscene ("E20h")
    call iscene ("E20x")
    jump_out E21

label E21:
    call iscene ("E21")
    call hscene ("E21h")
    call iscene ("E21x")
    jump_out E23

label E23:
    call iscene ("E23")
    jump_out E24

label E24:
    call iscene ("E24")
    jump_out E25

label E25:
    call iscene ("E25")
    jump_out E26

label E26:
    call iscene ("E26")
    call imenu ("choiceE26")
    if _return == m1:
        call iscene ("E26a")
        jump_out E27
    else:
        call iscene ("E26b")
    jump_out E29
    
label E26a:
    call iscene ("E26a")
    jump_out E27
    
label E26b:
    call iscene ("E26b")
    jump_out E29

label E27:
    call iscene ("E27")
    $ persistent.emi += 1
    call credits(False)
    jump_out restart

label E28:
    call iscene ("E28")
    jump_out E29

label E29:
    $ tcard(4, "emi")
    call iscene ("E29")
    #current script end
    $ persistent.emi += 1
    call credits
    jump_out restart

#######################
#      Rin path       #
#######################

label R2:
    $ tcard(2, "rin")
    call iscene ("R2")
    jump_out R3
    
label R3:
    call iscene ("R3")
    call rinscene("rintimeskip")
    jump_out R4

label R4:
    call rinscene ("R4")
    #call imenu ("choiceR4")
    #if _return == m1:
    #    call iscene ("R4a")
    #else:
    #    call iscene ("R4b")
    jump_out R5

label R5:
    call iscene ("R5")
    call rinscene("rintimeskip")
    jump_out R7

#label R6:
    #call iscene ("R6")
    #jump_out R7

label R7:
    call rinscene ("R7")
    call rinscene("rintimeskip")    
    jump_out R8

label R8:
    call rinscene ("R8")
    call rinscene("rintimeskip")
    jump_out R10

#label R9:
 #   call iscene ("R9")
  #  jump_out R10

label R10:
    call rinscene ("R10")
    call rinscene ("rintimeskip")
    jump_out R11

label R11:
    call rinscene ("R11")  
    jump_out R12

label R12:
    call rinscene ("R12")
    call rinscene ("rintimeskip")
    jump_out R13

label R13:
    call rinscene ("R13")
    jump_out R14

label R14:
    call rinscene ("R14")
    call rinscene ("rintimeskip")
    jump_out R15

label R15:
    call rinscene ("R15")
    call rinscene ("rintimeskip")
    jump_out R16

label R16:
    call rinscene ("R16")
    call rinscene ("rintimeskip")
    jump_out R17

label R17:
    call rinscene ("R17")
    call rinscene ("rintimeskip")
    jump_out R18

label R18:
    call rinscene ("R18")
    jump_out R19

label R19:
    $ tcard(3, "rin")
    call iscene ("R19")
    call rinscene ("rintimeskip")
    jump_out R20

label R20:
    call rinscene ("R20")
    call rinscene ("rintimeskip")
    jump_out R21

label R21:
    call rinscene ("R21")
    call rinscene ("rintimeskip")
    jump_out R22

label R22:
    call rinscene ("R22")
    jump_out R23

label R23:
    call rinscene ("R23")
    call rinscene ("rintimeskip")
    jump_out R24
    
label R24:
    call rinscene ("R24")
    call rinscene ("rintimeskip")
    jump_out R25
    
label R25:
    call rinscene ("R25")
    call rinscene ("rintimeskip")
    jump_out R26

label R26:
    call rinscene ("R26")
    call rinscene ("rintimeskip")
    jump_out R27

label R27:
    call rinscene ("R27")
    jump_out R28

label R28:
    call rinscene ("R28")
    call rinscene ("rintimeskip")
    jump_out R29

label R29:
    call rinscene ("R29")
    call hscene ("R29h")
    call rinscene ("R29x")
    jump_out R30

label R30:
    call rinscene ("R30")
    call rinscene ("rintimeskip")
    jump_out R31

label R31:
    call rinscene ("R31")
    call rinscene ("rintimeskip")
    jump_out R32

label R32:
    call rinscene ("R32")
    jump_out R33

label R33:
    $ tcard(4, "rin")
    call iscene ("R33")
    call imenu ("choiceR33")
    if _return == m1:
        call iscene ("R33a")
    else:
        call iscene ("R33b")
    
    call rinscene ("rintimeskip")
    jump_out R34

label R34:
    call rinscene ("R34")
    if seen_scene ("R33a"):
        jump_out R35
    else:
        call iscene ("R34a")
        jump_out R38

# Rin bad end path

label R35:
    call iscene ("R35")
    call rinscene ("rintimeskip")
    jump_out R36

label R36:
    call rinscene ("R36")
    jump_out R37

label R37:
    call iscene ("R37")
    call rinscene ("end_rinbad")
    $ persistent.rin += 1
    call credits(True)
    jump_out restart

# rin good end path

label R38:
    call iscene ("R38")
    jump_out R39

label R39:
    call iscene ("R39")
    jump_out R40

label R40:
    call iscene ("R40")
    call rinscene ("rintimeskip")
    jump_out R41

label R41:
    call rinscene ("R41")
    call hscene ("R41h")
    jump_out R42

label R42:
    call iscene ("R42")
    call rinscene ("end_ringood")
    $ persistent.rin += 1
    call credits(False)
    jump_out restart


#######################
#    Shizune path     #
#######################

label S8:
    $ tcard(2, "shizune")
    call iscene ("S8")
    jump_out S9

label S9:
    call iscene ("timeskip")
    pass
    call iscene ("S9")
    jump_out S10

label S10:
    call iscene ("timeskip")
    pass
    call iscene ("S10")
    jump_out S11

label S11:
    call iscene ("timeskip")
    pass
    call iscene ("S11")
    call imenu ("choiceS11")
    if _return == m1:
        call iscene ("S11a")
    else:
        call iscene ("S11b")
    call iscene ("S11c")
    jump_out S12

label S12:
    call iscene ("timeskip")
    pass
    call iscene ("S12")
    if seen_scene("S11a"):
        call iscene ("S12a")
    call iscene ("S12x")
    jump_out S13

label S13:
    call iscene ("timeskip")
    pass
    call iscene ("S13")
    jump_out S14

label S14:
    call iscene ("timeskip")
    pass
    call iscene ("S14")
    jump_out S15

label S15:
    call iscene ("S15")
    call imenu ("choiceS15")
    if _return == m1:
        call iscene ("S15a")
    else:
        call iscene ("S15b")
    call iscene ("S15c")
    jump_out S16

label S16:
    call iscene ("timeskip")
    pass
    call iscene ("S16")
    jump_out S17

label S17:
    call iscene ("S17")
    call imenu ("choiceS17")
    if _return == m1:
        call iscene ("S17a")
    else:
        call iscene ("S17b")
    call iscene ("S17c")
    call imenu ("choiceS17a")
    if _return == m1:
        call iscene("S17ca")
    elif _return == m2:
        call iscene("S17cb")
    elif _return == m3:
        call iscene("S17cc")
    else:
        call iscene("S17cd")
    call iscene ("S17d")
    jump_out S18

label S18:
    call iscene ("timeskip")
    pass
    call iscene ("S18")
    jump_out S19

label S19:
    call iscene ("timeskip")
    pass
    call iscene ("S19")
    #next choice doesn't matter
    call imenu ("choiceS19")
    if seen_scene("S17ca"):
        call iscene ("S19aa")
        call imenu ("choiceS19a")
        call iscene ("S19ba")
    elif seen_scene("S17cb"):
        call iscene ("S19ab")
        call imenu ("choiceS19a")
        call iscene ("S19bb")
    elif seen_scene("S17cc"):
        call iscene ("S19ac")
        call imenu ("choiceS19a")
        call iscene ("S19bc")
    else:
        call iscene ("S19ad")
        call imenu ("choiceS19a")
        call iscene ("S19bd")
    


label S20:
    $ tcard(3, "shizune")
    call iscene ("S20")
    call imenu ("choiceS20")
    if _return == m1:
        call iscene ("S20a")
    else:
        call iscene ("S20b")
    call iscene ("S20c")
    jump_out S21

label S21:
    call iscene ("timeskip")
    pass
    call iscene ("S21")
    jump_out S22

label S22:
    call iscene ("timeskip")
    pass
    call iscene ("S22")
    call imenu ("choiceS22")
    if _return == m1 or _return == m2:
        call iscene ("S22a")
    else:
        call iscene ("S22b")
    call iscene ("S22c")
    jump_out S23

label S23:
    call iscene ("timeskip")
    pass
    call iscene ("S23")
    call imenu ("choiceS23")
    call iscene ("S23a")
    jump_out S24

label S24:
    call iscene ("timeskip")
    pass
    call iscene ("S24")
    call imenu ("choiceS24")
    if _return == m1:
        call iscene ("S24a")
    else:
        call iscene ("S24b")
    call iscene ("S24c")
    jump_out S25

label S25:
    call iscene ("S25")
    if not seen_scene("S15b"):
        call iscene("S25a")
    else:
        call hscene("S25h")
    jump_out S26

label S26:
    call iscene ("timeskip")


    pass
    call iscene ("S26")
    if seen_scene("S25h"):
        call iscene("S26a")
    else:
        call iscene("S26b")
    call iscene ("S26c")
    if seen_scene("S25h"):
        call iscene("S26d")
    else:
        call iscene("S26e")
    jump_out S27
    
label S27:
    call iscene ("timeskip")
    pass
    call iscene ("S27")
    if seen_scene("S25h"):
        call iscene("S27a")
    else:
        call iscene("S27b")
    call iscene ("S27c")
    call imenu ("choiceS27")
    if _return == m1:
        call iscene ("S27d")
    else:
        call iscene ("S27e")
    call iscene ("S27f")
    call imenu ("choiceS27a")
    if _return == m1:
        call iscene ("S27g")
    elif _return == m2:
        call iscene ("S27h")
    else:
        call iscene ("S27i")
    call iscene("S27x")
    jump_out S28

label S28:
    call iscene ("timeskip")
    pass
    call iscene ("S28")
    call hscene ("S28h")
    call iscene ("S28x")
    jump_out S29

label S29:
    call iscene ("timeskip")
    pass
    call iscene ("S29")
    if seen_scene("S25h"):
        call iscene("S29a")
    else:
        call iscene("S29b")
    call iscene ("S29x")
    jump_out S30

label S30:
    call rinscene ("S30")
    jump_out S31

label S31:
    $ tcard(4, "shizune")
    call iscene ("S31")
    jump_out S32

label S32:
    call rinscene ("rintimeskip")
    pass
    call rinscene ("S32")
    jump_out S33

label S33:
    call rinscene ("rintimeskip")
    pass
    call rinscene ("S33")
    call imenu ("choiceS33a")
    if _return == m1:
        call rinscene ("S33a")
    elif _return == m2:
        call rinscene ("S33b")
    call rinscene ("S33c")
    call imenu ("choiceS33b")
    if _return == m1:
        jump_out S34
    elif _return == m2:
        jump_out S36

label S34:
    call rinscene ("rintimeskip")
    pass
    call rinscene("S34")
    call rinscene ("end_shizunebad")
    $ persistent.shizune += 1
    call credits(True)
    jump_out restart

label S36:
    #S35 does not exist because of lolA22
    call rinscene ("rintimeskip")
    pass
    call rinscene ("S36")
    if seen_scene ("S25h") or seen_scene ("S15b"):
        call rinscene ("S36a")
    else:
        call rinscene ("S36b")
    call rinscene ("S36c")
    jump_out S37

#S37 was originally merged with s36, but I felt it better that what was S37 should be it's own thing -md01
label S37:
    call rinscene ("rintimeskip")
    call rinscene ("S37")
    call hscene ("S37h")
    call rinscene ("S37x")
    jump_out S38

label S38:
    call rinscene ("rintimeskip")
    pass
    call rinscene("S38")
    call rinscene ("end_shizunegood")
    $ persistent.shizune += 1
    call credits(False)
    jump_out restart
