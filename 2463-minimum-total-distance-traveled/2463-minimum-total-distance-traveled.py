class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        # Flatten the factory positions based on their limits
        positions = []
        for pos, limit in factory:
            for _ in range(limit):
                positions.append(pos)
        
        num_robots = len(robot)
        num_positions = len(positions)

        memo = [[None] * num_positions for _ in range(num_robots)]

        def solve(robot_idx: int, slot_idx: int) -> int:
            # Base case 1: All robots are assigned
            if robot_idx >= num_robots:
                return 0
                
            # Base case 2: Ran out of slots, but robots still remain
            if slot_idx >= num_positions:
                return float("inf")
                
            # Return memoized result if already computed
            if memo[robot_idx][slot_idx] is not None:
                return memo[robot_idx][slot_idx]
            
            # Option 1: Take the current factory slot
            take = abs(robot[robot_idx] - positions[slot_idx]) + solve(robot_idx + 1, slot_idx + 1)

            # Option 2: Skip the current factory slot
            skip = solve(robot_idx, slot_idx + 1)

            # Assign the minimum of both choices to the memo table
            memo[robot_idx][slot_idx] = min(take, skip)

            return memo[robot_idx][slot_idx]
            
        return solve(0, 0)