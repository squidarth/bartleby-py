## Bartleby-Python

This is a library that allows Python users to use Bartleby, a tool for traking
changes in variables as your program runs.

## Installation

`sudo pip install git+git://github.com/squidarth/bartleby-py.git@master`

Will install the library and all dependencies.

## Usage

After running Bartleby (instructions [here](http://github.com/squidarth/bartleby)),
Bartleby-py must be initialized in your application to start tracing variable
assignments.

      # hello_bartleby.py

      Bartleby(
        files=["hello_bartleby.py"]
        redis_host="localhost"
        redis_port="6379"
      )

      def main():
        x = 5
        y = 3
        x = y + x
        z = 2
        print "%d:%d:%d" % (x,y,z)

     main()

The `files` parameter is a list of files that Bartleby will track. In cases
where there are many files in a given project, it's better to
programatically generate this list of files.  `Bartleby()` only needs to be
run in the file that is the main entry point to the program.

Note that in some applications, such as web applications, code is often reloaded.
In these applications, `Bartleby` will need to be run every time the code is
reloaded.

There is an example of this in `examples/flask_example.py`, using the Flask
web framework.

## Dependencies

Note that before running Bartleby, [Redis](http://redis.io) must be installed.
Also, in addition to this Python library, [Bartleby](http://github.com/squidarth/bartleby)
must be running.
