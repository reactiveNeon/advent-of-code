from collections import deque
import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 1 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    
    def transducer(s: str) -> list[int]:
        s = s[1:-1]
        return list(map(int, s.split(',')))
        
    def apply_buttons(s: str, buttons: list[int]) -> str:
        schars = list(s)
        for button in buttons:
            schars[button] = '#' if schars[button] == '.' else '.'
        return ''.join(schars)
    
    total_presses = 0
    
    for line in lines:
        splits = line.split(' ')
        final_state = splits[0][1:-1]
        buttons_list_raw = splits[1:-1]
        
        buttons_list = list(map(transducer, buttons_list_raw))
        
        initial_state = final_state.replace('#', '.')
        
        vis = set[str]()
        q = deque[str]()
        q.append(initial_state)
        vis.add(initial_state)
         
        dist = 0
        final_state_found = False
        while q:
            q_size = len(q)
            for _ in range(q_size):
                state = q.popleft()
                
                if state == final_state:
                    final_state_found = True
                    break
                    
                for buttons in buttons_list:
                    new_state = apply_buttons(state, buttons)
                    if new_state not in vis:
                        q.append(new_state)
                        vis.add(new_state)
                        
            if final_state_found:
                break
                
            dist += 1
            
        total_presses += dist
        
    return total_presses


def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
