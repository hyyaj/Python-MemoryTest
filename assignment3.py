from tkinter import *
from random import randint

# solution version 1: without extensions

def show_duo_names():
    print()
    print('┌─────────────────────┬───────────────────────┐')
    print('│ 0HV120 assignment 3 │ Memory Test           │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 1       │ name 1                │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 2       │ name 2                │')
    print('└─────────────────────┴───────────────────────┘')


class MemoryTestWindow:
    def __init__(self, root):
        self.window = root
        self.window.title("Memory Test")
        self.settings_frame = Frame(self.window)
        self.settings_frame.pack()
        self.status_info_lbl = Label(self.window)
        self.status_info_lbl.config(text='Click the Start button to start the memory test', font= 'Arial 20 bold')
        self.status_info_lbl.pack(anchor='center')
        self.canvas = Canvas(root)
        self.cwidth = 1200
        self.cheight = 700
        self.canvas.config(width = self.cwidth, height = self.cheight, bg = 'white')
        self.start_btn = Button(self.settings_frame)
        self.start_btn.config(text='Start', font='Arial 20 bold', command=self.start_pressed)
        self.start_btn.pack(side='left')
        self.invis_time_lbl = Label(self.settings_frame)
        self.invis_time_lbl.config(text='ms invisible:', font='Arial 20 bold')
        self.invis_time_lbl.pack(side='left')
        self.invis_time_ent = Entry(self.settings_frame)
        self.invis_time_ent.config(width=5, font='Arial 20 bold')
        self.invis_time_ent.pack(side='left')
        self.invis_time_ent.insert(0, '500')
        self.between_time_lbl = Label(self.settings_frame)
        self.between_time_lbl.config(text='ms between:', font='Arial 20 bold')
        self.between_time_lbl.pack(side='left')
        self.between_time_ent = Entry(self.settings_frame)
        self.between_time_ent.config(width=5, font='Arial 20 bold')
        self.between_time_ent.pack(side='left')
        self.between_time_ent.insert(0, '500')
        self.sequence_len_lbl = Label(self.settings_frame)
        self.sequence_len_lbl.config(text='sequence length:', font='Arial 20 bold')
        self.sequence_len_lbl.pack(side='left')
        self.sequence_len_ent = Entry(self.settings_frame)
        self.sequence_len_ent.config(width=5, font='Arial 20 bold')
        self.sequence_len_ent.pack(side='left')
        self.sequence_len_ent.insert(0, '3')
        self.square_size = 300
        self.coords_blue = [(self.cwidth / 2) - (self.square_size + 20), (self.cheight / 2) - (self.square_size + 20), (self.cwidth / 2) - 20, (self.cheight / 2) - 20]
        self.coords_yellow = [(self.cwidth / 2) + 20, (self.cheight / 2) + 20, (self.cwidth / 2) + (self.square_size + 20), (self.cheight / 2) + (self.square_size + 20)]
        self.coords_red = [(self.cwidth / 2) + 20, (self.cheight / 2) - (self.square_size + 20), (self.cwidth / 2) + (self.square_size + 20), (self.cheight/ 2) - 20]
        self.coords_green = [(self.cwidth / 2) - (self.square_size + 20) , (self.cheight / 2) + 20, (self.cwidth / 2) - 20, (self.cheight / 2) + (self.square_size + 20)]
        self.non_int = False
        self.levels_active = False
        self.dead = False
        self.level_counter = 1
        self.canvas.pack()
        self.settings_frame.pack(anchor = 's')
    def start_pressed(self):
        if (self.level_counter == 1 and self.levels_active != True) or (self.level_counter > 1 and self.levels_active == True):
            self.start_btn['state'] = DISABLED
            self.canvas.delete('all')
            self.status_info_lbl.config(text='Counting Down ...', font='Arial 20 bold')
            self.count_down_start()
        else:
            self.start_observation()
    def count_down_start(self):
        self.seconds_count = 3
        self.counting_dots = self.seconds_count * '.'
        self.canvas.create_text(self.cwidth / 2, self.cheight / 2, text=self.counting_dots, font='Arial 20 bold', tags= 'cd')
        self.seconds_count -= 1
        self.canvas.after(1000, self.count_down)
    def count_down(self):
        if self.seconds_count > 0:
            self.canvas.delete('cd')
            self.counting_dots = self.seconds_count * '.'
            self.canvas.create_text(self.cwidth / 2, self.cheight / 2, text=self.counting_dots, font='Arial 20 bold', tags='cd')
            self.seconds_count -= 1
            self.canvas.after(1000, self.count_down)
        else:
            self.canvas.delete('cd')
            self.start_observation()
    def draw_squares(self):
        self.canvas.create_rectangle((self.cwidth / 2) - (self.square_size + 20) , (self.cheight / 2) - (self.square_size + 20), (self.cwidth / 2) - 20, (self.cheight/ 2) - 20, fill='blue', tags= 'blue')
        self.canvas.create_rectangle((self.cwidth / 2) + 20, (self.cheight / 2) + 20, (self.cwidth / 2) + (self.square_size + 20), (self.cheight / 2) + (self.square_size + 20), fill='yellow', tags= 'yellow')
        self.canvas.create_rectangle((self.cwidth / 2) + 20, (self.cheight / 2) - 20, (self.cwidth / 2) + (self.square_size + 20), (self.cheight / 2) - (self.square_size + 20), fill='red', tags= 'red')
        self.canvas.create_rectangle((self.cwidth / 2) - 20, (self.cheight / 2) + 20, (self.cwidth / 2) - (self.square_size + 20), (self.cheight / 2) + (self.square_size + 20), fill='green', tags= 'green')
    def start_observation(self):
        self.draw_squares()
        self.status_info_lbl.config(text='Watch the sequence ...', font= 'Arial 20 bold')
        self.sequence_start()
    def sequence_start(self):
        if self.levels_active == False:
            try:
                self.sequence_len = int(self.sequence_len_ent.get())
                self.invis_time = int(self.invis_time_ent.get())
                self.between_time = int(self.between_time_ent.get())
            except ValueError:
                self.non_int = True
                self.clear_canvas()
                self.status_info_lbl.config(text='Please enter a number', font='Arial 20 bold')
                self.start_btn['state'] = NORMAL
        self.squares_lst = ['blue', 'yellow', 'red', 'green']
        self.sequence_id = []
        self.sequence_progress = self.sequence_len
        if self.sequence_len != 0 and self.non_int == False:
            self.canvas.after(self.between_time, self.to_click_indicator)
        elif self.non_int == False:
            self.start_levels()
    def to_click_indicator(self):
        self.square_to_remove = self.squares_lst[randint(0,3)]
        self.sequence_id.append(self.square_to_remove)
        self.canvas.delete(self.square_to_remove)
        self.canvas.after(self.invis_time, self.next_indicator)
        print(self.sequence_id)
    def next_indicator(self):
        self.draw_squares()
        self.sequence_progress -= 1
        if self.sequence_progress > 0:
            self.canvas.after(self.between_time, self.to_click_indicator)
        else:
            self.status_info_lbl.config(text= 'Repeat the sequence ...')
            self.clicked_squares_lst = []
            self.sequence_check_nr = []
            self.canvas.bind('<Button-1>', self.which_square_clicked)
    def which_square_clicked(self, event):
        if self.coords_blue[0] < event.x < self.coords_blue[2] and self.coords_blue[1] < event.y < self.coords_blue[3]:
            self.clicked_squares_lst.append('blue')
            self.canvas.delete('blue')
            self.sequence_check_nr.append(1)
            self.canvas.after(self.invis_time, self.check_sequence)
        elif self.coords_yellow[0] < event.x < self.coords_yellow[2] and self.coords_yellow[1] < event.y < self.coords_yellow[3]:
            self.clicked_squares_lst.append('yellow')
            self.canvas.delete('yellow')
            self.sequence_check_nr.append(1)
            self.canvas.after(self.invis_time, self.check_sequence)
        elif self.coords_red[0] < event.x < self.coords_red[2] and self.coords_red[1] < event.y < self.coords_red[3]:
            self.clicked_squares_lst.append('red')
            self.canvas.delete('red')
            self.sequence_check_nr.append(1)
            self.canvas.after(self.invis_time, self.check_sequence)
        elif self.coords_green[0] < event.x < self.coords_green[2] and self.coords_green[1] < event.y < self.coords_green[3]:
            self.clicked_squares_lst.append('green')
            self.canvas.delete('green')
            self.sequence_check_nr.append(1)
            self.canvas.after(self.invis_time, self.check_sequence)
    def check_sequence(self):
        self.sequence_progress_check = []
        self.draw_squares()
        for n in range(sum(self.sequence_check_nr)):
            self.sequence_progress_check.append(self.clicked_squares_lst[n])
        print(self.sequence_progress_check)
        if self.sequence_progress_check == self.sequence_id:
            self.canvas.after(self.invis_time, self.user_results_pos)
        elif self.sequence_progress_check[-1] != self.sequence_id[n]:
            print(self.sequence_id)
            self.canvas.after(self.invis_time, self.user_results_neg())
    def user_results_pos(self):
        self.canvas.delete('all')
        self.canvas.create_text(self.cwidth / 2, self.cheight / 2, text='The sequence was correct!', font='Arial 20 bold')
        self.status_info_lbl.config(text='Click the Start button to start a sequence', font='Arial 20 bold')
        self.start_btn['state'] = NORMAL
        self.dead = False
        if self.levels_active == True:
            self.check_dead()
    def user_results_neg(self):
        print('user_results_neg has been called')
        self.canvas.delete('all')
        if self.levels_active == False:
            self.canvas.create_text(self.cwidth / 2, self.cheight / 2, text='The sequence was incorrect ...', font='Arial 20 bold')
        self.status_info_lbl.config(text='Click the Start button to start a sequence', font='Arial 20 bold')
        self.start_btn['state'] = NORMAL
        self.dead = True
        if self.levels_active == True:
            self.check_dead()
    def start_levels(self):
        if self.level_counter == 1:
            self.sequence_len = 1
        self.levels_active = True
        print('start_levels has been called')
        if self.level_counter == 1:
            self.canvas.after(self.between_time, self.start_pressed)
        elif self.level_counter > 1:
            self.canvas.after(2000, self.start_pressed)
    def check_dead(self):
        if self.dead == False:
            self.level_counter += 1
            self.start_levels()
            self.sequence_len += 1
        elif self.dead == True:
            self.canvas.delete('all')
            print('finished')
            self.canvas.create_text(self.cwidth / 2, self.cheight / 2, text='You ended with a sequence of '+str(self.level_counter), font='Arial 20 bold')
            self.canvas.after(2000, self.clear_canvas)
            self.levels_active = False
    def clear_canvas(self):
        self.canvas.delete('all')


        return  # replace with you code

def main():
    show_duo_names()

    root = Tk()
    window = MemoryTestWindow(root)
    root.mainloop()

main()
