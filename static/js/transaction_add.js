function initBudgetNames(names) {
  var node = q('#budget-name-options');
  var ctn = '';

  names.forEach(name => {
    var norm_name = normalizeName(name);
    ctn += `<option value="${name}">${norm_name}</option>`;
  });

  appendNode(node, ctn);
}

function initForm() {
  // get budget names first
  fetch('/budgets/names')
  .then(resp => resp.json())
  .then(data => {
    initBudgetNames(data);
    initMaterials();
  })
  .catch(err => {
    console.error("Failed load transactions. " + err);
  })
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

function normalizeName(name) {
  var tokens = name.split('_');
  var res = [];

  tokens.forEach(token => {
    var title = token[0].toUpperCase() + token.substr(1);
    res.push(title);
  });

  return res.join(' ')
}

function submitForm() {
  var form = document.forms['form'];
  var date = form['date'].value;
  var budgets = M.FormSelect.getInstance(form['budget']).getSelectedValues();
  var thing = form['thing'].value;
  var income = parseInt(form['income'].value) || 0;
  var outcome = parseInt(form['outcome'].value) || 0;

  if (!thing) {
    M.toast({html: 'Thing is required'})
    return;
  }

  if (income == 0 && outcome == 0) {
    M.toast({html: 'Income or Outcome should be positive'})
    return;
  }

  submitTransaction(date, budgets, thing, income, outcome)
}

function submitTransaction(date, budgets, thing, income, outcome) {
  var url = `/transactions/add-split?date=${date}&thing=${thing}&income=${income}&outcome=${outcome}`;

  budgets.forEach(b => {
    url += `&budgets[]=${b}`;
  });

  fetch(url)
  .then(resp => resp.json())
  .then(data => {
    if (data.length == 0) {
      M.toast({html: 'Failed to create transaction'})
    } else {
      window.location.replace('/transactions');
    }
  })
  .catch(err => {
    console.error("Failed get transactions. " + err);
  })
}
