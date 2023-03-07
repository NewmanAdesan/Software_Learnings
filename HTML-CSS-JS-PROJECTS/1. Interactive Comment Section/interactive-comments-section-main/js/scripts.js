




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


function createDOMElement(html) {
    const range = document.createRange();
    const fragment = range.createContextualFragment(html);
    return fragment.firstChild;
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
    // create reply-comment section DOM Element
    let divElement = createDOMElement(`<div class="reply-comment">
        <img class="comment-photo" src="${png}">
        <textarea class="comment-area page-font-styles clickable" placeholder="Add a comment..."></textarea>
        <button class="comment-send-button page-font-styles clickable">SEND</button>
    </div>`);

    return divElement;
}


/**
 * a replyCommentSection is a div element with class "reply-comment show"
 * that contains "user profile picture", "user comment message", "send button"
 * 
 * This Function would place this data into an Object Notation
 * with properties "username", "content", "createdAt", "user:{image:{png}}"
 * this is based on how a commentInformation object would look like
 * 
 * @param {HTMLElement} replyCommentSection 
 * @returns {Object} 
 *  */
function generateCommentInformation(replyCommentSection) {
    let commentInformation = {
        content: replyCommentSection.querySelector("textarea").value,
        createdAt: "today",
        user: {
            image: {
                png: replyCommentSection.querySelector("img").getAttribute("src")
            }
        },

    }

    // extract the username info from the image path
    commentInformation["user"]["username"] = commentInformation.user.image.png.match(/image-(.+).png/)[1];

    return commentInformation;

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
    // create comment-score section DOM Element
    let divElement;
    if (score > 0 && score < 1000) {
        divElement = createDOMElement(`<div class="comment-score">
        <img src="./images/icon-plus.svg">
        <div class="score-value bold blue small-font-size">${score}</div>
        <img src="./images/icon-minus.svg">
      </div>`);
    }
    else {
        divElement = createDOMElement(`<div class="comment-score">
        <img src="./images/icon-plus.svg">
        <div class="score-value bold blue very-small-font-size">${score}</div>
        <img src="./images/icon-minus.svg">
      </div>`);
    }

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
    // create comment info button section DOM Element 
    let divElement;

    // add class & inner html to the divElement based on buttonType
    switch (buttonType) {
        case "delete":
            divElement = createDOMElement(`<div type="button" class="delete-button clickable bold red" data-bs-toggle="modal" data-bs-target="#myModal">
                    <img src="./images/icon-delete.svg">
                    <span>Delete</span>
                </div>
            `);

            // make delete button a bootstrap modal button
            divElement.setAttribute("type", "button");
            divElement.setAttribute("data-bs-toggle", "modal");
            divElement.setAttribute("data-bs-target", "#myModal");
            break;
        case "reply":
            divElement = createDOMElement(`<div class="reply-button clickable bold blue">
                    <img src="./images/icon-reply.svg">
                    <span>Reply</span>
                </div>
            `);
            break;
        case "edit":
            divElement = createDOMElement(`<div class="edit-button clickable bold blue">
                    <img src="./images/icon-edit.svg">
                    <span>Edit</span>
                </div>
            `);
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
    // create comment info section DOM Element
    let divElement = createDOMElement(`<div class="comment-info">
        <img class="comment-photo" src="${png}">
        <span class="comment-name bold">${username}</span>
        <span class="comment-time gray">${createdAt}</span>
  </div>`);


    /* add the comment interaction buttons to the divElement */
    // if it is the current user that has this comment info section; delete button & edit button
    if (username === DATA["currentUser"]["username"]) {
        divElement.querySelector('span.comment-name').classList.add("current-user");
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
function generateCommentMessageSection({ content, replyingTo = "" }) {
    // create comment info section DOM Element
    let divElement = createDOMElement(`<div class="comment-message gray">
        <span class="bold blue">${replyingTo}</span> ${content}
    </div>`);

    // CASE: function used to generate comment message section for a comment replying to another comment
    if (replyingTo != "") {
        divElement.firstElementChild.classList.add("reply-to");
    }

    // return the Element
    return divElement;
}


/**
 * Generate comment block section element 
 * this section consists of the comment-info section 
 * and the comment-message section.
 * 
 * @param {object} commentInformation - Object contains the information about comment. 
 * @returns {HTMLElement} The generated comment block section element.
 */
function generateCommentBlockSection(commentInformation) {
    // create comment block div container
    let divElement = createDOMElement(`<div class="comment-block"></div>`);

    // add Comment Info Section to the Comment block
    divElement.appendChild(generateCommentInfoSection(commentInformation));

    // add Comment Message Section to the Comment block
    divElement.appendChild(generateCommentMessageSection(commentInformation));

    // return the Element
    return divElement;
}


/**
 * Generate comment section element.
 * a comment section consists of a "comment score section"
 * and a "comment block section".
 * 
 * @param {object} commentInformation - Object contains the information about comment.
 * @returns {HTMLElement} The generated comment section element.
 */
function generateCommentSection(commentInformation) {
    // create Comment section div Element
    let divElement = createDOMElement(`<div class="comment"></div>`);

    // add the comment score section
    divElement.appendChild(generateCommentScoreSection(commentInformation));

    // add the comment block section
    divElement.appendChild(generateCommentBlockSection(commentInformation));

    // return the Element
    return divElement;

}


/**
 * Generate reply container section element.
 * every comment section should have a reply container 
 * where replies to the comment will be rendered
 * a comment with no replies would have no reply container YET.
 * 
 * 
 *  @returns {HTMLElement} The generated reply container section element.
 */
function generateReplyContainerSection() {
    // create reply container section DOM Element
    let divElement = createDOMElement(`<div class="reply-container">
        <div class="reply-vertical-line"></div>
        <div class="comment-replies"></div>
    </div>`);

    // return the Element
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
 * This function is an Event Handler for the Edit button 
 * it replaces the "comment message section" with an "edit section"
 * which instead consist of a textarea element and and update button
 * 
 * we also added a feature, such that whilst we are is editing 
 * if click outside the editing box, it would automatically be updated
 * 
 * @param {HTMLElement} editButton - The Edit button section element.
 */
function handleEditButton(editButton) {

    // comment section of edit button
    let commentSection = greatGrandFather(editButton);

    // comment message section element 
    let commentMessageSection = commentSection.querySelector(".comment-message");
    if (!commentMessageSection) return;

    // message
    let message = commentMessageSection.querySelector("span").nextSibling.textContent.trim();

    // replying to
    let replyingTo = commentMessageSection.querySelector("span").textContent.trim();

    // comment area section element (textarea element)
    let commentArea = createDOMElement(`<div><textarea style="width: 100%" class="comment-area page-font-styles clickable" placeholder="Add a comment..."></textarea>
    <button style="margin-left:77%; margin-top:0.6em;" class="comment-update-button page-font-styles clickable">UPDATE</button></div>`);

    commentArea.querySelector("textarea").value = message.replace(/\n\s+/g, " ");

    // Event handler for the update button
    let updateButton = commentArea.querySelector(".comment-update-button");
    updateButton.addEventListener('click', () => {
        handleUpdateButton(updateButton, replyingTo);
    });

    // replace the comment message section with the edit section
    commentMessageSection.parentNode.replaceChild(commentArea, commentMessageSection);

    // Updates edit if we click outside the edit box
    const handleClick = (event) => {
        // Element that trigger the click event
        let targetElement = event.target;

        if (targetElement.parentElement == editButton) {
            // Make the edit button unclickable
            editButton.classList.remove("clickable");
            return;
        }

        if (!commentArea.contains(targetElement)) {
            handleUpdateButton(updateButton, replyingTo);
            document.querySelector("body").removeEventListener('click', handleClick);
            editButton.classList.add("clickable");
        }
    }

    document.querySelector("body").addEventListener('click', handleClick);

}


/**
 * This function is an Event Handler for the "update button" in the "edit section"
 * it generate a new "comment message section" based on the new content
 * and replaces the "edit section"
 * 
 * @param {HTMLElement} updateButton - The update button element.
 * @param {string} replyingTo - the recipient username of the comment
 */
function handleUpdateButton(updateButton, replyingTo) {
    // get the edited message
    let editedMessage = updateButton.previousElementSibling.value;
    if (editedMessage == "") greatGrandFather(updateButton).remove();

    // parent of update Button
    let commentArea = updateButton.parentNode;

    // generate Comment Message Section for edited message
    let commentMessage = generateCommentMessageSection({ content: editedMessage, replyingTo });

    // replacing the edit section
    commentArea.parentNode.replaceChild(commentMessage, commentArea);
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
            // AND the click area is outside the reply comment section
            if ((replyCommentSection.querySelector("textarea").value == "") && (!replyCommentSection.contains(targetElement))) {

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


        /**
         * Because this replyCommentSection is dynamically generated by javascript
         * we have to add the event listener for the send button of the replyCommentSection
         * right here, right now 
         */
        const handleSendButton = (event) => {

            // return; if textarea element is empty
            if (replyCommentSection.querySelector("textarea").value === "") return;

            // generate comment information from the reply comment section
            // an object with attributes that describe the comment
            let commentInformation = generateCommentInformation(replyCommentSection);

            // add the "replyingTo" attribute to the commentInformation
            commentInformation["replyingTo"] = GGFather.querySelector(".comment-name").textContent;

            // use comment information to create a comment section element
            let commentSection = generateCommentSection(commentInformation);

            // Event handler for the edit button
            let editButton = commentSection.querySelector(".edit-button");
            editButton.addEventListener('click', () => {
                handleEditButton(editButton);
            });


            // generate a reply container if none exist EXCEPT if reply comment section is already in a reply container
            if (replyCommentSection.matches('.reply-container *')) {
                // comment section place after the comment
                insertAfterMe(commentSection, replyCommentSection.previousElementSibling);
            }
            else if (!replyCommentSection.nextElementSibling.classList.contains("reply-container")) {
                // insert reply container
                insertAfterMe(generateReplyContainerSection(), replyCommentSection);

                // comment section placed in reply container
                replyCommentSection.nextElementSibling.querySelector(".comment-replies").appendChild(commentSection);
            }

            // remove reply comment section
            replyCommentSection.remove();

            // Make the reply button clickable back
            if (!replyButton.classList.contains("clickable")) {
                replyButton.classList.add("clickable");
            }

        };

        // Add the click handler to the body element
        document.querySelector("body").addEventListener('click', handleClick);

        // Add click handler to the send button of the reply comment section
        replyCommentSection.querySelector(".comment-send-button").addEventListener('click', handleSendButton);

    })
})


/**
 * Set the Event Handler of the Send button
 */
document.querySelectorAll(".comment-send-button").forEach((CommentSendButton) => {
    CommentSendButton.addEventListener('click', (event) => {
        // "send button" parent element (reply comment section element)
        let replyCommentSection = CommentSendButton.parentNode;

        // return; if textarea element is empty
        if (replyCommentSection.querySelector("textarea").value === "") return;

        // generate comment information from the reply comment section
        let commentInformation = generateCommentInformation(replyCommentSection);

        // create a comment section element from comment information
        let commentSection = generateCommentSection(commentInformation);

        // replace the reply comment section with the comment section
        replyCommentSection.parentNode.replaceChild(commentSection, replyCommentSection);
    })

});


/**
 * Set the Evenet Handler of the Edit button
 *
 */
document.querySelectorAll(".edit-button").forEach((editButton) => {
    editButton.addEventListener('click', () => {
        handleEditButton(editButton);
    })
});



