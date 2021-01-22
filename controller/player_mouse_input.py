mouse_down = False  # Prevents user from pressing a button multiple times without first releasing the click button


def title_screen_mouse_input(all_buttons, mouse, click):
    global mouse_down

    for btn_name in all_buttons:  # Loops through every button's position and checks if the mouse \
                                                    # is interacting with it or not
        btn = all_buttons[btn_name]
        if btn.btn_pos_size[0] < mouse[0] < btn.btn_pos_size[0] + btn.btn_pos_size[2]:
            if btn.btn_pos_size[1] < mouse[1] < btn.btn_pos_size[1] + btn.btn_pos_size[3]:
                if click[0] == 1:  # and not mouse_down:
                    mouse_down = True
                    return btn_name, True, btn_name
                else:
                    check_mouse_down(click)
                    return btn_name, False, None

    check_mouse_down(click)
    return None, False, None


def check_mouse_down(click):
    global mouse_down
    if click[0] != 1:
        mouse_down = False

