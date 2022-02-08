"use strict";

BASE_URL = "http://localhost:5000/api";

async function getCupcakesFromApi(){
    let response = await axios.get({
        baseURL: BASE_URL,
        url: "/cupcakes",
        method: "GET",
        },);

    return response.data.cupcakes;
}

async function showCupcakes(){
    let cupcakesList = await getCupcakesFromApi();

    for(cupcake in cupcakesList){
        let $cupcakeLi = $(`<li> 
        ${cupcake.image},
        ${cupcake.flavor},
        ${cupcake.size},
        ${cupcake.rating}
        </li>`)
    }
}
