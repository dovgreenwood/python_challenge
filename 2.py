alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
#text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = "map"
for i in range(0, len(text)):
	if not text[i] == ' ' and not text[i] == '.' and not text[i] == '(' and not text[i] == ')' and not text[i] == ',' and not text[i] == '\'':
		
		print alphabet[alphabet.index(text[i]) + 2],
