# Architecture

## Flow Diagram (ASCII)

```text
[Input Signal]
      |
      v
[State Check] --> [Policy Check] --> [Safety Gates] --> [Bridge] --> [Action]
                                              |
                                              v
                                        [Audit Log]
```

## Explain Like a 10-Year-Old

Think of the AI like a robot at school.
It hears a request (signal), remembers class rules (state), asks a teacher if needed (safety gates),
then uses a safe door (bridge) to do the task.
Every step is written in a notebook (audit log).

## Integration Steps

1. Define your system signals.
2. Define state fields needed for decisions.
3. Add bridges for each tool/API.
4. Put safety gates before every bridge action.
5. Save a short explanation for every action.
