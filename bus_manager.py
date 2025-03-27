class BusManager:
    def __init__(self):
        self.buses = {}  # Dictionnaire des bus : {id: sortie_physique}

    def add_bus(self, bus_id, output_device_id):
        """Ajoute un bus de sortie"""
        self.buses[bus_id] = output_device_id

    def list_devices(self):
        """Liste les périphériques audio disponibles"""
        import sounddevice as sd
        return sd.query_devices()
