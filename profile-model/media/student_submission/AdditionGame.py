class AdditionGame:
    def getMaximumPoints(self,A, B, C, N):
        blackboard_numbers = (A,B,C)
        points = 0
        if ((1 <= N <= 150) and (1 <= A <= 50) and (1 <= B <= 50) and (1 <= C <= 50)):
            for i in range(0,N):
                sorted_blackboard_numbers = sorted(blackboard_numbers)
                max_sorted_blackboard_numbers = max(sorted_blackboard_numbers)
                points = points + max_sorted_blackboard_numbers
                blackboard_numbers = (sorted_blackboard_numbers[0] , sorted_blackboard_numbers[1] , sorted_blackboard_numbers[2] -1)
                if blackboard_numbers==(0,0,0):
                    return points
                else:
                    continue
        return (points)   
