import math

def minimax(cur_depth, node_index, max_turn, scores, target_depth):
    if cur_depth == target_depth:
        return scores[node_index]

    if max_turn:
        return max(minimax(cur_depth + 1, node_index * 2, False, scores, target_depth),
                   minimax(cur_depth + 1, node_index * 2 + 1, False, scores, target_depth))
    else:
        return min(minimax(cur_depth + 1, node_index * 2, True, scores, target_depth),
                   minimax(cur_depth + 1, node_index * 2 + 1, True, scores, target_depth))

# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_depth = int(math.log2(len(scores)))

print("The optimal value is:", minimax(0, 0, True, scores, tree_depth))
