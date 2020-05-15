call plug#begin('~/.vim/plugged')

Plug 'https://github.com/keith/swift.vim.git'
Plug 'https://github.com/scrooloose/nerdtree.git'
Plug 'vimwiki/vimwiki'

call plug#end()

"pour que vimwiki fonctionne avec markdown
"let g:vimwiki_list = [{'path': '~/vimwiki/',
"                      \ 'syntax': 'markdown', 'ext': '.md'}]
let g:vimwiki_list = [{'path': '~/vimwiki/', 'syntax': 'markdown', 'ext': '.md'}]
"Quellesques définitions claires et simples pour le code en général
set number
set wildmenu
set splitbelow
set splitright
set ignorecase
set smartcase
set incsearch
"pour que vimwiki n'ait pas trop de problème
set nocompatible
filetype plugin on
syntax on

let g:syntastic_mode_map = { 
    \ "mode": "passive",
    \ "active_filetypes": ["ruby"],
    \ "passive_filetypes": ["puppet", "php"] }

":SyntasticToggleMode

"liste de fonction
function Console()
  !./.set.sh console "%"
endfunction


function Vimrc()
   let g:vimrc_window= 1-g:vimrc_window
   if g:vimrc_window == 0
	wq
   else
	vsplit $MYVIMRC
   endif
endfunction

"----------------------------------C--------------------------------

function RunC()
	let @o= system("gcc ".bufname('%')." -o main && ./main") 
	echo @o
endfunction

function CLike()
	"Raccourci pour le langage c, le java et le javascript
	nnoremap <buffer> ép oprintf("%s\n", );<Esc>hi
	nnoremap <buffer> ésp oprintf("\n");<Esc>4hi
	nnoremap <buffer> éc ^i//<Esc>$<CR>
	nnoremap <buffer> édc ^xx
	nnoremap <buffer> <F5> :call RunC()<CR>

	inoremap <buffer> print	printf("%", );
endfunction


"----------------------------------JAVA--------------------------------

function RunJava()
	let filepath = expand('%:p')
	let parentname = expand('%:p:h:t')
	let nomunique = expand('%:r')
	execute ":! cd .. && javac -d . ".parentname."/".bufname("%")." && java ".nomunique
endfunction

function Java()
	inoremap <buffer> system. System.out.println("")<Esc><Left>i
	nnoremap <buffer> éc ^i//<Esc>
	nnoremap <buffer> <F5> :call RunJava()<CR>
	nnoremap <buffer> <F6> :call Run2()<CR>
	nnoremap <buffer> <F2> :let note= call Note("java")<CR>
endfunction	


"----------------------------------PYTHON--------------------------------


function RunPython()
	let @o= system("python3 ".bufname('%')) 
	echo @o
endfunction

function Python()
	"Raccourci pour le langage python
	nnoremap <buffer> éc ^i#<Esc><CR>
	nnoremap <buffer> édc ^x 
	inoremap <buffer> print print()<Left>
	inoremap <buffer> printg print("")<Left><Left>
	inoremap <buffer> def<Space> def ():<Esc>F(i
	nnoremap <buffer> <F4> :!python3<CR>
	nnoremap <buffer> <F5> :call RunPython()<CR>
	nnoremap <buffer> nf /def <CR>
	nnoremap <buffer> pf ?def <CR>
endfunction


"----------------------------------OCTAVE--------------------------------


function RunOctave()
	let @o= system("octave ".bufname('%')) 
	echo @o
	echom "octave!"
endfunction

function OctaveLike()
	"Raccourci pour le langage octave
	nnoremap <buffer> éc ^i%<Esc><CR>
	nnoremap <buffer> édc ^x 
	nnoremap <buffer> <F2> :call Note("octave")<CR>
	nnoremap <buffer> <F4> :!octave --no-gui<CR>
	nnoremap <buffer> <F5> :call RunOctave()<CR>
endfunction


"----------------------------------latex et sh--------------------------------
function Note(fichier)
	let g:note= 1-g:note
	if g:note == 0
		wq
	else
		execute "vsplit ~/note/note_".a:fichier  
	endif
endfunction

function Latex()
	nnoremap <buffer> éé i\<Esc>
	nnoremap <buffer> és o\section{}<Esc>i
	nnoremap <buffer> éss o\subsection{}<Esc>i
	nnoremap <buffer> éi i\textit{}<Esc>i
	nnoremap <buffer> éb i\textbf{}<Esc>i
	nnoremap <buffer> éc i\textsf{}<Esc>i
	nnoremap <buffer> éii o\includegraphics[scale=1.2]{image}
	inoremap <CR> \\<CR> 
	nnoremap <buffer> <F2> :call Note("tex")<CR>
	nnoremap <buffer> <F5> :execute ":!pdflatex ".bufname("%")." && zathura ".expand('%:r').".pdf" <CR>
endfunctio

function Sh()
	nnoremap <buffer> éc ^i#<Esc><CR>
	nnoremap <buffer> <F2> :call Note("sh")<CR>
	inoremap <buffer> [ [<Space><Space>]<Left><Left>
	inoreab <buffer> elif elif<Space>[<Space>];<Space>then<CR><Up><Right><Right>
	inoreab <buffer> if if<Space>[<Space>];<Space>then<CR><CR>fi<Up><Up><Right><Right>
	inoreab <buffer> function (){<CR><CR>}<Up><Up>
	nnoremap <buffer> <F5> :!./%<CR>
endfunction


"-----------------------------------MYSQL---------------------------------------


function RunSql()
	let contenu= system("cat ".bufname("%"))
	execute ":!mysql -u user -pd367*WGa! -e ".contenu 
endfunction

function Sql()
	nnoremap <buffer> éc ^i/*<Esc>A*/<Esc>
	nnoremap <buffer> éd ^xx$xx
	nnoremap <buffer> <F4> :!mysql -u user -pd367*WGa!<CR>
	nnoremap <buffer> <F5> :call RunSql()<CR>
endfunction


"------------------------------------------MARKDOWN-------------------------------------
"
function MarkdownLigne()
	execute ":normal! yyo"
	let tab= split(@", "	")
	for i in tab
		let n= len(i)
		let @a= "-"	
		execute ":normal! ".n."\"apa	"
	endfor
endfunction

let liste= 0
function ListeMode(liste)
	let liste= a:liste	
	let liste= 1-liste	
	if liste == 0
		echom "mode liste désactivé"
		inoremap <buffer> <CR> <Space><Space><CR>
		nnoremap <buffer> <Tab> <Tab>
	else 
		echom "mode liste activé"
		inoremap <buffer> <CR> <CR><Tab>*<Space>
		nnoremap <buffer> <Tab> I<Tab>*<Space><Esc>
	endif
		return liste
endfunction

function MarkdownTitre()
	execute ":normal! yyo"		
	let n=  len(@")-1
	let @a= "="
	execute ":normal! ".n."\"ap"
endfunction

function RunMarkdown(toc)
	let nomunique = expand('%:r')
	if a:toc == 0
		execute ":!pandoc ".bufname('%')." ~/note/pandoc_latex.yaml -s -o pdf/".nomunique.".pdf && zathura pdf/".nomunique.".pdf"
	else
		execute ":!pandoc --toc ".bufname('%')." ~/note/pandoc_latex.yaml -s -o pdf/".nomunique.".pdf && zathura pdf/".nomunique.".pdf"
	endif
endfunction

function RunMarkdown2()
	let nomunique = expand('%:r')
	execute ":!pandoc ".bufname('%')." -s -H ~/note/gfm.css -o html/".nomunique.".html && firefox html/".nomunique.".html"
endfunction

function RunMarkdown3()
	let nomunique = expand('%:r')
	execute ":!pandoc ".bufname('%')." --toc --to=dokuwiki -o doku/".nomunique.".doku && gedit doku/".nomunique.".doku"
endfunction

function Toc(toc)
	let toc= a:toc	
	let toc= 1-toc	
	if toc == 0
		echom "table des matière désactivée"
	else 
		echom "table des matières activée"
	endif
		return toc
endfunction

function Markdown()
	"Markdown commands
	"mode normal
	nnoremap <buffer> ét :call MarkdownTitre()<CR>
	nnoremap <buffer> és <Esc>I##<Space><Esc>
	nnoremap <buffer> éss <Esc>I###<Space><Esc>
	nnoremap <buffer> ésss <Esc>I####<Space><Esc>
	nnoremap <buffer> él <Esc>:let liste= ListeMode(liste)<CR>
	nnoremap <buffer> éb I**<Esc>A**<Esc>
	inoremap <buffer> éta :call MarkdownLigne()<CR>

	inoremap <buffer> ééb ****<Left><Left>
	inoremap <buffer> ééit __<Left>
	inoremap <buffer> ééti #<Space>
	inoremap <buffer> éés <Esc>I##<Space>
	inoremap <buffer> ééss <Esc>I###<Space>
	inoremap <buffer> ééss <Esc>I####<Space>
	inoremap <buffer> ééta <Esc>:call MarkdownLigne()<CR>
	inoremap <buffer> ééd \begin{tikzpicture}<CR><CR>\end{tikzpicture}
	inoremap <buffer> éél <Esc>:let liste= ListeMode(liste)<CR>
	inoremap <buffer> ééim ![](images/num.png)<Esc>^<Right>a
	inoremap <buffer> éér \rectangle{nom}{x}{y}
	inoremap <buffer> ééff \fleche{nom1}{nom2}{label}
	inoremap <buffer> ééfff \flechel{nom1}{nom2}{label}{angleIn}{angleOut}
	nnoremap <buffer> <F2> :let note= Note(note, "markdown")<CR>
	nnoremap <buffer> <F4> :let toc= Toc(toc)<CR>
	nnoremap <buffer> <F5> :let toc= RunMarkdown(toc)<CR>
	nnoremap <buffer> <F6> :call RunMarkdown2()<CR>
	nnoremap <buffer> <F7> :call RunMarkdown3()<CR>

	inoremap <buffer> <CR> <Space><Space><CR>
endfunction

"---------------------------------------PROLOG-------------------------------------

function Swipl()
	nnoremap <buffer> <F4> :!swipl<CR>
	nnoremap <buffer> <F5> :!swipl %<CR>
	nnoremap <buffer> <F2> :let note= Note(note, "pl")<CR>
endfunction

"---------------------------------------PHP-------------------------------------

function RunPhp()
	let nomunique = expand('%:r')
	execute ":!php ".bufname('%')
endfunction

function Php()
	"mode normal
	nnoremap <buffer> php i<?php<CR><CR>><Up>
	nnoremap <buffer> <F5> :call RunPhp()<CR>
	nnoremap <buffer> éc ^i//<Esc>

	"mode insertinon
	inoremap <buffer> echo echo "\n";<Left><Left><Left><Left>
	inoremap <buffer> function function (){<CR><CR>}<Up><Up><Esc>A<Left><Left><Left>
	inoremap <buffer> elseif elseif(){<CR><CR>}<Up><Up><Esc>A<Left><Left>
	inoremap <buffer> if if(){<CR><CR>}<Up><Up><Esc>A<Left><Left>
	inoremap <buffer> else else{<CR><CR>}<Up>
	inoremap <buffer> post $_POST['']<Left><Left>
endfunction 

function NoteWindow()
	let g:note= 0
	nnoremap <buffer> <F2> :wq<CR>
endfunction

"commandes en command mode
command O e .
command Vimrc :vsplit \~\/\.vimrc<CR>

"autocommande
autocmd FileType c call CLike()
autocmd FileType java call Java()
autocmd FileType javascript call CLike()
autocmd FileType python call Python()
autocmd FileType octave call OctaveLike()
autocmd FileType tex call Latex()
autocmd FileType sh call Sh()
autocmd FileType sql call Sql()
autocmd FileType markdown call Markdown()
autocmd BufReadPre *.m call OctaveLike()
autocmd BufReadPre *.pl call Swipl()
autocmd BufReadPre *.php call Php()
autocmd BufReadPre note_* call NoteWindow()

"Actions pour les plugins et les touches F1-F12
let g:vimrc_window= 0
nnoremap <F1> :call Vimrc()<CR>
nnoremap <F3> :!ranger<CR>
"pour faire une capture d'écran qui va directement dans le dossier images existant
nnoremap <F8> :~/sh/images.sh<CR>
nnoremap <F9> :so $VIMRUNTIME/syntax/hitest.vim<CR>
nnoremap <F12> :!clear<CR>
nnoremap <Space> .
nnoremap è :
nnoremap èè :wqall<CR>
nnoremap :w :mks!<CR>:w

function Collage(collage)
	let collage= a:collage
	let collage= 1-collage
	if collage == 1
		call CollageUnmap()
		echo "completion automatique desactivée"
	else
		call CollageMap()
		echo "completion automatique activée"
	endif
	return collage
endfunction

function CollageUnmap()
	inoremap " "
	inoremap ""  ""
	inoremap """ """
	inoremap ( (
	inoremap (( ((
	inoremap ((( (((
	inoremap [ [
	inoremap [[ [[
	inoremap [[[ [[[
	inoremap { {
	inoremap {{ {{
	inoremap {{{ {{{
	set nonumber
endfunction

function CollageMap()
	inoremap " ""<Left>
	inoremap "" "<Esc>
	inoremap """  "<Esc>A"<Esc>
	inoremap ( ()<Left>
	inoremap (( (<Esc>
	inoremap (((  (<Esc>A)<Esc>
	inoremap { {}<Left> 
	inoremap {{ {<Esc> 
	inoremap {{{ {<Esc>A}<Esc> 
	inoremap [ []<left>
	inoremap [[ [<Esc>
	inoremap [[[ [<Esc>A]<Esc> 
	set number
endfunction


"Raccourci pour le code en général
let collage= 0
call CollageMap()
let g:note= 0
let toc= 0
nnoremap éo o<Esc>O
nnoremap éé "
nnoremap vp  :vsp .<CR>
nnoremap tn  :tabnew .<CR>
inoremap <C-D>  <><left>
inoremap <C-D><C-D>  </><left>
nnoremap gi Gi<CR>
nnoremap go Go<CR>
inoremap <C-W> <Esc>:w<CR>
inoremap <C-L> <Right>
inoremap <C-Y> <C-X><C-P>
nnoremap <C-V> :let collage= Collage(collage)<CR>
nnoremap count :call Comptage()<CR>
"recherche google
nnoremap <C-G> :!. ~/sh/g.sh 
