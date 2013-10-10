
cmd = ""

def run(mem, cmd, base = 0) :

    def M(x) :
        if x in mem :
            return mem[x]
        
        print(mem, reg)
        raise RuntimeError(x + ' not in memory')
    
    def R(x) :
        if x in reg :
            return reg[x]
        print(mem, reg)
        raise RuntimeError(x + ' not in register')

    def encode(x) :
        x = hex(x)[2:]
        while len(x) <= 1 :
            x = '0' + x
        return x.upper()

    def arith(op, s, t) :
        s = int(s, base = 16)
        t = int(t, base = 16)

        if op == '5' :          # add
            x = (s + t) % 255
        elif op == '7' :        # or
            x = s | t
        elif op == '8' :        # and
            x = s & t
        elif op == '9' :        # xor
            x = s ^ t
        else :
            raise RuntimeError('bad operation')
        return encode(x)

    def rotate(x, t) :
        # print(x, t)
        t = int(t)
        x = bin(int(x, base = 16))[2:]
        while len(x) < 8 :
            x = '0' + x
        x = x[8 - t : ] + x[ : 8 - t]
        return encode(int(x, base = 2)).upper()

    cmd = cmd.replace(' ', '')
    reg = dict()

    lnk = encode(base)
    for i in range(len(cmd) // 2) :
        mem[encode(base)] = cmd[i * 2 : i * 2 + 2]
        base += 1

    while True :
        [op, r], [s, t] = M(lnk), M(arith('5', lnk, '01'))
        print('>', op + r + s + t, reg)
        lnk = arith('5', lnk, '02')
        if op == '1' :
            reg[r] = M(s + t)
        elif op == '2' :
            reg[r] = s + t
        elif op == '3' :
            mem[s + t] = R(r)
        elif op == '4' :
            assert(r == '0' and s != t)
            reg[t] = R(s)
        elif op in ['5', '7', '8', '9'] :
            reg[r] = arith(op, R(s), R(t))
        elif op == '6' :
            raise RuntimeError('unavailable command')
        elif op == 'A' :        # rotate
            assert(s == '0')
            reg[r] = rotate(R(r), t)
        elif op == 'B' :        # jump
            if R('0') == R(r) :
                lnk = s + t
        elif op == 'C' :
            assert(set([r, s, t]) == set('0'))
            print('Done!')
            return (mem, reg)
        else :
            raise RuntimeError('invalid command')

mem, reg = run({'8C' : '20'}, " 108C 2100 2A01 8BA0 A001 A107 711B 8BA0 A001 A107 711B 8BA0 A001 A107 711B 8BA0 A001 A107 711B 8BA0 A001 A107 711B 8BA0 A001 A107 711B 8BA0 A001 A107 711B 8BA0 A001 A107 711B 318C C000 ", base = 0x30)
# mem, reg = run({}, '2012 2111 8210 7310 C000')
# print('>> mem:', mem)
# print('>> reg:', reg)

