import numpy as np

length = int(input('length: '))
goal_state = np.arange(1, length+1)
current_state = np.repeat(0, length)
best_score = 0


def get_score(state):
    score = np.sum(goal_state == state)
    return score/length


def get_random_state():
    random_state = np.random.randint(low=1, high=length+1, size=length)
    return random_state


def step_ahead_heuristic(next_state):
    changes = []
    for i in range(length):
        if next_state[i] == goal_state[i] and next_state[i] != current_state[i]:
            current_state[i] = next_state[i]
            changes.append(i)
    return changes


if __name__ == '__main__':
    current_score = get_score(current_state)
    best_score = max(current_score, best_score)

    i = 0
    while best_score < 1:
        print('previous state:', current_state)
        adjacent_state = get_random_state()
        changes = step_ahead_heuristic(adjacent_state)
        current_score = get_score(current_state)

        print('adjacent state:', adjacent_state)
        if current_score > best_score:
            print('changes:', changes)
            best_score = current_score
        print('current state: ', current_state)
        print('score: {0:.3f}\n'.format(current_score))

        i += 1

    print('iterations:', i)
