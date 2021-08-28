#Módulos////////////////////////////////////////////////////////////////
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from ttkthemes import themed_tk as tkkk
import keyboard
import pygetwindow as win

#Ajustes Básicos de la ventana//////////////////////////////////////////
self = tkkk.ThemedTk()

self.wm_attributes("-topmost", 1)
self.set_theme("arc")

self.iconbitmap('icono.ico')
self.frame2 = ttk.Frame()
#///////////////////////////////////////////////////////////////////////
def bordevista():
    if seve.get() == 1:
        self.overrideredirect(True)
    elif seve.get() == 0:
        self.overrideredirect(False)
seve = tk.IntVar()
seve2 = tk.IntVar()
def menuvista():
    if seve2.get() == 1:
        self.menu5.destroy()
    elif seve2.get() == 0:
        self.configure(menu=self.menu5)

#Mantener activa la ventana donde se escribe////////////////////////////
if self.focus_get() != self.frame2:
  self.entry = win.getActiveWindow()

def checkfocus():
  self.entry = win.getActiveWindow()
  titulo = ''.join([win.getActiveWindow().title,'-MatematPad 0.01 WIP'])
  self.title(titulo)
  self.after(3000,checkfocus)

checkfocus()

def escribir(pal):
    self.entry.activate()
    keyboard.write(pal)
    self.frame2.focus()

#Botones////////////////////////////////////////////////////////////////

self.button11 = ttk.Button(self.frame2)
self.button11.grid(column='0', row='0')
self.button11.configure(text='Δ',command = lambda:escribir('Δ'))
self.button12 = ttk.Button(self.frame2)
self.button12.configure(text='δ',command = lambda:escribir('δ'))
self.button12.grid(column='1', row='0')
self.button13 = ttk.Button(self.frame2)
self.button13.configure(text='α',command = lambda:escribir('α'))
self.button13.grid(column='2', row='0')
self.button14 = ttk.Button(self.frame2)
self.button14.configure(text='λ',command = lambda:escribir('λ'))
self.button14.grid(column='3', row='0')
self.button15 = ttk.Button(self.frame2)
self.button15.configure(text='μ',command = lambda:escribir('μ'))
self.button15.grid(column='4', row='0')
self.button16 = ttk.Button(self.frame2)
self.button16.configure(text='ε',command = lambda:escribir('ε'))
self.button16.grid(column='5', row='0')
self.button17 = ttk.Button(self.frame2)
self.button17.configure(text='π',command = lambda:escribir('π'))
self.button17.grid(column='6', row='0')
self.button18 = ttk.Button(self.frame2)
self.button18.configure(text='β',command = lambda:escribir('β'))
self.button18.grid(column='0', row='1')
self.button19 = ttk.Button(self.frame2)
self.button19.configure(text='η',command = lambda:escribir('η'))
self.button19.grid(column='1', row='1')
self.button20 = ttk.Button(self.frame2)
self.button20.configure(text='Σ',command = lambda:escribir('Σ'))
self.button20.grid(column='2', row='1')
self.button21 = ttk.Button(self.frame2)
self.button21.configure(text='ρ',command = lambda:escribir('ρ'))
self.button21.grid(column='3', row='1')
self.button22 = ttk.Button(self.frame2)
self.button22.configure(text='φ',command = lambda:escribir('φ'))
self.button22.grid(column='4', row='1')
self.button23 = ttk.Button(self.frame2)
self.button23.configure(text='Φ',command = lambda:escribir('Φ'))
self.button23.grid(column='4', row='1')
self.button24 = ttk.Button(self.frame2)
self.button24.configure(text='Ω',command = lambda:escribir('Ω'))
self.button24.grid(column='5', row='1')
self.button25 = ttk.Button(self.frame2)
self.button25.configure(text='ω',command = lambda:escribir('ω'))
self.button25.grid(column='6', row='1')
self.button26 = ttk.Button(self.frame2)
self.button26.configure(text='θ',command = lambda:escribir('θ'))
self.button26.grid(column='0', row='2')
self.button27 = ttk.Button(self.frame2)
self.button27.configure(text='√',command = lambda:escribir('√'))
self.button27.grid(column='1', row='2')
self.button28 = ttk.Button(self.frame2)
self.button28.configure(text='σ',command = lambda:escribir('σ'))
self.button28.grid(column='2', row='2')
self.button29 = ttk.Button(self.frame2)
self.button29.configure(text='⁰',command = lambda:escribir('⁰'))
self.button29.grid(column='3', row='2')
self.button30 = ttk.Button(self.frame2)
self.button30.configure(text='¹',command = lambda:escribir('¹'))
self.button30.grid(column='4', row='2')
self.button31 = ttk.Button(self.frame2)
self.button31.configure(text='²',command = lambda:escribir('²'))
self.button31.grid(column='5', row='2')
self.button32 = ttk.Button(self.frame2)
self.button32.configure(text='ⁿ',command = lambda:escribir('ⁿ'))
self.button32.grid(column='6', row='2')
self.button33 = ttk.Button(self.frame2)
self.button33.configure(text='½',command = lambda:escribir('½'))
self.button33.grid(column='0', row='3')
self.button34 = ttk.Button(self.frame2)
self.button34.configure(text='¼',command = lambda:escribir('¼'))
self.button34.grid(column='1', row='3')
self.button35 = ttk.Button(self.frame2)
self.button35.configure(text='¾',command = lambda:escribir('¾'))
self.button35.grid(column='2', row='3')
self.button36 = ttk.Button(self.frame2)
self.button36.configure(text='₀',command = lambda:escribir('₀'))
self.button36.grid(column='3', row='3')
self.button37 = ttk.Button(self.frame2)
self.button37.configure(text='₁',command = lambda:escribir('₁'))
self.button37.grid(column='4', row='3')
self.button38 = ttk.Button(self.frame2)
self.button38.configure(text='₂',command = lambda:escribir('₂'))
self.button38.grid(column='5', row='3')
self.button39 = ttk.Button(self.frame2)
self.button39.configure(text='\\',command = lambda:escribir('\\'))
self.button39.grid(column='6', row='3')
self.button40 = ttk.Button(self.frame2)
self.button40.configure(text='·',command = lambda:escribir('·'))
self.button40.grid(column='0', row='4')
self.button41 = ttk.Button(self.frame2)
self.button41.configure(text='±',command = lambda:escribir('±'))
self.button41.grid(column='1', row='4')
self.button42 = ttk.Button(self.frame2)
self.button42.configure(text='^',command = lambda:escribir('^'))
self.button42.grid(column='2', row='4')
self.button43 = ttk.Button(self.frame2)
self.button43.configure(text='∞',command = lambda:escribir('∞'))
self.button43.grid(column='3', row='4')
self.button44 = ttk.Button(self.frame2)
self.button44.configure(text='≈',command = lambda:escribir('≈'))
self.button44.grid(column='4', row='4')
self.button45 = ttk.Button(self.frame2)
self.button45.configure(text='⌫',command = lambda:keyboard.send('Backspace'))
self.button45.grid(column='6', row='4')
self.frame2.configure(cursor='hand2', height='200', takefocus=True, width='200')
self.frame2.pack(side='top')

#-----------------------------------------------------------------------
def ayuda():
	messagebox.showinfo('Acerca de MatematPad','Ver. 0.01 WIP \nCreado por Ivan E. Ballester \n2021')
#Menu superior----------------------------------------------------------

self.menu5 = tk.Menu(self)
submenu5 = tk.Menu(self.menu5)
self.menu5.add(tk.CASCADE, menu=submenu5, label='Modo')
mi_themearc = 1
submenu5.add('radiobutton', label='Solo escribir')
mi_themebreeze = 2
submenu5.add('radiobutton', label='Escribir y copiar (No funciona aún)')

submenuver = tk.Menu(self.menu5)
self.menu5.add(tk.CASCADE, menu=submenuver, label='Ver')
mi_themearc = 1
submenuver.add('checkbutton', label='Barra de menú (No funciona aún)',variable=seve,command =lambda:menuvista())
mi_themebreeze = 2
submenuver.add('checkbutton', label='Borde',variable=seve,command=lambda:bordevista())

submenuthemes = tk.Menu(self.menu5)
self.menu5.add(tk.CASCADE, menu=submenuthemes, label='Tema')
mi_themearc = 1
submenuthemes.add('radiobutton', label='Arc',command =lambda:self.set_theme("arc"))
mi_themebreeze = 2
submenuthemes.add('radiobutton', label='Breeze',command =lambda:self.set_theme("breeze"))
mi_themeequilux = 3
submenuthemes.add('radiobutton', label='Equilux',command =lambda:self.set_theme("equilux"))
mi_themewin = 4
submenuthemes.add('radiobutton', label='Windows',command =lambda:self.set_theme('xpnative'))

submenuayuda = tk.Menu(self.menu5)
self.menu5.add(tk.CASCADE, menu=submenuayuda, label='Ayuda')
mi_themearc = 1
submenuayuda.add('command', label='Acerca de..',command =lambda:ayuda())

self.configure(menu=self.menu5)
self.configure(height='200', width='200')

#-----------------------------------------------------------------------

self.mainwindow = self.frame2
self.mainwindow.mainloop()


