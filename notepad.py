from tkinter import *
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_wd = Tk()

main_wd.title("Note-pad editor")
main_wd.geometry('700x500')
main_wd.wm_iconbitmap('icon.ico')

############################################################## main menu  #################################################

main_menu = Menu(main_wd)

# file icon

new_icon = PhotoImage(file='icons2/new.png')
open_icon = PhotoImage(file='icons2/open.png')
save_icon = PhotoImage(file='icons2/save.png')
save_as_icon = PhotoImage(file='icons2/save_as.png')
exit_icon = PhotoImage(file='icons2/exit.png')


# file menu
fileM = Menu(main_menu, tearoff=0)

# edit icons
copy_icon = PhotoImage(file='icons2/copy.png')
paste_icon = PhotoImage(file='icons2/paste.png')
clear_all_icon = PhotoImage(file='icons2/clear_all.png')
cut_icon = PhotoImage(file='icons2/cut.png')
find_icon = PhotoImage(file='icons2/find.png')
case_icon = PhotoImage(file='icons2/caseicon.png')

# etit menu
edit = Menu(main_menu, tearoff=0)


# view icons
tool_bar_icon = PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = PhotoImage(file='icons2/status_bar.png')


# view menu
view = Menu(main_menu, tearoff=0)

# color them icons
light_default_icon = PhotoImage(file='icons2/light_default.png')
light_plus_icon = PhotoImage(file='icons2/light_plus.png')
dark_icon = PhotoImage(file='icons2/dark.png')
red_icon = PhotoImage(file='icons2/red.png')
monokai_icon = PhotoImage(file='icons2/monokai.png')
night_blue_icon = PhotoImage(file='icons2/night_blue.png')

# color them menu
color_them = Menu(main_menu, tearoff=0)

theme_choice = StringVar()

color_icons = (light_default_icon, light_plus_icon, dark_icon,
               red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#ffffff', '#FFA500'),
    'Night Blue': ('#008000', '#000000')
}


# cascade
main_menu.add_cascade(label='file', menu=fileM)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color them', menu=color_them)


# ------------------------------------------------------------ End main menu -----------------------------------------------


############################################################## toolbar  #################################################
tool_bar = ttk.Label(main_wd)
tool_bar.pack(side=TOP, fill=X)

font_tuple = font.families()

# font box

font_family = StringVar()
font_box = ttk.Combobox(
    tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.grid(row=0, column=0, padx=5)
font_box.current(3)


# font size

size_var = IntVar()
font_size = ttk.Combobox(
    tool_bar, width=15, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8, 81, 2))
font_size.current(1)
font_size.grid(row=0, column=1, padx=5)


# bold button
bold_icon = PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# italic button
italic_icon = PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# underline button
underline_icon = PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# font color button
font_color_icon = PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# align left
align_left_icon = PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# align center
align_center_icon = PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

# align right
align_right_icon = PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

# ------------------------------------------------------------ End toolbar -----------------------------------------------


############################################################## text editor  #######################################

text_editor = Text(main_wd)
text_editor.config(wrap='word', relief=FLAT)

text_editor.focus_set()
scroll_bar = Scrollbar(main_wd)
scroll_bar.pack(side=RIGHT, fill=Y)
text_editor.pack(fill=BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

current_font_family = 'Arial'
current_font_size = 10


def change_font(value):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.config(font=(current_font_family, current_font_size))


def change_fontsize(value):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.config(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

# button functionality

# bolt functionality


def change_bold():
    text_property = font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.config(
            font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.config(
            font=(current_font_family, current_font_size, 'normal'))


bold_btn.config(command=change_bold)


# itelic functionality
def change_itelic():
    text_property = font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.config(
            font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.config(
            font=(current_font_family, current_font_size, 'roman'))


italic_btn.config(command=change_itelic)


# underline functionality
def change_underline():
    text_property = font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.config(
            font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.config(
            font=(current_font_family, current_font_size, 'normal'))


underline_btn.config(command=change_underline)

# font color functionality


def chenge_font_color():
    color_var = colorchooser.askcolor()
    text_editor.config(fg=color_var[1])


font_color_btn.config(command=chenge_font_color)

# aline functionality


def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=LEFT)
    text_editor.delete(1.0, END)
    text_editor.insert(INSERT, text_content, 'left')


align_left_btn.configure(command=align_left)

# center


def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=CENTER)
    text_editor.delete(1.0, END)
    text_editor.insert(INSERT, text_content, 'center')


align_center_btn.configure(command=align_center)

# right


def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=RIGHT)
    text_editor.delete(1.0, END)
    text_editor.insert(INSERT, text_content, 'right')


align_right_btn.configure(command=align_right)

text_editor.config(font=('Arial', 10))


# ------------------------------------------------------------ End text editor -------------------------------------


############################################################## main main status bar  ###############################

status_bar = ttk.Label(main_wd, text='Status bar')
status_bar.pack(side=BOTTOM)

text_changed=False
def chenged(event=None):
    global text_changed

    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c').replace(' ', ''))
        status_bar.config(text=f'Characters : {characters} words : {words}')
    text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', chenged)
# status_bar.config(command=chenged)
# ------------------------------------------------------------ End main main status bar -------------------------------------


############################################################## main main functionility  ###################################
# file submenu comands
# variable
url = ''


def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, END)

# submenu


fileM.add_command(label='New', image=new_icon,
                  compound=LEFT, accelerator='ctr+N', command=new_file)


# oppen functionality


def oppen_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', file=((
        ('all file', '*.*'), ("Text Documents", "*.txt"))))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, END)
            text_editor.insert(1.0, fr.read())

            main_wd.title(os.path.basename(url))
    except FileNotFoundError:
        return

    except:
        return main_wd.title(os.path.basename(url))


fileM.add_command(label='Open', image=open_icon,
                  compound=LEFT, accelerator='ctr+O', command=oppen_file)


# save fungtionality
def save_file(event=None):
    global url
    try:

        if url:
            content = str(text_editor.get(1.0, END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', file=(
                ('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, END)
            url.write(content2)
            url.close()
    except:
        return


fileM.add_command(label='Save', image=save_icon,
                  compound=LEFT, accelerator='ctr+S', command=save_file)


# save as functionality

def save_as(event=None):
    global url
    try:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', file=(
            ('Text File', '*.txt'), ('All files', '*.*')))
        content2 = text_editor.get(1.0, END)
        url.write(content2)
        url.close()

    except:
        return


fileM.add_command(label='Save as', image=save_as_icon,
                  compound=LEFT, accelerator='ctr+AS', command=save_as)


# exit file functionalty
# text_changed = False


def exit_file(event=None):
    global url, text_changed

    try:
        if text_changed is True:
            mb = messagebox.askyesnocancel('Allert', 'Do you want to save the file')
            if mb is True:
                if url:
                    content = text_editor.get(1.0, END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_wd.destroy()

                else:
                    content2 = str(text_editor.get(1.0, END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', file=(
                        ('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_wd.destroy()

            elif mb is False:
                main_wd.destroy()
        else:
            main_wd.destroy()
    except:
        return


fileM.add_separator()
fileM.add_command(label='Exit', image=exit_icon,
                  compound=LEFT, accelerator='ctr+Q', command=exit_file)


# edit submenu comands


# submenu

# copy functionality 




edit.add_command(label='Copy', image=copy_icon,
                 compound=LEFT, accelerator='ctr+C', command=lambda:text_editor.event_generate("<<Copy>>"))

# Past functionality 


edit.add_command(label='Paste', image=paste_icon,
                 compound=LEFT, accelerator='ctr+P', command=lambda:text_editor.event_generate("<<Paste>>"))
edit.add_separator()

# Cut functionality 



edit.add_command(label='Cut', image=cut_icon,
                 compound=LEFT, accelerator='ctr++Alt+t',command=lambda:text_editor.event_generate("<<Cut>>"))



# Clear all functionality


edit.add_command(label='Clear_all', image=clear_all_icon,
                 compound=LEFT, accelerator='ctr+A',command=lambda :text_editor.delete(1.0,END))

# Fontcase submenu 

font_case = Menu(edit,tearoff=0)

def upper_case():
    content = text_editor.get("1.0",END)
    new_content = content.upper()
    text_editor.delete(1.0,END)
    text_editor.insert(1.0,new_content)

def lover_case():
    content = text_editor.get("1.0",END)
    new_content = content.lower()
    text_editor.delete(1.0,END)
    text_editor.insert(1.0,new_content)

def title_case():
    content = text_editor.get("1.0",END)
    new_content = content.title()
    text_editor.delete(1.0,END)
    text_editor.insert(1.0,new_content)



font_case.add_command(label="Uppercase",command=upper_case)
font_case.add_command(label="lovercase",command=lover_case)
font_case.add_command(label="Titlecase",command=title_case)




edit.add_cascade(label='Fontcase',image=case_icon,compound=LEFT,accelerator='Alt+u',menu=font_case)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# find functionality

def find_txt(event=None):
    find_wd = Toplevel()
    find_wd.geometry('500x200')
    find_wd.title('Find/Replace')
    find_wd.resizable(0,0)

    def find():
        word = find_ipt.get()
        text_editor.tag_remove('match','1.0',END)
        matches=0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos,stopindex=END)
                if not start_pos:
                    break

                end_pos = f'{start_pos}+{len(word)}c'

                text_editor.tag_add('match', start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red',background='yellow')


    def replace():
        word = find_ipt.get()
        replace_txt = replace_ipt.get()
        content = text_editor.get(1.0,END)
        new_content = content.replace(word,replace_txt)
        text_editor.delete(1.0,END)
        text_editor.insert(1.0,new_content)




    # frame 
    find_f = ttk.LabelFrame(find_wd,text='Find/Replace')
    find_f.pack(pady=20)


    text_f_l = ttk.Label(find_f,text='find : ')
    text_r_l = ttk.Label(find_f,text='Replace : ')

    # Entry
    find_ipt= ttk.Entry(find_f,width=30)
    replace_ipt = ttk.Entry(find_f,width=30)

    # button 

    find_b = ttk.Button(find_f,text='Find',command=find)
    replace_b = ttk.Button(find_f,text='Replace',command=replace)
    

    # packing

    text_f_l.grid(row=0,column=0,padx=1,pady=4)
    text_r_l.grid(row=1,column=0,padx=1,pady=4)


    # enty pack
    find_ipt.grid(row=0,column=1,padx=1,pady=4)
    replace_ipt.grid(row=1,column=1,padx=1,pady=4)

    # btn pack
    find_b.grid(row=2,column=0,padx=1,pady=4)
    replace_b.grid(row=2,column=1,padx=1,pady=4)


    find_wd.mainloop()


edit.add_command(label='Find', image=find_icon,
                 compound=LEFT, accelerator='ctr+A',command=find_txt)

# view submenu comands

# view functionality 

# show_statusbar = BooleanVar()
# show_statusbar.set(True)
# show_toolbar = BooleanVar()
# show_toolbar.set(True)

show_statusbar = True
show_toolbar = True

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()

        # status_bar.pack_forget()

        tool_bar.pack(sid=TOP,fill=X)
        text_editor.pack(fill=BOTH,expand=True)

        # status_bar.pack(side=BOTTOM)

        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=BOTTOM)
        show_statusbar=True
        
view.add_checkbutton(label='Status bar', image=status_bar_icon, compound=LEFT, onvalue=True, offvalue=False,variable=show_statusbar,command=hide_statusbar)
view.add_checkbutton(label='Tool bar', image=tool_bar_icon, compound=LEFT, onvalue=True, offvalue=False,variable=show_toolbar,command=hide_toolbar)


# color them submenu comands

# color_them functionality 
def change_them():
    color_them = theme_choice.get()
    color_tuble = color_dict.get(color_them)
    fg_color,bg_color = color_tuble[0],color_tuble[1]
    text_editor.config(background=bg_color,fg=fg_color)

count = 0
for i in color_dict:
    color_them.add_radiobutton(
        label=i, image=color_icons[count], compound=LEFT, variable=theme_choice,command=change_them)
    count += 1


# ------------------------------------------------------------ End main manu functionility ------------------------------


main_wd.config(menu=main_menu)

#### bind shortcut keys 
main_wd.bind("<Control-n>", new_file)
main_wd.bind("<Control-o>", oppen_file)
main_wd.bind("<Control-s>", save_file)
main_wd.bind("<Control-Alt-s>", save_as)
main_wd.bind("<Control-q>", exit_file)
main_wd.bind("<Control-f>", find_txt)

main_wd.mainloop()
