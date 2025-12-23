function updateDate() {
    // 1. 한국 시간 기준 날짜 생성
    const today = new Date();
    
    const year = today.getFullYear();
    const month = today.getMonth() + 1;
    const date = today.getDate();
    const dayNames = ["일", "월", "화", "수", "목", "금", "토"];
    const day = dayNames[today.getDay()];

    const dateString = `${year}년 ${month}월 ${date}일 (${day})`;

    // 2. 박스 찾기 (없으면 새로 만들고, 있으면 내용만 교체)
    let box = document.querySelector('.my-box');
    
    if (!box) {
        // 처음 실행될 때 박스 생성
        const boxHTML = `<div class="my-box">${dateString}</div>`;
        document.body.insertAdjacentHTML('beforeend', boxHTML);
    } else {
        // 자정이 지나서 데이터가 바뀌면 텍스트만 업데이트
        if (box.innerText !== dateString) {
            box.innerText = dateString;
        }
    }
}

// 3. 페이지가 열릴 때 즉시 한 번 실행
updateDate();

// 4. 1초(1000ms)마다 시간을 체크해서 자정이 넘었는지 감시
setInterval(updateDate, 1000);