function updateDate() {
    const today = new Date();
    
    // 1. 날짜 부분 만들기 (2025년 12월 23일)
    const year = today.getFullYear();
    const month = today.getMonth() + 1;
    const date = today.getDate();
    
    // 2. 시간 부분 만들기 (시:분:초)
    // padStart(2, '0')는 숫자가 한 자리일 때 앞에 '0'을 붙여서 '09'처럼 보이게 해줍니다.
    const hours = String(today.getHours()).padStart(2, '0');
    const minutes = String(today.getMinutes()).padStart(2, '0');
    const seconds = String(today.getSeconds()).padStart(2, '0');

    // 3. 전체를 하나의 문자열로 합치기
    const fullText = `${year}년 ${month}월 ${date}일 ${hours}:${minutes}:${seconds}`;

    // 4. 화면에 뿌려주기
    let box = document.querySelector('.my-box');
    
    if (!box) {
        // 박스가 처음 생성될 때
        document.body.insertAdjacentHTML('beforeend', `<div class="my-box">${fullText}</div>`);
    } else {
        // 이미 있는 박스의 내용만 1초마다 업데이트
        box.innerText = fullText;
    }
}

// 1초마다 실행
setInterval(updateDate, 1000);
updateDate(); // 실행하자마자 첫 화면을 보여주기 위해 호출