# mangosort: Sort list by multiple keys and directions
**mangosort** is a small module that helps you sort lists of dictionaries by multiple keys

[![Build Status](https://travis-ci.com/raulmangolin/mangosort.svg?token=QfPxoKSpBQKuzP1gqVAS&branch=master)](https://travis-ci.com/raulmangolin/mangosort)
[![Build status](https://ci.appveyor.com/api/projects/status/ocarv813eslr0vr3?svg=true)](https://ci.appveyor.com/project/raulmangolin/mangosort)

## Hot to use
#### Sort by multiple directions:
To sort by different directions at same time you need to pass a list of dictionary keys with values `False` or `True`. 
* False: ASC
* True: DESC (reverse)    

```
from mangosort import mangosort
 
my_list =  [{'code': 'beta', 'number': 3}, 
            {'code': 'delta', 'number': 2},
            {'code': 'delta', 'number': 3}]
mangosort.sort_by_key_asc(my_list, ['code', 'number'])

[{'code': 'delta', 'number': 2}, 
{'code': 'delta', 'number': 3}, 
{'code': 'beta', 'number': 3}]
```
    
#### Sort by ASC:
```
from mangosort import mangosort
 
my_list =  [{'code': 'beta', 'number': 3}, 
            {'code': 'delta', 'number': 2},
            {'code': 'delta', 'number': 3}]
mangosort.sort_by_key_asc(my_list, ['code', 'number'])

[{'code': 'beta', 'number': 3}, 
{'code': 'delta', 'number': 2}, 
{'code': 'delta', 'number': 3}]
```

#### Sort by DESC:
```
from mangosort import mangosort
 
my_list =  [{'code': 'beta', 'number': 3}, 
            {'code': 'delta', 'number': 2},
            {'code': 'delta', 'number': 3}]
mangosort.sort_by_key_asc(my_list, ['code', 'number'])

[{'code': 'delta', 'number': 3}, 
{'code': 'delta', 'number': 2}, 
{'code': 'beta', 'number': 3}]
```

## How to Install
#### Install via PyPi
    pip install mangosort