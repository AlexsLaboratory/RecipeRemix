const addMoreBtn = document.getElementById("add-more");
const removeEmptyBtn = document.getElementById("remove-empty");
const totalNewForms = document.getElementById("id_form-TOTAL_FORMS");
addMoreBtn.addEventListener("click", (e) => {
  const currentAllergyForm = document.querySelectorAll(".allergy-form");
  const formCopyTarget = document.getElementById("allergy-form-list");
  const cloneEmptyFormEl = document.getElementById("empty-form").cloneNode(true);
  const currentAllergyFormCount = currentAllergyForm.length;
  cloneEmptyFormEl.setAttribute("class", "allergy-form");
  cloneEmptyFormEl.removeAttribute("id");
  const regex = new RegExp("__prefix__", "g");
  cloneEmptyFormEl.innerHTML = cloneEmptyFormEl.innerHTML.replace(regex, currentAllergyFormCount);
  totalNewForms.value = `${currentAllergyFormCount + 1}`;
  formCopyTarget.append(cloneEmptyFormEl)
});

removeEmptyBtn.addEventListener("click", (e) => {
  const currentAllergyForm = document.querySelectorAll(".allergy-form");
  const currentAllergyFormCount = currentAllergyForm.length;
  totalNewForms.setAttribute("value", `${currentAllergyFormCount - 1}`)
  const allergyFormList = document.getElementById("allergy-form-list");
  if (allergyFormList.lastElementChild.querySelector("input[type='text']").value !== "") return;
  allergyFormList.removeChild(allergyFormList.lastChild);
})
