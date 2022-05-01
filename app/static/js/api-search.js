let searchSubmit = document.getElementById("search-submit");
let ul = document.getElementById("results");
let li;
let a;
let baseUrl = "https://api.spoonacular.com";
let apiKey = "babb07a4fe7544289890cab2b47dd2e4";
searchSubmit.addEventListener("click", (e) => {
  e.preventDefault();
  ul.innerHTML = "";
  fetch(`${baseUrl}/recipes/complexSearch?query=${searchSubmit.previousElementSibling.value}&apiKey=${apiKey}`)
      .then(response => response.json())
      .then(response => {
        response.results.forEach((element) => {
          let id = element.id;
          fetch(`${baseUrl}/recipes/${id}/information?includeNutrition=false&apiKey=${apiKey}`)
              .then(response => response.json())
              .then(response => {
                a = document.createElement("a");
                a.href = response.sourceUrl;
                a.textContent = element.title;
                a.target = "_blank"
                li = document.createElement("li");
                li.appendChild(a);
                ul.appendChild(li);
              });
        });
      });
});
