// 기명 함수, return 함수

// 기명 함수 (Named Function)
function greet(name) {
    return "Hello, " + name + "!";
}
println(greet("Alice"));    // 출력: Hello, Alice!
// return 함수: 값을 반환하는 함수

// --------------------------------

// 다른 함수들
// 익명 함수 (Anonymous Function) - 함수 표현식
const farewell = function(name) {
    return "Goodbye, " + name + "!";
};
println(farewell("Bob"));   // 출력: Goodbye, Bob!

// 화살표 함수 (Arrow Function) - 익명 함수의 또 다른 형태
const add = (a, b) => a + b;
println(add(5, 3));        // 출력: 8
// 기명 함수는 함수 이름이 명시되어 있어 재귀 호출이나 디버깅에 유리합니다.
// 익명 함수는 주로 일회성 작업이나 콜백 함수로 사용됩니다.
// 화살표 함수는 간결한 문법을 제공하며, this 바인딩이 다르게 동작합니다.

// 실행 함수 (Execution function, exe)
// 실행만 시키고 종료하는 함수 = 서버 가동 후 종료되는 함수