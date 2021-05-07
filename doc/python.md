## Interfacing with Python modules

Example of importing Python modules:

```
    var io = System.pyimport("io");
    var sys = System.pyimport("sys");
    var f = io.open('something.txt');

    var line;
    while ((line = f.readline()) != '') {
	sys.stdout.write(line);
    }
```
