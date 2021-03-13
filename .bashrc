#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

### ARCHIVE EXTRACTION 
# usage: ex <file> 
ex () {   
	if [ -f $1 ] ; then   
	      	case $1 in   
		    	*.tar.bz2)   tar xjf $1   ;;   
		    	*.tar.gz)    tar xzf $1   ;;    
		     	*.bz2)       bunzip2 $1   ;;    
		     	*.rar)       unrar x $1   ;;   
		    	*.gz)        gunzip $1    ;;   
		    	*.tar)       tar xf $1    ;;   
		    	*.tbz2)      tar xjf $1   ;;   
		    	*.tgz)       tar xzf $1   ;;    
		     	*.zip)       unzip $1     ;;   
		    	*.Z)         uncompress $1;;   
		    	*.7z)        7z x $1      ;;   
		    	*.deb)       ar x $1      ;;    
		     	*.tar.xz)    tar xf $1    ;;   
		    	*.tar.zst)   unzstd $1    ;;   
	       		*)           echo "'$1' cannot be extracted via ex()" ;; 
	    	esac 
      	else   
	      	echo "'$1' is not a valid file" 
	      
	fi
}

# youtube-dl
alias yta-aac="youtube-dl --extract-audio --audio-format aac "
alias yta-best="youtube-dl --extract-audio --audio-format best "
alias yta-flac="youtube-dl --extract-audio --audio-format flac "
alias yta-m4a="youtube-dl --extract-audio --audio-format m4a "
alias yta-mp3="youtube-dl --extract-audio --audio-format mp3 "
alias yta-opus="youtube-dl --extract-audio --audio-format opus "
alias yta-vorbis="youtube-dl --extract-audio --audio-format vorbis "
alias yta-wav="youtube-dl --extract-audio --audio-format wav "
alias ytv-best="youtube-dl -f bestvideo+bestaudio "

# git
alias addup='git add -u'
alias addall='git add .'
alias branch='git branch'
alias checkout='git checkout'
alias clone='git clone'
alias commit='git commit -m'
alias fetch='git fetch'
alias pull='git pull origin'
alias push='git push origin'
alias status='git status'
alias tag='git tag'
alias newtag='git tag -a'


colorscript random
