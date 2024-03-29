<p align="center">
  <img src="https://raw.githubusercontent.com/matijakljajic/koznaznarevamp/main/resources/main/main.png" alt="logo">
  <h1 align="center" style="margin: 0 auto 0 auto;">KO ZNA ZNA - REVAMP</h1>
  </p>

[![portfolio](https://img.shields.io/badge/portfolio-2ea44f?style=for-the-badge)](https://matijakljajic.github.io/) [![Download](https://img.shields.io/badge/Download-2ea44f?style=for-the-badge)](https://github.com/matijakljajic/koznaznarevamp/releases/download/v1.0.3/KOZNAZNA103.exe)

A small project done in Python for one of the uni courses. 
It's kind of a fork of a Serbian TV show, but adapted for hosting pub quizes in Serbian.

Inspired by [Nenad Ilić](https://github.com/ilic5000) and his [pub quiz generator](https://github.com/ilic5000/pabkvizgenerator) made with the Anansi crawler.

*Some questions have issues because Anansi interpreted them in a wrong way but this can be fixed gradually with the report system I did (~~I intend to do~~)*

<p align="center">
<b><i>Please report the questions you find inadequate</i></b>
</p>

***UPDATE: Reports work, but won't be looked at. This repository is archived. There may be a version which will supersede this code.***

## Progress

- [x] Basic functionality
- [x] Basic UI and art
- [x] System intended for issue reporting
- [ ] Points system used in tandem with NLP library recognising if the typed answer is indeed correct


## Thought process

- Basic functionality is based upon ***qnagen.py***.
- Basic UI and art is something else to say the least. I used pygame and couple more libraries in combination with the art from the actual tv show. The whole project could have been done a lot faster if I used something else and not pygame. Will use Python just for scripts in the future - would rather use some other language for the GUI/UI etc.
- Issue reporting works using Discord webhooks (~~mail~~). If an issue with a question/answer has been found, the user can notify me to change it in the excel sheet in due time over a button.


## How to run

### Regular installation

- Download the latest release over the download button at the top of this README
- Install the program (It's preferable if you leave the default installation location, you can uninstall over control panel later if you want)
- Run

<sub>(When updating, it is recommended to deinstall the old version before installing the new one. You can ignore this  recommendation if you find it inconvenient)</sub>

### Over code

- If on Windows, execute run.bat to install needed libraries
- If on Linux/Mac, execute run.sh to install needed libraries
- Open game.py and run


## Copyright notice in Serbian
<sup>Овај рад нема намеру да крши било каква ауторска права. Ауторска права над именом "Слагалица" држи РТС и екипа.</sup>
