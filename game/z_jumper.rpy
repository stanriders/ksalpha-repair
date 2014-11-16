# vim: expandtab
# Provides an overlay to jump to different acts.
# By aki with love <3 (v0.7-pre.0)

init python:
    def jumper_menu_space():
        # so that i can change this quickly
        ui.text("     ")

    # Set the default target to 'start' so if we get called stupidly
    # we just go to the beginning of the game. This is only here in
    # the first place because we can't pass arguments to a label from
    # a jump, only a call... <_<
    jumper_target = jumper_default_target = 'start'

    def jumper_scene(target):
        # Like ui.jumps(target) but do our shit.
        def dothething():
            global jumper_target
            jumper_target = target
            renpy.jump_out_of_context('jumper_jump')
        return dothething

label jumper_jump:
    # basically replicating start_from_mm because none of that is designed to be
    # reusable at all thanks delta </3
    $ init_vars()
    $ playthroughflag = True
    $ ask_to_quit = True
    $ np_current_language = persistent.current_language
    $ renpy.block_rollback()
    $ readback_buffer = []

    # store the target locally
    $ target = jumper_target
    # and reset the global target to the default in case we fuck up (which we will)
    $ jumper_target = jumper_default_target

    nvl clear
    stop music fadeout 1.0
    stop ambient fadeout 1.0

    scene black
    with config.game_main_transition

    # YOU HAVE TO USE jump_in HERE OR EVERYTHING FUCKS UP WITH SAVES
    # FUCK REn'PY IN THE ASS SERIOUSLY I HATE IT SO MUCH
    jump_in expression target

label jumper:
    python:
        # don't show the gm
        layout.navigation(None)

        if renpy.context().main_menu: 
            # We'll draw a fake main menu for style reasons, or it'll just be boring black in the mm
            ui.image(style.mm_root.background)

        ui.image(style.gm_root.background)
        ui.image("ui/bg-config.png", xalign=0.5, yalign=0.5)

        ui.vbox(xpos=180, ypos=110, background=None)
        ui.text("Select Act", style="page_caption")
        ui.null(height=8)

        # Hanako
        ui.vbox()
        ui.text("Hanako: ", style="prefs_label")
        ui.hbox()
        jumper_menu_space()
        widget_button("Act 2", "ui/bt-blank.png", clicked=jumper_scene("H2"), xsize=65, textxoffset=0)
        widget_button("Act 3", "ui/bt-blank.png", clicked=jumper_scene("H11"), xsize=65, textxoffset=0)
        widget_button("Act 4 (Decision)", "ui/bt-blank.png", clicked=jumper_scene("H14"), xsize=155, textxoffset=0)
        widget_button("Act 5", "ui/bt-blank.png", clicked=jumper_scene("HT14"), xsize=65, textxoffset=0)
        ui.close()
        ui.close()

        # Lilly
        ui.vbox()
        ui.text("Lilly: ", style="prefs_label")
        ui.hbox()
        jumper_menu_space()
        widget_button("Act 2", "ui/bt-blank.png", clicked=jumper_scene("L1"), xsize=65, textxoffset=0)
        widget_button("Act 3", "ui/bt-blank.png", clicked=jumper_scene("L13"), xsize=65, textxoffset=0)
        widget_button("Act 4", "ui/bt-blank.png", clicked=jumper_scene("L21"), xsize=65, textxoffset=0)
        # apparently this doesn't need to be there
        # widget_button("Act 5", "ui/bt-blank.png", clicked=jumper_scene("L43"), xsize=65, textxoffset=0)
        ui.close()
        ui.close()

        # Emi
        ui.vbox()
        ui.text("Emi: ", style="prefs_label")
        ui.hbox()
        jumper_menu_space()
        widget_button("Act 2", "ui/bt-blank.png", clicked=jumper_scene("E3"), xsize=65, textxoffset=0)
        widget_button("Act 3", "ui/bt-blank.png", clicked=jumper_scene("E16"), xsize=65, textxoffset=0)
        ui.close()
        ui.close()

        # Rin
        ui.vbox()
        ui.text("Rin: ", style="prefs_label")
        ui.hbox()
        jumper_menu_space()
        widget_button("Act 2", "ui/bt-blank.png", clicked=jumper_scene("R2"), xsize=65, textxoffset=0)
        widget_button("Act 3", "ui/bt-blank.png", clicked=jumper_scene("R19"), xsize=65, textxoffset=0)
        widget_button("Act 4", "ui/bt-blank.png", clicked=jumper_scene("R33"), xsize=65, textxoffset=0)
        ui.close()
        ui.close()

        # Shizune
        ui.vbox()
        ui.text("Shizune: ", style="prefs_label")
        ui.hbox()
        jumper_menu_space()
        widget_button("Act 2", "ui/bt-blank.png", clicked=jumper_scene("S8"), xsize=65, textxoffset=0)
        widget_button("Act 3", "ui/bt-blank.png", clicked=jumper_scene("S20"), xsize=65, textxoffset=0)
        widget_button("Act 4", "ui/bt-blank.png", clicked=jumper_scene("S31"), xsize=65, textxoffset=0)
        ui.close()
        ui.close()
        
        # Hana-Lilly (just trying to understand what is it even) [str]
        ui.vbox()
        ui.text("Hana-Lilly: ", style="prefs_label")
        ui.hbox()
        jumper_menu_space()
        widget_button("Act 2", "ui/bt-blank.png", clicked=jumper_scene("HLT3"), xsize=65, textxoffset=0)
        ui.close()
        ui.close()

        ui.close()

        return_button(ui.returns("return"))

        # WHY IS THIS SHIT SO FUCKING DIFFICULT
        gi_result = ui.interact()
        if gi_result == "return":
            if renpy.context().main_menu:
                renpy.jump("_return")
            else:
                renpy.transition(config.intra_transition)
                renpy.jump(_game_menu_screen)

        # loop if we don't get anything useful from the interaction
        renpy.jump("jumper")

