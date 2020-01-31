from global_variables import BUTTON_TEXTS


def title_screen_mouse_input(title_screen_view, mouse, click):
    if title_screen_view.p1_btn_pos_size[0] < mouse[0] < title_screen_view.p1_btn_pos_size[0] + title_screen_view.p1_btn_pos_size[2]:
        if title_screen_view.p1_btn_pos_size[1] < mouse[1] < title_screen_view.p1_btn_pos_size[1] + title_screen_view.p1_btn_pos_size[3]:
            if click[0] == 1:
                return 0, True, BUTTON_TEXTS[0]
            else:
                return 0, False, None
    if title_screen_view.p2_btn_pos_size[0] < mouse[0] < title_screen_view.p2_btn_pos_size[0] + title_screen_view.p2_btn_pos_size[2]:
        if title_screen_view.p2_btn_pos_size[1] < mouse[1] < title_screen_view.p2_btn_pos_size[1] + title_screen_view.p2_btn_pos_size[3]:
            if click[0] == 1:
                return 1, True, BUTTON_TEXTS[1]
            else:
                return 1, False, None
    if title_screen_view.options_btn_pos_size[0] < mouse[0] < title_screen_view.options_btn_pos_size[0] + title_screen_view.options_btn_pos_size[2]:
        if title_screen_view.options_btn_pos_size[1] < mouse[1] < title_screen_view.options_btn_pos_size[1] + title_screen_view.options_btn_pos_size[3]:
            if click[0] == 1:
                return 2, True, BUTTON_TEXTS[2]
            else:
                return 2, False, None
    if title_screen_view.exit_btn_pos_size[0] < mouse[0] < title_screen_view.exit_btn_pos_size[0] + title_screen_view.exit_btn_pos_size[2]:
        if title_screen_view.exit_btn_pos_size[1] < mouse[1] < title_screen_view.exit_btn_pos_size[1] + title_screen_view.exit_btn_pos_size[3]:
            if click[0] == 1:
                return 3, True, BUTTON_TEXTS[3]
            else:
                return 3, False, None
    return -1, False, None
