# Reverse Engineering Basics
# Patching
- To replace a call with NOP you have to replace every single 2 digit hex number of the call with the HEX value of NOP, that's `90`; 
# Debugging
## AntiDebugging
If you are trying to use GDB but it doesn't work (i.e. message there is already a debugger), there is an anti-debugging technique applied.
Try to search for a `ptrace`. Usually it's called at the beginning of the main, and if it's not there you could try to search inside of `_start` (the file that calls the main to start the process).

**NOTE:** IDA offers a search function, where you can search ptrace (you have only to find the HEX values of the call to ptrace, to replace them with NOP).

## Usage of GDB
GDB is a debugger that you can use to execute commands, analyze memory cells, and inspect the program.

To use it you have to insert yourself in the folder where the binary you want to analyze is placed, and then call `gdb` in your terminal.

After that you can:
- run `file <pathAlBinary>`: to open a binary in debug mode;
- run `break <functionName>`: to set a breakpoint at the beginning of the funciont (i.e. <u>break main</u>);
    - alterantively:
      - `b <functionName>` you can abbreviate "break" with "b";
      - `break <pointer>` you can place a breakpoint on a specific pointer of a line of code (**keepInMind:** the pointer has to be specified in the 0x\<something> format to be accepted (i.e. b *0x00000000004008a8 or b *0x4008a8));

    **WARNING:** it could happen that GDB says 'Cannot insert breakpoint \<numberOfBreakpoint>' and that it can't access the memory at address \<addressOfBreakpoint>. To solve this problem just use the `delete` command, to remove all the breakpoints, then use the `c` command, to continue the execution of the program to reach its end. Now if you inspect again the `disas main`, or wathever function you were disassembling, the addresses are changed, and you can try re-setting you breakpoints with the new addresses.
- run `run` (alternatively just `r`): to run the execution of the code;
- run `jump <functionName>`: to execute a specific function (ignoring the codeflow);
- run `disas <functionName>`: to disassemble the function (keep in mind that the disassembler could reverse the operands order in the instructions);
- run `printf "%s", (char*) <nameOfBuffer>`: if you hit a specific breakpoint and you want to see inside of a specific buffer (and you know that there is a string there), you can use this command;
- run `x/s <ptrOfBuffer>`: it does the same thing as the command before; it allows you to see inside a buffer, that HAS TO BE specified in the 0x\<something> format (i.e. x/s *0x6013E8);
- run `exit`: to exit gdb;
- run `info registers`: this will show you the values inside every single register at a specific point in the code. You can combine the information of the registers during a specific breakpoint, with the `x/s` command, to analyze each value, inspecting parameters or return values as you wish.
# Pwning