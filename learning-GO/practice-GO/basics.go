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

func canIDrink(age int) bool {
	if age >= 18 {
		return true
	} else {
		return false
	}
}

func canIDrink2(age int) bool {
	switch {
	case age == 1:
		return false
	case age < 18:
		return true
	case age > 60:
		return false
	}
	return false
}

type testStruct struct { //struct (like Object) 선언
	name    string
	age     int
	favFood []string
}

func main() {
	a := 1
	fmt.Println(&a) //메모리주소 보는 법
	b := &a         //메모리 주소를 복사
	fmt.Println(b)
	fmt.Println(*b) //메모리 내용 보는 법
	*b = 10         //이런것도 가능
	fmt.Println(a)

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

	fmt.Println(canIDrink(25))
	fmt.Println(canIDrink2(25))

	names := [5]string{"doo", "too", "rye", "Eee"}
	fmt.Println(names)
	names[4] = "yeah"
	fmt.Println(names)
	infinityArray := []int{} //배열 크기를 명시하지 않으면 무한 입력 가능
	fmt.Println(infinityArray)

	li := []string{}
	li = append(li, "wowowow") //GO에서 Append는 기존 배열을 수정하지 않고 새로운 배열을 리턴
	fmt.Println(li)

	testmap := map[string]string{"name": "doto", "age": "29"} //Key : string, Value : string
	fmt.Println(testmap)
	for key, value := range testmap {
		fmt.Println(key, value)
	}

	//Struct 사용 예시
	favFood := []string{"hamburger", "chicken"}
	doto1 := testStruct{"jeong", 29, favFood}
	fmt.Println(doto1)
	fmt.Println(doto1.name)

	doto2 := testStruct{name: "jeongjeong", favFood: favFood, age: 15}
	fmt.Println(doto2)
}
