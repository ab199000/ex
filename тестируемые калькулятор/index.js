let firstNum = document.querySelector(".firstNum")
let Sumv = document.querySelector(".Sumv")
let secNum = document.querySelector(".secNum")
let button = document.querySelector(".info")

button.addEventListener("click", ()=>{
    let otvet = document.querySelector(".otvet")
    let znak = Sumv.value
    if(znak=="+"){
        otvet.textContent=Number(firstNum.value) +Number(secNum.value)
    }
    else if(znak=="-"){
        otvet.textContent=Number(firstNum.value) - Number(secNum.value)
    }
    else if(znak=="*"){
        otvet.textContent=Number(firstNum.value) * Number(secNum.value)
    }
    else if(znak=="/"){
        otvet.textContent=Number(firstNum.value) / Number(secNum.value)
    }
    else if(znak=="**"){
        otvet.textContent=Number(firstNum.value) ** Number(secNum.value)
    }
 
    
    else{
        console.log(1)
        alert("Чтото пошло не так, вам не повезло")
    }
    
    // if(isNaN(otvet.textContent) ){
    //     alert("а может число попробуешь ввести?")
    //     otvet.textContent=""
    // }
    
})