from datetime import datetime
from httpx import AsyncClient
from unittest.mock import patch, MagicMock
from main import app
from api.v1.production_service import ProductionService, PlantType
from crud.error_logs import error_logs
import schemas
import pytest


@pytest.fixture
def client():
    return AsyncClient(app=app, base_url="http://test")

@pytest.fixture
def mock_production_service():
    with patch('api.v1.production_service.ProductionService') as mock:
        yield mock

@pytest.fixture
def sample_payload(): #payload3.json data
    return {
        "load": 910,
        "fuels": {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
        "powerplants": [
            {"name": "gasfiredbig1", "type": "gasfired", "efficiency": 0.53, "pmin": 100, "pmax": 460},
            {"name": "gasfiredbig2", "type": "gasfired", "efficiency": 0.53, "pmin": 100, "pmax": 460},
            {"name": "gasfiredsomewhatsmaller", "type": "gasfired", "efficiency": 0.37, "pmin": 40, "pmax": 210},
            {"name": "tj1", "type": "turbojet", "efficiency": 0.3, "pmin": 0, "pmax": 16},
            {"name": "windpark1", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 150},
            {"name": "windpark2", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 36}
        ]
    }

@pytest.fixture
def expected_response(): #response3.json data
    return [
        {"name": "windpark1", "p": 90.0},
        {"name": "windpark2", "p": 21.6},
        {"name": "gasfiredbig1", "p": 460.0},
        {"name": "gasfiredbig2", "p": 338.4},
        {"name": "gasfiredsomewhatsmaller", "p": 0.0},
        {"name": "tj1", "p": 0.0}
    ]

@pytest.mark.asyncio
async def test_production_plan(client: AsyncClient, mock_production_service: MagicMock, sample_payload, expected_response):
    """
    Test the /powerplant/v1/productionplan/ endpoint.
    It sends a POST request with the data from payload3.json (sample_payload) and verifies that 
    the response status is 200 and the JSON matches response3.json (expected_response).
    """
    mock_service_instance = mock_production_service.return_value
    mock_service_instance.calculate_production_plan.return_value = expected_response

    response = await client.post("/powerplant/v1/productionplan/", json=sample_payload)

    assert response.status_code == 200
    assert response.json() == expected_response

@pytest.mark.asyncio
async def test_get_energy_generation_insufficient_capacity():
    """
    Test that get_energy_generation raises a ValueError with the correct message
    when there is insufficient capacity to cover the load and ensures an error log is created.
    """
    mock_db = MagicMock()
    production_service = ProductionService()
    payload = schemas.Payload(
        load=1000,
        fuels={
            "gas(euro/MWh)": 20.0,
            "kerosine(euro/MWh)": 50.0,
            "co2(euro/ton)": 30.0,
            "wind(%)": 40.0
        },
        powerplants=[
            schemas.PowerPlant(name="windpark1", type=PlantType.WIND_TURBINE, efficiency=1.0, pmin=0, pmax=50),
            schemas.PowerPlant(name="gasfiredbig1", type=PlantType.GAS_FIRED, efficiency=0.5, pmin=50, pmax=150)
        ]
    )
    powerplant_costs = [
        (payload.powerplants[0], 0),
        (payload.powerplants[1], 40.0)
    ]
    
    with patch.object(production_service, 'get_powerplant_costs', return_value=powerplant_costs), \
         patch.object(production_service, 'create_error_log') as mock_create_error_log:
        
        with pytest.raises(ValueError, match="There is not enough capacity to cover the load"):
            await production_service.get_energy_generation(payload, powerplant_costs, mock_db)

        mock_create_error_log.assert_called_once_with(mock_db, "There is not enough capacity to cover the load")


@pytest.mark.asyncio
async def test_create_error_log():
    """
    Verifies that create_error_log creates an ErrorLogsCreate object with the correct
    error_message and a valid timestamp.
    """
    production_service = ProductionService()
    error_message = "Test error message"
    mock_db = MagicMock()

    with patch.object(error_logs, 'create_error_log') as mock_create_error_log:
        await production_service.create_error_log(mock_db, error_message)
    
    args, _ = mock_create_error_log.call_args
    _, error_arg = args
    
    assert isinstance(error_arg, schemas.ErrorLogsCreate)
    assert error_arg.error_message == error_message
    assert isinstance(error_arg.timestamp, datetime)