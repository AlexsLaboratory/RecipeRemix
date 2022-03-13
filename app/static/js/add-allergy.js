const addMoreBtn = document.getElementById("add-more");
const removeEmptyBtn = document.getElementById("remove-empty");
const totalNewForms = document.getElementById("id_form-TOTAL_FORMS");
addMoreBtn.addEventListener("click", (e) => {
  const currentAllergyForm = document.querySelectorAll(".allergy-form");
  const formCopyTarget = document.getElementById("allergy-form-list");
  const cloneEmptyFormEl = document.getElementById("empty-form").cloneNode(true);
  cloneEmptyFormEl.setAttribute("class", "allergy-form");
  cloneEmptyFormEl.removeAttribute("id");
  const regex = new RegExp("__prefix__", "g");
  cloneEmptyFormEl.innerHTML = cloneEmptyFormEl.innerHTML.replace(regex, totalNewForms.value);
  totalNewForms.value = `${parseInt(totalNewForms.value) + 1}`
  formCopyTarget.append(cloneEmptyFormEl)
});

removeEmptyBtn.addEventListener("click", (e) => {
  totalNewForms.value = `${parseInt(totalNewForms.value) - 1}`
  const allergyFormList = document.getElementById("allergy-form-list");
  if (allergyFormList.lastElementChild.querySelector("input[type='text']").value !== "") return;
  allergyFormList.removeChild(allergyFormList.lastChild);
})
