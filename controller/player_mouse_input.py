import global_variables as gv

mouse_down = False


def title_screen_mouse_input(title_screen_view, mouse, click):
    global mouse_down
    mouse_down = False

    for btn_name in title_screen_view.all_buttons:  # Loops through every button's position and checks if the mouse \
                                                    # is interacting with it or not
        btn = title_screen_view.all_buttons[btn_name]
        if btn.btn_pos_size[0] < mouse[0] < btn.btn_pos_size[0] + btn.btn_pos_size[2]:
            if btn.btn_pos_size[1] < mouse[1] < btn.btn_pos_size[1] + btn.btn_pos_size[3]:
                if click[0] == 1 and not mouse_down:
                    mouse_down = True
                    return btn_name, True, btn_name
                else:
                    check_mouse_down(click)
                    return btn_name, False, None

    # if title_screen_view.all_buttons[gv.BUTTON_TEXTS[0]].btn_pos_size[0] < mouse[0] < \
    #         title_screen_view.all_buttons[gv.BUTTON_TEXTS[0]].btn_pos_size[0] + \
    #         title_screen_view.all_buttons[gv.BUTTON_TEXTS[0]].btn_pos_size[2]:
    #     if title_screen_view.all_buttons[gv.BUTTON_TEXTS[0]].btn_pos_size[1] < mouse[1] < \
    #             title_screen_view.all_buttons[gv.BUTTON_TEXTS[0]].btn_pos_size[1] + \
    #             title_screen_view.all_buttons[gv.BUTTON_TEXTS[0]].btn_pos_size[3]:
    #         if click[0] == 1 and not mouse_down:
    #             mouse_down = True
    #             return gv.BUTTON_TEXTS[0], True, gv.BUTTON_TEXTS[0]
    #         else:
    #             check_mouse_down(click)
    #             return gv.BUTTON_TEXTS[0], False, None
    # if title_screen_view.all_buttons[gv.BUTTON_TEXTS[1]].btn_pos_size[0] < mouse[0] < \
    #         title_screen_view.all_buttons[gv.BUTTON_TEXTS[1]].btn_pos_size[0] + \
    #         title_screen_view.all_buttons[gv.BUTTON_TEXTS[1]].btn_pos_size[2]:
    #     if title_screen_view.all_buttons[gv.BUTTON_TEXTS[1]].btn_pos_size[1] < mouse[1] < \
    #             title_screen_view.all_buttons[gv.BUTTON_TEXTS[1]].btn_pos_size[1] + \
    #             title_screen_view.all_buttons[gv.BUTTON_TEXTS[1]].btn_pos_size[3]:
    #         if click[0] == 1 and not mouse_down:
    #             mouse_down = True
    #             return gv.BUTTON_TEXTS[1], True, gv.BUTTON_TEXTS[1]
    #         else:
    #             check_mouse_down(click)
    #             return gv.BUTTON_TEXTS[1], False, None
    # if title_screen_view.all_buttons[gv.BUTTON_TEXTS[2]].btn_pos_size[0] < mouse[0] < \
    #         title_screen_view.all_buttons[gv.BUTTON_TEXTS[2]].btn_pos_size[0] + \
    #         title_screen_view.all_buttons[gv.BUTTON_TEXTS[2]].btn_pos_size[2]:
    #     if title_screen_view.all_buttons[gv.BUTTON_TEXTS[2]].btn_pos_size[1] < mouse[1] < \
    #             title_screen_view.all_buttons[gv.BUTTON_TEXTS[2]].btn_pos_size[1] + \
    #             title_screen_view.all_buttons[gv.BUTTON_TEXTS[2]].btn_pos_size[3]:
    #         if click[0] == 1 and not mouse_down:
    #             mouse_down = True
    #             return gv.BUTTON_TEXTS[2], True, gv.BUTTON_TEXTS[2]
    #         else:
    #             check_mouse_down(click)
    #             return gv.BUTTON_TEXTS[2], False, None
    # if title_screen_view.all_buttons[gv.BUTTON_TEXTS[3]].btn_pos_size[0] < mouse[0] < \
    #         title_screen_view.all_buttons[gv.BUTTON_TEXTS[3]].btn_pos_size[0] + \
    #         title_screen_view.all_buttons[gv.BUTTON_TEXTS[3]].btn_pos_size[2]:
    #     if title_screen_view.all_buttons[gv.BUTTON_TEXTS[3]].btn_pos_size[1] < mouse[1] < \
    #             title_screen_view.all_buttons[gv.BUTTON_TEXTS[3]].btn_pos_size[1] + \
    #             title_screen_view.all_buttons[gv.BUTTON_TEXTS[3]].btn_pos_size[3]:
    #         if click[0] == 1 and not mouse_down:
    #             mouse_down = True
    #             return gv.BUTTON_TEXTS[3], True, gv.BUTTON_TEXTS[3]
    #         else:
    #             check_mouse_down(click)
    #             return gv.BUTTON_TEXTS[3], False, None

    check_mouse_down(click)
    return None, False, None


def check_mouse_down(click):
    global mouse_down
    if click[0] != 1:
        mouse_down = False

