" Config
:set nocompatible
:set directory=/tmp

:set iskeyword=a-z,A-Z,48-57

"SOURCE FILES
:source ~/.vim/plugins/newbie.vim

"Abbreviation
:iab #!/ :call Hash_Bang()<CR>

"Leader
:let mapleader = '\'
"nmap <Leader>K :call <SID>PreGetPage(0)<CR>
:command! -range Wrapper call Align(<line1>, <line2>)

"Strip trailing space
 :map <Leader>S :1,$ s/\s\+$//g<CR>
:imap <Leader>S :1,$ s/\s\+$//g<CR>

"Comment selected lines
 :map <Leader># :call Comment()<CR>
:imap <Leader># :call Comment()<CR>
:vmap <Leader># :call Comment()<CR>

"Sort and align
:map <Leader>s :call Sort()<CR>

"Strip C-M
:map <Leader>f :%s s///g<CR>
"----------------------------------------------------------------------
"Open file
 :map <C-f> :call OpenFile()<CR>
:imap <C-f> <Esc>:call OpenFile()<CR>
"au BufWinEnter * :call OpenFile(expand("<abuf>"))
"nuke extra trailing spaces
"au BufWrite * :1,$ s/\s\+$//g


"Global quit
"
 :map <C-q>      :mksession! ~/.vim/sessions/default<CR>:qa!<CR>
:imap <C-q> <Esc>:mksession! ~/.vim/sessions/default<CR>:qa!<CR>

"Select
:map <S-End> <C-v>$
:imap <S-End> <Esc><C-v>$

:map <S-Home> <C-v>0
:imap <S-Home> <Esc><C-v>0

:map <S-Down> j
:imap <S-Down> j

:map <S-Up> k
:imap <S-Up> k

:map <C-a> ggvG$
:imap <C-a> <Esc>ggvG$
"----------------------------------------------------------------------
"Indent
:vmap <Tab> >

"----------------------------------------------------------------------
"Tabbed browsing
"Save
:map <M-s> :call Save_file()<CR>
:imap <M-s> <Esc>:call Save_file()<CR>a
"Next
:map <M-=> :tabnext<CR>
:imap <M-=> <Esc>:tabnext<CR>
"Previous
:map <M--> :tabprevious<CR>
:imap <M--> <Esc>:tabprevious<CR>
"Jump to Tab
:map <M-1> 1gt
:imap <M-1> <Esc>1gti
:map <M-2> 2gt
:imap <M-2> <Esc>2gti
:map <M-3> 3gt
:imap <M-3> <Esc>3gti
:map <M-4> 4gt
:imap <M-4> <Esc>4gti
:map <M-5> 5gt
:imap <M-5> <Esc>5gti
:map <M-6> 6gt
:imap <M-6> <Esc>6gti

"Open
:map <M-t> :tabnew<CR>i
:imap <M-t> <Esc>:tabnew<CR>i
"Close
:map <M-q> :q!<CR>
:imap <M-q> <Esc>:q!<CR>

"Tabbed editing
"Copy "*y
:vmap <M-c> "+y
"Cut
":vmap <M-x> "*d
:vmap <M-x> :call Cut()<CR>

"Paste "+p clipboard selection
:map <M-v> :call Paste()<CR>
:imap <M-v> <Esc>:call Paste()<CR>
:vmap <M-v> :call Paste()<CR>

":map <M-v> :pu<CR>i
":imap <M-v> <ESC>:pu<CR>

"Navigation
:map <M-f> /[a-zA-Z0-9_]\+\\|[^a-zA-Z0-9_]\+<CR>i
:imap <M-f> <Esc><Right>/[a-zA-Z0-9_]\+\\|[^a-zA-Z0-9_]\+<CR>i
:map <M-b> ?[a-zA-Z0-9_]\+\\|[^a-zA-Z0-9_]\+<CR>i
:imap <M-b> <Esc><Right>?[a-zA-Z0-9_]\+\\|[^a-zA-Z0-9_]\+<CR>i
:map <M-a> ^
:imap <M-a> <Esc>^i
:map <M-e> $
:imap <M-e> <Esc>$a

"Page-up
:map <PageUp> <C-U>i
:imap <PageUp> <Esc><C-U>i
"Page-down
:map <PageDown> <C-D>i
:imap <PageDown> <Esc><C-D>i

"Delete word backward
:map <M-Backspace> d?[a-zA-Z0-9_]\+\\|[^a-zA-Z0-9_]\+<CR>i
:imap <M-Backspace> <Esc><Right>?[a-zA-Z0-9_]\+\\|[^a-zA-Z0-9_]\+<CR>i
:cmap <M-Backspace> <C-w>
:cmap <M-b> <S-Left>
"Delete word forward
:map <M-d> d/[a-zA-Z0-9_]\+\\|[^a-zA-Z0-9_]\+<CR>i
:imap <M-d> <Esc><Right>d/[a-zA-Z0-9_]\+\\|[^a-zA-Z0-9]\+<CR>i
:cmap <M-f> <S-Right>

"Kill left of line
:map <M-k>r dv0
:imap <M-k>r <Esc>dv0i
"Kill right of line
:map <M-k>l d$i
:imap <M-k>l <Esc>d$i
"Kill complete line
:map <M-k>. ddi
:imap <M-k>. <Esc>ddi
:map <M-.> .
:imap <M-.> <Esc>.
"Repeat operation
:map <M-.> .i
:imap <M-.> <Esc>.
"Undo operation
:map <M-u> ui
:imap <M-u> <Esc>ui
"Redo operation
:map <M-r> :redo<CR>i
:imap <M-r> <Esc>:redo<CR>i

"Insert line
:map <M-l> o
:imap <M-l> <Esc>o

"Join line
:map <M-j> <Esc><S-j><End>i

"Search
:map <M-h> :set showmatch<CR>:set incsearch<CR>:set hlsearch<CR>
:imap <M-h> <Esc>:set showmatch<CR>:set incsearch<CR>:set hlsearch<CR>i
:map <M-o> :set noshowmatch<CR>:set noincsearch<CR>:set nohlsearch<CR>
:imap <M-o> <Esc>:set noshowmatch<CR>:set noincsearch<CR>:set nohlsearch<CR>i
:set ignorecase
:map <M-/> /
:imap <M-/> <Esc>/
:map <M-?> ?
:imap <M-?> <Esc>?
:map <M-n> n
:imap <M-n> <Esc>ni
:map <M-p> N
:imap <M-p> <Esc>Ni

:imap <M-%> <Esc><Right>%i
:map <M-%> %i
"----------------------------------------------------------------------
" Help
:fixdel
:map <C-?> :tabnew<CR>:h<CR><C-W><Down><C-W>c:h<Space>
:imap <C-?> <Esc>:tabnew<CR>:h<CR><C-W><Down><C-W>c:h<Space>

"----------------------------------------------------------------------
" Display
:syntax on

" GUI
:set guioptions=T
:set guifont=Monospace\ 12
"256 xterm colors
:set t_Co=256
if &term == "xterm"
    colorscheme desert256 "evening
else
    colorscheme desert256
endif

":au BufRead,BufAdd,BufCreate *.txt tabnew

:set tabline=%!Tab_line()
:highlight TabLine guibg=DarkGrey guifg=white

" Run Menu
:aunmenu *
:amenu icon=/usr/share/vlc/mozilla/play.xpm ToolBar.Goo :call Build_program()<CR>
:imap <Leader>r <Esc>:call Build_program()<CR>
:map <Leader>r :call Build_program()<CR>
"----------------------------------------------------------------------
" Programming
:set completefunc=Auto_complete
:set omnifunc=Auto_complete
:imap <Tab> <C-R>=Tab_wrapper()<CR>

:set number
:set tabstop=4
:set expandtab
:set textwidth=72

:set shiftwidth=4

"----------------------------------------------------------------------
" Sessions
:set sessionoptions+=resize
if &term != "xterm"
   au VimEnter * :source ~/.vim/sessions/default
endif

" Mouse
:set mouse=a
"----------------------------------------------------------------------


":highlight ErrorMsg ctermbg=green guibg=green
" text too long, empty spaces
"match ErrorMsg /\%>73v.\+/
match ErrorMsg /\%>72v.*/
match errorMsg /\s\+$/
"au BufWritePost * :1,$ s/\s*$//g

:set laststatus=2
":set showtabline=2
:set statusline=[TYPE=%Y]\ [ASCII=\%03.3b]\ [HEX=\%02.2B]\ [POS=%04l,%04v]\ [%p%%]\ [LEN=%L]

" test
":filetype plugin on
":let g:pydiction_location = '/tmp/complete-dict'
"au BufWinEnter * call My_dir(expand("<afile>"))


if &term =~ "xterm\\|rxvt"
  " use an white cursor in insert mode
  let &t_SI = "\<Esc>]12;white\x7"
  " use a red cursor otherwise
  let &t_EI = "\<Esc>]12;wheat\x7"
  silent !echo -ne "\033]12;wheat\007"
  " reset cursor when vim exits
  autocmd VimLeave * silent !echo -ne "\033]112\007"
  " use \003]12;gray\007 for gnome-terminal
endif

