
#Part 1
f1 = open("kdpf.txt", "r")
print (f1.name)
print(f1.readline())
seq = f1.read()
seq = seq.upper()
seq = seq.replace('\n', '')

#Part 2
length = len(seq)
print (seq,'length',length)

#Part 3
print (' '.join([seq[i:i+3]for i in range(0, length, 3)]))
#seq1 = seq
#for i in range(0, length, 3):
#    print (' ', (seq1[i:i+3])
    

print ('\n')


#Part 4

seqnext = seq
seqnext = seqnext.lower()
print ('DIRECT ORF READING FRAME: 1')

for j in range(0, len(seqnext), 3):
    print (' ', seqnext[j:j+3])
    if seqnext[j:j+3] == 'atg':
            seqnext = seqnext.upper()
            print ('------------------------------')
            start_pos = j
            for j in range (j + 3, length, 3):
                print (' ', seqnext[j:j+3])
                if (seqnext[j:j+3] == 'TGA') or (seqnext[j:j+3] == 'TAG') or (seqnext[j:j+3] == 'TAA'): #PART 6
                    end_pos = j - start_pos
                    print ("ORF length:", end_pos/3)
                    seqnext = seqnext.lower()
                elif (seqnext [j:j+3] == 'atg'): #PART 8
                    seqnext = seqnext.upper()
                    print ("Another start codon reached")
                    start_pos = j
                   
#PART 7
print ("End of the sequence has been reached")

print ('\n')

seqnext = seqnext.lower()
print ('DIRECT ORF READING FRAME: 2')
print (seqnext[0])

for j in range(1, len(seqnext), 3):
    print (' ', seqnext[j:j+3])
    if seqnext[j:j+3] == 'atg':
            seqnext = seqnext.upper()
            print ('------------------------------')
            start_pos = j
            for j in range (j + 3, length, 3):
                print (' ',seqnext[j:j+3])
                if (seqnext[j:j+3] == 'TGA') or (seqnext[j:j+3] == 'TAG') or (seqnext[j:j+3] == 'TAA'): #PART 6
                    end_pos = j - start_pos
                    print ("ORF length:", end_pos/3)
                    seqnext = seqnext.lower()
                elif (seqnext [j:j+3] == 'atg'): #PART 8
                    seqnext = seqnext.upper()
                    print ("Another start codon reached")
                    start_pos = j
             
print ("End of the sequence has been reached")  #PART 7

print ('\n')

seqnext = seqnext.lower()
print ('DIRECT ORF READING FRAME: 3')
print (seqnext[0:2])
for j in range(2, len(seqnext), 3):
    print (' ', seqnext[j:j+3])
    if seqnext[j:j+3] == 'atg':
            seqnext = seqnext.upper()
            print ('------------------------------')
            start_pos = j
            for j in range (j + 3, length, 3):
                print (' ', seqnext[j:j+3])
                if (seqnext[j:j+3] == 'TGA') or (seqnext[j:j+3] == 'TAG') or (seqnext[j:j+3] == 'TAA'): #PART 6
                    end_pos = j - start_pos
                    print ("ORF length:", end_pos/3)
                    seqnext = seqnext.lower()
                elif (seqnext [j:j+3] == 'atg'): #PART 8
                    seqnext = seqnext.upper()
                    print ("Another start codon reached")
                    start_pos = j
                
#PART 7
print ("End of the sequence has been reached")
   

#PART 10
#seqlist = list(seq)
#for k, value in enumerate(seqlist):
#    if (seqlist[k] == 'A'):
#        seqlist[k] == 'T'
#        seqlist = ''.join(seqlist)
#    if (seqlist[k] == 'C'):
#        seqlist[k] == 'G'
#        seqlist = ''.join(seqlist)
#    if (seqlist[k] == 'G'):
#        seqlist[k] == 'C'
#        seqlist = ''.join(seqlist)
#    if (seqlist[k] == 'T'):
#        seqlist[k] == 'A'
#        seqlist = ''.join(seqlist)

#print (' '.join([seqlist[k:k+3]for k in range(0, length, 3)]))


#print ('DIRECT ORF READING FRAME: -1')

#for j in range(length, 0, -3):
#    print (' ', seqlist[j:j-3])
#    if seqlist[j:j-3] == 'atg':
#            seqlist = seqlist.upper()
#            print ('------------------------------')
#            start_pos = j
#            for j in range (j - 3, length, -3):
#                print (' ', seqlist[j:j-3])
#                if (seqlist[j:j-3] == 'TGA') or (seqlist[j:j-3] == 'TAG') or (seqlist[j:j-3] == 'TAA'): #PART 6
#                    end_pos = j - start_pos
#                    print ("ORF length:", end_pos/3)
#                    seqlist = seqlist.lower()
#                elif (seqlist [j:j-3] == 'atg'): #PART 8
#                   seqlist = seqlist.upper()
#                    print ("Another start codon reached")
#                    start_pos = j
                   
#print ("End of the sequence has been reached")

#print ('\n')



