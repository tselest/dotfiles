# ==================================
#              __                  
#              \ \                 
#  ___ ____ ___ \ \   ___ ____ ___ 
# (   )  ._) __) > \ / __)  ._|   )
#  | ( () )> _) / ^ \> _| () ) | | 
#   \_)__/ \___)_/ \_\___)__/   \_)
#                                 
# 
# ==================================

from typing import List  # noqa: F401
from libqtile import qtile
from libqtile import bar, layout, widget,hook
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import sys
import time 
import os
import re
import socket
import subprocess 
import logging
import iwlib
import psutil
import arcobattery

mod = "mod4"
term = "usr/bin/kitty"
terminal = guess_terminal()
home = os.path.expanduser('~')

def update():
    qtile.cmd_spawn(terminal + "-e yay")

def pavu():
    qtile.cmd_spawn('pavucontrol')

def roffi():
    qtile.cmd_spawn(" rofi -show p -modi p:rofi-power-menu   -theme gruvbox-dark   -font 'JetbrainsMonoMedium Nerd Font Mono 13'   -width 20   -lines 6")

def power():
    qtile.cmd_spawn("xfce4-power-manager-settings")

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "h", lazy.layout.grow()),
    Key([mod], "l", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "m", lazy.layout.maximize()),


    # == move and update up, down, left, right
    Key([mod], "s", lazy.layout.down()),
    Key([mod], "z", lazy.layout.up()),
    Key([mod], "q", lazy.layout.left()),
    Key([mod], "d", lazy.layout.right()),
    Key([mod, "shift"], "s", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "z", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "q", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "d", lazy.layout.shuffle_right()),
    Key([mod, "mod1"], "s", lazy.layout.flip_down()),
    Key([mod, "mod1"], "z", lazy.layout.flip_up()),
    Key([mod, "mod1"], "q", lazy.layout.flip_left()),
    Key([mod, "mod1"], "d", lazy.layout.flip_right()),
    Key([mod, "control"], "s", lazy.layout.grow_down()),
    Key([mod, "control"], "z", lazy.layout.grow_up()),
    Key([mod, "control"], "q", lazy.layout.grow_left()),
    Key([mod, "control"], "d", lazy.layout.grow_right()),
    #Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn("dmenu_run -h 28 ")),
    Key([mod], "p", lazy.spawn("firefox --private-window")),
    Key([mod], "t", lazy.spawn("firefox")),
    Key([mod], "e", lazy.spawn("brave")),
    Key([mod], "f", lazy.spawn("rofi -combi-modi window,drun,ssh -theme gruvbox-dark -font 'JetbrainsMonoMedium Nerd Font Mono 13' -show combi")),
    Key([mod], "g", lazy.spawn("rhythmbox")),
    Key([], "Print", lazy.spawn(["sh", "-c", " maim -u ~/Pictures/screenshots/screen_$(date +%Y-%m-%d-%T).png"])), 
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key(["mod1"] , "Shift_L", lazy.widget['keyboardlayout'].next_keyboard()), 
    Key(["mod1"] , "r", lazy.spawn("retroarch")),
 Key([mod, "shift"], "x", lazy.spawn(" kitty -e shutdown now")),
 Key([mod], "a", lazy.spawn("pcmanfm")),

### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up()                # Move up a section in treetab
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down()              # Move down a section in treetab
             ),

]

#groups = [Group(i) for i in "123456"]
#-----------------------------------------------------------
group_names =  [("1", {'layout': 'monadtall', 'init': True}),
            ("2", {'layout': 'monadtall','matches':[Match(wm_class=["rhythmbox"])]}),
            ("3", {'layout': 'monadtall', 'matches':[Match(wm_class=["pcmanfm"])]}),
            ("4", {'layout': 'treetab', 'matches':[Match(wm_class=["firefox"])]}),
            ("5", {'layout': 'monadtall', 'matches':[Match(wm_class=["mpv"])]}),
            ("6", {'layout': 'monadtall','matches':[Match(wm_class=["Thunderbird"])]})]
#-----------------------------------------------------------

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
     keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
     keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 2,
                "margin": 6,  
                "border_focus": "#a13fa2",      
                "border_normal": "#1D2330"   
                }

layouts = [    
        #layout.MonadWide(**layout_theme),   
        #layout.Stack(stacks=2, **layout_theme),  
        #layout.Columns(**layout_theme),   
        #layout.RatioTile(**layout_theme),  
        #layout.VerticalTile(**layout_theme), 
        #layout.Matrix(**layout_theme),  
        #layout.Zoomy(**layout_theme),  
        layout.MonadTall(**layout_theme),  
        #layout.Bsp(**layout_theme),   
        #layout.Max(**layout_theme),  
        #layout.Tile(shift_windows=True, **layout_theme),  
        #layout.Stack(num_stacks=2),  
        layout.TreeTab(     
            font = "JetbrainsMonoMedium Nerd Font Mono",     
            fontsize = 10,     
            sections = ["FIRST", "SECOND"],     
            section_fontsize = 11,      
            bg_color = "#2e3440",        
            active_bg = "#a3be8c",     
            active_fg = "#2e3440",       
            inactive_bg = "#e5e9f0",    
            inactive_fg = "#2e3440",      
            padding_y = 5,    
            section_top = 10,      
            panel_width = 200,
            opacity = 0.7
            ),   
        #layout.Floating()
        ]

# Nord Color Theme
colors = [["#2e3440", "#2e3440"], #nord0    
        ["#3b4252", "#3b4252"], #nord1    
        ["#434c5e", "#434c5e"], #nord2     
        ["#4c566a", "#4c566a"], #nord3     
        ["#d8dee9", "#d8dee9"], #nord4      
        ["#e5e9f0", "#e5e9f0"], #nord5      
        ["#eceff4", "#eceff4"], #nord6      
        ["#8fbcbb", "#8fbcbb"], #nord7      
        ["#88c0d0", "#88c0d0"], #nord8      
        ["#81a1c1", "#81a1c1"], #nord9      
        ["#5e81ac", "#5e81ac"], #nord10     
        ["#bf616a", "#bf616a"], #nord11     
        ["#d08770", "#d08770"], #nord12     
        ["#ebcb8b", "#ebcb8b"], #nord13     
        ["#a3be8c", "#a3be8c"], #nord14      
        ["#b48ead", "#b48ead"]] #nord15

 # ### PROMPT ###
# prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
     widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground = colors[5],
                    background = colors[0]
                    ),
            
   widget.CurrentLayoutIcon(
                    background=colors[0],
                    foreground=colors[13],
                    scale=0.5,
                    ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground = colors[5],
                    background = colors[0]
                    ),
              

widget.GroupBox(
                    foreground=[ "#f1ffff", "#f1ffff"],
                    background=colors[0],#["#0f101a","#0f101a"],
                    font='JetbrainsMonoMedium Nerd Font Mono',
                    fontsize=14,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=[ "#f1ffff", "#f1ffff"],
                    inactive=colors[3],#[ "#4c566a", "#4c566a"],
                    rounded=True,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#F07178","#F07178"],
                    this_current_screen_border=["#a13fa2","#a13fa2"],
                    this_screen_border=["#353c4a","#353c4a"],
                    other_current_screen_border=["#0f101a","#0f101a"],
                    other_screen_border=["#0f101a","#0f101a"],
                    disable_drag=True
                ),
widget.Prompt(

                ),
widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground = colors[5],
                    background = colors[0]
                ),
              
widget.WindowName(
                     foreground=colors[13],            #["#a151d3","#a151d3"],
                     background=colors[0],  #["#0f101a","#0f101a"],
                     fontsize=13,
                     font='JetbrainsMonoExtraBold Nerd Font Mono',
                ),

widget.Sep(
                     linewidth=0,
                     padding=4,
                     background=colors[0],
                     foreground=colors[5],
                ),

 widget.TextBox(
                     text=' ',
                     background = colors[0],
                     foreground = colors[13],
                     font='Hack',
                     fontsize=12,
                ),

 widget.CheckUpdates(

                     background=colors[0],
                     foreground=colors[13],
                     colour_have_updates=colors[13],
                     custom_command="/home/tselest/.config/qtile/bin/sysupdate.sh",
                     display_format="{updates}",
                     execute=update,
                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('kitty -e sudo pacman -Syu')},
                     padding=2,
                     font='JetbrainsMonoMedium Nerd Font Mono',

                ),

widget.Sep(
                     linewidth=0,
                     padding=15,
                     background=colors[0],
                     foreground=colors[5],

                ),

widget.TextBox(
                     text = "",
                     padding = 2,
                     mouse_callbacks = {'Button1': pavu},
                     foreground = colors[13],
                     background = colors[0],
                     font='Hack',
                     fontsize = 12

                ),             
              
widget.PulseVolume(
                     foreground=colors[13],
                     background=colors[0],
                     limit_max_volume="True",
                     font='JetbrainsMonoMedium Nerd Font Mono',

                 ), 

widget.Sep(
                     linewidth=0,
                     padding=12,
                     background=colors[0],
                     foreground=colors[5],

                 ),
 
widget.TextBox(
                     text='',
                     background = colors[0],
                     foreground = colors[13],
                     fontsize=12,
                     font="Hack",

                ),
   
widget.Clock(
                     background=colors[0],
                     foreground=colors[13],
                     padding=2,
                     format='%d-%m-%Y',
                     font='JetbrainsMonoMedium Nerd Font Mono'

                ),

widget.Sep(
                     linewidth=0,
                     padding=12,
                     foreground = colors[0],
                     background = colors[0]

                ),
    
widget.TextBox(
                     text='',
                     background = colors[0],
                     foreground = colors[13],
                     fontsize=12,
                     font="Hack",

                ),
  
widget.Clock(
                     background=colors[0],
                     foreground=colors[13],
                     padding=2,
                     format='%H:%M ',
                     font='JetbrainsMonoMedium Nerd Font Mono'

                ),

widget.Sep(
                     linewidth=0,
                     padding=5,
                     foreground = colors[0],
                     background = colors[0]

                ),
             
widget.TextBox(
                     text='',
                     background = colors[0],
                     foreground = colors[13],
                     font='Hack',
                     fontsize=12,

                ),
  
widget.KeyboardLayout(

                     configured_keyboards = ['us', 'gr'],
                     font='JetbrainsMonoMedium Nerd Font Mono',
                     background=colors[0],
                     foreground=colors[13],

                ),

widget.Sep(
                     linewidth=0,
                     padding=5,
                     foreground = colors[0],
                     background = colors[0]

                ),

widget.CapsNumLockIndicator(   

                     background=colors[0],
                     foreground=colors[13],
                     font='JetbrainsMonoMedium Nerd Font Mono',

                ),
                                
widget.Sep(
                     linewidth=0,
                     padding=5,
                     foreground = colors[0],
                     background = colors[0]

                ),

widget.Battery(
                     background=colors[0],
                     foreground=colors[13],
                     format='{percent:2.0%}',
                     font='JetbrainsMonoMedium Nerd Font Mono',
                     update_interval=0.1,

                ),

arcobattery.BatteryIcon(

                     scale=0.4,
                     y_poss=7,
                     theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
                     update_interval = 5,
                     background = colors[0],
                     mouse_callbacks={"Button1":power}

                ),
   
widget.Systray(

                    foreground=colors[0],
                    background = colors[0],
                    padding = 5

                ),
   
 widget.Sep(
                    linewidth=0,
                    padding=3,
                    foreground = colors[0],
                    background = colors[0]

                ),

widget.TextBox(
                    text="⏻",
                    foreground=colors[13],
                    background=colors[0],
                    font="Font Awesome 5 Free Solid",
                    fontsize=22,
                    padding=15,
                    mouse_callbacks={"Button1": roffi}

                ),

 widget.Sep(
                    linewidth=0,
                    padding=3,
                    foreground = colors[0],
                    background = colors[0]

                ),
            ],
            38,
         #   opacity=0.92,
margin=[0, -4, 21, -4],
        ),
        bottom=bar.Gap(18),
        left=bar.Gap(18),
        right=bar.Gap(18),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating( **layout_theme,
        float_rules=[    *layout.Floating.default_float_rules,

    # Run the utility of `xprop` to see the wm class and name of an X client.
   Match(wm_class= 'confirm'),
   Match(wm_class= 'dialog'),
   Match(wm_class= 'download'),
   Match(wm_class= 'error'),
   Match(wm_class= 'file_progress'),
   Match(wm_class= 'notification'),
   Match(wm_class= 'splash'),
   Match(wm_class= 'toolbar'),
   Match(wm_class= 'confirmreset'),  # gitk
   Match(wm_class= 'makebranch'),  # gitk
   Match(wm_class= 'maketag'),  # gitk
   Match(title= 'branchdialog'),  # gitk
   Match(title= 'pinentry'),  # GPG key password entry
   Match(wm_class= 'ssh-askpass'),  # ssh-askpass
   Match(wm_class='pavucontrol'),
   Match(wm_class="megasync"),
   Match(title='Qalculate!'),
   Match(wm_class="xfce4-power-manager-settings"),
   Match(title="Picture in picture"),
])

auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
