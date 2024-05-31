const posts_url = "https://jsonplaceholder.typicode.com/posts";
const main_container = document.getElementById("main");

fetch("https://jsonplaceholder.typicode.com/posts/")
  .then((response) => response.json())
  .then((posts) => renderPosts(posts));

function renderPosts(posts) {
  for (let i = 0; i < posts.length; i++) {
    main_container.innerHTML += `<div class="post">
        <h2> ${posts[i].id}. ${posts[i].title}</h2>
        <p>${posts[i].body}</p>
    </div>`;
  }
}
