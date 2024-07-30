import schemas
from schemas.power_plant import PlantType

class ProductionService():
    WIND_TURBINE_COST = 0
    def calculate_production_plan(self, payload: schemas.Payload):
        
        powerplant_efficiencies = self.get_powerplant_costs(payload)
        result = self.get_energy_generation(payload, powerplant_efficiencies)

        return result
    
    def get_powerplant_costs(self, payload: schemas.Payload):
        powerplant_efficiencies = []
        fuels = payload.fuels

        for plant in payload.powerplants:
            if plant.type == PlantType.WIND_TURBINE:
                cost = 0
            elif plant.type == PlantType.GAS_FIRED:
                cost = fuels['gas(euro/MWh)'] / plant.efficiency
            elif plant.type == PlantType.TURBOJET:
                cost = fuels['kerosine(euro/MWh)'] / plant.efficiency
            else:
                raise ValueError(f"Unknown powerplant type: {plant.type}")
            
            powerplant_efficiencies.append((plant, cost))
        
        powerplant_efficiencies.sort(key=lambda x: x[1])
        
        return powerplant_efficiencies
    
    def get_energy_generation(self, payload: schemas.Payload, powerplant_efficiencies):
        response = []
        fuels = payload.fuels
        remaining_load = payload.load

        for plant, _ in powerplant_efficiencies:
            if plant.type == PlantType.WIND_TURBINE:
                generated = plant.pmax * (fuels['wind(%)'] / 100.0)
            else:
                if remaining_load <= 0:
                    generated = self.WIND_TURBINE_COST
                elif remaining_load >= plant.pmin:
                    generated = min(plant.pmax, remaining_load)
                else:
                    generated = plant.pmin
            
            remaining_load -= generated
            response.append(schemas.ResponseItem(name=plant.name, p=round(generated, 1)))
        
        if remaining_load > 0:
            raise ValueError("There is not enough capacity to cover the load")
        return response