" curl -flo $HOME/.config/nvim/autoload/plug.vim --create-dirs \
 "   https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

source ~/.config/nvim/autopair.vim
"source ~/.config/nvim/theme.vim

set nocompatible		" be IMproved, required
filetype off			" required

call plug#begin('~/.config/nvim/plugged')
" Plug 'sainnhe/gruvbox-material'
Plug 'sonph/onehalf', { 'rtp': 'vim' }
" Plug 'dracula/vim', { 'as': 'dracula' }
" Plug 'embark-theme/vim', { 'as': 'embark' }
" Plug 'gruvbox-community/gruvbox'
Plug 'tpope/vim-fugitive'
"Plug 'preservim/nerdtree'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'ap/vim-css-color' "Displays a preview of colors with CSS 
Plug 'vim-scripts/fountain.vim'
Plug 'junegunn/limelight.vim'
Plug 'lervag/vimtex'
Plug 'godlygeek/tabular'
Plug 'plasticboy/vim-markdown'
Plug 'vimwiki/vimwiki'
Plug 'itchyny/lightline.vim'
Plug 'vifm/vifm.vim'
"Plug 'ryanoasis/vim-devicons'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

call plug#end()

                                   
colorscheme onehalfdark
let g:lightline = { 'colorscheme': 'onehalfdark' }
set incsearch
set hidden
set undodir=~/.config/nvim/undodir
set undofile
set nobackup
set noswapfile
set number relativenumber       " Display line numbers

set encoding=utf8
syntax on
filetype plugin indent on 
set colorcolumn=80
set background=dark 
highlight ColorColumn ctermbg=0 guibg=lightgrey
set number
"set nowrap
set smartcase
set hlsearch
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4 autoindent 
set expandtab
set smartindent
"setlocal spell spelllang=en_us
set mouse=a  
set confirm             " Prompt confirmation dialogs
set showtabline=4       " Show tab bar
set splitbelow
set splitright
" set clipboard=unnamedplus
" split navigations

"map <silent> <C-n> :NERDTreeFocus<CR>
"let g:NERDTreeDirArrowExpandable = '►'
"let g:NERDTreeDirArrowCollapsible = '▼'
"let NERDTreeShowLineNumbers=1
"let NERDTreeShowHidden=1
"let NERDTreeMinimalUI = 1
"let g:NERDTreeWinSize=38
"let NERDTreeMapOpenInTab='<ENTER>'

nnoremap <F5> :VimtexCompile<CR>


" Exit Vim if NERDTree is the only window left.
"autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() |
"    \ quit | endif

" Tab shortcuts
nnoremap <C-t> :tabnew<CR>
nnoremap <C-w> :tabclose<CR>
nnoremap tk :tabnext<CR>
nnoremap tj :tabprev<CR>
nnoremap th :tabfirst<CR>
nnoremap tl :tablast<CR>

" Move visually selected line up and down in various modes
nnoremap K :m .-2<CR>==
nnoremap J :m .+1<CR>==
vnoremap K :m '<-2<CR>gv=gv
vnoremap J :m '>+1<CR>gv=gv

vmap <C-c> y:call system("xclip -i -selection clipboard", getreg("\""))<CR>:call system("xclip -i", getreg("\""))<CR> 

inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"

let mapleader=" "
" Makes vimwiki markdown links as [text](text.md) instead of [text](text)

let g:vimwiki_markdown_link_ext = 1

" vimwiki stuff "
" Run multiple wikis "
let g:vimwiki_list = [{'path': '~/Documents/VimWiki/', 'syntax':'markdown', 'ext':'.md' }]
let g:vimwiki_ext2syntax = {'.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}

"let g:lightline = {
"      \ 'colorscheme': 'seoul256',
"      \ }

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Vifm
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
map <Leader>vv :Vifm<CR>
map <Leader>vs :VsplitVifm<CR>
map <Leader>sp :SplitVifm<CR>
map <Leader>dv :DiffVifm<CR>
map <Leader>tv :TabVifm<CR>

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nnoremap <silent> <C-f> :Files<CR>
nnoremap <silent> <Leader>f :BLines<CR>

let g:fzf_action = {
      \ 'enter': 'tab split',
  \ }

" Toggle Vexplore with Ctrl-E
function! ToggleVExplorer()
  if exists("t:expl_buf_num")
      let expl_win_num = bufwinnr(t:expl_buf_num)
      if expl_win_num != -1
          let cur_win_nr = winnr()
          exec expl_win_num . 'wincmd w'
          close
          exec cur_win_nr . 'wincmd w'
          unlet t:expl_buf_num
      else
          unlet t:expl_buf_num
      endif
  else
      exec '1wincmd w'
      Vexplore
      let t:expl_buf_num = bufnr("%")
  endif
endfunction
map <silent> <C-E> :call ToggleVExplorer()<CR>

" Hit enter in the file browser to open the selected
" file with :vsplit to the right of the browser.
let g:netrw_browse_split = 4
let g:netrw_altv = 1
let g:netrw_banner=0
let g:netrw_liststyle=3
let g:netrw_winsize = 10

" close if final buffer is netrw or the quickfix
augroup finalcountdown
 au!
 autocmd WinEnter * if winnr('$') == 1 && getbufvar(winbufnr(winnr()), "&filetype") == "netrw" || &buftype == 'quickfix' |q|endif
 nmap - :Vexplore<cr>
augroup END


