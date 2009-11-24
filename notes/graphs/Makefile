
pdf: 	version
	pdflatex graf-teori.tex && pdflatex graf-teori.tex

version: graf-teori.tex
	(echo -n "0."; git log | grep -E "^commit [0-9a-f]{40}" | wc -l) > version

