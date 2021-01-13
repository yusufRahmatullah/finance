function generateTable(trxs, totalBudget) {
  var tableNode = q('#table-body');
  var ctn = '';
  var currentBudget = totalBudget;

  ctn += transactionView({
    date: '',
    budget: '',
    thing: '&lt;init&gt;',
    outcome: 0,
    income: totalBudget,
  }, 0, true);

  trxs.forEach(trx => {
    ctn += transactionView(trx, currentBudget);
    currentBudget = currentBudget + trx.income - trx.outcome;
  });
  appendNode(tableNode, ctn);
}

function getTransactions(totalBudget) {
  fetch('/transactions/get')
  .then(resp => resp.json())
  .then(data => {
    setPeriod();
    generateTable(data, totalBudget);
  })
  .catch(err => {
    console.error("Failed get transactions. " + err);
  })
}

function loadTransactions() {
  // get total budgets first
  fetch('/budgets/total')
  .then(resp => resp.json())
  .then(data => {
    getTransactions(data.total);
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
  `
}
