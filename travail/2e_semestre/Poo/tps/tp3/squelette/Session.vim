let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
imap <C-G>S <Plug>ISurround
imap <C-G>s <Plug>Isurround
inoremap <C-C> 
inoremap <C-S> <Right>
nnoremap <NL> }
nnoremap  {
nnoremap   .
nnoremap ! :!
xmap S <Plug>VSurround
nmap cS <Plug>CSurround
nmap cs <Plug>Csurround
nnoremap cp :CpL 
nmap ds <Plug>Dsurround
xmap gS <Plug>VgSurround
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
onoremap ins :call search("'") | normal! lvt'
onoremap ips :call search("'",'b') | normal! lvt'
onoremap in} :call search('{') | normal! lvi}
onoremap in] :call search('[') | normal! lvi]
onoremap in) :call search('(') | normal! lvi)
onoremap ip} :call search('{','b') | normal! lvi}
onoremap ip] :call search('[','b') | normal! lvi]
onoremap ip) :call search('(','b') | normal! lvi)
onoremap lp :normal t)vF,
onoremap nc :call search('//') | normal! llv$h
onoremap ns :call search('"') | normal! lvt"
onoremap nv :call search('=') | normal! llvt;
onoremap n' :normal f'lvt'
onoremap n" :normal f"lvt"
onoremap ps :call search('"','b') | normal! lvt"
onoremap pv :call search('=','b') | normal! llv$h
nnoremap sp :split .
nnoremap tn :LfNewTab
nnoremap vp :vsplit .
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
nnoremap <C-J> }
nnoremap <C-K> {
nnoremap <F12> :!clear
nnoremap <F10> :!gedit %
nnoremap <F9> :so $VIMRUNTIME/syntax/hitest.vim
nnoremap <F7> :make 
nnoremap <F3> :! ~/sh/mymake 
nnoremap <F2> :call Note()
nnoremap <F1> :tabnew ~/.vimrc
inoremap  
imap S <Plug>ISurround
imap s <Plug>Isurround
inoremap  <Right>
inoremap """ "A"
inoremap "" "
inoremap " ""<Left>
inoremap ((( (A)
inoremap (( (
inoremap ( ()<Left>
nmap écf G:call search('}','b')ofunction 
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
vmap <silent> éa :call AppendToTextObject(visualmode(), 1)
vmap <silent> éi :call InsertToTextObject(visualmode(), 1)
nmap <silent> éi :set opfunc=InsertToTextObjectg@
nnoremap éq :set opfunc=DoubleQuoteOperatorg@
nmap <silent> éa :set opfunc=AppendToTextObjectg@
nnoremap ékt :g!//d
nnoremap étb :TagbarToggle
nnoremap éns /"
nnoremap éct :Ctags
nnoremap édb :cope
nnoremap èè :call MakefileFunction()
xnoremap éspa :call MakeSpace()
inoremap [[[ [A] 
inoremap [[ [
inoremap [ []<Left>
inoremap {{{ {A} 
inoremap {{ { 
inoremap { {}<Left> 
let &cpo=s:cpo_save
unlet s:cpo_save
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
set matchpairs=(:),{:},[:],<:>
set nomodeline
set pastetoggle=<F8>
set path=.,/usr/include,,,**
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/pack/tpope/start/surround,~/.vim/pack/default/start/pythoncomplete,~/.vim/plugged/vimwiki/,~/.vim/plugged/hardmode/,~/.vim/plugged/lf.vim/,~/.vim/plugged/vim-javacomplete2/,~/.vim/plugged/AutoComplPop/,~/.vim/plugged/tagbar/,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after
set shiftwidth=4
set smartcase
set spelllang=fr_ch,en_us
set splitbelow
set splitright
set statusline=%#Cursor#\ VIM\ \ %#Normal#%{(mode()=='n')?'\ \ NORMAL\ ':''}%#PmenuThumb#%{(mode()=='i')?'\ \ INSERT\ ':''}%#TabLineFill#%{(mode()=='r')?'\ \ REPLACE\ ':''}%#SpellRare#%{(mode()=='v')?'\ \ VISUAL\ ':''}%#LineNr#\ %n\ %#Visual#%#CursorIM#%R%M%#Cursor#%#CursorLine#\ %t\ %=%#LineNr#\ %3l:%-2c\ %#Normal#\ %Y\ %#Cursor#%3p%%\ 
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc,.class
set suffixesadd=.java
set noswapfile
set timeoutlen=500
set virtualedit=onemore
set wildmenu
set window=22
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/projet/travail/2e_semestre/Poo/tps/tp2/squelette
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd Game.java
set stal=2
tabnew
tabrewind
edit Game.java
set splitbelow splitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
balt ch/unige/cui/rpg/Quest.java
let s:cpo_save=&cpo
set cpo&vim
imap <buffer> <silent> <C-J>a <Plug>(JavaComplete-Generate-AccessorSetterGetter)
imap <buffer> <silent> <C-J>g <Plug>(JavaComplete-Generate-AccessorGetter)
imap <buffer> <silent> <C-J>s <Plug>(JavaComplete-Generate-AccessorSetter)
imap <buffer> <silent> <C-J>jM <Plug>(JavaComplete-Generate-AbstractMethods)
imap <buffer> <silent> <C-J>ii <Plug>(JavaComplete-Imports-Add)
imap <buffer> <silent> <C-J>i <Plug>(JavaComplete-Imports-AddSmart)
imap <buffer> <silent> <C-J>R <Plug>(JavaComplete-Imports-RemoveUnused)
imap <buffer> <silent> <C-J>I <Plug>(JavaComplete-Imports-AddMissing)
nnoremap <buffer> <F6> :New 
nnoremap <buffer> <F5> :terminal ++shell find . -type f -name "*.class" -delete && javac %:p:h:r/*.java && java %
nnoremap <buffer> <F4> :terminal ++close ++shell cd %:p:h && jdb %:t:r
imap <buffer> <silent> <NL>a <Plug>(JavaComplete-Generate-AccessorSetterGetter)
imap <buffer> <silent> <NL>g <Plug>(JavaComplete-Generate-AccessorGetter)
imap <buffer> <silent> <NL>s <Plug>(JavaComplete-Generate-AccessorSetter)
imap <buffer> <silent> <NL>jM <Plug>(JavaComplete-Generate-AbstractMethods)
imap <buffer> <silent> <NL>ii <Plug>(JavaComplete-Imports-Add)
imap <buffer> <silent> <NL>i <Plug>(JavaComplete-Imports-AddSmart)
imap <buffer> <silent> <NL>R <Plug>(JavaComplete-Imports-RemoveUnused)
imap <buffer> <silent> <NL>I <Plug>(JavaComplete-Imports-AddMissing)
nmap <buffer> <silent> àjN <Plug>(JavaComplete-Generate-ClassInFile)
nmap <buffer> <silent> àjn <Plug>(JavaComplete-Generate-NewClass)
vmap <buffer> <silent> àja <Plug>(JavaComplete-Generate-AccessorSetterGetter)
vmap <buffer> <silent> àjg <Plug>(JavaComplete-Generate-AccessorGetter)
vmap <buffer> <silent> àjs <Plug>(JavaComplete-Generate-AccessorSetter)
nmap <buffer> <silent> àjcc <Plug>(JavaComplete-Generate-DefaultConstructor)
nmap <buffer> <silent> àjc <Plug>(JavaComplete-Generate-Constructor)
nmap <buffer> <silent> àjeq <Plug>(JavaComplete-Generate-EqualsAndHashCode)
nmap <buffer> <silent> àjts <Plug>(JavaComplete-Generate-ToString)
nmap <buffer> <silent> àja <Plug>(JavaComplete-Generate-AccessorSetterGetter)
nmap <buffer> <silent> àjg <Plug>(JavaComplete-Generate-AccessorGetter)
nmap <buffer> <silent> àjs <Plug>(JavaComplete-Generate-AccessorSetter)
nmap <buffer> <silent> àjA <Plug>(JavaComplete-Generate-Accessors)
nmap <buffer> <silent> àjM <Plug>(JavaComplete-Generate-AbstractMethods)
nmap <buffer> <silent> àjis <Plug>(JavaComplete-Imports-SortImports)
nmap <buffer> <silent> àjii <Plug>(JavaComplete-Imports-Add)
nmap <buffer> <silent> àji <Plug>(JavaComplete-Imports-AddSmart)
nmap <buffer> <silent> àjR <Plug>(JavaComplete-Imports-RemoveUnused)
nmap <buffer> <silent> àjI <Plug>(JavaComplete-Imports-AddMissing)
xnoremap <buffer> éd :normal ^xx
nnoremap <buffer> éd ^xx
xnoremap <buffer> éc :normal I//
nnoremap <buffer> éc ^i//
nnoremap <buffer> énv /\w\+\(\.\w\+\)\=\(\w\+\)\=\(;\|\ =[^;]\+;\)
nnoremap <buffer> énF :/\(public\|private\) \(static \)\=\w\+ \w\+(/normal! f(B
nnoremap <buffer> énf /\(public\|private\)\ \(static\ \)\=\w\+\ \w\+(
nnoremap <buffer> ésr yiw:Search 
nnoremap <buffer> égrn yiw:let @/=@":call SearchFunction2() | GRename 
nnoremap <buffer> érn yiw:Rename 
inoremap <buffer> print System.out.println();<Left>i
inoreabbr <buffer> for for(int i= 0; i<len; i++){}<Up>
inoreabbr <buffer> while while(){}<Up>t)a
inoreabbr <buffer> try try{}catch(InterruptedException e){System.out.println("Erreur");}<Up><Up><Up><Up>
inoreabbr <buffer> else else{}<Up>
inoreabbr <buffer> if if(){}<Up>t)a
inoreabbr <buffer> function public void (){}<Up>$Tda
let &cpo=s:cpo_save
unlet s:cpo_save
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
setlocal cinoptions=j1
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=sO:*\ -,mO:*\ \ ,exO:*/,s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=//%s
setlocal complete=.,w,b,u,t,i,kspell
setlocal concealcursor=
setlocal conceallevel=0
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
if &filetype != 'java'
setlocal filetype=java
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
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=GetJavaIndent()
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e,0=extends,0=implements
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
setlocal omnifunc=javacomplete#Complete
setlocal path=.,/usr/include,,,**
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
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=.java
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'java'
setlocal syntax=java
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
let s:l = 4 - ((3 * winheight(0) + 10) / 20)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 4
normal! 0
tabnext
edit ch/unige/cui/rpg/Character.java
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 60 + 61) / 122)
exe 'vert 2resize ' . ((&columns * 61 + 61) / 122)
argglobal
balt ~/projet/travail/2e_semestre/Poo/tps/tp2/squelette
let s:cpo_save=&cpo
set cpo&vim
imap <buffer> <silent> <C-J>a <Plug>(JavaComplete-Generate-AccessorSetterGetter)
imap <buffer> <silent> <C-J>g <Plug>(JavaComplete-Generate-AccessorGetter)
imap <buffer> <silent> <C-J>s <Plug>(JavaComplete-Generate-AccessorSetter)
imap <buffer> <silent> <C-J>jM <Plug>(JavaComplete-Generate-AbstractMethods)
imap <buffer> <silent> <C-J>ii <Plug>(JavaComplete-Imports-Add)
imap <buffer> <silent> <C-J>i <Plug>(JavaComplete-Imports-AddSmart)
imap <buffer> <silent> <C-J>R <Plug>(JavaComplete-Imports-RemoveUnused)
imap <buffer> <silent> <C-J>I <Plug>(JavaComplete-Imports-AddMissing)
nnoremap <buffer> <F6> :New 
nnoremap <buffer> <F5> :terminal ++shell find . -type f -name "*.class" -delete && javac %:p:h:r/*.java && java %
nnoremap <buffer> <F4> :terminal ++close ++shell cd %:p:h && jdb %:t:r
imap <buffer> <silent> <NL>a <Plug>(JavaComplete-Generate-AccessorSetterGetter)
imap <buffer> <silent> <NL>g <Plug>(JavaComplete-Generate-AccessorGetter)
imap <buffer> <silent> <NL>s <Plug>(JavaComplete-Generate-AccessorSetter)
imap <buffer> <silent> <NL>jM <Plug>(JavaComplete-Generate-AbstractMethods)
imap <buffer> <silent> <NL>ii <Plug>(JavaComplete-Imports-Add)
imap <buffer> <silent> <NL>i <Plug>(JavaComplete-Imports-AddSmart)
imap <buffer> <silent> <NL>R <Plug>(JavaComplete-Imports-RemoveUnused)
imap <buffer> <silent> <NL>I <Plug>(JavaComplete-Imports-AddMissing)
nmap <buffer> <silent> àjN <Plug>(JavaComplete-Generate-ClassInFile)
nmap <buffer> <silent> àjn <Plug>(JavaComplete-Generate-NewClass)
vmap <buffer> <silent> àja <Plug>(JavaComplete-Generate-AccessorSetterGetter)
vmap <buffer> <silent> àjg <Plug>(JavaComplete-Generate-AccessorGetter)
vmap <buffer> <silent> àjs <Plug>(JavaComplete-Generate-AccessorSetter)
nmap <buffer> <silent> àjcc <Plug>(JavaComplete-Generate-DefaultConstructor)
nmap <buffer> <silent> àjc <Plug>(JavaComplete-Generate-Constructor)
nmap <buffer> <silent> àjeq <Plug>(JavaComplete-Generate-EqualsAndHashCode)
nmap <buffer> <silent> àjts <Plug>(JavaComplete-Generate-ToString)
nmap <buffer> <silent> àja <Plug>(JavaComplete-Generate-AccessorSetterGetter)
nmap <buffer> <silent> àjg <Plug>(JavaComplete-Generate-AccessorGetter)
nmap <buffer> <silent> àjs <Plug>(JavaComplete-Generate-AccessorSetter)
nmap <buffer> <silent> àjA <Plug>(JavaComplete-Generate-Accessors)
nmap <buffer> <silent> àjM <Plug>(JavaComplete-Generate-AbstractMethods)
nmap <buffer> <silent> àjis <Plug>(JavaComplete-Imports-SortImports)
nmap <buffer> <silent> àjii <Plug>(JavaComplete-Imports-Add)
nmap <buffer> <silent> àji <Plug>(JavaComplete-Imports-AddSmart)
nmap <buffer> <silent> àjR <Plug>(JavaComplete-Imports-RemoveUnused)
nmap <buffer> <silent> àjI <Plug>(JavaComplete-Imports-AddMissing)
xnoremap <buffer> éd :normal ^xx
nnoremap <buffer> éd ^xx
xnoremap <buffer> éc :normal I//
nnoremap <buffer> éc ^i//
nnoremap <buffer> énv /\w\+\(\.\w\+\)\=\(\w\+\)\=\(;\|\ =[^;]\+;\)
nnoremap <buffer> énF :/\(public\|private\) \(static \)\=\w\+ \w\+(/normal! f(B
nnoremap <buffer> énf /\(public\|private\)\ \(static\ \)\=\w\+\ \w\+(
inoremap <buffer> print System.out.println();<Left>i
inoreabbr <buffer> for for(int i= 0; i<len; i++){}<Up>
inoreabbr <buffer> while while(){}<Up>t)a
inoreabbr <buffer> try try{}catch(InterruptedException e){System.out.println("Erreur");}<Up><Up><Up><Up>
inoreabbr <buffer> else else{}<Up>
inoreabbr <buffer> if if(){}<Up>t)a
inoreabbr <buffer> function public void (){}<Up>$Tda
let &cpo=s:cpo_save
unlet s:cpo_save
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
setlocal cinoptions=j1
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=sO:*\ -,mO:*\ \ ,exO:*/,s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=//%s
setlocal complete=.,w,b,u,t,i,kspell
setlocal concealcursor=
setlocal conceallevel=0
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
if &filetype != 'java'
setlocal filetype=java
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
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=GetJavaIndent()
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e,0=extends,0=implements
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
setlocal omnifunc=javacomplete#Complete
setlocal path=.,/usr/include,,,**
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
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=.java
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'java'
setlocal syntax=java
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
let s:l = 1 - ((0 * winheight(0) + 10) / 20)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
argglobal
if bufexists("ch/unige/cui/rpg/Quest.java") | buffer ch/unige/cui/rpg/Quest.java | else | edit ch/unige/cui/rpg/Quest.java | endif
balt ch/unige/cui/rpg
let s:cpo_save=&cpo
set cpo&vim
imap <buffer> <silent> <C-J>a <Plug>(JavaComplete-Generate-AccessorSetterGetter)
imap <buffer> <silent> <C-J>g <Plug>(JavaComplete-Generate-AccessorGetter)
imap <buffer> <silent> <C-J>s <Plug>(JavaComplete-Generate-AccessorSetter)
imap <buffer> <silent> <C-J>jM <Plug>(JavaComplete-Generate-AbstractMethods)
imap <buffer> <silent> <C-J>ii <Plug>(JavaComplete-Imports-Add)
imap <buffer> <silent> <C-J>i <Plug>(JavaComplete-Imports-AddSmart)
imap <buffer> <silent> <C-J>R <Plug>(JavaComplete-Imports-RemoveUnused)
imap <buffer> <silent> <C-J>I <Plug>(JavaComplete-Imports-AddMissing)
nnoremap <buffer> <F6> :New 
nnoremap <buffer> <F5> :terminal ++shell find . -type f -name "*.class" -delete && javac %:p:h:r/*.java && java %
nnoremap <buffer> <F4> :terminal ++close ++shell cd %:p:h && jdb %:t:r
imap <buffer> <silent> <NL>a <Plug>(JavaComplete-Generate-AccessorSetterGetter)
imap <buffer> <silent> <NL>g <Plug>(JavaComplete-Generate-AccessorGetter)
imap <buffer> <silent> <NL>s <Plug>(JavaComplete-Generate-AccessorSetter)
imap <buffer> <silent> <NL>jM <Plug>(JavaComplete-Generate-AbstractMethods)
imap <buffer> <silent> <NL>ii <Plug>(JavaComplete-Imports-Add)
imap <buffer> <silent> <NL>i <Plug>(JavaComplete-Imports-AddSmart)
imap <buffer> <silent> <NL>R <Plug>(JavaComplete-Imports-RemoveUnused)
imap <buffer> <silent> <NL>I <Plug>(JavaComplete-Imports-AddMissing)
nmap <buffer> <silent> àjN <Plug>(JavaComplete-Generate-ClassInFile)
nmap <buffer> <silent> àjn <Plug>(JavaComplete-Generate-NewClass)
vmap <buffer> <silent> àja <Plug>(JavaComplete-Generate-AccessorSetterGetter)
vmap <buffer> <silent> àjg <Plug>(JavaComplete-Generate-AccessorGetter)
vmap <buffer> <silent> àjs <Plug>(JavaComplete-Generate-AccessorSetter)
nmap <buffer> <silent> àjcc <Plug>(JavaComplete-Generate-DefaultConstructor)
nmap <buffer> <silent> àjc <Plug>(JavaComplete-Generate-Constructor)
nmap <buffer> <silent> àjeq <Plug>(JavaComplete-Generate-EqualsAndHashCode)
nmap <buffer> <silent> àjts <Plug>(JavaComplete-Generate-ToString)
nmap <buffer> <silent> àja <Plug>(JavaComplete-Generate-AccessorSetterGetter)
nmap <buffer> <silent> àjg <Plug>(JavaComplete-Generate-AccessorGetter)
nmap <buffer> <silent> àjs <Plug>(JavaComplete-Generate-AccessorSetter)
nmap <buffer> <silent> àjA <Plug>(JavaComplete-Generate-Accessors)
nmap <buffer> <silent> àjM <Plug>(JavaComplete-Generate-AbstractMethods)
nmap <buffer> <silent> àjis <Plug>(JavaComplete-Imports-SortImports)
nmap <buffer> <silent> àjii <Plug>(JavaComplete-Imports-Add)
nmap <buffer> <silent> àji <Plug>(JavaComplete-Imports-AddSmart)
nmap <buffer> <silent> àjR <Plug>(JavaComplete-Imports-RemoveUnused)
nmap <buffer> <silent> àjI <Plug>(JavaComplete-Imports-AddMissing)
xnoremap <buffer> éd :normal ^xx
nnoremap <buffer> éd ^xx
xnoremap <buffer> éc :normal I//
nnoremap <buffer> éc ^i//
nnoremap <buffer> énv /\w\+\(\.\w\+\)\=\(\w\+\)\=\(;\|\ =[^;]\+;\)
nnoremap <buffer> énF :/\(public\|private\) \(static \)\=\w\+ \w\+(/normal! f(B
nnoremap <buffer> énf /\(public\|private\)\ \(static\ \)\=\w\+\ \w\+(
inoremap <buffer> print System.out.println();<Left>i
inoreabbr <buffer> for for(int i= 0; i<len; i++){}<Up>
inoreabbr <buffer> while while(){}<Up>t)a
inoreabbr <buffer> try try{}catch(InterruptedException e){System.out.println("Erreur");}<Up><Up><Up><Up>
inoreabbr <buffer> else else{}<Up>
inoreabbr <buffer> if if(){}<Up>t)a
inoreabbr <buffer> function public void (){}<Up>$Tda
let &cpo=s:cpo_save
unlet s:cpo_save
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
setlocal cinoptions=j1
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=sO:*\ -,mO:*\ \ ,exO:*/,s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=//%s
setlocal complete=.,w,b,u,t,i,kspell
setlocal concealcursor=
setlocal conceallevel=0
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
if &filetype != 'java'
setlocal filetype=java
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
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=GetJavaIndent()
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e,0=extends,0=implements
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
setlocal omnifunc=javacomplete#Complete
setlocal path=.,/usr/include,,,**
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
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=.java
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'java'
setlocal syntax=java
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
let s:l = 2 - ((1 * winheight(0) + 10) / 20)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 2
normal! 0
lcd ~/projet/travail/2e_semestre/Poo/tps/tp2/squelette
wincmd w
exe 'vert 1resize ' . ((&columns * 60 + 61) / 122)
exe 'vert 2resize ' . ((&columns * 61 + 61) / 122)
tabnext 1
set stal=1
badd +5 ~/projet/travail/2e_semestre/Poo/tps/tp2/squelette/Game.java
badd +9 ~/projet/travail/2e_semestre/Poo/tps/tp2/squelette/Makefile
badd +13 ~/projet/travail/2e_semestre/Poo/tps/tp2/squelette/ch/unige/cui/rpg/Character.java
badd +2 ~/projet/travail/2e_semestre/Poo/tps/tp2/squelette/ch/unige/cui/rpg/Quest.java
badd +0 ~/note/note_java.md
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
let &g:so = s:so_save | let &g:siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
