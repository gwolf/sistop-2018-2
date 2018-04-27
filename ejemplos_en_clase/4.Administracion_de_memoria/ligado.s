	.file	"ligado.c"
	.section	.rodata
.LC0:
	.string	"\303\211xito en la ejecuci\303\263n"
.LC1:
	.string	"Fracasoooooo"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$0, %eax
	call	correme@PLT
	testl	%eax, %eax
	jne	.L2
	leaq	.LC0(%rip), %rdi
	call	puts@PLT
	jmp	.L4
.L2:
	leaq	.LC1(%rip), %rdi
	call	puts@PLT
.L4:
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Debian 6.3.0-18+deb9u1) 6.3.0 20170516"
	.section	.note.GNU-stack,"",@progbits
