function initForm() {
}

function submitBudget(name, amount) {
  var url = `/budgets/add?name=${name}&amount=${amount}`

  fetch(url)
  .then(resp => resp.json())
  .then(data => {
    if (data) {
      window.location.replace('/budgets');
    } else {
      M.toast({html: 'Failed to create budget'})
    }
  })
  .catch(err => {
    console.error("Failed create budget. " + err);
  })
}

function submitForm() {
  var form = document.forms['form'];
  var name = form['name'].value;
  var amount = parseInt(form['amount'].value) || 0;

  if (!name) {
    M.toast({html: 'Name is required'})
    return;
  }

  if (amount <= 0) {
    M.toast({html: 'Amount should be positive'})
    return;
  }

  submitBudget(name, amount);
}
