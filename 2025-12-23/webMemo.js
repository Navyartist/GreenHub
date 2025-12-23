// 1. 오늘 날짜 가져오기 (한국 시간 기준)
const today = new Date();

// 2. 원하는 형식으로 날짜 포맷 만들기 (예: 2025년 12월 23일)
const year = today.getFullYear();
const month = today.getMonth() + 1; // 월은 0부터 시작하므로 1을 더합니다.
const date = today.getDate();

const dateString = `${year}년 ${month}월 ${date}일`;

// 3. HTML에 삽입하기
const boxHTML = `<div class="my-box">오늘은 ${dateString} 입니다.</div>`;
document.body.insertAdjacentHTML('beforeend', boxHTML);