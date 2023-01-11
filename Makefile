remove = rm -f
empty = /dev/null

file = curriculum.tex
out = curriculum

pub = publications.tex
pub_out = publications

all:$(file)
	cd script && python metrics.py && cd ..
	latexmk -g -synctex=1 -interaction=nonstopmode -file-line-error -pdf $(basename $(file)) -jobname=$(out) -pdflatex="/usr/bin/pdflatex --file-line-error --shell-escape --synctex=1 %O '\input{$(file)}'"
	$(MAKE) clean

signed:
	cd script && python metrics.py && cd ..
	latexmk -g -synctex=1 -interaction=nonstopmode -file-line-error -pdf $(basename $(file)) -jobname=$(out) -pdflatex="/usr/bin/pdflatex --file-line-error --shell-escape --synctex=1 %O '\def\signed{1}\input{$(file)}'"
	$(MAKE) clean

eng:
	cd script && python metrics.py && cd ..
	latexmk -g -synctex=1 -interaction=nonstopmode -file-line-error -pdf $(basename $(file)) -jobname=$(out)_eng -pdflatex="/usr/bin/pdflatex --file-line-error --shell-escape --synctex=1 %O '\def\eng{1}\input{$(file)}'"
	$(MAKE) clean

eng-signed:
	cd script && python metrics.py && cd ..
	latexmk -g -synctex=1 -interaction=nonstopmode -file-line-error -pdf $(basename $(file)) -jobname=$(out)_eng -pdflatex="/usr/bin/pdflatex --file-line-error --shell-escape --synctex=1 %O '\def\signed{1}\def\eng{1}\input{$(file)}'"
	$(MAKE) clean

publications:
	cd script && python metrics.py && cd ..
	cd script && python bibliography_generator.py && cd ..
	latexmk -g -synctex=1 -interaction=nonstopmode -file-line-error -pdf $(basename $(pub)) -jobname=$(pub_out) -pdflatex="/usr/bin/pdflatex --file-line-error --shell-escape --synctex=1 %O '\def\signed{1}\input{$(pub)}'"
	$(MAKE) clean

.PHONY: clean
clean:
	@$(remove) $(out).blg 2> $(empty)
	@$(remove) $(out).log 2> $(empty)
	@$(remove) $(out).out 2> $(empty)
	@$(remove) $(out).fls 2> $(empty)
	@$(remove) $(out).synctex.gz 2> $(empty)

	@$(remove) $(out)_eng.blg 2> $(empty)
	@$(remove) $(out)_eng.log 2> $(empty)
	@$(remove) $(out)_eng.out 2> $(empty)
	@$(remove) $(out)_eng.fls 2> $(empty)
	@$(remove) $(out)_eng.synctex.gz 2> $(empty)

	@$(remove) $(pub_out).blg 2> $(empty)
	@$(remove) $(pub_out).log 2> $(empty)
	@$(remove) $(pub_out).out 2> $(empty)
	@$(remove) $(pub_out).fls 2> $(empty)
	@$(remove) $(pub_out).synctex.gz 2> $(empty)

.PHONY: cleanall
cleanall: $(out) clean
	@$(remove) $(out).aux 2> $(empty)
	@$(remove) $(out).bbl 2> $(empty)
	@$(remove) $(out).fdb_latexmk 2> $(empty)

	@$(remove) $(out)_eng.aux 2> $(empty)
	@$(remove) $(out)_eng.bbl 2> $(empty)
	@$(remove) $(out)_eng.fdb_latexmk 2> $(empty)

	@$(remove) $(pub_out).aux 2> $(empty)
	@$(remove) $(pub_out).bbl 2> $(empty)
	@$(remove) $(pub_out).fdb_latexmk 2> $(empty)