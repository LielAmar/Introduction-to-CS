def input_list():
  """
  Receives a list of numbers from the user as input
  and returns a list of those numbers, with the last
  element in the list being the sum of all inputs
  """
  user_numbers = list()
  input_sum = 0

  user_input = input()
  while len(user_input) > 0:
    user_numbers.append(float(user_input))
    input_sum += float(user_input)

    user_input = input()
  
  user_numbers.append(input_sum)

  return user_numbers


def inner_product(vec_1, vec_2):
  """
  Returns the inner product of 2 vectors
  """
  
  if len(vec_1) != len(vec_2):
    return None
  
  if len(vec_1) == 0:
    return 0
  
  product = 0

  for i in range(len(vec_1)):
    product += vec_1[i] * vec_2[i]

  return product


def sequence_monotonicity(sequence=[]):
  """
  Returns whether a sequence is monotonicly increasing,
  decreasing, strictly increasing or decreasing
  """

  # if sequence == None:
  #   sequence = []

  if len(sequence) <= 1:
    return [True, True, True, True]

  sequence_checks = list()

  sequence_checks.append(check_increasing(sequence))
  sequence_checks.append(check_strictly_increasing(sequence))
  sequence_checks.append(check_decreasing(sequence))
  sequence_checks.append(check_strictly_decreasing(sequence))

  return sequence_checks

def check_increasing(sequence):
  """
  Whether the given sequence is monotonicly increasing
  """
  for i in range(1, len(sequence)):
    if sequence[i-1] > sequence[i]:
      return False

  return True

def check_strictly_increasing(sequence):
  """
  Whether the given sequence is monotonicly strictly increasing
  """
  for i in range(1, len(sequence)):
    if sequence[i-1] >= sequence[i]:
      return False

  return True

def check_decreasing(sequence):
  """
  Whether the given sequence is monotonicly decreasing
  """
  for i in range(1, len(sequence)):
    if sequence[i-1] < sequence[i]:
      return False

  return True

def check_strictly_decreasing(sequence):
  """
  Whether the given sequence is monotonicly strictly decreasing
  """
  for i in range(1, len(sequence)):
    if sequence[i-1] <= sequence[i]:
      return False

  return True


def monotonicity_inverse(def_bool):
  """
  Returns an example list following the requirements
  given in def_bool.
  
  There is a total of 16 combinations,
  but 11 of them are not valid:

  X. | True  | True  | True  | True
  X. | True  | True  | True  | False
  X. | True  | True  | False | True
  V. | True  | True  | False | False
  X. | True  | False | True  | True
  V. | True  | False | True  | False
  X. | True  | False | False | True
  V. | True  | False | False | False
  X. | False | True  | True  | True
  X. | False | True  | True  | False
  X. | False | True  | False | True
  V. | False | True  | False | False
  V. | False | False | True  | True
  V. | False | False | True  | False
  V. | False | False | False | True
  V. | False | False | False | False

  For every returned list, we can use the previous function
  to make sure get the exact same list we passed to this function
  """
  if def_bool[0] == def_bool[1] == def_bool[2] == def_bool[3] == False:
    return [1, 2, 0, 0]

  if def_bool[0] and def_bool[2] and not (def_bool[1] or def_bool[3]):
    return [1, 1, 1, 1]

  if (def_bool[0] or def_bool[1]) and (def_bool[2] or def_bool[3]):
    return None


  if def_bool[0] and def_bool[1]:
    return [0, 1, 2, 3]
  
  if def_bool[0]:
    return [0, 1, 1, 2]


  if def_bool[2] and def_bool[3]:
    return [3, 2, 1, 0]

  if def_bool[2]:
    return [2, 1, 1, 0]


  return None


def primes_for_asafi(n):
  """
  Finds the first n primes

  Uses brute force
  """
  if n == 0:
    return []

  primes = list()
  primes.append(2)

  current_test_number = 3

  while len(primes) < n:
    if is_prime(current_test_number):
      primes.append(current_test_number)
    
    current_test_number += 1

  return primes

def is_prime(number):
  """
  Checks whether the given number is a prime
  """
  if number < 2:
    return False
  
  for i in range(2, int((number/2) + 1)):
    if number % i == 0:
      return False
  
  return True


def sum_of_vectors(vec_lst):
  """
  Returns a vector representing the sum
  of the given list of vectors
  """
  if len(vec_lst) == 0:
    return None

  if len(vec_lst[0]) == 0:
    return []

  sumed_vector = list()
  
  for i in range(len(vec_lst[0])):
    sum = 0
    for vector in vec_lst:
      sum += vector[i]
    
    sumed_vector.append(sum)

  return sumed_vector


def num_of_orthogonal(vectors):
  """
  Returns the number of orthogonal couples
  in a list of vectors
  """
  amount_of_orthogonal = 0

  for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
      if inner_product(vectors[i], vectors[j]) == 0:
        amount_of_orthogonal += 1

  return amount_of_orthogonal