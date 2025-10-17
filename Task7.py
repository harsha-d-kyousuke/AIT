def move(subject, x1, x2):
    return f"Move {subject} from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x, direction):
    return f"Climb box at {x} {direction}"

def have_banana(x):
    return f"Have banana at {x}"

initial_state = {
    'monkeyAt0': True,
    'monkeyLevel': 'Down',
    'bananaAt3': True,
    'boxAt1': True
}

goal_state = {
    'GetBanana': True,
    'at': 3
}

def plan_actions(initial_state, goal_state):
    actions = []
    if initial_state['monkeyAt0']:
        actions.append(move('Monkey', 0, 1))
    if initial_state['boxAt1']:
        actions.append(push_box(1, 2))
    actions.append(climb_box(2, 'Up'))
    actions.append(move('Monkey', 2, 3))
    if goal_state['GetBanana'] and goal_state['at'] == 3:
        actions.append(have_banana(3))
    return actions

actions = plan_actions(initial_state, goal_state)

print("Plan:")
for action in actions:
    print(action)
