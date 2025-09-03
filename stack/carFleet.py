class carFleet:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        zipped = list(zip(position, speed))
        sorted_zipped = sorted(zipped, reverse = True)
        stack = []
        count = 0
        for (i,j) in sorted_zipped:
            if not stack:
                stack.append((target-i)/j)
                count += 1
            else:
                current = stack.pop()
                if ((target-i)/j) <= current:
                    stack.append(current)
                else:
                    count += 1
                    stack.append((target-i)/j)
        return count
