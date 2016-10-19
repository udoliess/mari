# mari
# marble rings
# ULi161019

# heart shape
# rings start top left
# ring0 goes right, len=23, list r0 holds marble indices
# ring1 goes up, len=26, list r1 holds marble indices

def sl(ma, ri):
    t = ma[ri[0]]
    for i in range(len(ri)-1):
        ma[ri[i]] = ma[ri[i+1]]
    ma[ri[-1]] = t

def sr(ma, ri):
    t = ma[ri[-1]]
    for i in range(len(ri)-1):
        ma[ri[-i-1]] = ma[ri[-i-2]]
    ma[ri[0]] = t

def ops(ma, r0, r1, mo):
    while mo > 3:
        if mo & 0b10:
            if mo & 0b01:
                sl(ma, r1)
            else:
                sr(ma, r1)
        else:
            if mo & 0b01:
                sr(ma, r0)
            else:
                sl(ma, r0)
        mo >>= 2

def mov(mo):
    l = list()
    while mo > 3:
        if mo & 0b10:
            if mo & 0b01:
                l.append('D')
            else:
                l.append('U')
        else:
            if mo & 0b01:
                l.append('R')
            else:
                l.append('L')
        mo >>= 2
    return l

ma = [i for i in range(45)]
r0 = [0,26,27,28,29,30,31,12,32,33,34,35,36,16,37,38,39,22,40,41,42,43,44]
r1 = [i for i in range(26)]

###############################################################################

print(ma)

print('rotate small ring:')
r0x = [i for i in range(26, 45)]
r0xl = r0x[1:] + r0x[:1]
r0xr = r0x[-1:] + r0x[:-1]
mo = 0
while True:
    mc = ma[:]
    ops(mc, r0, r1, mo)
    rc0 = mc[26:]
    if rc0 == r0xl or rc0 == r0xr:
        print(mov(mo))
        print(mc)
        break
    mo += 1

print('exchange between rings:')
mo = 0
while True:
    mc = ma[:]
    ops(mc, r0, r1, mo)
    if sum(mc[i]<26 for i in r1) == 25:
        print(mov(mo))
        print(mc)
        break
    mo += 1
