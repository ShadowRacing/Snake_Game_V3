"""
Returning home screen manager.
"""

import time
import traceback

class HomeScreenManager:
    def __init__(self, classic_snake_canvas, endless_snake_canvas, leveling_snake_canvas, food_time_attack_canvas, challange_choice_canvas, challange_settings_canvas, info_canvas, info_general_canvas, info_classic_canvas, info_endless_canvas, info_leveling_canvas, info_challange_canvas, settings_canvas, settings_canvas_values, settings_canvas_reset, reset_label, reset_settings_frame, reset_settings_frame_1, scrollable_frame, framelabel_panel, button_commands, mini_snake_game_canvas, original_main_canvas):
        self.classic_snake_canvas = classic_snake_canvas
        self.endless_snake_canvas = endless_snake_canvas
        self.leveling_snake_canvas = leveling_snake_canvas
        self.food_time_attack_canvas = food_time_attack_canvas
        self.challange_choice_canvas = challange_choice_canvas
        self.challange_settings_canvas = challange_settings_canvas
        self.info_canvas = info_canvas
        self.info_general_canvas = info_general_canvas
        self.info_classic_canvas = info_classic_canvas
        self.info_endless_canvas = info_endless_canvas
        self.info_leveling_canvas = info_leveling_canvas
        self.info_challange_canvas = info_challange_canvas
        self.settings_canvas = settings_canvas
        self.settings_canvas_values = settings_canvas_values
        self.settings_canvas_reset = settings_canvas_reset
        self.reset_label = reset_label
        self.reset_settings_frame = reset_settings_frame
        self.reset_settings_frame_1 = reset_settings_frame_1
        self.scrollable_frame = scrollable_frame
        self.framelabel_panel = framelabel_panel
        self.button_commands = button_commands
        self.mini_snake_game_canvas = mini_snake_game_canvas
        self.original_main_canvas = original_main_canvas

    def destroy_canvas(self, canvas):
        """
        Destroy the canvas.
        """
        try:
            if canvas is not None:
                #self.framelabel_panel.set_create_label_canvas_flag(False)
                canvas.destroy()
                return None
            return canvas

        except ValueError as e:
            traceback.print_exc(e)
            return canvas


    def return_home(self):
        """
        Return to the home screen.
        """
        try:
            # Reset the patchnotes_displayed variable
            if not hasattr(self.button_commands, 'patchnotes_displayed'):
                if self.scrollable_frame is not None and self.scrollable_frame.winfo_exists():
                    self.scrollable_frame.place_forget()
                self.patchnotes_displayed = False

            if hasattr(self, 'button_commands'):
                self.create_reset_button_panel.destroy_buttons()

            if self.main_canvas == self.classic_snake_canvas:
                self.classic_snake_canvas.delete_game_labels()
            elif self.main_canvas == self.endless_snake_canvas:
                self.endless_snake_canvas.delete_game_labels_()
            elif self.main_canvas == self.leveling_snake_canvas:
                self.leveling_snake_canvas.delete_game_labels__()
            elif self.main_canvas == self.food_time_attack_canvas:
                self.food_time_attack_canvas.delete_game_labels___()
            elif self.main_canvas == self.info_general_canvas:
                self.close_mini_snake()

            time.sleep(0.1)
            # Destroy all game canvases
            self.classic_snake_canvas = self.destroy_canvas(self.classic_snake_canvas)
            self.endless_snake_canvas = self.destroy_canvas(self.endless_snake_canvas)
            self.leveling_snake_canvas = self.destroy_canvas(self.leveling_snake_canvas)
            self.food_time_attack_canvas = self.destroy_canvas(self.food_time_attack_canvas)
            self.challange_choice_canvas = self.destroy_canvas(self.challange_choice_canvas)
            self.challange_settings_canvas = self.destroy_canvas(self.challange_settings_canvas)
            self.info_canvas = self.destroy_canvas(self.info_canvas)
            self.info_general_canvas = self.destroy_canvas(self.info_general_canvas)
            self.info_classic_canvas = self.destroy_canvas(self.info_classic_canvas)
            self.info_endless_canvas = self.destroy_canvas(self.info_endless_canvas)
            self.info_leveling_canvas = self.destroy_canvas(self.info_leveling_canvas)
            self.info_challange_canvas = self.destroy_canvas(self.info_challange_canvas)
            self.settings_canvas = self.destroy_canvas(self.settings_canvas)
            self.settings_canvas_reset = self.destroy_canvas(self.settings_canvas_reset)
            self.settings_canvas_values = self.destroy_canvas(self.settings_canvas_values)
            self.mini_snake_game_canvas = self.destroy_canvas(self.mini_snake_game_canvas)

            # Show the original main canvas (home screen)
            self.original_main_canvas.pack(expand=True, fill="both")
        except ValueError as e:
            traceback.print_exc(e)
