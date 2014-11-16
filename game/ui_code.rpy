# ui_code.rpy: contains init code for the ui (duh)
# And by "ui" I mean pretty much anything.

init -1 python:

    # Alright, let's break everything with this code insert
    def is_glrenpy():
        if (int(renpy.version().split('.')[1])) > (10):
            return True
        else:
            return False
            
    class SoundTransitionClassCompat(renpy.display.transition.Transition):
        __doc__ = '\n        A transition that does nothing but play a sound.\n        To be used in MultipleTransitions, obviously.\n        '
        def __init__(self, sound, time=0.0001, channel='sound', old_widget=None, new_widget=None, **properties):
            super(SoundTransitionClassCompat, self).__init__(time, **properties)
            self.time = time
            self.old_widget = old_widget
            self.new_widget = new_widget
            self.events = False
            self.sound = sound
            self.channel = channel
        def render(self, width, height, st, at):
            if (st) >= (self.time):
                self.events = True
                return render(self.new_widget, width, height, st, at)
            if (st) < (self.time):
                renpy.display.render.redraw(self, 0)
            renpy.sound.play(self.sound, channel=self.channel)
            return renpy.display.render.Render(width, height, opaque=True)
    def disp_size(disp):
        if isinstance(disp, str):
            disp = im.Image(disp)
        return disp.load().get_size()
    def quasiblur(disp_in, factor, bilinear_out=True, bilinear_in=True):
        disp_down = im.FactorScale(disp_in, width=(1.0) / (factor), bilinear=bilinear_in)
        if bilinear_out:
            (in_w, in_h) = disp_size(disp_in)
            disp_up = im.Scale(disp_down, width=int((in_w) + (factor)), height=int((in_h) + (factor)), bilinear=True)
            disp_up = im.Crop(disp_up, 0, 0, in_w, in_h)
        else:
            disp_up = im.FactorScale(disp_down, width=factor, bilinear=False)
        return disp_up
    class SoundTransitionClassGL(renpy.display.transition.Transition):
        __doc__ = '\n        A transition that does nothing but play a sound.\n        To be used in MultipleTransitions, obviously.\n        '
        def __init__(self, sound, delay=0.0001, channel='sound', old_widget=None, new_widget=None, **properties):
            super(SoundTransitionClassGL, self).__init__(delay, **properties)
            self.old_widget = old_widget
            self.new_widget = new_widget
            self.events = True
            self.sound = sound
            self.channel = channel
            self.played = False
        def render(self, width, height, st, at):
            if not (self.played):
                renpy.sound.play(self.sound, channel=self.channel)
                self.played = True
            return renpy.display.transition.null_render(self, width, height, st, at)
    if is_glrenpy():
        SoundTransition = renpy.curry(SoundTransitionClassGL)
    else:
        SoundTransition = renpy.curry(SoundTransitionClassCompat)
    def transition_attach_sound(tr_in, sound):
        return MultipleTransition([False, SoundTransition(sound), False, tr_in, True])
        
    # And, we're done

    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            if self.show_function == quotefixer:
                what = change_quotes(what)
            store_say(who, what)
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            return

    def menu_init():
        store.playthroughflag = False
        store.ask_to_quit = False
        config.has_autosave=True
        switch_language(persistent.current_language)
        store.last_visited_label = None
        renpy.music.play(music_menus, fadein=5.0, fadeout=0.5, if_changed=True)
        config.skipping = None
        _preferences.afm_time = 0

    def test_sound():
        sounds = [sfx_slide, sfx_slide2, sfx_draw]
        this_sound = renpy.random.choice(sounds)
        renpy.music.play(this_sound, channel="sound")


    def acdc_warp_simple(x):
        n = 10.0        
        masterscale = n/(n-1)

        if (x < (1.0/n)):
            xmod = x*(n/2.0)
            res = (((2.0/n) * _ease_time_warp(xmod)) / 2.0) * masterscale

        elif (x > (1.0 - (1.0/n))):
            xmod = 1.0-(((x-1)*n)/2.0)
            res = (((2.0/n) * _ease_time_warp(xmod) / 2.0) + (1 - (2.0/n))) * masterscale

        else:
            res = (x - (0.5/n)) * masterscale
        
        return res

    def acdc_warp(x):
        import math
        n = 10.0 # number of sections        
        if (x < (1.0 / n)):
            res = (((2.0 / n) * (0.5 - math.cos(math.pi * (x * (n / 2.0))) / 2.0)) / 2.0) * (n / (n - 1.0))
        elif (x > (1.0 - (1.0 / n))):
            res = (((2.0 / n) * (0.5 - math.cos(math.pi * (1.0 - (((x - 1.0) * n) / 2.0))) / 2.0) / 2.0) + (1.0 - (2.0 / n))) * (n / (n - 1.0))
        else:
            res = (x - (0.5 / n)) * (n / (n - 1.0))
        return res     

    def fallthrough_catcher(label, not_ft):
        global available_languages
        is_script = False
        for rawprefix in available_languages:
            prefix = rawprefix + "_"
            if label.startswith(prefix):
               is_script = True
        if is_script and not not_ft:
            renpy.jump("simple_return")


    config.label_callback = fallthrough_catcher

    # Draw helper
    #renpy.image("dot","dot.png")
    #renpy.image("dot2",im.MatrixColor("dot.png",im.matrix.hue(120)))
    #renpy.image("dot3",im.MatrixColor("dot.png",im.matrix.hue(240)))

    def draw_graph():
        n = 300.0
        for i in xrange(n):
            x = (i / n)
            xd = x * 0.75 + 0.125
            
            #y = 1.0 - _ease_time_warp(x)
            #renpy.show("dot2", tag="test1"+str(i), at_list=[Position(xpos=xd, ypos=y)])
            
            y = 1.0 - acdc_warp(x)
            renpy.show("dot", tag="test"+str(i), at_list=[Position(xpos=xd, ypos=y)])


    renpy.music.register_channel("ambient", "sfx", True)
    renpy.music.register_channel("auxambient", "sfx", True)

init 2 python:


#    def menu(items, **add_input): #overwriting standard menu handler
#        newitems = []
#        for label, val in items:
#            if val == None:
#                narrator(label, interact=False)
#            else:
#                newitems.append((label, val))
#        rv = renpy.display_menu(newitems, **add_input)
#        for label, val in items:
#            if rv == val:
#                store_say(None, ">> " + label)
#        return rv

    ## benchmark/dev stuff that would only clutter up ui_settings but has to be present
    # in any case for the game to run properly
    if not persistent.emi:
        persistent.emi = 0
    if not persistent.hanako:
        persistent.hanako = 0
    if not persistent.lilly:
        persistent.lilly = 0
    if not persistent.shizune:
        persistent.shizune = 0
    if not persistent.rin:
        persistent.rin = 0
    if not persistent.bad:
        persistent.bad = 0

    automode = False
    notextmode = False
    config.auto_choice_delay = None
    nongamemenus = 0 # lint hack

    def autosave_metabuilder():
        if save_name:
            full_save_name = save_name + "#" + str(renpy.get_game_runtime())
        else:
            full_save_name = "#" + str(renpy.get_game_runtime())
        return full_save_name

    config.auto_save_extra_info = autosave_metabuilder

    ## readback
    max_readback_buffer_length = 256
    readback_buffer = []
    def store_say(who, what):
        global readback_buffer
        if not who:
            who = ""
        if not what:
            what = ""
        if not who.strip() and not (what.strip() and preparse_say_for_store(what)):
            return
        newline = (preparse_say_for_store(who),preparse_say_for_store(what))
        readback_buffer.append(newline)
        readback_prune()

    current_line = None
    def store_current_line(who, what):
        global current_line
        current_line = (preparse_say_for_store(who), preparse_say_for_store(what))

    import re
    remove_tags_expr = re.compile(r'{nw}|{image=.*?}|{/image}|{color=.*?}|{/color}|{a=.*?}|{/a}|{font=.*?}|{/font}|{size=.*?}|{/size}') # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > max_readback_buffer_length:
            del readback_buffer[0]

    def readback_catcher():
        ui.add(renpy.Keymap(rollback=ui.callsinnewcontext("text_history")))
        ui.add(renpy.Keymap(rollforward=ui.returns(None)))

    if not config.rollback_enabled:
        config.overlay_functions.append(readback_catcher)

    def turn_afm_on():
        if may_afm:
            _preferences.afm_time = persistent.afm_time

    def afm_ovl():
        ui.keymap(a=turn_afm_on)

    config.overlay_functions.append(afm_ovl)

    # viewport functions for readback:
    def increase_rb_yoffset():
        # scroll down
        store_rb_yoffset(yadj.get_value() + 50)

    def decrease_rb_yoffset():
        # scroll up
        store_rb_yoffset(yadj.get_value() - 50)

    def store_rb_yoffset(input):
        # actually move the viewport & save for posterity
        yadj.change(input)

    def wdt_on(do_with=True):
        global _window
        _window = True
        if do_with:
            renpy.with_statement(None)

    def wdt_off(do_with=True):
        global _window
        _window = False
        if do_with:
            renpy.with_statement(None)

    ## TL note display
    tl_note=None
    tl_note_id=None

    def add_note(id, text, author=""):
        store.tl_notes[id] = (author, text)

    def display_tl_note(new_tl_note_id=None):
        # hyperlink callback for showing commentary
        global tl_note, tl_note_id, tl_notes
        if new_tl_note_id != tl_note_id:
            tl_note_id = new_tl_note_id
            if tl_note_id==None:
                tl_note=None
            elif tl_note_id in tl_notes:
                 tl_note=tl_notes[tl_note_id]
            renpy.restart_interaction()

    def tl_note_overlay():
        # actually show commentary
        global tl_note
        if tl_note and not config.skipping and _preferences.afm_time <= 0:
            ui.frame(style="comment_frame")
            ui.vbox()
            if tl_note[0]:
                ui.text(tl_note[0], style="comment_label")
            ui.text(tl_note[1], style="comment_text")
            ui.close()
        else:
            tl_note=None

    config.overlay_functions.append(tl_note_overlay)

    def tl_dismiss(a):
        # hyperlink click callback stub
        display_tl_note()
        return True

    import re
    rh_expr = re.compile(r'{a=.*?}|{/a}')
    def remove_hyperlinks(input):
        # optionally suppress hyperlinks
        global rh_expr
        if not persistent.commentary_on:
            return re.sub(rh_expr, "", input)
        else:
            return input

    # register commentary framework
    config.hyperlink_callback = tl_dismiss
    config.hyperlink_focus = display_tl_note
    config.say_menu_text_filter = remove_hyperlinks

    ## custom defs

    def viewportkeys(upfunc, downfunc):
        # a set of common keymap changes when dealing with viewports
        ui.add(renpy.Keymap(mousedown_4=upfunc))
        ui.add(renpy.Keymap(K_PAGEUP=upfunc))
        ui.add(renpy.Keymap(mousedown_5=downfunc))
        ui.add(renpy.Keymap(K_PAGEDOWN=downfunc))

    def make_percentage(part, total, precision=0):
        if precision == 0:
            if total > 0:
                return int(round((float(part) / float(total)) * 100.0))
            else:
                return 0
        else:
            if total > 0:
                return round((float(part) / float(total)) * 100.0, precision)
            else:
                return 0.0
    
    #This function gets the currently playing track name, if there is one. -md01          
    def get_music_name():
        for (name, file) in ex_m_tracks:
            if (file) == (renpy.music.get_playing()):
                return name

    def get_completion_percentage():
        seen = len(get_available_scenes())
        total = len(get_available_scenes(include_locked=True, exclude_hidden=True))
        return make_percentage(seen, total, 0)

    def get_available_scenes(filter=False, include_locked=False, exclude_hidden=False):
        # what scenes to show in the replay menu?
        available_scenes = []
        for (name, label, display, path) in s_scenes:
            if renpy.has_label(label): # if it doesn't exist, don't even bother
                if not filter or filter == path or (isinstance(path, tuple) and filter in path): # path filter in effect?
                    unlocked = False
                    if (persistent_seen(label) or has_devlvl()) and not exclude_hidden:
                        unlocked = True
                    if (include_locked and display) or unlocked:
                        available_scenes.append((name, label, display, path, unlocked))
        if len(available_scenes) > 0:
            return available_scenes
        else:
            return False

    def get_available_images():
        # what images to show in the gallery?
        global ex_g_images
        available_images = []
        for thumb in ex_g_images:
            if isinstance(thumb, tuple):
                for image in thumb:
                    if tuple(image.split()) in persistent._seen_images or has_devlvl():
                        available_images.append(image)
            else:
                if tuple(thumb.split()) in persistent._seen_images or has_devlvl():
                    available_images.append(thumb)
        if len(available_images) > 0:
            return available_images
        else:
            return False

    def get_available_music():
        # what music to show in the jukebox?
        global ex_m_tracks
        available_music = []
        for title, filename in ex_m_tracks:
            if renpy.seen_audio(filename) or has_devlvl():
                available_music.append(filename)
        if len(available_music) > 1: # the menu music is a given
            return available_music
        else:
            return False

    ## OMG HAX
    def has_devlvl():
        global devlvl
        if devlvl > 4:
            return True
        return False
    def devlvl_I():
        global devlvl
        if devlvl==0:
            devlvl=1
        else:
            devlvl=0
    def devlvl_D():
        global devlvl
        if devlvl in (1,2):
            devlvl+=1
        else:
            devlvl=0
    def devlvl_Q():
        global devlvl
        if devlvl==3:
            devlvl=4
        else:
            devlvl=0
    def devlvl_N():
        global devlvl
        if devlvl==4:
            renpy.sound.play(sfx_heartfast)
            devlvl=5
        else:
            devlvl=0


    def widget_button(text,displayable,clicked=None,style='prefs_label',xsize=220,ysize=30,widgetyoffset=3,textxoffset=30,state="button", xpos=0, ypos=0):
        # Our half-graphical BUTAN
        textbase = Text(text, style=style)
        texthover = Text(text, style=style, color="#000")
        textdisabled = Text(text, style=style, color="#00000019")
        thisbutton_hover = LiveComposite((xsize, ysize), 
                                         (0, widgetyoffset), displayable,
                                         (textxoffset, 0), texthover)
        if xpos or ypos:
            ui.fixed(xpos=xpos, ypos=ypos)
        if state == "disabled":
            thisbutton_disabled = LiveComposite((xsize, ysize), 
                                                (0, widgetyoffset), ib_disabled(displayable),
                                                (textxoffset, 0), textdisabled)
            ui.image(thisbutton_disabled)
        elif state == "active":
            ui.imagebutton(thisbutton_hover,thisbutton_hover,clicked=None)
        else:
            thisbutton = LiveComposite((xsize, ysize), 
                                       (0, widgetyoffset), ib_base(displayable),
                                       (textxoffset, 0), textbase)
            ui.imagebutton(thisbutton, thisbutton_hover, clicked=clicked)
        if xpos or ypos:
            ui.close()

    def return_button(wherefunc, text=None, xpos=540, ypos=450):
        if text == None:
            text = displayStrings.return_button_text
        # return button, matched to bg-config.png
        ui.add(renpy.Keymap(game_menu=wherefunc))
        widget_button(text, "ui/bt-return.png", wherefunc, xsize=100, xpos=xpos, ypos=ypos)


    def time_from_seconds(seconds):
        # make a nice time string from raw int seconds
        mins, secs = divmod(int(float(seconds)), 60)
        hours, minutes = divmod(mins, 60)
        playhours = str(hours)
        if len(str(minutes)) == 1:
            playminutes = "0" + str(minutes)
        else:
            playminutes = str(minutes)
        return playhours+":"+playminutes

    def custom_render_savefile(index, name, filename, extra_info, screenshot, mtime, newest, clickable, has_delete, **positions):
        # custom save slot renderer
        if clickable:
            clicked = ui.returns((filename, True))
        else:
            clicked = None

        info_split = extra_info.split("#")
        scene_name = name_from_label(info_split[0])
        if len(info_split) > 1:
            playtime = time_from_seconds(info_split[1])
        else:
            playtime = "x:xx"

        if is_autosave(name):
        #    name = "A" + name[5:]
            name = name[5:]

        ui.vbox()
        ui.hbox()
        ui.button(style=style.file_picker_entry[index],
                  clicked=clicked,
                  **positions)
        ui.hbox(style=style.file_picker_entry_box[index])
        ui.add(screenshot)

        if newest:
            ui.text(" " + name + ". ", style=style.file_picker_new[index])
        else:
            ui.text(" " + name + ". ", style=style.file_picker_old[index])

        s = config.file_entry_format % dict(
            time=renpy.time.strftime(config.time_format,
                                     renpy.time.localtime(mtime)),
            save_name=scene_name, playtime=playtime)
        ui.text(s, style=style.file_picker_extra_info[index])
        ui.close()
        ui.vbox()
        ui.null(height=6)
        if has_delete:
            ui.imagebutton(ib_base("ui/bt-del.png"), "ui/bt-del.png", clicked=ui.returns(("delete", filename)))
        ui.close()
        ui.close()
        ui.null(height=3)
        ui.close()

    def is_autosave(fn):
        if fn.startswith("auto-"):
            return True
        return False

    def custom_file_picker(selected, save, mode="manual", background = None):
        # custom file picker
        global auto_offset, displayed_slots
        saved_games = renpy.list_saved_games(regexp=r'(auto-|quick-)?[0-9]+')
        newest = None
        newest_mtime = None
        newest_auto = None
        newest_automtime = None
        save_info = { }
        positions = { }
        for fn, extra_info, screenshot, mtime in saved_games:
            save_info[fn] = (extra_info, screenshot, mtime)
            if mtime > newest_mtime:
                newest = fn
                newest_mtime = mtime
            elif is_autosave(fn) and mtime > newest_automtime:
                newest_auto = fn
                newest_automtime = mtime

        def save_slot_sort(in_1, in_2):
            if len(in_1[0]) > len(in_2[0]):
                return 1
            elif len(in_1[0]) < len(in_2[0]):
                return -1
            if in_1[0] > in_2[0]:
                return 1
            elif in_1[0] < in_2[0]:
                return -1
            else:
                return 0

        # main loop, will only be exited once a file is chosen or an outside command comes in
        while True:

            displayed_manual = []
            displayed_auto = []

            for fn, extra_info, screenshot, mtime in saved_games:
                if not is_autosave(fn):
                    displayed_manual.append((fn, fn, False))
                else:
                    displayed_auto.append((fn, fn, True))

            if len(displayed_manual) < 1 and len(displayed_auto) > 0:
                mode = "auto"

            if mode == "auto" and not selected == "save":
                displayed_slots = displayed_auto
                newest = newest_auto
                has_delete = False
            else:
                displayed_slots = displayed_manual
                has_delete = True
            
            displayed_slots.sort(cmp=save_slot_sort)
            
            scrollable = False
            if len(displayed_slots) > 5:
                scrollable = True

            if scrollable:
                auto_offset = 1.0 / (len(displayed_slots) - 5)
                # emergency absolute value override
                auto_offset = 59
            else:
                auto_offset = 0

            if background:
                ui.image(background)
            layout.navigation(None)

            ui.window(style='file_picker_frame', xminimum=470)
            #ui.vbox(style='file_picker_frame_vbox') # whole thing.
            ui.vbox() # whole thing.

            if selected == "save":
                ui.text(displayStrings.save_page_caption, style="page_caption")
            else:
                ui.text(displayStrings.load_page_caption, style="page_caption")

            def entry(name, filename, offset, ro):
                place = positions.get("entry_" + str(offset + 1), { })

                if filename not in save_info:
                    clickable = save and not ro
                    _render_new_slot(offset, name, filename, clickable, **place)
                else:
                    clickable = not save or not ro
                    extra_info, screenshot, mtime = save_info[filename]
                    custom_render_savefile(offset, name, filename, extra_info, screenshot, mtime, newest == filename, clickable, has_delete, **place)

            def store_yoffset(input=persistent.fpicker_yoffset):
                global auto_offset, displayed_slots
                maxheight = auto_offset * (len(displayed_slots) - 5)
                if input > maxheight:
                    input = maxheight
                elif input < 0:
                    input = 0
                persistent.fpicker_yoffset = input
                yadj.change(input)

            def increase_yoffset():
                global auto_offset
                store_yoffset(persistent.fpicker_yoffset + auto_offset)

            def decrease_yoffset():
                global auto_offset
                store_yoffset(persistent.fpicker_yoffset - auto_offset)

            if not persistent.fpicker_yoffset:
                persistent.fpicker_yoffset = 0.0
            elif persistent.fpicker_yoffset > auto_offset * (len(displayed_slots) - 5) or persistent.fpicker_yoffset == -1:
                persistent.fpicker_yoffset = auto_offset * (len(displayed_slots) - 5)

            yadj = ui.adjustment(range=auto_offset * (len(displayed_slots) - 5), value=persistent.fpicker_yoffset, changed=store_yoffset)
            vp = ui.viewport(yadjustment=yadj, mousewheel=False, draggable=False, xmaximum=400, ymaximum = 296, xpos=0, ypos = 2)
            ui.vbox(xfill=True)

            maxname = 0
            
            for i, (filename, name, ro) in enumerate(displayed_slots):
                entry(name, filename, i, ro)
                maxname = name

            ui.close() # slots
            ui.close() # whole thing

            ui.vbox(xpos = 600, yalign=0.493, box_spacing=2)
            if scrollable:
                ui.imagebutton(ib_base("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=decrease_yoffset)
                ui.bar(style='vscrollbar', changed=store_yoffset, adjustment=yadj)
                ui.imagebutton(ib_base("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=increase_yoffset)
            else:
                ui.imagebutton(ib_disabled("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=None)
                ui.bar(style='vscrollbar_disabled')
                ui.imagebutton(ib_disabled("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=None)
            ui.close()
            if selected == "save":
                nextsaveslot=1
                #while True:
                #    if renpy.scan_saved_game(str(nextsaveslot)):
                #        nextsaveslot += 1
                #    else:
                #        break
                
                nextsaveslot = int(maxname) + 1
                widget_button(displayStrings.new_save_button, "ui/bt-star.png", ui.returns((str(nextsaveslot),False)), xsize=340, widgetyoffset=0, xpos=180, ypos=450)
            elif config.has_autosave:
                style_auto_b = "mm"
                clicked_auto_b = ui.returns(("_setmode", "auto"))
                if len(displayed_auto) < 1:
                    clicked_auto_b = None
                style_manual_b = "mm"
                clicked_manual_b = ui.returns(("_setmode", "manual"))
                if len(displayed_manual) < 1:
                    clicked_manual_b = None

                if mode == "auto":
                    style_auto_b = "rpa_active"
                    clicked_auto_b = None
                else:
                    style_manual_b = "rpa_active"
                    clicked_manual_b = None

                ui.hbox(xpos=180, ypos=450)
                layout.button(displayStrings.show_manual_saves, style_manual_b, clicked=clicked_manual_b)
                layout.button(displayStrings.show_auto_saves, style_auto_b, clicked=clicked_auto_b)
                ui.close()
                
            return_button(ui.returns(("return","return")))

            viewportkeys(decrease_yoffset,increase_yoffset)

            value = ui.interact()
            return value

    # We use the overlay for auto and skip mode.
    def automode_f():
        # If clicked, stop auto mode and refresh the overlay. 
        def clicked():
            _preferences.afm_time = 0
            config.skipping = None # cancel too or two clicks are needed
            renpy.restart_interaction() # redraw

        # If auto mode isn't on, do nothing.
        if _preferences.afm_time == 0:
            return
        else:
            # tell the user auto mode is on
            ui.image("ui/sd-auto.png", xanchor=1.0, xpos=790, ypos=10)
            # trap clicks and related
            if renpy.current_interact_type() != "menu":
                ui.add(renpy.Keymap(dismiss=clicked))
                ui.add(renpy.Keymap(rollforward=clicked))
                ui.add(renpy.Keymap(rollback=clicked))

    def custom_skip_indicator(): # Can't just overwrite because the original is hidden...
        if config.skipping == "slow" and config.allow_skipping:
            if _preferences.afm_time == 0:
                thisxpos = 790
            else:
                thisxpos = 769
            ui.image("ui/sd-skip.png", xanchor=1.0, xpos=thisxpos, ypos=10)

    # register the above
    config.overlay_functions.append(automode_f)
    config.overlay_functions.append(custom_skip_indicator)

    def _prompt(screen, message, image=None, isyesno = False, background=None, transition=config.intra_transition, interact = True):
    # more general method to draw a dialogue
        renpy.transition(transition)
        layout.navigation(screen)
        if background:
            ui.image(background)
        ui.image(style.gm_root.background)
        ui.window(style='yesno_frame')
        ui.vbox(style='yesno_frame_vbox')
        layout.prompt(message, "yesno")
        ui.hbox(style='yesno_button_hbox')
        if isyesno:
            layout.button(displayStrings.yesno_yes, 'yesno', clicked=ui.returns(True))
            layout.button(displayStrings.yesno_no, 'yesno', clicked=ui.returns(False))
            ui.add(renpy.Keymap(game_menu=ui.returns(False)))
        elif interact:
            ui.saybehavior()
            layout.button(displayStrings.yesno_okay, 'yesno', clicked=ui.returns(True))
            ui.add(renpy.Keymap(game_menu=ui.returns(True)))
        ui.close()
        ui.close()
        if image:
            ui.image(image)
        if interact:
            rv =  ui.interact()
        else:
            rv = False
        renpy.transition(config.intra_transition)
        return rv

    def _yesno_prompt(screen, message, image=None, background=None, transition=config.intra_transition):
    # draws a standard _yesno_prompt with an image added. image is a displayable to draw on top of everything. Just keeping this around for compatibility.
        return _prompt(screen, message, image=image, isyesno = True, background=background, transition=transition)

    class TogglePreference(object):
        """
        This is a class that's used to represent a 2-choice preference.
        We'll completely rewrite the presentation function (so this is not a general Ren'Py module, sorry tom) and reinit the classes.
        For the original documentation, see the class _Preference in 00preferences.rpy
        """
        def __init__(self, name, field, boolmap=(False,True), base=_preferences):
            # boolmap maps properties that actually have more values internally to "False" and "True"

            self.name = name
            self.field = field
            self.values = []
            self.boolmap = boolmap
            self.base = base

            config.all_preferences[name] = self

        def render_preference(self, thisxpos=0, thisypos=0):
            cur = getattr(self.base, self.field)

            if cur == self.boolmap[0]:
                boolCur = False
                checkboximage = "ui/bt-cf-unchecked.png"
            elif cur == self.boolmap[1]:
                boolCur = True
                checkboximage = "ui/bt-cf-checked.png"
            else:
                boolCur = cur
                checkboximage = "ui/bt-cf-unchecked.png"

            def clicked(value=boolCur):
                if value == True:
                    writevalue = self.boolmap[0]
                elif value == False:
                    writevalue = self.boolmap[1]
                else:
                    writevalue = value # just making safe we don't mess up TOO much

                setattr(self.base, self.field, writevalue)
                return True

            widget_button(self.name, checkboximage, clicked, xsize=325, widgetyoffset=0)

    class customSliderPreference(object):
        # customized slider prefs module (text speed etc.)
        def __init__(self, name, range, get, set, enable='True'):

            self.name = name
            self.range = range
            self.get = get
            self.set = set
            self.enable = enable

            config.all_preferences[name] = self

        def render_preference(self, thisxpos=0, thisypos=0):

            if not eval(self.enable):
                return

            def changed(v):
                self.set(v)

            ui.hbox()
            ui.bar(self.range,
                   self.get(),
                   changed=changed,
                   style=style.prefs_slider[self.name])
            ui.null(width=15)
            layout.label(self.name, "prefs")
            ui.close()


    class customVolumePreference(object):
        # customized slider prefs module (volume etc.)
        def __init__(self, name, mixer, enable='True', sound='None', channel=0):

            self.name = name
            self.mixer = mixer
            self.enable = enable
            self.sound = sound
            self.channel = channel

            config.all_preferences[name] = self

        def render_preference(self, thisxpos=0, thisypos=0):

            if not eval(self.enable):
                return

            def changed(v):
                _preferences.set_volume(self.mixer, self.fader_characteristic(v))

            ui.hbox()
            ui.bar(128,
                   self.get_slider_position(),
                   changed=changed,
                   style=style.prefs_volume_slider[self.name])
            ui.null(width=15)
            layout.label(self.name, "prefs")
            ui.close()

        def fader_characteristic(self, v):
            return _ease_out_time_warp(v / 128.0)
        
        def get_slider_position(self):
            return int(_ease_in_time_warp(_preferences.get_volume(self.mixer)) * 128)

    def cps_get():
        # make the text display speed settings sane
        cps = _preferences.text_cps
        if cps == 0:
            cps = 150
        else:
            cps -= 1
        return cps

    def cps_set(cps):
        # set the text display speed
        cps += 1
        if cps == 151:
            cps = 0
        _preferences.text_cps = cps

    def afm_get():
        # hacked version of the reader for autoread
        # afm = _preferences.afm_time
        afm = persistent.afm_time
        afm -= 1
        if afm < 1:
            afm = 1
        return afm

    def afm_set(afm):
        # hacked version of the setter for autoread
        afm += 1
        if afm > 40:
            afm = 40
        if _preferences.afm_time > 0:
            _preferences.afm_time = afm
        persistent.afm_time = afm


    # Now we initialize the new classes.
    def initialize_prefs():
        global fullscreen_p, transition_p, unreadskip_p, choiceskip_p, textspeed_p, afm_p, musicvol_p, musicvol_p_jukebox, sfxvol_p
        fullscreen_p = TogglePreference(displayStrings.config_fullscreen_label, 'fullscreen')
        transition_p = TogglePreference(displayStrings.config_transitions_label, 'transitions', (2,0)) # "1" would actually be a mythical "some" state we don't use
        unreadskip_p = TogglePreference(displayStrings.config_skip_unseen_label, 'skip_unseen')
        choiceskip_p = TogglePreference(displayStrings.config_skip_after_choice_label, 'skip_after_choices')
        textspeed_p = customSliderPreference(displayStrings.config_textspeed_label, 150, cps_get, cps_set)
        afm_p = customSliderPreference(displayStrings.config_afmspeed_label, 40, afm_get, afm_set)
        musicvol_p = customVolumePreference(displayStrings.config_musicvol_label, 'music')
        musicvol_p_jukebox = customVolumePreference(displayStrings.config_musicvol_jukebox_label, 'music')
        sfxvol_p = customVolumePreference(displayStrings.config_sfxvol_label, 'sfx')


# New CG Gallery Code
#
# Release 2 (2007-03-31)
# http://www.renpy.org/wiki/renpy/doc/cookbook/New_CG_Gallery
#
# copypasting this here because we want to rewrite some stuff and keep everything in one file.
# It's not well-documented code, but see the link above.

    style.create('gallery_nav_vbox', 'vbox')
    style.create('gallery_nav_button', 'mm_button')
    style.create('gallery_nav_button_text', 'mm_button_text')

    class GalleryGridLayout(object):
        def __init__(self, gridsize, upperleft, offsets):
            self.gridsize = gridsize
            self.upperleft = upperleft
            self.offsets = offsets

        def __call__(self, imagenum, image_count):

            cols, rows = self.gridsize
            ulx, uly = self.upperleft
            ox, oy = self.offsets

            return dict(
                xpos = ulx + (imagenum % cols) * ox,
                ypos = uly + (imagenum // cols) * oy,
                )

    class GalleryAllPriorCondition(object):

        def check(self, all_prior):
            return all_prior

    class GalleryArbitraryCondition(object):
        def __init__(self, condition):
            self.condition = condition

        def check(self, all_prior):
            return eval(self.condition)

    class GalleryUnlockCondition(object):
        def __init__(self, images):
            self.images = images

        def check(self, all_prior):
            for i in self.images:
                if tuple(i.split()) not in persistent._seen_images:
                    return False

            return True


    class GalleryImage(object):
        def __init__(self, gallery, images, displayable):
            self.gallery = gallery
            self.images = images or [ ]
            self.displayable = displayable
            self.conditions = [ ]

        def check_unlock(self, all_prior):
            for i in self.conditions:
                if not i.check(all_prior):
                    return False

            return True

        def show_locked(self, image_num, image_count):
            renpy.transition(self.gallery.transition)
            self.gallery.locked_image(image_num, image_count)
            ui.saybehavior()
            ui.interact()

        def show(self, image_num, image_count):
            renpy.transition(self.gallery.transition)

            renpy.scene()

            for i in self.images:
                renpy.show(i)

            if self.displayable:
                ui.add(self.displayable)

            ui.saybehavior()
            ui.interact()

    class GalleryButton(object):
        def __init__(self, gallery, idle, hover, insensitive, properties):
            self.gallery = gallery
            self.idle = idle
            self.hover = hover
            self.insensitive = insensitive
            self.properties = properties
            self.images  = [ ]
            self.conditions = [ ]

        def check_unlock(self):
            for i in self.conditions:
                if not i.check(True):
                    return False

            for i in self.images:
                if i.check_unlock(False):
                    return True

            return False

        def render(self, i, pos):
            props = pos.copy()
            props.update(self.properties)

            if not self.check_unlock():
                insensitive = self.insensitive or self.gallery.locked_button
                if insensitive is not None:
                    ui.fixed(**props)
                    ui.image(insensitive)
                    ui.close()
                    return

            if self.hover:
                ui.imagebutton(self.idle,
                               self.hover,
                               clicked=ui.returns(("button", i)),
                               **props)

            else:
                ui.fixed(**props)
                ui.image(self.idle)
                ui.imagebutton(self.gallery.idle_border,
                               self.gallery.hover_border,
                               clicked=ui.returns(("button", i)))
                ui.close()

        def show(self):

            all_prior = True

            # Sort function: Show unlocked images first
            im_sort = []
            im_locked = []
            im_locktext = ""
            for i, img in enumerate(self.images):
                if img.check_unlock(all_prior):
                    im_sort.append((i, img))
                else:
                    im_locked.append((i, img))
            im_sort.extend(im_locked)

            #for i, img in enumerate(self.images):
            for i, img in im_sort:
                ui.add(renpy.Keymap(game_menu=ui.returns(True)))
                if img.check_unlock(all_prior):
                    img.show(i, len(self.images))
                else:
                    if len(im_locked) == 1:
                        self.gallery.locked_images_screen(displayStrings.gallery_onelocked)
                    else:
                        self.gallery.locked_images_screen(_(displayStrings.gallery_manylocked) % (len(im_locked)))
                    return
                    #img.show_locked(i, len(self.images))
                    #all_prior = False


    class GalleryPage(object):

        def __init__(self, gallery, name, background):
            self.gallery = gallery
            self.name = name
            self.background = background
            self.buttons = [ ]


    class Gallery(object):

        transition = dissolve

        locked_button = None
        locked_background = "#000"

        hover_border = None
        idle_border = None

        background = None

        def __init__(self):
            self.pages = [ ]

            self.page_ = None
            self.button_ = None
            self.image_ = None
            self.unlockable = None

        def page(self, name, background=None):

            self.page_ = GalleryPage(self, name, background)
            self.pages.append(self.page_)

        def button(self, idle, hover=None, locked=None, **properties):
            self.button_ = GalleryButton(self, idle, hover, locked, properties)
            self.page_.buttons.append(self.button_)
            self.unlockable = self.button_

        def image(self, *images):
            self.image_ = GalleryImage(self, images, None)
            self.button_.images.append(self.image_)
            self.unlockable = self.image_

        def display(self, displayable):
            self.image_ = GalleryImage(self, [ ], displayable)
            self.button_.images.append(self.image_)
            self.unlockable = self.image_

        def unlock(self, *images):
            self.unlockable.conditions.append(GalleryUnlockCondition(images))

        def condition(self, condition):
            self.unlockable.conditions.append(GalleryArbitraryCondition(condition))

        def allprior(self):
            self.unlockable.conditions.append(GalleryAllPriorCondition())

        def unlock_image(self, *images):
            self.image(*images)
            self.unlock(*images)

        def navigation(self, page_name, page_num, pages, currentpage=0):

            ui.hbox(background=None,xpos=180,ypos=450)

            for i, p in enumerate(self.pages):
                layout.button(p.name,
                                "gallery_nav",
                                selected=(i == page_num),
                                clicked=ui.returns(("page", i)))
            ui.close()


        def grid_layout(self, gridsize, upperleft, offsets):
            self.layout = GalleryGridLayout(gridsize, upperleft, offsets)

        def layout(self, i, n):
            return { }

        def locked_image(self, num, total):
            ui.add(self.locked_background)
            ui.text(_(displayStrings.gallery_singlelocked) % (num + 1, total), xalign=0.5, yalign=0.7, style="prefs_label")

        def locked_images_screen(self, text):
            renpy.transition(self.transition)
            ui.add(self.locked_background)
            ui.text(text, xalign=0.5, ypos=400, style="prefs_label")
            ui.saybehavior()
            ui.interact()

        def show(self, page=0):

            while True:
                renpy.transition(self.transition)

                gallery_predict()

                p = self.pages[page]

                bg = p.background or self.background
                if bg is not None:
                    renpy.scene()
                    ui.add(bg)

                ui.text(displayStrings.gallery_page_caption, style="page_caption", xpos=180,ypos=120)
                if len(self.pages) > 1:
                    self.navigation(p.name, page, len(self.pages),page)

                for i, b in enumerate(p.buttons):
                    pos = self.layout(i, len(p.buttons))
                    b.render(i, pos)

                return_button(_intra_jumps("extra_menu", "intra_transition"))

                cmd, arg = ui.interact(suppress_overlay=True, suppress_underlay=True)

                if cmd == "return":
                    return

                elif cmd == "page":
                    page = arg
                    continue

                elif cmd == "button":
                    p.buttons[arg].show()
                    continue

        # custom gallery extensions
        def autobutton(self, in_images):
            # make a thumbnail button from just the image to display
            if in_images == "":
                return
            if isinstance(in_images, tuple):
                thumb_base = im.Image("ui/bg-ex-gallery-lockedimage.png") # This should never be shown, but we need a valid button
                for image in in_images:
                    if tuple(image.split()) in persistent._seen_images or has_devlvl():
                        thumb_base = image
                        break
            else:
                thumb_base = in_images
                in_images = (in_images,)
            thumbnail = im.Scale(ImageReference(thumb_base), 100, 75)
            button_base = LiveComposite((110, 85),
                                        (0, 0), ib_base("ui/bt-cg-locked.png"),
                                        (5, 5), im.MatrixColor(thumbnail, im.matrix.desaturate()))
            button_hover = LiveComposite((110, 85),
                                         (0, 0), "ui/bt-cg-locked.png",
                                         (5, 5), thumbnail)
            self.button(button_base, button_hover)
            for in_image in in_images:
                if has_devlvl():
                    self.image(in_image)
                else:
                    self.unlock_image(in_image)

    def gallery_predict():
        # aggressively cache all images for the gallery
        global ex_g_images
        for img in ex_g_images:
            if isinstance(img, tuple):
                for subimg in img:
                    renpy.predict(ImageReference(subimg))
            else:
                renpy.predict(ImageReference(img))

    # END GALLERY CODE

    def datedisplay(date):
        renpy.transition(fade)
        ui.image(Solid("000"))
        ui.text(date, xalign=0.5, yalign=0.5)
        ui.pausebehavior(5.0)
        ui.interact(suppress_overlay=True, suppress_underlay=True)
        renpy.transition(fade)

    def tcard(act_number, act_char):
        # title card constructor. construction data is in ui_settings.
        global act_names, playthroughflag, notextmode, _window
        id = (act_number, act_char)
        if notextmode or not playthroughflag:
            return
        wdt_off(False)
        renpy.transition(Dissolve(3.0), always=True)
        label = LiveComposite((480,123),
                              (115,20), Window(Text(" "+displayStrings.act_term+" " + str(act_number) + ":\n" + act_names[id][0], color="#716b5e"), left_padding=60, right_padding=30, ypadding=14, xfill=False, yminimum=86, background=Frame("ui/bg-acttitleframe.png", 16, 8)),
                              (0,0), "ui/bt-logoonly.png")
        fullcard = LiveComposite((800,600),
                                 (0,0), "ui/tc-" + act_names[id][1] + ".png",
                                 (act_names[id][2], act_names[id][3]), label)
        renpy.scene()
        renpy.show("bg tcard", what=anim.TransitionAnimation(Solid("#FFF"), 4.0, Dissolve(1.0),
                                          "ui/tc-neutral.png", 1.0, ImageDissolve("ui/tr-tcard-" + act_names[id][1] + ".png", 3.0),
                                          "ui/tc-" + act_names[id][1] + ".png", 4.0, wiperight,
                                          fullcard, 6.0, Dissolve(3.0),
                                          Solid("#FFF")))
        ui.timer(4.5, renpy.music.play, kwargs={"filenames":sfx_tcard, "loop":False})
        ui.pausebehavior(19.0, True)
        ui.interact(suppress_overlay=True, suppress_underlay=True)
        wdt_on()

    # Fireworks
    def fw_constructor(image, sparkle=True, normalprob = 1):
        sparklebase = anim.Blink(image, high=1.0, low=10.0, on=0.2, off=0.0, set=3.0)
        sparkleprob = 1
        if not sparkle:
            sparklestate = image
            onstate = image
        elif str(sparkle) == "True":
            sparklestate = sparklebase
            onstate = sparklebase
        else:
            sparklestate = sparklebase
            onstate = image
            sparkleprob = sparkle
        return anim.SMAnimation("blank",
                                anim.State("blank", Solid("#00000000")),
                                anim.Edge("blank", 0.1, "blank", prob=30),
                                anim.Edge("blank", 0.1, "flash", trans = Dissolve(0.04, alpha=True)),
                                anim.State("flash", Solid("#FFFFFF66")),
                                anim.Edge("flash", 0.1, "on", trans = Dissolve(0.04, alpha=True), prob=normalprob),
                                anim.Edge("flash", 0.1, "sparkle", trans = Dissolve(0.04, alpha=True), prob=sparkleprob),
                                anim.State("on", onstate),
                                anim.Edge("on", 6.0, "blank", trans = Dissolve(3.0, alpha=True)),
                                anim.State("sparkle", sparklestate),
                                anim.Edge("sparkle", 6.0, "blank", trans = Dissolve(3.0, alpha=True)),
                                showold=True)

    fireworks = LiveComposite((800,600),
                              (0,0), fw_constructor("vfx/fw1.png"),
                              (0,0), fw_constructor("vfx/fw2.png"),
                              (0,0), fw_constructor("vfx/fw3.png"),
                              (0,0), fw_constructor("vfx/fw4.png"),
                              (0,0), fw_constructor("vfx/fw5.png"),
                              (0,0), fw_constructor("vfx/fw6.png"),
                              (0,0), fw_constructor("vfx/fw7.png"),
                              (0,0), fw_constructor("vfx/fw8.png", sparkle=1),
                              (0,0), fw_constructor("vfx/fw9.png", sparkle=1))

    renpy.image("fireworks",fireworks)
 
    fireshine = LiveComposite((800,600),
                              (0,0), fw_constructor(Solid("#FF000009")),
                              (0,0), fw_constructor(Solid("#00FF0009")),
                              (0,0), fw_constructor(Solid("#0000FF09")),
                              (0,0), fw_constructor(Solid("#CC00CC09")),
                              (0,0), fw_constructor(Solid("#CCCC0009")),
                              (0,0), fw_constructor(Solid("#0000CC09")))

    renpy.image("fireshine",fireshine)
    
    #Hanako fireworks
    
    def hanako_fw_constructor(image, sparkle=True, normalprob = 1):
        sparklebase = anim.Blink(image, high=1.0, low=10.0, on=0.2, off=0.0, set=3.0)
        sparkleprob = 1
        if not sparkle:
            sparklestate = image
            onstate = image
        elif str(sparkle) == "True":
            sparklestate = sparklebase
            onstate = sparklebase
        else:
            sparklestate = sparklebase
            onstate = image
            sparkleprob = sparkle
        return anim.SMAnimation("blank",
                                anim.State("blank", Solid("#00000000")),
                                anim.Edge("blank", 0.1, "blank", prob=30),
                                anim.Edge("blank", 0.1, "flash", trans = Dissolve(0.04, alpha=True)),
                                anim.State("flash", Solid("#FFFFFF66")),
                                anim.Edge("flash", 0.1, "on", trans = Dissolve(0.04, alpha=True), prob=normalprob),
                                anim.Edge("flash", 0.1, "sparkle", trans = Dissolve(0.04, alpha=True), prob=sparkleprob),
                                anim.State("on", onstate),
                                anim.Edge("on", 6.0, "blank", trans = Dissolve(3.0, alpha=True)),
                                anim.State("sparkle", sparklestate),
                                anim.Edge("sparkle", 6.0, "blank", trans = Dissolve(3.0, alpha=True)),
                                showold=True)
    
    hanako_fireshine = LiveComposite((800,600),
                              #(0,0), hanako_fw_constructor("event/hanako_fireshine/hanako_fw_flash0.jpg"),
                              (0,0), hanako_fw_constructor("event/hanako_fireshine/hanako_fw_flash1.jpg"),
                              (0,0), hanako_fw_constructor("event/hanako_fireshine/hanako_fw_flash2.jpg"),
                              (0,0), fw_constructor("event/hanako_fireshine/hanako_fw_flash3.jpg"),
                              (0,0), fw_constructor("event/hanako_fireshine/hanako_fw_flash4.jpg"),
                              (0,0), fw_constructor("event/hanako_fireshine/hanako_fw_flash5.jpg"),
                              (0,0), fw_constructor("event/hanako_fireshine/hanako_fw_flash6.jpg"))
                                  
    renpy.image("hanako_fireshine",hanako_fireshine)

    # rain
    def rainAnim(offset=0, framelength=0.2, imageoffset=0, zoom=1.0):
        frame = []
        trans = Dissolve(framelength / 2.0, alpha=True)
        for i in xrange(6):
            frame.append(im.Rotozoom("vfx/fx-rain-bg" + str(i + imageoffset + 1) + ".png", 0, zoom))
        return anim.SMAnimation("start",
                                anim.State("start", Solid("#00000000")),
                                anim.Edge("start", offset, "one", trans=trans),
                                anim.State("one", frame[0]),
                                anim.Edge("one", framelength, "two", trans=trans),
                                anim.Edge("one", framelength, "three", trans=trans),
                                anim.Edge("one", framelength, "four", trans=trans),
                                anim.Edge("one", framelength, "five", trans=trans),
                                anim.Edge("one", framelength, "six", trans=trans),
                                anim.State("two", frame[1]),
                                anim.Edge("two", framelength, "one", trans=trans),
                                anim.Edge("two", framelength, "three", trans=trans),
                                anim.Edge("two", framelength, "four", trans=trans),
                                anim.Edge("two", framelength, "five", trans=trans),
                                anim.Edge("two", framelength, "six", trans=trans),
                                anim.State("three", frame[2]),
                                anim.Edge("three", framelength, "two", trans=trans),
                                anim.Edge("three", framelength, "one", trans=trans),
                                anim.Edge("three", framelength, "four", trans=trans),
                                anim.Edge("three", framelength, "five", trans=trans),
                                anim.Edge("three", framelength, "six", trans=trans),
                                anim.State("four", frame[3]),
                                anim.Edge("four", framelength, "two", trans=trans),
                                anim.Edge("four", framelength, "three", trans=trans),
                                anim.Edge("four", framelength, "one", trans=trans),
                                anim.Edge("four", framelength, "five", trans=trans),
                                anim.Edge("four", framelength, "six", trans=trans),
                                anim.State("five", frame[4]),
                                anim.Edge("five", framelength, "two", trans=trans),
                                anim.Edge("five", framelength, "three", trans=trans),
                                anim.Edge("five", framelength, "four", trans=trans),
                                anim.Edge("five", framelength, "one", trans=trans),
                                anim.Edge("five", framelength, "six", trans=trans),
                                anim.State("six", frame[5]),
                                anim.Edge("six", framelength, "two", trans=trans),
                                anim.Edge("six", framelength, "three", trans=trans),
                                anim.Edge("six", framelength, "four", trans=trans),
                                anim.Edge("six", framelength, "five", trans=trans),
                                anim.Edge("six", framelength, "one", trans=trans),
                                )

    rain = LiveComposite((800, 600),
                         (0,0), rainAnim(),
                         (0,0), rainAnim(offset=0.1, zoom=1.2),
                         )
    renpy.image("rain",rain)
    
    
    # double say box
    # Accepts two character objects and at least one string (the text being said)
    def doublespeak(char0, char1, msg0, msg1=False):
        # Determine what we're dealing with here
        global current_line
        speaker=dict()
        ctc=dict()
        for (n, char) in enumerate((char0,char1)):
            if hasattr(char,"name"):
                if hasattr(char,"dynamic") and char.dynamic == True:
                    myname = eval(char.name)
                else:
                    myname = char.name
                if hasattr(char,"who_args") and "color" in char.who_args:
                    speaker[n] = "{color="+char.who_args["color"]+"}"+myname+"{/color}"
                else:
                    speaker[n] = myname
            else:
                speaker[n] = str(char)
            if hasattr(char,"display_args") and "ctc" in char.display_args:
                ctc[n] = char.display_args["ctc"]
            else:
                ctc[n] = config.nvl_page_ctc

        msg0 = displayStrings.quote_outer_open + msg0 + displayStrings.quote_outer_close
        if not msg1:
            msg1 = msg0
        else:
            msg1 = displayStrings.quote_outer_open + msg1 + displayStrings.quote_outer_close

        current_line = None
        if msg0 == msg1:
            store_say(speaker[0] + " & " + speaker[1], msg0)
        else:
            store_say(speaker[0], msg0)
            store_say(speaker[1], msg1)

        renpy.shown_window()
        ui.frame(background="ui/bg-doublespeak.png", yalign=1.0, yminimum=160, style="say_window")
        ui.grid(2,1,xfill=True)
        ui.vbox(style="say_vbox")
        ui.text(speaker[0], style="say_label", **displayStrings.styleoverrides)
        ui.text(msg0, slow=True, style="say_dialogue", xmaximum=350, **displayStrings.styleoverrides)
        ui.close()
        ui.vbox(style="say_vbox", xpos=20)
        ui.text(speaker[1], style="say_label", **displayStrings.styleoverrides)
        ui.text(msg1, slow=True, style="say_dialogue", xmaximum=350, **displayStrings.styleoverrides)
        ui.close()
        ui.close()
        # Fake ctc indicator(s). This assumes the ctc is always in the lower right corner!
        ui.fixed(xpos=-400)
        ui.image(ctc[0])
        ui.close()
        ui.image(ctc[1])
        # Make it behave (somewhat) like a text page
        ui.saybehavior(afm=msg0+msg1)
        ui.interact(roll_forward=True, type="say")
        renpy.checkpoint()

    # show a written note
    def written_note(text, window_args={}, text_args={}):
        global current_line
        wdt_off()
        
        current_line = None
        store_say("Note", text.replace("\n\n","\n"))
        
        default_text_args = displayStrings.styleoverrides.copy()
        default_text_args.update(text_args)
        
        #default_text_args = text_args
        
        renpy.transition(dissolve)
        #ui.layer("master")
        ui.at(Move((0.5,0.8,0.5,0.5),(0.5,0.5,0.5,0.5),0.5,time_warp=_ease_in_time_warp))
        ui.frame(style="note_window", **window_args)
        ui.vbox()
        ui.text("", style="note_text")
        ui.text(text, style="note_text", **default_text_args)
        ui.text("", style="note_text")
        ui.close()
        ui.image(centered.display_args["ctc"])
        ui.saybehavior(afm=text)
        #ui.close()
        ui.interact(roll_forward=True, type="say")
        renpy.checkpoint()
        renpy.transition(hidenote, layer="transient")
        renpy.pause(0.7)
        wdt_on()

    
     # show a written note without window flickering! :D - Kelper
    def fixedwritten_note(text, window_args={}, text_args={}):
        global current_line
        
        current_line = None
        store_say("Note", text.replace("\n\n","\n"))
        
        default_text_args = displayStrings.styleoverrides.copy()
        default_text_args.update(text_args)
        
        #default_text_args = text_args
        
        renpy.transition(dissolve)
        #ui.layer("master")
        ui.at(Move((0.5,0.8,0.5,0.5),(0.5,0.5,0.5,0.5),0.5,time_warp=_ease_in_time_warp))
        ui.frame(style="note_window", **window_args)
        ui.vbox()
        ui.text("", style="note_text")
        ui.text(text, style="note_text", **default_text_args)
        ui.text("", style="note_text")
        ui.close()
        ui.image(centered.display_args["ctc"])
        ui.saybehavior(afm=text)
        #ui.close()
        ui.interact(roll_forward=True, type="say")
        renpy.checkpoint()
        renpy.transition(hidenote, layer="transient")
        renpy.pause(0.7)

    # functions for extra_menu:
    def extra_button(text,in_displayable,clicked=None,style='prefs_label',state="button"):

        image = im.Image(in_displayable[0:-4]+"-c.png", xalign=0.5)
        imagebase = VBox(in_displayable, xalign=0.5)
        imagedisabled = VBox(ib_base(in_displayable), xalign=0.5)
        textbase = Text(text, style=style, xalign=0.5)
        texthover = Text(text, style=style, color="#000", xalign=0.5)
        textdisabled = Text(text, style=style, color="#00000019", xalign=0.5)

        if state == "return": # "fake" return button
            textbase = LiveComposite((100, 30), 
                                     (0, 3), ib_base("ui/bt-return.png"),
                                     (30, 0), textbase)
            texthover = LiveComposite((100, 30), 
                                     (0, 3), "ui/bt-return.png",
                                     (30, 0), texthover)

        if state == "disabled":
            button_disabled = VBox(imagedisabled, textdisabled)
            ui.imagebutton(button_disabled,button_disabled,clicked=None, yalign=1.0) # ui.image layouts differently
            return
        button_base = VBox(imagebase, textbase)
        button_hover = VBox(image, texthover)
        ui.imagebutton(button_base,button_hover,clicked=clicked, yalign=1.0)

    def toggle_commentary():
        # self-explanatory y/n? if n, gtfo my code
        persistent.commentary_on = not persistent.commentary_on
        return False

    def toggle_h():
        # self-explanatory y/n? if n, gtfo my code
        persistent.hdisabled = not persistent.hdisabled
        return False

    # viewport functions for music_menu:
    def increase_m_yoffset():
        # scroll down
        global auto_offset
        store_m_yoffset(persistent.mpicker_yoffset + auto_offset)

    def decrease_m_yoffset():
        # scroll up
        global auto_offset
        store_m_yoffset(persistent.mpicker_yoffset - auto_offset)

    def store_m_yoffset(input=persistent.mpicker_yoffset):
        # actually move the viewport & save for posterity
        global auto_offset, ex_m_tracks
        maxheight = auto_offset * (len(ex_m_tracks) - 8)
        if input > maxheight:
            input = maxheight
        elif input < 0:
            input = 0
        persistent.mpicker_yoffset = input
        yadj.change(input)

    # functions for gamepad settings
    def joy_button(label,key):
        myclicked = renpy.curry(joy_clicked)(label=label, key=key)
        layout.button(_(label) + " - " + _(_preferences.joymap.get(key, displayStrings.gamepad_key_na)), "mm", clicked=myclicked, index=label)

    def joy_clicked(label, key):
        return renpy.invoke_in_new_context(set_binding, label, key)

    def set_binding(label, key):
        renpy.transition(config.intra_transition)
        if renpy.context().main_menu: # We'll draw a fake main menu for style reasons, or it'll just be boring black in the mm
            bgimage = style.mm_root.background
        else:
            bgimage = None

        message = displayStrings.gamepad_request_key % label

        _prompt(None, message, background=bgimage, interact=False)

        _joystick_get_binding()
        ui.add(renpy.Keymap(game_menu=ui.returns(True)))
        binding = ui.interact()
        _joystick_take_binding(binding, key)

        return True

    # functions for scene_select:
    def refresh_label(a,b):
        # display scene summary, if set. this is polled automatically at about 10 Hz.
        global ss_desc
        disp = Text(ss_desc, xalign=0.5, yalign=0.98, size=18)
        return (disp,0.05)

    def ss_unhovered():
        # clear summary
        global ss_desc
        ss_desc = ""

    def ss_hovered(hover_text=None):
        # write summary to crude display "buffer"
        global ss_desc
        if not hover_text or hover_text == True:
            ss_desc = ""
        else:
            ss_desc = hover_text

    def ss_button(text, hover_text=None, clicked=None, selected=False):
        # wrapper function for buttons with hover callback for summary display
        global ss_desc, ss_hovered, ss_unhovered
        myhovered = renpy.curry(ss_hovered)(hover_text=hover_text)
        layout.button(text, 'mm', clicked=clicked, hovered=myhovered, unhovered=ss_unhovered, selected=selected)

    def store_s_yoffset(input=persistent.spicker_yoffset):
        # actually move the viewport & save for posterity
        global auto_offset, available_scenes
        maxheight = auto_offset * (len(available_scenes) - 8)
        if input > maxheight:
            input = maxheight
        elif input < 0:
            input = 0
        persistent.spicker_yoffset = input
        yadj.change(input)

    def increase_s_yoffset():
        # scroll down
        global auto_offset
        store_s_yoffset(persistent.spicker_yoffset + auto_offset)

    def decrease_s_yoffset():
        # scroll up
        global auto_offset
        store_s_yoffset(persistent.spicker_yoffset - auto_offset)

    def toggle_playthrough():
        # the interaction in question needs a syntactically correct return variable to work.
        global playthroughflag
        playthroughflag = not playthroughflag
        return ("_pt_toggled", playthroughflag)

    # prefixes a dictionary. Used for styling
    def prefix_dict(indict, prefix=False, combine=False):
        if not prefix:
            return indict
        outdict = {}
        inkeys = indict.keys()
        for key in inkeys:
            outdict[prefix + key] = indict[key]
        
        if combine:
            outdict.update(indict)
        
        return outdict


    # Big old Wall o' Drugs animation

    class drugsDisp(renpy.Displayable):
        def __init__(self, width, height):
            renpy.Displayable.__init__(self)
            
            from random import shuffle, randrange

            self.length = 22.0 # this has to be a float or shit will hit the fan
            self.fadeintime = 1.0 # this too

            self.width = width
            self.height = height
            
            self.singlewordlist = displayStrings.drugs_wordlist
            shuffle(self.singlewordlist)
            self.wordlist = self.singlewordlist * 5
            
            self.timeperword = self.length / len(self.wordlist)
            self.words = []
            self.disps = []
            for word in self.wordlist:
                thisword = object()
                thisword.payload = word
                thisword.position = self.randompos()
                thisword.size = self.randomsize()
                thisword.alpha = 0
                thisword.fulldisp = self.subdisp(thisword.payload,thisword.size,255)
                self.words.append(thisword)
                self.disps.append(thisword.fulldisp)
            self.framelength = 0.04 # maximum frame length, 25 FPS
            self.progress = 0 # how many words are currently displayed?
            
            
        def visit(self):
            return self.disps
        
        def subdisp(self, payload, size, alpha):
               return Text(payload,size=size, color=(0,0,0,alpha), font=srsfont)
        
        def randompos(self):
            from random import randrange
            return (randrange(self.width), randrange(self.height))
        
        def randomsize(self):
            from random import randrange
            return randrange(30,100)
        
        def render(self, width, height, st, at):
            # st = displayable timebase
            # at = tag timebase
            
            width = self.width
            height = self.height
            
            from math import floor
            
            rv = renpy.Render(width, height)
            rv.fill((255,255,255,255))
            
            
            for n, word in enumerate(self.words):
                
                if n > self.progress:
                    break
                
                if word.alpha < 255:
                    word.alpha = ((st - (n * self.timeperword)) / self.fadeintime) * 255
                    if word.alpha > 255:
                        word.alpha = 255
                    disp = self.subdisp(word.payload, word.size, word.alpha)
                else:
                    disp = word.fulldisp
                
                rend = renpy.render(disp,width,height,st,at)
                size = rend.get_size()
                rv.blit(rend, (word.position[0]-(size[0]/2), word.position[1]-(size[1]/2)))
            
            
            newprogress = int(floor(st / self.timeperword))
            self.progress = newprogress
            renpy.redraw(self, self.framelength)
            #renpy.timeout(self.framelength)
            return rv
            

