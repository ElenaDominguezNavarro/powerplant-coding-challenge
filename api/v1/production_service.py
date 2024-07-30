import schemas
from schemas.power_plant import PlantType
from crud.error_logs import error_logs
from fastapi import Depends
from datetime import datetime
from sqlalchemy.orm import Session


class ProductionService():
    WIND_TURBINE_COST = 0

    async def calculate_production_plan(self, payload: schemas.Payload, db: Session):
        
        powerplant_efficiencies = await self.get_powerplant_costs(payload, db)
        result = await self.get_energy_generation(payload, powerplant_efficiencies, db)

        return result
    
    async def get_powerplant_costs(self, payload: schemas.Payload, db: Session):

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
                error_message = f"Unknown powerplant type: {plant.type}"
                await self.create_error_log(db, error_message)
                raise ValueError(error_message)
            
            powerplant_efficiencies.append((plant, cost))
        
        powerplant_efficiencies.sort(key=lambda x: x[1])
        
        return powerplant_efficiencies
    
    async def get_energy_generation(self, payload: schemas.Payload, powerplant_efficiencies, db: Session):

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
            error_message = "There is not enough capacity to cover the load"
            await self.create_error_log(db, error_message)
            raise ValueError(error_message)
        return response
    
    async def create_error_log(self, db, error_message):
        
        error = schemas.ErrorLogsCreate(error_message=error_message, timestamp=datetime.now())
        await error_logs.create_error_log(db, error)
