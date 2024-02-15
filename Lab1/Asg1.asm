section	.text
	global _start       ;must be declared for using gcc
_start:                     ;tell linker entry point
	mov	edx, len    ;message length
	mov	ecx, msg    ;message to write
	mov	ebx, 1	    ;file descriptor (stdout)
	mov	eax, 4	    ;system call number (sys_write)
	int	0x80        ;call kernel

	;second call/message
	mov edx, len2 	;message length
	mov ecx, msg2	;message to send
	mov ebx, 1		;file descripter (stdout/write)
	mov eax, 4		;system call write
	int 0x80		; call kernel to do the last few actions

	;exit system call
	mov	eax, 1	    ;system call number (sys_exit)
	int	0x80        ;call kernel

section	.data

msg	db	'Assignment 1 for Howard Chen',0xa	;our dear string
len	equ	$ - msg			;length of our dear string

msg2 db 'All done', 0xa	
len2 equ $ - msg2