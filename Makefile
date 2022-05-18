remove = rm -f
empty = /dev/null

file = curriculum.tex
out = curriculum


all:$(file)
	latexmk -synctex=1 -bibtex -interaction=nonstopmode -file-line-error -pdf $(basename $(file)) -jobname=$(out)
	$(MAKE) clean

.PHONY: clean
clean:
	@$(remove) $(out).blg 2> $(empty)
	@$(remove) $(out).log 2> $(empty)
	@$(remove) $(out).out 2> $(empty)
	@$(remove) $(out).fls 2> $(empty)
	@$(remove) $(out).synctex.gz 2> $(empty)

.PHONY: cleanall
cleanall: $(out) clean
	@$(remove) $(out).aux 2> $(empty)
	@$(remove) $(out).bbl 2> $(empty)
	@$(remove) $(out).fdb_latexmk 2> $(empty)