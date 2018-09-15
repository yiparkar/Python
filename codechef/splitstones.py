tcCount = int(input())
for i in range(0,tcCount):
   tc = map(int, input().strip().split())
   initial = tc[:3]
   after = tc[3:]
   if (sum(initial) == sum(after)):
    if(min(initial) <= min(after)):
        print('Yes')
    else:
        print('No')
        
   else:
       print('No')
