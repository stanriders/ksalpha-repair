# vim: expandtab
# By @__akiaki with love <3 (v0.5b, prealpha only)

#######################################################################
#               _   _   _  ___ _____ ___ ____ _____   _               #
#              | | | \ | |/ _ \_   _|_ _/ ___| ____| | |              # 
#              | | |  \| | | | || |  | | |   |  _|   | |              #
#              |_| | |\  | |_| || |  | | |___| |___  |_|              #
#              (_) |_| \_|\___/ |_| |___\____|_____| (_)              #
#                                                                     #
#   FOR THE LOVE OF RIN RENAME OR DELETE THIS FILE BEFORE RELEASING   #
#######################################################################

init 3 python:
    config.developer = True # change this to False to disable
    if config.developer:
        devlvl = 5

init python:
    def dev_overlay_previous():
        # damnit Kelper, asking for previous scene stepping <_<
        t = -2
        while len(seen_labels) >= abs(t):  
            try:
                label = str(seen_labels[t])
                if renpy.has_label(label):
                    for i in range(1, abs(t)):
                        del seen_labels[-1]
                    renpy.restart_interaction()
                    renpy.jump(label)
                    break
                t -= 1
            except renpy.game.JumpException:
                raise
            except Exception, e:
                t -= 1

    dev_overlay_show = False
    def dev_overlay_toggle():
        global dev_overlay_show
        try:
            dev_overlay_show = (not dev_overlay_show)
        except UnboundLocalError:
            dev_overlay_show = True
        renpy.restart_interaction()

    def dev_overlay():     
        if config.developer:
            ui.frame(xalign=1.0, yalign=0.0, spacing=5, left_padding=0, right_padding=0, top_padding=0, bottom_padding=0)
            ui.vbox(spacing=5)
            ui.hbox(spacing=5)
            if dev_overlay_show:
                ui.null(min_width=5)
                ui.text("interact: "+renpy.last_interact_type())
                if _return:
                    ui.text("_return: "+_return)
                ui.textbutton("restart", lambda: renpy.utter_restart())
                
            ui.textbutton("#", dev_overlay_toggle)
            ui.close()

            if dev_overlay_show:
                ui.hbox(spacing=5)
                ui.null(min_width=5)
                if last_visited_label:
                    ui.text("scene: " + last_visited_label)
                    ui.textbutton("<<", dev_overlay_previous if len(seen_labels) >= 2 else ui.jumps(last_visited_label))
                    ui.textbutton("0", ui.jumps(last_visited_label))
                    ui.textbutton(">>", ui.jumps("simple_return"))
                else:
                    ui.text("no scene info")
                ui.close()
            ui.close()

    config.overlay_functions.append(dev_overlay)
