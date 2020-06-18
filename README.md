# mangosort: Sort list by multiple keys and directions
**mangosort** is a small module that helps you sort lists of dictionaries by multiple keys

[![Build Status](https://travis-ci.com/raulmangolin/mangosort.svg?token=QfPxoKSpBQKuzP1gqVAS&branch=master)](https://travis-ci.com/raulmangolin/mangosort)
[![Build status](https://ci.appveyor.com/api/projects/status/ocarv813eslr0vr3?svg=true)](https://ci.appveyor.com/project/raulmangolin/mangosort)

## Hot to use
#### Sort by multiple directions:
To sort by different directions at same time you need to pass a list of dictionaries with keys you want to order and values `asc` or `desc`.     

```
from mangosort import mangosort
 
my_list =  [{'code': 'beta', 'number': 3}, 
            {'code': 'delta', 'number': 2},
            {'code': 'delta', 'number': 3}]

mangosort.sort_by_key(my_list, [{'code': 'desc'}, {'number': 'asc'}])

[{'code': 'delta', 'number': 2}, 
{'code': 'delta', 'number': 3}, 
{'code': 'beta', 'number': 3}]
```

If you need or prefer to pass bool, in this case, think reverse `True`(desc) or `False`(asc).
```
# Reverse True or False
mangosort.sort_by_key(my_list, [{'code': True}, {'number': 0}])

[{'code': 'delta', 'number': 2}, 
{'code': 'delta', 'number': 3}, 
{'code': 'beta', 'number': 3}]
```
    
#### Sort ASC:
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

#### Sort DESC:
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
    
## Contributing
I’m accepting pull requests that improve speed and legibility of the code or anything else you think will be good.
    
## License 
This module is under MIT License, but you can do what you want. It's just a bunch of code.

Just tell your friends about it.

Communism will win!

![Communism will win!](ico.png "Communism will win!")
