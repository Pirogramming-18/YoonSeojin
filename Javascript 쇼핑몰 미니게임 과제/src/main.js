
function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json()) //성공적으로 받아왔으면 json으로 변환
    .then(json => json.items); //json 안에 있는 items 리턴
}

function displayItems(items) {
    const container = document.querySelector('.items');
    //각각의 아이템을 Html로 변환한 후(map) join을 통해서 하나의 문자열로 만들기
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

//이 함수는 item을 html 요소로 바꿔주는 작업을 함! ₩₩ 이용
function createHTMLString(item) {
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail">
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

loadItems()
    .then(items => {
        displayItems(items);
        setEventListeners(items)
    })
    .catch(console.log)