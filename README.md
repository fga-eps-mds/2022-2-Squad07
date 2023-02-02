# ez-docs

### What's up everyone!

ez-docs is a MVP (minimum viable product) Python project that were build for an SDM (Software Development Methods) class, with the aim of learn the goals of different approaches for creating software through agile practices.

So, we contribute to the Open Source community with ez-docs, which helps users to issue a wide range of certificates, declarations, resumes, receipts, slips, or whatever else the imagination allows through a database and a template in markdown format.

#### Realised features

- [x] Generate doc's in .pdf [#20](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/20)
- [ ] e-mail generated doc's [#24](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/24)
- [x] Package pip installation [#30](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/30)
- [x] Argparse commands [#39](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/39)
- [x] Run package via CLI [#43](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/43)

#### Realised doc's

- [x] Github Page [#31](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/31)
- [x] README [#32](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/32)
- [x] Product Backlog [#33](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/33)
- [x] about [#39](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/39)
- [x] architecture [#39](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/39)
- [x] help [#39](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/39)
- [x] list [#39](https://github.com/fga-eps-mds/2022-2-ez-docs/issues/39)

#### Bugs

* Semicolon separator on .csv files not working.
* Format .xlsx
* key_pattern optionality.
* flag=1/flag=2 always generating .md files.

## Prerequisites

Before starting, make sure you've met the following requirements:
* You have installed the latest version of `<Python>`.
* You have a `<Windows / Linux / Mac>` machine.
* You read the [project GitPage](https://fga-eps-mds.github.io/2022-2-ez-docs/index.html).


## Installation

To install *ez-docs*, open an interactive shell and run:
```bash
$ python3 -m pip install ez-docs
```
Then, to assure the faultless installation, run:
```bash
$ ez-docs --about
```
The terminal ought to print something like this:
```
=====About this project=====

	This project was developed by Software Engineering students at the University of Brasilia - Campus Gama (UnB-FGA) - during the 2022.2 semester, in the course of Software Development Methods (SDM), under the guidance of prof. Dr. Carla Rocha Aguiar.
    ...
```

## Using ez-docs

To start using *ez-docs*, you'll need a markdown template, a database (.csv, .xlsx, .json) and a pattern of keys.

* directory_template: str - template.md
    
   In your markdown template you must to indicate the fields that you want to replace for the values in database, with the following pattern of keys:  <<SAME_DATABASE_COLUMN_NAME>> 
       

    ![Template file example](/docs/images/template.png "Template file example")

* database: str - database.(csv, txt, xls)
    
    ![Database file example](/docs/images/database.png "Database file example")

* file_name_pattern: str - parameter concerning the denominator key of the document name, which must follow the format {key_pattern}.
For example, for a template that has the keys "name" and "registration", the output could be "name_registration", generating the following results:
    - Aaron_3141592653.pdf
    - Barnardo_2718281828.pdf
    - Caliban_4815162342.pdf

    Valid separators: registration_name, registration-name, registration:name, registration name.

* flag: int - optional parameter that defines the final format of each document.
    - 1 (def.) - The doc will be converted to .pdf
    - 2 - The doc will remain in .md

* zip: int - optional parameter that defines the final format of the set.
    - 0 (def.) - The set will be kept at folder ./output;
    - 1 - The files will be joint in a output.zip;

* constraint: str - optional parameter that sets a constraint for data filtering.
    Exemple: Suppose you have a data set of students' grades, and you would like to generate a certificate for those whose grades are greater or equal than 8. In this case, you could simply type: "... --constraint 'Grade >= 8.0' (assuming you really have a column named "Grade").

With that, you may open an interactive shell and run:
```bash
$ ez-docs <~/template.md> <~/database.csv> <pattern_keys> --flag=1 or 2
```

![](/docs/images/exampleofuse.gif)

## Special functionalities

ez-docs has some in-line functionalities. To use it, type one of the commands below in your terminal:

Project overview, contributors, etc:
```bash
$ ez-docs --about
```

Architecture stuff:
```bash
$ ez-docs --architecture
```

How to use tutorial:
```bash
$ ez-docs --help
```

List of all command line commands:
```bash
$ ez-docs --list
```

## Getting involved
1. Read the [CONTRIBUTING.md](https://github.com/fga-eps-mds/2022-2-ez-docs/blob/main/docs/CONTRIBUTING.md) guide.
2. Fork this repository.
3. Create a branch on your local machine: `git checkout -b <branch_name>`.
4. Make your changes and confirm them following the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): `git commit -m "commit_message"`
5. Send to origin branch: `git push origin <branch_name> / <local>`
6. Create pull request through Github.


## Open source licensing info

This project is under license. See the [LICENSE](LICENSE) file for details.

---
## So, take it easy, and use ez-docs to make your docs!

#### Special thanks to:
Dr. [Carla Rocha Aguiar](https://github.com/RochaCarla), our professor at the University of Brasília.

**_ez-docs Team_**  

*Created by [Bruno Ribeiro](https://github.com/BrunoRiibeiro), [Bruno Martins](https://github.com/gitbmvb), [Diógenes Dantas](https://github.com/diogjunior100), [Igor Penha](https://github.com/igorpenhaa), [Lucas Bergholz](https://github.com/LucasBergholz) and [Rafael Nobre](https://github.com/RafaelN0bre) in 2022*