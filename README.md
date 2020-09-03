# Docassemble JsonLoader

> A Python package for loading and manipulating Docassemble-generated JSON files.

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger)  [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## Installation

- From within Docassemble, select Package Management from the dropdown menu.
- In GitHub URL, enter the url for this repository: `https://github.com/hzerrad/docassemble-jsonloader`
- Select `master` as branch, and hit Update. 

### Clone

- Clone this repo to your local machine using `https://github.com/hzerrad/docassemble-jsonloader`
- Select `master` as branch, and hit Update. 

### Setup

- Once installed, you can start using JsonLoader in your docassemble by importing it:

> update and install this package first

```python
from jsonloader import JsonLoader
```

## Features
- Loads and parses Docassemble-generated JSON files into Python objects.
- Ability to access each element using Python conventions
    - Accessing third collection:
    ```python
    myjson.collections[2]
  ```
    - Getting a specific attribute from a form:
    ```python
  myjson.collections[0].title # or
  myjson.collections[0]['title']
  ```
- Manipulating record information (update)

## Usage
> Import package
```python
from jsonloader import JsonLoader
```
> Load JSON file
```python
myjson = JsonLoader('path/to/file.json')
```

> Extract and manipulate records
```python
# Get all forms
forms = myjson.forms

# Get number of forms available
forms.size()

# Get sectionSelector of a record
for c in myjson.collections:
    print(c.sectionSelector)

# Get collections by their sectionSelector
evidences = myjson.collections.filter('evidence')

# Update a record
evidences[0].title = 'My Title'
```
---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://github.com/hzerrad">Houssem Eddine Zerrad</a>