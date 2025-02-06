
s = "dddbbeeebca"
k = 3

def removeKConsecutiveElements(s, k):
    
    stack = []
    i = 0
    n = len(s)
    while i < n:
        print(stack)
        if stack and stack[-1][0] == s[i]:
            stack.append([s[i], stack[-1][1] + 1])
        else: 
            stack.append([s[i], 1])
            
        if stack and stack[-1][1] == k:
            for _ in range(k):
                stack.pop()
        
        i += 1
        
    print("".join([x[0] for x in stack]))
        
    
s = "dddbbeeebca"
k = 3
removeKConsecutiveElements(s, k)

k = 2
s = "bacbbaac"
removeKConsecutiveElements(s, k)