| **Authors**   | **Project** | **Build Status** |
|:-------------:|:-----------:|:----------------:|
| [**N. Curti**](https://github.com/Nico-Curti) | **CV** | **Linux** : [![Linux CI](https://github.com/Nico-Curti/curriculum/actions/workflows/linux.yml/badge.svg)](https://github.com/Nico-Curti/curriculum/actions/workflows/linux.yml) |

# My Personal Curriculum

In this folder I store the updated version of my CV ([ita](https://github.com/Nico-Curti/curriculum/blob/main/curriculum.pdf), [eng](https://github.com/Nico-Curti/curriculum/blob/main/curriculum_eng.pdf)).

### Usage

You can build the different version of the CV using the `make` command, according to the following rules

```bash
 italian versions
    make ita                 Build Italian version
    make signed              Build Italian version with signature
 english versions
    make eng                 Build English version
    make eng-signed          Build English version with signature
 useful info
    make publications        Build list of publications only
    make metrics             Extract metrics from Google Scholar and update plots
 utils and help
    make clean               Clean files
    make cleanall            Clean all files
    make help                show this help text.
```


| :warning: WARNING: The uploaded file does not include the signature image, i.e. `img/Firma.png` |
| ----------------------------------------------------------------------------------------------- |

| :triangular_flag_on_post: Note |
| :----------------------------- |
| The automated generation of pubblication report is obtained by `make publications`, exporting the *Pubblicazioni* section from the CV |
| **The pubblication report is automatically signed!** |
