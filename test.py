#!/usr/bin/env python
# -*- Coding: utf-8 -*-
#
# Copyright (C) 2017 hidenorly
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyExecUtil import PyExecUtil

def my_process(args, stdout_data, stderr_data):
	print(stdout_data)
	print(stderr_data)


class MyExtCommandHandler(PyExecUtil):
	def __init__(self, cmd):
		super(MyExtCommandHandler, self).__init__(cmd)

	def onCompletion(self):
		print(self.stdout_data)
		print(self.stderr_data)


if __name__ == '__main__':
	cmd = PyExecUtil("echo 'started'; sleep 2; echo 'finished'")
	cmd.execute(timeout=3, onCompletion=my_process, args=None)
	cmd.execute(timeout=1, onCompletion=my_process, args=None)

	cmd2 = MyExtCommandHandler("echo 'started'; sleep 2; echo 'finished'");
	cmd2.execute(timeout=3)
	cmd2.execute(timeout=1)
	cmd2.execute() # infinite wait

	cmd.terminate() #optional
	cmd2.terminate() #optional
