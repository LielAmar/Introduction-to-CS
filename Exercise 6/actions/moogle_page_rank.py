from typing import Dict

import moogle_helper as helper


def calculate_page_rank(traffic_dict: Dict[str, Dict[str, int]],
        iterations) -> Dict[str, float]:

    rank = {}

    # Sets the initial page rank of each page to 1.0
    for page in traffic_dict.keys():
        rank[page] = 1.0


    # Executes ${iterations} iterations.
    # For each iteration, copies the previous rank of each page, loops over all
    # pages and calculates the new rank of that page, according to this formula:
    #
    # new_rank[target_page] = previous_rank[current_page] * 
    #       (amount_of_references_from_current_to_target_page
    #           / total_references_from_current_page)
    for _ in range(iterations):
        previous_iter_rank = rank.copy()

        for page in rank.keys():
            # Calculating the total amount of references from the page
            total_references = 0
            
            for amnt_of_references in traffic_dict[page].values():
                total_references += amnt_of_references

            # Removing the points the page had in the previous iteration
            # so we only have the ones given in the current iteration left
            rank[page] -= previous_iter_rank[page]


            # Looping over all references and adding the appropraite amount of
            # points
            for reference, amnt in traffic_dict[page].items():
                rank_points = previous_iter_rank[page] * (amnt / total_references)
                rank[reference] += rank_points

            previous_iter_rank[page] = 0

    return rank


def page_rank(args: list) -> None:
    iterations, dict_file, out_file = args
    iterations = int(iterations)

    # Loads traffic data from the given file using Pickle
    traffic_dict = helper.load_dict_pickle_format(dict_file)

    # Calculates the page rank of the given traffic data
    page_rank_dict = calculate_page_rank(traffic_dict, iterations)

    helper.save_dict_pickle_format(page_rank_dict, out_file)