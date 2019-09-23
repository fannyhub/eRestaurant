BASE_URL = "http://127.0.0.1:8000";
API_URL = BASE_URL + "/api";
MENUS_URL = API_URL + "/menus/";
MENUS_BY_NAME_URL = API_URL + "/menus/by_name/";
MENUS_BY_DISHES_URL = API_URL + "/menus/by_dish_number/";

function getJsonResponse(url) {

return new Promise(function(resolve, reject) {
    var request = new XMLHttpRequest();
    request.responseType = "json";
    request.open("GET", url, true);
    request.onload = function() {
        console.log(request.response);
        resolve(request.response);
        }
    request.send();
    });
}

async function goToNextPage(url) {

    let promise = getJsonResponse(url);
    promise.then(function(apiResponse){
        fillMenuListData(apiResponse);
    });
}

async function sortByID() {

    let promise = getJsonResponse(MENUS_URL);
    promise.then(function(apiResponse){
        fillMenuListData(apiResponse);

    });
}

async function sortByDishes() {

    let promise = getJsonResponse(MENUS_BY_DISHES_URL);
    promise.then(function(apiResponse){
        fillMenuListData(apiResponse);

    });
}

async function sortByName() {

    let promise = getJsonResponse(MENUS_BY_NAME_URL);
    promise.then(function(apiResponse){
        fillMenuListData(apiResponse);

    });
}

async function menuDetail(menuId) {
    let promise = getJsonResponse(MENUS_URL + menuId + "/");
    promise.then(function(apiResponse){
        fillDetailData(apiResponse);
    });
}

async function loadPage(url){
    sortByID();
}

function fillDetailData(apiResponse) {
    console.log(apiResponse.results);
    document.getElementById("name").innerHTML = apiResponse.name;
    document.getElementById("description").innerHTML = apiResponse.description;
    var table = document.getElementById("dish-table");
    table.innerHTML = '';
    let dishes = apiResponse.dishes;
    let fieldNames = ["name", "description", "price", "preparation_time"];
    let prefices = ["", "", "cena: ", "czas oczekiwania w min.: "]

    for (i=0; i < dishes.length; i++){
        let innerTable = document.createElement("table");
        for (j=0; j < fieldNames.length; j++) {
            let tr = document.createElement("tr");
            tr.innerHTML = prefices[j] + dishes[i][fieldNames[j]];
            innerTable.appendChild(tr);
        }
        if (dishes[i]["is_vege"]) {
            let tr = document.createElement("tr");
            tr.innerHTML = "danie vege";
            innerTable.appendChild(tr);
        }
        let space = document.createElement("br")
        innerTable.appendChild(space);

        table.appendChild(innerTable);

    }
}

function fillMenuListData(apiResponse) {
    var previous = document.getElementById("previous");
    var next = document.getElementById("next");
    var sort1 = document.getElementById("nameSort");
    var sort2 = document.getElementById("dishesSort");
    var sort3 = document.getElementById("idSort");
    var buttons = [sort1, sort2, sort3];
    for (i=0; i < buttons.length; i++) {
        if (apiResponse.results) {
            buttons[i].disabled = false;
        }
        else {
            buttons[i].disabled = true;
        }
    }
    if (apiResponse.previous) {
        previous.disabled = false;
        previous.setAttribute("title", apiResponse.previous);
    }
    else {
        previous.disabled = true;
    }
    if (apiResponse.next) {
        next.disabled = false;
        next.setAttribute("title", apiResponse.next);
    }
    else {
        next.disabled = true;
    }
    var table = document.getElementById("menu-table");
    table.innerHTML = "";
    for (i=0; i < apiResponse.results.length; i++) {
        let row = document.createElement("tr")
        row.innerHTML = apiResponse.results[i].name;
        let menuId = apiResponse.results[i].id;
        row.onclick = function() {menuDetail(menuId);};
        table.appendChild(row);
    }
}


function documentReady(fn) {
    if (document.readyState === "complete" || document.readyState === "interactive") {
        setTimeout(fn, 1);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}

documentReady(function() {
    loadPage(MENUS_URL);
});