## Interfacing with Python modules

Example of importing Python modules:

```
    var io = __xxl.pyimport("io");
    var sys = __xxl.pyimport("sys");
    var f = io.open('something.txt');

    var line;
    while ((line = f.readline()) != '') {
	sys.stdout.write(line);
    }
```
