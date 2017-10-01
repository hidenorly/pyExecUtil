# pyExecUtil

This is utility class to execute other program, especially easier to handle stdin/out.

What you need to do are
 * to use PyExecUtil with stdout/err handler function
 * or to derive ```pyExecUtil``` class and override onCompletion

# How to use

```
from pyExecUtil import PyExecUtil

def my_process(args, stdout_data, stderr_data):
	print(stdout_data)
	print(stderr_data)

if __name__ == '__main__':
	cmd = PyExecUtil("echo 'started'; sleep 2; echo 'finished'")
	cmd.execute(timeout=3, onCompletion=my_process, args=None)
	cmd.execute(timeout=1, onCompletion=my_process, args=None)
```

```
from pyExecUtil import PyExecUtil

class MyExtCommandHandler(PyExecUtil):
	def __init__(self, cmd):
		super(MyExtCommandHandler, self).__init__(cmd)

	def onCompletion(self):
		print(self.stdout_data)
		print(self.stderr_data)


if __name__ == '__main__':
	cmd2 = MyExtCommandHandler("echo 'started'; sleep 2; echo 'finished'");
	cmd2.execute(timeout=3)
	cmd2.execute(timeout=1)
```

Optinally, you can use

```
PyExecUtil.execute() # execute without infinite wait (no timeout specified)
```

```
PyExecUtil.terminate() # force terminate
```


# Confirmed environment

```
$ python --version
Python 2.7.12
$ python3 --version
Python 3.5.2
```