
<%
    from pwnlib.shellcraft.aarch64.linux import syscall
%>
<%page args="addr, len"/>
<%docstring>
Invokes the syscall munmap.  See 'man 2 munmap' for more information.

Arguments:
    addr(void): addr
    len(size_t): len
</%docstring>

    ${syscall('SYS_munmap', addr, len)}