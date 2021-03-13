# https://leetcode.com/problems/slowest-key/

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key_time = {}
        key_time[keysPressed[0]] = releaseTimes[0]
        
        for index, (key, end_time) in enumerate(zip(keysPressed[1:], releaseTimes[1:])):
            duration = end_time - releaseTimes[index]
            if key not in key_time:
                key_time[key] = duration
            elif duration > key_time[key]:
                key_time[key] = duration
                
        max_duration = max(key_time.values())
        
        result = [key for key, time in sorted(key_time.items(), reverse=True)
                  if time == max_duration]
                
        return result[0]