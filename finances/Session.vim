let SessionLoad = 1
if &cp | set nocp | endif
<<<<<<< HEAD
let s:cpo_save=&cpo
set cpo&vim
inoremap <C-Y> 
inoremap <C-L> <Right>
inoremap <C-W> :w
inoremap <C-D><C-D> <><Left>
inoremap <C-D> <><Left>
nnoremap  :!. ~/sh/g.sh 
nnoremap   .
nnoremap :w :mks!:w
nmap <silent> \w\m <Plug>VimwikiMakeTomorrowDiaryNote
nmap <silent> \w\y <Plug>VimwikiMakeYesterdayDiaryNote
nmap <silent> \w\t <Plug>VimwikiTabMakeDiaryNote
nmap <silent> \w\w <Plug>VimwikiMakeDiaryNote
nmap <silent> \w\i <Plug>VimwikiDiaryGenerateLinks
nmap <silent> \wi <Plug>VimwikiDiaryIndex
nmap <silent> \ws <Plug>VimwikiUISelect
nmap <silent> \wt <Plug>VimwikiTabIndex
nmap <silent> \ww <Plug>VimwikiIndex
nnoremap controlv :let collage= Collage(collage)
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
nnoremap go Go
nnoremap gi Gi
nnoremap tn :tabnew .
nnoremap vp :vsp .
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
nnoremap <C-G> :!. ~/sh/g.sh 
nnoremap <F12> :!clear
nnoremap <F9> :so $VIMRUNTIME/syntax/hitest.vim
nnoremap <F8> :call LinkImage()
nnoremap <F3> :! ~/sh/mymake.sh 
nnoremap <F1> :call Vimrc()
inoremap  <><Left>
inoremap  <><Left>
inoremap  <Right>
inoremap  :w
inoremap  
inoremap """ "A"
inoremap "" "
inoremap " ""<Left>
inoremap ((( (A)
inoremap (( (
inoremap ( ()<Left>
vnoremap ét :call Task()
nnoremap éé "
nnoremap éo oO
nnoremap èè :wqall
nnoremap è :
inoremap [[[ [A] 
inoremap [[ [
inoremap [ []<Left>
inoremap {{{ {A} 
inoremap {{ { 
inoremap { {}<Left> 
let &cpo=s:cpo_save
unlet s:cpo_save
set backspace=indent,eol,start
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=fr
set ignorecase
set incsearch
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/plugged/swift.vim/,~/.vim/plugged/nerdtree/,~/.vim/plugged/vimwiki/,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after
set smartcase
set splitbelow
set splitright
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set wildmenu
=======
>>>>>>> f61b6a18ce4982dc0dfb8ca16456337c997b2339
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/projet/finances
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd ~/note/note
edit ~/note/note
set splitbelow splitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
<<<<<<< HEAD
setlocal keymap=
setlocal noarabic
setlocal noautoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != ''
setlocal filetype=
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
set relativenumber
setlocal relativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=8
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != ''
setlocal syntax=
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 166 - ((53 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
166
=======
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
<<<<<<< HEAD
let s:l = 1 - ((0 * winheight(0) + 13) / 26)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
=======
let s:l = 8 - ((7 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
8
>>>>>>> 10721b7936ea8172eb63ffd2ae18823f9d2ccf5e
>>>>>>> f61b6a18ce4982dc0dfb8ca16456337c997b2339
normal! 0
tabnext 1
badd +0 ~/note/note
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOS
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
