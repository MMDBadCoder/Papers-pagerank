import random


def edge_weighted_pagerank(links, alpha, walk_count, walk_len):
    all_ids = set()
    outer_links = {}
    sum_of_outer_links_weight = {}
    for link in links:
        source, target, weight = link
        all_ids.add(source)

        if not outer_links.__contains__(source):
            outer_links[source] = {}
            sum_of_outer_links_weight[source] = 0

        if outer_links[source].__contains__(target):
            outer_links[source][target] += weight
        else:
            outer_links[source][target] = weight
        sum_of_outer_links_weight[source] += weight

    all_ids = list(all_ids)

    weights_by_id = {}
    for source_id in all_ids:
        weights = []
        other_targets_weight = (1 - alpha) * sum_of_outer_links_weight[source_id]
        other_targets_count = len(all_ids) - len(outer_links[source_id])
        other_target_weight = other_targets_weight / other_targets_count
        for target_id in all_ids:
            if outer_links[source_id].__contains__(target_id):
                weights.append(outer_links[source_id][target_id])
            else:
                weights.append(other_target_weight)
        weights_by_id[source_id] = weights

    n_ones = [1] * len(all_ids)
    end_at = {}

    start_ids = random.choices(all_ids, weights=n_ones, k=walk_count)

    for start_id in start_ids:
        current_id = start_id
        for ite in range(walk_len):
            current_id = random.choices(all_ids, weights_by_id[current_id], k=1)[0]
        if not end_at.__contains__(current_id):
            end_at[current_id] = 0
        end_at[current_id] += 1

    result = {}
    for id in all_ids:
        if end_at.__contains__(id):
            result[id] = end_at[id] / walk_count
        else:
            result[id] = 0

    return result
