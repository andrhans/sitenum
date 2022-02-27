# README.md
Files in the repository:
* [dir-disc.py](#directory-discovery)
* [dir-enum.py](#directory-enumeration)

## Directory Discovery
`file:dir-disc.py`

`dir-disc.py` is a directory discovery tool written in python following instructions.

### Usage
```
$ python dir-disc.py
 ____  _               _                   
|  _ \(_)_ __ ___  ___| |_ ___  _ __ _   _ 
| | | | | '__/ _ \/ __| __/ _ \| '__| | | |
| |_| | | | |  __/ (__| || (_) | |  | |_| |
|____/|_|_|  \___|\___|\__\___/|_|   \__, |
                                     |___/ 
 ____  _                                   
|  _ \(_)___  ___ _____   _____ _ __ _   _ 
| | | | / __|/ __/ _ \ \ / / _ \ '__| | | |
| |_| | \__ \ (_| (_) \ V /  __/ |  | |_| |
|____/|_|___/\___\___/ \_/ \___|_|   \__, |
                                     |___/ 

Enter target host: 127.0.0.1
Enter wordlist location: wordlist.txt
[*] Directory discovered: 127.0.0.1/server-status
[*] Directory discovered: 127.0.0.1/uploads
```

## Directory Enumeration
`file:dir-enum.py`

`dir-enum.py` is a directory enumeration tool written in python that allows arguments and is slightly more functional.

```
$ python dir-enum.py http://127.0.0.1 wordlist.txt
 ____  _               _                   
|  _ \(_)_ __ ___  ___| |_ ___  _ __ _   _ 
| | | | | '__/ _ \/ __| __/ _ \| '__| | | |
| |_| | | | |  __/ (__| || (_) | |  | |_| |
|____/|_|_|  \___|\___|\__\___/|_|   \__, |
                                     |___/ 
 _____                                      _   _             
| ____|_ __  _   _ _ __ ___   ___ _ __ __ _| |_(_) ___  _ __  
|  _| | '_ \| | | | '_ ` _ \ / _ \ '__/ _` | __| |/ _ \| '_ \ 
| |___| | | | |_| | | | | | |  __/ | | (_| | |_| | (_) | | | |
|_____|_| |_|\__,_|_| |_| |_|\___|_|  \__,_|\__|_|\___/|_| |_|
                                                              

*****************************************************************
Scanning target: http://127.0.0.1
Wordlist: wordlist.txt
Start time: 2022-02-25 09:04:35.247230
*****************************************************************

[*] Discovered directory: server-status
[*] Discovered directory: assets
```