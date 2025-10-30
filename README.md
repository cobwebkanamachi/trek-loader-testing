# trek-loader-testing
experimental serial basic source code loader for patb on tang nano 9k(sbc8080)
how to use:<BR>
<PRE>
on Windows11 cmd.exe, you type bellow.
type trektake.asc|python com5.py
Then wait for ending upload trektake.asc.
exit cmd.exe(press x button, or ctrl-c), then connect tang nano 9k with serial (teraterm).
Then you should type in Enter key, you would see OK on teraterm.
Then type RUN on teraterm.
But unfortunately you would see ocasionally error cause on basic.
Perhaps it is shortage of wait time or anything else.
Enjoy! 9600baud serial communication!
Python version: Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)](via microsoft store)
And trek basic source was taken from https://github.com/cobwebkanamachi/X-paloalto-tiny-basic
And SBC8080 on tang nano 9k was taken from https://github.com/cobwebkanamachi/tangnano9k-sbc8080-light8080
</PRE>
