from actions import moogle_crawler as cr
from actions import moogle_page_rank as pr


# === CONSTANTS ===

BASE_URL = "https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/"
SMALL_INDEX_FILE_LOCATION = "misc/small_index.txt"


# === TESTS ===

def test_page_rank_calculation():
    input = {
        "Hogwarts": {
            "Harry Potter": 1
        },
        "Harry Potter": {
            "Hermione Granger": 1,
            "Draco Malfoy": 1
        },
        "Hermione Granger": {},
        "Draco Malfoy": {
            "Harry Potter": 1
        }
    }

    result1 = pr.calculate_page_rank(input, 1)
    expected1 = {'Hogwarts': 0.0, 'Harry Potter': 2, 'Hermione Granger': 0.5, 'Draco Malfoy': 0.5}
    assert result1 == expected1

    result2 = pr.calculate_page_rank(input, 2)
    expected2 = {'Hogwarts': 0.0, 'Harry Potter': 0.5, 'Hermione Granger': 1.0, 'Draco Malfoy': 1.0}
    assert result2 == expected2

    result3 = pr.calculate_page_rank(input, 3)
    expected3 = {'Hogwarts': 0.0, 'Harry Potter': 1, 'Hermione Granger': 0.25, 'Draco Malfoy': 0.25}
    assert result3 == expected3

    result4 = pr.calculate_page_rank(input, 4)
    expected4 = {'Hogwarts': 0.0, 'Harry Potter': 0.25, 'Hermione Granger': 0.5, 'Draco Malfoy': 0.5}
    assert result4 == expected4

    result5 = pr.calculate_page_rank(input, 5)
    expected5 = {'Hogwarts': 0.0, 'Harry Potter': 0.5, 'Hermione Granger': 0.125, 'Draco Malfoy': 0.125}
    assert result5 == expected5


def test_crawler():  
    result1 = cr.load_traffic_dictionary(BASE_URL, SMALL_INDEX_FILE_LOCATION)
    expected1 = {'Albus_Dumbledore.html': {'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 21, 'Tom_Riddle.html': 29, 'Harry_Potter.html': 25, 'Ronald_Weasley.html': 4, 'Hermione_Granger.html': 5, 'Severus_Snape.html': 17, 'Rubeus_Hagrid.html': 8, 'Neville_Longbottom.html': 4, 'Ginevra_Weasley.html': 6, 'Luna_Lovegood.html': 3, 'Draco_Malfoy.html': 7}, 'Draco_Malfoy.html': {'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 12, 'Harry_Potter.html': 17, 'Tom_Riddle.html': 20, 'Albus_Dumbledore.html': 9, 'Severus_Snape.html': 10, 'Rubeus_Hagrid.html': 6, 'Ronald_Weasley.html': 10, 'Hermione_Granger.html': 15, 'Neville_Longbottom.html': 6, 'Ginevra_Weasley.html': 7, 'Luna_Lovegood.html': 2}, 'Ginevra_Weasley.html': {'Harry_Potter.html': 20, 'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 10, 'Tom_Riddle.html': 
            15, 'Albus_Dumbledore.html': 5, 'Severus_Snape.html': 4, 'Luna_Lovegood.html': 8, 'Ronald_Weasley.html': 13, 'Draco_Malfoy.html': 8, 'Hermione_Granger.html': 13, 'Rubeus_Hagrid.html': 3, 'Neville_Longbottom.html': 5}, 'Harry_Potter.html': {'Neville_Longbottom.html': 15, 'Tom_Riddle.html': 30, 'Severus_Snape.html': 32, 'Albus_Dumbledore.html': 30, 'Rubeus_Hagrid.html': 27, 'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 18, 'Ronald_Weasley.html': 19, 'Hermione_Granger.html': 27, 'Ginevra_Weasley.html': 12, 'Draco_Malfoy.html': 27, 'Luna_Lovegood.html': 13}, 'Hermione_Granger.html': {'Harry_Potter.html': 24, 'Ronald_Weasley.html': 31, 'Ginevra_Weasley.html': 14, 'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 17, 'Tom_Riddle.html': 16, 'Neville_Longbottom.html': 5, 'Draco_Malfoy.html': 9, 'Rubeus_Hagrid.html': 11, 'Severus_Snape.html': 10, 'Albus_Dumbledore.html': 11, 'Luna_Lovegood.html': 9}, 'Hogwarts_School_of_Witchcraft_and_Wizardry.html': {'Harry_Potter.html': 8, 'Albus_Dumbledore.html': 8, 'Tom_Riddle.html': 5, 'Rubeus_Hagrid.html': 1, 'Severus_Snape.html': 8, 'Ronald_Weasley.html': 3, 'Hermione_Granger.html': 2, 'Ginevra_Weasley.html': 2, 'Draco_Malfoy.html': 1, 'Neville_Longbottom.html': 1}, 'Luna_Lovegood.html': {'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 6, 'Harry_Potter.html': 10, 'Tom_Riddle.html': 6, 'Ginevra_Weasley.html': 7, 'Neville_Longbottom.html': 8, 'Ronald_Weasley.html': 7, 'Hermione_Granger.html': 7, 'Severus_Snape.html': 2, 'Albus_Dumbledore.html': 1, 'Rubeus_Hagrid.html': 2}, 'Neville_Longbottom.html': {'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 9, 'Harry_Potter.html': 10, 
            'Hermione_Granger.html': 9, 'Ronald_Weasley.html': 8, 'Ginevra_Weasley.html': 8, 'Tom_Riddle.html': 7, 'Rubeus_Hagrid.html': 3, 'Draco_Malfoy.html': 5, 'Severus_Snape.html': 8, 'Luna_Lovegood.html': 6, 'Albus_Dumbledore.html': 3}, 'Ronald_Weasley.html': {'Draco_Malfoy.html': 13, 'Harry_Potter.html': 20, 'Ginevra_Weasley.html': 17, 'Hermione_Granger.html': 20, 'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 12, 'Tom_Riddle.html': 12, 'Albus_Dumbledore.html': 16, 'Rubeus_Hagrid.html': 9, 'Neville_Longbottom.html': 8, 'Luna_Lovegood.html': 7, 'Severus_Snape.html': 7}, 'Rubeus_Hagrid.html': {'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 17, 'Tom_Riddle.html': 19, 'Albus_Dumbledore.html': 20, 'Harry_Potter.html': 20, 'Ronald_Weasley.html': 8, 'Hermione_Granger.html': 8, 'Draco_Malfoy.html': 3, 'Severus_Snape.html': 5, 'Ginevra_Weasley.html': 2, 'Luna_Lovegood.html': 1, 'Neville_Longbottom.html': 1}, 'Severus_Snape.html': {'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 14, 'Tom_Riddle.html': 21, 'Harry_Potter.html': 22, 'Albus_Dumbledore.html': 18, 'Draco_Malfoy.html': 10, 
            'Hermione_Granger.html': 5, 'Neville_Longbottom.html': 4, 'Ronald_Weasley.html': 5, 'Luna_Lovegood.html': 2, 'Ginevra_Weasley.html': 1, 'Rubeus_Hagrid.html': 3}, 'Tom_Riddle.html': {'Albus_Dumbledore.html': 21, 'Hogwarts_School_of_Witchcraft_and_Wizardry.html': 16, 'Harry_Potter.html': 29, 'Rubeus_Hagrid.html': 6, 'Severus_Snape.html': 15, 'Neville_Longbottom.html': 5, 'Hermione_Granger.html': 7, 'Draco_Malfoy.html': 9, 'Ginevra_Weasley.html': 4, 'Ronald_Weasley.html': 5, 'Luna_Lovegood.html': 1}}
    
    assert result1 == expected1
