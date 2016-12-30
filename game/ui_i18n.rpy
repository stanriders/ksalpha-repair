init -4 python:
    
    displayStrings = object()
    
    def switch_language(target):
        global displayStrings, gm_exit_to, s_scenes, save_name, act_names, np_current_language, _window_subtitle
        if target in available_languages:
            persistent.current_language = target
            np_current_language = target
            switch_runaming()
            displayStrings = displayDict[target]
            s_scenes = make_s_scenes(target)
            act_names = displayStrings.act_names
            save_name = last_scene_label
            _window_subtitle = displayStrings.window_name
            named_config()
            initialize_prefs()
            define_characters()
            if last_visited_label:
                gm_exit_to = wrap_label(last_visited_label)
        return True
        
    # # # [ russian hepburn/polivanov name translation switching [str]
    def switch_runamings(target):
        persistent.runamings = target
        switch_runaming()
        global displayStrings, gm_exit_to, s_scenes, save_name, act_names, np_current_language, _window_subtitle
        displayStrings = displayDict["ru"]
        s_scenes = make_s_scenes("ru")
        act_names = displayStrings.act_names
        save_name = last_scene_label
        return True
    # # # ] [str]
        
    def make_s_scenes(lang):
        if lang == master_language:
            return displayDict[master_language].s_scenes
        
        new_s_scenes = []
        for scene in displayDict[master_language].s_scenes:
            breakflag = False
            for langscene in displayDict[lang].s_scenes:
                if scene[1] == langscene[1]:
                    new_s_scenes.append(langscene)
                    breakflag = True
                    break
            if not breakflag:
                new_s_scenes.append(scene)
        return new_s_scenes
    
    def init_language(lang):
        if lang == master_language:
            store.displayDict[lang] = object()
            return
        import copy
        store.displayDict[lang] = copy.deepcopy(displayDict[master_language])
        store.available_languages.append(lang)

    # This is the language that contains the most information
    master_language = "en"
    
    available_languages = [master_language]
    
    if not persistent.current_language:
        persistent.current_language = master_language
    
    #fonts
    mainfont = "playtime.ttf"
    titlefont = mainfont
    interfacefont = mainfont
    srsfont = "gentium.ttf"
    jpfont = "mikachan.ttf"
    rufont = "playtime_cyr2.ttf"
    
    # it's being used in multiple scripts, much easier to put it here than redefine everywhere [str]
    def ruw(string):
        return (((('{font=') + (rufont)) + ('}')) + (string)) + ('{/font}')
        
    # container class for various UI strings. Yes, I am aware of config.translations.
    # Note that changing these may or may not be a good idea; sometimes the layout isn't flexible enough.
    
    displayDict = {}
    
    
    
init -2 python:
    ## TEST LANGUAGES
    # JAPANESE (just a stub for testing)
    
    init_language("jp")
    
    def jpw(string):
        return "{font=" + jpfont + "}" + string + "{/font} "
        
    displayDict["jp"].styleoverrides = {"font": jpfont, 
                                        "language": "eastasian",
                                        "line_spacing": 5}
    
    displayDict["jp"].quote_outer_open = u"「"
    displayDict["jp"].quote_outer_close = u"」"
    displayDict["jp"].quote_inner_open = u"『"
    displayDict["jp"].quote_inner_close = u"』"
    
    displayDict["jp"].window_name = u"かたわ少女"

    displayDict["jp"].activeLanguage = jpw(u"日本語")
    displayDict["jp"].allLanguages = {}
    displayDict["jp"].allLanguages["en"] = jpw(u"英語")
    displayDict["jp"].allLanguages["de"] = jpw(u"ドイツ語")
    displayDict["jp"].allLanguages["it"] = jpw(u"イタリア語")
    displayDict["jp"].allLanguages["jp"] = displayDict["jp"].activeLanguage
    displayDict["jp"].allLanguages["ru"] = jpw(u"ロシア語")
    
    displayDict["jp"].return_button_text = jpw(u"戻る")
    
    displayDict["jp"].config_language_caption = jpw(u"構成") + " > " + jpw(u"言語選択")

    displayDict["jp"].name_hi = u"寿勇"

# "雪の降りしきるある日、久夫の夢が叶おうとしたその時、心臓発作が彼を襲う"

    displayDict["jp"].s_scenes = ((jpw(u"寒空"), "NOP1", jpw("雪の降りしきるある日、久夫の夢が叶おうとしたその時、心臓発作が彼を襲う"), "Act 1"),
                                 )
    
    
    ##END TEST LANGUAGES

    # Master switch
    ### language-relevant config

    def named_config():

        config.file_entry_format = "%(time)s // "+displayStrings.play_time_label+": %(playtime)s\n%(save_name)s"

        config.time_format = displayStrings.timeformat
        config.menu_window_subtitle = displayStrings.window_name

        # The contents of the main menu.
        config.main_menu = [
            ( displayStrings.main_menu_start, ui.jumps("start_from_mm", "game_main_transition"), 'True'),
            ( displayStrings.main_menu_load, ui.jumps("load_screen", "main_game_transition"), 'renpy.list_saved_games()' ),
            ( displayStrings.main_menu_extra, ui.jumps("extra_from_mm"), 'get_available_scenes() or get_available_music() or get_available_images()'),
            ( displayStrings.main_menu_config, ui.jumps("prefs_screen", "main_game_transition"), 'True' ),
            ( displayStrings.main_menu_quit, ui.jumps("softquit"), 'True' ),
            ]

        # @__akiaki: added jumper to game/pause menu (only appears if z_jumper.rpy is present)
        if renpy.has_label('jumper'):
          config.main_menu.insert(3, (displayStrings.game_menu_jumper, ui.jumps("jumper", "intra_transition"), 'True')) #"Select Act"
          
        # it was done by ru translating team request [str]
        if persistent.current_language == "ru":
            config.main_menu.insert(5, (displayStrings.main_menu_credits, ui.jumps("show_credits", "intra_transition"), 'True')) #"Credits"

        # contents, game menu, etc.
        config.game_menu = [
           ( "return", displayStrings.game_menu_return, ui.jumps("_return"), 'True'),
           ( "gm_image", displayStrings.game_menu_show, ui.jumps("gm_image"), 'True'),
           ( "gm_image", displayStrings.game_menu_history,  ui.jumps("text_history_gm", "intra_transition"), 'True'), 
           ( "skipping", displayStrings.game_menu_skip, ui.jumps("_return_skipping"), 'config.allow_skipping and not renpy.context().main_menu'),
           ( "automode", displayStrings.game_menu_auto, ui.jumps("afm_on"), 'True'), 
           ( "prefs", displayStrings.game_menu_config, ui.jumps("prefs_screen", "intra_transition"), 'True' ),
           ( "save", displayStrings.game_menu_save, ui.jumps("save_screen", "intra_transition"), 'playthroughflag and not renpy.context().main_menu' ),
           ( "load", displayStrings.game_menu_load, ui.jumps("load_screen", "intra_transition"), 'renpy.list_saved_games()'),
           ( "mainmenu", displayStrings.game_menu_main, ui.jumps("confirm_mm", "intra_transition"), 'not renpy.context().main_menu' ),
           ( "quit", displayStrings.game_menu_quit, ui.jumps("confirm_quit", "intra_transition"), 'True' ),
           ]

        # @__akiaki: added jumper to game/pause menu (only appears if z_jumper.rpy is present)
        if renpy.has_label('jumper'):
          config.game_menu.insert(5, ('jumper', displayStrings.game_menu_jumper, ui.jumps("jumper", "intra_transition"), 'True')) #"Select Act"

        config.joystick_keys = [
            (displayStrings.joy_left, 'joy_left'),
            (displayStrings.joy_right, 'joy_right'),
            (displayStrings.joy_up, 'joy_up'),
            (displayStrings.joy_down, 'joy_down'),
            (displayStrings.joy_dismiss, 'joy_dismiss'),
            (displayStrings.joy_rollback, 'joy_rollback'),
            (displayStrings.joy_holdskip, 'joy_holdskip'),
            (displayStrings.joy_toggleskip, 'joy_toggleskip'),
            (displayStrings.joy_hide, 'joy_hide'),
            (displayStrings.joy_menu, 'joy_menu'),
            ]


init 5 python:

    switch_language(persistent.current_language)


### common / to be implemented from here on

init 3 python:

#    ex_m_tracks = (("Afternoon", music_tranquil),
#                   ("Ah Eh I Oh You", music_nurse),
#                   ("Air Guitar", music_soothing),
#                   ("Another Day", music_another),
#                   ("Cold Iron", music_tragic),
#                   ("Concord", music_lilly),
#                   ("Daylight", music_daily),
#                   ("Generic Happy Music", music_comedy),
#                   ("Painful History", music_hanako),
#                   ("Happiness", music_happiness),
#                   ("High Tension", music_tension),
#                   ("Hokabi", music_running),
#                   ("Lullaby of Open Eyes", music_serene),
#                   ("Moment of Decision", music_drama),
#                   ("Nocturne", music_night),
#                   ("Out of the Loop", music_kenji),
#                   ("Parity", music_rin),
#                   ("Passing of Time", music_timeskip),
#                   ("Raindrops and Puddles", music_dreamy),
#                   ("Rain", music_rain),
#                   ("Romance in Andante, arranged version", music_romance),
#                   ("Romance in Andante, piano version", music_credits),
#                   ("Sarabande from BVW1010", music_cellosolo),
#                   ("School Days", music_normal),
#                   ("Shadow of the Truth", music_sadness),
#                   ("Standing Tall", music_emi),
#                   ("Aria de l'etoile", music_twinkle),
#                   ("Stride", music_pearly),
#                   ("The Student Council", music_shizune),
#                   ("Wiosna", music_menus),
#                   ("Japanese Actually Think This is Rock", music_crappy))
                   


    # Commentary. A dictionary mapping identifier tags as they appear in the script to a tuple of title/text
    # Now handled in the script itself
    tl_notes = {}

