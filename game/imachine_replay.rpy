# This is the I-Machine, the flow control script for KS.
# Dedicated to Irina ~<3
# this is the replay version

#NEWSFLASH: 
#This now only contains scene that actually require different handling for replay

# Monday
    
label replay_A2: #we assume hisao has chosen to introduce himself
    call iscene ("A2")
    call iscene ("A2b")
    call iscene ("A2c")
    call iscene ("A2d")
    call iscene ("A2f")
    $ replay_end()

# Tuesday
    
label replay_A8: #this also assumes an introduction took place. Really minor difference.
    call iscene ("A8")
    call imenu ("choiceA8")
    if _return == m1:
        call iscene ("A8a")
        call iscene ("A8aa")
        call iscene ("A8ab")
    else:
        call iscene ("A8b")
    call iscene ("A8c")
    if seen_scene ("A8a"): #internal
        call iscene ("A8d")
    else:
        call iscene ("A8e")
    call iscene ("A8f")
    $ replay_end()
    

# Wednesday
label replay_A10: #this is the version with maximum choice breadth
    call iscene ("A10")
    call imenu ("choiceA10a")
    if _return == m1:
        call iscene ("A10a")
    elif _return == m2:
        call iscene ("A10b")
    else:
        call iscene ("A10c")
    $ replay_end()
    
label replay_A11_1: # Shizune end is assumed
    call iscene ("A11")
    call iscene ("A11a")
    call iscene ("A11b")
    call iscene ("A11x")
    $ replay_end()

#Thursday
label replay_A19: # we just go the positive route here
    call iscene ("A19")
    call iscene ("A19a")
    call iscene ("A19c")
    call iscene ("A19j")
    call iscene ("A19d")
    call iscene ("A19f")
    call iscene ("A19g")
    call iscene ("A19h")
    $ replay_end()

    
label replay_A21: #we assume the ending with more lilly
    call iscene ("A21")
    call imenu ("choiceA21")
    if _return == m1:
        call iscene ("A21a")
        $ replay_end()
    call iscene ("A21b")
    call iscene ("A21c")
    $ replay_end()

label replay_A22: #a is just a short leadout.
    call iscene ("A22")
    call iscene ("A22a")
    $ replay_end()

label replay_A23_1:
    call iscene ("A23")
    $ replay_end()

label replay_A23_2:
    call iscene ("A23a")
    $ replay_end()


label replay_A24: #happy go lucky lilly version
    call iscene ("A24")
    call iscene ("A24d")
    call iscene ("A24e")
    $ replay_end()

#Friday
label replay_A26:
    call iscene ("A26")
    call iscene ("A26a")
    call iscene ("A26e")
    $ replay_end()

label replay_A26_1:
    call iscene ("A26b")
    call imenu ("choiceA26")
    if _return == m1:
        call iscene ("A26c")
        $ replay_end()
    call iscene ("A26d")
    $ replay_end()

label replay_A27_1: #we assume the case that gives you more choices
    call iscene ("A27")
    call iscene ("A27a")
    call imenu ("choiceA27")
    if _return == m1: 
        call iscene ("A27b")
        $ attraction_kenji += 1
        call iscene ("A27f")
        $ replay_end()
    call iscene ("A27c")
    call imenu ("choice2A27")
    if _return == m1:
         call iscene ("A27h")
         call iscene ("A27e")
         $ replay_end()                                    
    call iscene ("A27i")
    jump_out A28

label replay_A27_2: #we're taking e for the funny misha moment
    call iscene ("A27d")
    call iscene ("A27e")
    $ replay_end()

label replay_A28: #the difference is minor, so we take the longest route
    call iscene ("A28")
    call iscene ("A28a")
    call iscene ("A28b")
    $ replay_end()

label replay_A29: #version without heart attack & more cute emi
    call iscene ("A29")
    call iscene ("A29x")
    call iscene ("A29b")
    call iscene ("A29c")
    $ replay_end()

label replay_A30: #the safeguard is probably irrelevant. c is just a short conditional, so it's in.
    call iscene ("A30")
    call imenu ("choiceA30")
    if _return == m2:
        call iscene ("A30a")
        $ replay_end()
    call iscene ("A30b")
    call iscene ("A30c")
    call iscene ("A30d")
    $ replay_end()

#Saturday
label replay_A31: #we assume no heart attack, and include the end
    call iscene ("A31")
    call iscene ("A31c")
    call iscene ("A31d")
    call iscene ("A31e")
    $ replay_end()

#Sunday
label replay_A38: #The various special bits are path-exclusive
    call iscene ("A38")
    $ replay_end()

