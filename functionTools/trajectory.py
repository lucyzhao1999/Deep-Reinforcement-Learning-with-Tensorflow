class SampleTrajectory:
    def __init__(self, maxRunningSteps, transit, isTerminal, reset):
        self.maxRunningSteps = maxRunningSteps
        self.transit = transit
        self.isTerminal = isTerminal
        self.reset = reset

    def __call__(self, policy):
        state = self.reset()
        while self.isTerminal(state):
            state = self.reset()

        trajectory = [state]
        for runningStep in range(self.maxRunningSteps):
            if self.isTerminal(state):
                break
            action = policy(state)
            nextState = self.transit(state, action)
            trajectory.append(nextState)
            state = nextState
        return trajectory


class SampleTrajectoryWithActions:
    def __init__(self, maxRunningSteps, transit, isTerminal, reset):
        self.maxRunningSteps = maxRunningSteps
        self.transit = transit
        self.isTerminal = isTerminal
        self.reset = reset

    def __call__(self, policy):
        state = self.reset()
        print('initState', state)

        while self.isTerminal(state):
            state = self.reset()

        trajectory = []
        for runningStep in range(self.maxRunningSteps):
            if self.isTerminal(state):
                break
            action = policy(state)
            trajectory.append((state, action))
            print(action)
            nextState = self.transit(state, action)
            state = nextState
        return trajectory

