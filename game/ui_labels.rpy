# ui_labels.rpy: contains actual labels used by the ui and game engine
# In short, non-init code.
label splashscreen:

    if config.developer:
            return

    # called automatically by the engine after init, is expected to return
    # @__akiaki: made to play standard 4ls intro after disclaimer
    $ renpy.pause(0)
    scene black
    play movie vid_disc
    python:
        ui.timer(15.85, ui.jumps('splashscreen_4ls'))
        ui.interact()
    return

label splashscreen_4ls:
    scene black
    stop movie
    hide movie
    python:
        #renpy.sound.play(sfx_4lslogo)
        #ui.image(flslogo)
        #ui.timer(9, ui.returns, kwargs={"value":True})
        #ui.interact()
        devlvl = 0
        renpy.sound.play(sfx_4lslogo)
        ui.image(flslogo)
        ui.saybehavior()
        ui.timer(9.0, ui.returns, kwargs={'value':True})
        ui.interact()
        renpy.sound.stop()
    return

label main_menu:
    # our custom main menu, initialize only, then hand through to classic mm
    $ menu_init()
    jump main_menu_screen

#This is the old gm_bare. Commented it out to make way for the version from the final. -md01
# gm screens
#label gm_bare:
#    # game menu without any particular screen shown. NOT adding this to config.game_menu because it shouldn't be jumped to
#    python:
#        if previous_language == None:
#            previous_language = persistent.current_language
#        gm_active = True
#        config.skipping = None
#        layout.navigation("gm_bare")
#        if name_from_label(save_name):
#            currentscenename = name_from_label(save_name)
#            if not playthroughflag:
#                currentscenename += " ("+ displayStrings.game_menu_replay_indicator +")"
#            ui.text(displayStrings.play_time_label+": "+time_from_seconds(renpy.get_game_runtime())+"\n"+displayStrings.game_menu_current_scene+": "+currentscenename, text_align=0.5, xalign=0.5, yalign=0.98, size=18)
#        ui.interact()

#This is label gm_bare from the final -md01
label gm_bare:

    python:
        footerstring = ''
        if (previous_language) == (None):
            previous_language = persistent.current_language
        gm_active = True
        config.skipping = None
        layout.navigation('gm_bare')
        if name_from_label(save_name):
            currentscenename = name_from_label(save_name)
            if not (playthroughflag):
                currentscenename += ((' (') + (displayStrings.game_menu_replay_indicator)) + (')')
            footerstring += ((((((displayStrings.play_time_label) + (': ')) + (time_from_seconds(renpy.get_game_runtime()))) + ('\n')) + (displayStrings.game_menu_current_scene)) + (': ')) + (currentscenename)
        nowplaying = get_music_name()
        if nowplaying:
            footerstring += ((('\n') + (displayStrings.game_menu_current_music)) + (': ')) + (nowplaying)
        ui.text(footerstring, text_align=0.5, xalign=0.5, yalign=0.97999999999999998, size=18)
        ui.interact()

label text_history:
    # "readback"
    $ renpy.transition(config.main_game_transition)
    $ gm_active = True
    $ entered_from_game = True

label text_history_gm:
    python:
        # don't show the gm
        layout.navigation(None)
        ui.image(style.gm_root.background)
        ui.image("ui/bg-config.png", xalign=0.5, yalign=0.5)

        yadj = ui.adjustment()
        
        if not current_line and len(readback_buffer) == 0:
            lines_to_show = []
        elif current_line and len(readback_buffer) == 0:
            lines_to_show = [current_line]
        elif current_line and current_line != readback_buffer[-1]:  # current line may not yet be in rb buffer, but has the same format
            lines_to_show = readback_buffer + [current_line]
        else:
            lines_to_show = readback_buffer

        ui.vbox(xpos=180, ypos=120, background=None)
        ui.text(displayStrings.text_history_caption, style="page_caption")
        ui.hbox(xpos=0)
        vp = ui.viewport(yadjustment=yadj, offsets=(0.0,1.0), mousewheel=False, draggable=False, xmaximum=415, ymaximum = 296, xalign=0.5, yalign=0.5)
        ui.vbox(xfill=True)
        for line in lines_to_show:
            if line[0] and line[0] != " ":
                ui.text(line[0], style="readback_label", **displayStrings.styleoverrides)
            ui.text(line[1], style="readback_text", **displayStrings.styleoverrides)
            ui.null(height=10)
        ui.close()
        ui.null(width=10)
        ui.vbox()
        ui.imagebutton(ib_base("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=decrease_rb_yoffset)
        ui.bar(adjustment=yadj, style='vscrollbar')
        ui.imagebutton(ib_base("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=increase_rb_yoffset)
        ui.close()
        ui.close()
        ui.close()

        viewportkeys(decrease_rb_yoffset,increase_rb_yoffset)

        if not entered_from_game:
            return_button(_intra_jumps(_game_menu_screen, "intra_transition"))
        else:
            entered_from_game = False
            return_button(ui.jumps("custom_return"))

        ui.interact()
        # here we do something with gi_result (or not)
        renpy.jump("text_history_gm")

label gm_image:
    # game menu without _anything_ shown. Also the base for building stuff from scratch.
    python:
        # don't show the gm
        layout.navigation(None)
        # use the predefined transition
        renpy.transition(config.intra_transition)
        # here we show stuff (or not)
        # invisible button as large as the screen. Not using the simpler cookbook example because it doesn't kill the overlay.
        ui.saybehavior()
        # wait for something to happen
        ui.add(renpy.Keymap(game_menu=ui.returns(True)))
        ui.interact()
        # here we do something with gi_result (or not)
        renpy.transition(config.intra_transition)
        renpy.jump(_game_menu_screen) # or "_return"?

label quit_from_os:
    # called when program quit is requested from outside the game
    call _enter_menu from quit_from_os_1
    $ quit_from_os_flag = True

label confirm_quit:
# Our personal quit message. Notably called when the OS wants to quit the game - has to be handled.
    python:
        if not ask_to_quit: 
            renpy.jump("softquit")
        else:
            transition = config.intra_transition
            if not gm_active:
                transition = config.enter_transition
            gi_result = _yesno_prompt(None, displayStrings.yesno_quit, im.Image("ui/sd-hanako.png",xpos=515,ypos=305), transition=transition)
            if gi_result:
                renpy.jump("softquit")
            else:
                if quit_from_os_flag and gm_active:
                    quit_from_os_flag = False
                    renpy.jump("simple_return")
                elif gm_active:
                    quit_from_os_flag = False
                    renpy.jump(_game_menu_screen)
                else:
                    quit_from_os_flag = False
                    renpy.jump("_return")

label confirm_mm:
# Our personal "back to main menu" message.
    python:
        layout.navigation(None)
        if playthroughflag:
            gi_result = _yesno_prompt(None, displayStrings.yesno_return_to_main, im.Image("ui/sd-shizune.png",xpos=195,ypos=275))
            if gi_result:
                renpy.music.stop()
                renpy.full_restart(transition=config.game_main_transition)
            else:
                renpy.jump(_game_menu_screen) # maybe this could _return instead if appropriate
        else:
            renpy.music.stop()
            renpy.full_restart(transition=config.game_main_transition)

label prefs_screen:
#custom preferences menu. Decidedly more custom than the rest.
    python:
    
        layout.navigation(None)
        if prefs_looped:
            renpy.transition(ImageDissolve(im.Tile("ui/tr-checkwipe.png"), 0.5, 8))
        elif renpy.context().main_menu and not coming_from_prefs_sub:
            renpy.transition(config.main_game_transition)
        else:
            renpy.transition(config.intra_transition)
        if renpy.context().main_menu: # We'll draw a fake main menu for style reasons, or it'll just be boring black in the mm
            ui.image(style.mm_root.background)
        coming_from_prefs_sub = False
        ui.image(style.gm_root.background)
        prefs_looped = False # or we'll have a problem the next time this menu is invoked
        ui.image("ui/bg-config.png", xalign=0.5, yalign=0.5)

        group_spacing = 1

        ui.vbox(xpos = 180, ypos = 120)
        ui.text(displayStrings.config_page_caption, style="page_caption")
        ui.null(height=8)
        ui.hbox()
        ui.null(width=20)
        ui.vbox()
        if not persistent.hdisabled:
            checkboximage = "ui/bt-cf-unchecked.png"
        else:
            checkboximage = "ui/bt-cf-checked.png"
        widget_button(displayStrings.hdisabled_label, checkboximage, toggle_h, xsize=300, widgetyoffset=0)
        ui.null(height=group_spacing)
        # here come the buttons. First our custom ones.
        fullscreen_p.render_preference()
        transition_p.render_preference()
        ui.null(height=group_spacing)
        unreadskip_p.render_preference()
        choiceskip_p.render_preference()
        ui.null(height=group_spacing)
        textspeed_p.render_preference()
        afm_p.render_preference()
        ui.null(height=group_spacing)
        musicvol_p.render_preference()
        ui.hbox()
        sfxvol_p.render_preference()
        ui.null(width=20)
        widget_button(displayStrings.config_sfxtest_label, "ui/bt-musicplay.png", test_sound)

        ui.close()
        ui.null(height=group_spacing)
        widget_button(displayStrings.config_language_sel, "ui/bt-language.png", ui.jumps("language_screen"), xsize=300, widgetyoffset=3)
        if renpy.display.joystick.enabled: #or config.always_has_joystick:
            widget_button(displayStrings.config_gamepad_label, "ui/bt-gamepad.png", ui.jumps("joystick_screen"), xsize=300, widgetyoffset=3)
        
        
        ui.close()
        ui.close()
        ui.close()

        return_button(ui.returns("return"))
        
        ui.keymap(I=devlvl_I)
        ui.keymap(D=devlvl_D)
        ui.keymap(Q=devlvl_Q)
        ui.keymap(N=devlvl_N)

        #ui.image("ui/sd-rin.png", xpos=580, ypos=60)
        gi_result = ui.interact()
        if gi_result == "return":
            if renpy.context().main_menu:
                renpy.jump("_return")
            else:
                renpy.transition(config.intra_transition)
                renpy.jump(_game_menu_screen)
        prefs_looped = True
        renpy.jump("prefs_screen")

label language_screen:
    python:
        coming_from_prefs_sub = True
        
        renpy.transition(config.intra_transition)
        if renpy.context().main_menu: # We'll draw a fake main menu for style reasons, or it'll just be boring black in the mm
            ui.image(style.mm_root.background)
        ui.image(style.gm_root.background)
        ui.image("ui/bg-config.png", xalign=0.5, yalign=0.5)
        layout.navigation(None)
        ui.vbox(xpos = 180, ypos = 120)
        ui.text(displayStrings.config_language_caption, style="page_caption")
        ui.null(height=8)
        ui.hbox()
        ui.null(width=10)
        ui.vbox()
        
        for language in available_languages:
            
            tl_progress = make_percentage(len(displayDict[language].s_scenes), len(displayDict[master_language].s_scenes))
            if tl_progress >= 100:
                tl_percentage = ""
            else:
                tl_percentage = ", " + str(tl_progress) + "%"
            
            button_label = displayDict[language].activeLanguage+" ("+ displayStrings.allLanguages[language] + tl_percentage + ")"
            if language == persistent.current_language:
                button_state = "active"
                button_image = "ui/bt-language.png"
                button_function = None
            else:
                button_state = "button"
                button_image = "ui/bt-blank.png"
                button_function = renpy.curry(switch_language)(target=language)
            widget_button(text=button_label, displayable=button_image, clicked=button_function, state=button_state, xsize=300, widgetyoffset=3)
        
        # # # [ russian hepburn/polivanov name translation switching [str]
        if persistent.current_language == "ru":
            widget_button(displayStrings.config_language_naming, "ui/bt-language.png", ui.jumps("language_runamings_screen"), xsize=300, widgetyoffset=3)
        # # # ] [str]
        
        ui.close()
        ui.close()
        ui.close()
        
        if not renpy.context().main_menu:
            ui.text(displayStrings.config_language_restart_note, text_align=0.5, xalign=0.5, yalign=0.98, size=18)
        
        return_button(ui.jumps("prefs_screen"))

        ui.interact()

    jump language_screen

# # #
# # # [ This is Russian-only name translation selection menu.   
label language_runamings_screen:
    python:
        coming_from_prefs_sub = True
        
        renpy.transition(config.intra_transition)
        if renpy.context().main_menu:
            ui.image(style.mm_root.background)
        ui.image(style.gm_root.background)
        ui.image("ui/bg-popup.png", xalign=0.5, yalign=0.5)
        layout.navigation(None)
        ui.vbox(xpos = 255, ypos = 220)
        ui.text(displayStrings.config_language_naming, style="page_caption")
        ui.null(height=4)
        ui.hbox()
        ui.null(width=4)
        ui.vbox()
        
        # persistent.runamings is defined in ui-strings-RU [str]
        button_label = ruw(u"Поливанов")
        if persistent.runamings == "poli":
            button_state = "active"
            button_image = "ui/bt-language.png"
            button_function = None
        else:
            button_state = "button"
            button_image = "ui/bt-blank.png"
            button_function = renpy.curry(switch_runamings)(target="poli")
        widget_button(text=button_label, displayable=button_image, clicked=button_function, state=button_state, xsize=200, widgetyoffset=3)
        
        button2_label = ruw(u"Хэпбёрн")
        if persistent.runamings == "hepb":
            button2_state = "active"
            button2_image = "ui/bt-language.png"
            button2_function = None
        else:
            button2_state = "button"
            button2_image = "ui/bt-blank.png"
            button2_function = renpy.curry(switch_runamings)(target="hepb")
        widget_button(text=button2_label, displayable=button2_image, clicked=button2_function, state=button2_state, xsize=200, widgetyoffset=3)
        
        ui.close()
        ui.close()
        ui.close()
        
        # using custom bg = need to create new return button
        # also, i'm so happy that KS is forced to run at 800x600 [str]
        widget_button(displayStrings.game_menu_return, "ui/bt-blank.png", clicked=ui.jumps("language_screen"), xsize=65, textxoffset=0, xpos=480, ypos=345)
        #return_button(ui.jumps("language_screen"))

        ui.interact()

    jump language_runamings_screen

# # # ] [str]
# # # 

label joystick_screen:
    python:
        coming_from_prefs_sub = True
        renpy.transition(config.intra_transition)
        if renpy.context().main_menu: # We'll draw a fake main menu for style reasons, or it'll just be boring black in the mm
            ui.image(style.mm_root.background)
        ui.image(style.gm_root.background)
        ui.image("ui/bg-config.png", xalign=0.5, yalign=0.5)
        layout.navigation(None)
        ui.vbox(xpos = 180, ypos = 120)
        ui.text(displayStrings.gamepad_caption, style="page_caption")
        ui.null(height=8)
        ui.hbox()
        ui.null(width=10)
        ui.vbox()
        for label, key in config.joystick_keys:
            joy_button(label, key)
        ui.close()
        ui.close()
        ui.close()

        return_button(ui.jumps("prefs_screen"))

        ui.interact()

    jump joystick_screen

label load_screen:
    $ mode = "manual"
    
label load_screen_loop:
#custom replacement for _load_screen
    python:
        if renpy.context().main_menu: # We'll draw a fake main menu for style reasons, or it'll just be boring black in the mm
            mybackground = LiveComposite((800, 600),
                                         (0, 0), style.mm_root.background,
                                         (0, 0), style.gm_root.background,
                                         (150, 100), "ui/bg-config.png")
        else:
            mybackground = LiveComposite((800, 600),
                                         (0, 0), style.gm_root.background,
                                         (150, 100), "ui/bg-config.png")

        fn, exists = custom_file_picker("load", False, mode, mybackground)

        if fn == "return":
            if renpy.context().main_menu:
                renpy.jump("_return")
            else:
                renpy.transition(config.intra_transition)
                renpy.jump(_game_menu_screen)
        elif fn == "_setmode":
            mode = exists
            renpy.jump("load_screen_loop")
        elif fn == "delete":
            background = None
            if renpy.context().main_menu:
                background = style.mm_root.background
            if _yesno_prompt(None, displayStrings.yesno_delete_savegame % exists, im.Image("ui/sd-emi.png",xpos=510,ypos=275), background=background):
                #persistent.fpicker_yoffset = 0
                renpy.unlink_save(exists)
        else:
            if not renpy.context().main_menu and playthroughflag:
                if _yesno_prompt(None, displayStrings.yesno_load_in_game, im.Image("ui/sd-emi.png",xpos=510,ypos=275)):
                    renpy.load(fn)
            else:
                renpy.load(fn)

        renpy.jump("load_screen")

label save_screen:
#custom replacement for _save_screen
    python:
        mybackground = LiveComposite((800, 600),
                                     (0, 0), style.gm_root.background,
                                     (150, 100), "ui/bg-config.png")

        _fn, _exists = custom_file_picker("save", True, False, mybackground)

        if _fn == "return":
            renpy.transition(config.intra_transition)
            renpy.jump(_game_menu_screen)
        elif _fn == "delete":
            if _yesno_prompt(None, displayStrings.yesno_delete_savegame % _exists, im.Image("ui/sd-emi.png",xpos=510,ypos=275)):
                #persistent.fpicker_yoffset = 0
                renpy.unlink_save(_exists)
        else:
            if not _exists or _yesno_prompt(None, displayStrings.yesno_save_overwrite, im.Image("ui/sd-lilly.png",xpos=195,ypos=275)):
                minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
                if save_name:
                    full_save_name = save_name + "#" + str(renpy.get_game_runtime())
                else:
                    full_save_name = "#" + str(renpy.get_game_runtime())
                try:
                    renpy.save(_fn, full_save_name)
                except Exception, e:
                    if config.debug:
                        raise
                    message = ( _(u"The error message was:") + "\n\n" + 
                                e.__class__.__name__  + ": " + unicode(e) + "\n\n" +
                                _(u"You may want to try saving in a different slot, or playing for a while and trying again later.") )
                    _show_exception(_(u"Save Failed."), message)
                else:
                    persistent.fpicker_yoffset = -1
                    _prompt(None, displayStrings.yesno_savesuccess % _fn, im.Image("ui/sd-rin.png",xpos=510,ypos=165))
                renpy.jump(_game_menu_screen)
        renpy.jump("save_screen")

label extra_from_mm:
# coming from main menu (i.e. not back from a submenu)? then it's a jump out of context.
    $ renpy.transition(config.main_game_transition)
    $ renpy.music.play(music_menus, fadeout=0.5, if_changed=True)

label extra_menu:
    # extras menu.
    python:

        # this can speed up gallery display considerably
        gallery_predict()

        sceneselectstate = "disabled"
        if get_available_scenes():
            sceneselectstate = "button"
        gallerystate = "disabled"
        if get_available_images():
            gallerystate = "button"
        musicstate = "disabled"
        if get_available_music():
            musicstate = "button"
        openingstate = "disabled"
        if persistent_seen("op_video"):
            openingstate = "button"

        ui.image(LiveComposite((800, 600),
                               (0, 0), style.mm_root.background,
                               (0, 0), style.gm_root.background,
                               (150, 100), "ui/bg-config.png"))

        ui.vbox(xpos=180, ypos=120, background=None)
        ui.text(displayStrings.extra_menu_caption, style="page_caption")
        ui.null(height=10)
        ui.hbox(box_spacing=15)
        extra_button(displayStrings.extra_music_button_label,"ui/sd-lilly.png",clicked=ui.jumps("music_menu", "intra_transition"), state=musicstate)
        extra_button(displayStrings.extra_gallery_button_label,"ui/sd-rin.png",clicked=ui.jumps("cg_gallery", "intra_transition"), state=gallerystate)
        extra_button(displayStrings.extra_scene_button_label,"ui/sd-shizune.png",clicked=ui.jumps("scene_select", "intra_transition"), state=sceneselectstate)
        extra_button(displayStrings.extra_opening_button_label,"ui/sd-emi.png",clicked=ui.jumps("opening_ex", "intra_transition"), state=openingstate)
        ui.close()
        ui.close()
        ui.hbox(xpos=540, ypos=346)
        extra_button(displayStrings.return_button_text,"ui/sd-hanako.png", clicked=ui.jumps("main_menu", "game_main_transition"), state="return")
        ui.close()

        if not persistent.commentary_on:
            checkboximage = "ui/bt-cf-unchecked.png"
        else:
            checkboximage = "ui/bt-cf-checked.png"
        widget_button(displayStrings.commentary_label, checkboximage, toggle_commentary, xsize=340, widgetyoffset=0, xpos=180, ypos=450)

        # hax
        if has_devlvl() and renpy.has_label("cruise_control"):
            layout.button("[ flow tests ]", "mm", clicked=ui.jumps("cruise_control"), xpos=510, ypos=115)

        ui.add(renpy.Keymap(game_menu=ui.jumps("main_menu", "game_main_transition")))
        ui.interact()
        renpy.transition(ImageDissolve(im.Tile("ui/tr-checkwipe2.png"), 0.5, 8))
        renpy.jump("extra_menu")


label opening_ex:
    scene black
    with config.game_main_transition
    python:
        renpy.movie_cutscene(vid_op)
        renpy.music.play(music_menus, fadein=5.0, fadeout=0.5, if_changed=True)
        renpy.transition(config.main_game_transition)
    jump extra_menu

label music_menu:
    # extras - music menu
    python:
        # this is a kinda roundabout way to do this but necessary since renpy.music.get_playing() can lag considerably.
        if renpy.music.get_playing():
            nowplaying = "???"
            for (name, file) in ex_m_tracks:
                if file == renpy.music.get_playing():
                    nowplaying = name
        else:
            nowplaying = ""
        available_music = get_available_music()

label music_menu_loop:
    # DON'T JUMP HERE DIRECTLY FROM OUTSIDE UNLESS YOU LIKE READING TRACEBACKS.
    python:
        auto_offset = 34
        if not persistent.mpicker_yoffset:
            persistent.mpicker_yoffset = 0

        yadj = ui.adjustment(range=auto_offset * (len(ex_m_tracks) - 8), value=persistent.mpicker_yoffset, changed=store_m_yoffset)

        viewportkeys(decrease_m_yoffset,increase_m_yoffset)

        ui.image(LiveComposite((800, 600),
                               (0, 0), style.mm_root.background,
                               (0, 0), style.gm_root.background,
                               (150, 100), "ui/bg-config.png"))

        ui.vbox(xpos=180, ypos=120, background=None)
        ui.text(displayStrings.music_page_caption, style="page_caption")
        if nowplaying:
            ui.text(displayStrings.music_now_playing + ": " + nowplaying, style="prefs_label")
        else:
            ui.text(" ", style="prefs_label")
        ui.null(height=4)
        ui.hbox(xpos=4)
        vp = ui.viewport(yadjustment=yadj, mousewheel=False, draggable=False, xmaximum=415, ymaximum = 270, xalign=0.5, yalign=0.5)
        ui.vbox(xfill=True)
        for name, file in ex_m_tracks:
            if file in available_music:
                if file == "" or not renpy.loadable(file):
                    layout.button(name, "mm", clicked=None)
                else:
                    layout.button(name, "mm", clicked=ui.returns((name, file)))
                ui.null(height=1)
            else:
                ui.null(height=1)
                ui.image(ib_disabled("ui/bg-lockedtrack.png", xpos=14))
                ui.null(height=1)
            ui.null(height=2)
        ui.close()
        ui.vbox()
        ui.imagebutton(ib_base("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=decrease_m_yoffset)
        ui.bar(style='vscrollbar2', adjustment = yadj, changed=store_m_yoffset)
        ui.imagebutton(ib_base("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=increase_m_yoffset)
        ui.close()
        ui.close()
        ui.close()

        ui.hbox(xpos=180, ypos=449)
        musicvol_p_jukebox.render_preference()
        ui.null(width=20)
        widget_button(displayStrings.music_stop_button_text, "ui/bt-musicstop.png", clicked=ui.returns(("", "")))
        ui.close()

        return_button(_intra_jumps("extra_menu", "intra_transition"))
        result = ui.interact()
        renpy.music.play(result[1], fadeout=0.5, if_changed=True)
        nowplaying = result[0]
        renpy.jump("music_menu_loop")

label scene_select:
    # entry point from outside
    # This needs some special code because it's possible to init the game to here
    python:
        menu_init()
        ss_desc = ""
        if filter != "Act 1":
            persistent.spicker_yoffset = 0
        filter = "Act 1"

label scene_select_loop:
    # entry point from self
    python:
        config.has_autosave=True
        ui.image(LiveComposite((800, 600),
                               (0, 0), style.mm_root.background,
                               (0, 0), style.gm_root.background,
                               (150, 100), "ui/bg-config.png"))

        available_scenes = get_available_scenes(filter, include_locked=True) or ()

        scrollable = False
        if len(available_scenes) > 8:
            scrollable = True

        if scrollable:
            auto_offset = 1.0 / (len(available_scenes) - 8)
            # emergency absolute value override
            auto_offset = 34
        else:
            auto_offset = 0

        if not persistent.spicker_yoffset:
            persistent.spicker_yoffset = 0.0

        ui.vbox(xpos=180, ypos=120, background=None)
        ui.text(displayStrings.scene_page_caption, style="page_caption")
        ui.hbox()
        shown_buttons = ("Act 1", "Emi", "Hanako", "Lilly", "Rin", "Shizune")
        
        for button in shown_buttons:
            if button == "Act 1":
                label = displayStrings.act_term + " 1"
            elif button == "Emi":
                label = displayStrings.name_emi
            elif button == "Hanako":
                label = displayStrings.name_ha
            elif button == "Lilly":
                label = displayStrings.name_li
            elif button == "Rin":
                label = displayStrings.name_rin
            else: # button == "Shizune":
                label = displayStrings.name_shi
            
            path = button
             
            if button == filter:
                layout.button(label, "rpa_active", clicked=None)
            elif get_available_scenes(path):
                layout.button(label, "rpa", clicked=ui.returns(("_setfilter",path)))
            else:
                layout.button(label, "rpa", clicked=None)
        ui.close()
        ui.hbox()

        yadj = ui.adjustment(range=auto_offset * (len(available_scenes) - 8), value=persistent.spicker_yoffset, changed=store_s_yoffset)

        vp = ui.viewport(yadjustment=yadj, mousewheel=False, draggable=False, xmaximum=400, ymaximum = 270, xalign=0.5, yalign=0.5)
        ui.vbox(xfill=True)
        for (name, label, display, path, unlocked) in available_scenes:
            if unlocked:
                if has_devlvl():
                    extension = " (" + label +")"
                else:
                    extension = ""
                ss_button(name+extension, display, clicked=ui.returns((name,label)))
                ui.null(height=1)
            else:
                ui.null(height=1)
                ui.image(ib_disabled("ui/bg-lockedtrack.png", xpos=14))
                ui.null(height=1)
            ui.null(height=2)

        viewportkeys(decrease_s_yoffset,increase_s_yoffset)

        ui.close()
        ui.null(width=20)
        ui.vbox(box_spacing=2)
        if scrollable:
            ui.imagebutton(ib_base("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=decrease_s_yoffset)
            ui.bar(style='vscrollbar2', adjustment = yadj, changed=store_s_yoffset)
            ui.imagebutton(ib_base("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=increase_s_yoffset)
        else:
            ui.imagebutton(ib_disabled("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=None)
            ui.bar(style='vscrollbar2_disabled')
            ui.imagebutton(ib_disabled("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=None)
        ui.close()
        ui.close()
        ui.close()

        return_button(ui.jumps("extra_menu", "intra_transition"))

        if has_devlvl():
            if playthroughflag:
                checkboximage = "ui/bt-cf-unchecked.png"
            else:
                checkboximage = "ui/bt-cf-checked.png"
            widget_button(displayStrings.scene_playthrough_label, checkboximage, toggle_playthrough, xsize=340, widgetyoffset=0, xpos=180, ypos=450)
        else:
            completion_percentage = get_completion_percentage()
            ui.text(displayStrings.scene_completion_label % completion_percentage, style="prefs_label", xpos=180, ypos=450)
            
        ui.add(DynamicDisplayable(refresh_label))
        what, where = ui.interact()
        readback_buffer = []
        if what not in ("_setfilter", "_pt_toggled"):
            init_vars()
            last_scene_label = where
            config.has_autosave=False
            renpy.music.stop(fadeout=0.5)
            renpy.transition(config.game_main_transition)
            renpy.scene()
            renpy.show("black")
            renpy.block_rollback()
            ui.timer(1.0, ui.returns, kwargs={"value":True})
            ui.interact() # or block_rollback() won't register. A pause() won't do for some reason.
            save_name = where
            if playthroughflag or not renpy.has_label("replay_"+where):
                jumptarget = where
            else:
                jumptarget = "replay_"+where
            ui.jumpsoutofcontext(jumptarget)() # function returns function
        elif what == "_setfilter":
            filter = where
            persistent.spicker_yoffset = 0
        elif what == "_pt_toggled":
            renpy.transition(ImageDissolve(im.Tile("ui/tr-checkwipe2.png"), 0.5, 8))

        renpy.jump("scene_select_loop")

label cg_gallery:
    # actual gallery display code. the libraries for this are in ui_code.
    python:

        mygallery = Gallery()
        mygallery.locked_background = "ui/bg-ex-gallery-lockedimage.png"
        mygallery.background = (LiveComposite((800, 600),
                                              (0, 0), style.mm_root.background,
                                              (0, 0), style.gm_root.background,
                                              (150, 100), "ui/bg-config.png"))
        mygallery.locked_button = ib_disabled("ui/bt-cg-locked.png")
        mygallery.grid_layout((4,3),(175,160),(115,90))
        i = 0
        page = 0
        for i_image in ex_g_images:
            if i == 0:
                page += 1
                mygallery.page(displayStrings.gallery_num_page_prefix + str(page))
                i = 0
            mygallery.autobutton(i_image)
            i += 1
            if i >= 12:
                i = 0
        if page == 0:
            mygallery.page(displayStrings.gallery_num_page_error)
        mygallery.show()

# utilities
label simple_return:
    return

label custom_noisy_return:
    $ renpy.play(config.exit_sound)

# Return to the game.
label custom_return:
    $ gm_active = False
    if renpy.context().main_menu:
        $ renpy.transition(config.game_main_transition)
        jump _main_menu_screen
    $ renpy.transition(config.exit_transition)
    if gm_exit_to and previous_language != persistent.current_language:
        nvl clear
        stop music fadeout 1.0
        $ temp_exit = gm_exit_to
        $ gm_exit_to = None
        $ previous_language = None
        $ renpy.jump_out_of_context(temp_exit)
    return

label afm_on:
# turn on auto mode.
    python:
        turn_afm_on()
        renpy.jump("_return")

label start_from_mm:
# do stuff that needs to be done when starting the game from the mm
    
    stop music fadeout 1.0
    
    scene black
    with config.game_main_transition

    python:
        playthroughflag = True
        init_vars()
        renpy.pause(2)
        renpy.jump_out_of_context("start")

label softquit:
# fades out (if transitions are on) and quits
    python:
        if _preferences.transitions != 0 :
            renpy.music.stop(fadeout=0.5)
            renpy.transition(dissolve)
            ui.image(Solid("#000"))
            renpy.pause(0.7)
        renpy.jump("_quit")


label scene_deleted:
    window hide
    # shown instead of h scenes if suppression is on
    play music sfx_heartfast

    scene pink
    with dissolve

    scene prawns
    with Dissolve(2.0)

    $ renpy.pause(2.0)

    scene white
    with Dissolve(8.0)

    stop music fadeout 1.0
    $ renpy.transition(dissolve)
    window show
    return

label en_timeskip:
    # s_ prefix because it's meant to be called from the I-Machine
    if playthroughflag:
        window hide
        $ renpy.pause(2.0)

        play music music_timeskip

        show kslogo heart at Position(xalign=0.5, yalign=0.5)
        with clockwipe

        scene black
        show kslogo words at Position(xalign=0.5, yalign=0.5)
        with clockwipe

        $ renpy.pause(2.0)

        stop music fadeout 2.0

        scene black
        with clockwipe

        $ renpy.pause(2.0)
        window show

    return
    
label en_rintimeskip:
    # s_ prefix because it's meant to be called from the I-Machine
    # TIMESKIP FOR RINS PATH
    if playthroughflag:
        $ renpy.pause(2.0)

        play music music_timeskip

        show kslogo heart at Position(xalign=0.5, yalign=0.5)
        with clockwipe

        scene black
        show kslogo words at Position(xalign=0.5, yalign=0.5)
        with clockwipe

        $ renpy.pause(2.0)

        stop music fadeout 2.0

        scene black
        with clockwipe

        $ renpy.pause(2.0)

    return


label credits (simple=False):
    
    python:
        if not simple:
            bouncepre = "{color=#00000000}____________________________________{/color}"
        else:
            bouncepre = ""
        
        creditprefix = "\n\n\n\n\n\n\n\n\n{image=ui/cred_logo.png}" + bouncepre + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        creditsuffix = "\n\n\n\n\n\n\n\n\n\n\n{image=ui/4lsl-small.png}" + bouncepre + "\n\n\n\n\n\n\n\n\n\n\n\n"
        credbgtr = Fade(1.0,0,1.0)
        slidetime = 6
        bgani = anim.TransitionAnimation("ui/cred_emi.png",slidetime,credbgtr,
                                      "ui/cred_hanako.png",slidetime,credbgtr,
                                      "ui/cred_lilly.png",slidetime,credbgtr,
                                      "ui/cred_rin.png",slidetime,credbgtr,
                                      "ui/cred_shizune.png",slidetime,credbgtr,
                                      "ui/cred_misha.png",slidetime,credbgtr,
                                      "ui/cred_none.png")
        
        allcredits = creditprefix + displayStrings.creditstring + creditsuffix
        
        class creditDisp(renpy.Displayable):
            def __init__(self):
                renpy.Displayable.__init__(self)
    
                self.creditstext = Text(allcredits, text_align=0.5)
                
                if simple:
                    self.xo = 302
                else:
                    self.xo = 310
                self.yo = 0
                self.runtime = 60
                self.isrunning = False
                self.hasfinished = False
                
                self.framelength = 0.04 # 25 fps
                
                self.rend = renpy.render(self.creditstext,  800, 600, 0, 0)
                self.cwidth, self.cheight = self.rend.get_size()
                
                self.normalspeed = self.cheight / ( self.runtime / self.framelength )
                self.fastspeed = self.normalspeed * 10
                self.currentspeed = self.normalspeed
                
            
            def start(self):
                self.isrunning = True
            
            def visit(self):
                return [ self.creditstext ]
            
            def yplus(self):
                newpos = self.yo - self.currentspeed
                if newpos > 600 - self.cheight:
                    return newpos
                else:
                    self.hasfinished = True
                    return self.yo
    
            def render(self, width, height, st, at):
                
                if self.isrunning:
                    self.yo = self.yplus()
                
                rv = renpy.Render(width, height)
                rv.blit(self.rend, (self.xo, self.yo))
                renpy.redraw(self, self.framelength)
                renpy.timeout(self.framelength)
                return rv
                
             
            def event(self, ev, x, y, st):

                import pygame
                if (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1):
                    self.currentspeed = self.fastspeed
                elif (ev.type == pygame.MOUSEBUTTONUP and ev.button == 1):
                    self.currentspeed = self.normalspeed
                
                if self.hasfinished:
                    return True
                
                raise renpy.IgnoreEvent()
                   
                   
        creditsInst = creditDisp()
    
        config.skipping = False
    
    
    ### begin showing stuff
    $ wdt_off()
    
    $ old_game_menu_screen = _game_menu_screen
    $ _game_menu_screen = None
    
    $ this_rollback = config.rollback_enabled
    $ config.rollback_enabled = False

    $ config.allow_skipping = False

    $ ask_to_quit = False
    $ _preferences.afm_time = 0
    $ may_afm = False

    scene black
    show credits mask
    with Dissolve(1.0)
    
    $ renpy.pause(1.0, hard=True)
    
    $ renpy.show("roll", behind="credits", what=creditsInst, at_list=[Position(xpos=0.5, xanchor=0.5, yalign=0.0)]) #0.4827
    with Dissolve(2.0)

    $ renpy.pause(2.0, hard=True)
    
    if not simple:
        $ renpy.music.play(music_credits, loop=False)
    $ creditsInst.start()
    
    $ renpy.pause(6.0, hard=True)
    
    if not simple:
        $ renpy.show("bgani", behind="roll", what=bgani, at_list=[Position(xpos=0.3, xanchor=0.5, yalign=0.5)])
    with Dissolve(2.0)
    
    $ renpy.pause(52.0, hard=True)
    
    scene endscreen
    with None
    
    # nope, it's only breaking simple credits [str]
    #if not simple:
    #    scene endscreen
    #    with None
    #else:
    #don't ask me why, I have NO idea
    #    scene endscreen at Position(xpos=0.5128) #397
    #    with None
    
    
    $ renpy.pause(2.0, hard=True)
    
    $ renpy.show("copyright", what=Text("© 2006 - 2009", text_align=0.5, size=15), at_list=[Position(xpos=0.5, xanchor=0.5, yalign=0.605)])
    with Dissolve(2.0)
    $ renpy.pause(3.0, hard=True)
    
    $ renpy.music.set_volume(0.0,1.0)

    scene black
    with Dissolve(2.0)

    $ renpy.pause(1.0, hard=True)
    
    $ config.allow_skipping = True
    $ config.rollback_enabled = this_rollback
    $ _game_menu_screen = old_game_menu_screen

    stop music
    
    $ renpy.music.set_volume(1.0,0.0)
    $ may_afm = True
    return

label after_load:
    $ ask_to_quit = True
    $ savegame_langage = np_current_language
    $ switch_language(persistent.current_language)
    if persistent.current_language != savegame_langage:
        $ renpy.pop_return()
        $ renpy.jump(wrap_label(last_visited_label))
    return
    
#**************************************
label start:
    # game entry point
    
    stop music

    $ ask_to_quit = True
    
    $ renpy.scene()
    $ np_current_language = persistent.current_language
    $ renpy.block_rollback()
    $ readback_buffer = []
    nvl clear
    #hand over control to the I-Machine
    jump imachine

# The following are I-Machine exit points.
# They also track stuff for the benchmark.

label emiend:
    $ wdt_off()
    scene white
    with Dissolve(4.0)
    $ persistent.emi += 1
    $ multipersistent.emi = True
    $ multipersistent.save()
    if not automode:
        call credits
    jump restart

label hanakoend:
    $ wdt_off()
    scene white
    with Dissolve(4.0)
    $ persistent.hanako += 1
    $ multipersistent.hanako = True
    $ multipersistent.save()
    if not automode:
        call credits
    jump restart

label lillyend:
    $ wdt_off()
    scene white
    with Dissolve(4.0)
    $ persistent.lilly += 1
    $ multipersistent.lilly = True
    $ multipersistent.save()
    if not automode:
        call credits
    jump restart

label rinend:
    $ wdt_off()
    scene white
    with Dissolve(4.0)
    $ persistent.rin += 1
    $ multipersistent.rin = True
    $ multipersistent.save()
    if not automode:
        call credits
    jump restart

label shizuneend:
    $ wdt_off()
    scene white
    with Dissolve(4.0)
    $ persistent.shizune += 1
    $ multipersistent.shizune = True
    $ multipersistent.save()
    if not automode:
        call credits
    jump restart

label badend:
    $ wdt_off()
    scene bloodred
    with Dissolve(4.0)
    $ persistent.bad += 1
    $ multipersistent.bad = True
    $ multipersistent.save()
    if not automode:
        call credits(True)
    call iscene("A45")
    jump restart

################


label restart:
    if automode:
        $ init_vars()
        jump imachine
    elif notextmode:
        jump cruise_control
    else:
        $ renpy.full_restart()
