
s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
  "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s1 = 'map'
new_s = ""
for c in s1:
    if ord(c) > 96 and ord(c) < 121:
        new_s += chr(ord(c) + 2)
    elif c == 'y':
        new_s = new_s + 'a'
    elif c == 'z':
        new_s = new_s + 'b'
    else:
        new_s = new_s + c

print(new_s)

new_s2 = ''
translator_dict = s.maketrans('yzabcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxyz')
for c in s:
    if ord(c) in translator_dict.keys():
        new_s2 = new_s2 + chr(translator_dict.get(ord(c)))
    else:
        new_s2 = new_s2 + c

print(new_s2)