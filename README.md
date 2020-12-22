# My Machine Language

## A Machine Language Designed and Implemented my Me

## Table of Contents
1. [Introduction](#introduction)
2. [Details on the Language](#details)
    * [Instruction Format](#instruction-format)
	* [Instruction Pointer Address](#instruction-pointer-address)
	* [Syntax](#syntax)
	* [Executing Programs](#executing-programs)
3. [Examples](#examples)
4. [Troubleshooting](#troubleshooting)

## Introduction

This program is based on the Von Neumann Architecture which is a stored program computer, meaing the program is loaded directly into the same RAM that stores data.
This program uses an implementaiton of a CPU requiring a program loader and fetch-evaluation cycle.
It also uses an implemetation of a RAM which can be found here: [RAM Implentation](https://github.com/tansonlee/ram)

## Details on the Language

### Instruction Format
Each instruction is formatted as follows: XXtttuuuvvv
* XX: 2-digit operation code
* ttt: 3-digit target address
* uuu: 3-digit source 1 address
* vvv: 3-digit source 2 address

### Instruction Pointer Address (IPA)
The instruction pointer address (IPA) is stored in RAM usually at address 0. 
The IPA stores the address for the instruction that will be executed.
After every instruction is executed, the IPA increments by 1.
For example, if the IPA stores the value 25 and the value at the address 25 is 0000000000, then 0000000000 will be treated as an instruction which halts the program (since 0000000000 corresponds to the halt operation).
Since the IPA is stored directly into RAM, operations can be performed on it. 
For example, if the IPA is stored at address 0, to skip an instruction, we need to add1 to the value at address 0.
To skip back 10 instructions, we need to subtract 10 from the value at address 0.

### Syntax
The instructions that will be loaded are represented by a Python list. This means each instruction is seperated my a comma and the entire instruction sequence is enclosed in square brackets.

### Executing Programms
There are two functions provided for executing programs. These are `run_and_return(instructions, load_address, instruction_pointer_address)` and `run_and_dump(instructions, load_address, instruction_pointer_address)`. 
`run_and_return` executes the program and returns the RAM in the final state. `run_and_dump` executes the program and performs a core dump which prints the contents of the RAM in the final state.
* `instructions` is the Python list of instructions that will be loaded into RAM
* `load_address` is the address of the first element of `instructions` the rest of the elements will be loaded sequentially
* `instruction_pointer_address` is the address that will hold the IPA
Commonly, `load_address` and `instruction_pointer_address` are default to 0


## Examples



## Troubleshooting 