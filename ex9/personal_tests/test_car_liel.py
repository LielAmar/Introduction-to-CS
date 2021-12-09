def test_car():
    car = Car("a", 2, (0, 0), VERTICAL)
    assert car.car_coordinates() == [(0, 0), (1, 0)]
    assert 'u' in car.possible_moves().keys()
    assert 'd' in car.possible_moves().keys()
    assert len(car.possible_moves().keys()) == 2
    assert car.movement_requirements('u') == [(-1, 0)]
    assert car.movement_requirements('d') == [(2, 0)]
    assert car.movement_requirements('l') == []
    assert car.movement_requirements('r') == []
    assert car.move('u') == True
    assert car.move('d') == True
    assert (0, 0) in car.car_coordinates()
    assert (1, 0) in car.car_coordinates()
    assert len(car.car_coordinates()) == 2


    car2 = Car("b", 3, (1, 1), HORIZONTAL)
    assert car2.car_coordinates() == [(1, 1), (1, 2), (1, 3)]
    assert 'l' in car2.possible_moves().keys()
    assert 'r' in car2.possible_moves().keys()
    assert len(car2.possible_moves().keys()) == 2
    assert car2.movement_requirements('u') == []
    assert car2.movement_requirements('d') == []
    assert car2.movement_requirements('l') == [(1, 0)]
    assert car2.movement_requirements('r') == [(1, 4)]
    assert car2.move('u') == False
    assert car2.move('l') == True
    assert car2.move('r') == True
    assert car2.move('l') == True
    assert (1, 0) in car2.car_coordinates()
    assert (1, 1) in car2.car_coordinates()
    assert (1, 2) in car2.car_coordinates()
    assert len(car2.car_coordinates()) == 3