#include <stdio.h>
#include <string.h>
#include "ebpf.h"

// Method responsible by model the instruction into the expected pattern;
void filterInst (FILE *f, unsigned int *opc) {

    signed int imm;
    unsigned int opcode;
    unsigned int src, dst;
    signed short int offset;

    opcode = opc[0];
    src    = opc[1] & 0x0F;
    dst    = opc[1] >> 4 & 0x0F;
    offset = opc[2] << 8 | opc[3];
    imm    = opc[4] << 24 | opc[5] << 16 | opc[6] << 8 | opc[7];

    // Checking if offset spent more than 4 digits:
    char str[10];
    char soffset[4];
    for (int i = 0; i <= 4; i++) soffset[i] = ' ';
    sprintf(str, "%x", offset);
    if (strlen(str) > 4) {
        int i, j = 3;
        for (i = strlen(str); i >= strlen(str) - 4; i--) {
            if (str[i] != '\n' && str[i] != '\0') {
                soffset[j] = str[i];
                j--;
            }
        }
    }

    soffset[4] = '\0';

    // Printing instruction:
    fprintf(f, "0x%08x ", imm);
    if (strlen(str) > 4) fprintf(f, "0x%s%x%x%02x\n", soffset, src, dst, opcode);
    else fprintf(f, "0x%04x%x%x%02x\n", offset, src, dst, opcode);
}

// Method responsible by write the final file with the number of instructions and it set.
void writeFile (int numInst) {

    char line[24];
    FILE *f = fopen("instructions.txt", "w");
    FILE *t = fopen("tempinst.txt", "r");
    fprintf(f, "0x%08x\n", numInst);
    while(fgets(line, sizeof(line), t) != NULL) {
        fprintf(f, "%s", line);
    }
    fclose(t);
    fclose(f);
}

void print (int opcode) {

    switch(opcode) {

        case EBPF_OP_ADD_IMM   : printf("add32 ")    ; break;
        case EBPF_OP_ADD_REG   : printf("add32 ")    ; break;
        case EBPF_OP_SUB_IMM   : printf("sub32 ")    ; break;
        case EBPF_OP_SUB_REG   : printf("sub32 ")    ; break;
        case EBPF_OP_MUL_IMM   : printf("mul32 ")    ; break;
        case EBPF_OP_MUL_REG   : printf("mul32 ")    ; break;
        case EBPF_OP_DIV_IMM   : printf("div32 ")    ; break;
        case EBPF_OP_DIV_REG   : printf("div32 ")    ; break;
        case EBPF_OP_OR_IMM    : printf("or32 ")     ; break;
        case EBPF_OP_OR_REG    : printf("or32 ")     ; break;
        case EBPF_OP_AND_IMM   : printf("and32 ")    ; break;
        case EBPF_OP_AND_REG   : printf("and32 ")    ; break;
        case EBPF_OP_LSH_IMM   : printf("lsh32 ")    ; break;
        case EBPF_OP_LSH_REG   : printf("lsh32 ")    ; break;
        case EBPF_OP_RSH_IMM   : printf("rsh32 ")    ; break;
        case EBPF_OP_RSH_REG   : printf("rsh32 ")    ; break;
        case EBPF_OP_NEG       : printf("neg32 ")    ; break;
        case EBPF_OP_MOD_IMM   : printf("mod32 ")    ; break;
        case EBPF_OP_MOD_REG   : printf("mod32 ")    ; break;
        case EBPF_OP_XOR_IMM   : printf("xor32 ")    ; break;
        case EBPF_OP_XOR_REG   : printf("xor32 ")    ; break;
        case EBPF_OP_MOV_IMM   : printf("mov32 ")    ; break;
        case EBPF_OP_MOV_REG   : printf("mov32 ")    ; break;
        case EBPF_OP_ARSH_IMM  : printf("arsh32 ")   ; break;
        case EBPF_OP_ARSH_REG  : printf("arsh32 ")   ; break;
        case EBPF_OP_LE        : printf("le ")       ; break;
        case EBPF_OP_BE        : printf("be ")       ; break;
        case EBPF_OP_ADD64_IMM : printf("add ")      ; break;
        case EBPF_OP_ADD64_REG : printf("add ")      ; break;
        case EBPF_OP_SUB64_IMM : printf("sub ")      ; break;
        case EBPF_OP_SUB64_REG : printf("sub ")      ; break;
        case EBPF_OP_MUL64_IMM : printf("mul ")      ; break;
        case EBPF_OP_MUL64_REG : printf("mul ")      ; break;
        case EBPF_OP_DIV64_IMM : printf("div ")      ; break;
        case EBPF_OP_DIV64_REG : printf("div ")      ; break;
        case EBPF_OP_OR64_IMM  : printf("or ")       ; break;
        case EBPF_OP_OR64_REG  : printf("or ")       ; break;
        case EBPF_OP_AND64_IMM : printf("and ")      ; break;
        case EBPF_OP_AND64_REG : printf("and ")      ; break;
        case EBPF_OP_LSH64_IMM : printf("lsh ")      ; break;
        case EBPF_OP_LSH64_REG : printf("lsh ")      ; break;
        case EBPF_OP_RSH64_IMM : printf("rsh ")      ; break;
        case EBPF_OP_RSH64_REG : printf("rsh ")      ; break;
        case EBPF_OP_NEG64     : printf("neg ")      ; break;
        case EBPF_OP_MOD64_IMM : printf("mod ")      ; break;
        case EBPF_OP_MOD64_REG : printf("mod ")      ; break;
        case EBPF_OP_XOR64_IMM : printf("xor ")      ; break;
        case EBPF_OP_XOR64_REG : printf("xor ")      ; break;
        case EBPF_OP_MOV64_IMM : printf("mov ")      ; break;
        case EBPF_OP_MOV64_REG : printf("mov ")      ; break;
        case EBPF_OP_ARSH64_IMM: printf("arsh ")     ; break;
        case EBPF_OP_ARSH64_REG: printf("arsh ")     ; break;
        case EBPF_OP_LDXW      : printf("ldxw ")     ; break;
        case EBPF_OP_LDXH      : printf("ldxh ")     ; break;
        case EBPF_OP_LDXB      : printf("ldxb ")     ; break;
        case EBPF_OP_LDXDW     : printf("ldxdw ")    ; break;
        case EBPF_OP_STW       : printf("stw ")      ; break;
        case EBPF_OP_STH       : printf("sth ")      ; break;
        case EBPF_OP_STB       : printf("stb ")      ; break;
        case EBPF_OP_STDW      : printf("stdw ")     ; break;
        case EBPF_OP_STXW      : printf("stxw ")     ; break;
        case EBPF_OP_STXH      : printf("stxh ")     ; break;
        case EBPF_OP_STXB      : printf("stxb ")     ; break;
        case EBPF_OP_STXDW     : printf("stxdw ")    ; break;
        case EBPF_OP_LDDW      : printf("lddw ")     ; break;
        case EBPF_OP_JA        : printf("ja ")       ; break;
        case EBPF_OP_JEQ_IMM   : printf("jeq ")      ; break;
        case EBPF_OP_JEQ_REG   : printf("jeq ")      ; break;
        case EBPF_OP_JGT_IMM   : printf("jgt ")      ; break;
        case EBPF_OP_JGT_REG   : printf("jgt ")      ; break;
        case EBPF_OP_JGE_IMM   : printf("jge ")      ; break;
        case EBPF_OP_JGE_REG   : printf("jge ")      ; break;
        case EBPF_OP_JSET_REG  : printf("jset ")     ; break;
        case EBPF_OP_JSET_IMM  : printf("jset ")     ; break;
        case EBPF_OP_JNE_IMM   : printf("jne ")      ; break;
        case EBPF_OP_JNE_REG   : printf("jne ")      ; break;
        case EBPF_OP_JSGT_IMM  : printf("jsgt ")     ; break;
        case EBPF_OP_JSGT_REG  : printf("jsgt ")     ; break;
        case EBPF_OP_JSGE_IMM  : printf("jsge ")     ; break;
        case EBPF_OP_JSGE_REG  : printf("jsge ")     ; break;
        case EBPF_OP_CALL      : printf("call ")     ; break;
        case EBPF_OP_EXIT      : printf("exit")      ; break;
    }
}

int main() {

    FILE *f;
    f = fopen("tempinst.txt", "w");

    int numInst = 0;
    uint64_t instr;
    unsigned int opcode;
    unsigned int dst;
    unsigned int src;
    signed short int offset;
    signed int imm;
    unsigned int class;
    unsigned int opc[8];
    int start=0;

    while(scanf("%x",&opc[0])!=EOF){

        for(int i=1;i<8;i++){

           scanf("%x",&opc[i]);
        }

        opcode = opc[0];
        class = opcode & 7;
        dst = opc[1] >> 4 &0x0F;
        src = opc[1] & 0x0F;
        offset = opc[2] << 8 | opc[3];
        imm = opc[4] << 24 | opc[5] << 16 | opc[6] << 8 | opc[7];

        if ((opcode !=0xb7) && !start) {
          continue;
        }
        else {
            start=1;
        }
        if (!opcode) {
          continue;
        }

        print(opcode);
        filterInst(f, opc);
        numInst++;

        if( (opcode!=EBPF_OP_CALL)
         && (opcode!=EBPF_OP_JA)
         && (opcode!=EBPF_OP_EXIT)
         && (class!=EBPF_CLS_ST)
         && (class!=EBPF_CLS_STX)
        ){
          printf("r%d, ", dst);
        }

        // class store
        if( (class == EBPF_CLS_ST)||(class == EBPF_CLS_STX) ){

            if (offset) printf("[");
            printf("r%d", dst);
            if (offset) {
                if (offset > 0) printf("+%hi]", offset);
                else printf("%hi]", offset);
            }
            printf(", r%d", src);
        }
        else if( ((opcode &  EBPF_SRC_REG) == EBPF_SRC_REG)
        || ( ((opcode & EBPF_MODE_MEM) == EBPF_MODE_MEM) && !((opcode & EBPF_CLS_ALU64)== EBPF_CLS_ALU64) )
        ){
            if ((offset)&&(class!=EBPF_CLS_JMP)) printf("[");
            printf("r%d", src);
            if ((offset)&&(class!=EBPF_CLS_JMP)) {
                if (offset > 0) printf("+%hi]", offset);
                else printf("%hi]", offset);
            }
        } else if(opcode !=EBPF_OP_JA){
        //immediate
          if (opcode != EBPF_OP_EXIT) printf("%d", imm);
        }

        //jump class - need offset of jump
        // not call nor exit operation
        if(class == EBPF_CLS_JMP) {
          if((opcode!=EBPF_OP_CALL) && (opcode != EBPF_OP_EXIT)) {
            if (offset > 0) printf(", +%d", offset);
            else printf(", %d", offset);
          }
        }

        printf("\n");

        if(opcode == EBPF_OP_EXIT) break;
    }
    fclose(f);
    writeFile(numInst);
    remove("tempinst.txt");
    return 0;
}
