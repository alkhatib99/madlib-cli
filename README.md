# Lab: 03 - Errors, Files, and Packaging

## Author: Abedalqader Alkhatib

- [Pull Request]()

---

### Estimate of time needed to complete

***5 h***

---

#### Start time: ***3:00 pm***

#### Finish time: ***6:00 pm***

#### Actual time needed to complete: ***3 h***

#### Version: ***1.0***

---

### Set it up

Use the following commands to set up the project:

```
$ poetry new madlib-cli
$ cd madlib-cli
$ poetry add --dev black --allow-prereleases
$ touch madlib-cli/madlib.py
$ mv README.rst README.md
$ git init
$ git add .
$ git commit -m "first commit"
$ git branch -M main
```

---

To start your enviornment use:
- ```$ poetry shell```

To run the program and see the output run:

- `$ python madlib.py` or `$ python3 madlib.py` depending on your seystem
