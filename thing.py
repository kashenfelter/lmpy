print ''.join('%(pre)s%(num)s %(bot)s on the wall, %(nul)s %(bot)s,\n%(tak)s\n' % (lambda c,b:  {'pre':['','%s %s on the wall.\n\n' % (c,b)][abs(cmp(c,'Ninety-nine'))], 'num':c, 'nul':c.lower(), 'bot':b, 'tak':['Go to the store and buy some more... Ninety-nine %s.' % b,'Take one down, pass it around,'][abs(cmp(x,0))]  })((lambda x,o: [(['Twenty','Thirty','Forty','Fifty',  'Sixty','Seventy','Eighty','Ninety'][x/10-2]+'-'+o.lower()).replace('-no more',''), o][int(x<20)])(x, ['No more','One','Two',  'Three','Four','Five','Six','Seven','Eight',  'Nine','Ten','Eleven','Twelve','Thirteen','Fourteen',  'Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'][[x,x%10][int(x>=20)]]),'bottle%s of beer' % ['','s'][abs(cmp(x,1))])  for x in xrange(99,-1,-1))