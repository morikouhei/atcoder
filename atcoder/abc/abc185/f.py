import sys
input = sys.stdin.readline

class SegTree:
    """ define what you want to do with 0 index, ex) size = tree_size, func = min or max, sta = default_value """
    
    def __init__(self,size,sta):
        self.n = size
        self.size = 1 << size.bit_length()
        self.sta = sta
        self.tree = [sta]*(2*self.size)

    def build(self, list):
        """ set list and update tree"""
        for i,x in enumerate(list,self.size):
            self.tree[i] = x

        for i in range(self.size-1,0,-1):
            self.tree[i] = self.tree[i<<1]^self.tree[i<<1 | 1]

    def set(self,i,x):
        i += self.size
        self.tree[i] ^= x
        while i > 1:
            i >>= 1
            self.tree[i] = self.tree[i<<1]^self.tree[i<<1 | 1]

    
    def get(self,l,r):
        """ take the value of [l r) with func (min or max)"""
        l += self.size
        r += self.size
        res = self.sta

        while l < r:
            if l & 1:
                res =self.tree[l]^res
                l += 1
            if r & 1:
                res = self.tree[r-1]^res
            l >>= 1
            r >>= 1
        return res

def main():
    n,q = map(int,input().split())
    l = list(map(int,input().split()))
    segt = SegTree(n,0)
    segt.build(l)
    ans = []
    for i in range(q):
        t,l,r = map(int,input().split())
        if t == 1:
            segt.set(l-1,r)
        else:
            ans.append(segt.get(l-1,r))
    for i in ans:
        print(i)
if __name__ == "__main__":
    main()