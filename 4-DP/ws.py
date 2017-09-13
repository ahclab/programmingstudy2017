#! python
import sys
from collections import defaultdict
import math

trainfilename = sys.argv[1]
testfilename  = sys.argv[2]

allwordcount = 0.0

train_file = open(trainfilename, "r")
test_file = open(testfilename, "r")
count_dict = defaultdict(lambda: 0.0)

for line in train_file:
    words = line.rstrip().split(" ")
    for word in words:
        allwordcount += 1
        count_dict[word] += 1
        

uniprob_dict = defaultdict(lambda: 0.0)
        
for dictword in count_dict.keys():
    wordcount = count_dict[dictword]
    uni_prob = - math.log2(wordcount) + math.log2(allwordcount)
    uniprob_dict[dictword] = uni_prob
        
    
for line in test_file:
    
    line = line.rstrip()

    best_scores = [0.0] * (len(list(line))+1)
    best_edges = [[]] * (len(list(line))+1)

    best_scores[0] = 0.0
    best_edges[0] = ""

    char_a = list(line)    

    end_cnt = 0

    #forward
    while end_cnt < len(char_a):
        end_cnt += 1
#        print(end_cnt,len(best_scores))        
        best_scores[end_cnt] = 1000000000
        begin_cnt = -1
        while begin_cnt < end_cnt-1:
            begin_cnt += 1
#            print("".join(char_a[begin_cnt:end_cnt]))
            word = "".join(char_a[begin_cnt:end_cnt])
            prob = uniprob_dict[word]
            if prob != 0.0 or len(word) == 1:                
                score = best_scores[begin_cnt] + prob
                print(begin_cnt," ",end_cnt," ",word," ",score," ",best_scores[end_cnt])
                if score < best_scores[end_cnt]:
                    best_scores[end_cnt] = score
                    best_edges[end_cnt] = [begin_cnt,end_cnt]
    
    #backward
    words = []
#    print(best_edges)
    best_edges.reverse()
    best_edges.pop()
    print(best_edges)    

    cnt = 0
    while cnt < len(best_edges):
        next_edge = best_edges[cnt]
        word = "".join(char_a[next_edge[0]:next_edge[1]])
        words.append(word)
        cnt += (next_edge[1]-next_edge[0])
    
#    for next_edge in best_edges:
#        word = "".join(char_a[next_edge[0]:next_edge[1]])
#        words.append(word)
    words.reverse()
    print(" ".join(words)+"\n")
        
    break
    


