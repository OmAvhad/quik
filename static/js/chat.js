// JavaScript function to get cookie by name; retrieved from https://docs.djangoproject.com/en/3.1/ref/csrf/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
       
function getResponse(){
    question = document.getElementById("question").value;
    console.log(question)
    document.getElementById("question").value = null;
    document.getElementById("chat-content").innerHTML += `<div class="media media-chat media-chat-reverse">
        <div class="media-body">
            <p>`+question+`</p>
        </div>
        </div>`;
    
    var settings = {
        "url": "http://127.0.0.1:8000/v1/get-response",
        "method": "POST",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/x-www-form-urlencoded",
          'X-CSRFToken':getCookie("csrftoken")
        },
        "data": {
          "question": question
        }
      };
      
    $.ajax(settings).done(function (response) {
        console.log(response.data['answer']);
        document.getElementById("chat-content").innerHTML +=`<div class="media media-chat">
        <img class="avatar" src="https://img.icons8.com/color/512/bot.png" alt="...">
        <div class="media-body">
            <p>`+response.data['answer']+`</p>
        </div>
        </div>`
    });
}