nivel_acesso: int = 5
porta_destravada: bool = False

if nivel_acesso >= 5:
    porta_destravada = True
    print()
    print("Acesso liberado")
else:
    print("Acesso negado: Permissão insuficiente!")


print(f"-------------------------------------------------------")


def analisar_temperaturas(leituras):
    if not leituras:
        return 0.0, 0
   
    media = sum(leituras) / len(leituras)

   
    alertas_calor = sum(1 for temp in leituras if temp > 30.0)

    return media, alertas_calor


def main():
    
    leituras_dia = [22.5, 25.0, 31.2, 28.4, 19.8, 32.1, 30.5]

  
    media, alertas = analisar_temperaturas(leituras_dia)

    
    print(" - Relatório de Temperaturas ")
    print(f"Temperatura média do dia: {media:.2f}°C")
    print(f"Quantidade de alertas de calor > 30.0°C: {alertas} vezes")


if __name__ == "__main__":
    main()


print(f"-------------------------------------------------------")


class LuminariaSmart:

    def __init__(self, id_dispositivo, ligada=False, intensidade=0):
        self.id_dispositivo = id_dispositivo
        self.ligada = ligada
        self.intensidade = self._validar_intensidade(intensidade)

    def alternar_estado(self):
        self.ligada = not self.ligada

    def ajustar_intensidade(self, valor):
        self.intensidade = self._validar_intensidade(valor)
    
    def _validar_intensidade(self, valor): 
        return max(0, min(100, valor))

    def __str__(self):
        estado = "Ligada" if self.ligada else "Desligada"
        return f"Luminária [{self.id_dispositivo}] | Estado: {estado} | Intensidade: {self.intensidade}%"

    def alternar_estado(self):
        
        self.ligada = not self.ligada

    def ajustar_intensidade(self, valor):
        
        self.intensidade = self._validar_intensidade(valor)

    def _validar_intensidade(self, valor):
       
        return max(0, min(100, valor))

    def __str__(self):
        estado = "Ligada" if self.ligada else "Desligada"
        return f"Luminária [{self.id_dispositivo}] | Estado: {estado} | Intensidade: {self.intensidade}%"

def main():
    
    minha_luminaria = LuminariaSmart(id_dispositivo="LUMINÁRIA-1")

    minha_luminaria.alternar_estado()
    
    minha_luminaria.ajustar_intensidade(75)
 
    print(minha_luminaria)


if __name__ == "__main__":
    main()


print(f"-------------------------------------------------------")


class DispositivoIoT:

    def __init__(self, nome: str, bateria: float):
        self.nome = nome
        self.bateria = max(0.0, min(100.0, float(bateria)))

class HubCentral:

    def __init__(self):
        self.dispositivos = []

    def adicionar_dispositivo(self, dispositivo: DispositivoIoT):
        self.dispositivos.append(dispositivo)

    def relatorio_bateria_baixa(self) -> str:
        com_bateria_baixa = [
            disp.nome for disp in self.dispositivos if disp.bateria < 20.0
        ]

        if not com_bateria_baixa:
            return "Nenhum dispositivo com bateria baixa."

        return "Dispositivos com bateria baixa (< 20%):\n- " + "\n- ".join(
            com_bateria_baixa)

def main():

    sensor_presenca = DispositivoIoT("Sensor de Presença", 85)
    fechadura_smart = DispositivoIoT("Fechadura Smart", 12)
    camera_seguranca = DispositivoIoT("Câmera Externa", 18)
    lampada_sala = DispositivoIoT("Lâmpada da Sala", 50)

    hub = HubCentral()
    hub.adicionar_dispositivo(sensor_presenca)
    hub.adicionar_dispositivo(fechadura_smart)
    hub.adicionar_dispositivo(camera_seguranca)
    hub.adicionar_dispositivo(lampada_sala)

    relatorio = hub.relatorio_bateria_baixa()
    print(relatorio)


if __name__ == "__main__":
    main()