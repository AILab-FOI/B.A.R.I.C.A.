import requests, json, os
import pandas as pd

class FOIAPIClient:
    BASE_URL = "https://nastava.foi.hr/foi-api/public"
    
    def get_buildings(self):
        return self._fetch_endpoint("buildings")

    def get_rooms(self):
        rooms = self._fetch_endpoint("rooms")
        rooms_with_details = []
        for room in rooms:
            building = room.get("building", {})
            room_detail = {
                "id": room.get("id"),
                "name": room.get("name"),
                "floor": room.get("floor"),
                "wing": room.get("wing"),
                "number": room.get("number"),
                "capacity": room.get("capacity"),
                "hrId": room.get("hrId"),
                "building_name": building.get("name"),
                "building_id": building.get("id"),
                "building_hrId": building.get("hrId")
            }
            rooms_with_details.append(room_detail)        
        return rooms_with_details

    def get_teaching_forms(self):
        return self._fetch_endpoint("teaching_forms")

    def _fetch_endpoint(self, endpoint):
        try:
            response = requests.get(f"{self.BASE_URL}/{endpoint}")
            response.raise_for_status()
            data = response.json().get("hydra:member", [])
            return data
        except Exception as e:
            print(f"Exception while getting data from endpoint {endpoint}: {e}")
            return []

    def get_json_context(self):        
        data = {
            "buildings": self.get_buildings(), 
            "rooms": self.get_rooms(), 
            "teaching_forms": self.get_teaching_forms()
        }
        return json.dumps(data, ensure_ascii = False, indent = 2)
    

    def save_to_csv(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))

        buildings = self.get_buildings()
        if buildings:
            df_buildings = pd.DataFrame(buildings)
            path_buildings = os.path.join(script_dir, "foi_buildings.csv")
            df_buildings.to_csv(path_buildings, index=False)

        rooms = self.get_rooms()
        if rooms:
            df_rooms = pd.DataFrame(rooms)
            path_rooms = os.path.join(script_dir, "foi_rooms.csv")
            df_rooms.to_csv(path_rooms, index=False)


        teaching_forms = self.get_teaching_forms()
        if teaching_forms:
            df_forms = pd.DataFrame(teaching_forms)
            path_forms = os.path.join(script_dir, "foi_teaching_forms.csv")
            df_forms.to_csv(path_forms, index=False)
            

if __name__ == "__main__":
    client = FOIAPIClient()
    client.save_to_csv()
