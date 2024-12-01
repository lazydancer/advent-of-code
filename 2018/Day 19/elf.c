#include <stdio.h>
int main()
{

  void *jump_table[36] = {
   &&L00, &&L01, &&L02, &&L03, &&L04, &&L05, &&L06, &&L07, &&L08, &&L09, 
   &&L10, &&L11, &&L12, &&L13, &&L14, &&L15, &&L16, &&L17, &&L18, &&L19, 
   &&L20, &&L21, &&L22, &&L23, &&L24, &&L25, &&L26, &&L27, &&L28, &&L29, 
   &&L30, &&L31, &&L32, &&L33, &&L34, &&L35 };

  int reg[6] = {1,0,0,0,0,0};

  L00: goto *jump_table[0+16+1]; //addi 3 16 3
  L01: reg[1] = 1; //seti 1 2 1
  L02: reg[2] = 1; //seti 1 1 2
  L03: reg[5] = reg[1] * reg[2]; //mulr 1 2 5
  L04: reg[5] = reg[5] == reg[4]; //eqrr 5 4 5
  L05: goto *jump_table[reg[5] + 5 + 1]; //addr 5 3 3
  L06: goto *jump_table[6 + 1 + 1]; //addi 3 1 3
  L07: reg[0] = reg[1] + reg[0]; //addr 1 0 0
  L08: reg[2] = reg[2] + 1; //addi 2 1 2
  L09: reg[5] = reg[2] > reg[4]; //gtrr 2 4 5
  L10: goto *jump_table[10 + reg[5] + 1]; //addr 3 5 3
  L11: goto *jump_table[2 + 1]; //seti 2 3 3
  L12: reg[1] = reg[1] + 1;//addi 1 1 1
  L13: reg[5] = reg[1] > reg[4];//gtrr 1 4 5
  L14: goto *jump_table[reg[5] + 14 + 1];//addr 5 3 3
  L15: goto *jump_table[1 + 1];//seti 1 6 3
  L16: goto END; //With the command below I beleive this is the exit goto *jump_table[16 * 16 + 1]; mulr 3 3 3
  L17: reg[4] = reg[4] + 2; // addi 4 2 4
  L18: reg[4] = reg[4] * reg[4]; // mulr 4 4 4
  L19: reg[4] = 19 * reg[4]; //mulr 3 4 4
  L20: reg[4] = reg[4] * 11; //muli 4 11 4
  L21: reg[5] = reg[5] + 5; //addi 5 5 5
  L22: reg[5] = reg[5] * 22; // mulr 5 3 5
  L23: reg[5] = reg[5] + 15; //addi 5 15 5
  L24: reg[4] = reg[4] + reg[5]; //addr 4 5 4
  L25: goto *jump_table[25 + reg[0] + 1]; //addr 3 0 3
  L26: goto *jump_table[0 + 1];//seti 0 6 3
  L27: reg[5] = 27;  //setr 3 5 5
  L28: reg[5] = reg[5] * 28; //mulr 5 3 5
  L29: reg[5] = 29 + reg[5];//addr 3 5 5
  L30: reg[5] = 30 * reg[5];//mulr 3 5 5
  L31: reg[5] = reg[5] * 14;//muli 5 14 5
  L32: reg[5] = reg[5] * 32;//mulr 5 3 5
  L33: reg[4] = reg[4] + reg[5];//addr 4 5 4
  L34: reg[0] = 0; //seti 0 5 0
  L35: goto *jump_table[0 + 1];//seti 0 1 3


  // printf() displays the string inside quotation
  //printf("Hello, World!\n");
  
  END:
    for(int i=0; i<6; i++){
      printf("%d, %d\n",i,reg[i]);
    }

    return 0;
  
}

/*
#ip 3
0 addi 3 16 3
1 seti 1 2 1
2 seti 1 1 2
3 mulr 1 2 5
4 eqrr 5 4 5
5 addr 5 3 3
6 addi 3 1 3
7 addr 1 0 0
8 addi 2 1 2
9 gtrr 2 4 5
10 addr 3 5 3
11 seti 2 3 3
12 addi 1 1 1
13 gtrr 1 4 5
14 addr 5 3 3
15 seti 1 6 3
16 mulr 3 3 3
17 addi 4 2 4
18 mulr 4 4 4
19 mulr 3 4 4
20 muli 4 11 4
21 addi 5 5 5
22 mulr 5 3 5
23 addi 5 15 5
24 addr 4 5 4
25 addr 3 0 3
26 seti 0 6 3
27 setr 3 5 5
28 mulr 5 3 5
29 addr 3 5 5
30 mulr 3 5 5
31 muli 5 14 5
32 mulr 5 3 5
33 addr 4 5 4
34 seti 0 5 0
35 seti 0 1 3
*/