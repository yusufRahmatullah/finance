function initForm() {
  // get wallet names first
  fetch('/wallets/names')
  .then(resp => resp.json())
  .then(data => {
    initWalletNames(data);
    initMaterials();
  })
  .catch(err => {
    console.error("Failed load transactions. " + err);
  })
}

function initWalletNames(names) {
  var nodeFrom = q('#from-wallet-name-options');
  var nodeTo = q('#to-wallet-name-options');
  var ctn = '';

  names.forEach(name => {
    var norm_name = humanizeName(name);
    ctn += `<option value="${name}">${norm_name}</option>`;
  });

  appendNode(nodeFrom, ctn);
  appendNode(nodeTo, ctn);
}

function initMaterials() {
  // select
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems);

  // datepicker
  var elems = document.querySelectorAll('.datepicker');
  var instances = M.Datepicker.init(elems, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: true,
  });
}

function submitForm() {
  var form = document.forms['form'];
  var date = form['date'].value;
  var thing = form['thing'].value;
  var from = form['from'].value;
  var to = form['to'].value;
  var amount = parseInt(form['amount'].value) || 0;

  if (!thing) {
    M.toast({html: 'Thing is required'})
    return;
  }

  if (amount <= 0) {
    M.toast({html: 'Amount should be positive'})
    return;
  }

  submitMutation(date, thing, from, to, amount);
}

function submitMutation(date, thing, from, to, amount) {
  var url = `/mutations/add?date=${date}&thing=${thing}&from=${from}&to=${to}&amount=${amount}`;

  fetch(url)
  .then(resp => resp.json())
  .then(data => {
    if (!data) {
      M.toast({html: 'Failed to create mutation'})
    } else {
      window.location.replace('/mutations');
    }
  })
  .catch(err => {
    console.error("Failed create mutations. " + err);
  })
}
