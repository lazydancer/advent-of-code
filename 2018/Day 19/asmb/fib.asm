; ----------------------------------------------------------------------------------------
; Writes "Hello, World" to the console using only system calls. Runs on 64-bit Linux only.
; To assemble and run:
;
;     nasm -felf64 hello.asm && ld hello.o && ./a.out
; ----------------------------------------------------------------------------------------

          global    _start
          section   .text
_start:
          mov       r10, 1          ; initalizing registers r0 --> r10
          mov       r11, 0              
          mov       r12, 0          ; r13 not defined as pointer in program
          mov       r14, 0  
          mov       r15, 0 

      jmp       l17             ;  L00: goto *jump_table[0+16+1]; //addi 3 16 3
l01:      mov       r11, 1          ;  L01: reg[1] = 1; //seti 1 2 1
l02:      mov       r12, 1          ;  L02: reg[2] = 1; //seti 1 1 2
l03:      mov       rax, r11        ;  L03: reg[5] = reg[1] * reg[2]; //mulr 1 2 5
      mov       rbx, r12        ;
      imul      rax, rbx        ;
      mov       r15, rax        ;
      cmp       r15, r14        ;  L04: reg[5] = reg[5] == reg[4]; //eqrr 5 4 5
      sete      al              ;  Grab the flag
      movzx     r15, al         ;  Move the flag to r15 extends with zeros
      je        l07             ;  L05: goto *jump_table[reg[5] + 5 + 1]; //addr 5 3 3
      jmp       l08             ;  L06: goto *jump_table[6 + 1 + 1]; //addi 3 1 3
l07:      add       r10, r11        ;  L07: reg[0] = reg[1] + reg[0]; //addr 1 0 0
l08:      add       r12, 1          ;  L08: reg[2] = reg[2] + 1; //addi 2 1 2
      cmp       r12, r14        ;  L09: reg[5] = reg[2] > reg[4]; //gtrr 2 4 5
      setg      al              ;
      movzx     r15, al         ; 
      jg        l12             ;  L10: goto *jump_table[10 + reg[5] + 1]; //addr 3 5 3
      jmp       l03             ;  L11: goto *jump_table[2 + 1]; //seti 2 3 3
l12:      add       r11, 1          ;  L12: reg[1] = reg[1] + 1;//addi 1 1 1
      cmp       r11, r14        ;  L13: reg[5] = reg[1] > reg[4];//gtrr 1 4 5
      setg      al              ;
      movzx     r15, al         ;
      jg        l16             ;  L14: goto *jump_table[reg[5] + 14 + 1];//addr 5 3 3
      jmp       l02             ;  L15: goto *jump_table[1 + 1];//seti 1 6 3
l16:      jmp       end             ;  L16: goto END; //With the command below I beleive this is the exit goto *jump_table[16 * 16 + 1]; mulr 3 3 3
l17:      add       r14, 2          ;  L17: reg[4] = reg[4] + 2; // addi 4 2 4
      imul      r14, r14        ;  L18: reg[4] = reg[4] * reg[4]; // mulr 4 4 4
      imul      r14, 19         ;  L19: reg[4] = 19 * reg[4]; //mulr 3 4 4
      imul      r14, 11         ;  L20: reg[4] = reg[4] * 11; //muli 4 11 4
      add       r15, 5          ;  L21: reg[5] = reg[5] + 5; //addi 5 5 5
      imul      r15, 22         ;  L22: reg[5] = reg[5] * 22; // mulr 5 3 5
      add       r15, 15         ;  L23: reg[5] = reg[5] + 15; //addi 5 15 5
      add       r14, r15        ;  L24: reg[4] = reg[4] + reg[5]; //addr 4 5 4
      cmp       r10, 1          ;  L25: goto *jump_table[25 + reg[0] + 1]; //addr 3 0 3
      je        l27             ;
      jmp       l01             ;  L26: goto *jump_table[0 + 1];//seti 0 6 3
l27:      mov       r15, 27         ;  L27: reg[5] = 27;  //setr 3 5 5
      imul      r15, 28         ;  L28: reg[5] = reg[5] * 28; //mulr 5 3 5
      add       r15, 29         ;  L29: reg[5] = 29 + reg[5];//addr 3 5 5
      imul      r15, 30         ;  L30: reg[5] = 30 * reg[5];//mulr 3 5 5
      imul      r15, 14         ;  L31: reg[5] = reg[5] * 14;//muli 5 14 5
      imul      r15, 32         ;  L32: reg[5] = reg[5] * 32;//mulr 5 3 5
      add       r14, r15        ;  L33: reg[4] = reg[4] + reg[5];//addr 4 5 4
      mov       r10, 0          ;  L34: reg[0] = 0; //seti 0 5 0
      jmp       l01             ;  L35: goto *jump_table[0 + 1];//seti 0 1 3

end: 

          sub      r10, 10708819    ; Solution should be 10708912 which will equal 93 or ]         


print:
          mov       [value], r10     
          mov       rax, 1             ; system call for write
          mov       rdi, 1             ; file handle 1 is stdout
          mov       rsi, value         ; address of string to output
          mov       rdx, 8             ; number of bytes
          syscall                      ; invoke operating system to do the write
          mov       rax, 60            ; system call for exit
          xor       rdi, rdi           ; exit code 0
          syscall                      ; invoke operating system to exit

          

          section   .bss

value:    resb      8