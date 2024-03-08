from tkinter import CENTER, ttk
import tkinter as tk
import math
#things considered by program when calculating damage
single = False
double = False
totalDamage = 100
buffs = []
cleanup_list = []
saved_entries = []
global gear_damage
gear_damage = 0
damageMath = ''
#asks for spell damage
def block_text(e):
   enemy_block.delete(0, "end")
def crit_text(e):
   critical_level.delete(0, "end")
def crit_rate_text(e):
   critical_chance.delete(0, "end")

def cleanupScreen():
   while len(cleanup_list) > 0:
      delete_this = cleanup_list[-1]
      delete_this.place_forget()
      cleanup_list.pop(-1)

def damageType():
   cleanupScreen()
   global single
   global double
   if single != False:
      single = False
   if double != False:
      double = False
   global damage_request
   global single_damage
   global damage_range
   create_new.pack_forget()
   damage_request = ttk.Label (
      window, text="""     What kind of damage 
      does this spell do?""", font= ("Arial", 25)
   )
   damage_request.place(relx=0.5, rely=0.3, anchor=CENTER)
   single_damage = ttk.Button(window, text="Definite Damage (ex. 335)", command=one)
   damage_range = ttk.Button(window, text="Damage Range (ex. 245-305)", command=two)
   single_damage.place(relx=0.3, y=500)
   damage_range.place(relx=0.6, y=500)

   #clean up stuff
   cleanup_list.append(damage_request)
   cleanup_list.append(single_damage)
   cleanup_list.append(damage_range)

def one():
   global single
   single = True
   spellDamageRequest()
def two():
   global double
   double = True
   spellDamageRequest()

def spellDamageRequest():
    cleanupScreen()
    global damage_high
    global damage_low
    global spell_damage_high
    global spell_damage_low
    global spell_damage_text
    global submit
    global gear_damage
    global gear_damage_text
    global attack_gear
    if gear_damage == 0:
      attack_gear = tk.IntVar()
      gear_damage_text = ttk.Label(window, text="Enter your gear damage", font=("Arial", 25))
      gear_damage_text.place(relx=0.5, y=100, anchor=CENTER)
      gear_damage = ttk.Entry(window, textvariable=attack_gear,
      font=("calibre",10), justify=CENTER)
      gear_damage.place(relx=0.45, y=150)
    damage_high = tk.IntVar()
    spell_damage_high = ttk.Entry(window, textvariable=damage_high, 
    font=("calibre",10), justify=CENTER)
    spell_damage_text = ttk.Label(window, text="Enter spell damage below (with damage buffs)", font=("Arial", 25))
    spell_damage_text.place(relx=0.55, y=250, anchor=CENTER)
    if double == True:
        print("a")
        damage_low = tk.IntVar()
        spell_damage_high.place(relx=0.2, y=500)
        spell_damage_low = ttk.Entry(window, textvariable=damage_low,
        font=("calibre",10), justify=CENTER)
        spell_damage_low.place(relx=0.7, y=500)
    else:
       spell_damage_high.place(relx=0.42, y=500)
    submit = ttk.Button(window, text="Submit", command=saveHighDamage)
    submit.place(x=550, y=700)

    #clean up process
    cleanup_list.append(gear_damage_text)
    cleanup_list.append(gear_damage)
    cleanup_list.append(spell_damage_high)
    cleanup_list.append(spell_damage_text)
    cleanup_list.append(submit)

def saveHighDamage():
   #getting the gear damage and multiplying it to spell damage
   #comes before all other math
   global gear_hurt
   global damageMath
   global chance_to_crit
   if damageMath != '':
      damageMath = ''
   chance_to_crit = ''
   gear_hurt = gear_damage.get()
   gear_hurt = int(gear_hurt)
   global totalDamage
   damage_high = spell_damage_high.get()
   if not damage_high in saved_entries and single == True:
      saved_entries.append(damage_high)
      print(saved_entries)
   totalDamage = int(damage_high)
   totalDamage = math.floor(totalDamage * ((gear_hurt/100) + 1))
   #if there's a range of damage the spell does, this happens
   if double == True:
      global totalDamageTwo
      damage_low = spell_damage_low.get()
      damage_double = str(damage_high) + '-' + str(damage_low)
      print(damage_double)
      if not damage_double in saved_entries:
         saved_entries.append(damage_double)
         print(saved_entries)
      totalDamageTwo = int(damage_low)
      totalDamageTwo = math.floor(totalDamageTwo * ((gear_hurt/100) + 1))
   buffChart()

def buffChart():
   cleanupScreen()
   #making them all global for looping the program
   global spell_damage
   global blade
   global sharpened_blade
   global trap
   global potent_trap
   global feint
   global weakness
   global tower_shield
   global reset_to_spell_type
   global boost
   global boost_amount
   global boost_submit
   global aura
   global aura_amount
   global aura_submit
   global critical_level
   global critical_chance
   global critical_rating
   global player_level
   global critical_submit
   global enemy_block
   global block_amount
   global reset_damage
   global current_math
   global damageMath
   global damage_with_crit_text
   global damage_with_crit
   #adds the lower end of spell damage in if the spell has a range of damage
   if double == True:
      global low_spell_damage
      spell_damage_low.place_forget()
      low_spell_damage = ttk.Label(window, text=totalDamageTwo, font=("calibre", 20), justify=CENTER)
      low_spell_damage.place(relx=0.7, y=700)
      cleanup_list.append(low_spell_damage)
   #all the buttons and commands to calculate damage
   boost_amount = tk.IntVar()
   aura_amount = tk.IntVar()
   player_level = tk.IntVar()
   block_amount = tk.IntVar()
   critical_rating = tk.IntVar()
   spell_damage = ttk.Label(window, text=totalDamage, font=("calibre", 20), justify=CENTER)
   if chance_to_crit != '':
      damage_with_crit_text = ttk.Label(window, text="Damage if critical (Chance: " + chance_to_crit + ")", font=("calibre", 16), justify=CENTER)
      damage_with_crit = ttk.Label(window, text=totalDamage*2, font=("calibre", 20), justify=CENTER)
      damage_with_crit_text.place(relx=0.4, y=750)
      damage_with_crit.place(relx=0.5, y=775)
      cleanup_list.append(damage_with_crit)
      cleanup_list.append(damage_with_crit_text)
   current_math = ttk.Label(window, text=damageMath, font=("calibre", 16), justify=CENTER)
   blade = ttk.Button(window, text="Blade", command=blade_increase)
   sharpened_blade = ttk.Button(window, text="Sharp Blade", command=s_blade_increase)
   bal_blade = ttk.Button(window, text="Balance Blade", command=b_blade)
   bubble = ttk.Button(window, text="Bubble", command=global_effect)
   weakness = ttk.Button(window, text="Weakness", command=weakness_decrease)
   tower_shield = ttk.Button(window, text="Tower Shield", command=shield_decrease)
   trap = ttk.Button(window, text="Trap", command=trap_increase)
   potent_trap = ttk.Button(window, text="Potent Trap", command=p_trap_increase)
   feint = ttk.Button(window, text="Feint", command=feint_increase)
   boost = ttk.Entry(window, textvariable=boost_amount, font=("calibre",10), justify=CENTER)
   boost_submit = ttk.Button(window, text="Submit Boost Amount", command=calculateBoost)
   aura = ttk.Entry(window, textvariable=aura_amount, font=("calibre", 10), justify=CENTER)
   aura_submit = ttk.Button(window, text="Submit Aura Amount", command=aura_increase)
   critical_level = ttk.Entry(window, textvariable=player_level, font=("calibre", 10), justify=CENTER)
   critical_level.insert(0, "Input Level")
   critical_level.bind("<FocusIn>", crit_text)
   critical_chance = ttk.Entry(window, textvariable=critical_rating, font=("calibre", 10), justify=CENTER)
   critical_chance.insert(0, "Input Crit Rating")
   critical_chance.bind("<FocusIn>", crit_rate_text)
   critical_submit = ttk.Button(window, text="Submit Crit Math", command=criticalMath)
   enemy_block = ttk.Entry(window, textvariable=block_amount, font=("calibre", 10), justify=CENTER)
   enemy_block.insert(0, "Input Enemy Block")
   enemy_block.bind("<FocusIn>", block_text)
   reset_damage = ttk.Button(window, text="Reset Damage", command=saveHighDamage)
   reset_to_spell_type = ttk.Button(window, text="Back To Start", command=damageType)

   #placing all of them
   reset_to_spell_type.place(relx=0.9, y=600)
   reset_damage.place(relx=0.2, y=600)
   spell_damage.place(relx=0.5, y=700)
   blade.place(relx=0.2, y=100)
   sharpened_blade.place(relx=0.2, y=150)
   bal_blade.place(relx=0.2, y=200)
   bubble.place(relx=0.2, y=250)
   weakness.place(relx=0.5, y=100)
   tower_shield.place(relx=0.5, y=150)
   trap.place(relx=0.8, y=100)
   potent_trap.place(relx=0.8, y=150)
   feint.place(relx=0.8, y=200)
   boost.place(relx=0.2, y=300)
   boost_submit.place(relx=0.2, y=350)
   aura.place(relx=0.8, y=300)
   aura_submit.place(relx=0.8, y=350)
   critical_chance.place(relx=0.47, y=425)
   critical_level.place(relx=0.47, y=450)
   enemy_block.place(relx=0.47, y=475)
   critical_submit.place(relx=0.5, y=500)
   current_math.place(relx=0.1, y=800)

   #clean up stuff
   cleanup_list.append(bubble)
   cleanup_list.append(bal_blade)
   cleanup_list.append(reset_to_spell_type)
   cleanup_list.append(spell_damage)
   cleanup_list.append(blade)
   cleanup_list.append(sharpened_blade)
   cleanup_list.append(weakness)
   cleanup_list.append(tower_shield)
   cleanup_list.append(trap)
   cleanup_list.append(potent_trap)
   cleanup_list.append(feint)
   cleanup_list.append(boost)
   cleanup_list.append(boost_submit)
   cleanup_list.append(aura)
   cleanup_list.append(aura_submit)
   cleanup_list.append(reset_damage)
   cleanup_list.append(current_math)
   cleanup_list.append(critical_level)
   cleanup_list.append(critical_submit)
   cleanup_list.append(enemy_block)
   cleanup_list.append(critical_chance)

#blade
def blade_increase():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*1.35)
   damageMath += 'Blade: 35% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*1.35)
   buffChart()

#sharpened blade
def s_blade_increase():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*1.45)
   damageMath += 'Blade: 45% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*1.45)
   buffChart()

#balance blade
def b_blade():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*1.25)
   damageMath += 'Blade: 25% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*1.25)
   buffChart()

#bubble
def global_effect():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*1.25)
   damageMath += 'Global: 25% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*1.25)
   buffChart()

#weakness
def weakness_decrease():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*0.75)
   damageMath += 'Weakness: -25% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*0.75)
   buffChart()

#tower shield
def shield_decrease():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*0.5)
   damageMath += 'Tower Shield: -50% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*0.5)
   buffChart()

#trap
def trap_increase():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*1.3)
   damageMath += 'Trap: 30% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*1.3)
   buffChart()

#potent trap
def p_trap_increase():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*1.4)
   damageMath += 'Trap: 40% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*1.4)
   buffChart()

#feint
def feint_increase():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*1.7)
   damageMath += 'Feint: 70% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*1.7)
   buffChart()

#boost
def calculateBoost():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*((boost_amount.get()/100)+1))
   damageMath += 'Boost: ' + str(boost_amount.get()) + '% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*((boost_amount.get()/100)+1))
   buffChart()

#aura
def aura_increase():
   global totalDamage
   global damageMath
   totalDamage = math.floor(totalDamage*((aura_amount.get()/100)+1))
   damageMath += 'Aura: ' + str(aura_amount.get()) + '% \n'
   if double == True:
      global totalDamageTwo
      totalDamageTwo = math.floor(totalDamageTwo*((aura_amount.get()/100)+1))
   buffChart()

#crit chance
def criticalMath():
   global damageMath
   global chance_to_crit
   chance_to_crit = str(math.floor((player_level.get()/100) * ((3*critical_rating.get())/((3*critical_rating.get())+block_amount.get())) * 100)) + '%'
   damageMath += 'Chance to crit: ' + chance_to_crit + ' \n'
   buffChart()

#window stuff
window = tk.Tk()
window_width = 1200
window_height = window.winfo_screenheight()

#text format: message = tkinter.Label(windowname, attribute)
message = ttk.Label(window, text="Damage Calculator")
window.title('Damage Calculator')
create_new = ttk.Button(window, text="Start", command=damageType)
create_new.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#window size format: (width, height, distance from left edge, distance from top)
message.pack()

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#center
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

#defines window size
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(True, True)




#makes it look better
try:
  from ctypes import windll

  windll.shcore.SetProcessDpiAwareness(1)
finally:
  window.mainloop()