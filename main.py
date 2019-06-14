
# family = The font family name as a string.
# size = The font height as an integer in points. To get a font n pixels high, use -n.
# weight = 'bold' for boldface, 'normal' for regular weight
# slant = 'italic' for italic, 'roman' for unslanted.
# underline = 1 for underlined text, 0 for normal
# overstrike = 1 for overstruck text, 0 for normal


from tkinter import *
from tkinter.font import Font
import keyboard
from tkinter import messagebox
from time import sleep

Key = keyboard.Key
keyboard = keyboard.Controller()

FONTS = sorted(['System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts', 'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Batang', '@Batang', 'BatangChe', '@BatangChe', 'Gungsuh', '@Gungsuh', 'GungsuhChe', '@GungsuhChe', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'DaunPenh', 'DokChampa', 'Estrangelo Edessa', 'Euphemia', 'Gautami', 'Vani', 'Gulim', '@Gulim', 'GulimChe', '@GulimChe', 'Dotum', '@Dotum', 'DotumChe', '@DotumChe', 'Impact', 'Iskoola Pota', 'Kalinga', 'Kartika', 'Khmer UI', 'Lao UI', 'Latha', 'Lucida Console', 'Malgun Gothic', '@Malgun Gothic', 'Mangal', 'Meiryo', '@Meiryo', 'Meiryo UI', '@Meiryo UI', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft YaHei', '@Microsoft YaHei', 'MingLiU', '@MingLiU', 'PMingLiU', '@PMingLiU', 'MingLiU_HKSCS', '@MingLiU_HKSCS', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS PGothic', '@MS PGothic', 'MS UI Gothic', '@MS UI Gothic', 'MS Mincho', '@MS Mincho', 'MS PMincho', '@MS PMincho', 'MV Boli', 'Microsoft New Tai Lue', 'Nyala', 'Microsoft PhagsPa', 'Plantagenet Cherokee', 'Raavi', 'Segoe Script', 'Segoe UI', 'Segoe UI Semibold', 'Segoe UI Light', 'Segoe UI Symbol', 'Shruti', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sylfaen', 'Microsoft Tai Le', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Tunga', 'Vrinda', 'Shonar Bangla', 'Microsoft Yi Baiti', 'Tahoma', 'Microsoft Sans Serif', 'Angsana New', 'Aparajita', 'Cordia New', 'Ebrima', 'Gisha', 'Kokila', 'Leelawadee', 'Microsoft Uighur', 'MoolBoran', 'Symbol', 'Utsaah', 'Vijaya', 'Wingdings', 'Andalus', 'Arabic Typesetting', 'Simplified Arabic', 'Simplified Arabic Fixed', 'Sakkal Majalla', 'Traditional Arabic', 'Aharoni', 'David', 'FrankRuehl', 'Levenim MT', 'Miriam', 'Miriam Fixed', 'Narkisim', 'Rod', 'FangSong', '@FangSong', 'SimHei', '@SimHei', 'KaiTi', '@KaiTi', 'AngsanaUPC', 'Browallia New', 'BrowalliaUPC', 'CordiaUPC', 'DilleniaUPC', 'EucrosiaUPC', 'FreesiaUPC', 'IrisUPC', 'JasmineUPC', 'KodchiangUPC', 'LilyUPC', 'DFKai-SB', '@DFKai-SB', 'Lucida Sans Unicode', 'Arial Black', 'Calibri', 'Cambria', 'Cambria Math', 'Candara', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Franklin Gothic Medium', 'Gabriola', 'Georgia', 'Palatino Linotype', 'Segoe Print', 'Trebuchet MS', 'Verdana', 'Webdings', 'Calibri Light', 'Noto Sans', 'Bowlby One SC', 'Cabin Sketch', 'Cookie', 'Doppio One', 'Courgette', 'Dead Kansas', 'Euphorigenic', 'Great Vibes', 'Kalam Light', 'Kalam', 'Lemon', 'Limelight', 'Megrim', 'Montserrat Subrayada', 'Permanent Marker', 'Russo One', 'Sigmar One', 'Yellowtail', 'Bungee Inline', 'Cinzel Black', 'Marcellus SC', 'Quicksand Light', 'Quicksand Medium', 'Quicksand', 'Ubuntu Mono', 'Fugaz One', 'Shrikhand', 'Playball', 'Arial Unicode MS', '@Arial Unicode MS', 'Century', 'Wingdings 2', 'Wingdings 3', 'Book Antiqua', 'Century Gothic', 'Arial Narrow', 'Bookman Old Style', 'Garamond', 'Segoe WP', 'Segoe WP Black', 'Segoe WP Light', 'Segoe WP Semibold', 'Segoe WP SemiLight'])
SIZE = "600x600+60+70"
FONTSIZE = (12)
TEXT = """\n<ASCII/Latin1>\nAaBbCcDdEeFfGgHhIiJj\n1234567890#:+=(){}[]\n¢£¥§©«®¶½ĞÀÁÂÃÄÅÇÐØß\n\n<IPA,Greek,Cyrillic>\nɐɕɘɞɟɤɫɮɰɷɻʁʃʆʎʞʢʫʭʯ\nΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκ\nБбДдЖжПпФфЧчЪъЭэѠѤѬӜ\n<Hebrew, Arabic>\n אבגדהוזחטיךכלםמןנסעף\n ابجدهوزحطي٠١٢٣٤٥٦٧٨٩\n\n<Devanagari, Tamil>\n०१२३४५६७८९अआइईउऊएऐओऔ\n௦௧௨௩௪௫௬௭௮௯அஇஉஎ\n\n<East Asian>\n〇一二三四五六七八九\n汉字漢字人木火土金水\n가냐더려모뵤수유즈치\nあいうえおアイウエオ\n"""
TEXTFONT = ["Terminal", 12, "normal", "roman"]
FONTVALUES = [7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 22, 25, 29, 34, 40, 50, 55, 60, 65]

    
def translate(side="w", percentage=None):

    side = side.upper()
    
    w = int(SIZE.split("x")[0])
    h = int(SIZE.split("x")[1].split("+")[0])

    if side == "W":
        rtnSize = (percentage * w) / 100
        return int(rtnSize)
    elif side == "H":
        rtnSize = (percentage * h) / 100
        return int(rtnSize)


def main():

    global listVar, resultsEnt

    def getResults(event):

        pass

    def makeFontSampleFrame(parent):

        global text

        canvas = Canvas(parent, bg="red", width=translate("w", 40))
        canvas.grid_rowconfigure(0, weight=1)

        text = Text(canvas, wrap=CHAR, width=translate("w", 50))
        text.insert(0.1, TEXT)
        text.configure(font=TEXTFONT)
        text.grid(sticky="nsew", padx=5, pady=5)

        return canvas
    
    def makeControlsFrame(parent):

        global resultsEnt

        def changeSpin():

            spinSize = sizeSpinbox.get()            
            TEXTFONT[1] = spinSize
            
            resultsEnt.delete(0, END)
            resultsEnt.insert(END, str(tuple(TEXTFONT)))
            text.configure(font=TEXTFONT)
        
        def changeBold():

            weight = boldCheckVar.get() 
            
            if weight == 1:
                weight="bold"
            elif weight == 0:
                weight = "normal"

            TEXTFONT[2] = weight
            
            resultsEnt.delete(0, END)
            resultsEnt.insert(END, str(tuple(TEXTFONT)))
            text.configure(font=TEXTFONT)


            # print(weight)

        def changeItalic():

            slant = italicCheckVar.get() 
            
            if slant == 1:
                slant="italic"
            elif slant == 0:
                slant = "roman"

            TEXTFONT[3] = slant
            
            resultsEnt.delete(0, END)
            resultsEnt.insert(END, str(tuple(TEXTFONT)))
            text.configure(font=TEXTFONT)

        def changeFontName(event):

            try:
                curItem = fontListbx.curselection()
                selectedFontName = fontListbx.get(curItem)
                # print(selectedFontName)

                TEXTFONT[0] = selectedFontName
            
                resultsEnt.delete(0, END)
                resultsEnt.insert(END, str(tuple(TEXTFONT)))
                resultsEnt.select_range(0, END)
                text.configure(font=TEXTFONT)

            except:
                pass

        def copyIT():

            rest = resultsEnt.get()
            resultsEnt.focus_get()

            if rest != None:

                keyboard.press(Key.ctrl)
                keyboard.press("c")
                keyboard.release(Key.ctrl)
                keyboard.release("c")
                
                # messagebox.showinfo("INFO", "{} Copied To Clipboard".format(rest))

            # print(rest)

        canvas = Canvas(parent, bg="white")

        lblFrm = LabelFrame(canvas, text="Font Name", bg="white", bd=3, font=FONTSIZE)
        lblFrm.pack(fill=X, anchor="n", padx=5, pady=10)

        lable1 = Label(lblFrm, text="Font Face:", font=FONTSIZE)
        lable1.pack(anchor="sw", padx=3)

        fontListbx = Listbox(lblFrm, width=translate("w", 6), height=20, listvariable=listVar)
        fontListbx.bind("<Button-1>", changeFontName) # bind mouse click
        fontListbx.bind("<Button-2>", changeFontName) # bind mouse click
        fontListbx.bind("<Double-Button-1>", changeFontName) # bind mouse click
        fontListbx.bind("<KeyPress-Up>", changeFontName) # bind keypress up
        fontListbx.bind("<KeyPress-Down>", changeFontName) # bind keypress up
        fontListbx.pack(fill=X, padx=5, pady=5)

        for font in FONTS:
            fontListbx.insert(END, font)

        fm2 = Frame(canvas)
        # frame1
        lable2 = Label(fm2, text="Size: ", font=FONTSIZE)
        lable2.pack(side=LEFT, pady=2, anchor="w")

        sizeSpinbox = Spinbox(fm2, values=FONTVALUES, width=7, command=changeSpin, textvariable=spinVar)
        spinVar.set(12)
        sizeSpinbox.pack(side=LEFT, pady=5)

        lable3 = Label(fm2, text="Bold", font=FONTSIZE)
        lable3.pack(side=LEFT, padx=5)

        boldCheck = Checkbutton(fm2, variable=boldCheckVar, command=changeBold)
        boldCheck.pack(side=LEFT)
        fm2.pack(side=TOP, padx=5, fill=X, pady=10)

        lable6 = Label(fm2, text="Italic", font=FONTSIZE)
        lable6.pack(side=LEFT, padx=5)

        boldCheck2 = Checkbutton(fm2, variable=italicCheckVar, command=changeItalic)
        boldCheck2.pack(side=LEFT)
        fm2.pack(side=TOP, padx=5, fill=X, pady=10)

        fm = Frame(canvas)
        # frame 2
        lable4 = Label(fm, text="Results : ", font=FONTSIZE)
        lable4.pack(side=TOP, anchor=W)

        resultsEnt = Entry(fm, font=12, textvariable=entryVar)
        entryVar.set(None)
        resultsEnt.pack(side=TOP, anchor=W, fill=X, padx=2, pady=2)
        fm.pack(side=TOP, padx=5, fill=X, pady=15)

        fm3 = Frame(canvas)
        # frame 3
        copyButton = Button(fm3, text="COPY To ClipBoard", bd=3, relief=RAISED, command=copyIT)
        copyButton.pack(padx=2, pady=3)
        fm3.pack(side=TOP, padx=5, fill=X, pady=7)

        return canvas

    root = Tk()
    root.geometry(SIZE)
    root.title("Font Choozer")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.bind("<KeyPress-Return>", getResults)

    listVar = StringVar()
    boldCheckVar = IntVar()
    italicCheckVar = IntVar()
    spinVar = IntVar()
    entryVar = StringVar()

    pane = PanedWindow(orient=HORIZONTAL, sashwidth=0, sashrelief=FLAT, bg='#ddd')
    pane.add(makeControlsFrame(pane))
    pane.add(makeFontSampleFrame(pane))
    pane.grid(row=0, sticky='news')

    root.mainloop()

if __name__ == "__main__":
    
    main()