
function loadItems() {
    return fetch('../data/data.json')
    .then(response => response.json()) //성공적으로 받아왔으면 json으로 변환
    .then(json => json.items); //json 안에 있는 items 리턴
}

loadItems()
    .then(items => {
        // displayItems(items);
        // setEventListeners(items)
    })
    .catch(console.log)