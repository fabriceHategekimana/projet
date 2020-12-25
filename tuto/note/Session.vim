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
xmap S <Plug>VSurround
nmap cS <Plug>CSurround
nmap cs <Plug>Csurround
nnoremap cp :CpL 
nmap ds <Plug>Dsurround
xmap gS <Plug>VgSurround
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
onoremap in( :normal! f(vi(
nnoremap tn :LfNewTab
nnoremap vs :sp .
nnoremap vp :vsp .
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
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
set autowriteall
set background=dark
set backspace=indent,eol,start
set cindent
set complete=.,w,b,u,t,i,kspell
set fileencodings=ucs-bom,utf-8,default,latin1
set formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
set helplang=fr
set ignorecase
set incsearch
set laststatus=2
set omnifunc=syntaxComplete#Complete
set pastetoggle=<F8>
set path=.,/usr/include,,,**
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/pack/tpope/start/surround,~/.vim/plugged/swift.vim/,~/.vim/plugged/nerdtree/,~/.vim/plugged/vimwiki/,~/.vim/plugged/hardmode/,~/.vim/plugged/lf.vim/,~/.vim/plugged/vim-javacomplete2/,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after
set smartcase
set spelllang=fr_ch,en_us
set splitbelow
set splitright
set statusline=%#Cursor#\ VIM\ \ %#Normal#%{(mode()=='n')?'\ \ NORMAL\ ':''}%#PmenuThumb#%{(mode()=='i')?'\ \ INSERT\ ':''}%#TabLineFill#%{(mode()=='r')?'\ \ REPLACE\ ':''}%#SpellRare#%{(mode()=='v')?'\ \ VISUAL\ ':''}%#LineNr#\ %n\ %#Visual#%#CursorIM#%R%M%#Cursor#%#CursorLine#\ %t\ %=%#LineNr#\ %3l:%-2c\ %#Normal#\ %Y\ %#Cursor#%3p%%\ 
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set wildmenu
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/projet/tuto/note
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd note.md
edit ~/projet/tuto/note/exercices_compléments_a_10_20_etc.md
set splitbelow splitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <expr> <S-Tab> vimwiki#tbl#kbd_shift_tab()
inoremap <buffer> <silent> <S-CR> :VimwikiReturn 2 2
imap <buffer> <silent> <C-L><C-M> <Plug>VimwikiListToggle
imap <buffer> <silent> <C-L><C-K> <Plug>VimwikiListPrevSymbol
imap <buffer> <silent> <C-L><C-J> <Plug>VimwikiListNextSymbol
imap <buffer> <silent> <C-T> <Plug>VimwikiIncreaseLvlSingleItem
imap <buffer> <silent> <C-D> <Plug>VimwikiDecreaseLvlSingleItem
nmap <buffer> <silent> 	 <Plug>VimwikiNextLink
vmap <buffer> <silent>  <Plug>VimwikiNormalizeLinkVisualCR
nmap <buffer> <silent>  <Plug>VimwikiFollowLink
nnoremap <buffer>  :!. ~/sh/cs.sh
vmap <buffer> <silent> + <Plug>VimwikiNormalizeLinkVisual
nmap <buffer> <silent> + <Plug>VimwikiNormalizeLink
nmap <buffer> <silent> - <Plug>VimwikiRemoveHeaderLevel
nmap <buffer> <silent> <D-CR> <Plug>VimwikiTabnewLink
nmap <buffer> <silent> = <Plug>VimwikiAddHeaderLevel
inoremap <buffer> ééfff \flechel{nom1}{nom2}{label}{angleIn}{angleOut}
inoremap <buffer> ééff \fleche{nom1}{nom2}{label}
inoremap <buffer> éér \rectangle{nom}{x}{y}
inoremap <buffer> ééim ![](../../images/num.png)^<Right>a
inoremap <buffer> ééd \begin{tikzpicture}\end{tikzpicture}
inoremap <buffer> ééta :call MarkdownLigne()
inoremap <buffer> éém ``<Left>
inoremap <buffer> ééco ``````<Left><Left><Left><Up>
inoremap <buffer> éésss I#### 
inoremap <buffer> ééss I### 
inoremap <buffer> éés I## 
inoremap <buffer> ééti # 
inoremap <buffer> ééit __<Left>
inoremap <buffer> ééb ****<Left><Left>
nnoremap <buffer> <silent> O :call vimwiki#lst#kbd_O()
nmap <buffer> <silent> [= <Plug>VimwikiGoToPrevSiblingHeader
nmap <buffer> <silent> [[ <Plug>VimwikiGoToPrevHeader
nmap <buffer> <silent> [u <Plug>VimwikiGoToParentHeader
nmap <buffer> <silent> ]= <Plug>VimwikiGoToNextSiblingHeader
nmap <buffer> <silent> ]] <Plug>VimwikiGoToNextHeader
nmap <buffer> <silent> ]u <Plug>VimwikiGoToParentHeader
vnoremap <buffer> <silent> al :call vimwiki#lst#TO_list_item(0, 1)
onoremap <buffer> <silent> al :call vimwiki#lst#TO_list_item(0, 0)
vnoremap <buffer> <silent> ac :call vimwiki#base#TO_table_col(0, 1)
onoremap <buffer> <silent> ac :call vimwiki#base#TO_table_col(0, 0)
vnoremap <buffer> <silent> a\ :call vimwiki#base#TO_table_cell(0, 1)
onoremap <buffer> <silent> a\ :call vimwiki#base#TO_table_cell(0, 0)
vnoremap <buffer> <silent> aH :call vimwiki#base#TO_header(0, 1, v:count1)
onoremap <buffer> <silent> aH :call vimwiki#base#TO_header(0, 1, v:count1)
vnoremap <buffer> <silent> ah :call vimwiki#base#TO_header(0, 0, v:count1)
onoremap <buffer> <silent> ah :call vimwiki#base#TO_header(0, 0, v:count1)
nnoremap <buffer> gww :VimwikiTableAlignW
nnoremap <buffer> gqq :VimwikiTableAlignQ
noremap <buffer> <silent> gL1 :VimwikiChangeSymbolInListTo 1.
noremap <buffer> <silent> gl1 :VimwikiChangeSymbolTo 1.
noremap <buffer> <silent> gL+ :VimwikiChangeSymbolInListTo +
noremap <buffer> <silent> gl+ :VimwikiChangeSymbolTo +
noremap <buffer> <silent> gL* :VimwikiChangeSymbolInListTo *
noremap <buffer> <silent> gl* :VimwikiChangeSymbolTo *
noremap <buffer> <silent> gL- :VimwikiChangeSymbolInListTo -
noremap <buffer> <silent> gl- :VimwikiChangeSymbolTo -
map <buffer> <silent> gL  <Plug>VimwikiRemoveCBInList
map <buffer> <silent> gl  <Plug>VimwikiRemoveSingleCB
map <buffer> <silent> gLL <Plug>VimwikiIncreaseLvlWholeItem
map <buffer> <silent> gLl <Plug>VimwikiIncreaseLvlWholeItem
map <buffer> <silent> gLH <Plug>VimwikiDecreaseLvlWholeItem
map <buffer> <silent> gLh <Plug>VimwikiDecreaseLvlWholeItem
map <buffer> <silent> gll <Plug>VimwikiIncreaseLvlSingleItem
map <buffer> <silent> glh <Plug>VimwikiDecreaseLvlSingleItem
nmap <buffer> <silent> gLR <Plug>VimwikiRenumberAllLists
nmap <buffer> <silent> gLr <Plug>VimwikiRenumberAllLists
nmap <buffer> <silent> glr <Plug>VimwikiRenumberList
vmap <buffer> <silent> glp <Plug>VimwikiDecrementListItem
nmap <buffer> <silent> glp <Plug>VimwikiDecrementListItem
vmap <buffer> <silent> gln <Plug>VimwikiIncrementListItem
nmap <buffer> <silent> gln <Plug>VimwikiIncrementListItem
vmap <buffer> <silent> glx <Plug>VimwikiToggleRejectedListItem
nmap <buffer> <silent> glx <Plug>VimwikiToggleRejectedListItem
vnoremap <buffer> <silent> il :call vimwiki#lst#TO_list_item(1, 1)
onoremap <buffer> <silent> il :call vimwiki#lst#TO_list_item(1, 0)
vnoremap <buffer> <silent> ic :call vimwiki#base#TO_table_col(1, 1)
onoremap <buffer> <silent> ic :call vimwiki#base#TO_table_col(1, 0)
vnoremap <buffer> <silent> i\ :call vimwiki#base#TO_table_cell(1, 1)
onoremap <buffer> <silent> i\ :call vimwiki#base#TO_table_cell(1, 0)
vnoremap <buffer> <silent> iH :call vimwiki#base#TO_header(1, 1, v:count1)
onoremap <buffer> <silent> iH :call vimwiki#base#TO_header(1, 1, v:count1)
vnoremap <buffer> <silent> ih :call vimwiki#base#TO_header(1, 0, v:count1)
onoremap <buffer> <silent> ih :call vimwiki#base#TO_header(1, 0, v:count1)
nnoremap <buffer> <silent> o :call vimwiki#lst#kbd_o()
nnoremap <buffer> <silent> <Plug>VimwikiGoToPrevSiblingHeader :call vimwiki#base#goto_sibling(-1)
nnoremap <buffer> <silent> <Plug>VimwikiGoToNextSiblingHeader :call vimwiki#base#goto_sibling(+1)
nnoremap <buffer> <silent> <Plug>VimwikiGoToPrevHeader :call vimwiki#base#goto_prev_header()
nnoremap <buffer> <silent> <Plug>VimwikiGoToNextHeader :call vimwiki#base#goto_next_header()
nnoremap <buffer> <silent> <Plug>VimwikiGoToParentHeader :call vimwiki#base#goto_parent_header()
nnoremap <buffer> <silent> <Plug>VimwikiRemoveHeaderLevel :call vimwiki#base#RemoveHeaderLevel()
nnoremap <buffer> <silent> <Plug>VimwikiAddHeaderLevel :call vimwiki#base#AddHeaderLevel()
nmap <buffer> <silent> <M-Right> <Plug>VimwikiTableMoveColumnRight
nmap <buffer> <silent> <M-Left> <Plug>VimwikiTableMoveColumnLeft
vmap <buffer> <silent> <C-@> <Plug>VimwikiToggleListItem
vmap <buffer> <silent> <Nul> <Plug>VimwikiToggleListItem
nmap <buffer> <silent> <C-@> <Plug>VimwikiToggleListItem
nmap <buffer> <silent> <Nul> <Plug>VimwikiToggleListItem
vmap <buffer> <silent> <C-Space> <Plug>VimwikiToggleListItem
nmap <buffer> <silent> <C-Space> <Plug>VimwikiToggleListItem
nmap <buffer> <silent> <C-Up> <Plug>VimwikiDiaryPrevDay
nmap <buffer> <silent> <C-Down> <Plug>VimwikiDiaryNextDay
nmap <buffer> <silent> <S-Tab> <Plug>VimwikiPrevLink
nmap <buffer> <silent> <BS> <Plug>VimwikiGoBackLink
nmap <buffer> <silent> <C-S-CR> <Plug>VimwikiTabnewLink
nmap <buffer> <silent> <C-CR> <Plug>VimwikiVSplitLink
nmap <buffer> <silent> <S-CR> <Plug>VimwikiSplitLink
xnoremap <buffer> <F8> y:call AddTask()
nnoremap <buffer> <F6> :call Imagerie()
nnoremap <buffer> <F5> :!bash ~/sh/compmd % 
nnoremap <buffer> <F4> :call LinkImage()
nnoremap <buffer> <F2> :let note= Note("markdown")
nnoremap <buffer> <C-P> :!. ~/sh/cs.sh
imap <buffer> <silent>  <Plug>VimwikiDecreaseLvlSingleItem
inoremap <buffer> <expr> 	 vimwiki#tbl#kbd_tab()
imap <buffer> <silent>  <Plug>VimwikiListToggle
imap <buffer> <silent>  <Plug>VimwikiListPrevSymbol
imap <buffer> <silent> <NL> <Plug>VimwikiListNextSymbol
inoremap <buffer> <silent>  :VimwikiReturn 1 5
imap <buffer> <silent>  <Plug>VimwikiIncreaseLvlSingleItem
nmap <buffer> <silent> àwr <Plug>VimwikiRenameLink
nmap <buffer> <silent> àwd <Plug>VimwikiDeleteLink
nmap <buffer> àwhh <Plug>Vimwiki2HTMLBrowse
nmap <buffer> àwh <Plug>Vimwiki2HTML
xnoremap <buffer> ém di``<Left>p
nnoremap <buffer> ém bi`ea`
nnoremap <buffer> éim i![](../../images/num.png)^<Right>a
nnoremap <buffer> éco i``````<Left><Left><Left><Up>
xnoremap <buffer> éb di****2<Left>p
nnoremap <buffer> éb I**A**
nnoremap <buffer> ésss I#### 
nnoremap <buffer> éss I### 
nnoremap <buffer> és I## 
nnoremap <buffer> éta :VimwikiTable
nnoremap <buffer> ét :call MarkdownTitre()
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
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
setlocal comments=
setlocal commentstring=%%%s
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
if &filetype != 'vimwiki'
setlocal filetype=vimwiki
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
setlocal formatoptions=tqn
setlocal formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
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
setlocal omnifunc=Complete_wikifiles
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
setlocal spelllang=fr_ch,en_us
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=.md
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'vimwiki'
setlocal syntax=vimwiki
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tagfunc=
setlocal tags=./tags,./TAGS,tags,TAGS,~/.tags
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
let s:l = 3 - ((2 * winheight(0) + 14) / 29)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
3
normal! 0
tabnext 1
badd +7 note.md
badd +6 ~/projet/tuto/note/math.md
badd +20 ~/projet/tuto/note/complément_a_10.md
badd +3 ~/projet/tuto/note/exercices_compléments_a_10_20_etc.md
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
