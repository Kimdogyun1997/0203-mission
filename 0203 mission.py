def find_and_insert_data(pokemon, k_hp) :
	findPos = -1
	for i in range(len(pokemons)) :
		pair = pokemons[i]
		if k_hp >= pair[1] :  #  위치 찾은 경우
			findPos = i
			break
	if findPos == -1 : # for문이 다 돌아도 값을 못 찾은 이유 -> 가장 작은 수가 옴
		findPos = len(pokemons)

	insert_data(findPos, [pokemon, k_hp])


def insert_data(position, pokemon):
	if position < 0 or position > len(pokemons):
		print("데이터를 삽입할 범위를 벗어났습니다.")
		return

	pokemons.append(None)	# 빈 칸 추가
	kLen = len(pokemons)		# 배열의 현재 크기

	for i in range(kLen - 1, position, -1):
		pokemons[i] = pokemons[i - 1]
		pokemons[i - 1] = None

	pokemons[position] = pokemon


## 전역 변수 선언 부분 ##
pokemons = [["거북왕", 1000], ["어니부기", 700], ["꼬부기", 500],["피카츄", 300]]

## 메인 코드 부분 ##
if __name__ == "__main__":

	while True:
		data = input("추가할 새로운 포켓몬--> ")
		hp = int(input("체력--> "))
		find_and_insert_data(data, hp)
		print(pokemons)
