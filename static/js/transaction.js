var transactionData = [];
var totalBudget = 0;

function generateTable() {
  var tableNode = q('#table-body');
  var ctn = '';
  var currentBudget = totalBudget;
  var form = document.forms['form'];
  var budget = q('#budget-name-options').value;

  tableNode.innerHTML = '';

  ctn += transactionView({
    date: '',
    budget: '',
    thing: '&lt;init&gt;',
    outcome: 0,
    income: totalBudget,
  }, 0, true);

  transactionData.forEach(trx => {
    if (budget == 'all' || budget == trx.budget) {
      ctn += transactionView(trx, currentBudget);
    }
    currentBudget = currentBudget + trx.income - trx.outcome;
  });
  appendNode(tableNode, ctn);
}

function getTransactions() {
  setPeriod();

  fetch('/transactions/get')
  .then(resp => resp.json())
  .then(data => {
    transactionData = data;
    generateTable();
  })
  .catch(err => {
    console.error("Failed get transactions. " + err);
  })
}

function initBudgetNames(names) {
  var node = q('#budget-name-options');
  var ctn = '';

  names.forEach(name => {
    var norm_name = humanizeName(name);
    ctn += `<option value="${name}">${norm_name}</option>`;
  });

  appendNode(node, ctn);
}

function initBudgets() {
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
}

function loadTransactions() {
  // to init budget name select
  initBudgets();

  // get total budgets first
  fetch('/budgets/total')
  .then(resp => resp.json())
  .then(data => {
    totalBudget = data.total;
    getTransactions();
  })
  .catch(err => {
    console.error("Failed load transactions. " + err);
  })
}

function transactionView(trx, currentBudget, bold) {
  var total = currentBudget + trx.income - trx.outcome;
  var tr_attr = '';
  if (bold) {
    tr_attr = 'class="bold"';
  }

  return `
  <tr ${tr_attr}>
    <td>${trx.date}</td>
    <td>${trx.budget}</td>
    <td>${trx.thing}</td>
    <td>${humanizeAmount(trx.income)}</td>
    <td>${humanizeAmount(trx.outcome)}</td>
    <td>${humanizeAmount(total)}</td>
  </tr> 
  `;
}
