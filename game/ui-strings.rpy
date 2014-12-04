init -3 python:
    # this is the master language so it lives at init level -3, not -2 like the others
    ### ENGLISH
    
    init_language("en")
    
    displayDict["en"].styleoverrides = {"font": mainfont, 
                                        "language": "western",
                                        "line_spacing": 0}
    
    displayDict["en"].timeformat = "%b %d, %H:%M"
    
    displayDict["en"].sayfont = mainfont
    
    displayDict["en"].quote_outer_open = u"“"
    displayDict["en"].quote_outer_close = u"”"
    displayDict["en"].quote_inner_open = u"‘"
    displayDict["en"].quote_inner_close = u"’"
    
    displayDict["en"].activeLanguage = "English"
    displayDict["en"].allLanguages = {}
    displayDict["en"].allLanguages["en"] = displayDict["en"].activeLanguage
    displayDict["en"].allLanguages["de"] = "German"
    displayDict["en"].allLanguages["it"] = "Italian"
    displayDict["en"].allLanguages["jp"] = "Japanese"
    displayDict["en"].allLanguages["ru"] = "Russian"
    
    displayDict["en"].act_term = u"Act"
    displayDict["en"].window_name = u"Katawa Shoujo"
    
    displayDict["en"].main_menu_start = u"Start"
    displayDict["en"].main_menu_load = u"Load"
    displayDict["en"].main_menu_extra = u"Extras"
    displayDict["en"].main_menu_config = u"Options"
    displayDict["en"].main_menu_quit = u"Quit"

    displayDict["en"].game_menu_return = u"Return"
    displayDict["en"].game_menu_show = u"Show image"
    displayDict["en"].game_menu_history = u"Text history"
    displayDict["en"].game_menu_skip = u"Skip mode"
    displayDict["en"].game_menu_auto = u"Auto mode"
    displayDict["en"].game_menu_config = u"Options"
    displayDict["en"].game_menu_save = u"Save"
    displayDict["en"].game_menu_load = u"Load"
    displayDict["en"].game_menu_main = u"Main menu"
    displayDict["en"].game_menu_quit = u"Quit"
    displayDict["en"].game_menu_current_scene = u"Current Scene"
    displayDict['en'].game_menu_current_music = u"Current music track"
    displayDict["en"].game_menu_replay_indicator = u"Replay"
    displayDict["en"].game_menu_jumper = u"Select Act"

    displayDict["en"].return_button_text = u"Return"

    displayDict["en"].hdisabled_label = u"Disable adult content"
    displayDict["en"].config_page_caption = u"Options"
    displayDict["en"].config_fullscreen_label = u'Fullscreen mode'
    displayDict["en"].config_transitions_label = u'Disable transitions'
    displayDict["en"].config_skip_unseen_label = u'Skip unread text'
    displayDict["en"].config_skip_after_choice_label = u'Keep skipping after choices'
    displayDict["en"].config_textspeed_label = u'Text speed'
    displayDict["en"].config_afmspeed_label = u'Auto mode delay'
    displayDict["en"].config_musicvol_label = u"Music volume"
    displayDict["en"].config_musicvol_jukebox_label = u"Vol."
    displayDict["en"].config_sfxvol_label = u"SFX volume"
    displayDict["en"].config_sfxtest_label = u"Test"
    displayDict["en"].config_gamepad_label = u"Gamepad keymap…"

    displayDict["en"].config_language_sel = u"Language selection…"
    displayDict["en"].config_language_caption = u"Options > Language selection"
    displayDict["en"].config_language_restart_note = "Note: Changing the language while a session is in progress will return the game to the latest script node."

    displayDict["en"].gamepad_caption = u"Options > Gamepad keymap"
    displayDict["en"].gamepad_key_na = u"Not assigned"
    displayDict["en"].gamepad_request_key = u"Press the button you want to assign “%s” to.\nClick the mouse or the select button to clear the mapping."

    displayDict["en"].yesno_yes = u"Yes"
    displayDict["en"].yesno_no = u"No"
    displayDict["en"].yesno_okay = u"Continue"
    displayDict["en"].yesno_savesuccess = u"Progress successfully saved\nas number %s."
    displayDict["en"].yesno_quit = u"Are you sure you want to\nquit Katawa Shoujo?"
    displayDict["en"].yesno_return_to_main = u"Are you sure you want to\nreturn to the main menu?"
    displayDict["en"].save_page_caption = u"Save"
    displayDict["en"].new_save_button = u"Create new save state"
    displayDict["en"].load_page_caption = u"Load"
    displayDict["en"].yesno_load_in_game = u"Are you sure you want to\ndiscard your progress?"
    displayDict["en"].yesno_save_overwrite = u"Are you sure you want to\noverwrite your save?"
    displayDict["en"].yesno_delete_savegame = u"Are you sure you want to\ndelete save number %s?"
    displayDict["en"].play_time_label = u"Play time"
    displayDict["en"].show_manual_saves = u"Manual"
    displayDict["en"].show_auto_saves = u"Auto"

    displayDict["en"].text_history_caption = u"Text history"

    displayDict["en"].extra_menu_caption = "Extras"
    displayDict["en"].extra_music_button_label = "Jukebox"
    displayDict["en"].extra_gallery_button_label = "Gallery"
    displayDict["en"].extra_scene_button_label = "Library"
    displayDict["en"].extra_omake_button_label = "Omake"
    displayDict["en"].extra_opening_button_label = "Cinema"
    displayDict["en"].commentary_label = "Enable commentary"

    displayDict["en"].music_page_caption = "Extras > Jukebox"
    displayDict["en"].music_stop_button_text = "Stop"
    displayDict["en"].music_now_playing = "Now playing"

    displayDict["en"].gallery_page_caption = "Extras > Gallery"
    displayDict["en"].gallery_onelocked = "One further image not unlocked."
    displayDict["en"].gallery_manylocked = "%d further images not unlocked."
    displayDict["en"].gallery_singlelocked = "Image %d of %d is not unlocked."
    displayDict["en"].gallery_num_page_prefix = "Page "
    displayDict["en"].gallery_num_page_error = "No images to display"

    displayDict["en"].scene_page_caption = "Extras > Library"
    displayDict["en"].scene_completion_label = "Completion: %s%%"
    displayDict["en"].scene_playthrough_label = "Use replay flow (recommended)"
    
    displayDict["en"].joy_left = "Left"
    displayDict["en"].joy_right = "Right"
    displayDict["en"].joy_up = "Up"
    displayDict["en"].joy_down = "Down"
    displayDict["en"].joy_dismiss = "Select/Advance"
    displayDict["en"].joy_rollback = "Text history"
    displayDict["en"].joy_holdskip = "Hold to skip"
    displayDict["en"].joy_toggleskip = "Skip mode"
    displayDict["en"].joy_hide = "Show image"
    displayDict["en"].joy_menu = "Show menu"

    ##Names

    displayDict["en"].name_hi = "Hisao"
    displayDict["en"].name_all = "All"
    displayDict["en"].name_ha = "Hanako"
    displayDict["en"].name_emi = "Emi"
    displayDict["en"].name_rin = "Rin"
    displayDict["en"].name_li = "Lilly"
    displayDict["en"].name_shi = "Shizune"
    displayDict["en"].name_mi = "Misha"
    
    displayDict["en"].name_ke = "Kenji"
    displayDict["en"].name_mu = "Mutou"
    displayDict["en"].name_nk = "Nurse"
    displayDict["en"].name_no = "Nomiya"
    displayDict["en"].name_yu = "Yuuko"
    displayDict["en"].name_sa = "Sae"
    displayDict["en"].name_aki = "Akira"
    displayDict["en"].name_hh = "Hideaki"
    displayDict["en"].name_hx = "Jigoro"
    displayDict["en"].name_emm = "Meiko"
    
    displayDict['en'].name_mk = "Miki"
    
    displayDict["en"].name_mystery = "???"

    displayDict["en"].name_ha_ = "Purple-haired girl"
    displayDict["en"].name_emi_ = "Twintails girl"
    displayDict["en"].name_rin_ = "Strange girl"
    displayDict["en"].name_li_ = "Wavy-haired girl"
    displayDict["en"].name_mi_ = "Laughing girl"
    displayDict["en"].name_ke_ = "Bespectacled hallmate"
    displayDict["en"].name_mu_ = "Tall man"
    displayDict["en"].name_yu_ = "Librarian"
    displayDict["en"].name_no_ = "Silver-haired man"
    displayDict["en"].name_sa_ = "Gallerist"
    displayDict["en"].name_aki_ = "Well-dressed person"
    displayDict["en"].name_nk_ = "Smiling man"
    displayDict["en"].name_hx_ = "Shizune's father"
    displayDict["en"].name_hh_ = "Slim girl"
    displayDict["en"].name_emm_ = "Emi's mother"
    
    # Scenes available in the extras -> scene select menu. Name, label, description, path (path may also be a tuple).
    # Now also doubles as a lookup list for the actual scene names. Display in the extras can be suppressed
    # by setting the third value in the tuple to False. Suppression doesn't work in DQN mode.
    # Note that Ren'Py doesn't like non-ASCII characters in scene titles if the titles are not unicode strings
    displayDict["en"].s_scenes = (("Out Cold", "NOP1", "On a cold, snowy day, Hisao's dreams were about to be realized, only to be cut short by a sudden heart attack.", "Act 1"), # NEW ACT 1
                                    ("Bundle of Hisao", "NOP2", "Hisao is told about Yamaku Academy, where he will likely spend the rest of his high school days.", "Act 1"),
                                    ("Gateway Effect", "A1", "Hisao steps into Yamaku Academy for the first time, and meets his homeroom teacher, Mutou.", "Act 1"),
                                    ("Enter Stage Left", "A2", "Introductions to the class, and meeting with the class representative and her interpreter.", "Act 1"),
                                    ("In the Nursery", "A3", "Misha and Shizune show Hisao the cafeteria, after which he goes to see the nurse.", "Act 1"),
                                    ("Nobody's Room", "A4", "Hisao moves into his new room, meeting his hallmate Kenji in the process.", "Act 1"),
                                    ("Smalltalk", "A5", "Shizune and Misha tell Hisao about the upcoming festival and invite him to lunch.", "Act 1"),
                                    ("Risk vs. Reward", "A6", "Shizune and Hisao battle for the world in a game of Risk.", "Act 1"),
                                    ("Pseudo Tea Cosy", "A7", "Looking for the library, Hisao gets lost and finds Lilly in a disused classroom.", "Act 1"),
                                    ("Shared Library", "A8", "Finally finding his way to the library, Hisao meets and scares off Hanako.", "Act 1"),
                                    ("Bizarre and Surreal", "A9", "Kenji reveals the dark secrets of Yamaku.", "Act 1"),
                                    ("Lunch Evolution Theory", "A10", "Shizune and Misha badger Hisao into joining the Student Council before discussing lunch.", "Act 1"),
                                    ("Short Sharp Shock", "A11_1", "On his way to lunch alongside Misha and Shizune, Hisao collides with Emi in the hallway.", "Act 1"),
                                    ("Meet Cute", "A11_2", "Hisao collides with a rampaging Emi on his way to lunch with Hanako and Lilly.", "Act 1"),
                                    ("Detour Ahead", "A12", "Shizune and Misha take Hisao to their favourite teahouse, the Shanghai.", "Act 1"),
                                    ("Sip (part 1)", "A13", "Hisao has a peaceful lunch with Lilly and Hanako.", "Act 1"), # there is no A14
                                    ("It Builds Character", "A15", "Mutou tries to have a D&M talk with Hisao, but Misha interrupts and puts Hisao to work.", "Act 1"),
                                    ("A Private Lunch", "A16", "Searching for supplies, Hisao happens across a strange girl in the art room.", "Act 1"),
                                    ("Waylay", "A17", "While helping Rin carry some paint, Hisao is quizzed by the nurse.", "Act 1"),
                                    ("The Other Green", "A18", "Hisao watches Rin paint her mural.", "Act 1"),
                                    ("The Running Girl", "A19", "When attempting to do some morning exercise, Hisao meets Emi at the running track.", "Act 1"),
                                    ("Soap", "A20", "Kenji ambushes Hisao in the shower in an attempt to get some cash.", "Act 1"),
                                    ("Cold War", "A21", "Shizune and Lilly face off over budget requests.", "Act 1"),
                                    ("Proof of Competency", "A22", "Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.", "Act 1"),
                                    ("Event Horizon", "A22_2", "Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.", "Act 1"),
                                    ("Above and Beyond", "A23_1", "Hisao gets a lecture about the noble duties of a Student Council.", "Act 1"),
                                    ("Things You Can Do", "A23_2", "After escaping from the clutches of Shizune and Misha, Hisao helps out Rin again.", "Act 1"),
                                    ("Paint by Numbers", "A24", "Hanako and Hisao lend a hand to Lilly's class by volunteering to help build their stall.", "Act 1"),
                                    ("Exercise", "A25", "Another early morning sees Hisao running at the track with Emi.", "Act 1"),
                                    ("Invisible Hat", "A26", "Kenji gives Hisao a few insider tips on how to socialize.", "Act 1"),
                                    ("Home Field Advantage", "A26_1", "Shizune and Misha hijack Hisao as he leaves his room for class.", "Act 1"),
                                    ("No Recovery", "A27", False, "Act 1"), #this is somewhat of a hack, and a special case
                                    ("Slow Recovery", "A27_1", "Recovering from his heart flutter, Hisao eventually makes it to class.", "Act 1"),
                                    ("No Recovery", "A27_2", "Hisao struggles to class after his hijacking by the Student Council.", "Act 1"),
                                    ("No Free Lunch", "A28", "Hisao is escorted to the Student Council office for his first official day there.", "Act 1"),
                                    ("Foot and Mouth", "A29", "Emi drags Hisao to the roof to have lunch with Rin.", "Act 1"),
                                    ("Mind Your Step", "A30", "Hisao and Lilly go shopping, meeting a very confused Rin on the way back.", "Act 1"),
                                    ("Support", "A31", "Hisao has his first Saturday lesson, complete with a talking to from Mutou.", "Act 1"),
                                    ("An Aesthetics", "A32", "Emi finds Hisao slacking around after class and recruits him to help Rin once again.", "Act 1"),
                                    ("Creative Pain", "A33", "Hisao meets the art teacher, Nomiya, as Rin paints her mural.", "Act 1"),
                                    ("Proper Exercise", "A34", "Emi and Hisao discuss the importance of being in shape.", "Act 1"),
                                    ("Sip (part 2)", "A35", "In an attempt to kill time, Hisao goes for a walk around the school.", "Act 1"),
                                    ("Shanghaied", "A36", "Tea, cake and competitions with Shizune and Misha at the Shanghai.", "Act 1"),
                                    ("Quiet", "A37", "Hanako and Hisao read books for the festival.", "Act 1"),
                                    ("Don't Panic", "A38", "After waking up on the day of the festival, Hisao is greeted by a ranting Kenji.", "Act 1"),
                                    ("Is Carnival!", "A39", "Emi catches Hisao eating fried food and makes him accompany her as punishment.", ("Act 1", "Emi")),
                                    ("Clouds in My Head", "A40", "Hisao keeps Rin and her now-finished mural company.", ("Act 1", "Rin")),
                                    ("Promise of Time", "A41", "After a trying morning at her stall, Hisao takes Lilly to find Hanako.", ("Act 1", "Lilly")),
                                    ("Nc5xb3", "A42", "Unable to help Lilly at her stall, Hisao searches for Hanako at the festival.", ("Act 1", "Hanako")),
                                    ("The Deep End", "A43", "Kenji and Hisao share a manly picnic on the roof instead of going to the festival.", "Act 1"),
                                    ("Throwing Balls", "A44", "True to his word, Hisao spends the day with Shizune and Misha.", ("Act 1", "Shizune")),
                                    ("Morning Run", "E3", "The first of Hisao's many morning runs with Emi.", "Emi"),
                                    ("Clouds, Time Travel, and Thou", "E4", "Another rooftop lunch with Emi and Rin. Hisao asks the two about the reasons for their friendship.", "Emi"),
                                    ("Questions That Need Answering!", "E5", "Idle chat between Emi and Hisao. Hisao asks Emi few more questions about her relationship with Rin.", "Emi"),
                                    ("Second Time's the Worst", "E6", "The second morning run. Hisao is almost dragged kicking and screaming around the track.", "Emi"),
                                    ("Let the Shipping Begin", "E7", "Hisao pays a visit to the nurse along with Emi, finding that the two have known each other for a while.", "Emi"),
                                    ("Track Meeting", "E8", "The day of the track meet. Another facet of Emi's personality is revealed.", "Emi"),
                                    ("Down that Medicine Now", "E9", "Hisao mentions a pain in his chest during a visit to the nurse and receives a lecture.", "Emi"),
                                    ("Piracy on the High Seas", "E10", "Hisao takes a nap on the rooftop, then discusses his future as a pirate with Emi.", "Emi"),
                                    ("Obligatory Dream Sequence", "E11", "And a very trippy dream sequence at that.", "Emi"),
                                    ("Famous Last Words", "E12", "Emi and Rin take Hisao along for a picnic, soon to be spoiled by rain.", "Emi"),
                                    ("Tracking Absences", "E13", "Hisao goes to the track as usual, but Emi is missing.", "Emi"),
                                    ("Dropping By", "E14", "A bedside visit for a sick Emi, which quickly changes to something else entirely.", "Emi"),
                                    ("The First Morning After", "E15", "Hisao reminisces about last morning, deciding to do something to help Emi.", "Emi"),
                                    ("The (Real) Beginning", "E16", "Another lunchtime on the rooftop, sans Rin.", "Emi"),
                                    (u"Eet Ees… Scienca!", "E17", "Mutou pulls Hisao into a short discussion about his future.", "Emi"),
                                    ("Definitions", "E18", "Emi and Hisao attempt another picnic, this time without any intervention from Mother Nature.", "Emi"),
                                    ("Science Sandwiches", "E19", "Back to the track in the morning, with business as usual, or so it seems.", "Emi"),
                                    ("Lunch and Science", "E20", "Hisao sees Mutou again about his future in the sciences.", "Emi"),
                                    ("Up, down, and up again", "E21", "Hisao helps further Kenji's causes using unusual methods.", "Emi"),
                                    ("Storage Space", "E22", "Emi pulls Hisao into the storage shed to talk with him, if you know what I mean.", "Emi"),
                                    ("After-School Plans", "E23", "Emi has Hisao make a few promises.", "Emi"),
                                    ("Putting the Fun in Funeral", "E24", "Hisao meets Emi's mom, as well as a graveside visit.", "Emi"),
                                    ("Clean Teeth", "E25", "Hisao wakes up, finding Emi sleeping next to him. Later, he finds Yuuko in his bathroom.", "Emi"),
                                    ("Hooray for Socks!", "E26", "Sex, drugs, but no rock and roll.", "Emi"),
                                    ("Debate Expresses Doubt", "E27", "Storytime with the nurse.", "Emi"),
                                    (u"Guess Who's Coming… Nevermind", "E28", True, "Emi"),
                                    ("Movement", "H2", "Lilly finishes her duties and treats Hanako and Hisao to tea", "Hanako"),
                                    ("Rosarium", "H3", "Hisao takes Hanako Shopping", "Hanako"),
                                    ("Chinese Tea", "H4", "Hanako invites Hisao to have lunch with her and Lilly.", "Hanako"),
                                    ("Dies Irae", "H5", "Hisao chooses between eating with Shizune or playing chess with Hanako", "Hanako"),
                                    ("Office Confessional", "H5_1", "Hisao and Misha discuss the plight of Hanako.", "Hanako"),
                                    ("Chess and Slides", "H5_2", "Hisao ditches the Student Council to read with Hanako", "Hanako"),
                                    ("On Waking Early", "H6", "Hisao wakes up early and has breakfast with Lilly.", "Hanako"),
                                    ("The First Tea Party", "HLT3", "The duet of trickery make Hisao their plaything in Lilly's private quarters.", ("Hanako", "Lilly")),
                                    ("Electric Angel", "HLT4", True, ("Hanako", "Lilly")),
                                    ("Kicks!", "HLT5", True, ("Hanako", "Lilly")),
                                    ("Droplets of Winter", "HLT6", True, ("Hanako", "Lilly")),
                                    ("Dining with the Mad Hatter", "H7", "Lilly invites Hisao to a tea party after hours.", "Hanako"), 
                                    ("Small Change", "H8", "Hisao forces Kenji to repay his loan.", "Hanako"),
                                    ("Through the Looking Glass", "H9", "Hisao and Lilly discuss Hanako's truancy.", "Hanako"),
                                    ("Dance Dance Dance!", "H10", "Hanako reveals her past to Hisao in return for learning about his heart.", "Hanako"),#End of Act 2 
                                    ("The Invitation", "H11", "Lilly finds Hisao cleaning up the Tea Room and tells him about Hanako's Birthday.", "Hanako"),
                                    ("Unexpected Alliance", "H12", "Shizune and Misha drag Hisao to dinner and Hisao finds out about Karaoke bars in town.", "Hanako"),#end of Final route similarities
                                    ("Kagerou", "H13", "Lilly and Hisao check out karaoke bars for Hanako's Party.", "Hanako"),
                                    #("Prompted Confession", "H14", "The trio get wasted during Lilly's party and Hisao half-heartedly admits his feelings to Hanako.", "Hanako"),
                                    ("Note From the Editor", "H14", "Choose your own adventure.", "Hanako"), # ending choice/personal notes
                                    ("Like Wildfire", "H15", True, "Hanako"),
                                    ("Fast and Thin", "H16", True, "Hanako"),
                                    ("Time Alone", "H17", True, "Hanako"),
                                    ("An Audience of Two", "H18", True, "Hanako"),
                                    ("Undue Concern", "H19", True, "Hanako"),
                                    ("Study Week", "H20", True, "Hanako"),
                                    ("Contemplation", "H21", True, "Hanako"),
                                    ("Tatters", "H22", True, "Hanako"),
                                    ("Waterfall", "H23", True, "Hanako"), # this scene exists online- Hisao's heartattack, leads to all bad ends
                                    ("Dawn", "H24", True, "Hanako"), # start of the returning script- scenes H14-H22/23 nonexistent
                                    ("Revelation", "H25", True, "Hanako"),
                                    ("In State", "H26", True, "Hanako"),
                                    ("Dulce Et Decorum Est", "H27", True, "Hanako"), # bad end 1
                                    ("Patience is a Virtue", "H28", True, "Hanako"),
                                    #("Future", "H29", True, "Hanako"), # want to also throw this between HT3 and HT4, if possible
                                    ("Triumphant Return", "H30", True, "Hanako"),
                                    ("Once more into the Breech", "H31", True, "Hanako"), # chance for bad end 2
                                    ("A Spoonful of Sugar", "H32", True, "Hanako"), # bad end 3, final destination
                                    ("Rhapsody in Blue", "L19", "Hisao visits Lilly in the hospital, where she makes a request of him.", "Hanako"),
                                    ("The Momentary Present", "L20", "After returning to the school, Hisao is met with a variety of surprises.", "Hanako"),
                                    ("A Pair of Steiffs", "HT1", "Hisao and Hanako visit the antique shop to find a present for Lilly.", "Hanako"), # Hanako True path
                                    ("Nothing's There", "HT2", "The duo deliver Lilly's presents to her in the hospital.", "Hanako"),
                                    ("Drizzly Night", "HT3", "Hisao attempts to give Hanako her bear and is met with a surprise.", "Hanako"),
                                    ("Painful History", "H29", "A life is forever changed.", "Hanako"), 
                                    ("Calling the Sunrise", "HT4", "Hisao returns to class after spending the night with Hanako in Lilly's room.", "Hanako"),
                                    ("Welcome Party", "HT5", "The group throws a party to celebrate Lilly's return and Hanako shows her growing confidence.", "Hanako"),
                                    ("Confession Vocal", "HT6", "Hisao consults Lilly about the previous night's events and Hanako gives Hisao a mysterious note.", "Hanako"),
                                    ("Girl Uppi", "HT7", "Hisao receives a pep talk from Lilly and meets Hanako behind the dorms.", "Hanako"),
                                    ("Four Right Feet", "HT8", "Hisao and Hanako's feelings for one another are finally realized.", "Hanako"),
                                    ("Lullaby for Strain", "HT9", "Hanako takes Hisao on a picnic date to a place that is special to her.", "Hanako"),
                                    ("Under Slave", "HT10", "The two share in their moment of embrace.", "Hanako"),
                                    ("Love is Psychadelic", "HT11", "After passing out the previous night, Hisao cleans up and makes a trip to the nurse's office.", "Hanako"),
                                    ("Eternal Dream", "HT12", "Hisao and Hanako visit Yuuko at the Shanghai, and Hisao tries to sneak a purchase past Hanako at the mart.", "Hanako"),
                                    ("Words I Cannot Say", "HT13", "The two share in another intimate moment, but are met by a surprise visitor.", "Hanako"),
                                    ("Re-Sublimity", "HT14", "Hanako invites Shizune and Misha to eat lunch on the rooftop, where they find Emi, Rin, and Lilly.", "Hanako"),
                                    ("Curves in Spacetime", "HT15", "Hisao gets roped into tutoring all six girls in science.", "Hanako"),
                                    ("Sucker Punch", "HT16", "After conquering finals, the group decides to celebrate in the Student Council room after-hours.", "Hanako"),
                                    ("I'm Here", "HT17", "Hanako faces the ghosts of her past.", "Hanako"),
                                    ("Mad Hatter", "L1", "Hisao shares the first of many lunchbreaks with Hanako and Lilly, resting from the day before.", "Lilly"),
                                    ("A One Rand Note", "L2", "Cornered by Kenji on Lilly's nationality, Hisao decides to investigate and finds out a great deal more.", "Lilly"),
                                    ("Presents and Presence", "L3", "While out in search of a present for Hanako, Lilly and Hisao meet Akira's fiancé.", "Lilly"),
                                    ("Unidentified Drinking Object", "L4", "The trio hold a birthday party for Hanako, interrupted by the surprise appearance of a certain sibling.", "Lilly"),
                                    ("The Day After", "L5", "Hisao and Lilly awaken, and try to recuperate from the previous evening's harried events.", "Lilly"),
                                    ("A Brief History of Thyme", "L6", "Hisao and Lilly go to get some groceries.", "Lilly"),
                                    ("The Two's Past", "L7", "Akira retells the childhood that she and Lilly have shared.", "Lilly"),
                                    ("Bon Voyage", "L8", "Lilly and Akira are seen off as they take a trip to their family in South Africa.", "Lilly"),
                                    ("Day by Day", "L9", "Hisao idly lets a day without Lilly slip by, having a talk with Mutou about Yamaku.", "Lilly"),
                                    ("Minor Discord", "L10", "Hisao talks with a quieter than usual Hanako, after Kenji gives him a little wanted promotion.", "Lilly"),
                                    ("Dissonance", "L11", "With Hanako withdrawing into herself completely, Hisao offers what little help he can before calling Lilly.", "Lilly"),
                                    ("A World Away", "L12", "Hisao's reassured mind begins to wonder about the relationship between he and Lilly.", "Lilly"),
                                    ("Renewal", "L13", "Hisao, Lilly and Hideaki greet Akira and Lilly after their return from South Africa.", "Lilly"),
                                    ("Northern Sojourn", "L14", "The trio begin their holiday in Hokkaido.", "Lilly"),
                                    ("Prelude", "L15", "A morning walk begins a chain reaction of events.", "Lilly"),
                                    ("Crescendo", "L16", "Lilly's true feelings are told in the endless gold of the wheat fields." , "Lilly"),
                                    ("Diminuendo", "L17", "The two share their first night together.", "Lilly"),
                                    ("Grey Outlook", "L18", "Confined to the summerhouse, Lilly and Hisao are forced to come to terms with their relationship.", "Lilly"),
                                    ("Rhapsody in Blue", "L19", "Hisao reflects on where he and Lilly are in life, before being joined by another.", "Lilly"),
                                    ("The Momentary Present", "L20", "Travelling back to Yamaku, Hisao and Lilly idly talk between themselves.", "Lilly"),
                                    ("Slow Steps 'fore a Waltz", "L21", "Back at school, the events of Hokkaido come to the fore.", "Lilly"),
                                    ("Joy and Conflict", "L22", "Settling back into daily life, Akira and Hideaki join the trio's teaparty.", "Lilly"),
                                    ("A Morning's Reverie", "L23", "Hisao and Lilly discuss their ambitions.", "Lilly"),
                                    ("Correct Procedure", "L24", "Hisao and Lilly arrange a date, before Hideaki and Akira join them.", "Lilly"),
                                    ("Out and About", "L25", "Hisao and Lilly go on their first date, finding out about each other's pasts.", "Lilly"),
                                    ("Steps of the Three", "L26", "Hisao, Hanako and Lilly muse on the upcoming holidays as they share tea together.", "Lilly"),
                                    ("Blackout", "L27", "An unexpected offer leads to an unexpected evening.", "Lilly"),
                                    ("A Faraway Future", "L28", "Lilly reveals her family's offer to join them in South Africa, With Hisao reluctantly accepting her wishes to go.", "Lilly"),
                                    ("Farewell", "L29", "Hisao and Hanako farewell Akira and Lilly the evening before they leave Japan.", "Lilly"),
                                    ("False Cadence", "L30", "Hisao rushes to confront Lilly, realising her conflict.", "Lilly"),
                                    ("Under a Maudlin Sky", "L31", "Waking in the hospital ward, Hisao struggles to come to terms with his life.", "Lilly"),
                                    ("Under a Bright Sky", "L32", "Lilly rejoins Hisao, the two beginning their life together anew.", "Lilly"),
                                    ("Forwards, with Gusto!", "L33", "Lilly and Hisao see off Akira.", "Lilly"),
                                    ("Cloud Lunch", "R2", "Hisao spends an afternoon of skipped class with Rin watching clouds on the rooftop.", "Rin"),
                                    ("Grayscale", "R3", "Hisao attends his first art club meeting and draws a portrait of Rin.", "Rin"),
                                    ("Black Mood", "R4", "After a particularly bad school day, Hisao ends up having a talk with Rin about an unexpected subject.", "Rin"),
                                    ("Dual Mono", "R5", "A lunch with Rin and Hanako. Rin philosophizes their reasons to be at Yamaku Academy.", "Rin"),
                                    ("Audience", "R7", True, "Rin"),
                                    ("Finding Places", "R8", True, "Rin"),
                                    ("Another Morning Ruined", "R9", True, "Rin"),
                                    ("The First Day of Summer", "R10", True, "Rin"),
                                    ("The Concept of Future", "R11", True, "Rin"),
                                    ("Umbrella Logic Cake", "R12", True, "Rin"),
                                    ("Six Meters Closer to Heaven", "R13", True, "Rin"),
                                    ("Understanding Words", "R14", True, "Rin"),
                                    ("Communication Problems", "R15", True, "Rin"),
                                    ("Signal/Noise Ratio", "R16", True, "Rin"),
                                    ("Contrast", "R17", True, "Rin"),
                                    ("The Secret Place", "R18", True, "Rin"),
                                    ("Teachers and Students", "R19", True, "Rin"),
                                    ("Left/Right", "R20", True, "Rin"),
                                    ("Twenty-Second", "R21", True, "Rin"),
                                    ("Seeking", "R22", True, "Rin"),
                                    ("The Scent of Light", "R23", True, "Rin"),
                                    ("Edge of the World", "R24", True, "Rin"),
                                    ("The Context of Rin", "R25", True, "Rin"),
                                    ("Haze", "R26", True, "Rin"),
                                    ("Escapism", "R27", True, "Rin"),
                                    ("Limbo", "R28", True, "Rin"),
                                    ("Delirium", "R29", True, "Rin"),
                                    ("The Physiology of Art", "R30", True, "Rin"),
                                    ("Door", "R31", True, "Rin"),
                                    ("Shards of Ire", "R32", True, "Rin"),
                                    ("Illusions for People", "R33", True, "Rin"),
                                    ("Desperate Glory", "R34", True, "Rin"),
                                    ("Wavelength", "R35", True, "Rin"),
                                    ("Blue Period", "R36", True, "Rin"),
                                    ("The World Only You Can See", "R37", True, "Rin"),
                                    ("Problems of Self-Referential Logic", "R38", True, "Rin"),
                                    ("Measuring Shadows", "R39", True, "Rin"),
                                    (u"Raison d'être", "R40", True, "Rin"),
                                    ("Cowgirls! Napalm! Happy Day!", "R41", True, "Rin"),
                                    ("Proof of Existence", "R42", True, "Rin"),
                                    ("Packet Sniffers", "S8", True, "Shizune"),
                                    ("Talk to the Hand", "S9", True, "Shizune"),
                                    ("Chinese Whispers", "S10", True, "Shizune"),
                                    ("Hypertension", "S11", True, "Shizune"),
                                    ("Chronic Fatigue", "S12", True, "Shizune"),
                                    ("Graduation", "S13", True, "Shizune"),
                                    ("Spring into Action", "S14", True, "Shizune"),
                                    ("Best Laid Plans", "S15", True, "Shizune"),
                                    ("The Box", "S16", True, "Shizune"),
                                    ("Force Feedback", "S17", True, "Shizune"),
                                    ("United Nations", "S18", True, "Shizune"),
                                    ("Use-Mention Distinction", "S19", True, "Shizune"),
                                    ("Happiness", "S20", True, "Shizune"),
                                    ("Laughing Matters", "S21", True, "Shizune"),
                                    ("Pangrammatic Window", "S22", True, "Shizune"),
                                    ("Headgames", "S23", True, "Shizune"),
                                    ("Confrontation", "S24", True, "Shizune"),
                                    ("Duality", "S25", True, "Shizune"),
                                    ("Acute Triangle", "S26", True, "Shizune"),
                                    ("Determinacy", "S27", True, "Shizune"),
                                    ("Tongue-Tied", "S28", True, "Shizune"),
                                    ("Lookahead", "S29", True, "Shizune"),
                                    ("Spiral", "S30", True, "Shizune"),
                                    ("Rock Bottom", "S31", True, "Shizune"),
                                    ("Connected", "S32", True, "Shizune"),
                                    ("Watershed", "S33", True, "Shizune"),
                                    ("Terminal", "S34", True, "Shizune"), #Shizune bad end
                                    ("On the Flipside", "S36", True, "Shizune"),
                                    #S37 doesnt exist.
                                    #It does now. -md01
                                    ("Below the Belt", "S37", True, "Shizune"),
                                    ("Infinity", "S38", True, "Shizune"),
                                    )

# TITLE CARDS
    # Definition. This maps an id tuple to a tuple of displayed text, filename modifier, and the position of said text.
    # the display function is tcard() in ui_code.rpy
    displayDict["en"].act_names = {(1, "all"): ("Life Expectancy", "act1", 190, 117), #lulz
                                 (2, "bad"): ("Deep Six", "act2badend", 100, 250), #climatic
                                 (2, "emi"): ("Acceleration", "act2emi", 120, 200), #NWS
                                 (3, "emi"): ("2x400 Relay", "act3emi", 70, 350), #konflikti
                                 (4, "emi"): ("Dicks", "act4emi", 200, 250), #konflikti
                                 (2, "hanalilly"): ("Entanglement", "act2hanalilly", 380, 50), #animejet # gotta test [str]
                                 (3, "hanako"): ("Party Line", "act3hanako", 100, 400), #somedude
                                 (4, "hanako"): ("Mors Mortis", "act4hanako", 150, 250), #anonymouslurker
                                 (4, "hanatrue"): ("Heterotic Strings", "act4hanatrue", 150, 250), #who the hell made this?
                                 (5, "hanatrue"): ("Elucidation", "act5hanatrue", 350, 400), #same herepurpl
                                 (2, "lilly"): ("Past", "act2lilly", 80, 170), #skim #Needs changing, maybe with Raide's child Lilly sketch
                                 (3, "lilly"): ("Present", "act3lilly", 350, 400), #syureria
                                 (4, "lilly"): ("Future", "act4lilly", 80, 170), #skim
                                 (2, "rin"): ("Dream", "act2rin", 300, 220), #aura
                                 (3, "rin"): ("Distance", "act3rin", 150, 230), #kekekeke
                                 (4, "rin"): ("Difference", "act4rin", 200, 250), 
                                 (2, "shizune"): ("Cat and Mouse", "act2shizune", 90, 90), #celiest
                                 (3, "shizune"): ("Ellipsis", "act3shizune", 100, 400), #lild227
                                 (4, "shizune"): ("Silent Voice", "act4shizune", 200, 250)
                                }
    # credits
    
    displayDict["en"].creditstring = """{b}Head Writer{/b}
Aura
                                     
{b}Writers{/b}
Anonymous22
cpl_crud
Suriko
TheHivemind

{b}Editors{/b}
Kagami
Losstarot
Silentcook

{b}Music{/b}
Blue123
Nicol Armarfi

{b}Artists{/b}
Ambi07
gebyy-terar
Kamifish
moekki
Raide
raemz

{b}Additional Artists{/b}
climatic
Doomfest
yujovi

{b}Engineering{/b}
delta

{b}Producers{/b}
cpl_crud
Suriko

                                     
                                     

{b}Thanks{/b}
Celiest
chendo
climatic
Dark_Mercury
DeuceTrick
frumplstlskn
Ismuth
Kagami
konflikti
Magaran
Moogy
OverCoat
Peorth
Petaru
skim
Solaris
silentkyon
stirfriedweasel
Syureria



{b}Special Thanks{/b}
PyTom
KSG Threads on /vg/
RAITA




{b}Prealpha Repair{/b}
smspf 
Alphabro
Kelper
Buttface
Aki <3
muffinduck01
Gift of Gab
Stan Riders

                                     
{b}Also Helped{/b}
Parity
BWildness
Twoface
Sapiens
cometodaddycome"""

#Who the fuck are these people? - Kelper
# probably 4chan's /b/ board and anonymouses from it [str]
#\"B\"
#Anonymous

#smspf = shitty ms paint faggot 


    displayDict["en"].drugs_wordlist  =  ["Disopyramide",
                        "Warfarin",
                        "Diltiazem",
                        "Felodipine",
                        "Propanolol",
                        "Penbutolol",
                        "Carteolol",
                        "Procainamide",
                        "Heparin",
                        "Phenytoin",
                        "Verapamil",
                        "Quinidine",
                        "Flecainide",
                        "5mg/day",
                        "400mg/day",
                        "15ml/day",
                        "100mg/day",
                        "10ml/48hrs",
                        "10ml/day",
                        "200mg/12hrs",
                        "50mg/12hrs",
                        "500mg/48hrs",
                        "125mg/12hrs",
                        "25ml/day",
                        "nightmares",
                        "decreased concentration",
                        "bradycardia",
                        "clinical depression",
                        "insomnia",
                        "erectile dysfunction",
                        "abnormal vision",
                        "heart failure",
                        "nausea",
                        "dizziness",
                        "hallucinations",
                        "bronchospasm",
                        "dyspnea",
                        "fatigue",
                        "hypotension",
                        "heart block",
                        "cold extremities",
                        "diarrhea",
                        "cardiac arrest",
                        "ventricular fibrillation",
                        "ataxia",
                        "asthma"]
