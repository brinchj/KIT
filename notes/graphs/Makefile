
pdf: 
	(echo -n "0."; git log | grep -E "^commit [0-9a-f]{40}" | wc -l) > version
	pdflatex grafteori.tex && pdflatex grafteori.tex

