"use strict";

const BASE_URL = "http://localhost:5001/api";
const $cupcakesList = $("#cupcakes-list");
// const $

async function getCupcakesFromApi() {
    let response = await axios.get({
        baseURL: BASE_URL,
        url: "/cupcakes",
        method: "GET",
    });

    return response.data.cupcakes;
}

async function showCupcakes() {
    $cupcakesList.empty();
    let cupcakesFromAPI = await getCupcakesFromApi();

    for (cupcake in cupcakesFromAPI) {
        let $cupcakeLi = $(`<li> 
        ${cupcake.image},
        ${cupcake.flavor},
        ${cupcake.size},
        ${cupcake.rating}
        </li>`)

        $cupcakesList.append($cupcakeLi)
    }
}   
