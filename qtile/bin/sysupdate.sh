#!/usr/bin/env bash

if ! updates_arch=$(checkupdates 2> /dev/null | wc -l ); then
    updates_arch=0
fi

if ! updates_aur=$(yay -Qum 2> /dev/null | wc -l); then
    updates_aur=0
fi

updates=$(("$updates_arch" + "$updates_aur"))

if [ "$updates" -gt 0 ]; then
    seq "$updates"
    #echo "<span foreground='#3b4252'> | </span><span font_desc='UbuntuMono Nerd Font' foreground='#bf616a'></span> $updates"
    #echo "%{F#bf616a}%{F-} $updates"
fi