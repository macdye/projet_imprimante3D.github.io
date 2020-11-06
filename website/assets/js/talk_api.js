const form = document.getElementById("recherche");
const message = document.querySelector("#ia-message");

if(form){
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const input = form.querySelector("#user-answer");
        answer = input.value
        url = 'https://imprimantes3d.herokuapp.com/' + answer;
        console.log(url)
        $.getJSON(url, function(data) {
            console.log(data)
            var my_string = JSON.stringify(data, null, 4)
            message.innerHTML = my_string;
        });
    });
}