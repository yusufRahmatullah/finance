function initForm() {
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

  submitWallet(name, amount);
}

function submitWallet(name, amount) {
  var url = `/wallets/add?name=${name}&amount=${amount}`

  fetch(url)
  .then(resp => resp.json())
  .then(data => {
    if (data) {
      window.location.replace('/wallets');
    } else {
      M.toast({html: 'Failed to create wallet'})
    }
  })
  .catch(err => {
    console.error("Failed create wallet. " + err);
  })
}
