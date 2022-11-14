const form = document.querySelector("form");
form.addEventListener("submit", event => {
	event.preventDefault();

	let queryText=document.querySelector("input").value;
	let content=document.querySelector("#content");

	fetch(form.action, { method: "post", body: new URLSearchParams(new FormData(form)) })
		.then(data => data.text())
		.then(messagesHTML => {
			content.innerHTML += messagesHTML;
			form.reset();
			document.querySelector(".message:last-child").scrollIntoView(true);
		});

});