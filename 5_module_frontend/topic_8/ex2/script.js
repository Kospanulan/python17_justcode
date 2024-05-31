const posts_url = "https://jsonplaceholder.typicode.com/posts";
const main_container = document.getElementById("main");

// fetch(posts_url")
// .then((response) => response.json())
// .then((posts) => renderPosts(posts));
async function fetchData() {
  const response = await fetch(posts_url);
  const data = await response.json();

  renderPosts(data);
}

function renderPosts(posts) {
  // for (let i = 0; i < posts.length; i++) {
  //   main_container.innerHTML += `<div class="post">
  //       <h2> ${posts[i].id}. ${posts[i].title}</h2>
  //       <p>${posts[i].body}</p>
  //   </div>`;
  // }

  // posts.forEach((post) => {
  //   main_container.innerHTML += `<div class="post">
  //       <h2> ${post.id}. ${post.title}</h2>
  //       <p>${post.body}</p>
  //   </div>`;
  // });

  posts.forEach((post) => {
    div_element = document.createElement("div"); // <div></div>

    div_element.classList = ["post bg-dark text-light p-3 rounded m-3"];

    div_element.innerHTML = `
        <h2> ${post.id}. ${post.title}</h2>
        <p>${post.body}</p>`;

    main_container.appendChild(div_element);
  });
}

fetchData();
