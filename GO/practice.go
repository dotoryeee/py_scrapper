package main

//fmt == Formatting
import (
	"fmt"
	"strings"
)

func lenAndUpper(name string) (int, string) { //다중 리턴 가능
	return len(name), strings.ToUpper(name)
}

func multiply(a int, b int) int {
	return a * b
}

func repeatMe(words ...string) { //무제한으로 인수를 받을 수 있다
	defer fmt.Println("리스트 생성 완료") //defer를 이용하면 return 후 할 일을 만들 수 있다
	fmt.Println(words)
}

func superAdd(numbers ...int) int { //GO에서 반복문은 for 밖에 없다
	sum := 0
	for _, number := range numbers { //range는 인덱스와 값을 반환 -> 원하는 기능을 위해 인덱스 무시
		fmt.Println(number)
		sum += number
	}
	return sum
}

func main() {
	fmt.Println(multiply(3, 4))

	num := "0" //Type 자동 선정, Function 내에서만 사용 가능
	var name string = "dotoryeee"
	name = "jeongwon"
	fmt.Println(num)
	fmt.Println(name) //Function 을 대문자로 시작하면 Export 가능\

	totalLength, upperName := lenAndUpper("dotoryeee")
	fmt.Println(totalLength, upperName)

	repeatMe("do", "to", "to", "ry", "ee", "eeeee")

	sum := superAdd(1, 6, 7, 9)
	fmt.Println(sum)
}
