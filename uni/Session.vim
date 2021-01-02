let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
imap <C-G>S <Plug>ISurround
imap <C-G>s <Plug>Isurround
inoremap <C-S> <Right>
inoremap <C-C> :w
nnoremap  /
nnoremap  :tabp
nnoremap <NL> }
nnoremap  {
nnoremap  :tabn
nnoremap   .
nnoremap Buffer é1 :%s/Pseudocode/Pseudo code/g
xmap S <Plug>VSurround
nmap cS <Plug>CSurround
nmap cs <Plug>Csurround
nnoremap cp :CpL 
nmap ds <Plug>Dsurround
xmap gS <Plug>VgSurround
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
onoremap in) :normal f)hvT(
onoremap in( :normal! f(vi(
onoremap lp :normal t)vF,
onoremap n" :normal f"lvt"
nnoremap tn :LfNewTab
nnoremap vs :sp .
nnoremap vp :vsp .
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
nnoremap <F5> :!~/sh/compmd % pdf && mv -f PDF
nnoremap <silent> <Plug>SurroundRepeat .
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
nnoremap <silent> <Plug>(JavaComplete-Imports-SortImports) :call javacomplete#imports#SortImports()
nnoremap <silent> <Plug>(JavaComplete-Generate-ClassInFile) :call javacomplete#newclass#CreateInFile()
nnoremap <silent> <Plug>(JavaComplete-Generate-NewClass) :call javacomplete#newclass#CreateClass()
nnoremap <silent> <Plug>(JavaComplete-Generate-DefaultConstructor) :call javacomplete#generators#GenerateConstructor(1)
nnoremap <silent> <Plug>(JavaComplete-Generate-Constructor) :call javacomplete#generators#GenerateConstructor(0)
nnoremap <silent> <Plug>(JavaComplete-Generate-EqualsAndHashCode) :call javacomplete#generators#GenerateEqualsAndHashCode()
nnoremap <silent> <Plug>(JavaComplete-Generate-ToString) :call javacomplete#generators#GenerateToString()
vnoremap <silent> <Plug>(JavaComplete-Generate-AccessorSetterGetter) :call javacomplete#generators#Accessor('sg')
vnoremap <silent> <Plug>(JavaComplete-Generate-AccessorGetter) :call javacomplete#generators#Accessor('g')
vnoremap <silent> <Plug>(JavaComplete-Generate-AccessorSetter) :call javacomplete#generators#Accessor('s')
nnoremap <silent> <Plug>(JavaComplete-Generate-AccessorSetterGetter) :call javacomplete#generators#Accessor('sg')
nnoremap <silent> <Plug>(JavaComplete-Generate-AccessorGetter) :call javacomplete#generators#Accessor('g')
nnoremap <silent> <Plug>(JavaComplete-Generate-AccessorSetter) :call javacomplete#generators#Accessor('s')
nnoremap <silent> <Plug>(JavaComplete-Generate-Accessors) :call javacomplete#generators#Accessors()
nnoremap <silent> <Plug>(JavaComplete-Generate-AbstractMethods) :call javacomplete#generators#AbstractDeclaration()
nnoremap <silent> <Plug>(JavaComplete-Imports-AddSmart) :call javacomplete#imports#Add(1)
nnoremap <silent> <Plug>(JavaComplete-Imports-Add) :call javacomplete#imports#Add()
nnoremap <silent> <Plug>(JavaComplete-Imports-RemoveUnused) :call javacomplete#imports#RemoveUnused()
nnoremap <silent> <Plug>(JavaComplete-Imports-AddMissing) :call javacomplete#imports#AddMissing()
nnoremap <C-F> /
nnoremap <C-J> }
nnoremap <C-K> {
nnoremap <C-H> :tabp
nnoremap <C-L> :tabn
nnoremap <F12> :!clear
nnoremap <F10> :!gedit %
nnoremap <F9> :so $VIMRUNTIME/syntax/hitest.vim
nnoremap <F7> :make 
nnoremap <F3> :! ~/sh/mymake 
nnoremap <F2> :call Note()
nnoremap <F1> :tabnew ~/.vimrc
inoremap  :w
imap S <Plug>ISurround
imap s <Plug>Isurround
inoremap  <Right>
inoremap """ "A"
inoremap "" "
inoremap " ""<Left>
inoremap ((( (A)
inoremap (( (
inoremap ( ()<Left>
nnoremap éa "ap
nnoremap éo :!zathura PDF/%:p:t:r.pdf&
nnoremap é2 :g/Problème/execute "normal! A  "
nnoremap é1 :%s/Pseudocode/Pseudo code/g
noremap é  :!~/sh/compmd % pdf && mv -f %:p:t:r.pdf PDF
nnoremap éém :make group ; make ; make clean
map àf :Lf
nmap <silent> àwàm <Plug>VimwikiMakeTomorrowDiaryNote
nmap <silent> àwày <Plug>VimwikiMakeYesterdayDiaryNote
nmap <silent> àwàt <Plug>VimwikiTabMakeDiaryNote
nmap <silent> àwàw <Plug>VimwikiMakeDiaryNote
nmap <silent> àwài <Plug>VimwikiDiaryGenerateLinks
nmap <silent> àwi <Plug>VimwikiDiaryIndex
nmap <silent> àws <Plug>VimwikiUISelect
nmap <silent> àwt <Plug>VimwikiTabIndex
nmap <silent> àww <Plug>VimwikiIndex
nnoremap écta :call Ctags()
nnoremap édb :cope
nnoremap èè :call Makefile()
xnoremap éspa :call MakeSpace()
inoremap [[[ [A] 
inoremap [[ [
inoremap [ []<Left>
inoremap {{{ {A} 
inoremap {{ { 
inoremap { {}<Left> 
let &cpo=s:cpo_save
unlet s:cpo_save
set paste
set autowriteall
set background=dark
set backspace=indent,eol,start
set cindent
set complete=.,w,b,u,t,i,kspell
set completeopt=menu,preview,noselect
set fileencodings=ucs-bom,utf-8,default,latin1
set formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
set helplang=fr
set ignorecase
set incsearch
set laststatus=2
set matchpairs=(:),{:},[:],<:>
set nomodeline
set pastetoggle=<F8>
set path=.,/usr/include,,,**
set printoptions=paper:a4
set runtimepath=~/.vim,~/.vim/pack/tpope/start/surround,~/.vim/pack/default/start/pythoncomplete,~/.vim/plugged/vimwiki/,~/.vim/plugged/hardmode/,~/.vim/plugged/lf.vim/,~/.vim/plugged/vim-javacomplete2/,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after
set shiftwidth=4
set smartcase
set spelllang=fr_ch,en_us
set splitbelow
set splitright
set statusline=%#Cursor#\ VIM\ \ %#Normal#%{(mode()=='n')?'\ \ NORMAL\ ':''}%#PmenuThumb#%{(mode()=='i')?'\ \ INSERT\ ':''}%#TabLineFill#%{(mode()=='r')?'\ \ REPLACE\ ':''}%#SpellRare#%{(mode()=='v')?'\ \ VISUAL\ ':''}%#LineNr#\ %n\ %#Visual#%#CursorIM#%R%M%#Cursor#%#CursorLine#\ %t\ %=%#LineNr#\ %3l:%-2c\ %#Normal#\ %Y\ %#Cursor#%3p%%\ 
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set noswapfile
set timeoutlen=500
set virtualedit=onemore
set wildmenu
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/projet/uni
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd note.md
edit ~/projet/uni/Makefile
set splitbelow splitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
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
setlocal cindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=sO:#\ -,mO:#\ \ ,b:#
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i,kspell
setlocal concealcursor=
set conceallevel=2
setlocal conceallevel=2
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
set cursorline
setlocal cursorline
setlocal cursorlineopt=both
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'make'
setlocal filetype=make
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
setlocal formatoptions=croql
setlocal formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*include
setlocal includeexpr=
setlocal indentexpr=GetMakeIndent()
setlocal indentkeys=!^F,o,O,<:>,=else,=endif
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:],<:>
setlocal nomodeline
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
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=fr_ch,en_us
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'make'
setlocal syntax=make
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
let s:l = 10 - ((9 * winheight(0) + 11) / 22)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
10
normal! 010|
tabnext 1
badd +22 note.md
badd +10 ~/projet/uni/Makefile
badd +0 ~/projet/uni/PDF/note.pdf
badd +0 Highlight\ test
badd +3 ~/projet/uni/Singleton.md
badd +589 ~/.vimrc
badd +15 ~/projet/uni/Abstract_Factory.md
badd +1 ~/projet/uni/Prototype.md
badd +40 ~/projet/uni/Wrapper.md
badd +41 ~/projet/uni/Proxy.md
badd +7 ~/cours/imagerie_numerique/tps/1IN/TP1_Hategekimana_Fabrice.md
badd +51 ~/projet/uni/Decorator.md
badd +21 ~/projet/uni/Template.md
badd +6 ~/projet/uni/Flyweight.md
badd +16 ~/projet/uni/Command.md
badd +10 ~/projet/uni/Compose.md
badd +1 ~/projet/uni/Builder.md
badd +8 ~/projet/uni/Facade.md
badd +8 ~/projet/uni/Observer.md
badd +1 ~/projet/uni/State.md
badd +2 ~/projet/uni/all.md
badd +0 ~/projet/uni/courPdf/liens.md
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
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
