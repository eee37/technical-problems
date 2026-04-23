class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        sub_paths = []

        cur = 0 # ASSUME: They alls start with / ?
        if len(path) == 1:
            return path

        while cur < len(path):
            print(sub_paths)
            print(cur)
            next_slash = path[cur+1:].find('/') + 1 + cur # bug: next_slash = path[cur+1:].find('/') it omits the first character hence it will alway be off by one
            if next_slash == -1:
                print('end')
                sub_paths.append(path[cur+1:])
                break
            sub_paths.append(path[cur+1:next_slash])
            if next_slash == len(path)-1:
                break
            cur = next_slash# bug: need to add next_slash to cur as I only consider substring in finding indexcur = next_slash
            # truncate forward slashes
            while cur < len(path)-1:
                if path[cur+1] == '/':
                    cur +=1
                else:
                    break
        
        ans = '/'
        while len(sub_paths) > 0:
            nxt = sub_paths.pop()
            if nxt == '.':
                continue
            elif nxt == '..' and len(sub_paths) > 0:
                sub_paths.pop()
            else:
                ans += ans + nxt
        return ans
            
            
