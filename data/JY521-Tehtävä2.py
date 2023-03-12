# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman
# ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f'the elevator goes up to the floor {self.current_floor}')

    def floor_down(self):
        self.current_floor -= 1
        print(f'the elevator goes down to the floor {self.current_floor}')

    def go_to_floor(self, floor):
        if floor >= self.bottom_floor and floor <= self.top_floor:
            while self.current_floor != floor:
                if floor > self.current_floor:
                    self.floor_up()
                else:
                    self.floor_down()
            print("You have reached floor ", floor)
        else:
            print("Invalid floor number")


class Building:
    def __init__(self, elevators, bottom_num, top_num):
        self.bottom_num = bottom_num
        self.top_num = top_num

        self.elevators = [Elevator(bottom_num, top_num) for i in range(elevators)]

    def run_elevator(self, elevator_number, destination):

        self.elevators[elevator_number].go_to_floor(destination)


new_Building = Building(2, 0, 10)

#elevator run floor values

new_Building.run_elevator(0, 5)
new_Building.run_elevator(1, 7)