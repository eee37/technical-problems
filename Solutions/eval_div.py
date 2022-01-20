'''
******************* PROBLEM STATEMENT
LC # ___

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
'''

from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
            node a: (a's root node i.e c: a/c)
        '''
        gid_weight = {}

        '''
            Return parent node

            NOTE: It is possible that during a union some nodes information becomes outdated (i.e. does
            not contain info on new root node). Find corrects this. It recalculates root node and weight
            everytime a node is not its own root. Not in the case where info is not outdated nothing really
            changes but if it is then it will update root node and correct weight
        '''
        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]
            # The above statements are equivalent to the following one
            #group_id, node_weight = gid_weight.setdefault(node_id, (node_id, 1))

            if group_id != node_id:
                # found inconsistency, trigger chain update
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = \
                    (new_group_id, node_weight * group_weight)
            return gid_weight[node_id]
        '''
            Union operator combines two (disjoint sets)


            NOTE: Weight of node a with root c is a/c = dividend/divisor
            root is always divisor in weight.
            divident is attached to divisors root node. Now they are share root
            input a, b, 2

            if b has root node c then a gets node c as root and a / c is calculated and assigned as weight
        '''
        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # merge the two groups together,
                # by attaching the dividend group to the one of divisor
                gid_weight[dividend_gid] = \
                    (divisor_gid, divisor_weight * value / dividend_weight) # NOTE: (divisor/root, divisor_weight)
                # NOTE: Py backward slash indicates logic continues in the next line

        # Step 1). build the union groups
        # NOTE: This creates graph
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []
        # Step 2). run the evaluation, with "lazy" updates in find() function
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                # case 1). at least one variable did not appear before
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # case 2). the variables do not belong to the same chain/group
                    results.append(-1.0)
                else:
                    # case 3). there is a chain/path between the variables
                    results.append(dividend_weight / divisor_weight)
        return results