import itertools
from os import remove

class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms

    def __str__(self):
        return self.illness + " for " + str(self.symptoms)
        
class Diagnoser:
    def __init__(self, root: Node):
        self.root = root
        
    def diagnose(self, symptoms):
        """
        Diagnoses your illness according to the symptoms given in ${symptoms}
        and the decision tree ${self.root}
        """
        
        copy = self.root
        
        # Keeps on going in-depth of the tree as long as we don't reach a leaf,
        # which means an illness was found
        while copy.positive_child and copy.negative_child:
            if copy.data in symptoms:
                copy = copy.positive_child
            else:
                copy = copy.negative_child

        return copy.data


    def calculate_success_rate(self, records):
        """
        Calculates the success rate of the diagnoser by
        examinating the given records and checking the decisions tree's
        diagnostic
        """
        
        length = len(records)

        if length <= 0:
            raise ValueError("The length of the records list cannot be 0 or \
                    negative")

        successes = 0

        # Loops over all records and adds 1 to successes if the diagnostic was
        # successfull
        for record in records:
            if record.illness == self.diagnose(record.symptoms):
                successes += 1

        return successes/length


    def all_illnesses(self):
        """
        Calculates the success rate of the diagnoser by
        examinating the given records and checking the decisions tree's
        diagnostic.
        The returned list is ordered based on occurences and doesn't have duplications
        """

        copy = self.root

        illnesses_map = dict()
        self.__all_illnesses_helper(copy, illnesses_map)

        results = [item for item in illnesses_map.keys()]
        results.sort(key=lambda illness: illnesses_map[illness], reverse=True)

        return results
    
    def __all_illnesses_helper(self, node, illnesses_map):
        """
        A helper function that uses recursion to loop over all leafs of a tree
        and add the data to the provided map at ${illnesses_map}
        """
        
        if not (node.positive_child and node.negative_child):
            if node.data is not None:
                if not node.data in illnesses_map:
                    illnesses_map[node.data] = 0
                
                illnesses_map[node.data] += 1
            return

        self.__all_illnesses_helper(node.positive_child, illnesses_map)
        self.__all_illnesses_helper(node.negative_child, illnesses_map)


    def paths_to_illness(self, illness):
        """
        Calculates all the paths to get to illness in the tree ${self.root}
        """

        copy = self.root

        results = self.__paths_to_illness_helper(copy, illness)

        # If results is None we return an empty list, otherwise we return results
        return [] if results == None else results

    def __paths_to_illness_helper(self, node, illness):
        """
        A helper function that uses recursion to loop over all leafs of a tree
        and add returns a path to that leaf if it's data is equal to ${illness}
        """

        # If we don't have any more children we want to return an empty list
        # if the leaf's data is indeed the illness we were looking for.
        # Otherwise, we return None
        if not (node.positive_child and node.negative_child):
            if node.data == illness:
                return [[]]
            
            return None

        # Creating a list of paths using this algorithm:
        # - Loops over all positive child's results and adds them to paths with
        #   'True' in the first index
        # - Loops over all negative child's results and adds them to paths with
        #   'False' in the first index
        paths = []

        results = self.__paths_to_illness_helper(node.positive_child, illness)
        if results != None:
            for result in results:
                paths.append([True] + result)
        
        results = self.__paths_to_illness_helper(node.negative_child, illness)
        if results != None:
            for result in results:
                paths.append([False] + result)
        
        # If both children had no paths we want to return None since we don't
        # have any solution.
        if len(paths) == 0:
            return None

        # Otherwise, we'd return our paths
        return paths


    def minimize(self, remove_empty=False):
        self.root = self.__deep_copy_node(self.root)

        self.__remove_unnecessary(self.root)

        if remove_empty:
            self.__remove_empty(self.root)


    def __remove_unnecessary(self, root):
        if not (root.positive_child and root.negative_child):
            return root

        positive_child = root.positive_child
        negative_child = root.negative_child
        
        if self.__compare_nodes(positive_child, negative_child):
            return self.__remove_unnecessary(positive_child)
        
        root.positive_child = self.__remove_unnecessary(positive_child)
        root.negative_child = self.__remove_unnecessary(negative_child)

        return root

    def __remove_empty(self, root):
        if not (root.positive_child and root.negative_child):
            return root

        positive_child = root.positive_child
        negative_child = root.negative_child
        
        if positive_child.data != None and negative_child.data == None and \
                positive_child.positive_child and positive_child.negative_child:
            return self.__remove_empty(positive_child)
        elif positive_child.data == None and negative_child.data != None and \
                negative_child.positive_child and negative_child.negative_child:
            return self.__remove_empty(negative_child)
        
        root.positive_child = self.__remove_empty(positive_child)
        root.negative_child = self.__remove_empty(negative_child)

        return root

    def __deep_copy_node(self, node):
        """
        Copies a node
        """
        
        new_node = Node(node.data)

        if node.positive_child:
            new_node.positive_child = self.__deep_copy_node(node.positive_child)

        if node.negative_child:
            new_node.negative_child = self.__deep_copy_node(node.negative_child)

        return node

    def __compare_nodes(self, node1, node2):
        """
        A recursive helper function to compare 2 given nodes
        """
        
        if not (node1.positive_child and node1.negative_child) and \
                not (node2.positive_child and node2.negative_child):
            return node1.data == node2.data

        if node1.positive_child and node1.negative_child and not \
                (node2.positive_child and node2.negative_child):
            return False

        if node2.positive_child and node2.negative_child and not \
                (node1.positive_child and node1.negative_child):
            return False

        return self.__compare_nodes(node1.negative_child, \
                node2.negative_child) and \
                self.__compare_nodes(node1.positive_child, \
                node2.positive_child)


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


def build_tree(records, symptoms):
    if len(symptoms) == 0:
        return Node(None, None, None)

    for item in symptoms:
        if type(item) != str:
            raise TypeError("A given symptom type is not a string!")

    for item in records:
        if type(item) != Record:
            raise TypeError("A given record type is not a Record!")

    return Diagnoser(__build_tree_helper(records, symptoms))

def __build_tree_helper(records, symptoms):
    """
    A recursive helper function to build a certain level of a tree
    """
    
    if len(symptoms) == 0:
        occorences_map = __build_oocorences_map(records)

        if len(occorences_map) == 0:
            illness = None
        else:
            illness = max(occorences_map, key=lambda item: occorences_map[item])
        
        return Node(illness, None, None)

    node = Node(symptoms[0])

    positive_records = [record for record in records if (symptoms[0] in record.symptoms)]
    negative_records = [record for record in records if (symptoms[0] not in record.symptoms)]

    node.positive_child = __build_tree_helper(positive_records, symptoms[1:])
    node.negative_child = __build_tree_helper(negative_records, symptoms[1:])

    return node

def __build_oocorences_map(records):
    occorences_map = dict()
        
    for record in records:
        if not record.illness in occorences_map:
            occorences_map[record.illness] = 0
        else:
            occorences_map[record.illness] += 1
        
    return occorences_map


def optimal_tree(records, symptoms, depth):
    if not 0 <= depth <= len(symptoms):
        raise ValueError("Invalid depth")
    
    for item in symptoms:
        if symptoms.count(item) > 1:
            raise ValueError("Duplications found in symptoms")

    best_diagnoser = None

    for sub_symptoms in itertools.combinations(symptoms, depth):
        diagnoser = build_tree(records, list(sub_symptoms))

        if best_diagnoser == None:
            best_diagnoser = diagnoser
        else:
            if diagnoser.calculate_success_rate(records) > \
                    best_diagnoser.calculate_success_rate(records):
                best_diagnoser = diagnoser
    
    return best_diagnoser


if __name__ == "__main__":
    data = parse_data("medium_data.txt")

    symptoms = ["cough", "fatigue", "headache", "nausea",
                "fever", "irritability", "rigidity", "sore_throat"]
    diagnoser = optimal_tree(data, symptoms, 8)
    print(diagnoser.calculate_success_rate(data))

    pass