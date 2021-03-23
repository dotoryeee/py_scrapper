package something

import "fmt"

func sayBye(){ //소문자로 시작한 함수는 Export 불가
	fmt.Println("Good bye")
}

func SayHello(){ //대문자 함수는 Export 가능
	fmt.Println("Hello")
}