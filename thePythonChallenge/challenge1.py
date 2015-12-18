'''
k ->M
O->Q
E->G

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.


'''
#Solution must be incrementing all character by 1

strin ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#strinp = strin.replace(" ","")
print strin
strop =""
specChar =".{}()', "
print len(specChar)
for i in strin:
	#print chr(ord(i)+1)
	#print chr(ord(i)+2)
	if i in specChar:
		strop = strop + i
	if (i in "yz"):
		strop = strop+chr(ord(i)-24)
	else:
		strop = strop+ chr(ord(i)+2)
	

print strop
