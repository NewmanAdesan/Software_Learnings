




/**
 * LOAD THE JSON DATA INTO WORKING ENVIRONMENT
 * CONVERTING JSON INTO JAVASCRIPT OBJECT
 * 
 * fetch JSON data from the file 'data.json' 
 * using XMLHttpRequest synchronously,
 * parses the JSON response into a JavaScript object.
 *
 * 
 */

// Create a new XMLHttpRequest Object
let xhr = new XMLHttpRequest();

// Set the request URL
xhr.open('GET', "./data.json", false)

// Send the request
xhr.send();

// parse the JSON response
const DATA = JSON.parse(xhr.responseText);




/**
 * Returns the great-grandfather element of a given DOM element.
 * 
 * @param {HTMLElement} element - The DOM element to start from.
 * @returns {HTMLElement} - The great-grandfather element of the input element.
 */
function greatGrandFather(element) {
    return element.parentElement.parentElement.parentElement;
}


/**
 * Checks if a given DOM element's class name contains the word "comment".
 * 
 * @param {HTMLElement} element - The DOM element to check.
 * @returns {boolean} - True if the element's class contains the word "comment", false otherwise.
 */
function hasCommentClass(element) {
    return element.classList.contains("comment") ? true : false;
}


/**
 * This function inserts a new DOM element after a selected element in the DOM tree.
 * 
 * @param {HTMLElement} newElement - The new DOM element to be inserted.
 * @param {HTMLElement} selectedElement - The existing DOM element after which the new element will be inserted.
 */
function insertAfterMe(newElement, selectedElement) {
    selectedElement.insertAdjacentElement("afterend", newElement);
}


/**
 * This function creates a reply-comment section with a div element with class "reply-comment"
 * which houses a user image, a text area for comments, and a send button.
 * 
 * @param {object} DATA - This object contains data about the current user.
 * we would destructure it to obtain the user profile image
 * @returns {HTMLElement} - The HTMLElement depicting the comment section.
 */
function generateReplyCommentSection({ currentUser: { image: { png } } }) {
    // create div element
    let divElement = document.createElement("div");

    // add class "reply-comment"
    divElement.classList.add("reply-comment");

    // add the inner html 
    divElement.innerHTML = `
    <img class="comment-photo" src="${png}" >
    <textarea class="comment-area clickable" placeholder="Add a comment..." ></textarea >
    <button class="comment-send-button clickable">REPLY</button>
  `;

    return divElement;
}


/**
 * Generate a comment score section element with an optional score value.
 * 
 * @param {object} commentInformation - Object contains the information about comment.
 * we destructure it to obtain the score information,
 * if an empty object is given, the score value will default to 0.
 * 
 * @returns {HTMLElement} The generated comment score section element.
 */
function generateCommentScoreSection({ score = 0 }) {
    // create a div element 
    let divElement = document.createElement("div");

    // add class "comment-score"
    divElement.className = "comment-score";

    // add inner html
    divElement.innerHTML = `
    <img src="./images/icon-plus.svg">
    <div class="score-value bold blue small-font-size">${score}</div>
    <img src="./images/icon-minus.svg">
  `;

    return divElement;
}


/**
 * Generate comment info section button element 
 * there are three types of this button element that can be in comment info
 * "delete button", "reply button", "edit button".
 * 
 * @param {string} buttonType - The type of button to generate.
 * @returns {HTMLElement} The generated comment info section button element.
 */
function generateCommentInfoButtonSection(buttonType) {
    // create a div element 
    let divElement = document.createElement("div");

    // add class & inner html to the divElement based on buttonType
    switch (buttonType) {
        case "delete":
            divElement.className = "delete-button clickable bold red";
            divElement.innerHTML = `
                <img src="./images/icon-delete.svg">
                <span>Delete</span>
            `;
            break;
        case "reply":
            divElement.className = "reply-button clickable bold blue";
            divElement.innerHTML = `
                <img src="./images/icon-reply.svg">
                <span>Reply</span>
            `;
            break;
        case "edit":
            divElement.className = "edit-button clickable bold blue";
            divElement.innerHTML = `
                <img src="./images/icon-edit.svg">
                <span>Edit</span>
            `;
            break;
    }

    // return the divElement
    return divElement;
}


/**
 * Generate comment info section element 
 * this section consists of the "comment-photo", "comment-name", "comment-time"
 * and one or two "comment interaction buttons".
 * 
 * @param {object} commentInformation - Object contains the information about comment. 
 * we destructure the object to obtain information we need.
 * 
 * @returns {HTMLElement} The generated comment info section element.
 */
function generateCommentInfoSection({ user: { image: { png }, username }, createdAt }) {
    // create a div element 
    let divElement = document.createElement("div");

    // add class "comment-info" to div
    divElement.className = "comment-info";

    // add the "comment-photo", "comment-name", "comment-time" html 
    divElement.innerHTML = `
        <img class="comment-photo" src="${png}">
        <span class="comment-name bold">${username}</span>
        <span class="comment-time gray">${createdAt}</span>
    `;

    /* add the comment interaction buttons to the divElement */
    // if it is the current user that has this comment info section; delete button & edit button
    if (username === DATA["currentUser"]["username"]) {
        divElement.appendChild(generateCommentInfoButtonSection("delete"));
        divElement.appendChild(generateCommentInfoButtonSection("edit"));
    }

    // if not, maybe using this function to generate comment info section for someone else; reply button
    else {
        divElement.appendChild(generateCommentInfoButtonSection("reply"));
    }

    // return the divElement
    return divElement;
}


/**
 * Generate comment message section element 
 * this section consists of the comment "message content" 
 * and the comment "recipient username".
 * 
 * @param {object} commentInformation - Object contains the information about comment. 
 * we destructure the object to obtain information we need.
 * i.e "message content" & "recipient username".
 * 
 * @returns {HTMLElement} The generated comment message section element.
 */
function generateCommentMessageSection({ content, replyingTo }) {
    // create div element
    let divElement = document.createElement("div");

    // add class "comment-message gray"
    divElement.className = "comment-message gray";

    // add inner html
    divElement.innerHTML = `<span class="reply-to bold blue">@${replyingTo}</span> ${content}`;

    return divElement;
}


/**
 * This function is called when a reply button is clicked.
 * it adds a comment section below the comment element associated with the reply button
 * 
 * @param {HTMLElement} targetElement - The Dom Element of the Reply Button.
 */
function addReplyCommentSection(targetElement) {
    // obtain the great-grandparent of the target Element
    let GGFather = greatGrandFather(targetElement);

    // ensure the great-grandparent contains the class "comments"
    if (!hasCommentClass(GGFather)) {
        console.log("The Great Grand Father of the target element does not have the 'comments' class.");
        return;
    }

    // obtain a reply comment section element
    let replyCommentSection = generateReplyCommentSection(DATA);

    // insert reply comment section immediately after grand parent element
    insertAfterMe(replyCommentSection, GGFather);

    // make the reply comment show -> this is done because we control the transitioning via "opacity property"
    setTimeout(() => {
        replyCommentSection.classList.add("show");
    }, 1);

    // return the great grand parent element & the comment section element
    return { GGFather, replyCommentSection };
}










/**
 * Set the Event handler of the reply-button
 */
document.querySelectorAll(".reply-button").forEach((replyButton) => {
    replyButton.addEventListener('click', () => {

        // if replyButton is not clickable then do nothing
        if (!replyButton.classList.contains("clickable")) {
            return;
        }

        // add a reply comment section to the great grand parent element of the reply button
        const { GGFather, replyCommentSection } = addReplyCommentSection(replyButton);


        /**
         * This function is a click event handler added to the body element.
         * if the textarea of the reply comment section has no value
         * and if we clicked on anywhere outside the reply comment section element
         * then the reply comment section will be removed from the DOM tree.
         * 
         */
        const handleClick = (event) => {
            // Get the Element that trigger the click event
            let targetElement = event.target;

            // Exit function if clicked element is the reply button. since this click adds the reply comment section
            if (targetElement.parentElement == replyButton) {

                // Make the reply button unclickable
                replyButton.classList.remove("clickable");
                return;
            }

            // Check if there is no reply text in the comment section
            if (replyCommentSection.querySelector("textarea").value == "") {

                // Check if the click area is outside the reply comment section
                if (!replyCommentSection.contains(targetElement)) {

                    // Removes the reply comment section
                    replyCommentSection.remove();

                    // Remove the click handler form body
                    document.querySelector("body").removeEventListener('click', handleClick);

                    // Make the reply button clickable
                    if (!replyButton.classList.contains("clickable")) {
                        replyButton.classList.add("clickable");
                    }
                }
            }
        }


        // Add the click handler to the body element
        document.querySelector("body").addEventListener('click', handleClick);
    })
})

