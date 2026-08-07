import pytest
from project import calculate_daily_cost, calculate_costs, load_vehicles



def test_calculate_daily_cost_basic():
    assert calculate_daily_cost(30, 15, 262) == 524.0

def test_calculate_daily_cost_motorcycle():
    assert calculate_daily_cost(60, 60, 300) == 300.0

def test_calculate_daily_cost_small_trip():
    assert calculate_daily_cost(10, 10, 100) == 100.0

def test_calculate_daily_cost_rounds_correctly():
    assert calculate_daily_cost(10, 3, 100) == 333.33



def test_calculate_costs_whole_number():
    costs = calculate_costs(100)
    assert costs["daily"]   == 100
    assert costs["weekly"]  == 500      
    assert costs["monthly"] == 2200     
    assert costs["yearly"]  == 26400    

def test_calculate_costs_decimal():
    costs = calculate_costs(50.5)
    assert costs["daily"]   == 50.5
    assert costs["weekly"]  == 252.5
    assert costs["monthly"] == 1111.0
    assert costs["yearly"]  == 13332.0

def test_calculate_costs_returns_all_keys():
    costs = calculate_costs(200)
    assert "daily"   in costs
    assert "weekly"  in costs
    assert "monthly" in costs
    assert "yearly"  in costs



def test_load_vehicles_reads_correctly(tmp_path):
    csv_file = tmp_path / "vehicles.csv"
    csv_file.write_text("name,efficiency_kmpl\nSuzuki Swift,15\nHonda CD 70,60\n")

    vehicles = load_vehicles(str(csv_file))

    assert len(vehicles) == 2
    assert vehicles[0].name == "Suzuki Swift"
    assert vehicles[0].efficiency == 15.0
    assert vehicles[1].name == "Honda CD 70"
    assert vehicles[1].efficiency == 60.0

def test_load_vehicles_efficiency_is_float(tmp_path):
    csv_file = tmp_path / "vehicles.csv"
    csv_file.write_text("name,efficiency_kmpl\nYamaha YBR 125,45\n")

    vehicles = load_vehicles(str(csv_file))

    assert isinstance(vehicles[0].efficiency, float)

def test_load_vehicles_file_not_found():
    with pytest.raises(SystemExit):
        load_vehicles("this_file_does_not_exist.csv")
