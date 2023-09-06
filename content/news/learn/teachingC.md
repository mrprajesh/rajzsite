Title: Learning to Teach CS1100/CS1111
Date: 18-Sep-2018 12:28:12
Category: Learning Curve
Modified: 18-Sep-2019 12:28:12
Status: draft


## Terminal

- Open `terminal` after pressing super key or using shortcut `CTRL+ALT+T`
- `ls` - list the files in the current directory
- `pwd` - List the path of the working directory/folder.
- `mkdir <DIRNAME>` - Creates a directory named `<DIRNAME>`
- `cd <DIRNAME>` - change directory to whatever specified in `<DIRNAME>`
- `rmdir <DIRNAME> `- removed the empty directory as specfied.
- `date`  - system date/time
- `clear` - clear
- `man <CMD>` - manual or help pages for all the commands.

## Hello World Program
- Learn `Hello World` program.
- Learn to type and save
- Learn to compile and debug errors if any.
- Learn to execute or run the program.

## Evaluations of expressions / datatypes

## scanf and printf

## functions

## condition - if else

## loop - while/do-while/for

## File reading

## Self learning

- gets is deprecated
	fgets(str, 100, stdin)
- terminal buffer
- variable length array vs malloc // stack vs host alloc
- variadic function
- Not to return char array
- there is no reference in c // only pointers
- the blow is a error in C/gcc. it is okay if you compile with gcc

swap(a,b);

```
void swap(int &a, int &b){
  *a = *a + *b;
  *b = *a - *b;
  *a = *a - *b;
}

```

- This is how we should do in c/gcc

swap(&a,&b)

```
void swap(int *a, int *b){
  *a = *a + *b;
  *b = *a - *b;
  *a = *a - *b;
}
```
