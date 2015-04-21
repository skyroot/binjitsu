STDIN_FILENO = 0
STDOUT_FILENO = 1
STDERR_FILENO = 2
__BSD_VISIBLE = 99999999
__POSIX_VISIBLE = 99999999
__XSI_VISIBLE = 99999999
INADDR_ANY = 0
INADDR_BROADCAST = 0xffffffff
INADDR_NONE = 0xffffffff
INADDR_LOOPBACK = 0x7f000001
EPERM = 1
ENOENT = 2
ESRCH = 3
EINTR = 4
EIO = 5
ENXIO = 6
E2BIG = 7
ENOEXEC = 8
EBADF = 9
ECHILD = 10
EDEADLK = 11
ENOMEM = 12
EACCES = 13
EFAULT = 14
ENOTBLK = 15
EBUSY = 16
EEXIST = 17
EXDEV = 18
ENODEV = 19
ENOTDIR = 20
EISDIR = 21
EINVAL = 22
ENFILE = 23
EMFILE = 24
ENOTTY = 25
ETXTBSY = 26
EFBIG = 27
ENOSPC = 28
ESPIPE = 29
EROFS = 30
EMLINK = 31
EPIPE = 32
EDOM = 33
ERANGE = 34
EAGAIN = 35
EWOULDBLOCK = 35
EINPROGRESS = 36
EALREADY = 37
ENOTSOCK = 38
EDESTADDRREQ = 39
EMSGSIZE = 40
EPROTOTYPE = 41
ENOPROTOOPT = 42
EPROTONOSUPPORT = 43
ESOCKTNOSUPPORT = 44
EOPNOTSUPP = 45
ENOTSUP = 45
EPFNOSUPPORT = 46
EAFNOSUPPORT = 47
EADDRINUSE = 48
EADDRNOTAVAIL = 49
ENETDOWN = 50
ENETUNREACH = 51
ENETRESET = 52
ECONNABORTED = 53
ECONNRESET = 54
ENOBUFS = 55
EISCONN = 56
ENOTCONN = 57
ESHUTDOWN = 58
ETOOMANYREFS = 59
ETIMEDOUT = 60
ECONNREFUSED = 61
ELOOP = 62
ENAMETOOLONG = 63
EHOSTDOWN = 64
EHOSTUNREACH = 65
ENOTEMPTY = 66
EPROCLIM = 67
EUSERS = 68
EDQUOT = 69
ESTALE = 70
EREMOTE = 71
EBADRPC = 72
ERPCMISMATCH = 73
EPROGUNAVAIL = 74
EPROGMISMATCH = 75
EPROCUNAVAIL = 76
ENOLCK = 77
ENOSYS = 78
EFTYPE = 79
EAUTH = 80
ENEEDAUTH = 81
EIDRM = 82
ENOMSG = 83
EOVERFLOW = 84
ECANCELED = 85
EILSEQ = 86
ENOATTR = 87
EDOOFUS = 88
EBADMSG = 89
EMULTIHOP = 90
ENOLINK = 91
EPROTO = 92
ENOTCAPABLE = 93
ECAPMODE = 94
ELAST = 94
O_RDONLY = 0x0000
O_WRONLY = 0x0001
O_RDWR = 0x0002
O_ACCMODE = 0x0003
FREAD = 0x0001
FWRITE = 0x0002
O_NONBLOCK = 0x0004
O_APPEND = 0x0008
O_SHLOCK = 0x0010
O_EXLOCK = 0x0020
O_ASYNC = 0x0040
O_FSYNC = 0x0080
O_SYNC = 0x0080
O_NOFOLLOW = 0x0100
O_CREAT = 0x0200
O_TRUNC = 0x0400
O_EXCL = 0x0800
O_NOCTTY = 0x8000
O_DIRECT = 0x00010000
O_DIRECTORY = 0x00020000
O_EXEC = 0x00040000
O_TTY_INIT = 0x00080000
O_CLOEXEC = 0x00100000
FAPPEND = 0x0008
FASYNC = 0x0040
FFSYNC = 0x0080
FNONBLOCK = 0x0004
FNDELAY = 0x0004
O_NDELAY = 0x0004
FRDAHEAD = 0x0200
AT_FDCWD = -100
AT_EACCESS = 0x100
AT_SYMLINK_NOFOLLOW = 0x200
AT_SYMLINK_FOLLOW = 0x400
AT_REMOVEDIR = 0x800
F_DUPFD = 0
F_GETFD = 1
F_SETFD = 2
F_GETFL = 3
F_SETFL = 4
F_GETOWN = 5
F_SETOWN = 6
F_OGETLK = 7
F_OSETLK = 8
F_OSETLKW = 9
F_DUP2FD = 10
F_GETLK = 11
F_SETLK = 12
F_SETLKW = 13
F_SETLK_REMOTE = 14
F_READAHEAD = 15
F_RDAHEAD = 16
F_DUPFD_CLOEXEC = 17
F_DUP2FD_CLOEXEC = 18
FD_CLOEXEC = 1
F_RDLCK = 1
F_UNLCK = 2
F_WRLCK = 3
F_UNLCKSYS = 4
F_CANCEL = 5
LOCK_SH = 0x01
LOCK_EX = 0x02
LOCK_NB = 0x04
LOCK_UN = 0x08
POSIX_FADV_NORMAL = 0
POSIX_FADV_RANDOM = 1
POSIX_FADV_SEQUENTIAL = 2
POSIX_FADV_WILLNEED = 3
POSIX_FADV_DONTNEED = 4
POSIX_FADV_NOREUSE = 5
INHERIT_SHARE = 0
INHERIT_COPY = 1
INHERIT_NONE = 2
PROT_NONE = 0x00
PROT_READ = 0x01
PROT_WRITE = 0x02
PROT_EXEC = 0x04
MAP_SHARED = 0x0001
MAP_PRIVATE = 0x0002
MAP_COPY = 0x0002
MAP_FIXED = 0x0010
MAP_RENAME = 0x0020
MAP_NORESERVE = 0x0040
MAP_RESERVED0080 = 0x0080
MAP_RESERVED0100 = 0x0100
MAP_HASSEMAPHORE = 0x0200
MAP_STACK = 0x0400
MAP_NOSYNC = 0x0800
MAP_FILE = 0x0000
MAP_ANON = 0x1000
MAP_ANONYMOUS = 0x1000
MAP_NOCORE = 0x00020000
MAP_PREFAULT_READ = 0x00040000
MCL_CURRENT = 0x0001
MCL_FUTURE = 0x0002
MS_SYNC = 0x0000
MS_ASYNC = 0x0001
MS_INVALIDATE = 0x0002
_MADV_NORMAL = 0
_MADV_RANDOM = 1
_MADV_SEQUENTIAL = 2
_MADV_WILLNEED = 3
_MADV_DONTNEED = 4
MADV_NORMAL = 0
MADV_RANDOM = 1
MADV_SEQUENTIAL = 2
MADV_WILLNEED = 3
MADV_DONTNEED = 4
MADV_FREE = 5
MADV_NOSYNC = 6
MADV_AUTOSYNC = 7
MADV_NOCORE = 8
MADV_CORE = 9
MADV_PROTECT = 10
MINCORE_INCORE = 0x1
MINCORE_REFERENCED = 0x2
MINCORE_MODIFIED = 0x4
MINCORE_REFERENCED_OTHER = 0x8
MINCORE_MODIFIED_OTHER = 0x10
POSIX_MADV_NORMAL = 0
POSIX_MADV_RANDOM = 1
POSIX_MADV_SEQUENTIAL = 2
POSIX_MADV_WILLNEED = 3
POSIX_MADV_DONTNEED = 4
SIGHUP = 1
SIGINT = 2
SIGQUIT = 3
SIGILL = 4
SIGTRAP = 5
SIGABRT = 6
SIGIOT = 6
SIGEMT = 7
SIGFPE = 8
SIGKILL = 9
SIGBUS = 10
SIGSEGV = 11
SIGSYS = 12
SIGPIPE = 13
SIGALRM = 14
SIGTERM = 15
SIGURG = 16
SIGSTOP = 17
SIGTSTP = 18
SIGCONT = 19
SIGCHLD = 20
SIGTTIN = 21
SIGTTOU = 22
SIGIO = 23
SIGXCPU = 24
SIGXFSZ = 25
SIGVTALRM = 26
SIGPROF = 27
SIGWINCH = 28
SIGINFO = 29
SIGUSR1 = 30
SIGUSR2 = 31
SIGTHR = 32
SIGLWP = 32
SIGRTMIN = 65
SIGRTMAX = 126
SIGEV_NONE = 0
SIGEV_SIGNAL = 1
SIGEV_THREAD = 2
SIGEV_KEVENT = 3
SIGEV_THREAD_ID = 4
ILL_ILLOPC = 1
ILL_ILLOPN = 2
ILL_ILLADR = 3
ILL_ILLTRP = 4
ILL_PRVOPC = 5
ILL_PRVREG = 6
ILL_COPROC = 7
ILL_BADSTK = 8
BUS_ADRALN = 1
BUS_ADRERR = 2
BUS_OBJERR = 3
SEGV_MAPERR = 1
SEGV_ACCERR = 2
FPE_INTOVF = 1
FPE_INTDIV = 2
FPE_FLTDIV = 3
FPE_FLTOVF = 4
FPE_FLTUND = 5
FPE_FLTRES = 6
FPE_FLTINV = 7
FPE_FLTSUB = 8
TRAP_BRKPT = 1
TRAP_TRACE = 2
TRAP_DTRACE = 3
CLD_EXITED = 1
CLD_KILLED = 2
CLD_DUMPED = 3
CLD_TRAPPED = 4
CLD_STOPPED = 5
CLD_CONTINUED = 6
POLL_IN = 1
POLL_OUT = 2
POLL_MSG = 3
POLL_ERR = 4
POLL_PRI = 5
POLL_HUP = 6
SA_NOCLDSTOP = 0x0008
SA_ONSTACK = 0x0001
SA_RESTART = 0x0002
SA_RESETHAND = 0x0004
SA_NODEFER = 0x0010
SA_NOCLDWAIT = 0x0020
SA_SIGINFO = 0x0040
NSIG = 32
SI_NOINFO = 0
SI_USER = 0x10001
SI_QUEUE = 0x10002
SI_TIMER = 0x10003
SI_ASYNCIO = 0x10004
SI_MESGQ = 0x10005
SI_KERNEL = 0x10006
SI_LWP = 0x10007
SI_UNDEFINED = 0
SS_ONSTACK = 0x0001
SS_DISABLE = 0x0004
SV_ONSTACK = 0x0001
SV_INTERRUPT = 0x0002
SV_RESETHAND = 0x0004
SV_NODEFER = 0x0010
SV_NOCLDSTOP = 0x0008
SV_SIGINFO = 0x0040
SIG_BLOCK = 1
SIG_UNBLOCK = 2
SIG_SETMASK = 3
SOCK_STREAM = 1
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_RDM = 4
SOCK_SEQPACKET = 5
SO_DEBUG = 0x0001
SO_ACCEPTCONN = 0x0002
SO_REUSEADDR = 0x0004
SO_KEEPALIVE = 0x0008
SO_DONTROUTE = 0x0010
SO_BROADCAST = 0x0020
SO_USELOOPBACK = 0x0040
SO_LINGER = 0x0080
SO_OOBINLINE = 0x0100
SO_REUSEPORT = 0x0200
SO_TIMESTAMP = 0x0400
SO_NOSIGPIPE = 0x0800
SO_ACCEPTFILTER = 0x1000
SO_BINTIME = 0x2000
SO_NO_OFFLOAD = 0x4000
SO_NO_DDP = 0x8000
SO_SNDBUF = 0x1001
SO_RCVBUF = 0x1002
SO_SNDLOWAT = 0x1003
SO_RCVLOWAT = 0x1004
SO_SNDTIMEO = 0x1005
SO_RCVTIMEO = 0x1006
SO_ERROR = 0x1007
SO_TYPE = 0x1008
SO_LABEL = 0x1009
SO_PEERLABEL = 0x1010
SO_LISTENQLIMIT = 0x1011
SO_LISTENQLEN = 0x1012
SO_LISTENINCQLEN = 0x1013
SO_SETFIB = 0x1014
SO_USER_COOKIE = 0x1015
SO_PROTOCOL = 0x1016
SO_PROTOTYPE = 0x1016
SO_VENDOR = 0x80000000
SOL_SOCKET = 0xffff
AF_UNSPEC = 0
AF_UNIX = 1
AF_INET = 2
AF_IMPLINK = 3
AF_PUP = 4
AF_CHAOS = 5
AF_NETBIOS = 6
AF_ISO = 7
AF_OSI = 7
AF_ECMA = 8
AF_DATAKIT = 9
AF_CCITT = 10
AF_SNA = 11
AF_DECnet = 12
AF_DLI = 13
AF_LAT = 14
AF_HYLINK = 15
AF_APPLETALK = 16
AF_ROUTE = 17
AF_LINK = 18
pseudo_AF_XTP = 19
AF_COIP = 20
AF_CNT = 21
pseudo_AF_RTIP = 22
AF_IPX = 23
AF_SIP = 24
pseudo_AF_PIP = 25
AF_ISDN = 26
AF_E164 = 26
pseudo_AF_KEY = 27
AF_INET6 = 28
AF_NATM = 29
AF_ATM = 30
pseudo_AF_HDRCMPLT = 31
AF_NETGRAPH = 32
AF_SLOW = 33
AF_SCLUSTER = 34
AF_ARP = 35
AF_BLUETOOTH = 36
AF_IEEE80211 = 37
AF_MAX = 38
AF_VENDOR00 = 39
AF_VENDOR01 = 41
AF_VENDOR02 = 43
AF_VENDOR03 = 45
AF_VENDOR04 = 47
AF_VENDOR05 = 49
AF_VENDOR06 = 51
AF_VENDOR07 = 53
AF_VENDOR08 = 55
AF_VENDOR09 = 57
AF_VENDOR10 = 59
AF_VENDOR11 = 61
AF_VENDOR12 = 63
AF_VENDOR13 = 65
AF_VENDOR14 = 67
AF_VENDOR15 = 69
AF_VENDOR16 = 71
AF_VENDOR17 = 73
AF_VENDOR18 = 75
AF_VENDOR19 = 77
AF_VENDOR20 = 79
AF_VENDOR21 = 81
AF_VENDOR22 = 83
AF_VENDOR23 = 85
AF_VENDOR24 = 87
AF_VENDOR25 = 89
AF_VENDOR26 = 91
AF_VENDOR27 = 93
AF_VENDOR28 = 95
AF_VENDOR29 = 97
AF_VENDOR30 = 99
AF_VENDOR31 = 101
AF_VENDOR32 = 103
AF_VENDOR33 = 105
AF_VENDOR34 = 107
AF_VENDOR35 = 109
AF_VENDOR36 = 111
AF_VENDOR37 = 113
AF_VENDOR38 = 115
AF_VENDOR39 = 117
AF_VENDOR40 = 119
AF_VENDOR41 = 121
AF_VENDOR42 = 123
AF_VENDOR43 = 125
AF_VENDOR44 = 127
AF_VENDOR45 = 129
AF_VENDOR46 = 131
AF_VENDOR47 = 133
SOCK_MAXADDRLEN = 255
PF_UNSPEC = 0
PF_LOCAL = 1
PF_UNIX = 1
PF_INET = 2
PF_IMPLINK = 3
PF_PUP = 4
PF_CHAOS = 5
PF_NETBIOS = 6
PF_ISO = 7
PF_OSI = 7
PF_ECMA = 8
PF_DATAKIT = 9
PF_CCITT = 10
PF_SNA = 11
PF_DECnet = 12
PF_DLI = 13
PF_LAT = 14
PF_HYLINK = 15
PF_APPLETALK = 16
PF_ROUTE = 17
PF_LINK = 18
PF_XTP = 19
PF_COIP = 20
PF_CNT = 21
PF_SIP = 24
PF_IPX = 23
PF_RTIP = 22
PF_PIP = 25
PF_ISDN = 26
PF_KEY = 27
PF_INET6 = 28
PF_NATM = 29
PF_ATM = 30
PF_NETGRAPH = 32
PF_SLOW = 33
PF_SCLUSTER = 34
PF_ARP = 35
PF_BLUETOOTH = 36
PF_MAX = 38
NET_MAXID = 38
NET_RT_DUMP = 1
NET_RT_FLAGS = 2
NET_RT_IFLIST = 3
NET_RT_IFMALIST = 4
NET_RT_IFLISTL = 5
NET_RT_MAXID = 6
SOMAXCONN = 128
MSG_OOB = 0x1
MSG_PEEK = 0x2
MSG_DONTROUTE = 0x4
MSG_EOR = 0x8
MSG_TRUNC = 0x10
MSG_CTRUNC = 0x20
MSG_WAITALL = 0x40
MSG_NOTIFICATION = 0x2000
MSG_DONTWAIT = 0x80
MSG_EOF = 0x100
MSG_NBIO = 0x4000
MSG_COMPAT = 0x8000
MSG_NOSIGNAL = 0x20000
CMGROUP_MAX = 16
SCM_RIGHTS = 0x01
SCM_TIMESTAMP = 0x02
SCM_CREDS = 0x03
SCM_BINTIME = 0x04
SHUT_RD = 0
SHUT_WR = 1
SHUT_RDWR = 2
PRU_FLUSH_RD = 0
PRU_FLUSH_WR = 1
PRU_FLUSH_RDWR = 2
SF_NODISKIO = 0x00000001
SF_MNOWAIT = 0x00000002
SF_SYNC = 0x00000004
S_ISUID = 0o004000
S_ISGID = 0o002000
S_ISTXT = 0o001000
S_IRWXU = 0o000700
S_IRUSR = 0o000400
S_IWUSR = 0o000200
S_IXUSR = 0o000100
S_IREAD = 0o000400
S_IWRITE = 0o000200
S_IEXEC = 0o000100
S_IRWXG = 0o000070
S_IRGRP = 0o000040
S_IWGRP = 0o000020
S_IXGRP = 0o000010
S_IRWXO = 0o000007
S_IROTH = 0o000004
S_IWOTH = 0o000002
S_IXOTH = 0o000001
S_IFMT = 0o170000
S_IFIFO = 0o010000
S_IFCHR = 0o020000
S_IFDIR = 0o040000
S_IFBLK = 0o060000
S_IFREG = 0o100000
S_IFLNK = 0o120000
S_IFSOCK = 0o140000
S_ISVTX = 0o001000
S_IFWHT = 0o160000
ACCESSPERMS = (0o000700|0o000070|0o000007)
ALLPERMS = (0o004000|0o002000|0o001000|0o000700|0o000070|0o000007)
DEFFILEMODE = (0o000400|0o000200|0o000040|0o000020|0o000004|0o000002)
S_BLKSIZE = 512
UF_SETTABLE = 0x0000ffff
UF_NODUMP = 0x00000001
UF_IMMUTABLE = 0x00000002
UF_APPEND = 0x00000004
UF_OPAQUE = 0x00000008
UF_NOUNLINK = 0x00000010
SF_SETTABLE = 0xffff0000
SF_ARCHIVED = 0x00010000
SF_IMMUTABLE = 0x00020000
SF_APPEND = 0x00040000
SF_NOUNLINK = 0x00100000
SF_SNAPSHOT = 0x00200000
SYS_syscall = 0
SYS_exit = 1
SYS_fork = 2
SYS_read = 3
SYS_write = 4
SYS_open = 5
SYS_close = 6
SYS_wait4 = 7
SYS_link = 9
SYS_unlink = 10
SYS_chdir = 12
SYS_fchdir = 13
SYS_mknod = 14
SYS_chmod = 15
SYS_chown = 16
SYS_break = 17
SYS_freebsd4_getfsstat = 18
SYS_getpid = 20
SYS_mount = 21
SYS_unmount = 22
SYS_setuid = 23
SYS_getuid = 24
SYS_geteuid = 25
SYS_ptrace = 26
SYS_recvmsg = 27
SYS_sendmsg = 28
SYS_recvfrom = 29
SYS_accept = 30
SYS_getpeername = 31
SYS_getsockname = 32
SYS_access = 33
SYS_chflags = 34
SYS_fchflags = 35
SYS_sync = 36
SYS_kill = 37
SYS_getppid = 39
SYS_dup = 41
SYS_pipe = 42
SYS_getegid = 43
SYS_profil = 44
SYS_ktrace = 45
SYS_getgid = 47
SYS_getlogin = 49
SYS_setlogin = 50
SYS_acct = 51
SYS_sigaltstack = 53
SYS_ioctl = 54
SYS_reboot = 55
SYS_revoke = 56
SYS_symlink = 57
SYS_readlink = 58
SYS_execve = 59
SYS_umask = 60
SYS_chroot = 61
SYS_msync = 65
SYS_vfork = 66
SYS_sbrk = 69
SYS_sstk = 70
SYS_vadvise = 72
SYS_munmap = 73
SYS_mprotect = 74
SYS_madvise = 75
SYS_mincore = 78
SYS_getgroups = 79
SYS_setgroups = 80
SYS_getpgrp = 81
SYS_setpgid = 82
SYS_setitimer = 83
SYS_swapon = 85
SYS_getitimer = 86
SYS_getdtablesize = 89
SYS_dup2 = 90
SYS_fcntl = 92
SYS_select = 93
SYS_fsync = 95
SYS_setpriority = 96
SYS_socket = 97
SYS_connect = 98
SYS_getpriority = 100
SYS_bind = 104
SYS_setsockopt = 105
SYS_listen = 106
SYS_gettimeofday = 116
SYS_getrusage = 117
SYS_getsockopt = 118
SYS_readv = 120
SYS_writev = 121
SYS_settimeofday = 122
SYS_fchown = 123
SYS_fchmod = 124
SYS_setreuid = 126
SYS_setregid = 127
SYS_rename = 128
SYS_flock = 131
SYS_mkfifo = 132
SYS_sendto = 133
SYS_shutdown = 134
SYS_socketpair = 135
SYS_mkdir = 136
SYS_rmdir = 137
SYS_utimes = 138
SYS_adjtime = 140
SYS_setsid = 147
SYS_quotactl = 148
SYS_nlm_syscall = 154
SYS_nfssvc = 155
SYS_freebsd4_statfs = 157
SYS_freebsd4_fstatfs = 158
SYS_lgetfh = 160
SYS_getfh = 161
SYS_freebsd4_getdomainname = 162
SYS_freebsd4_setdomainname = 163
SYS_freebsd4_uname = 164
SYS_sysarch = 165
SYS_rtprio = 166
SYS_semsys = 169
SYS_msgsys = 170
SYS_shmsys = 171
SYS_freebsd6_pread = 173
SYS_freebsd6_pwrite = 174
SYS_setfib = 175
SYS_ntp_adjtime = 176
SYS_setgid = 181
SYS_setegid = 182
SYS_seteuid = 183
SYS_stat = 188
SYS_fstat = 189
SYS_lstat = 190
SYS_pathconf = 191
SYS_fpathconf = 192
SYS_getrlimit = 194
SYS_setrlimit = 195
SYS_getdirentries = 196
SYS_freebsd6_mmap = 197
SYS___syscall = 198
SYS_freebsd6_lseek = 199
SYS_freebsd6_truncate = 200
SYS_freebsd6_ftruncate = 201
SYS___sysctl = 202
SYS_mlock = 203
SYS_munlock = 204
SYS_undelete = 205
SYS_futimes = 206
SYS_getpgid = 207
SYS_poll = 209
SYS_freebsd7___semctl = 220
SYS_semget = 221
SYS_semop = 222
SYS_freebsd7_msgctl = 224
SYS_msgget = 225
SYS_msgsnd = 226
SYS_msgrcv = 227
SYS_shmat = 228
SYS_freebsd7_shmctl = 229
SYS_shmdt = 230
SYS_shmget = 231
SYS_clock_gettime = 232
SYS_clock_settime = 233
SYS_clock_getres = 234
SYS_ktimer_create = 235
SYS_ktimer_delete = 236
SYS_ktimer_settime = 237
SYS_ktimer_gettime = 238
SYS_ktimer_getoverrun = 239
SYS_nanosleep = 240
SYS_ntp_gettime = 248
SYS_minherit = 250
SYS_rfork = 251
SYS_openbsd_poll = 252
SYS_issetugid = 253
SYS_lchown = 254
SYS_aio_read = 255
SYS_aio_write = 256
SYS_lio_listio = 257
SYS_getdents = 272
SYS_lchmod = 274
SYS_netbsd_lchown = 275
SYS_lutimes = 276
SYS_netbsd_msync = 277
SYS_nstat = 278
SYS_nfstat = 279
SYS_nlstat = 280
SYS_preadv = 289
SYS_pwritev = 290
SYS_freebsd4_fhstatfs = 297
SYS_fhopen = 298
SYS_fhstat = 299
SYS_modnext = 300
SYS_modstat = 301
SYS_modfnext = 302
SYS_modfind = 303
SYS_kldload = 304
SYS_kldunload = 305
SYS_kldfind = 306
SYS_kldnext = 307
SYS_kldstat = 308
SYS_kldfirstmod = 309
SYS_getsid = 310
SYS_setresuid = 311
SYS_setresgid = 312
SYS_aio_return = 314
SYS_aio_suspend = 315
SYS_aio_cancel = 316
SYS_aio_error = 317
SYS_oaio_read = 318
SYS_oaio_write = 319
SYS_olio_listio = 320
SYS_yield = 321
SYS_mlockall = 324
SYS_munlockall = 325
SYS___getcwd = 326
SYS_sched_setparam = 327
SYS_sched_getparam = 328
SYS_sched_setscheduler = 329
SYS_sched_getscheduler = 330
SYS_sched_yield = 331
SYS_sched_get_priority_max = 332
SYS_sched_get_priority_min = 333
SYS_sched_rr_get_interval = 334
SYS_utrace = 335
SYS_freebsd4_sendfile = 336
SYS_kldsym = 337
SYS_jail = 338
SYS_nnpfs_syscall = 339
SYS_sigprocmask = 340
SYS_sigsuspend = 341
SYS_freebsd4_sigaction = 342
SYS_sigpending = 343
SYS_freebsd4_sigreturn = 344
SYS_sigtimedwait = 345
SYS_sigwaitinfo = 346
SYS___acl_get_file = 347
SYS___acl_set_file = 348
SYS___acl_get_fd = 349
SYS___acl_set_fd = 350
SYS___acl_delete_file = 351
SYS___acl_delete_fd = 352
SYS___acl_aclcheck_file = 353
SYS___acl_aclcheck_fd = 354
SYS_extattrctl = 355
SYS_extattr_set_file = 356
SYS_extattr_get_file = 357
SYS_extattr_delete_file = 358
SYS_aio_waitcomplete = 359
SYS_getresuid = 360
SYS_getresgid = 361
SYS_kqueue = 362
SYS_kevent = 363
SYS_extattr_set_fd = 371
SYS_extattr_get_fd = 372
SYS_extattr_delete_fd = 373
SYS___setugid = 374
SYS_eaccess = 376
SYS_afs3_syscall = 377
SYS_nmount = 378
SYS___mac_get_proc = 384
SYS___mac_set_proc = 385
SYS___mac_get_fd = 386
SYS___mac_get_file = 387
SYS___mac_set_fd = 388
SYS___mac_set_file = 389
SYS_kenv = 390
SYS_lchflags = 391
SYS_uuidgen = 392
SYS_sendfile = 393
SYS_mac_syscall = 394
SYS_getfsstat = 395
SYS_statfs = 396
SYS_fstatfs = 397
SYS_fhstatfs = 398
SYS_ksem_close = 400
SYS_ksem_post = 401
SYS_ksem_wait = 402
SYS_ksem_trywait = 403
SYS_ksem_init = 404
SYS_ksem_open = 405
SYS_ksem_unlink = 406
SYS_ksem_getvalue = 407
SYS_ksem_destroy = 408
SYS___mac_get_pid = 409
SYS___mac_get_link = 410
SYS___mac_set_link = 411
SYS_extattr_set_link = 412
SYS_extattr_get_link = 413
SYS_extattr_delete_link = 414
SYS___mac_execve = 415
SYS_sigaction = 416
SYS_sigreturn = 417
SYS_getcontext = 421
SYS_setcontext = 422
SYS_swapcontext = 423
SYS_swapoff = 424
SYS___acl_get_link = 425
SYS___acl_set_link = 426
SYS___acl_delete_link = 427
SYS___acl_aclcheck_link = 428
SYS_sigwait = 429
SYS_thr_create = 430
SYS_thr_exit = 431
SYS_thr_self = 432
SYS_thr_kill = 433
SYS__umtx_lock = 434
SYS__umtx_unlock = 435
SYS_jail_attach = 436
SYS_extattr_list_fd = 437
SYS_extattr_list_file = 438
SYS_extattr_list_link = 439
SYS_ksem_timedwait = 441
SYS_thr_suspend = 442
SYS_thr_wake = 443
SYS_kldunloadf = 444
SYS_audit = 445
SYS_auditon = 446
SYS_getauid = 447
SYS_setauid = 448
SYS_getaudit = 449
SYS_setaudit = 450
SYS_getaudit_addr = 451
SYS_setaudit_addr = 452
SYS_auditctl = 453
SYS__umtx_op = 454
SYS_thr_new = 455
SYS_sigqueue = 456
SYS_kmq_open = 457
SYS_kmq_setattr = 458
SYS_kmq_timedreceive = 459
SYS_kmq_timedsend = 460
SYS_kmq_notify = 461
SYS_kmq_unlink = 462
SYS_abort2 = 463
SYS_thr_set_name = 464
SYS_aio_fsync = 465
SYS_rtprio_thread = 466
SYS_sctp_peeloff = 471
SYS_sctp_generic_sendmsg = 472
SYS_sctp_generic_sendmsg_iov = 473
SYS_sctp_generic_recvmsg = 474
SYS_pread = 475
SYS_pwrite = 476
SYS_mmap = 477
SYS_lseek = 478
SYS_truncate = 479
SYS_ftruncate = 480
SYS_thr_kill2 = 481
SYS_shm_open = 482
SYS_shm_unlink = 483
SYS_cpuset = 484
SYS_cpuset_setid = 485
SYS_cpuset_getid = 486
SYS_cpuset_getaffinity = 487
SYS_cpuset_setaffinity = 488
SYS_faccessat = 489
SYS_fchmodat = 490
SYS_fchownat = 491
SYS_fexecve = 492
SYS_fstatat = 493
SYS_futimesat = 494
SYS_linkat = 495
SYS_mkdirat = 496
SYS_mkfifoat = 497
SYS_mknodat = 498
SYS_openat = 499
SYS_readlinkat = 500
SYS_renameat = 501
SYS_symlinkat = 502
SYS_unlinkat = 503
SYS_posix_openpt = 504
SYS_gssd_syscall = 505
SYS_jail_get = 506
SYS_jail_set = 507
SYS_jail_remove = 508
SYS_closefrom = 509
SYS___semctl = 510
SYS_msgctl = 511
SYS_shmctl = 512
SYS_lpathconf = 513
SYS_cap_new = 514
SYS_cap_getrights = 515
SYS_cap_enter = 516
SYS_cap_getmode = 517
SYS_pdfork = 518
SYS_pdkill = 519
SYS_pdgetpid = 520
SYS_pselect = 522
SYS_getloginclass = 523
SYS_setloginclass = 524
SYS_rctl_get_racct = 525
SYS_rctl_get_rules = 526
SYS_rctl_get_limits = 527
SYS_rctl_add_rule = 528
SYS_rctl_remove_rule = 529
SYS_posix_fallocate = 530
SYS_posix_fadvise = 531
SYS_wait6 = 532
SYS_MAXSYSCALL = 533
_POSIX_ADVISORY_INFO = 200112
_POSIX_ASYNCHRONOUS_IO = 0
_POSIX_CHOWN_RESTRICTED = 1
_POSIX_CLOCK_SELECTION = (-1)
_POSIX_CPUTIME = (-1)
_POSIX_FSYNC = 200112
_POSIX_IPV6 = 0
_POSIX_JOB_CONTROL = 1
_POSIX_MAPPED_FILES = 200112
_POSIX_MEMLOCK = (-1)
_POSIX_MEMLOCK_RANGE = 200112
_POSIX_MEMORY_PROTECTION = 200112
_POSIX_MESSAGE_PASSING = 200112
_POSIX_MONOTONIC_CLOCK = 200112
_POSIX_NO_TRUNC = 1
_POSIX_PRIORITIZED_IO = (-1)
_POSIX_PRIORITY_SCHEDULING = 200112
_POSIX_RAW_SOCKETS = 200112
_POSIX_REALTIME_SIGNALS = 200112
_POSIX_SEMAPHORES = 200112
_POSIX_SHARED_MEMORY_OBJECTS = 200112
_POSIX_SPORADIC_SERVER = (-1)
_POSIX_SYNCHRONIZED_IO = (-1)
_POSIX_TIMEOUTS = 200112
_POSIX_TIMERS = 200112
_POSIX_TYPED_MEMORY_OBJECTS = (-1)
_POSIX_VDISABLE = 0xff
_XOPEN_SHM = 1
_XOPEN_STREAMS = (-1)
_POSIX_VERSION = 200112
F_OK = 0
X_OK = 0x01
W_OK = 0x02
R_OK = 0x04
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2
SEEK_DATA = 3
SEEK_HOLE = 4
L_SET = 0
L_INCR = 1
L_XTND = 2
_PC_LINK_MAX = 1
_PC_MAX_CANON = 2
_PC_MAX_INPUT = 3
_PC_NAME_MAX = 4
_PC_PATH_MAX = 5
_PC_PIPE_BUF = 6
_PC_CHOWN_RESTRICTED = 7
_PC_NO_TRUNC = 8
_PC_VDISABLE = 9
_PC_ASYNC_IO = 53
_PC_PRIO_IO = 54
_PC_SYNC_IO = 55
_PC_ALLOC_SIZE_MIN = 10
_PC_FILESIZEBITS = 12
_PC_REC_INCR_XFER_SIZE = 14
_PC_REC_MAX_XFER_SIZE = 15
_PC_REC_MIN_XFER_SIZE = 16
_PC_REC_XFER_ALIGN = 17
_PC_SYMLINK_MAX = 18
_PC_ACL_EXTENDED = 59
_PC_ACL_PATH_MAX = 60
_PC_CAP_PRESENT = 61
_PC_INF_PRESENT = 62
_PC_MAC_PRESENT = 63
_PC_ACL_NFS4 = 64
_PC_MIN_HOLE_SIZE = 21
RFNAMEG = (1<<0)
RFENVG = (1<<1)
RFFDG = (1<<2)
RFNOTEG = (1<<3)
RFPROC = (1<<4)
RFMEM = (1<<5)
RFNOWAIT = (1<<6)
RFCNAMEG = (1<<10)
RFCENVG = (1<<11)
RFCFDG = (1<<12)
RFTHREAD = (1<<13)
RFSIGSHARE = (1<<14)
RFLINUXTHPN = (1<<16)
RFSTOPPED = (1<<17)
RFHIGHPID = (1<<18)
RFTSIGZMB = (1<<19)
RFTSIGSHIFT = 20
RFTSIGMASK = 0xFF
RFPROCDESC = (1<<28)
RFPPWAIT = (1<<31)
RFFLAGS = ((1<<2) | (1<<4) | (1<<5) | (1<<6) | (1<<12) |      (1<<13) | (1<<14) | (1<<16) | (1<<17) | (1<<18) | (1<<19) |      (1<<28) | (1<<31))
RFKERNELONLY = ((1<<17) | (1<<18) | (1<<31) | (1<<28))
