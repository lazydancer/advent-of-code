; ----------------------------------------------------------------------------------------
; Writes "Hello, World" to the console using only system calls. Runs on 64-bit Linux only.
; To assemble and run:
;
;     nasm -felf64 hello.asm && ld hello.o && ./a.out
; ----------------------------------------------------------------------------------------

          global    _start
          section   .text
_start:
          mov       rdx, output             ; rdx holds address of next byte to write
          mov       r8, 1                   ; inital line length
          mov       r9, 0                   ; number of starts written on line so far
line:
          mov byte [rdx], '*'               ; write single star
          inc       rdx                     ; advance pointer to next cell to write 
          inc       r9                      ; 'count' number so far on line
          cmp       r9, r8            ; did we reach the number of starts for this line
          jne       line                ; not yet, keep writing on this line
lineDone:
          mov       byte [rdx],10            ; write a new line char
          inc       rdx                      ; and move pointer to where next char goes
          inc       r8                       ; next line will be one char longer
          mov       r9, 0                   ; reset count of starts written on this line
          cmp       r8, maxlines            ; wait, did we already finish the last line?
          jng       line                    ; if not, begin writing this line
print:
          mov       rax, 1                  ; system call for write
          mov       rdi, 1                  ; file handle 1 is stdout
          mov       rsi, output            ; address of string to output
          mov       rdx, dataSize            ; number of bytes
          syscall                           ; invoke operating system to do the write
          mov       rax, 60                 ; system call for exit
          xor       rdi, rdi                ; exit code 0
          syscall                           ; invoke operating system to exit

          section   .bss
maxlines  equ       8
dataSize  equ       44
output:   resb      dataSize