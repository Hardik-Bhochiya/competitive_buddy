const input = document.querySelector(".chat-input input");
const button = document.querySelector(".chat-input button");
const chatBox = document.getElementById("chat-box");


function scrollToBottom(){
    chatBox.scrollTo({
        top: chatBox.scrollHeight,
        behavior: "smooth"
    });
}


// ADD USER MESSAGE
function addUserMessage(message){

    const userMsg = document.createElement("div");

    userMsg.className = "user-message";
    userMsg.textContent = message;

    chatBox.appendChild(userMsg);

    setTimeout(scrollToBottom,50);

}


// ADD AI MESSAGE
function addAIMessage(message){

    const aiMsg = document.createElement("div");

    aiMsg.className = "bot-message";
    aiMsg.textContent = message;

    chatBox.appendChild(aiMsg);

    setTimeout(scrollToBottom,50);

}


// SEND MESSAGE
button.addEventListener("click", () => {

    const message = input.value.trim();
    if(!message) return;

    addUserMessage(message);

    input.value = "";

    // AI Thinking message
    const thinking = document.createElement("div");
    thinking.className = "bot-message";
    thinking.textContent = "AI is thinking...";

    chatBox.appendChild(thinking);

    scrollToBottom();

});


// ENTER KEY SUPPORT
input.addEventListener("keypress", function(e){
    if(e.key === "Enter"){
        button.click();
    }
});