from abc import ABC, abstractmethod

# Classe abstraite pour les Véhicules Unmanned
class UnmannedVehicle(ABC):
    @abstractmethod
    def execute_mission(self):
        print("le véhicule va quadriller la zone de combat")

# Classe pour UUV (Unmanned Underwater Vehicle)
class UUV(UnmannedVehicle):
    def execute_mission(self):
        print("L'UUV effectue la mission sous-marine.")

# Classe pour UAV (Unmanned Aerial Vehicle)
class UAV(UnmannedVehicle):
    def execute_mission(self):
        print("L'UAV effectue la mission aérienne.")

# Classe pour UGV (Unmanned Ground Vehicle)
class UGV(UnmannedVehicle):
    def execute_mission(self):
        print("L'UGV effectue la mission terrestre.")

# Classe pour un véhicule final qui hérite de plusieurs types
class FinalVehicle(UUV, UAV, UGV):
    def execute_all_missions(self):
        print("Le véhicule final va exécuter toutes les missions.")
        UUV.execute_mission(self)
        UAV.execute_mission(self)
        UGV.execute_mission(self)

# Utilisation
if __name__ == "__main__":
    final_vehicle = FinalVehicle()
    final_vehicle.execute_all_missions()