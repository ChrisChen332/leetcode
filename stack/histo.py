class histo:
        heights = [7,1,7,2,2,4]
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            print(stack)

            left = i
            while stack and stack[-1][1] > h:
                left, h1 = stack.pop()
                maxArea = max(maxArea, h1*(i - left))

            stack.append((left,h))
        
        for i,h in stack:
            print(h*(len(heights)- i))
            maxArea = max(maxArea, h*(len(heights)- i))
