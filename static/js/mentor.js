const input = document.querySelector(".chat-input input");
const button = document.querySelector(".chat-input button");
const chatBox = document.getElementById("chat-box");


function scrollToBottom(){
    chatBox.scrollTop = chatBox.scrollHeight;
}


button.addEventListener("click", () => {

    const message = input.value.trim();
    if(!message) return;

    // USER MESSAGE
    const userMsg = document.createElement("div");
    userMsg.className = "msg user";
    userMsg.textContent = message;

    chatBox.appendChild(userMsg);
    scrollToBottom();


    // AI MESSAGE
    const aiMsg = document.createElement("div");
    aiMsg.className = "msg ai";
    aiMsg.textContent = "AI is thinking...";

    chatBox.appendChild(aiMsg);
    scrollToBottom();

    input.value = "";

});


input.addEventListener("keypress", function(e){
    if(e.key === "Enter"){
        button.click();
    }
});