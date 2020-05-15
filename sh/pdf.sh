
pdftotext $1.pdf - | less ou pdftohtml -stdout -i $1.pdf  | lynx -stdin
